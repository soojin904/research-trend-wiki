"""
raw/의 미등록 OpenAlex 파일을 일괄 인제스트한다.

- 관련도 점수가 높은 논문 → pages/papers/ 개별 페이지 (한국어 번역 포함)
- 나머지 → pages/papers/catalog_YYYY.md 연도별 목록

사용법:
  python batch_ingest.py [--threshold 3] [--dry-run] [--no-translate]
"""

import argparse
import os
import re
import time
from pathlib import Path

try:
    import anthropic as _anthropic
    _ANTHROPIC_AVAILABLE = True
except ImportError:
    _ANTHROPIC_AVAILABLE = False

WIKI_DIR = Path(__file__).parent.parent
RAW_DIR = WIKI_DIR / "raw"
APPLIED_DIR = RAW_DIR / "applied"
PAGES_DIR = WIKI_DIR / "pages" / "papers"
APPLIED_PAGES_DIR = PAGES_DIR / "applied"
INDEX_PATH = WIKI_DIR / "index.md"

# 이미 인제스트된 논문 raw 파일명 (stem)
ALREADY_INGESTED = {
    "2026_openalex_Causal_inference_for_intervention_spillover_in_j_socnet_2026_04_017",
    "2026_openalex_Mapping_the_relational_ecology_of_multiorganizational_j_socnet_2026_04_005",
    "2026_openalex_Social_influences_in_network_and_households_j_socnet_2026_04_001",
    "2026_openalex_From_hidden_populations_to_social_structure_j_socnet_2026_04_002",
    "2026_openalex_Making_the_peers_subjective_wellbeing_visible_j_socnet_2026_03_002",
    "2026_openalex_Estimating_peer_influence_in_multilayer_networks_j_socnet_2026_03_003",
    "2026_openalex_The_sociability_space_Putting_social_networks_j_socnet_2026_03_005",
    "2026_openalex_Network_threats_to_causal_inference_Variations_j_socnet_2026_03_004",
    "2026_openalex_What_accompanies_companionship_Reassessing_personal_networks_j_socnet_2026_03_001",
    "2026_openalex_A_hybrid_mixed_methods_design_for_j_socnet_2026_02_005",
    "2026_openalex_Understanding_the_personal_networks_of_people_j_socnet_2026_02_003",
    "2026_openalex_From_survey_data_to_social_multiplex_j_socnet_2026_01_005",
    "2026_openalex_Who_benefits_most_Interventioninduced_changes_in_j_socnet_2026_01_006",
    "2026_openalex_The_influence_of_social_network_on_j_socnet_2025_12_008",
}

# 고관련도 키워드 (점수 +2)
HIGH_KEYWORDS = [
    "topic model", "lda", "text mining", "text analysis", "semantic network",
    "natural language", "nlp", "sentiment", "bert", "word embedding",
    "machine learning", "deep learning", "neural network", "gnn", "graph neural",
    "mixed method", "bibliometric", "systematic review", "keyword network",
    "two-mode network", "bipartite", "affiliation network",
    "netminer", "gephi", "ucinet", "software", "tool",
]

# 중간 관련도 키워드 (점수 +1)
MED_KEYWORDS = [
    "exponential random graph", "ergm", "saom", "stochastic actor",
    "community detect", "centrality", "betweenness", "closeness",
    "multilayer", "multiplex", "temporal network", "dynamic network",
    "diffusion", "contagion", "influence", "peer effect",
    "ego", "egocentric", "personal network",
    "visualization", "data collection", "survey",
    "method", "model", "algorithm", "estimation",
    "content analysis", "discourse", "frame",
]

# 스킵 패턴
SKIP_PATTERNS = ["editorial_board", "corrigendum"]


def translate_paper_ko(meta: dict) -> dict:
    """Claude API로 논문 제목·초록을 한국어로 번역/요약. 실패 시 빈 dict 반환."""
    if not _ANTHROPIC_AVAILABLE:
        return {}
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        return {}

    title = meta["title"]
    abstract = meta["abstract"] or "(초록 없음)"
    keywords = ", ".join(meta["keywords"][:8])

    prompt = f"""다음 학술 논문의 정보를 읽고 아래 형식에 맞게 한국어로 번역/요약해줘.

제목(원문): {title}
키워드: {keywords}
초록: {abstract}

출력 형식 (각 항목을 정확히 이 레이블로 시작해):
제목(한글): <논문 제목의 한국어 번역>
연구질문: <이 논문이 답하려는 핵심 질문 1–2문장>
방법론: <사용된 주요 방법론 2–4개, 각 항목은 "- " 로 시작>
주요결과: <핵심 발견 2–4개, 각 항목은 "- " 로 시작>

번역 시 학술 용어는 한국어 표준 용어를 사용하고, 모호하면 영문 병기. 불필요한 설명 없이 형식만 출력."""

    try:
        client = _anthropic.Anthropic(api_key=api_key)
        msg = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=600,
            messages=[{"role": "user", "content": prompt}],
        )
        raw = msg.content[0].text.strip()
    except Exception as e:
        print(f"  [번역 오류] {e}")
        return {}

    # 섹션별 파싱: "레이블:" 이후 다음 "레이블:" 이전까지 수집
    sections = {"제목(한글)": "", "연구질문": "", "방법론": "", "주요결과": ""}
    labels = list(sections.keys())
    current = None
    buf = []

    for line in raw.splitlines():
        matched = None
        for label in labels:
            if line.startswith(f"{label}:"):
                matched = label
                break
        if matched:
            if current and buf:
                sections[current] = "\n".join(buf).strip()
                buf = []
            current = matched
            rest = line.split(":", 1)[1].strip()
            if rest:
                buf.append(rest)
        elif current:
            buf.append(line)

    if current and buf:
        sections[current] = "\n".join(buf).strip()

    return {
        "title_ko": sections["제목(한글)"],
        "research_question": sections["연구질문"],
        "methods_ko": sections["방법론"],
        "results_ko": sections["주요결과"],
    }


def score_paper(text: str) -> int:
    t = text.lower()
    score = 0
    for kw in HIGH_KEYWORDS:
        if kw in t:
            score += 2
    for kw in MED_KEYWORDS:
        if kw in t:
            score += 1
    return score


def parse_metadata(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    def get_field(field):
        m = re.search(rf'^{field}:\s*"?([^"\n]+)"?', text, re.MULTILINE)
        return m.group(1).strip() if m else ""
    def get_list_field(field):
        m = re.search(rf'^{field}:\s*\[([^\]]*)\]', text, re.MULTILINE)
        if not m:
            return []
        items = re.findall(r"'([^']+)'", m.group(1))
        return items

    title = get_field("title")
    year = get_field("year")
    authors_raw = get_list_field("authors")
    venue = get_field("venue")
    doi = get_field("doi")
    tags = get_list_field("tags")
    keywords = get_list_field("keywords")
    pub_date = get_field("publication_date")
    volume = get_field("volume")
    pages = get_field("pages")

    # 초록 추출
    abstract = ""
    m = re.search(r'## 초록\n\n(.+?)(?=\n\n##|\Z)', text, re.DOTALL)
    if m:
        abstract = m.group(1).strip()
        if abstract == "(초록 없음)":
            abstract = ""

    first_author = authors_raw[0].split()[-1] if authors_raw else "unknown"

    return {
        "title": title,
        "year": year,
        "pub_date": pub_date,
        "authors": authors_raw,
        "first_author": first_author,
        "venue": venue,
        "volume": volume,
        "pages": pages,
        "doi": doi,
        "tags": tags,
        "keywords": keywords,
        "abstract": abstract,
        "raw_text": text,
        "source_file": path.name,
    }


def make_page_slug(meta: dict) -> str:
    year = meta["year"]
    author = re.sub(r"[^a-zA-Z]", "", meta["first_author"]).lower()[:10]
    title_words = re.sub(r"[^a-zA-Z ]", "", meta["title"]).split()
    title_slug = "_".join(w.lower() for w in title_words[:4] if len(w) > 2)[:30]
    return f"{year}_{author}_{title_slug}"


def make_individual_page(meta: dict, ko: dict | None = None) -> str:
    authors_str = "; ".join(meta["authors"])
    kw_str = ", ".join(meta["keywords"][:8])

    # 연관 페이지 추천
    related = []
    t = (meta["title"] + " " + " ".join(meta["keywords"])).lower()
    if any(k in t for k in ["topic model", "lda", "text"]):
        related.append("[[pages/methods/topic_modeling|토픽모델링]]")
    if any(k in t for k in ["semantic", "keyword network"]):
        related.append("[[pages/methods/semantic_network_analysis|의미연결망]]")
    if any(k in t for k in ["centrality", "community"]):
        related.append("[[pages/methods/centrality|Centrality]]")
    if any(k in t for k in ["multilayer", "multiplex"]):
        related.append("[[pages/concepts/multilayer_network|다층 네트워크]]")
    if any(k in t for k in ["egocentric", "personal network", "ego"]):
        related.append("[[pages/concepts/personal_network|퍼스널 네트워크]]")
    if any(k in t for k in ["causal", "rct", "intervention", "spillover"]):
        related.append("[[pages/concepts/causal_inference_networks|인과 추론과 네트워크]]")
    if any(k in t for k in ["mixed method", "bibliometric", "systematic review"]):
        related.append("[[pages/methods/mixed_methods|복합 방법론]]")
    if not related:
        related.append("[[pages/concepts/social_network_analysis|SNA]]")

    abstract_section = meta["abstract"] if meta["abstract"] else "(초록 비공개)"

    # 한국어 번역 섹션
    if ko and ko.get("title_ko"):
        title_ko_line = f"\n**제목(한글)**: {ko['title_ko']}"
        ko_section = f"""
## 한국어 요약

**연구질문**: {ko.get('research_question', '')}

**방법론**:
{ko.get('methods_ko', '')}

**주요 결과**:
{ko.get('results_ko', '')}
"""
    else:
        title_ko_line = ""
        ko_section = ""

    return f"""---
title: "{meta['title']}"
authors: [{', '.join(repr(a) for a in meta['authors'])}]
year: {meta['year']}
venue: "{meta['venue']}"
tags: [{', '.join(repr(t) for t in meta['tags'][:4])}]
source: raw/{meta['source_file']}
---

# {meta['title']}{title_ko_line}

**저자**: {authors_str}
**출처**: {meta['venue']}, Vol.{meta['volume']}{', pp.' + meta['pages'] if meta['pages'] else ''}
**발행일**: {meta['pub_date']}
**DOI**: {meta['doi']}
{ko_section}
## 초록 (원문)

{abstract_section}

## 키워드

{kw_str}

## 위키 연관

{chr(10).join('- ' + r for r in related)}

## 메모

"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--threshold", type=int, default=3, help="개별 페이지 생성 관련도 임계값")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-translate", action="store_true", help="한국어 번역 API 호출 건너뜀")
    args = parser.parse_args()
    use_translate = not args.no_translate and _ANTHROPIC_AVAILABLE

    # 신규 파일 수집
    new_files = []
    for f in sorted(RAW_DIR.glob("*.md")):
        stem = f.stem
        if stem in ALREADY_INGESTED:
            continue
        if any(p in stem.lower() for p in SKIP_PATTERNS):
            continue
        new_files.append(f)

    print(f"신규 파일 {len(new_files)}개 발견\n")

    # 점수 계산 및 분류
    selected = []   # 개별 페이지
    catalog = {}    # {year: [meta, ...]}

    for f in new_files:
        meta = parse_metadata(f)
        score_text = " ".join([meta["title"]] + meta["keywords"] + meta["tags"] + [meta["abstract"]])
        score = score_paper(score_text)
        meta["score"] = score

        year = meta["year"] or "unknown"
        if score >= args.threshold:
            selected.append(meta)
        else:
            catalog.setdefault(year, []).append(meta)

    print(f"개별 페이지 대상: {len(selected)}편 (score >= {args.threshold})")
    print(f"카탈로그 대상: {sum(len(v) for v in catalog.values())}편\n")

    # 개별 페이지 생성
    PAGES_DIR.mkdir(parents=True, exist_ok=True)
    individual_created = []
    for meta in sorted(selected, key=lambda m: (m["year"], m["pub_date"])):
        slug = make_page_slug(meta)
        page_path = PAGES_DIR / f"{slug}.md"
        if page_path.exists():
            print(f"  [skip] {page_path.name}")
            continue
        ko = {}
        if use_translate and not args.dry_run:
            print(f"  [translate] {slug} ...")
            ko = translate_paper_ko(meta)
            time.sleep(0.3)  # API 호출 간 짧은 대기
        content = make_individual_page(meta, ko)
        if args.dry_run:
            print(f"  [dry] {page_path.name} (score={meta['score']})")
        else:
            page_path.write_text(content, encoding="utf-8")
            individual_created.append((slug, meta))
            print(f"  [page] {page_path.name} (score={meta['score']}, translated={'yes' if ko else 'no'})")

    # 연도별 카탈로그 생성
    catalog_created = []
    for year, papers in sorted(catalog.items()):
        cat_path = PAGES_DIR / f"catalog_{year}.md"
        # 기존 카탈로그가 있으면 합산
        existing_titles = set()
        existing_lines = []
        if cat_path.exists():
            existing_text = cat_path.read_text(encoding="utf-8")
            existing_lines = existing_text.splitlines()
            existing_titles = set(re.findall(r'\*\*(.+?)\*\*', existing_text))

        new_entries = []
        for meta in sorted(papers, key=lambda m: m["pub_date"]):
            if meta["title"] in existing_titles:
                continue
            kw = ", ".join(meta["keywords"][:5])
            tags = " ".join(f"#{t.lower().replace(' ', '-')}" for t in meta["tags"][:3])
            new_entries.append(
                f"- **{meta['title']}** — {meta['authors'][0] if meta['authors'] else '?'} 외 "
                f"({meta['pub_date']}) | {kw} {tags}"
            )

        if not new_entries:
            continue

        if not cat_path.exists():
            header = f"""---
title: "Social Networks 학술지 {year} — 논문 카탈로그"
tags: [catalog, social-networks-journal, {year}]
---

# Social Networks {year} — 논문 목록

관련도 기준 이하 논문 요약 목록. 상세 분석이 필요한 경우 raw/ 파일 참조.

## 논문 목록

"""
            content = header + "\n".join(new_entries) + "\n"
        else:
            # 기존 파일에 추가
            content = "\n".join(existing_lines) + "\n" + "\n".join(new_entries) + "\n"

        if args.dry_run:
            print(f"  [dry-catalog] catalog_{year}.md +{len(new_entries)}편")
        else:
            cat_path.write_text(content, encoding="utf-8")
            catalog_created.append((year, len(new_entries)))
            print(f"  [catalog] catalog_{year}.md +{len(new_entries)}편")

    print(f"\n완료: 개별 페이지 {len(individual_created)}개, 카탈로그 업데이트 {len(catalog_created)}건")
    return individual_created, catalog_created


def ingest_applied(use_translate: bool = True, threshold: int = 3, dry_run: bool = False):
    """raw/applied/ 파일을 점수 기반으로 분류.
    score >= threshold → pages/papers/applied/ 개별 페이지
    score < threshold  → pages/papers/applied/catalog_YYYY.md
    """
    if not APPLIED_DIR.exists() or not any(APPLIED_DIR.glob("*.md")):
        print("raw/applied/ 에 새 파일 없음 - 스킵")
        return [], []

    APPLIED_PAGES_DIR.mkdir(parents=True, exist_ok=True)

    selected = []
    catalog_map = {}  # {year: [meta, ...]}

    for f in sorted(APPLIED_DIR.glob("*.md")):
        meta = parse_metadata(f)
        meta["source_file"] = f"applied/{f.name}"
        score_text = " ".join([meta["title"]] + meta["keywords"] + meta["tags"] + [meta["abstract"]])
        score = score_paper(score_text)
        meta["score"] = score

        slug = make_page_slug(meta)
        page_path = APPLIED_PAGES_DIR / f"{slug}.md"
        if page_path.exists():
            print(f"  [skip] applied/{page_path.name}")
            continue

        year = meta["year"] or "unknown"
        if score >= threshold:
            selected.append(meta)
        else:
            catalog_map.setdefault(year, []).append(meta)

    total_catalog = sum(len(v) for v in catalog_map.values())
    print(f"\napplied: 개별 페이지 대상 {len(selected)}편 (score>={threshold}), 카탈로그 대상 {total_catalog}편\n")

    # 개별 페이지 생성
    individual_created = []
    for meta in sorted(selected, key=lambda m: (m["year"], m["pub_date"])):
        slug = make_page_slug(meta)
        page_path = APPLIED_PAGES_DIR / f"{slug}.md"
        ko = {}
        if use_translate and not dry_run and _ANTHROPIC_AVAILABLE:
            print(f"  [translate] {slug} ...")
            ko = translate_paper_ko(meta)
            time.sleep(0.3)
        content = make_individual_page(meta, ko)
        if dry_run:
            print(f"  [dry-applied] {page_path.name} (score={meta['score']})")
        else:
            page_path.write_text(content, encoding="utf-8")
            individual_created.append((slug, meta))
            print(f"  [applied-page] {page_path.name} (score={meta['score']}, translated={'yes' if ko else 'no'})")

    # 연도별 카탈로그 (pages/papers/applied/catalog_YYYY.md)
    catalog_created = []
    for year, papers in sorted(catalog_map.items()):
        cat_path = APPLIED_PAGES_DIR / f"catalog_{year}.md"
        existing_titles = set()
        existing_lines = []
        if cat_path.exists():
            existing_text = cat_path.read_text(encoding="utf-8")
            existing_lines = existing_text.splitlines()
            existing_titles = set(re.findall(r'\*\*(.+?)\*\*', existing_text))

        new_entries = []
        for meta in sorted(papers, key=lambda m: m["pub_date"]):
            if meta["title"] in existing_titles:
                continue
            kw = ", ".join(meta["keywords"][:5])
            tags = " ".join(f"#{t.lower().replace(' ', '-')}" for t in meta["tags"][:3])
            new_entries.append(
                f"- **{meta['title']}** — {meta['authors'][0] if meta['authors'] else '?'} 외 "
                f"({meta['pub_date']}) | {kw} {tags}"
            )

        if not new_entries:
            continue

        if not cat_path.exists():
            header = f"""---
title: "응용 분야 논문 {year} — 카탈로그"
tags: [catalog, applied, {year}]
---

# 응용 분야 논문 {year} — 목록

관련도 기준 이하 논문 요약 목록. 상세 분석이 필요한 경우 raw/applied/ 파일 참조.

## 논문 목록

"""
            content = header + "\n".join(new_entries) + "\n"
        else:
            content = "\n".join(existing_lines) + "\n" + "\n".join(new_entries) + "\n"

        if dry_run:
            print(f"  [dry-catalog] applied/catalog_{year}.md +{len(new_entries)}편")
        else:
            cat_path.write_text(content, encoding="utf-8")
            catalog_created.append((year, len(new_entries)))
            print(f"  [applied-catalog] catalog_{year}.md +{len(new_entries)}편")

    print(f"\napplied 완료: 개별 페이지 {len(individual_created)}개, 카탈로그 {len(catalog_created)}건")
    return individual_created, catalog_created


if __name__ == "__main__":
    import sys
    _no_translate = "--no-translate" in sys.argv
    _dry_run = "--dry-run" in sys.argv
    _threshold = 3
    for _arg in sys.argv:
        if _arg.startswith("--threshold="):
            _threshold = int(_arg.split("=")[1])
    _use_tr = not _no_translate and _ANTHROPIC_AVAILABLE
    individual_created, catalog_created = main()
    ingest_applied(use_translate=_use_tr, threshold=_threshold, dry_run=_dry_run)
