---
title: "Improving ERGM starting values using simulated annealing"
authors: ['Christian S. Schmid', 'David R. Hunter']
year: 2023
venue: "Social Networks"
tags: ['Bayesian Modeling and Causal Inference', 'Complex Network Analysis Techniques', 'Statistical Methods and Inference']
source: raw/2023_openalex_Improving_ERGM_starting_values_using_simulated_j_socnet_2023_10_002.md
---

# Improving ERGM starting values using simulated annealing
**제목(한글)**: 시뮬레이티드 어닐링을 이용한 ERGM 초기값 개선

**저자**: Christian S. Schmid; David R. Hunter
**출처**: Social Networks, Vol.76, pp.209–214
**발행일**: 2023-11-07
**DOI**: https://doi.org/10.1016/j.socnet.2023.10.002


## 한국어 요약

**연구질문**: ERGM의 최대우도 추정(MLE) 근사 알고리즘의 초기값을 개선하여 수렴 실패 문제를 해결할 수 있는가?

**방법론**:
- MPLE(최대 의사우도 추정)의 "가능성 원리" 위반을 활용한 초기값 탐색
- 시뮬레이티드 어닐링(simulated annealing) 기법으로 개선된 초기값 탐색
- 기존 방법으로 추정 실패했던 네트워크 데이터에 적용 검증

**주요 결과**:
- 시뮬레이티드 어닐링 기반 초기값이 기존 MPLE보다 우수한 수렴 성능 제공
- 기존의 모든 방법으로 추정 불가했던 네트워크 모형 추정 성공
- ERGM 추정의 수렴 실패 문제에 대한 실용적 해결책 제시


## 초록 (원문)

Much of the theory of estimation for exponential family models, which include exponential-family random graph models (ERGMs) as a special case, is well-established and maximum likelihood estimates (MLEs) in particular enjoy many desirable properties. However, in the case of many ERGMs, direct calculation of MLEs is impossible and therefore methods for approximating MLEs and/or alternative estimation methods must be employed. Many MLE approximation algorithms require an alternative estimate as a starting point. The maximum pseudo-likelihood estimator (MPLE) is frequently taken as this starting point. Here, we discuss a potentially large class of such alternatives based on the fact that, unlike the MLE, the MPLE fails to satisfy the so-called “likelihood principle”. This means that different networks may have different MPLEs even if they have the same sufficient statistics. We exploit this fact here to search for improved starting values for approximation-based MLE methods. The method we propose has shown its merit in producing an MLE for a network dataset and model that had defied estimation using all other known methods.

## 키워드

Exponential family, Estimator, Mathematics, Exponential random graph models, Maximum likelihood, Quasi-maximum likelihood, Simulated annealing, Mathematical optimization

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

