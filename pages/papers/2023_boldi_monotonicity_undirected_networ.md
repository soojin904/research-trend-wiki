---
title: "Monotonicity in undirected networks"
authors: ['Paolo Boldi', 'Flavio Furia', 'Sebastiano Vigna']
year: 2023
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'Graph theory and applications', 'Opinion Dynamics and Social Influence']
source: raw/2023_openalex_Monotonicity_in_undirected_networks_nws_2022_42.md
---

# Monotonicity in undirected networks
**제목(한글)**: 무방향 네트워크에서의 단조성

**저자**: Paolo Boldi; Flavio Furia; Sebastiano Vigna
**출처**: Network Science, Vol.11, pp.351–373
**발행일**: 2023-02-02
**DOI**: https://doi.org/10.1017/nws.2022.42


## 한국어 요약

**연구질문**: 무방향 네트워크에서 새로운 엣지를 추가하는 것이 항상 해당 노드의 중심성을 높이는가(단조성이 성립하는가)?

**방법론**:
- 점수 단조성(score monotonicity)과 순위 단조성(rank monotonicity) 형식적 정의
- 근접(closeness), 조화(harmonic), 매개(betweenness), 아이겐벡터, PageRank 등 주요 중심성 척도 분석
- 수학적 증명 및 반례(counterexample) 제시

**주요 결과**:
- 무방향 네트워크에서 closeness, harmonic, betweenness, eigenvector, PageRank 모두 순위 단조성 불만족
- betweenness와 PageRank는 점수 단조성조차 불만족
- "팔로워를 얻는 것과 달리 친구를 얻는 것이 항상 유익하지는 않다"는 역설 수학적 증명


## 초록 (원문)

Abstract Is it always beneficial to create a new relationship (have a new follower/friend) in a social network? This question can be formally stated as a property of the centrality measure that defines the importance of the actors of the network. Score monotonicity means that adding an arc increases the centrality score of the target of the arc; rank monotonicity means that adding an arc improves the importance of the target of the arc relatively to the remaining nodes. It is known that most centralities are both score and rank monotone on directed, strongly connected graphs. In this paper, we study the problem of score and rank monotonicity for classical centrality measures in the case of undirected networks: in this case, we require that score, or relative importance, improves at both endpoints of the new edge. We show that, surprisingly, the situation in the undirected case is very different, and in particular that closeness, harmonic centrality, betweenness, eigenvector centrality, Seeley’s index, Katz’s index, and PageRank are not rank monotone; betweenness and PageRank are not even score monotone. In other words, while it is always a good thing to get a new follower, it is not always beneficial to get a new friend.

## 키워드

Betweenness centrality, Centrality, Monotonic function, PageRank, Rank (graph theory), Mathematics, Monotone polygon, Closeness

## 위키 연관

- [[pages/methods/centrality|Centrality]]

## 메모

