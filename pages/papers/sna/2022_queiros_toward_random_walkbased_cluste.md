---
title: "Toward random walk-based clustering of variable-order networks"
authors: ['Julie Queiros', 'Célestin Coquidé', 'François Queyroi']
year: 2022
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'Human Mobility and Location-Based Analysis', 'Data Management and Algorithms']
source: raw/2022_openalex_Toward_random_walkbased_clustering_of_variableorder_nws_2022_36.md
---

# Toward random walk-based clustering of variable-order networks
**제목(한글)**: 가변 차수 네트워크의 랜덤 워크 기반 군집화를 향하여

**저자**: Julie Queiros; Célestin Coquidé; François Queyroi
**출처**: Network Science, Vol.10, pp.381–399
**발행일**: 2022-12-01
**DOI**: https://doi.org/10.1017/nws.2022.36


## 한국어 요약

**연구질문**: 가변 차수 네트워크(variable-order network)에 랜덤 워크 기반 군집화 알고리즘을 직접 적용할 때 발생하는 편향을 어떻게 해결할 수 있는가?

**방법론**:
- 가변 차수 네트워크의 표현 집약(representation aggregation) 알고리즘 개발
- 실제 인간 이동 데이터셋에 대해 다양한 네트워크 표현의 군집 결과 비교
- 고차원(higher-order) 일반화 논의

**주요 결과**:
- 각 위치를 표현하는 '기억 노드(memory nodes)' 수 차이로 인한 군집 편향 확인
- 표현 집약 알고리즘이 편향을 줄이면서 정확한 네트워크 모델 생성
- 랜덤 워크 기반 군집화 도구를 가변 차수 네트워크에 직접 적용하는 방향성 제시


## 초록 (원문)

Abstract Higher-order networks aim at improving the classical network representation of trajectories data as memory-less order $1$ Markov models. To do so, locations are associated with different representations or “memory nodes” representing indirect dependencies between visited places as direct relations. One promising area of investigation in this context is variable-order network models as it was suggested by Xu et al. that random walk-based mining tools can be directly applied on such networks. In this paper, we focus on clustering algorithms and show that doing so leads to biases due to the number of nodes representing each location. To address them, we introduce a representation aggregation algorithm that produces smaller yet still accurate network models of the input sequences. We empirically compare the clustering found with multiple network representations of real-world mobility datasets. As our model is limited to a maximum order of $2$ , we discuss further generalizations of our method to higher orders.

## 키워드

Cluster analysis, Computer science, Representation (politics), Random walk, Markov chain, Variable (mathematics), Context (archaeology), Theoretical computer science

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

