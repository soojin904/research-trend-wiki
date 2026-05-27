---
title: "Automated detection of edge clusters via an overfitted mixture prior"
authors: ['Hanh T. D. Pham', 'Daniel K. Sewell']
year: 2024
publication_date: 2024-01-19
venue: "Network Science"
volume: "12"
issue: "1"
pages: "88–106"
doi: "https://doi.org/10.1017/nws.2023.22"
oa_status: "hybrid"
oa_url: "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/73BC6AE9C66E4170843B64B4B651F323/S205012422300022Xa.pdf/div-class-title-automated-detection-of-edge-clusters-via-an-overfitted-mixture-prior-div.pdf"
openalex_id: "https://openalex.org/W4391033704"
tags: ['Complex Network Analysis Techniques', 'Bayesian Methods and Mixture Models', 'Advanced Clustering Algorithms Research']
keywords: ['Cluster analysis', 'Computer science', 'Mixture model', 'Scalability', 'Artificial intelligence', 'Data mining', 'Machine learning']
source: openalex
---

# Automated detection of edge clusters via an overfitted mixture prior

**저자**: Hanh T. D. Pham; Daniel K. Sewell
**출처**: Network Science, Vol.12 No.1, pp.88–106
**발행일**: 2024-01-19
**DOI**: https://doi.org/10.1017/nws.2023.22

## 초록

Abstract Most community detection methods focus on clustering actors with common features in a network. However, clustering edges offers a more intuitive way to understand the network structure in many real-life applications. Among the existing methods for network edge clustering, the majority are algorithmic, with the exception of the latent space edge clustering (LSEC) model proposed by Sewell ( Journal of Computational and Graphical Statistics, 30 (2), 390–405, 2021). LSEC was shown to have good performance in simulation and real-life data analysis, but fitting this model requires prior knowledge of the number of clusters and latent dimensions, which are often unknown to researchers. Within a Bayesian framework, we propose an extension to the LSEC model using a sparse finite mixture prior that supports automated selection of the number of clusters. We refer to our proposed approach as the automated LSEC or aLSEC. We develop a variational Bayes generalized expectation-maximization approach and a Hamiltonian Monte Carlo-within Gibbs algorithm for estimation. Our simulation study showed that aLSEC reduced run time by 10 to over 100 times compared to LSEC. Like LSEC, aLSEC maintains a computational cost that grows linearly with the number of actors in a network, making it scalable to large sparse networks. We developed the R package aLSEC which implements the proposed methodology.

## 키워드

Cluster analysis, Computer science, Mixture model, Scalability, Artificial intelligence, Data mining, Machine learning

## 주제 분류 (OpenAlex Topics)

- Complex Network Analysis Techniques (score: 0.999)
- Bayesian Methods and Mixture Models (score: 0.994)
- Advanced Clustering Algorithms Research (score: 0.992)

## 메모

