---
title: "Algorithmic aspects of temporal betweenness"
authors: ['Sebastian Buß', 'Hendrik Molter', 'Rolf Niedermeier', 'Maciej Rymar']
year: 2024
venue: "Network Science"
tags: ['Opportunistic and Delay-Tolerant Networks', 'Complex Network Analysis Techniques', 'Human Mobility and Location-Based Analysis']
source: raw/2024_openalex_Algorithmic_aspects_of_temporal_betweenness_nws_2024_5.md
---

# Algorithmic aspects of temporal betweenness

**제목(한글)**: 시간 매개 중심성의 알고리즘적 측면

**저자**: Sebastian Buß; Hendrik Molter; Rolf Niedermeier; Maciej Rymar
**출처**: Network Science, Vol.12, pp.160–188
**발행일**: 2024-04-12
**DOI**: https://doi.org/10.1017/nws.2024.5

## 한국어 요약

**연구질문**: 시간적 그래프에서 다양한 최적 경로 기준(최단·최선도·최속 경로)에 따른 시간 매개 중심성(temporal betweenness centrality)의 계산 복잡도는 어떠하며 효율적인 알고리즘을 어떻게 설계할 수 있는가?

**방법론**:
- 정적 그래프 vs 시간 그래프에서 매개 중심성(betweenness centrality) 비교 분석
- 최단·최선도(foremost)·최속(fastest) 경로 기준별 계산 복잡도 이론적 분석
- 다항 시간 알고리즘 설계 및 실제 시간 네트워크 실험 검증

**주요 결과**:
- 최선도·최속 경로 수 계산은 #P-hard로 계산적으로 처리 불가능
- 최단 경로 및 특정 최선도 경로 특수 사례에 대해 다항 시간 알고리즘 제시
- 실제 시간 네트워크에서 다양한 시간 매개 중심성 개념 비교 및 실용적 권고사항 도출

## 초록 (원문)

Abstract The betweenness centrality of a graph vertex measures how often this vertex is visited on shortest paths between other vertices of the graph. In the analysis of many real-world graphs or networks, the betweenness centrality of a vertex is used as an indicator for its relative importance in the network. In particular, it is among the most popular tools in social network analysis. In recent years, a growing number of real-world networks have been modeled as temporal graphs instead of conventional (static) graphs. In a temporal graph, we have a fixed set of vertices and there is a finite discrete set of time steps, and every edge might be present only at some time steps. While shortest paths are straightforward to define in static graphs, temporal paths can be considered “optimal” with respect to many different criteria, including length, arrival time, and overall travel time (shortest, foremost, and fastest paths). This leads to different concepts of temporal betweenness centrality , posing new challenges on the algorithmic side. We provide a systematic study of temporal betweenness variants based on various concepts of optimal temporal paths. Computing the betweenness centrality for vertices in a graph is closely related to counting the number of optimal paths between vertex pairs. While in static graphs computing the number of shortest paths is easily doable in polynomial time, we show that counting foremost and fastest paths is computationally intractable (#P-hard), and hence, the computation of the corresponding temporal betweenness values is intractable as well. For shortest paths and two selected special cases of foremost paths, we devise polynomial-time algorithms for temporal betweenness computation. Moreover, we also explore the distinction between strict (ascending time labels) and non-strict (non-descending time labels) time labels in temporal paths. In our experiments with established real-world temporal networks, we demonstrate the practical effectiveness of our algorithms, compare the various betweenness concepts, and derive recommendations on their practical use.

## 키워드

Betweenness centrality, Vertex (graph theory), Centrality, Computer science, Shortest path problem, Theoretical computer science, Combinatorics, Mathematics

## 위키 연관

- [[pages/methods/centrality|Centrality]]

## 메모

