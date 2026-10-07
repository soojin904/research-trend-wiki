---
title: "Bhygnn+: unsupervised representation learning for heterophilic hypergraphs"
authors: ['Tianyi Ma', 'Yiyue Qian', 'Zehong Wang', 'Zheyuan Zhang', 'Chuxu Zhang', 'Yanfang Ye']
year: 2026
venue: "Knowledge and Information Systems"
tags: ['Advanced Graph Neural Networks', 'Graph Theory and Algorithms', 'Complex Network Analysis Techniques']
source: raw/applied/applied_2026_Bhygnn_unsupervised_repre_s10115_026_02834_x.md
---

# Bhygnn+: unsupervised representation learning for heterophilic hypergraphs

**저자**: Tianyi Ma; Yiyue Qian; Zehong Wang; Zheyuan Zhang; Chuxu Zhang; Yanfang Ye
**출처**: Knowledge and Information Systems, Vol.68
**발행일**: 2026-09-26
**DOI**: https://doi.org/10.1007/s10115-026-02834-x

## 초록 (원문)

Abstract Hypergraph neural networks (HyGNNs) have demonstrated remarkable success in modeling higher-order relationships among entities. However, their performance often degrades on heterophilic hypergraphs, where nodes connected by the same hyperedge tend to have dissimilar semantic representations or belong to different classes. While several HyGNNs, including our prior work BHyGNN, have been proposed to address heterophily, their reliance on labeled data significantly limits their applicability in real-world scenarios where annotations are scarce or costly. To overcome this limitation, we introduce BHyGNN+ , a self-supervised learning framework that extends BHyGNN for representation learning on heterophilic hypergraphs without requiring ground-truth labels. The core idea of BHyGNN+ is hypergraph duality , a structural transformation where the roles of nodes and hyperedges are interchanged. By contrasting augmented views of a hypergraph against its dual using cosine similarity, our framework captures essential structural patterns in a fully unsupervised manner. Notably, this duality-based formulation eliminates the need for negative samples, a common requirement in existing hypergraph contrastive learning methods that is often difficult to satisfy in practice. Extensive experiments on eleven benchmark datasets demonstrate that BHyGNN+ consistently outperforms state-of-the-art supervised and self-supervised baselines on both heterophilic and homophilic hypergraphs. Our results validate the effectiveness of leveraging hypergraph duality for self-supervised learning and establish a new paradigm for representation learning on challenging, unlabeled hypergraphs.

## 키워드

hypergraph neural networks, unsupervised feature learning, self-supervised learning, contrastive learning, higher-order relations

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

