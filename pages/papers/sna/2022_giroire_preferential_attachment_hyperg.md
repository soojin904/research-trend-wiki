---
title: "Preferential attachment hypergraph with high modularity"
authors: ['Frédéric Giroire', 'Nicolas Nisse', 'Thibaud Trolliet', 'Małgorzata Sulkowska']
year: 2022
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'Peer-to-Peer Network Technologies', 'Bioinformatics and Genomic Networks']
source: raw/2022_openalex_Preferential_attachment_hypergraph_with_high_modularity_nws_2022_35.md
---

# Preferential attachment hypergraph with high modularity
**제목(한글)**: 높은 모듈성을 가진 선호적 부착 하이퍼그래프

**저자**: Frédéric Giroire; Nicolas Nisse; Thibaud Trolliet; Małgorzata Sulkowska
**출처**: Network Science, Vol.10, pp.400–429
**발행일**: 2022-12-01
**DOI**: https://doi.org/10.1017/nws.2022.35


## 한국어 요약

**연구질문**: 실제 대규모 네트워크의 특성(멱함수 차수 분포 + 높은 모듈성)을 동시에 재현하는 하이퍼그래프(hypergraph) 생성 모델을 어떻게 개발할 수 있는가?

**방법론**:
- 커뮤니티 파티션을 포함한 동적 선호적 부착(preferential attachment) 하이퍼그래프 모델 제안
- 차수 분포의 멱함수 성질 이론적 증명
- 모듈성(modularity) 이론적 하한 제시
- 실제 공저자 네트워크와 비교 검증

**주요 결과**:
- 제안 모델의 차수 분포가 멱함수 법칙을 따름을 이론적으로 증명
- 실제 공저자 네트워크의 특성에 근접한 우수한 성능 달성
- 다양한 연구 분야에서 실제 현상을 더 잘 반영하는 유용한 하이퍼그래프 도구 제공


## 초록 (원문)

Abstract Numerous works have been proposed to generate random graphs preserving the same properties as real-life large-scale networks. However, many real networks are better represented by hypergraphs. Few models for generating random hypergraphs exist, and also, just a few models allow to both preserve a power-law degree distribution and a high modularity indicating the presence of communities. We present a dynamic preferential attachment hypergraph model which features partition into communities. We prove that its degree distribution follows a power-law, and we give theoretical lower bounds for its modularity. We compare its characteristics with a real-life co-authorship network and show that our model achieves good performances. We believe that our hypergraph model will be an interesting tool that may be used in many research domains in order to reflect better real-life phenomena.

## 키워드

Hypergraph, Preferential attachment, Modularity (biology), Degree distribution, Partition (number theory), Computer science, Theoretical computer science, Random graph

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

