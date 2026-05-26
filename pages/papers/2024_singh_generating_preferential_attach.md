---
title: "Generating preferential attachment graphs via a Pólya urn with expanding colors"
authors: ['Somya Singh', 'Fady Alajaji', 'Bahman Gharesifard']
year: 2024
venue: "Network Science"
tags: ['Advanced Graph Theory Research', 'Graph Labeling and Dimension Problems', 'Data Management and Algorithms']
source: raw/2024_openalex_Generating_preferential_attachment_graphs_via_a_nws_2024_3.md
---

# Generating preferential attachment graphs via a Pólya urn with expanding colors

**제목(한글)**: 확장 색상 폴리아 항아리를 활용한 선호적 연결 그래프 생성

**저자**: Somya Singh; Fady Alajaji; Bahman Gharesifard
**출처**: Network Science, Vol.12, pp.139–159
**발행일**: 2024-04-08
**DOI**: https://doi.org/10.1017/nws.2024.3

## 한국어 요약

**연구질문**: 폴리아 항아리(Pólya urn) 모형을 확장하여 Barabási-Albert 모형과 다르게 나중에 추가된 노드도 높은 연결차수를 가질 수 있는 선호적 연결 그래프를 어떻게 생성할 수 있는가?

**방법론**:
- 색상 확장 폴리아 항아리 모형 기반 선호적 연결(preferential attachment) 그래프 생성 모델 제안
- 각 노드를 고유 색상으로 코딩하여 시간에 따라 변하는 강화 파라미터 활용
- Barabási-Albert 모형과 시뮬레이션 비교 분석

**주요 결과**:
- 색상 코딩과 시변 강화 파라미터를 통해 후기 추가 노드의 높은 연결차수 획득 가능
- 연결차수 분포의 확률 분포 수학적 도출
- 의견 영향력 모델링에 더 유연한 대안 네트워크 성장 모형 제공

## 초록 (원문)

Abstract We introduce a novel preferential attachment model using the draw variables of a modified Pólya urn with an expanding number of colors, notably capable of modeling influential opinions (in terms of vertices of high degree) as the graph evolves. Similar to the Barabási-Albert model, the generated graph grows in size by one vertex at each time instance; in contrast however, each vertex of the graph is uniquely characterized by a color, which is represented by a ball color in the Pólya urn. More specifically at each time step, we draw a ball from the urn and return it to the urn along with a number of reinforcing balls of the same color; we also add another ball of a new color to the urn. We then construct an edge between the new vertex (corresponding to the new color) and the existing vertex whose color ball is drawn. Using color-coded vertices in conjunction with the time-varying reinforcing parameter allows for vertices added (born) later in the process to potentially attain a high degree in a way that is not captured in the Barabási-Albert model. We study the degree count of the vertices by analyzing the draw vectors of the underlying stochastic process. In particular, we establish the probability distribution of the random variable counting the number of draws of a given color which determines the degree of the vertex corresponding to that color in the graph. We further provide simulation results presenting a comparison between our model and the Barabási-Albert network.

## 키워드

Combinatorics, Mathematics, Computer science

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

