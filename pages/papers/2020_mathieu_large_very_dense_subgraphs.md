---
title: "Large Very Dense Subgraphs in a Stream of Edges"
authors: ['Claire Mathieu', 'Michel de Rougemont']
year: 2020
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'Markov Chains and Monte Carlo Methods', 'Complexity and Algorithms in Graphs']
source: raw/2020_openalex_Large_Very_Dense_Subgraphs_in_a_nws_2021_17.md
---

# Large Very Dense Subgraphs in a Stream of Edges
**제목(한글)**: 엣지 스트림에서의 대규모 초밀집 부분 그래프

**저자**: Claire Mathieu; Michel de Rougemont
**출처**: Network Science, Vol.9, pp.107–117
**발행일**: 2020-10-15
**DOI**: https://doi.org/10.1017/nws.2021.17

## 한국어 요약

**연구질문**: 엣지 스트림으로 주어진 소셜 그래프에서 대규모 초밀집 부분 그래프를 효율적으로 탐지하고 재구성할 수 있는가?

**방법론**:
- 저장소 샘플링(Reservoir Sampling, 크기 k=O(√n·log n)) 기반 알고리즘
- 거대 연결 컴포넌트(giant component) 탐지를 통한 초밀집 부분 그래프 감지
- 파워 법칙 차수 분포를 따르는 랜덤 그래프 모델 정의 및 이론적 분석

**주요 결과**:
- √n 크기 이상의 초밀집 부분 그래프를 높은 확률로 탐지 가능
- 파워 법칙 분포를 따르는 그래프에는 대형 초밀집 부분 그래프가 거의 없음을 증명
- 슬라이딩 윈도우 기반 동적 그래프로 결과 일반화


## 초록 (원문)

Abstract We study the detection and the reconstruction of a large very dense subgraph in a social graph with n nodes and m edges given as a stream of edges, when the graph follows a power law degree distribution, in the regime when $m=O(n. \log n)$ . A subgraph S is very dense if it has $\Omega(|S|^2)$ edges. We uniformly sample the edges with a Reservoir of size $k=O(\sqrt{n}.\log n)$ . Our detection algorithm checks whether the Reservoir has a giant component. We show that if the graph contains a very dense subgraph of size $\Omega(\sqrt{n})$ , then the detection algorithm is almost surely correct. On the other hand, a random graph that follows a power law degree distribution almost surely has no large very dense subgraph, and the detection algorithm is almost surely correct. We define a new model of random graphs which follow a power law degree distribution and have large very dense subgraphs. We then show that on this class of random graphs we can reconstruct a good approximation of the very dense subgraph with high probability. We generalize these results to dynamic graphs defined by sliding windows in a stream of edges.

## 키워드

Combinatorics, Mathematics, Degree (music), Random graph, Graph, Omega, Degree distribution, Discrete mathematics

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

