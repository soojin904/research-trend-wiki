---
title: "Uncertainty-Aware Expert Allocation for Efficient Multitask Fine-Tuning of Large Language Models"
authors: ['Maab Elhassan', 'Minhee Jun', 'Hanseok Ko']
year: 2026
publication_date: 2026-07-10
venue: "Data"
volume: "11"
issue: "7"
pages: "172-172"
doi: "https://doi.org/10.3390/data11070172"
oa_status: "gold"
openalex_id: "https://openalex.org/W7167918162"
query_keyword: "text analysis"
tags: ['Artificial Intelligence in Healthcare and Education', 'Topic Modeling', 'Machine Learning in Healthcare']
keywords: ['Language model', 'Expert system', 'Benchmark (surveying)', 'Entropy (arrow of time)', 'Principle of maximum entropy', 'Routing (electronic design automation)']
source: openalex-keyword
---

# Uncertainty-Aware Expert Allocation for Efficient Multitask Fine-Tuning of Large Language Models

**저자**: Maab Elhassan; Minhee Jun; Hanseok Ko
**출처**: Data, Vol.11 No.7, pp.172-172
**발행일**: 2026-07-10
**DOI**: https://doi.org/10.3390/data11070172
**수집 키워드**: text analysis

## 초록

Large Language Models increasingly rely on Mixture-of-Experts architectures to scale model capacity while controlling computational cost. However, most MoE systems employ static expert routing strategies that allocate identical computational resources to all tokens, regardless of their uncertainty or difficulty. This paper proposes Confidence-Based Dynamic Routing (CBDR), an uncertainty-aware expert allocation mechanism for multitask fine-tuning of large language models. CBDR estimates token-level confidence from the entropy of the gating distribution and dynamically adjusts the number of activated experts accordingly. Tokens with high confidence are processed with fewer experts, while uncertain tokens receive additional expert capacity. To mitigate expert imbalance, we introduce Confidence-Based Importance Balancing (CBIB), a training objective that encourages balanced expert utilization. Experiments on multiple biomedical question-answering datasets demonstrate that CBDR improves model performance across multiple biomedical QA datasets, achieving absolute improvements of up to 3% in F1 score on the BioASQ benchmark while maintaining efficient expert utilization. These results suggest that uncertainty-aware routing provides a practical mechanism for adaptive compute allocation in sparse large language models.

## 키워드

Language model, Expert system, Benchmark (surveying), Entropy (arrow of time), Principle of maximum entropy, Routing (electronic design automation)

## 주제 분류 (OpenAlex Topics)

- Artificial Intelligence in Healthcare and Education (score: 0.299)
- Topic Modeling (score: 0.198)
- Machine Learning in Healthcare (score: 0.164)

## 메모

