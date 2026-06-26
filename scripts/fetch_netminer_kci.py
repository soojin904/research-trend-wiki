"""
KCI에서 'netminer' 관련 논문을 수집하고 raw/netminer/ 에 .md로 저장한다.
저장된 파일은 fetch_netminer.py --sync-only 로 citations.xlsx 에 합산된다.

사용법:
  python fetch_netminer_kci.py
  python fetch_netminer_kci.py --from-date 20200101 --to-date 20261231
  python fetch_netminer_kci.py --dry-run
"""

import argparse
import re
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

WIKI_DIR = Path(__file__).parent.parent
NM_RAW_DIR = WIKI_DIR / "raw" / "netminer"
KEY_PATH = Path("D:/soojin/.claude/config/kci_key.txt")

BASE_URL = "https://open.kci.go.kr/po/openapi/openApiSearch.kci"
DISPLAY_COUNT = 100


def load_api_key() -> str:
    return KEY_PATH.read_text(encoding="utf-8").strip()


def build_url(api_key: str, page: int, from_date: str = None, to_date: str = None) -> str:
    url = (
        f"{BASE_URL}?apiCode=articleSearch"
        f"&key={api_key}"
        f"&abs=netminer"
        f"&displayCount={DISPLAY_COUNT}"
        f"&page={page}"
    )
    if from_date:
        url += f"&regDateFrom={from_date}"
    if to_date:
        url += f"&regDateTo={to_date}"
    return url


def fetch_page(url: str) -> ET.Element:
    req = urllib.request.Request(url, headers={"User-Agent": "wiki-fetcher/1.0 (mailto:netminer@cyram.com)"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return ET.fromstring(resp.read().decode("utf-8"))


def text(el: ET.Element, path: str, default: str = "") -> str:
    found = el.find(path)
    return (found.text or "").strip() if found is not None else default


def parse_records(root: ET.Element) -> list[dict]:
    records = []
    for rec in root.findall(".//record"):
        journal = text(rec, "journalInfo/journal-name")
        publisher = text(rec, "journalInfo/publisher-name")
        pub_year = text(rec, "journalInfo/pub-year")
        pub_mon = text(rec, "journalInfo/pub-mon")
        volume = text(rec, "journalInfo/volume")
        issue = text(rec, "journalInfo/issue")

        # 제목: 원문 우선, 없으면 영문
        title_ko = ""
        title_en = ""
        for t in rec.findall(".//article-title"):
            lang = t.get("lang", "")
            val = (t.text or "").strip()
            if lang == "original" and val:
                title_ko = val
            elif lang in ("english", "foreign") and val and not title_en:
                title_en = val
        title = title_ko or title_en

        # 저자
        authors = []
        for a in rec.findall(".//author"):
            name_en = a.get("english", "")
            name_ko = (a.text or "").split("(")[0].strip()
            authors.append(name_en if name_en else name_ko)

        # 초록
        abstract_ko = ""
        abstract_en = ""
        for ab in rec.findall(".//abstract"):
            lang = ab.get("lang", "")
            val = (ab.text or "").strip()
            if lang == "original" and val:
                abstract_ko = val
            elif lang == "english" and val and not abstract_en:
                abstract_en = val

        article_id = rec.find(".//articleInfo")
        article_id_str = article_id.get("article-id", "") if article_id is not None else ""

        doi = text(rec, ".//doi")
        url_val = text(rec, ".//url")
        fpage = text(rec, ".//fpage")
        lpage = text(rec, ".//lpage")
        pages = f"{fpage}-{lpage}" if fpage and lpage else fpage

        # 인용 수
        cc = rec.find(".//citation-count")
        cite_kci = int(cc.get("kci", 0)) if cc is not None else 0
        cite_wos = int(cc.get("wos", 0)) if cc is not None else 0

        records.append({
            "title": title,
            "title_ko": title_ko,
            "title_en": title_en,
            "authors": authors,
            "journal": journal,
            "publisher": publisher,
            "year": pub_year,
            "pub_mon": pub_mon,
            "volume": volume,
            "issue": issue,
            "pages": pages,
            "doi": doi,
            "url": url_val,
            "abstract_ko": abstract_ko,
            "abstract_en": abstract_en,
            "article_id": article_id_str,
            "cite_kci": cite_kci,
            "cite_wos": cite_wos,
        })
    return records


def safe_filename(title: str, year: str, article_id: str) -> str:
    id_slug = re.sub(r"[^a-zA-Z0-9]", "_", article_id)[:20] if article_id else "noid"
    title_slug = re.sub(r"[^\w\s]", "", title or "").strip()
    title_slug = "_".join(title_slug.split()[:5])[:25]
    return f"kci_{year}_{title_slug}_{id_slug}.md"


def record_to_markdown(r: dict) -> str:
    authors_repr = ", ".join(repr(a) for a in r["authors"])
    doi_url = r["doi"] if r["doi"].startswith("http") else f"https://doi.org/{r['doi']}" if r["doi"] else ""

    lines = [
        "---",
        f'title: "{r["title_ko"] or r["title"]}"',
        f'title_en: "{r["title_en"]}"',
        f"authors: [{authors_repr}]",
        f"year: {r['year']}",
        f'venue: "{r["journal"]}"',
        f'publisher: "{r["publisher"]}"',
        f'volume: "{r["volume"]}"',
        f'issue: "{r["issue"]}"',
        f'pages: "{r["pages"]}"',
        f'doi: "{doi_url}"',
        f'kci_id: "{r["article_id"]}"',
        f'url: "{r["url"]}"',
        f'cite_kci: {r["cite_kci"]}',
        f'cite_wos: {r["cite_wos"]}',
        "source: kci-netminer",
        "---",
        "",
        f"# {r['title']}",
        "",
        f"**저자**: {'; '.join(r['authors'])}",
        f"**출처**: {r['journal']}" + (f", Vol.{r['volume']}" if r["volume"] else "") + (f" No.{r['issue']}" if r["issue"] else "") + (f", pp.{r['pages']}" if r["pages"] else ""),
        f"**발행**: {r['year']}.{r['pub_mon']}",
        f"**DOI**: {doi_url}",
        f"**KCI**: {r['url']}",
        "",
    ]

    if r["abstract_ko"]:
        lines += ["## 초록 (원문)", "", r["abstract_ko"], ""]
    if r["abstract_en"]:
        lines += ["## Abstract", "", r["abstract_en"], ""]

    lines += ["## 메모", "", ""]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="KCI NetMiner 논문 수집")
    parser.add_argument("--from-date", metavar="YYYYMMDD", help="수집 시작일 (예: 20200101)")
    parser.add_argument("--to-date", metavar="YYYYMMDD", help="수집 종료일 (예: 20261231)")
    parser.add_argument("--dry-run", action="store_true", help="저장 없이 결과만 출력")
    args = parser.parse_args()

    api_key = load_api_key()
    NM_RAW_DIR.mkdir(parents=True, exist_ok=True)

    print("\n=== KCI 'netminer' 검색 ===")

    # 1페이지로 total 파악
    url = build_url(api_key, page=1, from_date=args.from_date, to_date=args.to_date)
    print(f"URL: {url}\n")
    root = fetch_page(url)
    total = int(text(root, ".//result/total") or "0")
    print(f"총 {total}건")

    all_records = parse_records(root)
    total_pages = (total + DISPLAY_COUNT - 1) // DISPLAY_COUNT

    for page in range(2, total_pages + 1):
        time.sleep(0.5)
        url = build_url(api_key, page=page, from_date=args.from_date, to_date=args.to_date)
        print(f"  page {page}/{total_pages}: {url[:80]}...")
        try:
            root = fetch_page(url)
            all_records.extend(parse_records(root))
        except Exception as e:
            print(f"  ERROR: {e}")
            break

    print(f"\n파싱 완료: {len(all_records)}건")

    saved, skipped = 0, 0
    for r in all_records:
        fname = safe_filename(r["title"], r["year"], r["article_id"])
        fpath = NM_RAW_DIR / fname

        if fpath.exists():
            skipped += 1
            continue

        if args.dry_run:
            print(f"  [dry] {fname}")
        else:
            fpath.write_text(record_to_markdown(r), encoding="utf-8")
            print(f"  [saved] {fname}")
        saved += 1

    print(f"\n저장: {saved}건 / 스킵(기존): {skipped}건")
    if saved and not args.dry_run:
        print("\n다음 단계: python fetch_netminer.py --sync-only")


if __name__ == "__main__":
    main()
