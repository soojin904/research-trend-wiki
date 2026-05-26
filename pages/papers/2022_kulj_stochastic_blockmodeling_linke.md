---
title: "Stochastic blockmodeling of linked networks"
authors: ['Damjan Škulj', 'Aleš Žiberna']
year: 2022
venue: "Social Networks"
tags: ['Complex Network Analysis Techniques', 'Statistical Methods and Bayesian Inference']
source: raw/2022_openalex_Stochastic_blockmodeling_of_linked_networks_j_socnet_2022_02_001.md
---

# Stochastic blockmodeling of linked networks
**제목(한글)**: 연결 네트워크의 확률적 블록모델링

**저자**: Damjan Škulj; Aleš Žiberna
**출처**: Social Networks, Vol.70, pp.240–252
**발행일**: 2022-02-19
**DOI**: https://doi.org/10.1016/j.socnet.2022.02.001


## 한국어 요약

**연구질문**: 서로 다른 유형의 노드 집합이 연결된 복합 네트워크(linked network)에서 두 집합을 동시에 군집화하는 확률적 블록모델링 방법을 어떻게 개발하고 그 성능을 향상시킬 수 있는가?

**방법론**:
- 혼합 모델(mixture model) 기반 확률적 블록모델링(stochastic blockmodeling) 적용
- CEM 알고리즘으로 우도 함수를 최대화하며 반복 추정
- 데이터 불균형 보완을 위한 가중 우도(weighted likelihood) 방법 제안
- 시뮬레이션을 통한 접근법 성능 비교 평가

**주요 결과**:
- 기본 알고리즘은 큰 부분 집합에 과도한 영향을 부여하는 비대칭 문제가 있음
- 가중 우도 접근법은 대규모 네트워크와 명확한 블록 구조에서 성능이 더 우수함
- 소규모 집합의 블록 구조가 더 명확할수록 가중 방법의 이점이 두드러짐


## 초록 (원문)

Blockmodeling linked networks aims to simultaneously cluster two or more sets of units into clusters based on a network where ties are possible both between units from the same set as well as between units of different sets. While this has already been developed for generalized and k-means blockmodeling, our approach is based on the well-known stochastic blockmodeling technique, utilizing a mixture model. Estimation is performed using the CEM algorithm, which iteratively estimates the parameters by maximizing a suitable likelihood function and reclusters the units according to the parameters. The steps are repeated until the likelihood function ceases to improve. A key drawback of the basic algorithm is that it treats all units equally, consequently yielding higher influence to larger parts of the data. The greater size, however, does not necessarily imply higher importance. To mitigate this asymmetry, we propose a solution where underrepresented parts of the data are given more influence through an appropriate weighting. This idea leads to the so-called weighted likelihood approach, where the ordinary likelihood function is replaced by a weighted likelihood. The efficiency of the different approaches is tested via simulations. It is shown through simulations that the weighted likelihood approach performs better for larger networks and a clearer blockmodel structure, especially when the one-mode blockmodels within the smaller sets are clearer.

## 키워드

Weighting, Function (biology), Set (abstract data type), Computer science, Likelihood function, Stochastic block model, Algorithm, Data mining

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

