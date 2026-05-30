---
title: "LawLLM-DS: A Two-Stage Parameter-Efficient Fine-Tuning Framework for Legal Judgment Prediction with Symmetry-Aware Label Graphs"
authors: ['Pengcheng Zhao', 'Chengcheng Han', 'Kun Han']
year: 2025
publication_date: 2025-12-17
venue: "Preprints.org"
volume: "None"
issue: "None"
pages: ""
doi: "https://doi.org/10.20944/preprints202512.1406.v1"
oa_status: "green"
openalex_id: "https://openalex.org/W4417445626"
query_keyword: "text analysis"
tags: ['Artificial Intelligence in Law', 'Topic Modeling', 'Explainable Artificial Intelligence (XAI)']
keywords: ['Transformer', 'Graph', 'Knowledge graph', 'Structured prediction', 'Path (computing)', 'Domain adaptation', 'Training set']
source: openalex-keyword
---

# LawLLM-DS: A Two-Stage Parameter-Efficient Fine-Tuning Framework for Legal Judgment Prediction with Symmetry-Aware Label Graphs

**저자**: Pengcheng Zhao; Chengcheng Han; Kun Han
**출처**: Preprints.org
**발행일**: 2025-12-17
**DOI**: https://doi.org/10.20944/preprints202512.1406.v1
**수집 키워드**: text analysis

## 초록

Legal judgment prediction (LJP) increasingly relies on large language models whose full fine-tuning is memory-intensive and susceptible to catastrophic forgetting. We present LawLLM-DS, a two-stage Low-Rank Adaptation (LoRA) framework that first performs legal knowledge pre-tuning with an aggressive learning rate and subsequently refines judgment relations with conservative updates, using dedicated LoRA adapters, 4-bit quantization, and targeted modification of seven Transformer projection matrices to keep only 0.21% of parameters trainable. From a structural perspective, the twenty annotated legal elements form a symmetric label co-occurrence graph that exhibits both cluster-level regularities and asymmetric sparsity patterns, and LawLLM-DS implicitly captures these graph-informed dependencies while remaining compatible with downstream GNN-based representations. Experiments on 5,096 manually annotated divorce cases show that LawLLM-DS lifts macro F1 to 0.8893 and achieves an accuracy of 0.8786, outperforming single-stage LoRA and BERT baselines under the same data regime. Ablation studies further verify the contributions of stage-wise learning rates, adapter placement, and low-rank settings. These findings demonstrate that curriculum-style, parameter-efficient adaptation provides a practical path toward lightweight yet structure-aware LJP systems for judicial decision support.

## 키워드

Transformer, Graph, Knowledge graph, Structured prediction, Path (computing), Domain adaptation, Training set

## 주제 분류 (OpenAlex Topics)

- Artificial Intelligence in Law (score: 0.626)
- Topic Modeling (score: 0.072)
- Explainable Artificial Intelligence (XAI) (score: 0.036)

## 메모

