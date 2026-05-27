# 위키 인덱스

> LLM이 쿼리 시 가장 먼저 읽는 카탈로그. 새 페이지 생성 시 즉시 업데이트.

---

## Overview

- [[overview|분야 전체 합성]] — NetMiner 사용 사례 + 학계 트렌드 분리 정리

> **분석 시 주의사항** (검증된 오류 패턴 — 자세한 내용: [[SCHEMA.md]])
> 1. OpenAlex `tags`는 AI 자동 태그 — 오태깅 빈번. 방법론 빈도 집계 시 초록·본문으로 재확인 필수
> 2. "NetMiner 지원 ✅" ≠ "학술 수요 높음" — 항상 분리해서 서술 (BERTopic·GNN이 대표 사례)
> 3. 논문 주제 → NetMiner 기능 연결 시 실제 워크플로우 성립 여부를 구체적으로 확인 (데이터수집 논문 → Extension 연결은 오류였음)
> 4. "Reprint of: ..." 논문은 빈도 집계에서 원본과 동일 취급 (중복 제거)

---

## Papers

### A. NetMiner 사용 논문 (PDF 원문 수집)

> 실제 NetMiner를 사용한 연구. 제품 마케팅·사례 연구 자료로 활용.

- [[pages/papers/netminer/2024_jang_happiness_topic_nn|Jang & Nemoto (2024)]] — 행복 영향 요인: LDA + 신경망, **NetMiner 4.5** (#topic-modeling #neural-network #mixed-methods)
- [[pages/papers/netminer/2022_morashti_sustainable_packaging|Morashti 외 (2022)]] — 지속가능 패키징 SLR: 키워드 네트워크 + LDA, **NetMiner 4** (#systematic-review #keyword-network #sustainability)
- [[pages/papers/netminer/2022_park_digital_healthcare_network|Park 외 (2022)]] — 디지털 헬스케어 생태계 네트워크 분석, **NetMiner** + R (#network-analysis #digital-healthcare)
- [[pages/papers/netminer/2022_jeon_social_network_health_elderly|Jeon & Park (2022)]] — 노인 우정 네트워크와 건강: SNA + 회귀, **NetMiner 4.0** (#sna #centrality #health)
- [[pages/papers/netminer/2021_kang_csr_ad_semantic_network|강윤지 외 (2021)]] — 광고홍보학 CSR 연구동향: 의미연결망 + LDA, **NetMiner 4** (#semantic-network #topic-modeling #csr)

---

### B. 학계 트렌드 파악용 논문 (OpenAlex 수집, Social Networks 학술지)

> NetMiner 사용 여부와 무관한 SNA 학계 동향 파악 목적. 제품 기획·방향 설정 참고용.

**트렌드 분석 요약**: [[pages/insights/sna_method_frequency|SNA 방법론 빈도 (2021–2026)]] · [[pages/insights/netminer_trend_insight|NetMiner 기능-트렌드 인사이트]]

#### 2026년 주요 논문 (개별 페이지)
- [[pages/papers/sna/2026_omalley_spillover_rct|O'Malley 외 (2026)]] — Stepped-wedge RCT 의사 네트워크 spillover 인과 추론 (#causal-inference #spillover)
- [[pages/papers/sna/2026_haapanen_coalition_sna_design|Haapanen 외 (2026)]] — 다중 조직 연합의 다층 구조와 SNA 설계 (#coalition #multilevel)
- [[pages/papers/sna/2026_mcmillan_network_rct_causal|McMillan 외 (2026)]] — 네트워크 위치 차이가 RCT 인과 추론에 미치는 위협 (#causal-inference #saom)
- [[pages/papers/sna/2026_zhang_egocentric_csa|Zhang & Wang (2026)]] — 에고중심 네트워크와 CSA 소비자 반응 (#egocentric #csa)
- [[pages/papers/sna/2026_almquist_homelessness_personal_network|Almquist 외 (2026)]] — 노숙 경험자 퍼스널 네트워크 (3,000명+, 종단) (#personal-network)
- [[pages/papers/sna/2026_schafer_personal_network_loneliness|Schafer 외 (2026)]] — 동반 관계와 외로움: 퍼스널 네트워크 재평가 (#personal-network #loneliness)
- [[pages/papers/sna/2026_gebhard_intervention_dementia|Gebhard & Ellinger (2026)]] — 치매 환자 개입과 네트워크 변화 (#intervention #dementia)
- [[pages/papers/sna/2026_nishi_wellbeing_experimental_network|Nishi 외 (2026)]] — 동료 웰빙 가시화와 협력 네트워크 (#experimental-network #wellbeing)
- [[pages/papers/sna/2026_lubbers_nsm_ard|Lubbers 외 (2026)]] — Network Scale-Up Method & ARD 발전 리뷰 (#nsum #ard)
- [[pages/papers/sna/2026_fluer_multiplex_survey|Fluer 외 (2026)]] — 설문 → 멀티플렉스 모델 (#multiplex #interlayer)
- [[pages/papers/sna/2026_an_peer_influence_multilayer|An 외 (2026)]] — 다층 네트워크에서 동료 영향 추정 (#multilayer #peer-influence)
- [[pages/papers/sna/2026_kreager_mixed_methods_lifecourse|Kreager 외 (2026)]] — 생애 과정 전환의 혼합 방법론 설계 (#mixed-methods #network-dynamics)
- [[pages/papers/sna/2026_qiao_ecommerce_rural_china|Qiao & Qiu (2026)]] — 농촌 중국 e-커머스 창업의 소셜 영향 (#social-influence)
- [[pages/papers/sna/2026_fancello_sociability_space|Fancello 외 (2026)]] — 소셜 네트워크를 지리 공간에 배치 (#spatial-network)

#### 2020–2026년 고관련도 논문 (개별 페이지 258편)
`pages/papers/sna/` 폴더 직접 탐색 또는 `/wiki:query`로 검색

#### 연도별 카탈로그 (관련도 하위 논문 목록)
- [[pages/papers/sna/catalog_2020|2020년 카탈로그]] — 85편
- [[pages/papers/sna/catalog_2021|2021년 카탈로그]] — 80편
- [[pages/papers/sna/catalog_2022|2022년 카탈로그]] — 87편
- [[pages/papers/sna/catalog_2023|2023년 카탈로그]] — 44편
- [[pages/papers/sna/catalog_2024|2024년 카탈로그]] — 26편
- [[pages/papers/sna/catalog_2025|2025년 카탈로그]] — 39편
- [[pages/papers/sna/catalog_2026|2026년 카탈로그 (추가분)]] — 16편

---

### C. 응용 분야 논문 (키워드 수집, `raw/applied/`)

> **수집 범위**: SNA 전문 학술지(Social Networks·Network Science·Connections) 외 전 저널·분야.
> **수집 방식**: `fetch_applied.py` — "social network" 또는 "text analysis" 키워드로 OpenAlex 검색, 인용 수 상위 500건/쿼리.
> **성격**: NetMiner 사용 여부와 무관. SNA·텍스트마이닝이 마케팅·보건학·경영학·커뮤니케이션 등 응용 분야에서 어떻게 쓰이는지 파악하고 신규 고객 세그먼트를 발굴하는 목적.
> **인제스트**: `batch_ingest.py` → 관련도 점수 기반 분류 (개별 페이지: `pages/papers/applied/`, 카탈로그: `pages/papers/applied/catalog_YYYY.md`).

**현황**: 973편 수집 (2026년) — 개별 페이지 379편 (`pages/papers/applied/`, arXiv ~80편 제외) · 카탈로그 240편 (`pages/papers/applied/catalog_2026.md`)

`pages/papers/applied/` 폴더 직접 탐색 또는 `/wiki:query`로 검색

---

## Concepts (연구 설계 패턴)

> 연구를 어떻게 설계·구성하는가에 관한 프레임워크와 패턴

- [[pages/concepts/social_network_analysis|Social Network Analysis (SNA)]] — SNA 개요, 핵심 분석 유형, 도구 비교
- [[pages/concepts/personal_network|퍼스널·에고중심 네트워크]] — 개념, 측정, 적용 사례
- [[pages/concepts/causal_inference_networks|인과 추론과 네트워크]] — spillover·SAOM·RCT 위협 요인
- [[pages/concepts/multilayer_network|다층·멀티플렉스 네트워크]] — 복수 레이어 구조, 분석 방법
- [[pages/concepts/mixed_methods|복합 방법론 (Mixed Methods)]] — 텍스트+네트워크 결합 패턴, NetMiner 연관성
- [[pages/concepts/systematic_literature_review|체계적 문헌 고찰 (SLR)]] — 데이터마이닝 기반 SLR 워크플로우

---

## Methods (구체적 분석 기법)

> **용도**: [[pages/tools/netminer]] 기능 목록을 기준선으로, 두 가지 제품 기획 질문에 답하기 위한 자료.
> 1. **신규 기능 후보** — NetMiner에 없는 방법론 (❌ 표시)
> 2. **기존 기능 개선 근거** — NetMiner에 있지만 학술 트렌드와 격차가 있는 방법론 (⚠️ 표시)
>
> NetMiner 현재 기능 요약: LDA·BERTopic ✅ / GCN·GAT·GraphSAGE ✅ / 감성분석(Lab, 7개 언어) ✅ / 지식그래프(Lab) ✅ / SHAP·Classical ML ✅ / ERGM ✅ | SAOM·LLM·RAG·텍스트분류(Transformer) ❌

### 기존 (유형 A → B 보강)
- [[pages/methods/centrality|Centrality (중심성)]] — degree/closeness/betweenness 등 중심성 지표 (24편, 4위) ✅
- [[pages/methods/topic_modeling|Topic Modeling (토픽모델링)]] — LDA·키워드 보조 토픽 모델, 네트워크 연계 패턴 (20편, 6위) ✅
- [[pages/methods/semantic_network_analysis|Semantic Network Analysis (의미연결망)]] — 키워드 공출현 네트워크, 시계열 담론 분석 ✅

### 신규 (유형 B 기반)
- [[pages/methods/ergm|ERGM (지수 랜덤 그래프 모형)]] — STERGM·ergmito·Bayesian 변형 포함 (26편, 3위) ✅ 기본 / ⚠️ 변형
- [[pages/methods/saom|SAOM / RSiena (확률적 행위자 지향 모형)]] — 종단 공진화 모형, NetMiner 이탈 요인 (18편, 7위) ❌
- [[pages/methods/longitudinal_network|종단/동적 네트워크 분석]] — TERGM·REM·시간 그래프 포함 (30편, 2위) ⚠️ 부분
- [[pages/methods/community_detection|커뮤니티 탐지]] — 모듈성·블록모델·코어-퍼리퍼리 (11편, 공동10위) ✅
- [[pages/methods/bayesian_network_model|Bayesian / 잠재공간 모델]] — LPCM·LSPCM·MCMC 추론 (14편, 9위) ❌
- [[pages/methods/diffusion_propagation|확산/전파/면역화]] — SIR 모형·면역화 전략·WIP 중심성 (11편, 공동10위) ❌
- [[pages/methods/ml|전통 ML / 앙상블]] — 링크 예측·노드 분류·SVM·RF·XGBoost (15편, 8위) ✅
- [[pages/methods/gnn|GNN (그래프 신경망)]] — GCN·GAT·지식 그래프·GraphRAG (~19편) ✅
- [[pages/methods/network_scaleup|Network Scale-Up / ARD]] — 은닉 집단 규모 추정·RDS (7편, 13위) ❌

### 신규 (유형 C 응용 분야 기반)
- [[pages/methods/llm_nlp|LLM / GPT 활용]] — 파인튜닝·RAG·자동 코딩, 응용 분야 1위 (~150편, 40%) ❌
- [[pages/methods/sentiment_analysis|감성 분석 (Sentiment Analysis)]] — BERT·VADER·ABSA, 응용 분야 2위 (~115편, 30%) ⚠️ 기본
- [[pages/methods/text_classification|텍스트 분류 (Text Classification)]] — BERT 파인튜닝·제로샷·앙상블, 응용 분야 3위 (~76편, 20%) ⚠️ 부분

---

## Insights (분석 결과·인사이트)

> 위키 쿼리 결과 및 누적 분석 정보

- [[pages/insights/sna_method_frequency|SNA 방법론 사용 빈도 (2020–2026)]] — 181편 집계, 트렌드 순위
- [[pages/insights/netminer_trend_insight|NetMiner 기능-트렌드 인사이트]] — ERGM 즉시홍보·GNN/BERTopic 미래선점·SAOM공백, 우선순위 정리
- [[pages/insights/applied_domain_venue_2026|응용 분야 도메인 및 학술지 분포 (2026)]] — 379편 (arXiv 제외), 7개 분야, 181개 학술지 분포
- [[pages/insights/applied_method_frequency_2026|응용 분야 방법론 빈도 (2026)]] — 379편 전체 집계, LLM 40%·감성분석 30%·토픽 18%·SNA 10%, NetMiner 시사점
- [[pages/insights/applied_data_source_2026|응용 분야 주요 데이터 소스 (2026)]] — Twitter/X 1위, 소셜미디어 40%·뉴스 16%·리뷰 14%, 다국어 NLP 15–20%
- [[pages/insights/sna_data_source|SNA 학술지 주요 데이터 소스 (2020–2026)]] — 설문/에고넷 인터뷰 56%, 종단 28%, 응용 분야와 수집 방식 대조 정리

---

## Tools (도구)

- [[pages/tools/netminer|NetMiner]] — 전체 기능 메뉴, PDF 사용 사례 5편, 학술 트렌드 대조 (ERGM·GNN·BERTopic 지원 현황)
- [[pages/tools/other_tools|Other Tools]] — R·SPSS MODELER·RSiena 실사용 + Gephi·UCINET·Python 비교

---

## 통계

- 총 페이지: 767 (papers 740 · concepts 6 · methods 13 · insights 6 · tools 2)
- 최근 업데이트: 2026-05-27 (applied 합성 완료 — methods 2개, insights 1개 추가)
- NetMiner 사용 논문: 5편 (PDF, `pages/papers/netminer/`)
- 학계 트렌드 논문: 635편 (OpenAlex, 2020–2026) — 개별 페이지 258편 + 카탈로그 7개(377편)
- 응용 분야 논문: 699편 (키워드 수집, 2026) — 개별 페이지 459편 + 카탈로그 1개(240편)
- 수집 학술지 (유형 B): Social Networks (ISSN 0378-8733), Network Science (ISSN 2050-1250), Connections (ISSN 2816-4245, INSNA)
