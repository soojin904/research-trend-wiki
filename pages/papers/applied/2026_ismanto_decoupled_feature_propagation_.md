---
title: "Decoupled Feature Propagation and Structural Boosting: A Robust Framework for Node Classification on Heterophilous Graphs"
authors: ['Heru Ismanto', 'Izak Habel Wayangkau']
year: 2026
venue: "Engineering Technology & Applied Science Research"
tags: ['Advanced Graph Neural Networks', 'Graph Theory and Algorithms', 'Complex Network Analysis Techniques']
source: raw/applied/applied_2026_Decoupled_Feature_Propaga_etasr_20162.md
---

# Decoupled Feature Propagation and Structural Boosting: A Robust Framework for Node Classification on Heterophilous Graphs

**저자**: Heru Ismanto; Izak Habel Wayangkau
**출처**: Engineering Technology & Applied Science Research, Vol.16, pp.38876-38884
**발행일**: 2026-10-02
**DOI**: https://doi.org/10.48084/etasr.20162

## 초록 (원문)

Standard Graph Neural Networks (GNNs) frequently struggle with heterophilous structures where local proximity does not imply label similarity, leading to significant performance degradation due to signal oversmoothing. This study aimed to bridge the gap between theoretical complexity and empirical reliability by proposing a rigorously deterministic framework that evaluates decoupled feature diffusion and structural boosting strategies. Using five standardized heterophilous benchmarks, including Roman-Empire and Minesweeper, Multi-hop Propagated Features and Gradient Boosting architectures were validated under a strict anti-leakage protocol. Empirical results demonstrate a fundamental dichotomy in learning dynamics: the Multi-hop model achieves a Macro-F1 of 70.07% on Roman-Empire, drastically outperforming the graph-only baseline of 4.45%, whereas structural boosting dominates on attribute-heavy datasets like Questions with 60.94% Macro-F1. Furthermore, ablation studies reveal that removing multi-hop propagation induces a massive 35% performance drop on synthetic structures, confirming the critical necessity of capturing long-range dependencies in specific topologies. These findings challenge the prevailing reliance on complex deep architectures, advocating instead for an adaptive methodological taxonomy where model selection is directly anchored to the specific spectral and structural characteristics of the graph data.

## 키워드

heterophilous graphs, node classification, graph neural networks, gradient boosting, long-range dependencies

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

