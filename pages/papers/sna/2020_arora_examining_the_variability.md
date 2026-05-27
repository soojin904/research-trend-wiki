---
title: "Examining the variability in network populations and its role in generative models"
authors: ['Viplove Arora', 'Dali Guo', 'Katherine D. Dunbar', 'Mario Ventresca']
year: 2020
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'Opinion Dynamics and Social Influence', 'Bioinformatics and Genomic Networks']
source: raw/2020_openalex_Examining_the_variability_in_network_populations_nws_2019_63.md
---

# Examining the variability in network populations and its role in generative models
**제목(한글)**: 네트워크 모집단의 변동성과 생성 모델에서의 역할 검토

**저자**: Viplove Arora; Dali Guo; Katherine D. Dunbar; Mario Ventresca
**출처**: Network Science, Vol.8, pp.S43–S64
**발행일**: 2020-01-17
**DOI**: https://doi.org/10.1017/nws.2019.63

## 한국어 요약

**연구질문**: 단일 네트워크 관측치에서 학습한 생성 모델은 네트워크 모집단의 자연적 변동성을 얼마나 잘 포착하는가?

**방법론**:
- 네트워크 모집단 변동성 정량화 (비유사도 공간 비교, 데이터 기반 엔트로피 측도)
- 4가지 생성 모델(generative models) 평가
- 모의 실험 및 실증 분석

**주요 결과**:
- 단일 네트워크 관측치로 학습된 생성 모델은 모집단의 변동성을 포착하지 못함
- 네트워크 모델 적합도 평가 방식의 재고 필요성 제기
- 변동성을 반영한 새로운 모델 개발 방향 제시


## 초록 (원문)

Abstract A principled approach to understand networks is to formulate generative models and infer their parameters from given network data. Due to the scarcity of data in the form of multiple networks that have evolved from the same process, generative models are typically formulated to learn parameters from a single network observation, hence ignoring the natural variability of the “true” process. In this paper, we highlight the importance of variability in evaluating generative models and present two ways of quantifying the variability for a finite set of networks. The first evaluation scheme compares the statistical properties of networks in a dissimilarity space, while the other relies on data-driven entropy measures to compute variability in network populations. Using these measures, we evaluate the ability of four generative models to synthesize networks that capture the variability of the “true” process. Our empirical analysis suggests that generative models fitted for a single network observation fail to capture the variability in the network population. Our work highlights the need for rethinking the way we evaluate the goodness-of-fit of new and existing network models and devising models that are capable of matching the variability of network populations when available.

## 키워드

Generative grammar, Computer science, Generative model, Machine learning, Population, Matching (statistics), Artificial intelligence, Data mining

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

