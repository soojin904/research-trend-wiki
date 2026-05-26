---
title: "Colorful path detection in vertex-colored temporal"
authors: ['Riccardo Dondi', 'Mohammad Mehdi Hosseinzadeh']
year: 2023
venue: "Network Science"
tags: ['Advanced Graph Theory Research', 'Opportunistic and Delay-Tolerant Networks', 'Graph Labeling and Dimension Problems']
source: raw/2023_openalex_Colorful_path_detection_in_vertexcolored_temporal_nws_2023_17.md
---

# Colorful path detection in vertex-colored temporal
**제목(한글)**: 정점 색상 시간적 그래프에서의 다색 경로 탐지

**저자**: Riccardo Dondi; Mohammad Mehdi Hosseinzadeh
**출처**: Network Science, Vol.11, pp.615–631
**발행일**: 2023-08-18
**DOI**: https://doi.org/10.1017/nws.2023.17

## 한국어 요약

**연구질문**: 정적·시간적 그래프에서 서로 다른 색상(레이블)을 가진 노드를 최대한 포함하는 경로(다색 경로)를 어떻게 효율적으로 탐지할 수 있는가?

**방법론**:
- 정적·시간적 그래프 모두에서 최대 색상 수를 포함하는 경로 탐색 문제 정식화
- 근사 복잡도(approximation complexity) 이론 분석 및 근사 불가능성(inapproximability) 하한 증명
- 시간적 그래프에 특화된 휴리스틱 알고리즘 설계 및 실험적 평가

**주요 결과**:
- 해당 최적화 문제가 NP-난해(NP-hard)이며 근사 불가능성 하한 존재
- 제안된 휴리스틱이 합성·실제 그래프 모두에서 최적 해에 근접
- 시간적 그래프 분석에서 다색 경로 탐지의 실용적 알고리즘 제시

## 초록 (원문)

Abstract Finding paths is a fundamental problem in graph theory and algorithm design due to its many applications. Recently, this problem has been considered on temporal graphs, where edges may change over a discrete time domain. The analysis of graphs has also taken into account the relevance of vertex properties, modeled by assigning to vertices labels or colors. In this work, we deal with a problem that, given a static or temporal graph, whose vertices are colored graph looks for a path such that (1) the vertices of the path have distinct colors and (2) that path includes the maximum number of colors. We analyze the approximation complexity of the problem on static and temporal graphs, and we prove an inapproximability bound. Then, we consider the problem on temporal graphs, and we design a heuristic for it. We present an experimental evaluation of our heuristic, both on synthetic and real-world graphs. The experimental results show that for many instances of the problem, our method is able to return near-optimal solutions.

## 키워드

Colored, Vertex (graph theory), Heuristic, Combinatorics, Graph, Mathematics, Computer science, Longest path problem

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

