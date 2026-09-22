---
title: "SNA 방법론 사용 빈도 분석 (전수 318편)"
tags: [method-frequency, ergm, saom, relational-event, centrality, egocentric, nsum]
generated_by: wiki:query
query_date: 2026-09-22
supersedes: "2026-05-25/26 버전 (139~181편 기반)"
---

# SNA 방법론 사용 빈도 분석 (전수 318편)

**분석 기준**: 318편 (2026-09-22 기준, `pages/papers/sna/` 전체)
**대상**: 유형 B — SNA 전문 학술지(Social Networks, Network Science, Connections) 2020–2026
**집계 방식**: 개별 논문 페이지 전수 판독(초록·방법론 직접 확인). catalog 파일 제외, reprint 중복 6건은 1편으로 병합, Pinheiro 교과서 챕터 6건은 연구 논문이 아니므로 빈도 집계 제외.

> **이전 버전과의 차이**: 2026-05-25/26 버전은 139~181편 표본 기반이었다. 이번 판은 **약 2배 규모의 전수 집계**이며 순위·수치가 모두 갱신되었다. 이전 수치는 더 이상 인용하지 말 것.

---

## 순위표 (318편 전수)

| 순위 | 방법론 클러스터 | 논문 수 | 분류 | NetMiner 지원 |
|------|----------------|--------:|------|:-------------:|
| 1 | **에고중심 네트워크 연구설계·측정 방법론** | **46** | 측정·설계 | ⚠️ 부분 |
| 2 | **ERGM 및 변형** (DERGM·multilevel·Bayesian·bipartite·count-valued·ERNM·TERGM) | **40** | 통계 모델링 | ⚠️ 기본만 |
| 3 | **SAOM / RSiena** | **29** | 종단 통계 모델 | ❌ |
| 4 | 중심성 (연구 주제로 다룬 경우) | 25 | 구조 측정 | ⚠️ 기본 7종 |
| 5 | 커뮤니티 탐지 / 블록모델링 / 코어-퍼리퍼리 | 24 | 구조 분석 | ⚠️ 기본만 |
| 6 | 다층 / 멀티플렉스 / 이분(2-mode) 네트워크 | 23 | 데이터 구조 | ⚠️ 부분 |
| 7 | **REM / RHEM / DyNAM** (관계 사건 모형) | **17** | 이벤트 기반 동적 모델 | ❌ |
| 8 | 그래프 이론·알고리즘 (triad census, 시간 경로 등) | 14 | 알고리즘 | ⚠️ 부분 |
| 9 | 텍스트 → 네트워크 (의미연결망·담론 네트워크·NLP/LLM 파이프라인) | 10 | 텍스트+네트워크 | ✅/⚠️ |
| 9 | 네트워크 형성 이론 · 의견 동학 · 확산 (ABM/이론) | 10 | 이론·시뮬레이션 | ❌ |
| 11 | **NSUM / ARD** (은닉 집단 규모 추정) | **9** | 측정·추정 | ❌ |
| 12 | 그래프 임베딩 (SVD·VAE·CCA 등, GNN 인접) | 8 | 표현학습 | ⚠️ |
| 13 | 잠재공간 / Bayesian 네트워크 모형 | 6+ | 통계 추정 | ❌ |
| 14 | 계량서지학 / 과학 네트워크 | 5 | 응용 | ✅ |
| 15 | 혼합 방법론 (질적+SNA) | 4 | 설계 | — |
| 16 | 인과 추론 (RCT·spillover) | 3 | 설계 | ❌ |
| 16 | 결측·불확실 데이터 처리 | 3 | 측정 | ❌ |
| 18 | 부호 네트워크 / 부정적 유대 | 2 | 데이터 구조 | ⚠️ |
| — | **진짜 GNN 방법론 논문** | **0** | — | ✅ (수요 없음) |

*중심성은 "논문의 연구 대상이 중심성 자체인 경우"만 집계했다. 다른 방법의 한 구성요소로 중심성을 계산한 논문까지 포함하면 100편을 훌쩍 넘으므로 순위 비교에 의미가 없다.*

---

## 주요 해석

### (a) 양대 클러스터 — 에고넷 방법론(46) + ERGM(40)

두 클러스터가 전체의 27%를 차지한다. 성격은 정반대다.

- **에고중심 방법론(46편)**: "네트워크 데이터를 어떻게 제대로 수집·측정할 것인가". 이름 생성기 설계, 시각적 수집 도구(GENSI·Network Canvas·Trellis·VINA), 회상 편향·대리 응답 정확도, 알터 수 설계, **에고넷 구조 유형 자동 분류(군집화·Random Forest)**. → [[pages/concepts/egocentric_network_design|에고중심 네트워크 연구설계]]
- **ERGM(40편)**: 단일 모형이 아니라 **변형의 계열**로 분화 중 (DERGM, multilevel, Bayesian, bipartite, count-valued, ERNM, TERGM). → [[pages/methods/ergm|ERGM]]

### (b) 행위자·이벤트 기반 동적 모델링 슈퍼클러스터 (ERGM 40 + SAOM 29 + REM 17 = 86편)

318편 중 **27%**가 "네트워크가 어떻게 생성·변화하는가"를 생성 모형으로 추정하는 통계 방법론이다. SNA 학술지의 방법론적 주류라고 봐도 무방하다.

- SAOM(29) — 행위자가 유대를 선택하는 연속시간 과정 → [[pages/methods/saom|SAOM/RSiena]]
- REM/RHEM/DyNAM(17) — 타임스탬프가 찍힌 **개별 사건(event)** 시퀀스를 직접 모형화. 2023년 Social Networks에 REM 특별호가 존재할 만큼 성숙한 하위 분야 → [[pages/methods/relational_event_model|관계 사건 모형(REM)]]

**학술 수요**: 매우 높음(86편). **NetMiner 지원**: 기본 ERGM만 ✅, SAOM·REM은 ❌. 두 축은 별개 사실로 분리해서 서술할 것.

### (c) 진짜 GNN 논문 0편 / 318편 — 재확인된 음성 결과

OpenAlex "Advanced Graph Neural Networks" 태그가 붙은 논문은 10편 이상이지만, 초록·방법론을 직접 확인한 결과 **GCN/GraphSAGE/GAT 등 GNN 방법론을 실제로 사용한 논문은 0편**이었다(berenhaut, zuev, nijs, yanchenko, koskinen 등 모두 오태깅 확인). 임베딩 계열 8편도 SVD·VAE·CCA 기반으로 GNN이 아니다.

- 이는 2026-05 시점의 판단("GNN 실사용 2–3건")을 **약 2배 표본에서 0건으로 더 강하게 재확인**한 것이다.
- **분리 서술**: NetMiner는 GNN(GCN/GraphSAGE/GAT)을 지원한다 ✅. 그러나 **SNA 전문지 학계 수요는 실질적으로 0**이다. GNN은 현재 수요 대응이 아니라 미래 선점·차별화 메시지로만 다뤄야 한다.
- 동일 구도: BERTopic도 NetMiner 지원 ✅ / SNA 전문지 사용 0건.

### (d) 신규 발견 클러스터 — NSUM/ARD 9편

이전 집계(7편)보다 늘었을 뿐 아니라, **전용 리뷰 논문**과 **Bayesian/Stan 통합 툴킷 논문**이 등장해 하나의 독립 하위 분야로 자리잡았다. 다만 이는 GUI SNA 소프트웨어보다 R/Stan 패키지 영역에 가깝다 — 학술 트렌드로는 기록하되 곧바로 NetMiner 기능 공백으로 환산하지 말 것. → [[pages/methods/network_scaleup|NSUM / ARD]]

### (e) "측정 방법론" 자체가 독립 연구 흐름

에고넷 설계(46) + NSUM/ARD(9) + 결측·불확실 데이터(3)를 합치면 58편. **"네트워크 데이터를 어떻게 올바르게 수집·추정할 것인가"** 가 SNA 학술지의 가장 큰 단일 관심사다. 분석 알고리즘 경쟁보다 데이터 입력 단계의 품질 문제가 학계 화두라는 뜻이다.

---

## NetMiner 포지셔닝 시사점

> SCHEMA 규칙 2: 아래 표는 **학술 수요(편수)** 와 **NetMiner 지원 여부**를 별개 열로 분리해 읽을 것. 지원한다고 수요가 있는 것도, 수요가 있다고 지원하는 것도 아니다.

| 클러스터 | 학술 수요 | NetMiner 지원 | 해석 |
|---------|:--------:|:------------:|------|
| 에고넷 연구설계·측정 | 46편 (1위) | ⚠️ Ego Network Extract (수집 후 분석만) | 수집 도구 결과물 분석 워크플로우는 성립. **구조 유형 자동 분류**는 미지원 — 업그레이드 기회 |
| ERGM | 40편 (2위) | ⚠️ 기본 ERGM ✅ / 변형 ❌ | 기본 지원 사실 자체가 미홍보. 변형 수요는 R 연계 |
| SAOM | 29편 | ❌ | 고급 종단 연구자 R 이탈 요인 |
| REM/RHEM/DyNAM | 17편 | ❌ | 데이터 구조부터 다름(이벤트 로그). 신규 패러다임 |
| 중심성 | 25편 | ⚠️ 기본 7종 | 신규 변형(temporal betweenness, WIP, distinctiveness) 미지원 |
| 커뮤니티/블록모델 | 24편 | ⚠️ Louvain·Leiden·Conventional Blockmodel | 확률적 블록모델·코어-퍼리퍼리 미지원 |
| 다층/이분 | 23편 | ⚠️ Two-Mode 중심성·Merge Layers | 이분 ERGM·다층 모형화 미지원 |
| NSUM/ARD | 9편 | ❌ | R/Stan 영역 — 제품 공백으로 직결시키지 말 것 |
| 잠재공간/Bayesian | 6+편 | ❌ | 고급 연구자 수요 |
| GNN | **0편** | ✅ | 지원은 하나 학술 수요 없음 — 미래 선점용 |
| BERTopic/LDA | LDA 계열만 소수 | ✅ | 동일 구도 |

**핵심 결론**: 이번 전수 집계에서 확인된 가장 큰 NetMiner 기능 공백은 **ERGM 변형 + SAOM + REM으로 구성된 86편 규모의 "동적·생성적 통계 네트워크 모형" 군**이다. 개별 기능이 아니라 하나의 방법론 계열로 묶인 공백이라는 점이 중요하다.

---

## 위키 연관

- [[pages/insights/netminer_trend_insight|NetMiner 기능-트렌드 인사이트]]
- [[pages/methods/ergm|ERGM]]
- [[pages/methods/saom|SAOM / RSiena]]
- [[pages/methods/relational_event_model|관계 사건 모형 (REM/RHEM/DyNAM)]]
- [[pages/methods/network_scaleup|Network Scale-Up / ARD]]
- [[pages/methods/centrality|중심성 분석]]
- [[pages/methods/community_detection|커뮤니티 탐지]]
- [[pages/methods/bayesian_network_model|Bayesian / 잠재공간 모델]]
- [[pages/concepts/egocentric_network_design|에고중심 네트워크 연구설계]]
- [[pages/concepts/personal_network|퍼스널 네트워크]]
- [[pages/concepts/multilayer_network|다층 네트워크]]
- [[pages/methods/gnn|GNN]]
- [[pages/tools/netminer|NetMiner]]
