---
title: "A zero-inflated Poisson latent position cluster model"
authors: ['Chaoyi Lu', 'Riccardo Rastelli', 'Nial Friel']
year: 2026
venue: "Network Science"
tags: ['Bayesian Methods and Mixture Models', 'Complex Network Analysis Techniques', 'Data Visualization and Analytics']
source: raw/2026_openalex_A_zeroinflated_Poisson_latent_position_cluster_nws_2025_10021.md
---

# A zero-inflated Poisson latent position cluster model

**제목(한글)**: 영 과잉 포아송 잠재 위치 군집 모델

**저자**: Chaoyi Lu; Riccardo Rastelli; Nial Friel
**출처**: Network Science, Vol.14
**발행일**: 2026-01-01
**DOI**: https://doi.org/10.1017/nws.2025.10021

## 한국어 요약

**연구질문**: 결측 네트워크 데이터와 비음수 정수 가중치를 가진 소셜 네트워크를 동시에 처리하는 잠재 공간 군집 모델을 어떻게 구성할 수 있는가?

**방법론**:
- 잠재 위치 군집 모델(LPCM)에 영 과잉 포아송(Zero-Inflated Poisson) 분포를 결합한 확장 모델 제안
- 부분 붕괴 마르코프 체인 몬테카를로(MCMC) 알고리즘으로 사후 추론 수행
- 유한 혼합의 혼합(Mixture-of-Finite-Mixtures, MFM) 모델로 군집 수를 자동 결정
- 3차원 잠재 공간을 이용해 2차원보다 유연한 시각화 제공

**주요 결과**:
- 결측 데이터를 "비정상적 영 상호작용"으로 처리하여 가중 네트워크의 군집 구조 회복
- 절단 흡수-배출 이동(truncated absorb-eject move)이 MFM 샘플러의 효율을 크게 향상
- 4개 실제 네트워크 데이터에서 흥미로운 새로운 구조적 패턴 발견

## 초록 (원문)

Abstract The Latent Position Model (LPM) is a popular approach for the statistical analysis of network data. A central aspect of this model is that it assigns nodes to random positions in a latent space, such that the probability of an interaction between each pair of individuals or nodes is determined by their distance in this latent space. A key feature of this model is that it allows one to visualize nuanced structures via the latent space representation. The LPM can be further extended to the Latent Position Cluster Model (LPCM), to accommodate the clustering of nodes by assuming that the latent positions are distributed following a finite mixture distribution. In this paper, we extend the LPCM to accommodate missing network data and apply this to non-negative discrete weighted social networks. By treating missing data as “unusual” zero interactions, we propose a combination of the LPCM with the zero-inflated Poisson distribution. Statistical inference is based on a novel partially collapsed Markov chain Monte Carlo algorithm, where a Mixture-of-Finite-Mixtures (MFM) model is adopted to automatically determine the number of clusters and optimal group partitioning. Our algorithm features a truncated absorb-eject move, which is a novel adaptation of an idea commonly used in collapsed samplers, within the context of MFMs. Another aspect of our work is that we illustrate our results on 3-dimensional latent spaces, maintaining clear visualizations while achieving more flexibility than 2-dimensional models. The performance of this approach is illustrated via three carefully designed simulation studies, as well as four different publicly available real networks, where some interesting new perspectives are uncovered.

## 키워드

Cluster analysis, Probabilistic latent semantic analysis, Inference, Mixture model, Statistical inference, Markov chain Monte Carlo, Latent class model, Markov chain

## 위키 연관

- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모

