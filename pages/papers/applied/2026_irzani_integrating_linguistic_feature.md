---
title: "Integrating Linguistic Features with IndoBERT for Detecting Underage-Associated Comments in Indonesian YouTube"
authors: ['Inez Nurdika Irzani', 'Maya Rini Handayani', 'Dwi Pebrianti', 'Khothibul Umam']
year: 2026
venue: "Applied Information System and Management (AISM)"
tags: ['Hate Speech and Cyberbullying Detection', 'Text and Document Classification Technologies', 'Sentiment Analysis and Opinion Mining']
source: raw/applied/applied_2026_Integrating_Linguistic_Fe_aism_v9i2_53149.md
---

# Integrating Linguistic Features with IndoBERT for Detecting Underage-Associated Comments in Indonesian YouTube

**저자**: Inez Nurdika Irzani; Maya Rini Handayani; Dwi Pebrianti; Khothibul Umam
**출처**: Applied Information System and Management (AISM), Vol.9, pp.343-356
**발행일**: 2026-10-09
**DOI**: https://doi.org/10.15408/aism.v9i2.53149

## 초록 (원문)

Indonesia has issued Government Regulation No. 17 of 2025 on Electronic System Governance for Child Protection (PP TUNAS), which prohibits independent access to digital platforms for individuals under 16. However, age verification remains difficult since users may provide fake birth dates during registration. This study aims to develop a hybrid text classification framework that integrates IndoBERT contextual embeddings with eight handcrafted linguistic features (teen_score, adult_score, emotion_score, grammar_score, word_count, exclamation_count, question_count, and teen_adult_ratio) to identify underage-associated comments on Indonesian YouTube. This study collected 37,450 comments from 271 videos using the YouTube Data API v3 and validated annotation consistency through manual labeling of 500 stratified samples, achieving Cohen's Kappa of 0.853 (almost perfect agreement). To address severe class imbalance, in which under-16 samples accounted for only 1.64%, then applied stratified 5-fold cross-validation with weighted sampling. The hybrid model achieved F1-scores of 0.7777 ± 0.0680 (cross-validation) and 0.9609 (test set). Ablation experiments confirmed explicit age disclosures are essential for the current annotation strategy. Although no significant performance difference was observed versus IndoBERT-only (p = 0.5743), the hybrid model provides explicit linguistic evidence through SHAP and LIME analyses, substantially improving interpretability. This makes the proposed framework suitable for transparent policy-oriented comment screening under PP TUNAS.

## 키워드

child online protection, IndoBERT, Indonesian language, YouTube comments, age verification, linguistic features, class imbalance, interpretability

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

