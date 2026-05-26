---
title: "Accounting for edge uncertainty in stochastic actor-oriented models for dynamic network analysis"
authors: ['Heather Shappell', 'Mark Kramer', 'Catherine J. Chu', 'Eric D. Kolaczyk']
year: 2025
venue: "Network Science"
tags: ['Functional Brain Connectivity Studies', 'Opinion Dynamics and Social Influence', 'Complex Network Analysis Techniques']
source: raw/2025_openalex_Accounting_for_edge_uncertainty_in_stochastic_nws_2025_6.md
---

# Accounting for edge uncertainty in stochastic actor-oriented models for dynamic network analysis
**제목(한글)**: 동적 네트워크 분석을 위한 확률적 행위자 지향 모델에서 에지 불확실성 처리

**저자**: Heather Shappell; Mark Kramer; Catherine J. Chu; Eric D. Kolaczyk
**출처**: Network Science, Vol.13
**발행일**: 2025-01-01
**DOI**: https://doi.org/10.1017/nws.2025.6

## 한국어 요약

**연구질문**: 관측된 네트워크에 위양성(false positive)·위음성(false negative) 에지가 포함된 경우, 확률적 행위자 지향 모델(SAOM)을 어떻게 확장해 에지 불확실성을 반영할 수 있는가?

**방법론**:
- 은닉 마르코프 모델(HMM) 확장을 SAOM에 적용: 잠재 모델(true networks의 마르코프 과정) + 측정 모델(관측 네트워크의 조건부 분포)
- EM 알고리즘과 입자 필터링(particle filtering)을 이용한 파라미터 추정
- 뇌파(EEG) 데이터 기반 기능적 뇌 네트워크 사례 적용

**주요 결과**:
- HMM 확장 SAOM이 노이즈 포함 네트워크에서 표준 SAOM보다 추정 정확도 향상
- EEG 뇌 네트워크 적용 시 표준 SAOM 대비 더 큰 효과 크기 확인
- 에지 불확실성을 체계적으로 처리하는 새로운 동적 네트워크 분석 방법론 제시

## 초록 (원문)

Stochastic actor-oriented models (SAOMs) were designed in the social network setting to capture network dynamics representing a variety of influences on network change. The standard framework assumes the observed networks are free of false positive and false negative edges, which may be an unrealistic assumption. We propose a hidden Markov model (HMM) extension to these models, consisting of two components: 1) a latent model, which assumes that the unobserved, true networks evolve according to a Markov process as they do in the SAOM framework; and 2) a measurement model, which describes the conditional distribution of the observed networks given the true networks. An expectation-maximization algorithm is developed for parameter estimation. We address the computational challenge posed by a massive discrete state space, of a size exponentially increasing in the number of vertices, through the use of the missing information principle and particle filtering. We present results from a simulation study, demonstrating our approach offers improvement in accuracy of estimation, in contrast to the standard SAOM, when the underlying networks are observed with noise. We apply our method to functional brain networks inferred from electroencephalogram data, revealing larger effect sizes when compared to the naive approach of fitting the standard SAOM.

## 키워드

Computer science, Markov chain, Hidden Markov model, Expectation–maximization algorithm, Algorithm, Enhanced Data Rates for GSM Evolution, Artificial intelligence, Theoretical computer science

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

