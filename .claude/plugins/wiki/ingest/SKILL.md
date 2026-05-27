---
name: wiki:ingest
description: |
  raw/ 폴더의 소스(논문 PDF, 마크다운 등)를 위키에 통합하는 명령어.
  인수 없이 호출하면 미등록 파일을 자동 탐지해 처리하고, 파일명을 주면 해당 파일만 처리한다.
  "위키에 추가", "논문 등록", "ingest", "raw 처리" 등을 요청할 때 사용.
argument-hint: "[파일명 또는 경로]"
---

새 소스를 위키에 통합한다.

## 인수
`/wiki:ingest [파일명 또는 경로]`
- 인수 없이 호출하면 `D:\soojin\wiki\raw\`에서 index.md에 등록되지 않은 파일을 탐지해 모두 처리한다.
- 인수를 주면 해당 파일만 처리한다 (raw/ 기준 상대경로 또는 절대경로 모두 허용).

## 절차

### 1. 소스 파악
- 처리할 파일 목록 확인
- PDF면 PyMuPDF(fitz)로 텍스트 추출 (가상환경: `D:\soojin\.venv`)
- 마크다운이면 직접 읽기

### 2. 내용 분석
- 소스 유형 판단: 논문 / 기사 / 보고서 / 기타
- 핵심 내용 파악: 연구질문, 방법론, 주요 결과, 사용 도구

### 3. 페이지 생성
소스 유형에 따라 적절한 카테고리에 생성:

**batch_ingest.py 대상 (raw/applied/ 또는 raw/*.md 다수)**
```bash
cd /d/soojin && source .venv/Scripts/activate && python wiki/scripts/batch_ingest.py --no-translate
```
- 항상 `--no-translate` 사용 — 번역은 아래 4단계에서 병렬 에이전트로 처리

**소수 파일 (PDF 또는 수동 raw 파일)**
→ 직접 읽어서 아래 형식으로 페이지 생성:

```yaml
---
title:
authors: []
year:
venue:
tags: []
source: raw/파일명
---
```
내용:
- **제목(한글)**: 논문 제목 한국어 번역
- **연구질문**: 1–2문장 한국어 요약
- **방법론**: 한국어 불릿
- **주요 결과**: 핵심 발견 한국어 불릿
- **초록(원문)**: 영어 원문 초록

### 4. 한국어 번역 (병렬 에이전트)

batch_ingest.py로 생성된 페이지는 번역이 없으므로, 생성 후 아래 절차로 병렬 처리한다.

**4-1. 번역 대상 파일 목록 수집**
`## 한국어 요약` 섹션이 없는 신규 페이지를 찾는다:
```powershell
Get-ChildItem d:\soojin\wiki\pages\papers\applied\*.md |
  Where-Object { (Get-Content $_.FullName -Raw) -notmatch '## 한국어 요약' } |
  Select-Object -ExpandProperty FullName
```
(유형 B라면 `pages\papers\*.md`에서 catalog_* 제외)

**4-2. 청크 분할 및 병렬 에이전트 실행**
- 파일 수에 따라 청크 크기 결정:
  - ~50편 이하: 에이전트 1개
  - 51–200편: 에이전트 4개 (50편씩)
  - 201–500편: 에이전트 8개
  - 500편 초과: 에이전트 10개 (최대)
- **단일 메시지에 모든 에이전트를 동시에 spawn** (순차 실행 금지)

**4-3. 각 에이전트에게 전달할 프롬프트 형식**
```
다음 파일 목록의 논문 페이지에 한국어 번역 섹션을 추가해줘.

파일 목록:
- d:\soojin\wiki\pages\papers\applied\파일1.md
- d:\soojin\wiki\pages\papers\applied\파일2.md
...

각 파일에 대해:
1. 파일을 읽는다
2. "## 한국어 요약" 섹션이 이미 있으면 건너뜀
3. 없으면 제목·초록·키워드를 바탕으로 아래 내용을 작성해 H1 제목 바로 아래에 삽입:

**제목(한글)**: <제목 한국어 번역>

## 한국어 요약

**연구질문**: <핵심 질문 1–2문장>

**방법론**:
- <방법론 항목>

**주요 결과**:
- <결과 항목>

삽입 위치: H1(`# 제목`) 다음 줄 (기존 `**저자**:` 줄 바로 앞)
학술 용어는 한국어 표준 용어 사용, 모호하면 영문 병기.
모든 파일 처리 후 완료된 파일 수를 보고.
```

**4-4. 완료 확인**
모든 에이전트 완료 후 미번역 페이지가 0인지 확인:
```powershell
(Get-ChildItem d:\soojin\wiki\pages\papers\applied\*.md |
  Where-Object { (Get-Content $_.FullName -Raw) -notmatch '## 한국어 요약' }).Count
```

### 5. index.md 업데이트
- 새로 생성된 모든 페이지를 해당 섹션에 추가 (형식: `- [[경로|제목]] — 한 줄 요약 (#태그)`)
- 통계 (총 페이지 수, 소스 수, 최근 업데이트) 갱신

### 6. log.md 기록
```
## [YYYY-MM-DD] ingest | 소스 제목
- 처리 파일: 파일명
- 생성 페이지: N개 (번역 완료 N개)
- 핵심 인사이트: 1~2줄
```

> **methods/concepts/insights/tools/overview 업데이트는 `/wiki:synthesize`로 별도 실행.**
> ingest는 raw → pages 변환에만 집중.

## 규칙
- `raw/` 파일은 절대 수정하지 않는다
- 위키링크는 `[[파일경로|표시텍스트]]` 형식
- 모든 신규 페이지는 최소 2개 위키링크 포함
- NetMiner 관련 내용이 있으면 반드시 `pages/tools/netminer.md`에 사례 추가
