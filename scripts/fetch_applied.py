"""
키워드 검색으로 OpenAlex 논문을 수집해 raw/applied/ 에 저장한다.

수집 쿼리 2종:
  1. "social network" 검색 (SNA 전문 학술지 제외)
  2. "text analysis" 검색 + topic 필터 (t10028 OR t13910 OR t10664 중 1개 이상, SNA 전문 학술지 제외)

사용법:
  python fetch_applied.py
  python fetch_applied.py --from-date 2026-05-01 --to-date 2026-05-31
  python fetch_applied.py --from-date 2022-01-01 --to-date 2022-12-31 --max-per-query 200
  python fetch_applied.py --dry-run
"""

import argparse
import json
import re
import time
import urllib.request
from pathlib import Path

WIKI_DIR = Path(__file__).parent.parent
APPLIED_RAW_DIR = WIKI_DIR / "raw" / "applied"

# text analysis 검색 시 적용할 topic ID (OR 조건)
TEXT_ANALYSIS_TOPIC_IDS = ["t10028", "t13910", "t10664"]

BASE_URL = "https://api.openalex.org/works"
USER_AGENT = "wiki-fetcher/1.0 (mailto:netminer@cyram.com)"

# fetch_openalex.py 가 수집하는 전문 SNA 학술지 ISSN — social network 쿼리에서 제외
# 2331-8422 : arXiv (OpenAlex 등록 ISSN)
EXCLUDE_ISSNS = ["0378-8733", "2816-4245", "2050-1250", "2331-8422"]

# venue display_name 에 포함된 경우 제외할 키워드 (소문자 비교)
# arXiv는 ISSN 필터 외에 "arxiv (cornell university)" 표기도 별도 존재
EXCLUDE_VENUE_KEYWORDS = ["arxiv"]


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
    doi_slug = re.sub(r"[^a-zA-Z0-9]", "_", doi.split("/")[-1])[:25] if doi else "nodoi"
    title_slug = re.sub(r"[^a-zA-Z0-9 ]", "", title or "").strip()
    title_slug = "_".join(title_slug.split()[:5])[:25]
    return f"applied_{year}_{title_slug}_{doi_slug}.md"


def openalex_id_short(paper: dict) -> str:
    return paper.get("id", "").replace("https://openalex.org/", "")


MAX_PER_QUERY = 500


def fetch_all(url: str) -> list:
    results = []
    page = 1
    while True:
        paged_url = url + f"&page={page}" if page > 1 else url
        print(f"  page {page}: {paged_url[:90]}...")
        req = urllib.request.Request(paged_url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=90) as resp:
                data = json.loads(resp.read().decode())
        except Exception as e:
            print(f"  ERROR: {e}")
            break
        batch = data.get("results", [])
        results.extend(batch)
        meta = data.get("meta", {})
        total = min(meta.get("count", 0), MAX_PER_QUERY)
        per_page = meta.get("per_page", 25)
        print(f"  {len(results)}/{total} 건 수신")
        if len(results) >= total or len(batch) < per_page:
            break
        page += 1
        time.sleep(0.3)
    return results[:MAX_PER_QUERY]


def paper_to_markdown(paper: dict, query_keyword: str) -> str:
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
        (paper.get("primary_location") or {})
        .get("source") or {}
    ).get("display_name", "") or ""

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

    oa_status = paper.get("open_access", {}).get("oa_status", "")
    openalex_id = paper.get("id", "")

    lines = [
        "---",
        f'title: "{title}"',
        f"authors: [{', '.join(repr(a) for a in authors)}]",
        f"year: {year}",
        f"publication_date: {pub_date}",
        f'venue: "{venue}"',
        f'volume: "{volume}"',
        f'issue: "{issue}"',
        f'pages: "{pages}"',
        f'doi: "{doi_url}"',
        f'oa_status: "{oa_status}"',
        f'openalex_id: "{openalex_id}"',
        f'query_keyword: "{query_keyword}"',
        f"tags: [{', '.join(repr(t) for t in topics[:5])}]",
        f"keywords: [{', '.join(repr(k) for k in keywords[:8])}]",
        "source: openalex-keyword",
        "---",
        "",
        f"# {title}",
        "",
        f"**저자**: {author_str}",
        f"**출처**: {venue}" + (f", Vol.{volume}" if volume else "") + (f" No.{issue}" if issue else "") + (f", pp.{pages}" if pages else ""),
        f"**발행일**: {pub_date}",
        f"**DOI**: {doi_url}",
        f"**수집 키워드**: {query_keyword}",
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


def build_social_network_url(from_date: str, to_date: str, per_page: int = 100) -> str:
    # SNA 전문 학술지(Social Networks·Network Science·Connections)는
    # fetch_openalex.py 에서 이미 수집하므로 여기서 제외
    exclude_filter = "".join(
        f",primary_location.source.issn:!{issn}" for issn in EXCLUDE_ISSNS
    )
    return (
        f"{BASE_URL}"
        f'?search=("social+network")'
        f"&filter=from_publication_date:{from_date},to_publication_date:{to_date}{exclude_filter}"
        f",type:article|book|book-chapter|preprint|review"
        f"&sort=publication_date:desc"
        f"&per_page={per_page}"
    )


def build_text_analysis_url(from_date: str, to_date: str, per_page: int = 100) -> str:
    topic_filter = "|".join(TEXT_ANALYSIS_TOPIC_IDS)
    exclude_filter = "".join(
        f",primary_location.source.issn:!{issn}" for issn in EXCLUDE_ISSNS
    )
    return (
        f"{BASE_URL}"
        f'?search=("text+analysis")'
        f"&filter=from_publication_date:{from_date},to_publication_date:{to_date}"
        f",topics.id:{topic_filter}{exclude_filter}"
        f",type:article|book|book-chapter|preprint|review"
        f"&sort=publication_date:desc"
        f"&per_page={per_page}"
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--from-date", default="2025-12-01", metavar="YYYY-MM-DD",
                        help="수집 시작일 (기본: 2026-01-01)")
    parser.add_argument("--to-date", default="2025-12-31", metavar="YYYY-MM-DD",
                        help="수집 종료일 (기본: 2026-12-31)")
    parser.add_argument("--dry-run", action="store_true",
                        help="저장 없이 결과만 출력")
    args = parser.parse_args()

    APPLIED_RAW_DIR.mkdir(parents=True, exist_ok=True)

    queries = [
        ("social network", build_social_network_url(args.from_date, args.to_date)),
        ("text analysis", build_text_analysis_url(args.from_date, args.to_date)),
    ]

    all_papers: dict[str, tuple] = {}  # openalex_id → (paper, keyword)

    for keyword, url in queries:
        print(f"\n=== 쿼리: \"{keyword}\" ===")
        print(f"URL: {url}\n")
        papers = fetch_all(url)
        for p in papers:
            oid = openalex_id_short(p)
            if oid not in all_papers:
                all_papers[oid] = (p, keyword)
            # 중복 시 먼저 수집된 것 유지 (social network 우선)

    print(f"\n중복 제거 후 총 {len(all_papers)}건")

    # venue 이름 기반 후처리 필터 (arXiv 등 ISSN 필터를 우회하는 경우 대응)
    filtered_out = []
    for oid in list(all_papers.keys()):
        paper, _ = all_papers[oid]
        venue = (
            (paper.get("primary_location") or {})
            .get("source") or {}
        ).get("display_name", "") or ""
        if any(kw in venue.lower() for kw in EXCLUDE_VENUE_KEYWORDS):
            filtered_out.append(venue)
            del all_papers[oid]
    if filtered_out:
        print(f"venue 필터로 제외: {len(filtered_out)}건 ({', '.join(set(filtered_out))})")
    print(f"venue 필터 후 총 {len(all_papers)}건\n")

    saved, skipped_existing, dry_list = [], [], []
    for oid, (paper, keyword) in all_papers.items():
        title = paper.get("title") or paper.get("display_name", "untitled")
        year = paper.get("publication_year", 0)
        doi = (paper.get("doi") or "").replace("https://doi.org/", "")
        fname = safe_filename(title, year, doi)
        fpath = APPLIED_RAW_DIR / fname

        if fpath.exists():
            skipped_existing.append(fname)
            print(f"  [skip] {fname}")
            continue

        md = paper_to_markdown(paper, keyword)
        if args.dry_run:
            dry_list.append(fname)
            print(f"  [dry] {fname}")
        else:
            fpath.write_text(md, encoding="utf-8")
            saved.append(fname)
            print(f"  [saved] {fname} ({keyword})")

    print(f"\n완료: 저장 {len(saved)}건, 스킵(기존) {len(skipped_existing)}건" +
          (f", dry {len(dry_list)}건" if args.dry_run else ""))
    if saved or dry_list:
        print("\n다음 단계: python batch_ingest.py 로 인제스트 실행")


if __name__ == "__main__":
    main()
