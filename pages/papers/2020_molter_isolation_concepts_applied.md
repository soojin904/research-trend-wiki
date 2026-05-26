---
title: "Isolation concepts applied to temporal clique enumeration"
authors: ['Hendrik Molter', 'Rolf Niedermeier', 'Malte Renken']
year: 2020
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'Advanced Graph Neural Networks', 'Caching and Content Delivery']
source: raw/2020_openalex_Isolation_concepts_applied_to_temporal_clique_nws_2020_38.md
---

# Isolation concepts applied to temporal clique enumeration
**제목(한글)**: 시간적 클리크 열거에 적용된 고립 개념

**저자**: Hendrik Molter; Rolf Niedermeier; Malte Renken
**출처**: Network Science, Vol.9, pp.S83–S105
**발행일**: 2020-10-16
**DOI**: https://doi.org/10.1017/nws.2020.38

## 한국어 요약

**연구질문**: 정적 네트워크에서의 클리크 고립 개념을 시간적 네트워크로 확장했을 때 어떤 새로운 유형의 고립이 발생하며, 이를 효율적으로 열거할 수 있는가?

**방법론**:
- 정적 네트워크 클리크 고립(isolation) 개념의 시간적 네트워크 적용 확장
- 6가지 시간적 고립 유형 정의
- "고립 정도"를 파라미터로 하는 파라미터화 열거 알고리즘 개발 및 실제 데이터 구현

**주요 결과**:
- 시간 차원 추가로 6가지 자연스러운 고립 유형 도출
- 5가지 고립 유형에 대한 파라미터화 열거 알고리즘 제안
- 더 고립된 클리크일수록 더 빠르게 발견 가능함을 실증


## 초록 (원문)

Abstract Isolation is a concept originally conceived in the context of clique enumeration in static networks, mostly used to model communities that do not have much contact to the outside world. Herein, a clique is considered isolated if it has few edges connecting it to the rest of the graph. Motivated by recent work on enumerating cliques in temporal networks, we transform the isolation concept to the temporal setting. We discover that the addition of the time dimension leads to six distinct natural isolation concepts. Our main contribution is the development of parameterized enumeration algorithms for five of these six isolation types for clique enumeration, employing the parameter “degree of isolation.” In a nutshell, this means that the more isolated these cliques are, the faster we can find them. On the empirical side, we implemented and tested these algorithms on (temporal) social network data, obtaining encouraging results.

## 키워드

Enumeration, Clique, Isolation (microbiology), Parameterized complexity, Context (archaeology), Computer science, Dimension (graph theory), Theoretical computer science

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

