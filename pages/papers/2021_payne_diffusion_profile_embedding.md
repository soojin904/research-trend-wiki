---
title: "Diffusion profile embedding as a basis for graph vertex similarity"
authors: ['Scott Payne', 'Edgar Fuller', 'George A. Spirou', 'Cun‐Quan Zhang']
year: 2021
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'Mental Health Research Topics', 'Functional Brain Connectivity Studies']
source: raw/2021_openalex_Diffusion_profile_embedding_as_a_basis_nws_2021_11.md
---

# Diffusion profile embedding as a basis for graph vertex similarity
**제목(한글)**: 그래프 정점 유사도의 기초로서의 확산 프로파일 임베딩

**저자**: Scott Payne; Edgar Fuller; George A. Spirou; Cun‐Quan Zhang
**출처**: Network Science, Vol.9, pp.328–353
**발행일**: 2021-09-01
**DOI**: https://doi.org/10.1017/nws.2021.11

## 한국어 요약

**연구질문**: 그래프 정점 임베딩(graph vertex embedding)을 통해 확산 유사도(diffusion similarity) 개념을 정의함으로써 네트워크 내 정점 간 유사도를 어떻게 효과적으로 측정할 수 있는가?

**방법론**:
- 무작위 보행(random walk)의 발산·수렴 패턴을 기반으로 정점 임베딩 벡터 생성
- 코사인 유사도(cosine similarity)로 정점 쌍의 유사도 계산
- C. elegans 신경 연결체(connectome) 및 마우스 망막 데이터에 적용

**주요 결과**:
- 확산 유사도가 커뮤니티 구조 내 정점 유사도와 이분 부분그래프(bipartite subgraph) 내 유사도 모두 표현 가능
- 불확실성 지수(uncertainty index)로 유사도 방법의 품질 측정 가능
- 가중·비가중, 방향성·비방향성 그래프 모두 적용 가능

## 초록 (원문)

Abstract We describe here a notion of diffusion similarity , a method for defining similarity between vertices in a given graph using the properties of random walks on the graph to model the relationships between vertices. Using the approach of graph vertex embedding, we characterize a vertex v i by considering two types of diffusion patterns: the ways in which random walks emanate from the vertex v i to the remaining graph and how they converge to the vertex v i from the graph. We define the similarity of two vertices v i and v j as the average of the cosine similarity of the vectors characterizing v i and v j . We obtain these vectors by modifying the solution to a differential equation describing a type of continuous time random walk. This method can be applied to any dataset that can be assigned a graph structure that is weighted or unweighted, directed or undirected. It can be used to represent similarity of vertices within community structures of a network while at the same time representing similarity of vertices within layered substructures (e.g., bipartite subgraphs) of the network. To validate the performance of our method, we apply it to synthetic data as well as the neural connectome of the C. elegans worm and a connectome of neurons in the mouse retina. A tool developed to characterize the accuracy of the similarity values in detecting community structures, the uncertainty index , is introduced in this paper as a measure of the quality of similarity methods.

## 키워드

Mathematics, Vertex (graph theory), Random walk, Bipartite graph, Combinatorics, Cosine similarity, Embedding, Graph embedding

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

