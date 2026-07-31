"""
OpenAlex에서 SNA 관련 저널 논문 서지를 가져와 raw/ 폴더에 마크다운으로 저장한다.
저장된 파일은 /wiki:ingest로 처리한다.

사용법:
  python fetch_openalex.py
  python fetch_openalex.py --url "https://api.openalex.org/works?..."
  python fetch_openalex.py --dry-run   # 저장 없이 결과만 출력
"""

import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

RAW_DIR = Path(__file__).parent.parent / "raw" / "sna"

DEFAULT_FROM = "2026-01-01"
DEFAULT_TO = "2026-12-31"
ISSN = "0378-8733|2816-4245|2050-1250"

DEFAULT_URL = (
    f"https://api.openalex.org/works"
    f"?filter=from_publication_date:{DEFAULT_FROM},to_publication_date:{DEFAULT_TO}"
    f",locations.source.issn:{ISSN}"
    f",type:article|book|book-chapter|preprint|review"
    f"&sort=publication_date:desc"
    f"&per_page=100"
)


def reconstruct_abstract(inverted_index: dict) -> str:
    if not inverted_index:
        return ""
    positions = []
    for word, locs in inverted_index.items():
        for pos in locs:
            positions.append((pos, word))
    positions.sort()
    return " ".join(w for _, w in positions)


def safe_filename(title: str, year: int, doi: str) -> str:
    # DOI 끝부분에서 고유 식별자 추출
    doi_slug = re.sub(r"[^a-zA-Z0-9]", "_", doi.split("/")[-1])[:30] if doi else "nodoi"
    title_slug = re.sub(r"[^a-zA-Z0-9 ]", "", title).strip()
    title_slug = "_".join(title_slug.split()[:6])
    return f"{year}_openalex_{title_slug}_{doi_slug}.md"


def fetch_all(base_url: str) -> list:
    results = []
    url = base_url
    page = 1
    while url:
        print(f"  fetching page {page}: {url[:80]}...")
        req = urllib.request.Request(url, headers={"User-Agent": "wiki-fetcher/1.0 (mailto:netminer@cyram.com)"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
        batch = data.get("results", [])
        results.extend(batch)
        meta = data.get("meta", {})
        total = meta.get("count", 0)
        per_page = meta.get("per_page", 100)
        fetched = len(results)
        print(f"  {fetched}/{total} 건 수신")
        # 다음 페이지 URL 구성
        if fetched < total and len(batch) == per_page:
            page += 1
            sep = "&" if "?" in base_url else "?"
            url = base_url + f"{sep}page={page}"
        else:
            url = None
    return results


def paper_to_markdown(paper: dict) -> str:
    title = paper.get("title") or paper.get("display_name", "")
    year = paper.get("publication_year", "")
    pub_date = paper.get("publication_date", "")
    doi = paper.get("doi", "") or ""
    doi_url = doi if doi.startswith("http") else f"https://doi.org/{doi}" if doi else ""

    authors = [
        a["author"]["display_name"]
        for a in paper.get("authorships", [])
        if a.get("author", {}).get("display_name")
    ]
    author_str = "; ".join(authors)

    venue = (
        paper.get("primary_location", {})
        .get("source", {})
        .get("display_name", "")
    )

    topics = [t["display_name"] for t in paper.get("topics", [])]
    keywords = [k["display_name"] for k in paper.get("keywords", [])]

    abstract = reconstruct_abstract(paper.get("abstract_inverted_index") or {})

    biblio = paper.get("biblio", {})
    volume = biblio.get("volume", "")
    issue = biblio.get("issue", "")
    pages = ""
    if biblio.get("first_page"):
        pages = biblio["first_page"]
        if biblio.get("last_page"):
            pages += f"–{biblio['last_page']}"

    oa = paper.get("open_access", {})
    oa_status = oa.get("oa_status", "")
    oa_url = oa.get("oa_url", "") or doi_url

    openalex_id = paper.get("id", "")

    lines = [
        "---",
        f"title: \"{title}\"",
        f"authors: [{', '.join(repr(a) for a in authors)}]",
        f"year: {year}",
        f"publication_date: {pub_date}",
        f"venue: \"{venue}\"",
        f"volume: \"{volume}\"",
        f"issue: \"{issue}\"",
        f"pages: \"{pages}\"",
        f"doi: \"{doi_url}\"",
        f"oa_status: \"{oa_status}\"",
        f"oa_url: \"{oa_url}\"",
        f"openalex_id: \"{openalex_id}\"",
        f"tags: [{', '.join(repr(t) for t in topics[:5])}]",
        f"keywords: [{', '.join(repr(k) for k in keywords[:8])}]",
        "source: openalex",
        "---",
        "",
        f"# {title}",
        "",
        f"**저자**: {author_str}",
        f"**출처**: {venue}, Vol.{volume}" + (f" No.{issue}" if issue else "") + (f", pp.{pages}" if pages else ""),
        f"**발행일**: {pub_date}",
        f"**DOI**: {doi_url}",
        "",
        "## 초록",
        "",
        abstract if abstract else "(초록 없음)",
        "",
        "## 키워드",
        "",
        ", ".join(keywords) if keywords else "(없음)",
        "",
        "## 주제 분류 (OpenAlex Topics)",
        "",
    ]
    for t in paper.get("topics", []):
        lines.append(f"- {t['display_name']} (score: {t['score']:.3f})")
    lines += ["", "## 메모", "", ""]

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default=None, help="OpenAlex API URL (직접 지정 시 --from/--to 무시)")
    parser.add_argument("--from-date", default=DEFAULT_FROM, metavar="YYYY-MM-DD", help=f"수집 시작일 (기본: {DEFAULT_FROM})")
    parser.add_argument("--to-date", default=DEFAULT_TO, metavar="YYYY-MM-DD", help=f"수집 종료일 (기본: {DEFAULT_TO})")
    parser.add_argument("--dry-run", action="store_true", help="저장 없이 결과만 출력")
    args = parser.parse_args()

    if args.url is None:
        args.url = (
            f"https://api.openalex.org/works"
            f"?filter=from_publication_date:{args.from_date},to_publication_date:{args.to_date}"
            f",locations.source.issn:{ISSN}"
            f",type:article|book|book-chapter|preprint|review"
            f"&sort=publication_date:desc"
            f"&per_page=100"
        )

    print(f"OpenAlex 논문 수집 시작")
    print(f"URL: {args.url}...")

    papers = fetch_all(args.url)
    print(f"\n총 {len(papers)}건 수신\n")

    saved, skipped = [], []
    for paper in papers:
        title = paper.get("title") or paper.get("display_name", "untitled")
        year = paper.get("publication_year", 0)
        doi = (paper.get("doi") or "").replace("https://doi.org/", "")
        fname = safe_filename(title, year, doi)
        fpath = RAW_DIR / fname

        if fpath.exists():
            skipped.append(fname)
            print(f"  [skip] {fname}")
            continue

        md = paper_to_markdown(paper)
        if args.dry_run:
            print(f"  [dry-run] {fname}")
            print(md[:300])
            print("  ...")
        else:
            fpath.write_text(md, encoding="utf-8")
            saved.append(fname)
            print(f"  [saved] {fname}")

    print(f"\n완료: 저장 {len(saved)}건, 스킵(기존) {len(skipped)}건")
    if saved:
        print("\n저장된 파일:")
        for f in saved:
            print(f"  raw/{f}")
        print("\n다음 단계: /wiki:ingest 로 위키에 통합하세요.")


if __name__ == "__main__":
    main()
