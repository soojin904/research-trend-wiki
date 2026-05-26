---
title: "A multi-purposed unsupervised framework for comparing embeddings of undirected and directed graphs"
authors: ['Bogumił Kamiński', 'Łukasz Kraiński', 'Paweł Prałat', 'François Théberge']
year: 2022
venue: "Network Science"
tags: ['Advanced Graph Neural Networks', 'Complex Network Analysis Techniques', 'Social Media and Politics']
source: raw/2022_openalex_A_multipurposed_unsupervised_framework_for_comparing_nws_2022_27.md
---

# A multi-purposed unsupervised framework for comparing embeddings of undirected and directed graphs
**제목(한글)**: 비방향·방향 그래프 임베딩 비교를 위한 다목적 비지도 프레임워크

**저자**: Bogumił Kamiński; Łukasz Kraiński; Paweł Prałat; François Théberge
**출처**: Network Science, Vol.10, pp.323–346
**발행일**: 2022-09-28
**DOI**: https://doi.org/10.1017/nws.2022.27


## 한국어 요약

**연구질문**: 도메인 전문가 없이도 그래프 임베딩의 품질을 평가하고 최적 임베딩을 선택할 수 있는 비지도(unsupervised) 프레임워크를 어떻게 구축할 수 있는가?

**방법론**:
- 로컬 점수와 글로벌 점수를 각각 부여하는 이중 평가 프레임워크 확장
- 비방향/방향 그래프, 가중/비가중 그래프 모두 처리 가능
- 로컬·글로벌 네트워크 특성 표현 품질을 기준으로 임베딩 비교

**주요 결과**:
- 프레임워크가 비지도 방식으로 임베딩 품질을 평가하거나 후보군 식별 가능
- 유연하고 확장 가능하며 다양한 그래프 유형에 적용 가능
- 로컬·글로벌 특성의 균형을 기준으로 최적 임베딩 선택 지침 제공


## 초록 (원문)

Abstract Graph embedding is a transformation of nodes of a network into a set of vectors. A good embedding should capture the underlying graph topology and structure, node-to-node relationship, and other relevant information about the graph, its subgraphs, and nodes themselves. If these objectives are achieved, an embedding is a meaningful, understandable, and often compressed representation of a network. Unfortunately, selecting the best embedding is a challenging task and very often requires domain experts. In this paper, we extend the framework for evaluating graph embeddings that was recently introduced in [15]. Now, the framework assigns two scores, local and global, to each embedding that measure the quality of an evaluated embedding for tasks that require good representation of local and, respectively, global properties of the network. The best embedding, if needed, can be selected in an unsupervised way, or the framework can identify a few embeddings that are worth further investigation. The framework is flexible and scalable and can deal with undirected/directed and weighted/unweighted graphs.

## 키워드

Embedding, Computer science, Scalability, Theoretical computer science, Graph embedding, Graph, Node (physics), Topological graph theory

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

