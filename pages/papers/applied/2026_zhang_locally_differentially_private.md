---
title: "Locally differentially private graph clustering via structure-preserving graph compression"
authors: ['Dongyue Zhang', 'Weiwei Ni', 'Nan Fu', 'Hongdou Yao']
year: 2026
venue: "Cybersecurity"
tags: ['Privacy-Preserving Technologies in Data', 'Advanced Graph Neural Networks', 'Complex Network Analysis Techniques']
source: raw/applied/applied_2026_Locally_differentially_pr_s42400_026_00652_w.md
---

# Locally differentially private graph clustering via structure-preserving graph compression

**저자**: Dongyue Zhang; Weiwei Ni; Nan Fu; Hongdou Yao
**출처**: Cybersecurity, Vol.9
**발행일**: 2026-09-28
**DOI**: https://doi.org/10.1186/s42400-026-00652-w

## 초록 (원문)

Abstract Locally differentially private clustering is an effective approach to uncover latent structures in decentralized social graphs while preserving individual privacy. Existing solutions encode graph data using adjacency bit vectors, whose high dimensionality introduces substantial differential noise and consequently degrades clustering utility. Besides, they typically require multiple rounds of interaction and iterative aggregation to construct clusters, leading to inevitable error accumulation and reduced clustering efficiency. To address these issues, we propose GCC-LDP, a graph compression-based clustering scheme that achieves efficient and accurate clustering under local differential privacy constraints. Specifically, we introduce an adjacency set vector encoding model, which leverages the Re-Pair compression method to adaptively reduce encoding length, significantly mitigating noise injection. Furthermore, a two-round decentralized social graph aggregation framework is designed to alleviate error accumulation. It employs a second-order difference method to detect distinguishing characteristics among nodes, facilitating rapid identification of cluster centers. Subsequently, a center expansion procedure forms clusters by exploiting intra-group node cohesion, avoiding costly iterative aggregation. Theoretical analysis and experiments on real-world datasets demonstrate that GCC-LDP substantially improves clustering performance by $$10\%$$ 10 % to $$20\%$$ 20 % , significantly outperforming state-of-the-art privacy-preserving clustering methods.

## 키워드

Cluster analysis, Adjacency matrix, Differential privacy, Adjacency list, Correlation clustering, Clustering high-dimensional data, Graph, CURE data clustering algorithm

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

