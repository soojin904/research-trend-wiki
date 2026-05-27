---
title: "Is it correct to project and detect? How weighting unipartite projections influences community detection"
authors: ['Tristan J. B. Cann', 'Iain S. Weaver', 'Hywel T. P. Williams']
year: 2020
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'Opinion Dynamics and Social Influence', 'Misinformation and Its Impacts']
source: raw/2020_openalex_Is_it_correct_to_project_and_nws_2020_11.md
---

# Is it correct to project and detect? How weighting unipartite projections influences community detection
**제목(한글)**: 투영 후 탐지가 올바른가? 단일 모드 투영의 가중치 부여가 커뮤니티 탐지에 미치는 영향

**저자**: Tristan J. B. Cann; Iain S. Weaver; Hywel T. P. Williams
**출처**: Network Science, Vol.8, pp.S145–S163
**발행일**: 2020-04-17
**DOI**: https://doi.org/10.1017/nws.2020.11

## 한국어 요약

**연구질문**: 이분 네트워크를 단일 모드로 투영한 후 커뮤니티 탐지를 적용하는 방식은 얼마나 신뢰할 수 있으며, 어떤 투영 방식이 가장 강건한가?

**방법론**:
- 7가지 투영 방식(projection schemes) 비교 실험
- 소셜 미디어 실제 데이터 및 인공 네트워크 앙상블 평가
- 커뮤니티 탐지 성능 및 정확도 지표 분석

**주요 결과**:
- 롱테일 차수 분포를 가진 네트워크에서 다수 투영 방식의 성능 저하 확인
- "쌍곡선(hyperbolic)" 투영 방식이 가장 강건한 결과 제공
- 투영 네트워크 커뮤니티 탐지 해석 시 이분 구조 고려 필요


## 초록 (원문)

Abstract Bipartite networks represent pairwise relationships between nodes belonging to two distinct classes. While established methods exist for analyzing unipartite networks, those for bipartite network analysis are somewhat obscure and relatively less developed. Community detection in such instances is frequently approached by first projecting the network onto a unipartite network, a method where edges between node classes are encoded as edges within one class. Here we test seven different projection schemes by assessing the performance of community detection on both: (i) a real-world dataset from social media and (ii) an ensemble of artificial networks with prescribed community structure. A number of performance and accuracy issues become apparent from the experimental findings, especially in the case of long-tailed degree distributions. Of the methods tested, the “hyperbolic” projection scheme alleviates most of these difficulties and is thus the most robust scheme of those tested. We conclude that any interpretation of community detection algorithm performance on projected networks must be done with care as certain network configurations require strong community preference for the bipartite structure to be reflected in the unipartite communities. Our results have implications for the analysis of detected community structure in projected unipartite networks.

## 키워드

Computer science, Bipartite graph, Weighting, Pairwise comparison, Community structure, Projection (relational algebra), Artificial intelligence, Node (physics)

## 위키 연관

- [[pages/methods/centrality|Centrality]]

## 메모

