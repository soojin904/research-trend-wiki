---
title: "Spectral goodness-of-fit tests for complete and partial network data"
authors: ['Shane Lubold', 'Bolun Liu', 'Tyler H. McCormick']
year: 2025
venue: "Network Science"
tags: ['Random Matrices and Applications', 'Complex Network Analysis Techniques', 'Statistical Methods and Inference']
source: raw/2025_openalex_Spectral_goodnessoffit_tests_for_complete_and_nws_2025_10005.md
---

# Spectral goodness-of-fit tests for complete and partial network data
**제목(한글)**: 완전 및 부분 네트워크 데이터를 위한 스펙트럼 적합도 검정

**저자**: Shane Lubold; Bolun Liu; Tyler H. McCormick
**출처**: Network Science, Vol.13
**발행일**: 2025-01-01
**DOI**: https://doi.org/10.1017/nws.2025.10005

## 한국어 요약

**연구질문**: 확률적 블록 모델이나 잠재 공간 모델 같은 파라미터 모델이 네트워크 데이터에 적합한지를 시뮬레이션 없이 빠르게 검정하는 방법은 무엇인가?

**방법론**:
- 랜덤 행렬 이론(random matrix theory)을 이용한 이원 데이터(dyadic data) 일반 적합도(GoF) 검정 개발
- 잠재 공간 모델의 차원 선택 방법으로 적용
- 집합적 관계 데이터(ARD, Aggregated Relational Data) 등 부분 네트워크 데이터에도 적용 가능

**주요 결과**:
- 후보 모델로부터 시뮬레이션 없이 파라미터 선택 가능한 계산 효율적 방법 제시
- 다양한 네트워크 모델에 적용 가능한 일반성 확보
- 부분 네트워크(ARD 등)에도 적합도 검정 확장 가능하며 커뮤니티 탐지 알고리즘 성능 개선

## 초록 (원문)

Abstract Networks describe complex relationships between individual actors. In this work, we address the question of how to determine whether a parametric model, such as a stochastic block model or latent space model, fits a data set well, and will extrapolate to similar data. We use recent results in random matrix theory to derive a general goodness-of-fit (GoF) test for dyadic data. We show that our method, when applied to a specific model of interest, provides a straightforward, computationally fast way of selecting parameters in a number of commonly used network models. For example, we show how to select the dimension of the latent space in latent space models. Unlike other network GoF methods, our general approach does not require simulating from a candidate parametric model, which can be cumbersome with large graphs, and eliminates the need to choose a particular set of statistics on the graph for comparison. It also allows us to perform GoF tests on partial network data, such as Aggregated Relational Data. We show with simulations that our method performs well in many situations of interest. We analyze several empirically relevant networks and show that our method leads to improved community detection algorithms.

## 키워드

Goodness of fit, Mathematics, Artificial intelligence, Statistics, Computer science

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

