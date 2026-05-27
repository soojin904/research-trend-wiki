---
title: "Algorithmic aspects of temporal betweenness"
authors: ['Sebastian Buß', 'Hendrik Molter', 'Rolf Niedermeier', 'Maciej Rymar']
year: 2024
publication_date: 2024-04-12
venue: "Network Science"
volume: "12"
issue: "2"
pages: "160–188"
doi: "https://doi.org/10.1017/nws.2024.5"
oa_status: "hybrid"
oa_url: "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/5AC743D74B11417B032C389E3D0C5B27/S2050124224000055a.pdf/div-class-title-algorithmic-aspects-of-temporal-betweenness-div.pdf"
openalex_id: "https://openalex.org/W3034876319"
tags: ['Opportunistic and Delay-Tolerant Networks', 'Complex Network Analysis Techniques', 'Human Mobility and Location-Based Analysis']
keywords: ['Betweenness centrality', 'Vertex (graph theory)', 'Centrality', 'Computer science', 'Shortest path problem', 'Theoretical computer science', 'Combinatorics', 'Mathematics']
source: openalex
---

# Algorithmic aspects of temporal betweenness

**저자**: Sebastian Buß; Hendrik Molter; Rolf Niedermeier; Maciej Rymar
**출처**: Network Science, Vol.12 No.2, pp.160–188
**발행일**: 2024-04-12
**DOI**: https://doi.org/10.1017/nws.2024.5

## 초록

Abstract The betweenness centrality of a graph vertex measures how often this vertex is visited on shortest paths between other vertices of the graph. In the analysis of many real-world graphs or networks, the betweenness centrality of a vertex is used as an indicator for its relative importance in the network. In particular, it is among the most popular tools in social network analysis. In recent years, a growing number of real-world networks have been modeled as temporal graphs instead of conventional (static) graphs. In a temporal graph, we have a fixed set of vertices and there is a finite discrete set of time steps, and every edge might be present only at some time steps. While shortest paths are straightforward to define in static graphs, temporal paths can be considered “optimal” with respect to many different criteria, including length, arrival time, and overall travel time (shortest, foremost, and fastest paths). This leads to different concepts of temporal betweenness centrality , posing new challenges on the algorithmic side. We provide a systematic study of temporal betweenness variants based on various concepts of optimal temporal paths. Computing the betweenness centrality for vertices in a graph is closely related to counting the number of optimal paths between vertex pairs. While in static graphs computing the number of shortest paths is easily doable in polynomial time, we show that counting foremost and fastest paths is computationally intractable (#P-hard), and hence, the computation of the corresponding temporal betweenness values is intractable as well. For shortest paths and two selected special cases of foremost paths, we devise polynomial-time algorithms for temporal betweenness computation. Moreover, we also explore the distinction between strict (ascending time labels) and non-strict (non-descending time labels) time labels in temporal paths. In our experiments with established real-world temporal networks, we demonstrate the practical effectiveness of our algorithms, compare the various betweenness concepts, and derive recommendations on their practical use.

## 키워드

Betweenness centrality, Vertex (graph theory), Centrality, Computer science, Shortest path problem, Theoretical computer science, Combinatorics, Mathematics, Graph, Discrete mathematics

## 주제 분류 (OpenAlex Topics)

- Opportunistic and Delay-Tolerant Networks (score: 1.000)
- Complex Network Analysis Techniques (score: 0.999)
- Human Mobility and Location-Based Analysis (score: 0.998)

## 메모

