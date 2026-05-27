---
title: "Is One Score Enough? Rethinking the Evaluation of Sequentially Evolving LLM Memory"
authors: ['Songwei Dong', 'Zihan Chen', 'Chengshuai Shi', 'Peng Wang', 'Jundong Li', 'Cong Shen']
year: 2026
publication_date: 2026-05-14
venue: "ArXiv.org"
volume: "None"
issue: "None"
pages: ""
doi: ""
oa_status: "green"
openalex_id: "https://openalex.org/W7161655685"
query_keyword: "text analysis"
tags: ['Domain Adaptation and Few-Shot Learning', 'Topic Modeling', 'Multimodal Machine Learning Applications']
keywords: ['Forgetting', 'Aggregate (composite)', 'Memory model', 'Reuse', 'Stability (learning theory)', 'Property (philosophy)', 'Adaptability']
source: openalex-keyword
---

# Is One Score Enough? Rethinking the Evaluation of Sequentially Evolving LLM Memory

**저자**: Songwei Dong; Zihan Chen; Chengshuai Shi; Peng Wang; Jundong Li; Cong Shen
**출처**: ArXiv.org
**발행일**: 2026-05-14
**DOI**: 
**수집 키워드**: text analysis

## 초록

Memory plays a central role in enabling large language models (LLMs) to operate over sequential tasks by accumulating and reusing experience over time. However, existing evaluations of LLM memory mostly rely on aggregate metrics such as final hold-out accuracy or cumulative online performance, which can obscure critical failure modes such as forgetting and negative transfer. In this paper, we introduce SeqMem-Eval, a diagnostic evaluation framework for sequentially evolving LLM memory. Drawing inspiration from continual learning, it targets a test-time setting in which memory is external, prompt-mediated, and updated without modifying model parameters. Rather than focusing only on final performance, SeqMem-Eval evaluates how memory states evolve, generalize, consolidate experience, and retain useful information during sequential inference. Specifically, it measures online utility, hold-out generalization, backward transfer, and forgetting, providing a finer-grained view of memory quality. Through extensive experiments across diverse tasks and memory methods, we show that higher final or cumulative accuracy does not necessarily imply better memory quality: many methods exhibit strong performance gains while suffering from substantial forgetting or negative transfer. Moreover, different memory designs exhibit distinct trade-offs between adaptability and stability that remain invisible under standard evaluation metrics.

## 키워드

Forgetting, Aggregate (composite), Memory model, Reuse, Stability (learning theory), Property (philosophy), Adaptability

## 주제 분류 (OpenAlex Topics)

- Domain Adaptation and Few-Shot Learning (score: 0.380)
- Topic Modeling (score: 0.240)
- Multimodal Machine Learning Applications (score: 0.045)

## 메모

