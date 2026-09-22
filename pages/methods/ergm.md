---
title: "ERGM (지수 랜덤 그래프 모형)"
tags: [ergm, dergm, ernm, tergm, bipartite-ergm, statistical-network-model, exponential-random-graph]
netminer_support: "⚠️ 부분 (기본 ERGM ✅ / 변형 모형 ❌)"
updated: 2026-09-22
---

# 지수 랜덤 그래프 모형 (Exponential Random Graph Model, ERGM)

관찰된 네트워크 구조가 어떤 사회적 과정에 의해 형성되었는지를 통계적으로 추정하는 모형.
**SNA 전문 학술지 전수 318편 중 40편(2위)** 이 활용하는 핵심 통계 방법론이다 ([[pages/insights/sna_method_frequency|방법론 빈도 분석]], 2026-09-22 기준).
ERGM(40) + [[pages/methods/saom|SAOM]](29) + [[pages/methods/relational_event_model|REM]](17) = **86편**으로, 생성적·통계적 네트워크 모형이 SNA 학술지 방법론의 주류를 형성한다.

## 핵심 개념

관찰된 네트워크 $y$가 특정 충분통계량(sufficient statistics) 집합을 가질 확률을 지수족 분포로 모델링한다. 주요 충분통계량:
- **상호성(reciprocity)**: 방향 네트워크에서 쌍방 유대 형성 경향
- **동종 선호(homophily)**: 유사 속성 노드 간 연결 선호
- **삼각 관계(transitivity)**: 공통 친구가 있는 노드들의 연결 경향
- **인기도(popularity)**: 고차수 노드 선호 (preferential attachment)

## 변형 모형 계열 (318편 전수에서 확인)

ERGM은 이제 단일 모형이 아니라 **적용 맥락별로 분화한 모형 계열**이다.

| 변형 | 해결하는 문제 | 대표 논문 | 도구 |
|------|--------------|-----------|------|
| **기본 ERGM** | 단일 시점 네트워크 | [[pages/papers/sna/2024_pattison_exponential_random_graph_model\|Pattison 외 (2024)]] | R statnet, **NetMiner** |
| **DERGM** (degeneracy-restricted) | ERGM의 고질적 퇴화(degeneracy) 문제를 모수 공간 제약으로 해결 | [[pages/papers/sna/2022_karwa_dergms_degeneracyrestricted_ex\|Karwa 외 (2022)]] | R |
| **Bipartite ERGM + nodal random effects** | 2-mode(행위자-사건) 네트워크, 노드 이질성 | [[pages/papers/sna/2021_kevork_bipartite_exponential_random_g\|Kevork & Kauermann (2021)]] | R |
| **Count-valued ERGM** | 이진 유대가 아닌 **빈도·가중치** 네트워크 | [[pages/papers/sna/2023_huang_parameter_estimation_procedure\|Huang 외 (2023)]] | R ergm.count |
| **ERNM** (Exponential-family Random *Network* Model) | 유대와 **노드 속성을 동시에** 내생 변수로 모델링 | [[pages/papers/sna/2023_wang_understanding_networks_with_ex\|Wang 외 (2023)]] | R ernm |
| **Multilevel ERGM** | 조직-개인 등 다수준 네트워크 | [[pages/papers/sna/2024_broccatell_multilevel_integrated_healthca\|Broccatelli 외 (2024)]], [[pages/papers/sna/2023_koskinen_analysing_networks_networks\|Koskinen (2023)]] | R MPNet/statnet |
| **Bayesian hierarchical ERGM** | 다중 소집단 동시 분석 | [[pages/papers/sna/2022_agneessens_network_formation_organization\|Agneessens 외 (2022)]] | R Bergm |
| **TERGM / STERGM** | 종단 — 유대 형성·소멸 분리 | (SAOM 비교 논쟁 참조) | R statnet/btergm |
| **ergmito** | 소규모 네트워크(에고넷 등) 정확 MLE | — | R ergmito |

> **TERGM vs SAOM 비교 인용 시 주의**: Leifeld & Cranmer (2019)의 TERGM–SAOM 경험적 비교는 [[pages/papers/sna/2022_block_circular_specifications_and_pr\|Block 외 (2022)]]가 **순환 논법(circular specification, 미래 정보로 "예측")** 이라고 반박했고, [[pages/papers/sna/2022_leifeld_theoretical_and_empirical\|Leifeld & Cranmer (2022) Corrigendum]]이 뒤따랐다. "TERGM이 SAOM보다 예측력이 좋다"는 식의 단정적 인용은 금지.

## 실제 사용 패턴 (SNA 학술지 논문 기반)

| 논문 | 적용 방식 | 핵심 발견 |
|------|-----------|-----------|
| [[pages/papers/sna/2021_ingold_the_roles_actors_play\|Ingold 외 (2021)]] | t1 중심성을 독립변수로 포함한 ERGM으로 t2 활동성·인기도 예측 | 소수 행위자만 중심 위치 유지; 국가 기관이 이익집단보다 안정적 |
| [[pages/papers/sna/2022_agneessens_network_formation_organization\|Agneessens 외 (2022)]] | 베이지안 계층적 ERGM으로 다중 소집단 네트워크 동시 분석 | 상호성·동종 선호가 핵심; 팀 수준 맥락 변수 추가 효과 확인 |
| [[pages/papers/sna/2024_pattison_exponential_random_graph_model\|Pattison 외 (2024)]] | 의존 구조 위계에 펜던트 삼각형 통계량 추가 | 경계·교량 형성 모델링에서 적합도 현저히 개선 |
| [[pages/papers/sna/2023_wang_understanding_networks_with_ex\|Wang 외 (2023)]] | ERNM — 네트워크와 노드 속성의 공동 분포를 하나의 지수족으로 추정 | 선택(selection)과 영향(influence)을 단일 틀에서 분리 |
| [[pages/papers/sna/2022_karwa_dergms_degeneracyrestricted_ex\|Karwa 외 (2022)]] | 퇴화 문제를 구조적으로 배제한 모수 공간 제약 | 기존 ERGM 추정 실패 사례에서 안정적 수렴 |

## NetMiner 지원 현황

**✅ 지원 — 기본 ERGM**
`Network > Models > ERGM` 메뉴 존재. 상호성·동종 선호·삼각 관계 등 주요 네트워크 통계량 기반 모형 추정 가능 ([[pages/tools/netminer|NetMiner 기능 목록]] 확인).

**❌ 미지원 — 변형 모형 전체**
DERGM, bipartite ERGM(NetMiner의 Two-Mode 메뉴는 중심성 산출만 제공, ERGM 연계 없음), count-valued ERGM, ERNM, multilevel ERGM, Bayesian ERGM, TERGM/STERGM, ergmito 모두 미지원.
- **대안**: R `statnet`(ERGM/TERGM), `ergm.count`, `Bergm`, `ernm`, `ergmito`, MPNet(다수준)

### 제품 기획 시사점 (학술 수요 ≠ 지원 여부 분리)

- **학술 수요**: ERGM 계열 40편으로 2위. 그중 상당수가 **변형 모형**이다 — 기본 ERGM만으로 커버되는 범위는 절반 이하로 봐야 한다.
- **NetMiner 지원**: 기본 ERGM은 이미 있다. 문제는 (1) 지원 사실 자체가 시장에 알려지지 않았고, (2) 변형 수요를 못 받는다는 두 가지다.
- **우선순위 제안**: ① 기본 ERGM 지원 사실 홍보(즉시, 비용 0) → ② 가중치/빈도 네트워크(count-valued)와 이분 네트워크 ERGM 확장 검토(NetMiner가 이미 Two-Mode 자료구조를 다루므로 진입 비용이 상대적으로 낮음) → ③ 다수준·Bayesian은 R 연계 가이드로 대응.

## 위키 연관

- [[pages/insights/sna_method_frequency|방법론 빈도 분석 (318편 전수)]]
- [[pages/methods/saom|SAOM / RSiena]] (경쟁·보완 관계의 종단 통계 모형)
- [[pages/methods/relational_event_model|관계 사건 모형 (REM)]] (이벤트 단위 동적 모형)
- [[pages/methods/longitudinal_network|종단/동적 네트워크]] (TERGM/STERGM이 속하는 범주)
- [[pages/methods/bayesian_network_model|Bayesian/잠재공간 모델]]
- [[pages/concepts/multilayer_network|다층 네트워크]] (multilevel ERGM)
- [[pages/tools/netminer|NetMiner]]
- [[pages/tools/other_tools|Other Tools (ERGM·SAOM 지원 도구)]]
