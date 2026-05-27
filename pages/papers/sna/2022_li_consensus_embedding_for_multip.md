---
title: "Consensus embedding for multiple networks: Computation and applications"
authors: ['Mengzhen Li', 'Mustafa Coşkun', 'Mehmet Koyutürk']
year: 2022
venue: "Network Science"
tags: ['Advanced Graph Neural Networks', 'Functional Brain Connectivity Studies', 'Complex Network Analysis Techniques']
source: raw/2022_openalex_Consensus_embedding_for_multiple_networks_Computation_nws_2022_17.md
---

# Consensus embedding for multiple networks: Computation and applications
**제목(한글)**: 다중 네트워크의 합의 임베딩: 계산과 응용

**저자**: Mengzhen Li; Mustafa Coşkun; Mehmet Koyutürk
**출처**: Network Science, Vol.10, pp.190–206
**발행일**: 2022-05-30
**DOI**: https://doi.org/10.1017/nws.2022.17


## 한국어 요약

**연구질문**: 동일 네트워크의 여러 버전 또는 다중 연결 유형을 가진 복합 네트워크에서, 개별 임베딩을 결합한 합의 임베딩(consensus embedding)을 효과적으로 계산하는 방법은 무엇인가?

**방법론**:
- 특이값 분해(SVD), 변분 오토인코더(VAE), 정준 상관 분석(CCA, canonical correlation analysis) 세 가지 차원 축소 방법 비교
- 링크 예측 작업에서 합의 임베딩 성능 평가
- 조합 링크 예측 쿼리 효율성 측정

**주요 결과**:
- CCA가 합의 임베딩 계산에서 다른 차원 축소 방법들을 능가함
- 합의 임베딩이 통합 네트워크 임베딩에 근접한 링크 예측 정확도 달성
- 다중 네트워크 조합 쿼리 효율을 수십 배 향상 가능


## 초록 (원문)

Abstract Machine learning applications on large-scale network-structured data commonly encode network information in the form of node embeddings. Network embedding algorithms map the nodes into a low-dimensional space such that the nodes that are “similar” with respect to network topology are also close to each other in the embedding space. Real-world networks often have multiple versions or can be “multiplex” with multiple types of edges with different semantics. For such networks, computation of Consensus Embedding s based on the node embeddings of individual versions can be useful for various reasons, including privacy, efficiency, and effectiveness of analyses. Here, we systematically investigate the performance of three dimensionality reduction methods in computing consensus embeddings on networks with multiple versions: singular value decomposition, variational auto-encoders, and canonical correlation analysis (CCA). Our results show that (i) CCA outperforms other dimensionality reduction methods in computing concensus embeddings, (ii) in the context of link prediction, consensus embeddings can be used to make predictions with accuracy close to that provided by embeddings of integrated networks, and (iii) consensus embeddings can be used to improve the efficiency of combinatorial link prediction queries on multiple networks by multiple orders of magnitude.

## 키워드

Computer science, Embedding, Dimensionality reduction, Node (physics), Theoretical computer science, Computation, Curse of dimensionality, Context (archaeology)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

