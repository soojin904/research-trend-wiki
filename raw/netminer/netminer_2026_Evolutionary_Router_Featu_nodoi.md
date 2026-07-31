---
title: "Evolutionary Router Feature Generation for Zero-Shot Graph Anomaly Detection with Mixture-of-Experts"
authors: ['Haiyang Jiang', 'Tong Chen', 'Xinyi Gao', 'Guansong Pang', 'Quoc Viet Hung Nguyen', 'Hongzhi Yin']
year: 2026
publication_date: 2026-02-12
venue: "ArXiv.org"
publisher: ""
volume: "None"
issue: "None"
pages: ""
doi: ""
openalex_id: "https://openalex.org/W7128864754"
cited_by_count: 0
fwci: 0.0
tags: ['Advanced Graph Neural Networks', 'Anomaly Detection Techniques and Applications', 'Complex Network Analysis Techniques']
keywords: ['Router', 'Anomaly detection', 'Routing (electronic design automation)', 'Generator (circuit theory)', 'Feature (linguistics)', 'Graph', 'Semantics (computer science)']
source: openalex-netminer
---

# Evolutionary Router Feature Generation for Zero-Shot Graph Anomaly Detection with Mixture-of-Experts

**저자**: Haiyang Jiang; Tong Chen; Xinyi Gao; Guansong Pang; Quoc Viet Hung Nguyen; Hongzhi Yin
**출처**: ArXiv.org
**발행일**: 2026-02-12
**DOI**: 

## 초록

Zero-shot graph anomaly detection (GAD) has attracted increasing attention recent years, yet the heterogeneity of graph structures, features, and anomaly patterns across graphs make existing single GNN methods insufficiently expressive to model diverse anomaly mechanisms. In this regard, Mixture-of-experts (MoE) architectures provide a promising paradigm by integrating diverse GNN experts with complementary inductive biases, yet their effectiveness in zero-shot GAD is severely constrained by distribution shifts, leading to two key routing challenges. First, nodes often carry vastly different semantics across graphs, and straightforwardly performing routing based on their features is prone to generating biased or suboptimal expert assignments. Second, as anomalous graphs often exhibit pronounced distributional discrepancies, existing router designs fall short in capturing domain-invariant routing principles that generalize beyond the training graphs. To address these challenges, we propose a novel MoE framework with evolutionary router feature generation (EvoFG) for zero-shot GAD. To enhance MoE routing, we propose an evolutionary feature generation scheme that iteratively constructs and selects informative structural features via an LLM-based generator and Shapley-guided evaluation. Moreover, a memory-enhanced router with an invariant learning objective is designed to capture transferable routing patterns under distribution shifts. Extensive experiments on six benchmarks show that EvoFG consistently outperforms state-of-the-art baselines, achieving strong and stable zero-shot GAD performance.

## 메모

