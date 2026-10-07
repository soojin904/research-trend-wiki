---
title: "A Citation Recommendation Algorithm Based on SciBERT and a Temporal-Aware Graph Attention Network"
authors: ['Jiabo Liu', 'Huaxiong Zhang']
year: 2026
venue: "JUCS - Journal of Universal Computer Science"
tags: ['Advanced Graph Neural Networks', 'Recommender Systems and Techniques', 'Topic Modeling']
source: raw/applied/applied_2026_A_Citation_Recommendation_jucs_176807.md
---

# A Citation Recommendation Algorithm Based on SciBERT and a Temporal-Aware Graph Attention Network

**저자**: Jiabo Liu; Huaxiong Zhang
**출처**: JUCS - Journal of Universal Computer Science, Vol.32, pp.1470-1491
**발행일**: 2026-09-25
**DOI**: https://doi.org/10.3897/jucs.176807

## 초록 (원문)

Citation recommendation plays a critical role in scholarly information retrieval by assisting researchers in identifying relevant and influential literature. Existing approaches typically rely on either textual semantic modeling or graph-based citation analysis, but often fail to jointly capture semantic relevance, structural dependencies, and temporal dynamics inherent in academic citation networks. In this paper, we propose SB-TGAT, a context-aware citation recommendation model that integrates scientific text representations with a Temporal-Aware graph attention mechanism. Specifically, we employ SciBERT to encode the semantic information of paper titles and abstracts, and design a Temporal-Aware Graph Attention Network (TGAT) to model citation relationships while explicitly incorporating temporal decay effects. The Temporal-Aware attention mechanism dynamically adjusts neighbor contributions according to publication time differences, enabling the model to balance long-term foundational works and short-term emerging research. To effectively integrate semantic and structural information, the textual embeddings and Temporal-Aware graph embeddings are fused through a feature interaction module and further optimized using a feed-forward neural network. We conduct extensive experiments on the DBLP-v14 dataset and evaluate the proposed model using standard information retrieval metrics, including MAP, MRR, and Recall@K. Experimental results demonstrate that SB-TGAT consistently outperforms strong baseline methods, validating the effectiveness of Temporal-Aware modeling and semantic– structural fusion for citation recommendation.

## 키워드



## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

