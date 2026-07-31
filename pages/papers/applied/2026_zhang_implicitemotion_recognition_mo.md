---
title: "Implicit-Emotion Recognition Model Based on Content–Style Decoupling and Conditional Fusion"
authors: ['Yu Zhang', 'Junqing Zhu', 'Hua Zhao']
year: 2026
venue: "Electronics"
tags: ['Emotion and Mood Recognition', 'Sentiment Analysis and Opinion Mining', 'Mental Health via Writing']
source: raw/applied/applied_2026_ImplicitEmotion_Recogniti_electronics15143002.md
---

# Implicit-Emotion Recognition Model Based on Content–Style Decoupling and Conditional Fusion

**저자**: Yu Zhang; Junqing Zhu; Hua Zhao
**출처**: Electronics, Vol.15, pp.3002-3002
**발행일**: 2026-07-08
**DOI**: https://doi.org/10.3390/electronics15143002

## 초록 (원문)

Implicit-emotional expressions are common in college students’ social media posts, where literal meanings may contradict underlying emotions. Bidirectional Encoder Representations from Transformers (BERT)-based models face two coupled challenges in this setting: feature confusion between semantic content and expression style, and coarse-grained feature fusion. We propose CSD-IFRN (Content–Style Disentanglement with Conditional Fusion for Implicit Emotion Recognition Network), which disentangles content and style using dual non-shared BERT encoders, combines gradient-reversal adversarial training with a content–style orthogonality regularizer (Lorth), and applies conditional layer normalization (CLN) for adaptive fusion. On a dedicated dataset of 11,154 triple-annotated texts, averaged over five random seeds, CSD-IFRN achieves 88.58% accuracy and 88.43% macro-F1, improving over BERT-base-chinese by 6.99 points and over the strongest SOTA baseline by 2.61 points. The main gains remain significant after Holm correction (p &lt; 0.01) and also hold on a public benchmark. A frozen style probe trained on content features falls to 50.40% balanced accuracy, close to chance level, supporting effective disentanglement. Among fusion strategies, CLN achieves the best accuracy with low seed-to-seed variance. These results suggest that CSD-IFRN can provide an auxiliary signal for university mental-health monitoring, rather than a clinical diagnostic tool.

## 키워드

Normalization (sociology), Encoder, Pattern recognition (psychology), Fusion, Feature (linguistics), Orthogonality, Autoencoder, Decoupling (probability)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

