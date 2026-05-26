---
title: "The latent cognitive structures of social networks"
authors: ['Izabel Aguiar', 'Johan Ugander']
year: 2024
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'Opinion Dynamics and Social Influence']
source: raw/2024_openalex_The_latent_cognitive_structures_of_social_nws_2024_7.md
---

# The latent cognitive structures of social networks

**제목(한글)**: 소셜 네트워크의 잠재 인지 구조

**저자**: Izabel Aguiar; Johan Ugander
**출처**: Network Science, Vol.12, pp.202–233
**발행일**: 2024-04-25
**DOI**: https://doi.org/10.1017/nws.2024.7

## 한국어 요약

**연구질문**: 인지 사회 구조(CSS)에서 네트워크를 지각할 때 사용하는 인지적 휴리스틱을 공유하는 사람들을 어떻게 식별할 수 있는가?

**방법론**:
- 인지 사회 구조(CSS)를 3차원 텐서(tensor)로 모델링
- 비음 저차원 Tucker 분해(NNTuck)로 잠재 사회·인지 구조 동시 추정
- 다층 확률 블록 모형(SBM) 추정과 유사한 절차 적용

**주요 결과**:
- 네트워크 지각의 잠재 인지 공간을 사회-인지 일치(agreement) 검정으로 운용화
- 4개 CSS 분석을 통해 네트워크별 잠재 인지 구조의 이질성 규명
- 인지적으로 독립·종속·중복인 네트워크 구조를 모델링하는 통계적 프레임워크 제공

## 초록 (원문)

Abstract When people are asked to recall their social networks, theoretical and empirical work tells us that they rely on shortcuts, or heuristics. Cognitive social structures (CSSs) are multilayer social networks where each layer corresponds to an individual’s perception of the network. With multiple perceptions of the same network, CSSs contain rich information about how these heuristics manifest, motivating the question, Can we identify people who share the same heuristics? In this work, we propose a method for identifying cognitive structure across multiple network perceptions, analogous to how community detection aims to identify social structure in a network. To simultaneously model the joint latent social and cognitive structure, we study CSSs as three-dimensional tensors, employing low-rank nonnegative Tucker decompositions (NNTuck) to approximate the CSS—a procedure closely related to estimating a multilayer stochastic block model (SBM) from such data. We propose the resulting latent cognitive space as an operationalization of the sociological theory of social cognition by identifying individuals who share relational schema . In addition to modeling cognitively independent , dependent , and redundant networks, we propose a specific model instance and related statistical test for testing when there is social-cognitive agreement in a network: when the social and cognitive structures are equivalent. We use our approach to analyze four different CSSs and give insights into the latent cognitive structures of those networks.

## 키워드

Cognition, Psychology, Neuroscience

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

