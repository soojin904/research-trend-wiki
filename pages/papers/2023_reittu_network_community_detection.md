---
title: "A network community detection method with integration of data from multiple layers and node attributes"
authors: ['Hannu Reittu', 'Lasse Leskelä', 'Tomi Räty']
year: 2023
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'Opinion Dynamics and Social Influence', 'Mental Health Research Topics']
source: raw/2023_openalex_A_network_community_detection_method_with_nws_2023_2.md
---

# A network community detection method with integration of data from multiple layers and node attributes
**제목(한글)**: 다층 레이어와 노드 속성 데이터를 통합한 네트워크 커뮤니티 탐지 방법

**저자**: Hannu Reittu; Lasse Leskelä; Tomi Räty
**출처**: Network Science, Vol.11, pp.374–396
**발행일**: 2023-03-07
**DOI**: https://doi.org/10.1017/nws.2023.2

## 한국어 요약

**연구질문**: 다층 네트워크의 토폴로지 정보와 노드 속성을 동시에 통합하는 커뮤니티 탐지 방법을 어떻게 설계할 수 있는가?

**방법론**:
- 노드를 행, 데이터 항목을 열로 표현하는 데이터 행렬(data matrix) 프레임워크 제안
- 정규 분해(regular decomposition) 방법을 비정방 행렬로 확장하여 커뮤니티 분할
- 거리 행렬, 차수 증강 행렬, 다층 네트워크의 연결 행렬 연결 등 다양한 데이터 행렬 유형 적용
- 합성 멱함수 그래프 및 실제 인터넷·항공 네트워크 데이터로 검증

**주요 결과**:
- 노드 차수를 별도 열로 추가하면 계층적 스케일프리 네트워크의 계층 구조와 잘 일치하는 커뮤니티 탐지
- 다층 네트워크의 거리 행렬 연결을 통해 단일 네트워크보다 더 풍부한 커뮤니티 구조 파악 가능
- 제안 방법이 다른 커뮤니티 탐지 방법 대비 우수한 성능 확인

## 초록 (원문)

Abstract Multilayer networks are in the focus of the current complex network study. In such networks, multiple types of links may exist as well as many attributes for nodes. To fully use multilayer—and other types of complex networks in applications, the merging of various data with topological information renders a powerful analysis. First, we suggest a simple way of representing network data in a data matrix where rows correspond to the nodes and columns correspond to the data items. The number of columns is allowed to be arbitrary, so that the data matrix can be easily expanded by adding columns. The data matrix can be chosen according to targets of the analysis and may vary a lot from case to case. Next, we partition the rows of the data matrix into communities using a method which allows maximal compression of the data matrix. For compressing a data matrix, we suggest to extend so-called regular decomposition method for non-square matrices. We illustrate our method for several types of data matrices, in particular, distance matrices, and matrices obtained by augmenting a distance matrix by a column of node degrees, or by concatenating several distance matrices corresponding to layers of a multilayer network. We illustrate our method with synthetic power-law graphs and two real networks: an Internet autonomous systems graph and a world airline graph. We compare the outputs of different community recovery methods on these graphs and discuss how incorporating node degrees as a separate column to the data matrix leads our method to identify community structures well-aligned with tiered hierarchical structures commonly encountered in complex scale-free networks.

## 키워드

Row, Row and column spaces, Computer science, Column (typography), Matrix (chemical analysis), Node (physics), Partition (number theory), Algorithm

## 위키 연관

- [[pages/methods/centrality|Centrality]]

## 메모

