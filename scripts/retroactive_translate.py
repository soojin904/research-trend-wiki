"""
기존 pages/papers/*.md 페이지에 한국어 요약 섹션을 소급 추가한다.

- 이미 "## 한국어 요약" 섹션이 있는 파일은 건너뜀
- netminer/, applied/ 서브디렉토리 제외 (이미 한국어 작성됨)
- catalog_*.md 제외

사용법:
  python retroactive_translate.py [--dry-run] [--limit N] [--resume-from 파일명]
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
    print("ERROR: anthropic 패키지 없음. pip install anthropic 후 재실행.")
    exit(1)

WIKI_DIR = Path(__file__).parent.parent
PAGES_DIR = WIKI_DIR / "pages" / "papers"


def translate_paper_ko(title: str, abstract: str, keywords: str) -> dict:
    """Claude Haiku API로 논문 번역/요약. 실패 시 빈 dict 반환."""
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        print("  ERROR: ANTHROPIC_API_KEY 환경변수 없음")
        return {}

    prompt = f"""다음 학술 논문의 정보를 읽고 아래 형식에 맞게 한국어로 번역/요약해줘.

제목(원문): {title}
키워드: {keywords}
초록: {abstract or '(초록 없음)'}

출력 형식 (각 항목을 정확히 이 레이블로 시작해):
제목(한글): <논문 제목의 한국어 번역>
연구질문: <이 논문이 답하려는 핵심 질문 1-2문장>
방법론: <사용된 주요 방법론 2-4개, 각 항목은 "- " 로 시작>
주요결과: <핵심 발견 2-4개, 각 항목은 "- " 로 시작>

학술 용어는 한국어 표준 용어 사용, 모호하면 영문 병기. 불필요한 설명 없이 형식만 출력."""

    try:
        client = _anthropic.Anthropic(api_key=api_key)
        msg = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=600,
            messages=[{"role": "user", "content": prompt}],
        )
        raw = msg.content[0].text.strip()
    except Exception as e:
        print(f"  API 오류: {e}")
        return {}

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


def extract_from_page(text: str) -> dict:
    """기존 페이지에서 제목·초록·키워드 추출."""
    # frontmatter title
    m = re.search(r'^title:\s*"?([^"\n]+)"?', text, re.MULTILINE)
    title = m.group(1).strip() if m else ""

    # 초록 섹션 (구버전: "## 초록", 신버전: "## 초록 (원문)")
    m = re.search(r'## 초록.*?\n\n(.+?)(?=\n\n##|\Z)', text, re.DOTALL)
    abstract = m.group(1).strip() if m else ""
    if abstract in ("(초록 비공개)", "(초록 없음)"):
        abstract = ""

    # 키워드 섹션
    m = re.search(r'## 키워드\n\n(.+?)(?=\n\n##|\Z)', text, re.DOTALL)
    keywords = m.group(1).strip() if m else ""

    return {"title": title, "abstract": abstract, "keywords": keywords}


def patch_page(text: str, ko: dict) -> str:
    """기존 페이지 텍스트에 한국어 요약 섹션을 삽입하고 초록 섹션 이름을 변경."""
    if not ko.get("title_ko"):
        return text

    # 헤더 줄 (# 제목) 에 한글 제목 추가
    title_ko_suffix = f"\n**제목(한글)**: {ko['title_ko']}"

    ko_section = f"""
## 한국어 요약

**연구질문**: {ko.get('research_question', '')}

**방법론**:
{ko.get('methods_ko', '')}

**주요 결과**:
{ko.get('results_ko', '')}
"""

    # H1 줄에 한글 제목 추가 (이미 있으면 건너뜀)
    if "**제목(한글)**" not in text:
        text = re.sub(
            r'^(# .+)$',
            r'\1' + title_ko_suffix,
            text,
            count=1,
            flags=re.MULTILINE,
        )

    # DOI 줄 다음에 한국어 요약 삽입 (DOI 줄이 없으면 H1 바로 다음)
    if "\n\n## 초록" in text and "## 한국어 요약" not in text:
        text = text.replace("\n\n## 초록\n", ko_section + "\n## 초록 (원문)\n", 1)
    elif "\n\n## 초록 (원문)" not in text and "## 한국어 요약" not in text:
        # 초록 섹션이 없는 경우 키워드 앞에 삽입
        text = text.replace("\n\n## 키워드\n", ko_section + "\n\n## 키워드\n", 1)

    return text


def collect_target_files() -> list[Path]:
    """번역 대상 파일 목록 수집 (서브디렉토리·카탈로그 제외)."""
    files = []
    for f in sorted(PAGES_DIR.glob("*.md")):
        if f.name.startswith("catalog_"):
            continue
        files.append(f)
    return files


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="실제 파일 수정 없이 대상만 출력")
    parser.add_argument("--limit", type=int, default=0, help="처리할 최대 파일 수 (0=전체)")
    parser.add_argument("--resume-from", default="", help="이 파일명부터 처리 재개")
    args = parser.parse_args()

    files = collect_target_files()
    print(f"전체 대상: {len(files)}편\n")

    # resume-from 적용
    if args.resume_from:
        idx = next((i for i, f in enumerate(files) if f.name >= args.resume_from), 0)
        files = files[idx:]
        print(f"  {args.resume_from} 부터 재개 ({len(files)}편 남음)\n")

    processed = 0
    skipped = 0
    errors = 0

    for i, path in enumerate(files):
        if args.limit and processed >= args.limit:
            print(f"\n--limit {args.limit} 도달, 중단.")
            break

        text = path.read_text(encoding="utf-8")

        # 이미 번역 있으면 건너뜀
        if "## 한국어 요약" in text:
            skipped += 1
            continue

        info = extract_from_page(text)
        if not info["title"]:
            print(f"  [skip-notitle] {path.name}")
            skipped += 1
            continue

        print(f"[{i+1}/{len(files)}] {path.name} ...", end=" ", flush=True)

        if args.dry_run:
            print("[dry]")
            processed += 1
            continue

        ko = translate_paper_ko(info["title"], info["abstract"], info["keywords"])
        if not ko or not ko.get("title_ko"):
            print("[번역실패]")
            errors += 1
            time.sleep(1)
            continue

        new_text = patch_page(text, ko)
        path.write_text(new_text, encoding="utf-8")
        print(f"[완료] {ko.get('title_ko', '')[:30]}")
        processed += 1
        time.sleep(0.3)  # API 호출 간격

    print(f"\n--- 결과 ---")
    print(f"번역 완료: {processed}편")
    print(f"기존 번역 있어 건너뜀: {skipped}편")
    print(f"오류: {errors}편")


if __name__ == "__main__":
    main()
