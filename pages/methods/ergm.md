---
title: "ERGM (지수 랜덤 그래프 모형)"
tags: [ergm, stergm, ergmito, statistical-network-model, exponential-random-graph]
netminer_support: "✅ 지원 (기본 ERGM; 변형은 부분 지원)"
---

# 지수 랜덤 그래프 모형 (Exponential Random Graph Model, ERGM)

관찰된 네트워크 구조가 어떤 사회적 과정에 의해 형성되었는지를 통계적으로 추정하는 모형. SNA 학술지 2020–2026 논문에서 26편이 활용하여 3위를 차지하는 핵심 통계 방법론이다. ERGM + SAOM 합산 44편으로 SNA 논문의 표준 통계 도구로 확고한 위치를 차지한다.

## 핵심 개념

관찰된 네트워크 $y$가 특정 충분통계량(sufficient statistics) 집합을 가질 확률을 지수족 분포로 모델링한다. 주요 충분통계량:
- **상호성(reciprocity)**: 방향 네트워크에서 쌍방 유대 형성 경향
- **동종 선호(homophily)**: 유사 속성 노드 간 연결 선호
- **삼각 관계(transitivity)**: 공통 친구가 있는 노드들의 연결 경향
- **인기도(popularity)**: 고차수 노드 선호 (preferential attachment)

### 변형 모형

| 변형 | 적용 맥락 | 도구 |
|------|-----------|------|
| **기본 ERGM** | 단일 시점 네트워크 | R statnet, NetMiner |
| **STERGM** | 유대 형성·소멸을 분리 모델링 (종단) | R statnet |
| **ergmito** | 소규모 네트워크(ego net 등)에 MLE 적용 | R ergmito |
| **Bayesian hierarchical ERGM** | 다중 소집단 동시 분석 | R |
| **Mixed ERGM** | 노드 수준 이질성(random effects) 포함 | R |

## 실제 사용 패턴 (SNA 학술지 논문 기반)

| 논문 | 적용 방식 | 핵심 발견 |
|------|-----------|-----------|
| [[pages/papers/2021_ingold_the_roles_actors_play\|Ingold 외 (2021)]] | t1 중심성을 독립변수로 포함한 ERGM으로 t2 행위자 활동성·인기도 예측 | 소수 행위자만 시간에 걸쳐 중심 위치 유지; 국가 기관이 이익집단보다 안정적 |
| [[pages/papers/2022_agneessens_network_formation_organization\|Agneessens 외 (2022)]] | 베이지안 계층적 ERGM으로 다중 소집단 네트워크 동시 분석 | 상호성·동종 선호가 소집단 네트워크 형성에 핵심; 팀 수준 맥락 변수 추가 효과 확인 |
| [[pages/papers/2022_bohnett_resilience_and_fragmentation\|Bohnett 외 (2022)]] | ERGM으로 의료 연합 조직 간 네트워크에서 자원 기여 → 중심성 예측 | 자원 기여도 높은 조직이 더 중심적 위치 차지 |
| [[pages/papers/2024_pattison_exponential_random_graph_model\|Pattison 외 (2024)]] | 의존 구조 위계 프레임워크에 펜던트 삼각형 통계량 추가 | 경계·교량 형성 과정 모델링에서 모형 적합도 현저히 개선 |

## NetMiner 지원 현황

✅ 기본 ERGM 지원 — 주요 네트워크 통계량(상호성, 동종 선호, 삼각 관계 등) 포함 모형 추정 가능.

⚠️ 변형 미지원 — STERGM, ergmito, Bayesian hierarchical ERGM 등 변형 모형은 NetMiner 미지원.
- **대안**: R `statnet` 패키지 (ERGM, STERGM), `ergmito` 패키지, `Bergm` 패키지 (Bayesian)

**시사점**: NetMiner의 기본 ERGM 기능 홍보가 가능하나, 변형 모형 수요(26편 중 STERGM·ergmito 포함 사례 다수)를 충족하려면 R 연계 워크플로우 콘텐츠 필요.

## 위키 연관

- [[pages/insights/sna_method_frequency|방법론 빈도 분석]]
- [[pages/methods/saom|SAOM / RSiena]] (경쟁·보완 관계의 종단 통계 모형)
- [[pages/methods/longitudinal_network|종단/동적 네트워크]] (STERGM이 이 범주에 속함)
- [[pages/methods/bayesian_network_model|Bayesian/잠재공간 모델]] (Bayesian ERGM 변형과 연결)
- [[pages/tools/other_tools|Other Tools (ERGM·SAOM 지원 도구)]]
