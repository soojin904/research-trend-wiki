---
title: "From Similarity to Structure: Training-free LLM Context Compression with Hybrid Graph Priors"
authors: ['Yitian Zhou', 'Chaoning Zhang', 'Jiaquan Zhang', 'Zhenzhen Huang', 'Jinyu Guo', 'Sung-Ho Bae', 'Lik‐Hang Lee', 'Caiyan Qin', 'Yang Yang']
year: 2026
publication_date: 2026-04-25
venue: "ArXiv.org"
volume: "None"
issue: "None"
pages: ""
doi: ""
oa_status: "green"
openalex_id: "https://openalex.org/W7158422662"
query_keyword: "text analysis"
tags: ['Natural Language Processing Techniques', 'Topic Modeling', 'Machine Learning in Healthcare']
keywords: ['Redundancy (engineering)', 'Graph', 'Set (abstract data type)', 'Context (archaeology)', 'Coherence (philosophical gambling strategy)', 'Heuristic', 'Data compression', 'Pattern recognition (psychology)']
source: openalex-keyword
---

# From Similarity to Structure: Training-free LLM Context Compression with Hybrid Graph Priors

**저자**: Yitian Zhou; Chaoning Zhang; Jiaquan Zhang; Zhenzhen Huang; Jinyu Guo; Sung-Ho Bae; Lik‐Hang Lee; Caiyan Qin; Yang Yang
**출처**: ArXiv.org
**발행일**: 2026-04-25
**DOI**: 
**수집 키워드**: text analysis

## 초록

Long-context large language models remain computationally expensive to run and often fail to reliably process very long inputs, which makes context compression an important component of many systems. Existing compression approaches typically rely on trained compressors, dense retrieval-style selection, or heuristic trimming, and they often struggle to jointly preserve task relevance, topic coverage, and cross-sentence coherence under a strict token budget. To address this, we propose a training-free and model-agnostic compression framework that selects a compact set of sentences guided by structural graph priors. Our method constructs a sparse hybrid sentence graph that combines mutual k-NN semantic edges with short-range sequential edges, extracts a topic skeleton via clustering, and ranks sentences using an interpretable score that integrates task relevance, cluster representativeness, bridge centrality, and a cycle coverage cue. A budgeted greedy selection with redundancy suppression then produces a readable compressed context in original order. Experimental results on four datasets show that our approach is competitive with strong extractive and abstractive baselines, demonstrating larger gains on long-document benchmarks.

## 키워드

Redundancy (engineering), Graph, Set (abstract data type), Context (archaeology), Coherence (philosophical gambling strategy), Heuristic, Data compression, Pattern recognition (psychology), Sentence, Compression (physics)

## 주제 분류 (OpenAlex Topics)

- Natural Language Processing Techniques (score: 0.286)
- Topic Modeling (score: 0.261)
- Machine Learning in Healthcare (score: 0.092)

## 메모

