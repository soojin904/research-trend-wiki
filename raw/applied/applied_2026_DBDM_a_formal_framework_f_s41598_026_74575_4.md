---
title: "DBDM: a formal framework for bias detection and mitigation in distributed large language models"
authors: ['K. J. Sahana Devi', 'Nishant Tripathi', 'S. Santhosh Kumar', 'M. Vinaya Babu', 'T R Mahesh', 'Suresh Guluwadi']
year: 2026
publication_date: 2026-10-11
venue: "Scientific Reports"
volume: "None"
issue: "None"
pages: ""
doi: "https://doi.org/10.1038/s41598-026-74575-4"
oa_status: "gold"
openalex_id: "https://openalex.org/W7221308250"
query_keyword: "social network"
tags: ['Ethics and Social Impacts of AI', 'Hate Speech and Cyberbullying Detection', 'Topic Modeling']
keywords: ['bias detection', 'bias mitigation', 'formal framework', 'algorithmic fairness']
source: openalex-keyword
---

# DBDM: a formal framework for bias detection and mitigation in distributed large language models

**저자**: K. J. Sahana Devi; Nishant Tripathi; S. Santhosh Kumar; M. Vinaya Babu; T R Mahesh; Suresh Guluwadi
**출처**: Scientific Reports
**발행일**: 2026-10-11
**DOI**: https://doi.org/10.1038/s41598-026-74575-4
**수집 키워드**: social network

## 초록

Large language models (LLMs) are increasingly being deployed in distributed settings, where different nodes may work on heterogeneous data, user populations, and local model updates. In such settings, bias can arise in an emergent fashion via local interactions and spread over the connected nodes, turning fairness into a property of the network rather than of the model. In this paper, we introduce Distributed Bias Detection and Mitigation (DBDM), a formal framework to model, detect, and mitigate dynamically evolving bias in distributed LLM settings. DBDM captures node-level bias in a multi-dimensional state consisting of statistical divergence, embedding disparity and response asymmetry, allowing bias to be monitored beyond a single output-level metric. The proposed framework combines local bias-aware optimisation with cross-node bias propagation modelling and graph-based consensus alignment, such that neighbouring nodes can coordinate fairness corrections while preserving the underlying distributed learning process. We evaluate the proposed framework through controlled distributed simulations with publicly available fairness benchmarks including StereoSet, CrowS-Pairs and BOLD. Experiments examine convergence, stability, scalability and multi-dimensional bias mitigation. Further, a real-transformer proof-of-concept experiment is performed on an open-access CrowS-Pairs subset with a lightweight PyTorch Transformer Encoder. In the pilot experiment, DBDM reduces the composite bias by ~ 48.5% and the inter-node bias-state variance by ~ 87.4% when compared to FedAvg over ten independent runs, while achieving statistically comparable fairness performance to FairFL. We also observe from communication analysis that explicitly communicating the bias state incurs a moderate additional communication overhead of around 8.3–8.8% over the conventional parameter aggregation for the configurations we experimented with. The results provide evidence that explicit modelling of bias states and consensus-based coordination can improve the fairness consistency of distributed learning systems at the network-level. The study also exposes practical challenges around communication latency, asynchronous participation, privacy protection, heterogeneous nodes, and production scale LLM validation which are important directions for future work.

## 키워드

bias detection, bias mitigation, formal framework, algorithmic fairness

## 주제 분류 (OpenAlex Topics)

- Ethics and Social Impacts of AI (score: 0.967)
- Hate Speech and Cyberbullying Detection (score: 0.010)
- Topic Modeling (score: 0.006)

## 메모

