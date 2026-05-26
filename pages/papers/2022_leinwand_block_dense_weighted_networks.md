---
title: "Block dense weighted networks with augmented degree correction"
authors: ['Benjamin Leinwand', 'Vladas Pipiras']
year: 2022
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'Mental Health Research Topics', 'Bioinformatics and Genomic Networks']
source: raw/2022_openalex_Block_dense_weighted_networks_with_augmented_nws_2022_23.md
---

# Block dense weighted networks with augmented degree correction
**제목(한글)**: 증강 차수 보정을 적용한 블록 밀집 가중 네트워크

**저자**: Benjamin Leinwand; Vladas Pipiras
**출처**: Network Science, Vol.10, pp.301–321
**발행일**: 2022-09-01
**DOI**: https://doi.org/10.1017/nws.2022.23


## 한국어 요약

**연구질문**: 대부분의 노드가 연결된 밀집 가중 네트워크에서 커뮤니티 구조를 어떻게 모델링하고 추정할 수 있으며, 새로운 네트워크를 효과적으로 생성할 수 있는가?

**방법론**:
- 노드 특성을 엣지 가중치로 매핑하는 함수 클래스 기반 새 프레임워크 제안
- 개별 노드 특성에서 엣지를 생성하는 유연한 파라미터 효율적 모델
- 이론 분석, 시뮬레이션, 실제 데이터로 성능 검증
- 동일 노드 집합에서 새 네트워크 생성을 위한 부트스트랩 방법론 개발

**주요 결과**:
- 커뮤니티 멤버십에 따른 에지 가중치 패턴 차이를 효과적으로 포착
- 엣지 수 대비 적은 파라미터로 유연성 확보
- 부트스트랩 방법이 다중 데이터 수집이 어려운 상황에서 유용함


## 초록 (원문)

Abstract Dense networks with weighted connections often exhibit a community-like structure, where although most nodes are connected to each other, different patterns of edge weights may emerge depending on each node’s community membership. We propose a new framework for generating and estimating dense weighted networks with potentially different connectivity patterns across different communities. The proposed model relies on a particular class of functions which map individual node characteristics to the edges connecting those nodes, allowing for flexibility while requiring a small number of parameters relative to the number of edges. By leveraging the estimation techniques, we also develop a bootstrap methodology for generating new networks on the same set of vertices, which may be useful in circumstances where multiple data sets cannot be collected. Performance of these methods is analyzed in theory, simulations, and real data.

## 키워드

Computer science, Node (physics), Degree (music), Flexibility (engineering), Set (abstract data type), Enhanced Data Rates for GSM Evolution, Class (philosophy), Block (permutation group theory)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

