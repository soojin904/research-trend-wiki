---
title: "에고중심 네트워크 연구설계 (Egocentric Network Design)"
tags: [egocentric-network, personal-network, name-generator, data-collection, measurement, recall-bias, typology]
netminer_relevance: "⚠️ Ego Network Extract (수집 후 분석) — 구조 유형 자동 분류는 미지원"
created: 2026-09-22
---

# 에고중심 네트워크 연구설계 (Egocentric Network Design)

개인(ego)을 중심으로 그의 알터(alter)와 알터 간 관계를 **어떻게 수집·측정·분류할 것인가**를 다루는 연구설계 영역.
**SNA 전문 학술지 전수 318편 중 46편으로 단일 최대 클러스터**다 ([[pages/insights/sna_method_frequency|방법론 빈도 분석]], 2026-09-22 기준). [[pages/methods/ergm|ERGM]](40편)보다도 많다.

개념 자체는 [[pages/concepts/personal_network|퍼스널 네트워크]] 문서에서 다루며, 이 문서는 **연구설계·측정 방법론**에 집중한다.

> **왜 중요한가**: SNA 학술지의 최대 관심사가 "새 알고리즘"이 아니라 **"네트워크 데이터를 애초에 제대로 얻는 법"** 이라는 뜻이다. 분석 기능 경쟁과는 다른 축의 시장 신호다.

---

## 1. 이름 생성기(Name Generator) 방법론

에고에게 "누구를 아는가"를 묻는 질문 설계가 결과를 좌우한다.

| 논문 | 발견 |
|------|------|
| [[pages/papers/sna/2024_neal_methodological_moderators_aver\|Neal (2024)]] | 아동·청소년 우정 네트워크 **71편 메타분석** — 명칭 생성기 방식과 선택 횟수 제한이 outdegree 추정치를 유의하게 좌우 |
| [[pages/papers/sna/2021_tpfer_order_recall_and\|Töpfer 외 (2021)]] | 회상 **순서**와 "친밀함"의 의미가 정서적 네트워크 데이터에 미치는 영향 |
| [[pages/papers/sna/2025_chen_social_isolation_design\|Chen 외 (2025)]] | 대만 조사에서 핵심 네트워크 측정 설계가 **"사회적 고립"을 인위적으로 만들어내는지** 검증 |
| [[pages/papers/sna/2020_feld_egonets_systematically_biased\|Feld 외 (2020)]] | 에고넷은 사회 전체를 보는 **체계적으로 편향된 창** — 구조적으로 불가피한 편향 규명 |
| [[pages/papers/sna/2025_everett_alter_composition_with_overlap\|Everett 외 (2025)]] | 알터가 복수 집단에 중첩 소속될 때의 구성(composition) 지표 계산 |

**시사점**: 동일 집단을 조사해도 질문 설계에 따라 밀도·규모·고립도가 달라진다. 분석 도구가 아무리 정교해도 입력 단계에서 결론이 갈린다.

---

## 2. 알터 수 설계 — 편향 대 응답 부담

| 논문 | 발견 |
|------|------|
| [[pages/papers/sna/2021_stadel_balancing_bias_and_burden\|Stadel & Stulp (2021)]] | 퍼스널 네트워크 연구의 **편향(bias) vs 응답 부담(burden)** 트레이드오프 정량화 |
| [[pages/papers/sna/2020_stulp_collecting_large_personal_netw\|Stulp (2020)]] | 네덜란드 여성 대표 표본에서 **대규모** 퍼스널 네트워크 수집 실행 |
| [[pages/papers/sna/2025_gonzlezcas_collecting_large_number\|González-Casado 외 (2025)]] | 다수 알터 수집 **3가지 접근법 비교** |

고정 알터 수(fixed) vs 가변 알터 수(variable) 설계 논쟁이 핵심이며, 최근에는 정보량 기준(수집 1명당 정보 획득량 최대화)으로 최적 알터 수를 정하려는 접근이 등장했다.

---

## 3. 데이터 수집 도구 (소프트웨어)

에고넷 수집 전용 인터뷰 지원 소프트웨어가 독자적 연구 대상이 되었다.

| 도구 | 논문 | 성격 |
|------|------|------|
| **Network Canvas** | [[pages/papers/sna/2021_birkett_network_canvas_key_decisions\|Birkett 외 (2021)]] | 면접원 보조형 네트워크 데이터 수집 스위트의 설계 결정 |
| **Trellis** | [[pages/papers/sna/2021_lungeanu_using_trellis_software\|Lungeanu 외 (2021)]] | 현장 대규모 고품질 수집 |
| **VINA** | [[pages/papers/sna/2026_nijs_introducing_vina_engaging\|Nijs 외 (2026)]] | 스마트폰 기반, 인지적 사회구조(CSS)까지 수집, 윤리 설계 강조 |
| **GENSI 등 시각적 도구** | [[pages/papers/sna/2020_hollstein_collecting_egocentric_network_\|Hollstein 외 (2020)]] | 시각적 수집 도구 비교 연구 |

> ⚠️ **연결 규칙 (SCHEMA 규칙 3)**: 이 논문들은 **설문·인터뷰 기반 수집** 연구다. NetMiner의 **Extension(SNS/Biblio/News Data Collector)** 과는 무관하다 — 그쪽은 온라인 데이터 크롤링 기능이다. 성립하는 연결은 **"수집 도구 산출물 → NetMiner Ego Network Extract → 에고넷 분석·시각화"** 파이프라인뿐이다.

---

## 4. 회상 편향 · 대리 응답 정확도

| 논문 | 발견 |
|------|------|
| [[pages/papers/sna/2021_stark_predicting_data_quality\|Stark & Krosnick (2021)]] | **대리 응답(proxy report)** 데이터 품질 예측 — 누구에 대한 대리 응답이 정확한가 |
| [[pages/papers/sna/2020_beuthner_effects_smartphone_use\|Beuthner 외 (2020)]] | 스마트폰 응답 환경이 이름 생성기 응답에 미치는 영향 |

---

## 5. 에고넷 **구조 유형 자동 분류** — 학계가 앞서간 지점

최근 흐름은 개별 에고넷을 하나씩 해석하는 대신, **수천 개 에고넷을 구조 패턴별로 자동 분류**하는 것이다. 군집분석·Random Forest 등 ML 기법이 동원된다.

| 논문 | 접근 |
|------|------|
| [[pages/papers/sna/2024_gonzlezcas_towards_general_method\|González-Casado 외 (2024)]] | **퍼스널 네트워크 구조의 일반적 분류 방법** 제안 — 특정 표본에 종속되지 않는 범용 유형 체계 지향 |
| [[pages/papers/sna/2022_laier_inductive_typology\|Laier (2022)]] | 독일 SOEP 패널 데이터 기반 **귀납적 에고넷 유형론** |
| [[pages/papers/sna/2023_kennedy_typologies_duocentric_networks\|Kennedy 외 (2023)]] | 부부 단위(duocentric) 네트워크 유형론 |
| [[pages/papers/sna/2022_mayajarieg_use_hierarchical\|Maya-Jariego & González-Tinoco (2022)]] | 반복적 매개 노드 제거로 에고넷 내 계층적 하위집단 탐색 |
| [[pages/papers/sna/2025_riddell_methods_for_interventions_usin\|Riddell 외 (2025)]] | 네트워크 기반 건강 개입의 수집·시각화·개입 방법론 종합 |

**여기가 NetMiner의 기존 에고넷 기능이 따라가지 못하는 지점이다.** 현재 기능은 "에고 하나를 추출해 지표를 계산"하는 단건 분석이고, 학계는 "N개 에고넷을 구조 유형으로 자동 분류"로 이동했다.

---

## NetMiner 연관성

> 학술 수요와 NetMiner 지원 여부는 분리해 읽을 것 (SCHEMA 규칙 2).

| 구분 | 상태 | 근거 |
|------|:----:|------|
| 에고 네트워크 추출·지표 계산 | ✅ | `Pre-process > Network Transform > Ego Network Extract` ([[pages/tools/netminer\|기능 목록]]) |
| 알터 구성·밀도·동질성 분석, 시각화 | ✅ | 중심성·Network Metric·시각화 메뉴 조합으로 가능 |
| 수집 도구(Network Canvas·Trellis·VINA·GENSI) 산출물 분석 | ✅ (워크플로우) | 수집은 외부 도구, 분석은 NetMiner — 성립하는 파이프라인 |
| 설문·인터뷰 기반 에고넷 **수집** 기능 | ❌ | NetMiner Extension은 온라인 크롤링용. 혼동 금지 |
| **다수 에고넷 일괄 처리 + 구조 유형 자동 분류** | ❌ | 학계 최신 흐름 — 업그레이드 기회 |

### 제품 기획 제안

1. **즉시(비용 0)**: "수집 도구 → NetMiner 분석" 워크플로우 콘텐츠·세미나. 46편이라는 최대 클러스터에 직접 대응하면서 기존 기능만으로 가능하다.
2. **중기(개발)**: **배치 에고넷 분석** — 수백~수천 개 에고넷의 지표를 일괄 산출하고, 군집분석(NetMiner의 Hierarchical Clustering·k-means 보유)으로 **구조 유형을 자동 분류**하는 기능. 필요한 구성요소(Ego Network Extract + 지표 + 군집분석 + Random Forest)가 **이미 모두 NetMiner 안에 있다** — 이들을 잇는 워크플로우/자동화가 없을 뿐이다. 투입 대비 효과가 가장 좋은 업그레이드 후보.
3. **주의**: 데이터 수집 방법론 논문 다수를 근거로 Extension(SNS/Biblio/News Collector)을 홍보하는 연결은 과거 확인된 오류다 — 반복하지 말 것.

## 위키 연관

- [[pages/concepts/personal_network|퍼스널 네트워크]] (개념 정의)
- [[pages/insights/sna_method_frequency|방법론 빈도 분석 (318편 전수)]]
- [[pages/methods/network_scaleup|Network Scale-Up / ARD]] (동일한 "측정 방법론" 흐름)
- [[pages/methods/centrality|중심성 분석]] (명칭 생성기 설계가 중심성 추정치를 왜곡)
- [[pages/methods/ml|머신러닝]] (에고넷 유형 자동 분류)
- [[pages/insights/netminer_trend_insight|NetMiner 기능-트렌드 인사이트]]
- [[pages/tools/netminer|NetMiner]]
