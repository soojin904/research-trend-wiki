---
title: "LawLLM-DS: A Two-Stage LoRA Framework for Multi-Label Legal Judgment Prediction with Structured Label Dependencies"
authors: ['Pengcheng Zhao', 'Chengcheng Han', 'Kun Han']
year: 2026
publication_date: 2026-01-13
venue: "Symmetry"
volume: "18"
issue: "1"
pages: "150-150"
doi: "https://doi.org/10.3390/sym18010150"
oa_status: "gold"
openalex_id: "https://openalex.org/W7123873249"
query_keyword: "text analysis"
tags: ['Artificial Intelligence in Law', 'Topic Modeling', 'Explainable Artificial Intelligence (XAI)']
keywords: ['Structured prediction', 'Transformer', 'Graph', 'Adapter (computing)', 'Collision', 'Adaptation (eye)', 'Projection (relational algebra)']
source: openalex-keyword
---

# LawLLM-DS: A Two-Stage LoRA Framework for Multi-Label Legal Judgment Prediction with Structured Label Dependencies

**저자**: Pengcheng Zhao; Chengcheng Han; Kun Han
**출처**: Symmetry, Vol.18 No.1, pp.150-150
**발행일**: 2026-01-13
**DOI**: https://doi.org/10.3390/sym18010150
**수집 키워드**: text analysis

## 초록

Legal judgment prediction (LJP) increasingly relies on large language models whose full fine-tuning is memory-intensive and susceptible to catastrophic forgetting. We present LawLLM-DS, a two-stage Low-Rank Adaptation (LoRA) framework that first performs legal knowledge pre-tuning with an aggressive learning rate and subsequently refines judgment relations with conservative updates, using dedicated LoRA adapters, 4-bit quantization, and targeted modification of seven Transformer projection matrices to keep only 0.21% of parameters trainable. From a structural perspective, the twenty annotated legal elements form a symmetric label co-occurrence graph that exhibits both cluster-level regularities and asymmetric sparsity patterns, and LawLLM-DS implicitly captures these graph-informed dependencies while remaining compatible with downstream GNN-based representations. Experiments on 5096 manually annotated divorce cases show that LawLLM-DS lifts macro F1 to 0.8893 and achieves an accuracy of 0.8786, outperforming single-stage LoRA and BERT baselines under the same data regime. Ablation studies further verify the contributions of stage-wise learning rates, adapter placement, and low-rank settings. These findings demonstrate that curriculum-style, parameter-efficient adaptation provides a practical path toward lightweight yet structure-aware LJP systems for judicial decision support.

## 키워드

Structured prediction, Transformer, Graph, Adapter (computing), Collision, Adaptation (eye), Projection (relational algebra)

## 주제 분류 (OpenAlex Topics)

- Artificial Intelligence in Law (score: 0.431)
- Topic Modeling (score: 0.182)
- Explainable Artificial Intelligence (XAI) (score: 0.025)

## 메모

