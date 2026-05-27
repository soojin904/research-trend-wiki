# 위키 로그

## [2026-05-27] schema | methods 페이지 목적 명시 — 제품 기획 검토 자료
- `SCHEMA.md` — methods/ 폴더 설명 갱신: NetMiner 기능 목록([[pages/tools/netminer]])을 기준으로 ① 신규 기능 후보(❌) ② 기존 기능 개선 근거(⚠️) 두 가지 용도 명시
- `index.md` — Methods 섹션 헤더에 기준선(NetMiner 현재 기능 요약) 및 용도 주석 추가

## [2026-05-27] synthesize | method 페이지 분리 및 텍스트 분류 신규 추가
- `pages/methods/ml_gnn.md` → 삭제 후 3개로 분리
  - `pages/methods/ml.md` (신규) — 전통 ML / 앙상블: SVM·RF·XGBoost·K-Means·SHAP/XAI
  - `pages/methods/gnn.md` (신규) — GNN: GCN·GAT·지식 그래프·GraphRAG, SNA 학술지 사용 사례 포함
  - `pages/methods/text_classification.md` (신규) — 텍스트 분류 (~76편, 20%, 응용 3위): BERT 파인튜닝·제로샷·앙상블
- `index.md`, `applied_method_frequency_2026.md`, `topic_modeling.md`, `bayesian_network_model.md` 링크 갱신

## [2026-05-27] synthesize | applied 논문 arXiv 제외 후 재합성 완료 — 379편 전체
- arXiv 제외 후 남은 개별 페이지 379편, 탐색 에이전트 10개 × 38편 (chunks 0–9, 100% 커버)
- **업데이트 파일**:
  - `pages/insights/applied_method_frequency_2026.md` — 분석 기준 379편으로 갱신, 수치 재조정 (LLM 40%·감성 30%·토픽 18%·SNA 10%)
  - `pages/insights/applied_domain_venue_2026.md` — 379편, arXiv 게재 학술지 행 제거, 분야별 편수 재조정
  - `pages/insights/applied_data_source_2026.md` — 379편 기준 데이터 소스 비율 재조정
  - `overview.md` — Part 3 제목·수치 갱신 (100% 커버, arXiv 제외)
  - `index.md` — applied 현황 379편으로 갱신
- 주요 발견 (청크 8·9 추가 반영): 토픽+감성 복합, GNN/RAG 적용 확산, 도메인: 법률·의료·관광 등 다양화 확인

## [2026-05-27] synthesize | sna 데이터 소스 insight 추가
- `pages/insights/sna_data_source.md` (신규) — 설문/에고넷 56%, 종단 28%, 표준 데이터셋(Add Health·SSND·BHPS 등), 응용 분야 데이터 소스와 대조 테이블

## [2026-05-27] synthesize | applied 신규 method·insight 페이지 추가
- `pages/methods/llm_nlp.md` (신규) — LLM/GPT 활용, 응용 분야 1위(~186편), ❌ NetMiner
- `pages/methods/sentiment_analysis.md` (신규) — 감성 분석, 응용 분야 2위(~140편), ⚠️ 부분 지원, ABSA 심화 포함
- `pages/insights/applied_data_source_2026.md` (신규) — Twitter/X 1위, 소셜미디어 40%·뉴스 16%·리뷰 14%, 다국어 NLP 15–20%, 고객 세그먼트별 데이터 소스 정리

## [2026-05-27] synthesize | applied 응용 분야 논문 지식 합성 완료 — 592편
- 대상: `pages/papers/applied/` 개별 페이지 459편 (에이전트 8개 × 74편 = 592편 분석)
- 에이전트 실패: chunks 8–9 (141편, 세션 한도) — 약 80% 커버
- **생성/업데이트 파일**:
  - `pages/insights/applied_domain_venue_2026.md` (신규) — 7개 분야 분포, 261개 학술지
  - `pages/insights/applied_method_frequency_2026.md` (신규) — LLM 31%·감성 24%·토픽 14%·SNA 8%
  - `pages/methods/topic_modeling.md` — 응용 분야 섹션 추가 (LDA 55편, BERTopic 18편, 조합 패턴)
  - `pages/methods/ml_gnn.md` — 응용 분야 섹션 추가 (Transformer 120편, GPT 60편, XGBoost 30편)
  - `pages/methods/semantic_network_analysis.md` — 응용 분야 섹션 추가 (공출현 18편, Textom 경쟁 언급)
  - `pages/concepts/mixed_methods.md` — 패턴 6 (토픽+감성), 패턴 7 (텍스트+SNA) 추가
  - `pages/tools/other_tools.md` — BERTopic, Textom, Sometrend, Orange, Hugging Face 추가
  - `overview.md` — Part 3 (응용 분야 인사이트 + NetMiner 시사점) 추가
- 핵심 발견: LLM 방법론 도구화 급증, BERTopic이 LDA 잠식 중, SNA+텍스트 결합이 응용 분야 표준 패턴, Textom이 국내 직접 경쟁자로 부상

## [2026-05-26] update | 폴더 구조 재편 — raw/sna/, pages/papers/sna/ 신설
- `raw/*.md` (667개) → `raw/sna/` 이동
- `pages/papers/*.md` (265개, 개별 258편 + catalog 7개) → `pages/papers/sna/` 이동
- wikilink 업데이트: index.md + concepts 4개 + methods 9개 + tools 1개 (총 17개 파일)
- SCHEMA.md, overview.md 경로 표기 갱신
- batch_ingest.py 경로 상수 갱신 (RAW_DIR, PAGES_DIR → sna/ 하위)

## [2026-05-26] ingest | 응용 분야 논문 (유형 C) 최초 인제스트 — 973편
- 수집 스크립트: `fetch_applied.py` — "social network" + "text analysis" 키워드, cited_by_count:desc 정렬, 쿼리당 최대 500건
- 수집 기간: 2026년 (--from-date 2026-01-01 --to-date 2026-12-31)
- 제외 학술지: Social Networks / Network Science / Connections (유형 B와 중복 방지)
- 인제스트 결과: 개별 페이지 733편 (`pages/papers/applied/`) + 카탈로그 240편 (`pages/papers/applied/catalog_2026.md`)
- 번역: 미적용 (--no-translate). 필요 시 소급 번역 가능
- 총 페이지: 291 → 1,025

> append-only. 인제스트·쿼리·린트 이력.
> 파싱 팁: `grep "^## \[" log.md | tail -10` → 최근 10개 항목

## [2026-05-26] lint | 위키 건강 점검
- 총 페이지: 291 (papers 270 · concepts 6 · methods 11 · insights 2 · tools 2)
- 깨진 링크: 0개 ✅
- 고아 페이지: 0개 ✅
- index.md 누락: 0개 ✅
- 링크 부족(2개 미만): 0개 ✅
- 수정: social_network_analysis.md가 methods/에 잘못 생성 → concepts/으로 이동
- 수정: overview.md 메타데이터 "370편" → "635편", index.md 통계 291로 갱신

## [2026-05-26] update | methods/ 페이지 전면 재구성 — 유형 B(OpenAlex SNA 학술지) 기반

**작업 내용**:
- 기존 3개 페이지 유형 B 논문으로 보강 (centrality, topic_modeling, semantic_network_analysis)
  - 유형 A(netminer/) 참조만 있던 내용 → 유형 B 논문 실제 사용 패턴으로 교체/보완
  - 각 페이지에 YAML frontmatter(netminer_support 포함) 추가
- 신규 8개 페이지 생성:
  - ergm.md (26편, 3위) — STERGM·ergmito·Bayesian 변형 포함
  - saom.md (18편, 7위) — 종단 공진화, NetMiner 이탈 요인
  - longitudinal_network.md (30편, 2위) — TERGM·REM·시간 그래프
  - community_detection.md (11편, 공동10위) — 모듈성·블록모델·코어-퍼리퍼리
  - bayesian_network_model.md (14편, 9위) — LPCM·LSPCM·MCMC
  - diffusion_propagation.md (11편, 공동10위) — SIR·면역화·WIP 중심성
  - ml_gnn.md (15편, 8위) — 링크 예측·신경망·그래프 임베딩
  - network_scaleup.md (7편, 13위) — NSUM·ARD·RDS
- index.md Methods 섹션 업데이트 (3개 → 11개), 통계 수치 갱신 (283 → 294)
- 각 페이지: 2–5편 유형 B 논문 실제 사용 맥락 반영

## [2026-05-26] update | 폴더 구조 재편 — concepts/methods/insights 분리
- concepts/ (연구 설계 패턴): social_network_analysis, personal_network, causal_inference_networks, multilayer_network, mixed_methods, systematic_literature_review
- methods/ (구체적 분석 기법): centrality, topic_modeling, semantic_network_analysis
- insights/ (신규, 쿼리 결과): sna_method_frequency, netminer_trend_insight
- wikilink 60개 파일 일괄 업데이트, index.md·SCHEMA.md 구조 문서 갱신

## [2026-05-26] update | 개별 페이지 244편 한국어 요약 소급 적용 완료
- 대상: pages/papers/*.md 개별 페이지 전체 (netminer/ 서브디렉토리 제외)
- 추가 내용: **제목(한글)**, ## 한국어 요약 (연구질문·방법론·주요결과), ## 초록 (원문)
- 처리 현황: 2020(37) + 2021(28) + 2022-2023(23) + 2024(33) + 2025(25) + 2026(14) = 160편 신규 추가
  - 나머지 84편: 이미 한국어 내용 있어 건너뜀
- 최종 확인: 미번역 페이지 0편

## [2026-05-26] update | 2024_*.md 33편 한국어 요약 섹션 일괄 추가
- pages/papers/2024_*.md 34개 파일 탐색, 1편(netminer/2024_jang_*) 건너뜀 (이미 한국어 작성)
- 나머지 33편에 **제목(한글)**, ## 한국어 요약 (연구질문·방법론·주요결과), ## 초록 (원문) 삽입
- 초록 비공개 3편(ceoldo, lai, neal_stopping)은 제목+키워드 기반 추정 번역 적용

## [2026-05-26] update | batch_ingest.py 한국어 번역 기능 추가
- 개별 페이지 생성 시 Claude Haiku API 호출 → 제목(한글), 연구질문, 방법론, 주요결과 번역
- 생성 페이지 포맷: 한국어 요약 섹션 + 초록(원문) 구조로 변경
- `--no-translate` 플래그로 번역 건너뜀 가능
- ingest_applied() 에도 동일 번역 적용
- SCHEMA.md, ingest/SKILL.md 규칙 업데이트

## [2026-05-26] query | 수집 학술지 3종 확인 — ISSN 목록 갱신
- ISSN 2050-1250 = Network Science (Cambridge UP), raw/nws_* 188편
- ISSN 2816-4245 = Connections (INSNA, De Gruyter, Diamond OA), raw/connections_2025_000* 5편
- index.md, overview.md 수집 학술지 항목에 3종 모두 명시 (Social Networks + Network Science + Connections)

## [2026-05-26] update | 분석 오류 패턴 문서화 — SCHEMA.md, index.md
- 검증된 오류 3가지를 SCHEMA.md "분석 시 반드시 지켜야 할 규칙" 섹션에 추가
- index.md Overview 하단에 요약 주의사항 추가
- 오류 내용: ① OpenAlex 태그 오신뢰, ② NetMiner 지원=학술수요 오판, ③ 논문주제→기능 잘못 연결(데이터수집→Extension)

## [2026-05-26] ingest + update | Network Science 2026 신규 9편 처리 및 인사이트 반영
- 신규 raw 파일 9편 발견 (Network Science 학술지, nws_2026/nws_2025)
- 개별 페이지 5편 생성, 카탈로그 4편 추가 (catalog_2026 → 16편)
- 수집 학술지 확장: Social Networks → Social Networks + Network Science
- 신규 인사이트:
  - 텍스트→가치 네트워크 파이프라인 (Almquist 2026, climate talks)
  - 중심성 기반 immunization in multiplex (Asil 2026)
  - 코어-퍼리퍼리 탐지 알고리즘 (Yanchenko 2026)
- 업데이트: sna_method_frequency (181편), netminer_trend_insight (신규 섹션 2개), overview/index 수치 갱신
- batch_ingest.py UnicodeEncodeError 수정 (em-dash → -)

## [2026-05-26] update | 2020 논문 인사이트 반영 — 빈도 분석·트렌드·우선순위 갱신
- sna_method_frequency.md: 분석 범위 2020–2026 (176편)으로 확대, 순위 재계산
  - 종단/동적 30편으로 2위 상승, ERGM 26편 3위, 데이터수집방법론 10편 신규 진입
- overview.md: Part2 데이터 갱신, 트렌드 #6(데이터수집방법론) 신규 추가, 우선순위표 갱신
- netminer_trend_insight.md: 우선순위표에 "데이터수집 Extension 홍보" 즉시 항목 추가
- 핵심 신규 발견: 데이터 수집 방법론이 2020년 독자 연구 흐름 — NetMiner Extension과 직결

## [2026-05-26] update | 응용 분야 논문 유형 C 체계 추가
- SCHEMA.md: 논문 소스 3유형 표 및 폴더 구조 업데이트 (A·B 기존 + C 신규)
- index.md: Section C 플레이스홀더 추가 (raw/applied/ → pages/papers/applied/)
- overview.md: 소스 구성 표에 C열 추가
- batch_ingest.py: ingest_applied() 함수 추가 — applied/ 전량 개별 페이지, 점수 임계값 없음

## [2026-05-26] ingest | Social Networks 2020 + 2021–2025 추가분 (OpenAlex 신규 127편+)
- 신규 처리: 2020 논문 127편 + 2021–2025 미처리분 추가
- 개별 페이지 119개 신규 생성 (2020: 37편, 2021–2025 추가분 포함)
- 카탈로그 업데이트: 2020 신규(85편) + 2021~2025 각 추가
- 최종 현황: 개별 페이지 253편, 카탈로그 7개(373편), 총 626편 (2020–2026)

## [2026-05-26] update | overview·index 인사이트 전면 반영
- overview.md: 방법론 빈도 표에 GNN 실사용 ≈ 0 비고 추가, BERTopic 0건 명시, ERGM 홍보 1순위 강조, 트렌드 #6(GNN·BERTopic 미래선점) 신규 추가
- index.md: topic_modeling·netminer_trend_insight·netminer 설명 갱신, 통계 수치 정확화 (147+ → 159)

## [2026-05-26] update | NetMiner PDF 논문 페이지 분리 — pages/papers/netminer/ 서브디렉토리
- pages/papers/ 내 PDF 기반 5편을 pages/papers/netminer/ 로 이동
- 참조 파일 11개 wikilink 전체 업데이트 (index, overview, concepts 4개, methods 2개, tools 2개, papers 1개)
- raw/netminer/ 구조와 대칭

## [2026-05-26] update | 논문 유형 A/B 분리 — index.md, overview.md 재구성
- index.md: A(NetMiner 사용 논문 PDF 5편) / B(학계 트렌드 OpenAlex 370편) 명확히 분리
- overview.md: Part 1(PDF 기반 인사이트) / Part 2(OpenAlex 트렌드 인사이트)로 재구성

## [2026-05-25] update | NetMiner 메뉴 반영 및 인사이트 재정리
- netminer.md: 전체 기능 메뉴 정확히 업데이트 (ERGM·GNN·BERTopic·Two-Mode 등 확인)
- concepts/netminer_trend_insight.md 신규 생성: 트렌드-기능 대조, 홍보 기회·공백·우선순위

## [2026-05-25] query | 가장 자주 사용된 SNA 방법론
- 참조 페이지: 139편 (개별 페이지 전체)
- 신규 저장 페이지: pages/insights/sna_method_frequency.md
- 핵심 결과: 1위 에고중심(30), 2위 ERGM·종단(22), 4위 중심성·토픽모델링·다층(19)

## [2026-05-25] ingest | Social Networks 2021–2025 + 2026 추가분 (OpenAlex 351편)
- 관련도 점수 3 이상: 개별 페이지 120편 생성 (pages/papers/)
- 관련도 하위: 연도별 카탈로그 6개 생성 (catalog_2021~2026.md, 총 231편)
- 핵심 선별 기준: 텍스트마이닝, 복합 방법론, 신규 SNA 방법론, 소프트웨어·도구

## [2026-05-25] update | tools/other_tools 신규 생성
- 이 위키 논문에서 실제 사용된 도구(R, SPSS MODELER, RSiena) + 비교 대상 도구(Gephi, UCINET, Python, VOSviewer) 정리
- NetMiner 포지셔닝 요약 표 포함

## [2026-05-25] update | methods/mixed_methods, tools/netminer 보완
- mixed_methods.md: 패턴 5 추가 (정성+네트워크 동학 — Kreager 2026 기반)
- netminer.md: 기능 개발 방향 인사이트 섹션 추가 (2026 트렌드 기반), 위키링크 경로 수정

## [2026-05-25] ingest | Social Networks 학술지 2026 (OpenAlex 14편)
- 처리 파일: scripts/fetch_openalex.py → raw/2026_openalex_*.md (14건)
- 생성 페이지: 14개 (논문) + 3개 (개념: personal_network, causal_inference_networks, multilayer_network)
- 업데이트 페이지: index.md, overview.md
- 핵심 인사이트: 2026년 Social Networks 학술지 주요 흐름 — 인과 추론×네트워크, 퍼스널 네트워크 다양화, 다층 네트워크로의 전환, 네트워크×공간 통합

---

## [2026-05-25] init | 위키 초기화

- SCHEMA.md, index.md, log.md, overview.md 생성
- 폴더 구조: raw/, pages/concepts, papers, methods, tools

---

## [2026-05-25] ingest | 5개 PDF 일괄 인제스트

**처리 소스**:
1. Jang & Nemoto (2024) — 행복 영향 요인: 토픽모델링 + 신경망
2. Morashti 외 (2022) — 지속가능 패키징 SLR
3. Park 외 (2022) — 디지털 헬스케어 생태계 네트워크 분석
4. Jeon & Park (2022) — 노인 소셜 네트워크와 건강
5. 강윤지 외 (2021) — 광고홍보학 CSR 연구동향 (의미연결망 + 토픽)

**생성 페이지 (12개)**:
- papers/: 5개 논문 요약 페이지
- concepts/: social_network_analysis, centrality, topic_modeling, semantic_network_analysis
- methods/: mixed_methods, systematic_literature_review
- tools/: netminer

**핵심 인사이트**:
- 5개 논문 전부 NetMiner 사용 → 인용 사례 마케팅 자료로 활용 가능
- 의미연결망 + 토픽모델링 복합 방법론이 연구동향 분석의 표준 패턴으로 부상
