"""
1. citations.xlsx 헤더 업데이트
2. raw/netminer/*.md → research_metadata.xlsx 신규 행 추가
"""

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import openpyxl
import yaml

WIKI_DIR = Path(__file__).parent.parent
CITATIONS_PATH = WIKI_DIR / "nm-reference" / "citations.xlsx"
META_PATH = WIKI_DIR / "nm-reference" / "research_metadata.xlsx"
NM_RAW_DIR = WIKI_DIR / "raw" / "netminer"

CITATIONS_COLUMNS = [
    "title", "authors", "journal", "publisher", "year", "doi",
    "Web of Science Core Collection",
    "초록", "openalex_id", "kci_id",
    "cited_by_count", "cite_kci", "cite_wos", "fwci", "인용합",
    "구분",
]

META_COLS = {
    "출처": 1, "title": 2, "title_ko": 3, "authors": 4, "first_institution": 5,
    "journal": 6, "publisher": 7, "year": 8, "publication_date": 9, "month": 10,
    "volume": 11, "issue": 12, "fpage": 13, "lpage": 14, "category": 15,
    "type": 16, "language": 17, "is_oa": 18, "doi": 19, "url": 20,
    "abstract": 21, "article_id": 22, "openalex_id": 23,
    "cited_by_count": 24, "cite_kci": 25, "cite_wos": 26, "fwci": 27,
    "topics": 28, "keywords": 29,
    "활용": 30, "인용합": 31, "filename": 32,
    "analysis category": 33, "data": 34, "method": 35,
    "비고 작성": 36, "Web of Science Core Collection": 37,
}
MAX_COL = 37


def normalize_doi(doi: str) -> str:
    m = re.search(r"10\.\d{4,}", doi or "")
    if m:
        return doi[m.start():].lower().strip()
    return (doi or "").lower().strip()


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    end = text.find("---", 3)
    if end == -1:
        return {}
    try:
        return yaml.safe_load(text[3:end]) or {}
    except Exception:
        return {}


def get_abstract_from_body(text: str) -> str:
    end = text.find("---", 3)
    if end == -1:
        return ""
    body = text[end + 3:]
    for header in ["## 초록 (원문)\n", "## 초록\n", "## Abstract\n"]:
        idx = body.find(header)
        if idx != -1:
            start = idx + len(header)
            next_sec = body.find("\n##", start)
            chunk = body[start:next_sec].strip() if next_sec != -1 else body[start:].strip()
            if chunk:
                return chunk
    return ""


def load_md_papers() -> list[dict]:
    papers = []
    for fpath in sorted(NM_RAW_DIR.glob("*.md")):
        text = fpath.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if not fm:
            continue

        abstract = fm.get("abstract") or get_abstract_from_body(text)
        journal = fm.get("journal") or fm.get("venue") or ""
        doi_raw = fm.get("doi") or ""
        doi = normalize_doi(doi_raw)

        source = fm.get("source", "")
        if "kci" in source:
            origin = "KCI"
        elif "openalex" in source:
            origin = "OpenAlex"
        else:
            origin = "수동"

        topics = fm.get("tags") or fm.get("topics") or []
        if isinstance(topics, list):
            topics = ", ".join(str(t) for t in topics)
        keywords = fm.get("keywords") or []
        if isinstance(keywords, list):
            keywords = ", ".join(str(k) for k in keywords)

        pages = str(fm.get("pages") or "")
        fpage, lpage = "", ""
        if "-" in pages:
            parts = pages.split("-", 1)
            fpage, lpage = parts[0], parts[1]
        elif pages:
            fpage = pages

        cbc = fm.get("cited_by_count")
        ckci = fm.get("cite_kci")
        cwos = fm.get("cite_wos")
        cfwci = fm.get("fwci")

        def to_num(v):
            try:
                return float(v) if v is not None else None
            except (ValueError, TypeError):
                return None

        nums = [to_num(v) for v in (cbc, ckci, cwos, cfwci) if to_num(v) is not None]
        citation_sum = sum(nums) if nums else None

        authors = fm.get("authors") or []
        if isinstance(authors, list):
            authors = "; ".join(str(a) for a in authors)

        papers.append({
            "출처": origin,
            "title": fm.get("title") or "",
            "title_ko": fm.get("title_ko") or (fm.get("title") if origin == "KCI" else ""),
            "authors": authors,
            "journal": journal,
            "publisher": fm.get("publisher") or "",
            "year": fm.get("year") or "",
            "publication_date": fm.get("publication_date") or "",
            "volume": str(fm.get("volume") or ""),
            "issue": str(fm.get("issue") or ""),
            "fpage": fpage,
            "lpage": lpage,
            "doi": doi,
            "url": fm.get("url") or "",
            "abstract": abstract,
            "article_id": fm.get("kci_id") or fm.get("article_id") or "",
            "openalex_id": str(fm.get("openalex_id") or ""),
            "cited_by_count": to_num(cbc),
            "cite_kci": to_num(ckci),
            "cite_wos": to_num(cwos),
            "fwci": to_num(cfwci),
            "topics": topics,
            "keywords": keywords,
            "인용합": citation_sum,
            "filename": fpath.name,
        })
    return papers


# ── research_metadata.xlsx 신규 행 추가 ──────────────────────
print("=== research_metadata.xlsx 업데이트 ===")
wb_m = openpyxl.load_workbook(META_PATH)
ws_m = wb_m.worksheets[0]  # 1번 시트

# 마지막 실제 데이터 행 찾기 (빈 행 제외)
last_row = 1
for row in ws_m.iter_rows(min_row=2):
    if any(cell.value is not None for cell in row):
        last_row = row[0].row

existing_dois = set()
existing_titles = set()
for row in ws_m.iter_rows(min_row=2, max_row=last_row, values_only=True):
    doi_cell = row[META_COLS["doi"] - 1]
    title_cell = row[META_COLS["title"] - 1]
    if doi_cell:
        existing_dois.add(normalize_doi(str(doi_cell)))
    if title_cell:
        existing_titles.add(str(title_cell).strip().lower())

papers = load_md_papers()
print(f"  .md 파일 수: {len(papers)}건")

added = 0
skipped = 0
for p in papers:
    doi_norm = normalize_doi(p["doi"])
    title_norm = p["title"].strip().lower()

    if (doi_norm and doi_norm in existing_dois) or (title_norm and title_norm in existing_titles):
        print(f"  [skip] {p['title'][:60]}")
        skipped += 1
        continue

    new_row = [None] * MAX_COL
    for field, col_idx in META_COLS.items():
        val = p.get(field)
        if val is not None and val != "":
            new_row[col_idx - 1] = val

    # 빈 행 건너뛰고 마지막 데이터 다음에 삽입
    last_row += 1
    for col_idx, val in enumerate(new_row, 1):
        ws_m.cell(row=last_row, column=col_idx, value=val)
    if doi_norm:
        existing_dois.add(doi_norm)
    existing_titles.add(title_norm)
    print(f"  [added] {p['title'][:70]}")
    added += 1

wb_m.save(META_PATH)
print(f"\n완료: 추가 {added}건 / 스킵(기존) {skipped}건")
print(f"  저장: {META_PATH}")
