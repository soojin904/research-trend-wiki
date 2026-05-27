---
title: "DERGMs: Degeneracy-restricted exponential family random graph models"
authors: ['Vishesh Karwa', 'Sonja Petrović', 'Denis Bajić']
year: 2022
venue: "Network Science"
tags: ['Markov Chains and Monte Carlo Methods', 'Statistical Methods and Inference', 'Complex Network Analysis Techniques']
source: raw/2022_openalex_DERGMs_Degeneracyrestricted_exponential_family_random_graph_nws_2022_5.md
---

# DERGMs: Degeneracy-restricted exponential family random graph models
**제목(한글)**: DERGM: 퇴화 제한 지수족 랜덤 그래프 모델

**저자**: Vishesh Karwa; Sonja Petrović; Denis Bajić
**출처**: Network Science, Vol.10, pp.82–110
**발행일**: 2022-03-01
**DOI**: https://doi.org/10.1017/nws.2022.5


## 한국어 요약

**연구질문**: ERGM(지수 랜덤 그래프 모델)의 퇴화(degeneracy) 문제를 해결하면서 실제 네트워크 데이터에 적용 가능한 새로운 모델 체계를 어떻게 구축할 수 있는가?

**방법론**:
- 그래프 이론의 퇴화도(degeneracy) 개념을 기반으로 지원 공간 제한
- DERGM(Degeneracy-Restricted ERGMs) 새 모델군 제안
- 새로운 고속 몬테카를로 방법을 도입하여 모수 추정 수행
- 이론적 성질 분석과 시뮬레이션·실제 데이터 실험

**주요 결과**:
- DERGM은 ERGM의 퇴화 및 계산 불가 문제를 해결하며 현실적 그래프에 확률 질량을 더 균등하게 분포시킴
- 퇴화도 파라미터가 낮으면 실제 네트워크의 희소성을 적절히 반영
- 새로운 몬테카를로 추정 알고리즘이 기존 MCMC보다 빠르고 확장 가능


## 초록 (원문)

Abstract Exponential random graph models, or ERGMs, are a flexible and general class of models for modeling dependent data. While the early literature has shown them to be powerful in capturing many network features of interest, recent work highlights difficulties related to the models’ ill behavior, such as most of the probability mass being concentrated on a very small subset of the parameter space. This behavior limits both the applicability of an ERGM as a model for real data and inference and parameter estimation via the usual Markov chain Monte Carlo algorithms. To address this problem, we propose a new exponential family of models for random graphs that build on the standard ERGM framework. Specifically, we solve the problem of computational intractability and “degenerate” model behavior by an interpretable support restriction. We introduce a new parameter based on the graph-theoretic notion of degeneracy, a measure of sparsity whose value is commonly low in real-world networks. The new model family is supported on the sample space of graphs with bounded degeneracy and is called degeneracy-restricted ERGMs, or DERGMs for short. Since DERGMs generalize ERGMs—the latter is obtained from the former by setting the degeneracy parameter to be maximal—they inherit good theoretical properties, while at the same time place their mass more uniformly over realistic graphs. The support restriction allows the use of new (and fast) Monte Carlo methods for inference, thus making the models scalable and computationally tractable. We study various theoretical properties of DERGMs and illustrate how the support restriction improves the model behavior. We also present a fast Monte Carlo algorithm for parameter estimation that avoids many issues faced by Markov Chain Monte Carlo algorithms used for inference in ERGMs.

## 키워드

Exponential random graph models, Degeneracy (biology), Exponential family, Inference, Markov chain Monte Carlo, Computer science, Random graph, Theoretical computer science

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

