# 연구 동향 개요

> 이 페이지는 위키 전체의 합성 요약. 소스가 쌓일수록 계속 갱신됨.
> 마지막 업데이트: 2026-05-26 (PDF 5편 + OpenAlex 635편 기반)

---

## 위키 소스 구성

| 구분 | raw 경로 | 편수 | 활용 목적 |
|------|----------|------|-----------|
| **A. NetMiner 사용 논문** | `raw/netminer/` | 5편 | 제품 마케팅·사례 연구 |
| **B. SNA 학계 트렌드 논문** | `raw/*.md` | 626편 (2020–2026) | 학계 트렌드 파악, 제품 기획 방향 |
| &emsp;└ Social Networks | — | ~621편 | ISSN 0378-8733 |
| &emsp;└ Network Science | — | 188편 raw | ISSN 2050-1250 |
| &emsp;└ Connections (INSNA) | — | 5편 (2025) | ISSN 2816-4245 |
| **C. 응용 분야 논문** | `raw/applied/` | 수집 예정 | 타 분야 SNA 응용 파악, 신규 시장 발굴 |

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

## Part 2: 학계 트렌드 논문 (OpenAlex 635편) 기반 인사이트

> Social Networks + Network Science + Connections 학술지 2020–2026 수집. NetMiner 사용 여부와 무관하며, SNA 연구 동향 파악 및 제품 기획 방향 설정에 활용.
> - Social Networks (ISSN 0378-8733): 621편 / Network Science (ISSN 2050-1250): 크로스오버 포함 / Connections (ISSN 2816-4245, INSNA): 5편 (2025)

### SNA 방법론 빈도 순위 (2020–2026, 181편 개별 분석)

→ 상세: [[pages/insights/sna_method_frequency|SNA 방법론 빈도 분석]]

| 순위 | 방법론 | 논문 수 | NetMiner 지원 | 비고 |
|------|--------|---------|:------------:|------|
| 1 | 에고중심 / 퍼스널 네트워크 | 37 | ✅ | 강점 영역 |
| 2 | 종단 / 동적 네트워크 | 30 | ⚠️ 부분 | **2020 추가 후 순위 상승** |
| 3 | ERGM (및 변형: STERGM·ergmito) | 26 | ✅ | **즉시 홍보 1순위** |
| 4 | 중심성 분석 | 23 | ✅ | 핵심 강점 |
| 5 | 다층 / 멀티플렉스 / 이분 | 22 | ✅ | 지원 확인, 홍보 부족 가능성 |
| 6 | 토픽모델링 / LDA | 19 | ✅ | 전부 LDA. BERTopic 0건 |
| 7 | SAOM / RSiena | 18 | ❌ | 고급 연구자 이탈 요인 |
| 8 | ML (GNN 실사용 ≈ 2–3건) | 15 | ✅ | 미래 선점 포지셔닝 |
| 9 | Bayesian / MCMC | 13 | ❌ | — |
| 10 | 커뮤니티 탐지 / 코어-퍼리퍼리 | 11 | ✅ | Network Science 논문 추가 |
| 11 | 데이터 수집 방법론 | 10 | ✅ (Extension) | **2020년 신규 발견 트렌드** |
| 11 | 확산 / 전파 | 11 | ❌ | 중심성 기반 immunization 포함 |
| 13 | Bayesian / 잠재공간 모델 | 14 | ❌ | — |

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

**5. ERGM 변형 확산 + SAOM과의 이분화** *(2020~)*
- ERGM(26편) + SAOM(18편) = 44편 — 횡단/종단 쌍으로 통계적 네트워크 모델링의 양 축
- 2020년부터 ERGM 변형(STERGM·ergmito 등) 등장 — 적용 맥락에 맞게 분화 중
- NetMiner는 기본 ERGM 지원, SAOM 미지원 → ERGM 홍보 + SAOM 연계 전략 필요

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
| 🔴 즉시 | ERGM 기능 홍보 (콘텐츠·세미나) | 26편 트렌드, 지원 중이나 미홍보 |
| 🟠 단기 | 에고넷 수집→분석 워크플로우 콘텐츠 | 10편 트렌드 — Network Canvas·Trellis·GENSI 등 수집 도구 결과물을 NetMiner로 분석하는 파이프라인 (Extension과는 별개) |
| 🟠 단기 | Two-Mode / 이분 네트워크 사례 | 22편 트렌드 대응 |
| 🟠 단기 | GNN 케이스 스터디 제작 | 차별화 포인트, 현재 학술 수요 낮음 — 미래 선점 |
| 🟠 단기 | BERTopic 튜토리얼 | 실무·마케팅 분석가 타깃, 미래 선점 |
| 🟡 중기 | 종단 네트워크 시각화 강화 | 30편 트렌드 2위, 부분 대응 가능 |
| 🟡 중기 | SAOM 연계 워크플로우 가이드 | 18편, R 연계로 보완 |
| 🔵 장기 | 확산 시뮬레이션 기능 | 10편, 개발 비용 대비 검토 필요 |

---

## 미해결 질문 / 추가 조사 필요

- GNN(Graph Neural Network)과 전통 SNA의 결합: 최신 논문은?
- LLM + 네트워크 분석 결합 사례는?
- 시간적 네트워크(temporal network) 분석 방법론 트렌드?
- 한국 SNA 연구에서 NetMiner 점유율 변화 추이?
- Social Networks 외 SNA 주요 학술지(Network Science, JOSS 등) 동향은?
