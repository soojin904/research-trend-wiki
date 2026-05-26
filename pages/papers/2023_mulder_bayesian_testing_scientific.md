---
title: "Bayesian testing of scientific expectations under exponential random graph models"
authors: ['Joris Mulder', 'Nial Friel', 'Philip Leifeld']
year: 2023
venue: "Social Networks"
tags: ['Complex Network Analysis Techniques', 'Opinion Dynamics and Social Influence', 'Advanced Causal Inference Techniques']
source: raw/2023_openalex_Bayesian_testing_of_scientific_expectations_under_j_socnet_2023_11_004.md
---

# Bayesian testing of scientific expectations under exponential random graph models
**제목(한글)**: 지수 랜덤 그래프 모형 하에서의 과학적 기대값에 대한 베이지안 검정

**저자**: Joris Mulder; Nial Friel; Philip Leifeld
**출처**: Social Networks, Vol.78, pp.40–53
**발행일**: 2023-12-03
**DOI**: https://doi.org/10.1016/j.socnet.2023.11.004


## 한국어 요약

**연구질문**: ERGM 맥락에서 p값 기반 유의성 검정의 한계를 극복하는 베이지안 가설 검정 방법론을 어떻게 개발할 수 있는가?

**방법론**:
- 베이지안 프레임워크 기반 베이즈 인수(Bayes factor) 및 사후 확률 계산
- 등호·순서 제약 조건을 포함한 다중 가설 동시 검정
- R 패키지 BFpack 구현 및 협력 네트워크·정책 네트워크 적용

**주요 결과**:
- 귀무 가설 지지 증거를 정량화할 수 있는 베이지안 검정 방법론 제시
- 경쟁 가설 간 직접 비교 가능한 프레임워크 구축
- p값의 일관성 없는 동작 등 기존 방법의 한계 극복


## 초록 (원문)

The exponential random graph (ERGM) model is a commonly used statistical framework for studying the determinants of tie formations from social network data. To test scientific theories under ERGMs, statistical inferential techniques are generally used based on traditional significance testing using p-values. This methodology has certain limitations, however, such as its inconsistent behavior when the null hypothesis is true, its inability to quantify evidence in favor of a null hypothesis, and its inability to test multiple hypotheses with competing equality and/or order constraints on the parameters of interest in a direct manner. To tackle these shortcomings, this paper presents Bayes factors and posterior probabilities for testing scientific expectations under a Bayesian framework. The methodology is implemented in the R package BFpack. The applicability of the methodology is illustrated using empirical collaboration networks and policy networks.

## 키워드

Exponential random graph models, Null hypothesis, Statistical hypothesis testing, Bayes factor, Econometrics,  theorem", , , 

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

