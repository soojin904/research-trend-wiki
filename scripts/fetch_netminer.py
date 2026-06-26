"""
NetMiner 관련 논문을 수집하고 nm-reference/citations.xlsx 를 업데이트한다.

1. OpenAlex에서 'netminer' 키워드 논문 수집 → raw/netminer/*.md 저장
2. raw/netminer/ 의 .md(OpenAlex) + .pdf(수동) 를 읽어 citations.xlsx 업데이트

사용법:
  python fetch_netminer.py                    # 수집 + 싱크
  python fetch_netminer.py --sync-only        # 싱크만 (수집 건너뜀)
  python fetch_netminer.py --dry-run          # 저장 없이 결과 출력
  python fetch_netminer.py --from-date 2020-01-01 --to-date 2026-12-31
"""

import argparse
import json
import re
import time
import urllib.request
from difflib import SequenceMatcher
from pathlib import Path

import openpyxl
import yaml

try:
    import fitz  # PyMuPDF
    _PYMUPDF = True
except ImportError:
    _PYMUPDF = False

try:
    import anthropic as _anthropic
    _ANTHROPIC = True
except ImportError:
    _ANTHROPIC = False

WIKI_DIR = Path(__file__).parent.parent
NM_RAW_DIR = WIKI_DIR / "raw" / "netminer"
CITATIONS_PATH = Path("D:/soojin/03_marketing/netminer_info/nm-reference/citations.xlsx")

BASE_URL = "https://api.openalex.org/works"
USER_AGENT = "wiki-fetcher/1.0 (mailto:netminer@cyram.com)"
MAX_RESULTS = 500

COLUMNS = [
    "title", "authors", "journal", "publisher", "year", "doi",
    "Web of Science Core Collection",
    "초록", "openalex_id", "kci_id",
    "cited_by_count", "cite_kci", "cite_wos", "fwci", "인용합",
    "구분",
]


# ─────────────────────────────────────────
# OpenAlex fetch
# ─────────────────────────────────────────

def reconstruct_abstract(inverted_index: dict) -> str:
    if not inverted_index:
        return ""
    positions = [(pos, word) for word, locs in inverted_index.items() for pos in locs]
    positions.sort()
    return " ".join(w for _, w in positions)


def safe_filename(title: str, year: int, doi: str) -> str:
    doi_slug = re.sub(r"[^a-zA-Z0-9]", "_", doi.split("/")[-1])[:25] if doi else "nodoi"
    title_slug = re.sub(r"[^a-zA-Z0-9 ]", "", title or "").strip()
    title_slug = "_".join(title_slug.split()[:5])[:25]
    return f"netminer_{year}_{title_slug}_{doi_slug}.md"


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

    source = (paper.get("primary_location") or {}).get("source") or {}
    venue = source.get("display_name", "") or ""
    publisher = source.get("host_organization_name", "") or ""

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
            pages += f"-{biblio['last_page']}"

    openalex_id = paper.get("id", "")
    cited_by_count = paper.get("cited_by_count", 0) or 0
    fwci = paper.get("fwci", "")

    lines = [
        "---",
        f'title: "{title}"',
        f"authors: [{', '.join(repr(a) for a in authors)}]",
        f"year: {year}",
        f"publication_date: {pub_date}",
        f'venue: "{venue}"',
        f'publisher: "{publisher}"',
        f'volume: "{volume}"',
        f'issue: "{issue}"',
        f'pages: "{pages}"',
        f'doi: "{doi_url}"',
        f'openalex_id: "{openalex_id}"',
        f"cited_by_count: {cited_by_count}",
        f"fwci: {fwci if fwci != '' else 'null'}",
        f"tags: [{', '.join(repr(t) for t in topics[:5])}]",
        f"keywords: [{', '.join(repr(k) for k in keywords[:8])}]",
        "source: openalex-netminer",
        "---",
        "",
        f"# {title}",
        "",
        f"**저자**: {'; '.join(authors)}",
        f"**출처**: {venue}"
        + (f", Vol.{volume}" if volume else "")
        + (f" No.{issue}" if issue else "")
        + (f", pp.{pages}" if pages else ""),
        f"**발행일**: {pub_date}",
        f"**DOI**: {doi_url}",
        "",
        "## 초록",
        "",
        abstract if abstract else "(초록 없음)",
        "",
        "## 메모",
        "",
        "",
    ]
    return "\n".join(lines)


def fetch_all(url: str) -> list:
    results = []
    page = 1
    while True:
        paged_url = url + f"&page={page}" if page > 1 else url
        print(f"  page {page}: {paged_url[:90]}...")
        req = urllib.request.Request(paged_url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode())
        except Exception as e:
            print(f"  ERROR: {e}")
            break
        batch = data.get("results", [])
        results.extend(batch)
        meta = data.get("meta", {})
        total = min(meta.get("count", 0), MAX_RESULTS)
        per_page = meta.get("per_page", 25)
        print(f"  {len(results)}/{total} 건 수신")
        if len(results) >= total or len(batch) < per_page:
            break
        page += 1
        time.sleep(0.3)
    return results[:MAX_RESULTS]


def build_netminer_url(from_date: str = None, to_date: str = None, per_page: int = 100) -> str:
    filters = []
    if from_date:
        filters.append(f"from_publication_date:{from_date}")
    if to_date:
        filters.append(f"to_publication_date:{to_date}")
    url = f"{BASE_URL}?search=netminer&sort=cited_by_count:desc&per_page={per_page}"
    if filters:
        url += "&filter=" + ",".join(filters)
    return url


# ─────────────────────────────────────────
# Citations sync
# ─────────────────────────────────────────

def normalize_doi(doi: str) -> str:
    m = re.search(r"10\.\d{4,}", (doi or ""))
    if m:
        return doi[m.start():].lower().strip()
    return (doi or "").lower().strip()


def normalize_title(title: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", "", (title or "").lower())).strip()


_KO_RE = re.compile(r"[가-힣]")


def is_korean(text: str) -> bool:
    return bool(_KO_RE.search(text or ""))


def parse_md_entry(md_path: Path) -> dict:
    text = md_path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}
    try:
        fm = yaml.safe_load(match.group(1))
    except Exception:
        return {}
    if not isinstance(fm, dict):
        return {}

    authors = fm.get("authors", [])
    if isinstance(authors, list):
        author_str = "; ".join(authors)
    else:
        author_str = str(authors)

    title = str(fm.get("title", ""))
    title_en = str(fm.get("title_en", ""))

    # 초록: frontmatter 없으면 본문에서 추출
    abstract = str(fm.get("abstract", ""))
    if not abstract:
        body = text[match.end():]
        ab = re.search(r"## (?:초록[^\n]*|Abstract[^\n]*)\n\n(.*?)(?=\n\n##|\Z)", body, re.DOTALL)
        if ab:
            abstract = ab.group(1).strip()

    def _num(key):
        v = fm.get(key, None)
        if v is None or v == "null" or v == "":
            return None
        try:
            return float(v)
        except (ValueError, TypeError):
            return None

    return {
        "title": title,
        "title_en": title_en,
        "authors": author_str,
        "journal": str(fm.get("venue", "")),
        "publisher": str(fm.get("publisher", "")),
        "year": fm.get("year", ""),
        "doi": normalize_doi(str(fm.get("doi", ""))),
        "abstract": abstract,
        "openalex_id": str(fm.get("openalex_id", "")),
        "kci_id": str(fm.get("kci_id", "")),
        "cited_by_count": _num("cited_by_count"),
        "cite_kci": _num("cite_kci"),
        "cite_wos": _num("cite_wos"),
        "fwci": _num("fwci"),
    }


_INVALID_TITLE = re.compile(r"^<[0-9A-Fa-f]+>$")
_GENERIC_TITLES = {"untitled", "untitled document", "document", ""}


def _is_valid_title(t: str) -> bool:
    t = t.strip()
    if not t:
        return False
    if _INVALID_TITLE.match(t):
        return False
    if t.lower() in _GENERIC_TITLES:
        return False
    return True


def parse_pdf_entry(pdf_path: Path) -> dict:
    title, author_str = "", ""
    if _PYMUPDF:
        try:
            doc = fitz.open(str(pdf_path))
            meta = doc.metadata or {}
            title = (meta.get("title") or "").strip()
            author_str = (meta.get("author") or "").strip()
            doc.close()
        except Exception:
            pass
    if not _is_valid_title(title):
        title = pdf_path.stem

    return {
        "title": title,
        "title_en": "",
        "authors": author_str,
        "journal": "",
        "publisher": "",
        "year": "",
        "doi": "",
        "abstract": "",
        "openalex_id": "",
        "kci_id": "",
        "cited_by_count": None,
        "cite_kci": None,
        "cite_wos": None,
        "fwci": None,
    }


def collect_all_entries() -> list:
    entries = []
    if not NM_RAW_DIR.exists():
        print(f"  [경고] raw/netminer/ 없음: {NM_RAW_DIR}")
        return entries

    md_files = sorted(NM_RAW_DIR.glob("*.md"))
    pdf_files = sorted(NM_RAW_DIR.glob("*.pdf"))
    print(f"  .md (OpenAlex/KCI): {len(md_files)}건 / .pdf (수동): {len(pdf_files)}건")

    for f in md_files:
        entry = parse_md_entry(f)
        if entry.get("title"):
            entries.append(entry)

    for f in pdf_files:
        entry = parse_pdf_entry(f)
        if entry.get("title"):
            entries.append(entry)

    return entries


# ─────────────────────────────────────────
# Merge logic
# ─────────────────────────────────────────

def _best_title(a: dict, b: dict) -> str:
    """영문 제목 우선, 없으면 더 긴 제목 반환."""
    candidates = [
        a.get("title_en", ""), b.get("title_en", ""),
        a.get("title", ""),    b.get("title", ""),
    ]
    # 한국어 아닌 것 중 가장 긴 것
    en = [c for c in candidates if c and not is_korean(c)]
    if en:
        return max(en, key=len)
    return max((c for c in candidates if c), key=len, default="")


def _merge_authors(a: str, b: str) -> str:
    """두 저자 문자열을 합쳐 중복 제거."""
    parts = set()
    for s in (a, b):
        for p in re.split(r"[;,]", s or ""):
            p = p.strip()
            if p:
                parts.add(p)
    return "; ".join(sorted(parts))


def _max_num(a, b):
    """둘 다 None이면 None, 아니면 최대값."""
    if a is None and b is None:
        return None
    return max(v for v in (a, b) if v is not None)


def merge_two(a: dict, b: dict) -> dict:
    return {
        "title":          _best_title(a, b),
        "title_en":       a.get("title_en") or b.get("title_en", ""),
        "authors":        _merge_authors(a.get("authors", ""), b.get("authors", "")),
        "journal":        a.get("journal") or b.get("journal", ""),
        "publisher":      a.get("publisher") or b.get("publisher", ""),
        "year":           a.get("year") or b.get("year", ""),
        "doi":            a.get("doi") or b.get("doi", ""),
        "wos":            a.get("wos") or b.get("wos", ""),
        "abstract":       a.get("abstract") or b.get("abstract", ""),
        "openalex_id":    a.get("openalex_id") or b.get("openalex_id", ""),
        "kci_id":         a.get("kci_id") or b.get("kci_id", ""),
        "cited_by_count": _max_num(a.get("cited_by_count"), b.get("cited_by_count")),
        "cite_kci":       _max_num(a.get("cite_kci"), b.get("cite_kci")),
        "cite_wos":       _max_num(a.get("cite_wos"), b.get("cite_wos")),
        "fwci":           _max_num(a.get("fwci"), b.get("fwci")),
    }


def _match_title(entry: dict, translate_fn=None) -> str:
    """매칭에 쓸 정규화된 영문 제목 반환. 한국어만 있으면 번역."""
    t = entry.get("title_en", "") or entry.get("title", "")
    if is_korean(t) and translate_fn:
        t = translate_fn(t)
    return normalize_title(t)


def _titles_similar(a: str, b: str, threshold: float = 0.88) -> bool:
    if not a or not b:
        return False
    return SequenceMatcher(None, a, b).ratio() >= threshold


def _journals_compatible(a: str, b: str) -> bool:
    """둘 다 있을 때만 비교; 하나라도 없으면 True."""
    na, nb = normalize_title(a), normalize_title(b)
    if not na or not nb:
        return True
    return _titles_similar(na, nb, threshold=0.75)


def merge_entries(entries: list, translate_fn=None) -> list:
    """
    DOI 일치 → 병합.
    DOI 없으면 제목(한/영 번역 포함) + 저널 일치 → 병합.
    """
    canonical: list[dict] = []

    for entry in entries:
        doi = normalize_doi(entry.get("doi", ""))
        matched_idx = None

        # 1. DOI 매칭
        if doi:
            for i, c in enumerate(canonical):
                if normalize_doi(c.get("doi", "")) == doi:
                    matched_idx = i
                    break

        # 2. 제목 + 저널 매칭
        if matched_idx is None:
            t = _match_title(entry, translate_fn)
            j = entry.get("journal", "")
            for i, c in enumerate(canonical):
                ct = _match_title(c, translate_fn)
                if _titles_similar(t, ct) and _journals_compatible(j, c.get("journal", "")):
                    matched_idx = i
                    break

        if matched_idx is not None:
            canonical[matched_idx] = merge_two(canonical[matched_idx], entry)
        else:
            canonical.append(dict(entry))

    return canonical


def make_translate_fn():
    """Claude API로 한→영 번역 함수 생성. 캐시 포함."""
    if not _ANTHROPIC:
        return None
    import os
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        return None
    client = _anthropic.Anthropic(api_key=api_key)
    cache: dict[str, str] = {}

    def translate(title_ko: str) -> str:
        if title_ko in cache:
            return cache[title_ko]
        try:
            resp = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=200,
                messages=[{
                    "role": "user",
                    "content": f"Translate this Korean academic paper title to English. Return only the translation:\n{title_ko}"
                }]
            )
            result = resp.content[0].text.strip()
        except Exception:
            result = title_ko
        cache[title_ko] = result
        return result

    return translate


def sync_citations(dry_run: bool = False, translate: bool = False) -> int:
    print(f"\n=== citations.xlsx 싱크 ===")
    print(f"  경로: {CITATIONS_PATH}")

    raw_entries = collect_all_entries()
    print(f"  수집 항목 합계: {raw_entries and len(raw_entries)}건 (병합 전)")

    translate_fn = make_translate_fn() if translate else None
    if translate and not translate_fn:
        print("  [경고] ANTHROPIC_API_KEY 미설정 — 번역 없이 진행")

    entries = merge_entries(raw_entries, translate_fn)
    print(f"  병합 후: {len(entries)}건 (중복 {len(raw_entries) - len(entries)}건 합산)")

    CITATIONS_PATH.parent.mkdir(parents=True, exist_ok=True)

    if not CITATIONS_PATH.exists():
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(COLUMNS)
    else:
        wb = openpyxl.load_workbook(CITATIONS_PATH)
        ws = wb.active

    headers = [cell.value for cell in ws[1]]
    doi_idx = headers.index("doi") if "doi" in headers else -1
    title_idx = headers.index("title") if "title" in headers else -1

    existing_keys: set[str] = set()
    for row in ws.iter_rows(min_row=2, values_only=True):
        if doi_idx >= 0 and row[doi_idx]:
            existing_keys.add(normalize_doi(str(row[doi_idx])))
        if title_idx >= 0 and row[title_idx]:
            existing_keys.add(normalize_title(str(row[title_idx])))

    added, skipped = 0, 0
    for entry in entries:
        doi_key = normalize_doi(entry.get("doi", ""))
        title_key = normalize_title(entry.get("title", ""))

        is_dup = (doi_key and doi_key in existing_keys) or (
            not doi_key and title_key and title_key in existing_keys
        )
        if is_dup:
            skipped += 1
            continue

        cbc  = entry.get("cited_by_count")
        ckci = entry.get("cite_kci")
        cwos = entry.get("cite_wos")
        fwci = entry.get("fwci")
        citation_sum = sum(v for v in (cbc, ckci, cwos, fwci) if v is not None) or None

        row_data = [
            entry.get("title", ""),
            entry.get("authors", ""),
            entry.get("journal", ""),
            entry.get("publisher", ""),
            entry.get("year", ""),
            entry.get("doi", ""),
            entry.get("wos", ""),
            entry.get("abstract", ""),
            entry.get("openalex_id", ""),
            entry.get("kci_id", ""),
            cbc,
            ckci,
            cwos,
            fwci,
            citation_sum,
            "검증필요",
        ]

        if dry_run:
            print(f"  [dry] {entry.get('title', '')[:70]}")
        else:
            ws.append(row_data)
            if doi_key:
                existing_keys.add(doi_key)
            if title_key:
                existing_keys.add(title_key)
        added += 1

    if not dry_run and added > 0:
        wb.save(CITATIONS_PATH)
        print(f"  저장 완료: {CITATIONS_PATH}")

    print(f"  신규 추가: {added}건 / 스킵(기존): {skipped}건")
    return added


# ─────────────────────────────────────────
# Main
# ─────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="NetMiner 논문 수집 및 citations.xlsx 업데이트")
    parser.add_argument("--from-date", metavar="YYYY-MM-DD", help="수집 시작일")
    parser.add_argument("--to-date", metavar="YYYY-MM-DD", help="수집 종료일")
    parser.add_argument("--dry-run", action="store_true", help="저장 없이 결과만 출력")
    parser.add_argument("--sync-only", action="store_true", help="OpenAlex 수집 건너뛰고 싱크만 실행")
    parser.add_argument("--translate", action="store_true", help="한국어 제목을 Claude API로 번역해 중복 감지 (ANTHROPIC_API_KEY 필요)")
    args = parser.parse_args()

    NM_RAW_DIR.mkdir(parents=True, exist_ok=True)

    if not args.sync_only:
        url = build_netminer_url(args.from_date, args.to_date)
        print(f"\n=== OpenAlex 'netminer' 검색 ===")
        print(f"URL: {url}\n")
        papers = fetch_all(url)
        print(f"\n총 {len(papers)}건 수신")

        saved, skipped = 0, 0
        for paper in papers:
            title = paper.get("title") or paper.get("display_name", "untitled")
            year = paper.get("publication_year", 0)
            doi = (paper.get("doi") or "").replace("https://doi.org/", "")
            fname = safe_filename(title, year, doi)
            fpath = NM_RAW_DIR / fname

            if fpath.exists():
                skipped += 1
                continue

            md = paper_to_markdown(paper)
            if args.dry_run:
                print(f"  [dry] {fname}")
            else:
                fpath.write_text(md, encoding="utf-8")
                print(f"  [saved] {fname}")
            saved += 1

        print(f"\nOpenAlex 저장: {saved}건 / 스킵(기존): {skipped}건")

    sync_citations(dry_run=args.dry_run, translate=args.translate)


if __name__ == "__main__":
    main()
