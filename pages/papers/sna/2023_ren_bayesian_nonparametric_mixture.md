---
title: "Bayesian nonparametric mixtures of Exponential Random Graph Models for ensembles of networks"
authors: ['Sa Ren', 'Xue Wang', 'Peng Liu', 'Jian Zhang']
year: 2023
venue: "Social Networks"
tags: ['Bayesian Methods and Mixture Models', 'Complex Network Analysis Techniques', 'Markov Chains and Monte Carlo Methods']
source: raw/2023_openalex_Bayesian_nonparametric_mixtures_of_Exponential_Random_j_socnet_2023_03_005.md
---

# Bayesian nonparametric mixtures of Exponential Random Graph Models for ensembles of networks
**제목(한글)**: 네트워크 앙상블을 위한 ERGM의 베이지안 비모수 혼합 모형

**저자**: Sa Ren; Xue Wang; Peng Liu; Jian Zhang
**출처**: Social Networks, Vol.74, pp.156–165
**발행일**: 2023-03-28
**DOI**: https://doi.org/10.1016/j.socnet.2023.03.005


## 한국어 요약

**연구질문**: 다수의 독립적 네트워크 앙상블을 동시에 모델링하여 클러스터를 자동 탐지하는 방법론을 어떻게 개발할 수 있는가?

**방법론**:
- 디리클레 프로세스 혼합 ERGM(DPM-ERGM) 제안
- 디리클레 프로세스로 클러스터 수를 자동 결정
- Metropolis-within-slice 샘플링 알고리즘으로 베이지안 추론 수행
- 시뮬레이션 및 실제 데이터로 성능 검증

**주요 결과**:
- 클러스터 수 사전 지정 없이 네트워크 앙상블을 자동 군집화 가능
- 추적 불가능한 ERGM에서도 완전 베이지안 추론 구현
- 학급 학생 네트워크 등 실제 앙상블 데이터에 적용 가능성 확인


## 초록 (원문)

Ensembles of networks arise in various fields where multiple independent networks are observed, for example, a collection of student networks from different classes. However, there are few models that describe both the variations and characteristics of networks in an ensemble at the same time. In this manuscript, we propose to model ensembles of networks using a Dirichlet Process Mixture of Exponential Random Graph Models (DPM-ERGMs), which divides an ensemble into different clusters and models each cluster of networks using a separate Exponential Random Graph Model (ERGM). By employing a Dirichlet process mixture, the number of clusters can be determined automatically and changed adaptively with the data provided. Moreover, in order to perform full Bayesian inference for DPM-ERGMs, we develop a Metropolis-within-slice sampling algorithm to address the problem of sampling from the intractable ERGMs on an infinite sample space. We also demonstrate the performance of DPM-ERGMs with both simulated and real datasets.

## 키워드

Exponential random graph models, Dirichlet process, Inference, Computer science, Dirichlet distribution, Random graph, Hierarchical Dirichlet process, Bayesian probability

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

