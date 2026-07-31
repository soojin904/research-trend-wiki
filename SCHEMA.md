# 연구 동향 위키 스키마

## 목적
소셜 네트워크 분석(SNA) 및 인접 방법론(텍스트 마이닝, 토픽 모델링, GNN 등)의
연구 동향을 누적·연결하는 개인 지식 베이스.

사이람 제품 기획 및 마케팅에 활용할 수 있는 수준의 분석·합성 포함.

---

## 논문 소스 유형 (3가지)

| 유형 | raw 경로 | pages 경로 | 수집 방식 | 활용 목적 |
|------|----------|-----------|----------|----------|
| **A. NetMiner 사용 논문** | `raw/netminer/` | `pages/papers/netminer/` | 논문 출처 수집 | 제품 마케팅·사례 연구 |
| **B. SNA 학계 트렌드 논문** | `raw/sna/` | `pages/papers/sna/` | OpenAlex API 수집 (Social Networks 등 SNA 전문지) | 학계 트렌드 파악, 제품 기획 방향 |
| **C. 응용 분야 논문** | `raw/applied/` | `pages/papers/applied/` | `fetch_applied.py` — 키워드 검색 (OpenAlex, 전 저널) | SNA·텍스트마이닝의 응용 분야 파악. 신규 고객 세그먼트 발굴 |

- **유형 C 특징**:
  - 수집 키워드: `"social network"` (SNA 전문 학술지 제외) / `"text analysis"` (topic ID t10028·t13910·t10664 포함, SNA 전문 학술지 제외)
  - 정렬: 인용 수 내림차순 (`cited_by_count:desc`), 쿼리당 최대 500건
  - NetMiner 사용 여부·SNA 전문지 여부와 무관 — 응용 분야 전반 포괄
  - 인제스트 시 관련도 점수 기반 분류: 점수 ≥ 임계값 → 개별 페이지, 미달 → `catalog_YYYY.md`
- 유형 C 파일명 규칙: `applied_YYYY_제목슬러그_DOI슬러그.md` (`fetch_applied.py` 자동 생성)

---

## 폴더 구조

```
wiki/
├── SCHEMA.md          ← 이 파일 (위키 운영 규칙)
├── index.md           ← 페이지 카탈로그 (LLM이 쿼리 시 가장 먼저 읽음)
├── log.md             ← 인제스트·쿼리·린트 이력 (append-only)
├── overview.md        ← 분야 전체 합성·현황 요약 (항상 최신 유지)
│
├── raw/               ← 원본 소스 (수정 금지)
│   ├── assets/        ← 다운로드된 이미지
│   ├── netminer/      ← [유형 A] NetMiner 사용 논문
│   ├── applied/       ← [유형 C] 응용 분야 논문 (타 분야 SNA 응용, 수동 큐레이션)
│   └── sna/           ← [유형 B] OpenAlex 수집 SNA 학술지 논문
│
└── pages/
    ├── concepts/      ← 연구 설계 패턴·프레임워크 (SNA 전반, 에고넷 연구 설계, 인과추론, 복합방법론 등)
    ├── methods/       ← 구체적 분석 기법·알고리즘. **NetMiner 기능 검토용 자료**: (1) NetMiner에 없는 방법 → 신규 기능 후보, (2) NetMiner에 있어도 개선 여지가 있는 방법 → 업그레이드 항목 근거. 기준선: [[pages/tools/netminer]]
    ├── insights/      ← 쿼리 결과·누적 분석 정보 (방법론 빈도, NetMiner 트렌드 인사이트 등)
    ├── papers/
    │   ├── netminer/  ← [유형 A] NetMiner 사용 논문 요약
    │   ├── sna/       ← [유형 B] SNA 학술지 논문 (개별 페이지 + catalog_YYYY.md)
    │   └── applied/   ← [유형 C] 응용 분야 논문 (개별 페이지 + catalog_YYYY.md)
    └── tools/         ← 소프트웨어·라이브러리 페이지
```

---

## 페이지 타입 및 규칙

### 폴더별 분류 기준

| 폴더 | 기준 | 예시 |
|------|------|------|
| `concepts/` | 연구 설계 패턴·프레임워크 | SNA 개요, 에고넷 연구 설계, 인과 추론 설계, 복합 방법론, SLR |
| `methods/` | 구체적 분석 기법·알고리즘 | 중심성 측정, 토픽모델링(LDA/BERTopic), 의미연결망, ERGM, SAOM |
| `insights/` | 쿼리 결과·누적 분석 정보 | 방법론 빈도 집계, NetMiner 트렌드 분석, 시장 기회 정리 |
- `methods/` 페이지의 **핵심 용도**: [[pages/tools/netminer]]의 현재 기능 목록을 기준으로 두 가지 검토
  - **신규 기능 후보**: NetMiner에 없는 방법론 (예: LLM/RAG, SAOM, 텍스트 분류 Transformer)
  - **기존 기능 개선 근거**: NetMiner에 있지만 학술 트렌드와 격차가 있는 방법론 (예: 감성 분석 Lab → ABSA 미지원, BERTopic → 지원하지만 홍보 부족)
  - 각 방법론 페이지에는 반드시 `NetMiner 지원 현황` 섹션을 포함하고, ✅/⚠️/❌ 기호로 명시
- `insights/`는 wiki:query 결과나 분석 요약을 저장 — raw 데이터가 아닌 합성된 인사이트

### 개념 페이지 (`pages/concepts/`)
- 파일명: `개념명_영문.md` (예: `egocentric_network_design.md`)
- 내용: 연구 설계 패턴 설명, 적용 맥락, 관련 논문, NetMiner 연관성

### 방법론 페이지 (`pages/methods/`)
- 파일명: `방법명_영문.md` (예: `ergm.md`, `sentiment_analysis.md`)
- 내용: 알고리즘·기법 설명, 수식(필요시), 대표 논문, **NetMiner 지원 현황**, 적용 사례
- **NetMiner 지원 현황 섹션 필수 포함**: [[pages/tools/netminer]] 기능 목록 기준으로
  - ✅ 지원: NetMiner 메뉴에 존재, 실사용 사례 있음
  - ⚠️ 부분: 기능 있으나 학술 트렌드 대비 커버 범위 제한 (개선 기회)
  - ❌ 미지원: NetMiner에 없음 (신규 기능 후보)
- 방법론 페이지 생성 기준:
  1. 응용 분야(유형 C) 또는 SNA 학술지(유형 B) 논문에서 빈도 높은 방법론
  2. NetMiner 기능과의 격차가 제품 기획에 의미 있는 방법론

### 인사이트 페이지 (`pages/insights/`)
- 파일명: 자유 (예: `sna_method_frequency.md`, `netminer_trend_insight.md`)
- 내용: 분석 결과 요약, 순위표, 전략적 시사점 — 반드시 분석 기준(날짜·대상 편수 등) 명시

### 논문 페이지 (`pages/papers/`)
- 파일명: `YYYY_저자성_키워드.md` (예: `2024_wang_gnn_community.md`)
- Frontmatter:
  ```yaml
  ---
  title: 논문 제목
  authors: [성1, 성2]
  year: YYYY
  venue: 저널/학회명
  tags: [sna, gnn, community-detection]
  source: raw/파일명.md
  ---
  ```
- 내용: 연구 질문, 방법, 주요 결과, NetMiner 연관성, 인용 관계

### 방법론 페이지 (`pages/methods/`)
- 파일명: `방법론명.md` (예: `topic_network_analysis.md`)
- 내용: 방법 설명, 적용 워크플로우, 대표 논문, 도구, 사이람 제품 적용 가능성

### 도구 페이지 (`pages/tools/`)
- 파일명: `도구명.md` (예: `gephi.md`, `netminer.md`)
- 내용: 기능 개요, 장단점, 주요 사용 사례, 경쟁 포지션

---

## 크로스 레퍼런스 규칙
- Obsidian 위키링크 문법 사용: `[[파일명]]` 또는 `[[파일명|표시텍스트]]`
- 모든 페이지는 최소 2개 이상의 위키링크 포함
- 고아 페이지(inbound 링크 0개)는 린트 시 플래그

---

## 운영 워크플로우

### Ingest (새 소스 추가)
1. 소스 파일을 `raw/`에 저장 (Obsidian Web Clipper 또는 직접 저장)
2. Claude에게 "이 소스 인제스트해줘" 요청
3. LLM 수행 순서:
   - 소스 읽기 → 핵심 내용 파악
   - `pages/papers/` 또는 적절한 카테고리에 요약 페이지 생성
     - **한국어 번역 포함**: 제목(한글), 연구질문, 방법론, 주요 결과를 한국어로 요약
     - batch_ingest.py 사용 시: 자동으로 Claude Haiku API 호출해 번역 생성 (`--no-translate`로 건너뜀 가능)
   - 관련 개념·방법론·도구 페이지 업데이트 (5~15개)
   - `overview.md` 관련 섹션 갱신
   - `index.md`에 새 페이지 항목 추가
   - `log.md`에 인제스트 기록 추가

### Query (질문)
1. 질문 → LLM이 `index.md` 읽어 관련 페이지 탐색
2. 관련 페이지 읽어 합성 답변 생성
3. 새로운 인사이트이면 위키 페이지로 저장

### Lint (건강 검진)
- "위키 린트해줘" 요청 시:
  - 고아 페이지 탐색
  - 모순된 내용 플래그
  - 누락된 크로스 레퍼런스 추가
  - `overview.md` 최신성 확인

---

## index.md 갱신 규칙
- 새 페이지 생성 시 즉시 `index.md`에 한 줄 추가
- 형식: `- [[파일경로|제목]] — 한 줄 요약 (태그: #tag1 #tag2)`

## log.md 기록 규칙
- 형식: `## [YYYY-MM-DD] ingest | 소스 제목`
- 또는: `## [YYYY-MM-DD] query | 질문 요약`
- 또는: `## [YYYY-MM-DD] lint | 처리 내용 요약`

---

## 분석 시 반드시 지켜야 할 규칙 (검증된 오류 패턴)

### 1. OpenAlex 자동 태그를 곧이곧대로 믿지 말 것
- OpenAlex의 `tags` 필드는 AI가 자동 부여한 것으로 **오태깅이 빈번함**
- 특히 "Advanced Graph Neural Networks" 태그: 그래프 관련 논문에 광범위하게 붙음. 실제 GNN 방법론 논문인지는 초록·키워드·방법론 섹션을 직접 확인해야 함
- 태그만 보고 방법론 빈도를 집계하지 말 것 — **반드시 초록/본문 내용으로 재확인**

### 2. "NetMiner가 지원한다 ≠ 학계에서 많이 쓴다"
- NetMiner 기능 목록에 있다고 해서 SNA 학술지 논문에서 실제 사용된다는 의미가 아님
- 인사이트 작성 시 **학술 수요(논문 편수)와 NetMiner 지원 여부를 반드시 분리해서 서술**
- 확인된 사례:
  - BERTopic: NetMiner 지원 ✅, Social Networks 학술지 실사용 0건
  - GNN(GCN/GraphSAGE/GAT): NetMiner 지원 ✅, SNA 학술지 실사용 ≈ 2–3건

### 3. 논문 주제와 NetMiner 기능을 연결할 때 기능명을 정확히 대응시킬 것
- 논문 주제가 A라고 해서 NetMiner의 관련 기능 B가 자동으로 마케팅 포인트가 되지는 않음
- 연결하기 전에 **실제 워크플로우가 성립하는지** 구체적으로 확인할 것
- 확인된 오류 사례:
  - "데이터 수집 방법론 논문 10편" → NetMiner SNS/Biblio/News **Extension** 홍보로 연결 ❌
    - 해당 논문들은 에고넷 인터뷰·설문 수집 방법론 (GENSI, Network Canvas, Trellis)
    - 올바른 연결: NetMiner **Ego Network Extract** 기능 + 수집 도구 결과물 분석 워크플로우

### 4. 방법론 빈도 집계 시 reprint 중복 주의
- Social Networks 학술지는 특별호에 기존 논문을 reprint하는 경우 있음
- "Reprint of: ..." 제목의 논문은 원본과 같은 내용 → **빈도 집계에서 1편으로 처리**

---

## 핵심 관심 태그
`#sna` `#centrality` `#community-detection` `#gnn` `#topic-modeling`
`#text-mining` `#sentiment` `#mixed-methods` `#netminer` `#temporal-network`
`#citation-network` `#knowledge-graph` `#llm-network`
