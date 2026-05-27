---
title: "Efficient Context Filtering for Extractive Question Answering: A Hybrid Approach with Semantic Validation"
authors: ['Vahid Ghanbarizadeh', 'Amin Moeinian', 'Zahra Younes Pour Langaroudi', 'Mohsen Mohammadagha', 'Athar Sharifi']
year: 2026
publication_date: 2026-01-25
venue: "Journal of Computer Science and Technology Studies"
volume: "8"
issue: "2"
pages: "01-09"
doi: "https://doi.org/10.32996/jcsts.2026.8.2.1"
oa_status: "diamond"
openalex_id: "https://openalex.org/W7126208571"
query_keyword: "text analysis"
tags: ['Topic Modeling', 'Natural Language Processing Techniques', 'Information Retrieval and Search Behavior']
keywords: ['Inference', 'Robustness (evolution)', 'Context (archaeology)', 'Cosine similarity', 'Speedup', 'Similarity (geometry)', 'Computational complexity theory', 'Latency (audio)']
source: openalex-keyword
---

# Efficient Context Filtering for Extractive Question Answering: A Hybrid Approach with Semantic Validation

**저자**: Vahid Ghanbarizadeh; Amin Moeinian; Zahra Younes Pour Langaroudi; Mohsen Mohammadagha; Athar Sharifi
**출처**: Journal of Computer Science and Technology Studies, Vol.8 No.2, pp.01-09
**발행일**: 2026-01-25
**DOI**: https://doi.org/10.32996/jcsts.2026.8.2.1
**수집 키워드**: text analysis

## 초록

Extractive question answering on lengthy documents remains computationally expensive due to quadratic attention complexity and context truncation requirements in modern language models. This work proposes a hybrid context filtering framework that combines classical similarity metrics, including cosine similarity and Word Mover’s Distance, with the Bitap algorithm, and utilizes selective LLM-based validation to reduce inference cost while maintaining competitive accuracy. The method filters irrelevant sentences before passage encoding, thereby reducing computational overhead without requiring learned retrieval components. Evaluation on SQuAD 2.0 across four open-source models (Llama 2 8B, T5-3B, Flan-T5-XL, mT5-Base) using 5-shot learning and fine-tuning demonstrates a 2.3 inference speedup and 58% latency reduction with a modest accuracy trade-off of 5.7% relative F1 degradation compared to full-context baselines. Component ablation confirms the synergistic contribution of each similarity metric, while robustness evaluation across various context lengths and out-of-distribution settings validates the method’s generalization capabilities. These results indicate that intelligent, parameter-free context filtering can achieve meaningful computational efficiency without necessitating complex learned retrievers.

## 키워드

Inference, Robustness (evolution), Context (archaeology), Cosine similarity, Speedup, Similarity (geometry), Computational complexity theory, Latency (audio)

## 주제 분류 (OpenAlex Topics)

- Topic Modeling (score: 0.950)
- Natural Language Processing Techniques (score: 0.010)
- Information Retrieval and Search Behavior (score: 0.004)

## 메모

