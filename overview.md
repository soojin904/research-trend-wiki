# 연구 동향 개요

> 이 페이지는 위키 전체의 합성 요약. 소스가 쌓일수록 계속 갱신됨.
> 마지막 업데이트: 2026-09-22 (PDF 5편 + SNA 학계 318편 + 응용 분야 789편 전수 재합성 — 2026-05-27판 대체)

---

## 위키 소스 구성

| 구분 | raw 경로 | 편수 | 활용 목적 |
|------|----------|------|-----------|
| **A. NetMiner 사용 논문** | `raw/netminer/` | 5편(PDF) + raw 수집분 다수(인제스트 대기) | 제품 마케팅·사례 연구 |
| **B. SNA 학계 트렌드 논문** | `raw/sna/` | 개별 페이지 318편 | 학계 트렌드 파악, 제품 기획 방향 |
| **C. 응용 분야 논문** | `raw/applied/` | 개별 페이지 789편 | 타 분야 SNA·텍스트마이닝 응용 파악, 신규 고객 세그먼트 발굴 |

---

## Part 1: NetMiner 사용 논문 (PDF 5편) 기반 인사이트

### 복합 방법론의 부상

5개 논문 전부에서 "단일 방법론 → 복합 방법론" 패턴이 관찰됨.

| 결합 패턴 | 사례 논문 |
|-----------|----------|
| 의미연결망 + 토픽모델링 | [[pages/papers/netminer/2021_kang_csr_ad_semantic_network\|강윤지 외]], [[pages/papers/netminer/2022_morashti_sustainable_packaging\|Morashti 외]] |
| 토픽모델링 + 신경망/ML | [[pages/papers/netminer/2024_jang_happiness_topic_nn\|Jang & Nemoto]] |
| 네트워크 분석 + 토픽모델링 | [[pages/papers/netminer/2022_park_digital_healthcare_network\|Park 외]] |
| SNA 지표 + 통계 회귀 | [[pages/papers/netminer/2022_jeon_social_network_health_elderly\|Jeon & Park]] |

→ 자세한 패턴 분석: [[pages/concepts/mixed_methods|복합 방법론]]

### NetMiner 포지션 (사용 사례 기반)

**5개 논문 전부에서 [[pages/tools/netminer|NetMiner]] 사용** — 데이터마이닝 + SNA 통합 도구로서의 위치 확인.

- 외국인 연구자도 선택 (Morashti 외 — 부산대 외국인 교수)
- 복합 방법론 전체 파이프라인을 단일 도구로 지원하는 점이 차별화

### 주요 연구 흐름 (PDF 논문)

**1. 연구동향 분석 (Bibliometric + Text Mining)**
- 특정 분야의 논문을 대량 수집 → 키워드 네트워크 + 토픽으로 트렌드 파악
- 사례: [[pages/papers/netminer/2021_kang_csr_ad_semantic_network|CSR 연구동향]], [[pages/papers/netminer/2022_morashti_sustainable_packaging|지속가능 패키징 SLR]]

**2. 이해관계자·생태계 네트워크 분석**
- 뉴스·소셜 데이터로 산업 구조·담론 파악
- 사례: [[pages/papers/netminer/2022_park_digital_healthcare_network|디지털 헬스케어 생태계]]

**3. 개인 네트워크(에고넷)와 사회적 결과**
- 개인의 네트워크 위치 → 건강·웰빙 등 결과에 미치는 영향
- 사례: [[pages/papers/netminer/2022_jeon_social_network_health_elderly|노인 건강 연구]]

**4. 텍스트 마이닝 → 예측 모델**
- 비정형 텍스트 분석 결과를 ML/신경망에 연결
- 사례: [[pages/papers/netminer/2024_jang_happiness_topic_nn|행복 요인 연구]]

---

## Part 2: 학계 트렌드 논문 (SNA 318편 전수) 기반 인사이트

> Social Networks + Network Science + Connections 학술지 2020–2026 수집, `pages/papers/sna/` 개별 페이지 318편 **전수** 재분석(2026-09-22). NetMiner 사용 여부와 무관하며, SNA 연구 동향 파악 및 제품 기획 방향 설정에 활용. 이전 판(181편, 2026-05-27)을 대체.

### SNA 방법론 빈도 순위 (318편 전수)

→ 상세: [[pages/insights/sna_method_frequency|SNA 방법론 빈도 분석]]

| 순위 | 방법론 | 논문 수 | NetMiner 지원 | 비고 |
|------|--------|---------|:------------:|------|
| 1 | 에고중심 / 퍼스널 네트워크 설계·수집 방법론 | ~46 | ✅ (분석) / ❌ (수집도구 자체) | **단일 최대 클러스터**. 수집 도구(GENSI·Network Canvas·Trellis)는 Ego Network Extract로 연결 |
| 2 | ERGM (및 변형: DERGM·다층·Bayesian·이분·count-valued 등) | ~40 | ⚠️ 기본만 | 변형 다수는 미지원 |
| 3 | SAOM / RSiena | ~29 | ❌ | 고급 연구자 이탈 요인 |
| 4 | 중심성 분석 (신규 변형: temporal betweenness·WIP·distinctiveness 포함) | ~25 | ✅ (기본 7종) / ❌ (신규 변형) | 핵심 강점이나 최신 변형은 공백 |
| 5 | 커뮤니티 탐지 / 블록모델링 | ~24 | ✅ (기본) / ❌ (BMCD 등 신규) | — |
| 6 | 다층 / 멀티플렉스 / 이분(Two-Mode) | ~23 | ✅ | Two-Mode는 중심성 3종뿐 — bipartite ERGM 등은 ❌ |
| 7 | 관계적 사건 모형 (REM/RHEM/DyNAM) | ~17 | ❌ | **신규 발견 클러스터** — 2023 Social Networks 특별호로 성숙 확인 |
| 8 | Network Scale-Up / ARD | 9 | ❌ | **신규 발견 클러스터**, R/Stan 패키지 영역에 가까움 |
| 9 | 임베딩/GNN인접 (진짜 GNN 0건) | 8 | ✅(GNN 자체는 지원) | 태그 오탐 10건+ 전수 확인, 실제 GNN 논문 0/318 |
| 10 | 잠재공간 / Bayesian 네트워크 모형 | ~6 | ❌ | — |

**ERGM(40) + SAOM(29) + REM(17) = 86편(전체의 27%)** — 하나의 "동적·생성적 통계 네트워크 모형" 계열로 묶임. 개별 기능 공백이 아니라 방법론 계열 전체의 공백.

### 주요 트렌드 흐름 (2020–2026)

**1. 인과 추론 × 네트워크** *(2021–2026 중심)*
- RCT와 네트워크의 교차점 — 행위자 간 상호의존이 인과 추론 가정(SUTVA)을 위반
- Spillover 효과 모델링, SAOM, counterfactual 프레임워크 등이 핵심 방법론
- 관련: [[pages/concepts/causal_inference_networks|인과 추론과 네트워크]]

**2. 퍼스널·에고중심 네트워크의 다양한 응용** *(2020~)*
- 2020년: 데이터 수집 방법론 집중 (GENSI 등 시각적 도구, 대규모 수집 노하우)
- 2021~: 노숙인·치매·노년 등 취약계층 연구로 확산, ARD·RDS 등 방법론 정교화
- 관련: [[pages/concepts/personal_network|퍼스널 네트워크]]

**3. 다층·멀티플렉스 네트워크** *(2020~, 2024–2026 집중)*
- 단일 레이어 → 다층 구조로의 전환이 분명한 흐름
- 레이어 간 상관, 동료 영향 추정, 연합의 다층성 등 이슈 대두
- 관련: [[pages/concepts/multilayer_network|다층·멀티플렉스 네트워크]]

**4. 네트워크 × 공간·지리** *(2021–2026)*
- 소셜 네트워크를 물리적 공간과 통합하는 연구 등장
- 이동성 데이터 + 네트워크 데이터 결합

**5. ERGM·SAOM·REM — "동적·생성적 통계 네트워크 모형" 3대 축** *(전수 재확인, 2026-09-22)*
- ERGM(40편) + SAOM(29편) + REM/RHEM(17편) = 86편(27%) — 횡단(ERGM)/종단(SAOM)/이벤트(REM) 3갈래로 분화
- REM은 신규 발견 클러스터: 이벤트 로그 단위 데이터라 SAOM·ERGM과 자료구조부터 다름, NetMiner 메뉴 하나로 해결 안 되는 영역
- NetMiner는 기본 ERGM만 지원, SAOM·REM 모두 미지원 → 전체 계열 공백으로 인식하고 우선순위 판단 필요 (개별 기능 추가보다 R 연계 가이드가 현실적)

**10. 에고넷 배치 분석 — 가장 저비용 실행 가능한 기회** *(전수 재확인, 2026-09-22)*
- 에고넷 관련 논문 46편(단일 최대 클러스터)이지만, 필요 부품(Ego Network Extract·지표 계산·Hierarchical Clustering·Random Forest)은 이미 NetMiner에 모두 존재
- 학계는 이미 "구조 유형 자동 분류"(clustering/Random Forest로 에고넷 유형화) 단계로 진화 — NetMiner는 개별 지표 계산까지만 지원, 이들을 잇는 워크플로우가 없음
- 신규 기능 개발 없이 **워크플로우 문서화·템플릿화만으로 대응 가능** — ROI 가장 높은 항목

**6. 데이터 수집 방법론이 독자 연구 흐름으로** *(2020년 신규 발견)*
- 시각적 에고넷 수집 도구(GENSI, Network Canvas, Trellis 등), 설문 설계, 데이터 품질 연구 집중
- 전부 **에고넷 인터뷰·설문 수집** 방법론 — SNS/Biblio/News Collector Extension과는 무관
- **NetMiner 연결**: 수집 도구로 모은 에고넷 데이터를 Ego Network Extract로 분석하는 파이프라인 콘텐츠 기회. 조직 설문 수집 → NetMiner 분석 워크플로우 케이스 스터디

**7. GNN·BERTopic: NetMiner가 학계보다 앞선 상태** *(전 기간)*
- GNN 실사용 ≈ 2–3건(2020 포함), BERTopic 0건 — 학술 수요 낮음
- 미래 선점 포지셔닝: GNN(코딩 없는 그래프 ML) / BERTopic(실무·마케팅 분석가 타깃)

**8. 텍스트 → 네트워크 파이프라인이 정책·기후 분야로 확장** *(Network Science 2026 신규)*
- keyword-assisted topic model → value network 추출 → 국가 간 협상 구조 분석 (Almquist 외 2026)
- NetMiner 핵심 강점(텍스트 마이닝 + 네트워크 분석 통합)의 응용 분야가 확장 중
- 기후 협약, 국제 협상, 정책 담론 분석 등 새로운 고객 세그먼트 발굴 가능

**9. 중심성 기반 네트워크 개입(Immunization)** *(Network Science 2026 신규)*
- 다층 네트워크에서 중심성으로 핵심 노드 식별 → 바이러스/정보 확산 차단
- 중심성(✅ NetMiner) + 다층 네트워크(✅) + 확산 분석(❌) 교차 영역
- 확산 시뮬레이션 없이도 "중심성으로 개입 대상 선별" 워크플로우는 NetMiner로 가능

### NetMiner 제품 기획 시사점

→ 상세: [[pages/insights/netminer_trend_insight|NetMiner 기능-트렌드 인사이트]]

| 우선순위 | 액션 | 근거 |
|---------|------|------|
| 🔴 즉시 | **에고넷 배치 분석 워크플로우 템플릿화** | 46편(1위 클러스터), 필요 부품 이미 존재 — 개발비용 0, 문서화만 필요 |
| 🔴 즉시 | ERGM 기능 홍보 (콘텐츠·세미나) | 40편, 지원 중이나 미홍보 |
| 🟠 단기 | Two-Mode / 이분 네트워크 사례 | 23편 트렌드 대응 |
| 🟠 단기 | 최신 중심성 변형 검토(temporal betweenness 등) | 중심성 25편 중 신규 변형 다수 미지원 |
| 🟡 중기 | SAOM·REM 연계 워크플로우 가이드(R 연계) | SAOM 29편+REM 17편=46편, 신규 기능보다 연계 가이드가 현실적 |
| 🟡 중기 | 커뮤니티 탐지 신규 변형(BMCD 등) 검토 | 24편 중 신규 알고리즘 다수 |
| 🔵 장기 | Network Scale-Up/ARD 연계 검토 | 9편, R/Stan 패키지 영역에 가까워 자체 개발 우선순위 낮음 |

---

## Part 3: 응용 분야 논문 (789편 전수) 기반 인사이트

> `raw/applied/` 수집("social network"/"text analysis" 키워드) `pages/papers/applied/` 개별 페이지 789편 **전수** 재분석(2026-09-22). SNA·텍스트마이닝이 마케팅·보건·법률 등 응용 분야에서 어떻게 쓰이는지, 신규 고객 세그먼트를 파악하기 위한 목적. 이전 판(592편/80%커버리지, 2026-05-27)을 대체.

→ 상세 분석: [[pages/insights/applied_method_frequency_2026|응용 분야 방법론 빈도]] · [[pages/insights/applied_domain_venue_2026|도메인 및 학술지 분포]] · [[pages/insights/applied_data_source_2026|데이터 소스 분석]]

### 방법론 순위 (응용 분야, 789편 기준)

| 순위 | 방법론 | 편수 | NetMiner 지원 |
|------|--------|------|:-------------:|
| 1 | LLM/GPT 활용 (분류·추출·RAG·에이전트) | ~215 (27%) | ❌ |
| 2 | 감성 분석 (BERT·VADER·TextBlob·ABSA) | ~213 (27%) | ⚠️ 부분 (ABSA·멀티모달 ❌) |
| 3 | 토픽 모델링 (LDA·BERTopic·STM) | ~145 (18%) | ✅ (BERTopic 포함 — 과거 기록 오류 정정) |
| 4 | 텍스트 분류 / 트랜스포머 파인튜닝 | ~120 (15%) | ⚠️ 부분 |
| 5 | **진짜 SNA/네트워크 분석** | ~50–57 (7%) | ✅ |
| 6 | 혼합방법론 | ~45 (6%) | ⚠️ 부분 |
| 7 | GNN | ~25–30 (3%) | ✅(지원 자체는) / 실사용 낮음 |
| 8 | 멀티모달 분석 (텍스트+이미지/오디오/영상) | ~25 (3%) | ❌ |

> 응용분야에서도 SNA는 소수(7%)다 — 유형 C 수집의 목적 자체가 "SNA 심화"가 아니라 "텍스트마이닝의 폭넓은 응용 확인"이기 때문. 저자원 언어 NLP(아랍어·네팔어·카자흐어·벵골어·인도네시아어·헝가리어·타지크어 등)가 15~20%를 차지하는 지속적 교차 클러스터.

### 응용 분야 분포 (789편 기준)

| 분야 | 편수(대략) | NetMiner 기회 |
|------|------|---------------|
| 보건/정신건강 | ~140 (18%) | **최대 분야, NetMiner 침투도 최저** — 최우선 타깃 |
| 정치/거버넌스/미디어 | ~135 (17%) | 담론·프레이밍 분석 — SNA+텍스트 결합 강점 |
| 마케팅/이커머스/관광 | ~110 (14%) | 리뷰 감성+토픽+SNA — 실사용자층 직결 |
| 디지털 인문학 | ~55 (7%) | Voyant·Quanteda 사용자층 — 진입점 다름 |
| 교육 | ~50 (6%) | 텍스트 분석 중심 |
| 법률 | ~45 (6%) | LLM RAG 중심 — 진입 어려움 |
| 환경/지속가능성 | ~40 (5%) | — |
| 금융 | ~35 (4%) | — |

### 핵심 발견 및 NetMiner 시사점

**1. 도메인 특화 소형 모델이 범용 LLM을 이긴다 (최우선 전략 시사점)**
- ConfliBERT·DEBATE/DeBERTa·BERTimbau-LoRA·RuBioBERT 등 도메인 파인튜닝 소형 모델이 GPT-4o/Claude 등 범용 LLM 프롬프팅보다 정확도·비용·속도 모두 우위 — 7개 청크 중 4개 이상에서 독립적으로 반복 확인된 강한 근거.
- 터키어 법률 텍스트에서는 TF-IDF+SVM이 GPT-4o-mini와 정확도 동률(속도는 압도적 우위)인 사례도 확인.
- **NetMiner 포지셔닝**: 범용 LLM과 직접 경쟁(추격)하지 말고, 가벼운 도메인 모델 연계 지점 + 재현성·비용 우위를 내세울 것.

**2. BERTopic·BERT 감성분석 — "기능 공백"이 아니라 "홍보 실패"였음 (2026-09-22 정정)**
- 기존 기록: BERTopic ❌, BERT 기반 감성분석 ❌ → **오류로 확인됨**. NetMiner는 Text > BERTopic/BERTrend, Lab > Sentiment Analysis(7개 언어)를 이미 지원.
- SNA 전문지(Social Networks 등)에서는 BERTopic 실사용 0건이지만, 응용분야 문헌(789편)에서는 거의 매 청크마다 반복 확인될 정도로 표준 도구화됨 — "학술 수요는 있는데 지원 사실이 덜 알려진" 전형적 마케팅 갭.

**3. 진짜 SNA 응용 사례는 소수지만 질 높은 데모 후보 존재**
- 가장 강력한 데모 후보: `lie_quantifying_multidisciplinary`(의료진 협진 네트워크 — 공출현+modularity+Degree/Betweenness/PageRank, NetMiner 메뉴와 1:1 대응, 최대 분야인 보건에서 침투도 최저)
- 차순위: `kim_big_datadriven_topical`(K-POP 키워드 네트워크, NetworkX — 국내 마케팅 콘텐츠 적합), `gu_analyzing_natural_disaster`(81편 코퍼스 — 세미나·소규모 데이터 적합)

**4. 신규 경쟁 도구 확인 — pyBiblioNet, Sometrend(썸트렌드), TEXTOM**
- **pyBiblioNet**: OpenAlex 연동 오픈소스 Python 라이브러리, 인용·공저·키워드공출현 네트워크+중심성+커뮤니티탐지+NLP 통합 — **Biblio Extension과 직접 경쟁**(무료라는 점에서 위협적)
- **Sometrend/TEXTOM**: 국내 상용 텍스트분석 플랫폼 2종, 공출현 네트워크+중심성 기능 보유 확인 — 기존에 "SNA 없음"으로 잘못 기록돼 있던 부분 정정
- VOSviewer·CiteSpace·R bibliometrix 등 서지계량 무료 도구 생태계가 이미 형성되어 있어, Biblio Extension 홍보 시 차별점을 명확히 제시해야 함

**5. 저자원 언어 + 글로벌 연구자 수요 지속**
- 아랍어·네팔어·카자흐어·벵골어·인도네시아어·헝가리어·타지크어 등 비영어 논문이 15~20% 지속 — 다국어 텍스트 분석 수요, NetMiner 다국어 지원 확장 기회

**6. "Post-API 시대" 데이터 수집 위기 — SNS Extension 전략 신호**
- 플랫폼 API 제한으로 소셜미디어 데이터 수집이 갈수록 어려워진다는 언급 확인 — NetMiner SNS Extension 포지셔닝(대안 수집 경로 제공)에 중요한 시장 신호

### NetMiner 제품 기획 추가 시사점 (응용 분야 기반)

| 우선순위 | 액션 | 근거 |
|---------|------|------|
| 🔴 즉시 | 보건/의료 분야 SNA 케이스 스터디 제작 (`lie_quantifying_multidisciplinary` 등) | 최대 분야(18%)인데 NetMiner 침투도 최저 |
| 🔴 즉시 | BERTopic·BERT 감성분석 지원 사실 홍보 | 기능은 있는데 몰라서 못 씀 — 즉시 실행 가능, 개발비용 0 |
| 🟠 단기 | 마케팅/이커머스/관광 케이스 스터디 | 리뷰 감성+토픽+SNA 패턴, 실사용자층 직결 |
| 🟠 단기 | ABSA(측면 기반 감성분석) 기능 강화 | 감성분석 213편, 도메인 확산 추세 |
| 🟠 단기 | 가벼운 도메인 모델 연계 가이드(범용 LLM 대신) | 소형 파인튜닝 모델이 범용 LLM보다 우위라는 근거 축적 |
| 🟡 중기 | pyBiblioNet·Sometrend·TEXTOM 대비 차별화 콘텐츠 | 무료/국내 경쟁 도구 확인 |
| 🟡 중기 | 허위정보·에코챔버 분석 케이스 스터디 | 정치/미디어 분야(17%) SNA+텍스트 수요 |

---

## 미해결 질문 / 추가 조사 필요

- GNN(Graph Neural Network)과 전통 SNA의 결합: 최신 논문은?
- LLM + 네트워크 분석 결합 사례는?
- 시간적 네트워크(temporal network) 분석 방법론 트렌드?
- 한국 SNA 연구에서 NetMiner 점유율 변화 추이?
- Social Networks 외 SNA 주요 학술지(Network Science, JOSS 등) 동향은?
