---
title: "Toward a generalized notion of discrete time for modeling temporal networks"
authors: ['Konstantin Kueffner', 'Mark Strembeck']
year: 2021
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'Data Visualization and Analytics', 'Data Management and Algorithms']
source: raw/2021_openalex_Toward_a_generalized_notion_of_discrete_nws_2021_20.md
---

# Toward a generalized notion of discrete time for modeling temporal networks
**제목(한글)**: 시간적 네트워크 모델링을 위한 이산 시간 개념의 일반화

**저자**: Konstantin Kueffner; Mark Strembeck
**출처**: Network Science, Vol.9, pp.443–477
**발행일**: 2021-12-01
**DOI**: https://doi.org/10.1017/nws.2021.20

## 한국어 요약

**연구질문**: 시간적 네트워크(temporal network) 모델링에서 시간의 개념을 어떻게 일반화할 수 있으며, 비결정론적 시간과 불완전 데이터를 어떻게 처리할 수 있는가?

**방법론**:
- 이산 시간(discrete time)의 일반화된 개념적 프레임워크 제안
- 비결정론적 시간(nondeterministic time) 및 불완전 데이터 처리 방법 도입
- R 패키지 구현 및 공개

**주요 결과**:
- 일반화된 이산 시간 개념이 온라인 소셜 네트워크 분석에서 흔히 발생하는 불완전 데이터 처리에 유용
- 시간적 최단 경로(temporal shortest path) 계산에 대한 함의 도출
- 모든 개념을 지원하는 R 패키지를 공개 배포

## 초록 (원문)

Abstract Many real-world networks, including social networks and computer networks for example, are temporal networks. This means that the vertices and edges change over time. However, most approaches for modeling and analyzing temporal networks do not explicitly discuss the underlying notion of time. In this paper, we therefore introduce a generalized notion of discrete time for modeling temporal networks. Our approach also allows for considering nondeterministic time and incomplete data, two issues that are often found when analyzing datasets extracted from online social networks, for example. In order to demonstrate the consequences of our generalized notion of time, we also discuss the implications for the computation of (shortest) temporal paths in temporal networks. In addition, we implemented an R-package that provides programming support for all concepts discussed in this paper. The R-package is publicly available for download.

## 키워드

Computer science, Nondeterministic algorithm, Theoretical computer science, Computation, Temporal database, Discrete time and continuous time, Artificial intelligence, Algorithm

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

