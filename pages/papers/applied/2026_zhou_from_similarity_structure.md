---
title: "From Similarity to Structure: Training-free LLM Context Compression with Hybrid Graph Priors"
authors: ['Yitian Zhou', 'Chaoning Zhang', 'Jiaquan Zhang', 'Zhenzhen Huang', 'Jinyu Guo', 'Sung-Ho Bae', 'Lik‐Hang Lee', 'Caiyan Qin', 'Yang Yang']
year: 2026
venue: "ArXiv.org"
tags: ['Natural Language Processing Techniques', 'Topic Modeling', 'Machine Learning in Healthcare']
source: raw/applied/applied_2026_From_Similarity_to_Struct_nodoi.md
---

# From Similarity to Structure: Training-free LLM Context Compression with Hybrid Graph Priors

**저자**: Yitian Zhou; Chaoning Zhang; Jiaquan Zhang; Zhenzhen Huang; Jinyu Guo; Sung-Ho Bae; Lik‐Hang Lee; Caiyan Qin; Yang Yang
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-04-25
**DOI**: 

## 초록 (원문)

Long-context large language models remain computationally expensive to run and often fail to reliably process very long inputs, which makes context compression an important component of many systems. Existing compression approaches typically rely on trained compressors, dense retrieval-style selection, or heuristic trimming, and they often struggle to jointly preserve task relevance, topic coverage, and cross-sentence coherence under a strict token budget. To address this, we propose a training-free and model-agnostic compression framework that selects a compact set of sentences guided by structural graph priors. Our method constructs a sparse hybrid sentence graph that combines mutual k-NN semantic edges with short-range sequential edges, extracts a topic skeleton via clustering, and ranks sentences using an interpretable score that integrates task relevance, cluster representativeness, bridge centrality, and a cycle coverage cue. A budgeted greedy selection with redundancy suppression then produces a readable compressed context in original order. Experimental results on four datasets show that our approach is competitive with strong extractive and abstractive baselines, demonstrating larger gains on long-document benchmarks.

## 키워드

Redundancy (engineering), Graph, Set (abstract data type), Context (archaeology), Coherence (philosophical gambling strategy), Heuristic, Data compression, Pattern recognition (psychology)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

