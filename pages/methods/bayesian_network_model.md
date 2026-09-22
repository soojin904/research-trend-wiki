---
title: "Bayesian / 잠재공간 모델 (Bayesian & Latent Space Models)"
tags: [bayesian, latent-space, mcmc, latent-position, mixture-model, probabilistic]
netminer_support: "❌ 미지원"
updated: 2026-09-22
---

# Bayesian / 잠재공간 모델 (Bayesian & Latent Space Models)

네트워크 데이터에 확률론적 추론을 적용하는 통계 모형 범주. 관찰되지 않는 잠재 구조(노드의 위치, 군집 소속)를 MCMC 등으로 추정한다. **SNA 전문 학술지 전수 318편 중 6편 이상**이 잠재공간 모형 자체를 주제로 다루며, Bayesian ERGM·Bayesian REM·Bayesian ARD 등 다른 클러스터에 흡수된 사례까지 합치면 범위는 더 넓다 ([[pages/insights/sna_method_frequency|방법론 빈도 분석]], 2026-09-22 기준).

> **2026-09-22 갱신의 핵심**: 잠재공간 모형이 단독 기법에서 **다른 문제를 푸는 공통 인프라**로 확장되고 있다 — 매개(mediation) 분석, 결측 데이터 처리, 텐서/다층 구조, 인지적 사회구조 추정.

## 핵심 개념

### 잠재 공간 모형 (Latent Space Model, LSM)

각 노드를 저차원 유클리드 공간에 임베딩하고, 두 노드 간 연결 확률을 잠재 공간 거리의 함수로 모델링한다:

$$P(y_{ij}=1) = \text{logit}^{-1}(\alpha - ||z_i - z_j||)$$

- **직관**: 잠재 공간에서 가까운 노드일수록 연결 확률 높음
- **군집화**: 잠재 위치를 혼합 모형(GMM 등)으로 클러스터링 → 커뮤니티 탐지와 연결
- **MCMC 추론**: 사후 분포에서 노드 위치와 군집 소속 동시 추정

### 변형 모형

| 모형 | 특징 |
|------|------|
| **LPCM** (Latent Position Cluster Model) | 혼합 분포로 노드 군집화 동시 추정 |
| **LSPCM** (Latent Shrinkage Position Cluster Model) | 잠재 공간 차원수 자동 결정 (무한 차원 + 수축 사전분포) |
| **Zero-Inflated Poisson LPCM** | 결측 네트워크 + 가중치 동시 처리 |
| **Continuous LSM** | 연속 시간 순간 상호작용 모형화 |
| **Bayesian hierarchical ERGM** | ERGM에 베이지안 추론 적용 |
| **계층적 잠재공간 매개 모형** | 네트워크를 매개변수로 두는 mediation 분석 |
| **교환가능 잠재오차 프로빗 회귀** | 이진 네트워크 회귀에서 이자 간 의존성을 잠재 오차로 흡수 |
| **결측 데이터 잠재공간 모형** | 결측 메커니즘별 처리 방식이 추정에 미치는 영향 |
| **텐서/다층 잠재 구조 (NNTuck 계열)** | 다층 네트워크의 레이어 간 공유 구조를 분해 |

## 실제 사용 패턴 (SNA 학술지 논문 기반)

| 논문 | 적용 방식 | 핵심 발견 |
|------|-----------|-----------|
| [[pages/papers/sna/2026_lu_zeroinflated_poisson_latent\|Lu 외 (2026)]] | 결측 데이터+가중치 동시 처리하는 Zero-Inflated Poisson LPCM에 MFM + 부분 붕괴 MCMC 적용 | 절단 absorb-eject 이동이 MFM 샘플러 효율 대폭 향상; 군집 수 자동 결정 |
| [[pages/papers/sna/2025_gwee_modelbased_clustering_for_netw\|Gwee 외 (2025)]] | LSPCM으로 잠재 공간 차원수와 군집 수 동시 자동 추론 — Twitter 네트워크 적용 | 모형 비교 없이 최적 차원과 군집 수 추론 가능; 스포츠·정치 맥락 검증 |
| [[pages/papers/sna/2023_rastelli_continuous_latent_position_mod\|Rastelli & Corneli (2023)]] | 노드가 잠재 공간에서 연속 이동하는 궤적 모형으로 이메일·전화 순간 상호작용 분석 | 타이밍·빈도 동시 모형화; 동적 네트워크 분석의 연속 시간 확장 |
| [[pages/papers/sna/2022_agneessens_network_formation_organization\|Agneessens 외 (2022)]] | 베이지안 계층적 ERGM으로 다중 소집단 조직 네트워크 동시 분석 | 팀 수준 맥락 변수와 개인 수준 과정의 동시 추정 |
| [[pages/papers/sna/2022_sweet_hierarchical_latent_space\|Sweet & Adhikari (2022)]] | **계층적 잠재공간 네트워크 모형으로 매개(mediation) 분석** | 네트워크 구조 자체를 매개 경로로 모형화 |
| [[pages/papers/sna/2026_sweet_investigating_the_impacts\|Sweet 외 (2026)]] | 잠재공간 모형에서 **결측 메커니즘·처리 방법**의 영향 검증 | 결측 처리 선택이 잠재 위치 추정을 체계적으로 왜곡 |
| [[pages/papers/sna/2023_marrs_regression_binary_network\|Marrs 외 (2023)]] | **교환가능 잠재 오차**를 갖는 이진 네트워크 프로빗 회귀 | 이자 의존성을 무시한 회귀의 표준오차 과소 추정 교정 |
| [[pages/papers/sna/2024_aguiar_the_latent_cognitive_structure\|Aguiar 외 (2024)]] | 인지적 사회구조(CSS)의 잠재 구조를 텐서 분해 계열로 추정 | 응답자별 인식 차이를 잠재 레이어로 분리 |
| [[pages/papers/sna/2024_pham_automated_detection_edge\|Pham 외 (2024)]] | 과적합 혼합 사전분포로 **엣지 군집 자동 탐지** | 군집 수 사전 지정 없이 추론 |

## NetMiner 지원 현황

❌ 미지원 — NetMiner는 잠재 공간 모형, Bayesian ERGM, MCMC 기반 네트워크 모형을 지원하지 않는다.

**대안 도구**:
- R `latentnet` 패키지 (LPCM, LSM)
- R `Bergm` 패키지 (Bayesian ERGM)
- R `lsm` 패키지
- Python `pymc`, `stan` (범용 베이지안 추론)

**시사점 (학술 수요 ≠ 지원 여부 분리)**: 학술 수요는 편수 자체보다 **파급 범위**로 봐야 한다 — 잠재공간·베이지안 추론은 ERGM·REM·ARD·커뮤니티 탐지 등 다른 클러스터에 인프라로 스며들고 있다. NetMiner 지원은 전무하며, MCMC 엔진이 필요해 단기 대응은 비현실적이다. 다만 **잠재공간 플롯**은 시각적으로 직관적이어서, 자체 구현 없이도 "R 결과를 NetMiner로 시각화" 형태의 콘텐츠 소재로 활용할 수 있다.

## 위키 연관

- [[pages/insights/sna_method_frequency|방법론 빈도 분석 (318편 전수)]]
- [[pages/methods/relational_event_model|관계 사건 모형 (REM)]] (Bayesian 정규화 REM)
- [[pages/methods/network_scaleup|Network Scale-Up / ARD]] (Bayesian ARD 통합 프레임워크)
- [[pages/methods/ergm|ERGM]] (Bayesian ERGM 변형)
- [[pages/methods/community_detection|커뮤니티 탐지]] (잠재 공간 군집화와 연결)
- [[pages/methods/gnn|GNN]] (임베딩 방법론과의 경계)
- [[pages/methods/ml|전통 ML]] (분류·회귀 방법론과의 경계)
- [[pages/tools/other_tools|Other Tools (ERGM·SAOM 지원 도구)]]
