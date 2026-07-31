---
title: "Uncertainty-Aware Expert Allocation for Efficient Multitask Fine-Tuning of Large Language Models"
authors: ['Maab Elhassan', 'Minhee Jun', 'Hanseok Ko']
year: 2026
venue: "Data"
tags: ['Artificial Intelligence in Healthcare and Education', 'Topic Modeling', 'Machine Learning in Healthcare']
source: raw/applied/applied_2026_UncertaintyAware_Expert_A_data11070172.md
---

# Uncertainty-Aware Expert Allocation for Efficient Multitask Fine-Tuning of Large Language Models

**저자**: Maab Elhassan; Minhee Jun; Hanseok Ko
**출처**: Data, Vol.11, pp.172-172
**발행일**: 2026-07-10
**DOI**: https://doi.org/10.3390/data11070172

## 초록 (원문)

Large Language Models increasingly rely on Mixture-of-Experts architectures to scale model capacity while controlling computational cost. However, most MoE systems employ static expert routing strategies that allocate identical computational resources to all tokens, regardless of their uncertainty or difficulty. This paper proposes Confidence-Based Dynamic Routing (CBDR), an uncertainty-aware expert allocation mechanism for multitask fine-tuning of large language models. CBDR estimates token-level confidence from the entropy of the gating distribution and dynamically adjusts the number of activated experts accordingly. Tokens with high confidence are processed with fewer experts, while uncertain tokens receive additional expert capacity. To mitigate expert imbalance, we introduce Confidence-Based Importance Balancing (CBIB), a training objective that encourages balanced expert utilization. Experiments on multiple biomedical question-answering datasets demonstrate that CBDR improves model performance across multiple biomedical QA datasets, achieving absolute improvements of up to 3% in F1 score on the BioASQ benchmark while maintaining efficient expert utilization. These results suggest that uncertainty-aware routing provides a practical mechanism for adaptive compute allocation in sparse large language models.

## 키워드

Language model, Expert system, Benchmark (surveying), Entropy (arrow of time), Principle of maximum entropy, Routing (electronic design automation)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

