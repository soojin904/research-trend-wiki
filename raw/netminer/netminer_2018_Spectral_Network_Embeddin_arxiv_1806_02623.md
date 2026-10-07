---
title: "Spectral Network Embedding: A Fast and Scalable Method via Sparsity"
authors: ['Jie Zhang', 'Yan Wang', 'Jie Tang', 'Ming Ding']
year: 2018
publication_date: 2018-06-07
venue: "arXiv (Cornell University)"
publisher: "Cornell University"
volume: "None"
issue: "None"
pages: ""
doi: "https://doi.org/10.48550/arxiv.1806.02623"
openalex_id: "https://openalex.org/W2806249323"
cited_by_count: 2
fwci: None
tags: ['Advanced Graph Neural Networks', 'Complex Network Analysis Techniques', 'Recommender Systems and Techniques']
keywords: ['Scalability', 'Computer science', 'Embedding', 'Node (physics)', 'Sparse matrix', 'Theoretical computer science', 'Matrix decomposition', 'Word2vec']
source: openalex-netminer
---

# Spectral Network Embedding: A Fast and Scalable Method via Sparsity

**저자**: Jie Zhang; Yan Wang; Jie Tang; Ming Ding
**출처**: arXiv (Cornell University)
**발행일**: 2018-06-07
**DOI**: https://doi.org/10.48550/arxiv.1806.02623

## 초록

Network embedding aims to learn low-dimensional representations of nodes in a network, while the network structure and inherent properties are preserved. It has attracted tremendous attention recently due to significant progress in downstream network learning tasks, such as node classification, link prediction, and visualization. However, most existing network embedding methods suffer from the expensive computations due to the large volume of networks. In this paper, we propose a $10\times \sim 100\times$ faster network embedding method, called Progle, by elegantly utilizing the sparsity property of online networks and spectral analysis. In Progle, we first construct a \textit{sparse} proximity matrix and train the network embedding efficiently via sparse matrix decomposition. Then we introduce a network propagation pattern via spectral analysis to incorporate local and global structure information into the embedding. Besides, this model can be generalized to integrate network information into other insufficiently trained embeddings at speed. Benefiting from sparse spectral network embedding, our experiment on four different datasets shows that Progle outperforms or is comparable to state-of-the-art unsupervised comparison approaches---DeepWalk, LINE, node2vec, GraRep, and HOPE, regarding accuracy, while is $10\times$ faster than the fastest word2vec-based method. Finally, we validate the scalability of Progle both in real large-scale networks and multiple scales of synthetic networks.

## 메모

