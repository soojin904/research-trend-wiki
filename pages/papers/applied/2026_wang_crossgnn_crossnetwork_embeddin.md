---
title: "Cross-GNN: a cross-network embedding framework for link prediction based graph neural networks"
authors: ['M C Wang', 'Haijuan Yang', 'Huanmin Luo', 'Yan Jia']
year: 2026
venue: "Scientific Reports"
tags: ['Advanced Graph Neural Networks', 'Complex Network Analysis Techniques', 'Bioinformatics and Genomic Networks']
source: raw/applied/applied_2026_CrossGNN_a_crossnetwork_e_s41598_026_63790_8.md
---

# Cross-GNN: a cross-network embedding framework for link prediction based graph neural networks

**저자**: M C Wang; Haijuan Yang; Huanmin Luo; Yan Jia
**출처**: Scientific Reports, Vol.None
**발행일**: 2026-07-27
**DOI**: https://doi.org/10.1038/s41598-026-63790-8

## 초록 (원문)

Link prediction serves as a core task in multilayer network mining and has extensive applications in social recommendation, biological interaction analysis, academic collaboration mining and other fields. Existing multilayer link prediction methods suffer from two prominent drawbacks. First, they rely on the ideal full node alignment assumption, which cannot adapt to real-world scenarios with partially overlapping nodes and scarce cross-layer anchor links. Second, single-layer models fail to exploit complementary cross-layer topological information, and their prediction performance is severely degraded by missing edges and structural noise within individual networks. To address these bottlenecks, this paper proposes Cross-GNN, a cross-network embedding framework based on graph neural networks for link prediction on partially aligned multilayer networks. The core Cross-GNN layer adopts a three-branch aggregation architecture, which fuses node self-features, degree-discounted intra-layer neighborhood information and topological messages from cross-layer anchor nodes via learnable adaptive attention weights. All network layers are projected into a unified shared latent space to simultaneously preserve intra-layer proximity and cross-layer structural consistency. A joint optimization objective function is constructed: the random-walk-based Skip-gram loss with negative sampling captures high-order topological connections within each layer, while the anchor-aware inter-layer loss equipped with hard negative sampling mitigates sample imbalance and enforces consistent embeddings of cross-layer nodes. Comprehensive experiments are conducted on four real-world cross-domain datasets, namely Facebook-Twitter, Twitter-YouTube, DBLP-Scholar and bio-CE-GT. The results demonstrate that Cross-GNN outperforms 16 state-of-the-art baseline methods in terms of AUC, AUPRC and Precision@10 under all anchor ratios ranging from 0 to 90%, and retains prominent advantages even in sparse scenarios with merely 30% anchor links. Supplementary experiments including ablation tests, node degree grouping analysis, noise robustness evaluation and computational efficiency comparison further verify that the proposed framework significantly improves prediction accuracy for low-degree nodes, exhibits strong resistance against missing edges and fake topological noise, and achieves better training and memory efficiency than most multilayer competitors. This study breaks the full alignment limitation of traditional multilayer modeling, delivers a robust and efficient technical solution for link prediction under scarce anchor links, and enriches the research ecosystem of cross-network graph representation learning.

## 키워드

Embedding, Node (physics), Exploit, Graph, Link (geometry), Artificial neural network, Task (project management), Core (optical fiber)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

