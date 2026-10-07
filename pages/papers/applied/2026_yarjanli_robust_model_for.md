---
title: "A robust model for improving digital marketing using sentiment analysis and two-agent off-policy proximal policy optimization"
authors: ['Mohammad Yarjanli', 'Neda Mahdinasab']
year: 2026
venue: "Scientific Reports"
tags: ['Sentiment Analysis and Opinion Mining', 'Digital Marketing and Social Media', 'Topic Modeling']
source: raw/applied/applied_2026_A_robust_model_for_improv_s41598_026_71894_4.md
---

# A robust model for improving digital marketing using sentiment analysis and two-agent off-policy proximal policy optimization

**저자**: Mohammad Yarjanli; Neda Mahdinasab
**출처**: Scientific Reports, Vol.None
**발행일**: 2026-10-04
**DOI**: https://doi.org/10.1038/s41598-026-71894-4

## 초록 (원문)

Understanding consumer sentiment is important in digital marketing because it strongly influences brand perception and purchasing decisions. This paper proposes a novel two-agent off-policy proximal policy optimization (PPO) framework. Unlike standard multi-agent reinforcement learning (RL) approaches, the proposed framework uses a two-agent off-policy PPO design. It combines an active learning (AL) agent for sample selection with a sentiment analysis (SA) agent to improve labeling efficiency and classification robustness. Current SA methods often face challenges related to labeling efficiency, feature selection, class imbalance, generalization, and hyperparameter optimization. Unlike existing SA approaches that tackle these challenges independently, the proposed framework addresses them within a unified learning workflow. To address these challenges, the proposed two‑agent framework has the first agent select the most informative unlabeled samples for annotation. This reduces labeling costs. The second agent then performs SA. Within the second agent, local interpretable model‑agnostic explanations (LIME) guides feature selection. Augmented rewards are also used to improve the recognition of underrepresented classes. A relational generative adversarial network framework enhanced with gradient signal exclusion (RelGANGE) is used for online data augmentation. To increase sample diversity, the generator in RelGANGE ignores gradients from samples that receive high discriminator weights. Hyperparameters are optimized using Bayesian optimization hyperband (BOHB). Comprehensive evaluations on the Amazon Instant Video (AIV), Amazon Apps and Games Reviews (AA), and Yelp datasets were conducted using 5-fold cross-validation. The proposed framework achieved F-measure scores of 95.163%, 95.580%, and 93.054%, respectively. These results significantly outperformed traditional and transformer-based baselines. Statistical analyses confirmed that the improvements were significant ( p < 0.01). The findings demonstrate the effectiveness of the proposed framework for e-commerce recommendation systems (RSs) and decision-support applications.

## 키워드

sentiment analysis, active learning (machine learning), label efficiency, class imbalance, generative adversarial network data augmentation, e-commerce recommendation systems, consumer confidence, online reviews

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

