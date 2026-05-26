---
title: "Bayesian / 잠재공간 모델 (Bayesian & Latent Space Models)"
tags: [bayesian, latent-space, mcmc, latent-position, mixture-model, probabilistic]
netminer_support: "❌ 미지원"
---

# Bayesian / 잠재공간 모델 (Bayesian & Latent Space Models)

네트워크 데이터에 확률론적 추론을 적용하는 통계 모형 범주. 관찰되지 않는 잠재 구조(노드의 위치, 군집 소속)를 MCMC 등으로 추정한다. SNA 학술지 2020–2026에서 14편이 활용하여 9위를 기록했다.

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

## 실제 사용 패턴 (SNA 학술지 논문 기반)

| 논문 | 적용 방식 | 핵심 발견 |
|------|-----------|-----------|
| [[pages/papers/2026_lu_zeroinflated_poisson_latent\|Lu 외 (2026)]] | 결측 데이터+가중치 동시 처리하는 Zero-Inflated Poisson LPCM에 MFM + 부분 붕괴 MCMC 적용 | 절단 absorb-eject 이동이 MFM 샘플러 효율 대폭 향상; 군집 수 자동 결정 |
| [[pages/papers/2025_gwee_modelbased_clustering_for_netw\|Gwee 외 (2025)]] | LSPCM으로 잠재 공간 차원수와 군집 수 동시 자동 추론 — Twitter 네트워크 적용 | 모형 비교 없이 최적 차원과 군집 수 추론 가능; 스포츠·정치 맥락 검증 |
| [[pages/papers/2023_rastelli_continuous_latent_position_mod\|Rastelli & Corneli (2023)]] | 노드가 잠재 공간에서 연속 이동하는 궤적 모형으로 이메일·전화 순간 상호작용 분석 | 타이밍·빈도 동시 모형화; 동적 네트워크 분석의 연속 시간 확장 |
| [[pages/papers/2022_agneessens_network_formation_organization\|Agneessens 외 (2022)]] | 베이지안 계층적 ERGM으로 다중 소집단 조직 네트워크 동시 분석 | 팀 수준 맥락 변수와 개인 수준 과정의 동시 추정 |

## NetMiner 지원 현황

❌ 미지원 — NetMiner는 잠재 공간 모형, Bayesian ERGM, MCMC 기반 네트워크 모형을 지원하지 않는다.

**대안 도구**:
- R `latentnet` 패키지 (LPCM, LSM)
- R `Bergm` 패키지 (Bayesian ERGM)
- R `lsm` 패키지
- Python `pymc`, `stan` (범용 베이지안 추론)

**시사점**: 방법론적 정교화를 추구하는 고급 연구자 수요. 시각화 결과(잠재 공간 플롯)는 직관적이어서 콘텐츠 활용 가능성 있음.

## 위키 연관

- [[pages/insights/sna_method_frequency|방법론 빈도 분석]]
- [[pages/methods/ergm|ERGM]] (Bayesian ERGM 변형)
- [[pages/methods/community_detection|커뮤니티 탐지]] (잠재 공간 군집화와 연결)
- [[pages/methods/ml_gnn|ML/딥러닝/GNN]] (임베딩 방법론과의 경계)
- [[pages/tools/other_tools|Other Tools (ERGM·SAOM 지원 도구)]]
