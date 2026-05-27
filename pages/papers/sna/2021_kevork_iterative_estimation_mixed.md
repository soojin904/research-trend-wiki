---
title: "Iterative estimation of mixed exponential random graph models with nodal random effects"
authors: ['Sevag Kevork', 'Göran Kauermann']
year: 2021
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'Bayesian Modeling and Causal Inference', 'Advanced Graph Neural Networks']
source: raw/2021_openalex_Iterative_estimation_of_mixed_exponential_random_nws_2021_22.md
---

# Iterative estimation of mixed exponential random graph models with nodal random effects
**제목(한글)**: 노드 무작위 효과를 포함한 혼합 지수 랜덤 그래프 모델의 반복 추정

**저자**: Sevag Kevork; Göran Kauermann
**출처**: Network Science, Vol.9, pp.478–498
**발행일**: 2021-12-01
**DOI**: https://doi.org/10.1017/nws.2021.22

## 한국어 요약

**연구질문**: 지수 랜덤 그래프 모델(ERGM)에서 노드 수준의 관측되지 않은 이질성(unobserved heterogeneity)을 무작위 효과로 포함할 때, 안정적이고 효율적인 추정 방법을 어떻게 개발할 수 있는가?

**방법론**:
- 노드별 무작위 효과를 포함한 혼합 ERGM(mixed ERGM) 모델 제안
- 무작위 효과: 근사 유사가능도(approximate pseudolikelihood) 추정, 나머지 파라미터: 최대가능도(maximum likelihood) 추정을 반복 적용
- 아카이케 정보 기준(AIC)을 활용한 모델 선택

**주요 결과**:
- 반복 추정 알고리즘이 안정적으로 수렴하며 대규모 네트워크에도 적용 가능
- 노드 이질성 효과 통제로 모델 타당성 및 추정 안정성 향상
- AIC 기반 모델 선택으로 노드 이질성 유무 검정 가능

## 초록 (원문)

Abstract The presence of unobserved node-specific heterogeneity in exponential random graph models (ERGM) is a general concern, both with respect to model validity as well as estimation instability. We, therefore, include node-specific random effects in the ERGM that account for unobserved heterogeneity in the network. This leads to a mixed model with parametric as well as random coefficients, labelled as mixed ERGM. Estimation is carried out by iterating between approximate pseudolikelihood estimation for the random effects and maximum likelihood estimation for the remaining parameters in the model. This approach provides a stable algorithm, which allows to fit nodal heterogeneity effects even for large scale networks. We also propose model selection based on the Akaike Information Criterion to check for node-specific heterogeneity.

## 키워드

Exponential random graph models, Random effects model, Mathematics, Parametric statistics, Random graph, Statistics, Estimation, Node (physics)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

