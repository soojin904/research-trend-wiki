---
title: "Confidence-Guided Dual Representation Learning for Code-Mixed Sentiment Analysis"
authors: ['Sandhya A. Kulkarni', 'N. Kayarvizhy']
year: 2026
venue: "Engineering Technology & Applied Science Research"
tags: ['Sentiment Analysis and Opinion Mining', 'Topic Modeling', 'Hate Speech and Cyberbullying Detection']
source: raw/applied/applied_2026_ConfidenceGuided_Dual_Rep_etasr_20052.md
---

# Confidence-Guided Dual Representation Learning for Code-Mixed Sentiment Analysis

**저자**: Sandhya A. Kulkarni; N. Kayarvizhy
**출처**: Engineering Technology & Applied Science Research, Vol.16, pp.39703-39710
**발행일**: 2026-10-02
**DOI**: https://doi.org/10.48084/etasr.20052

## 초록 (원문)

Sentiment analysis in Kannada-English code-mixed social media text presents unique challenges arising from non-standard orthography, transliteration variability, and the structural dissimilarity between the two languages. This study proposes a Confidence-Guided Dual Representation Learning framework that fine-tunes multilingual BERT (mBERT) and augments it with three specialized components: a Character-level convolutional encoder (CharCNN) for morphological robustness, a language-aware cross-attention mechanism for explicit code-switching modeling, and a supervised contrastive loss for inter-class separation in the embedding space. The architecture incorporates a dedicated confidence head that produces a calibrated scalar confidence score alongside the sentiment prediction, and is trained using a self-supervised binary correctness signal. On a corpus of 6,321 annotated comments, the proposed model achieves a macro-F1 of 0.7566 — the highest among all deep learning models evaluated — with 94.8% macro-F1 retention under combined spelling and transliteration perturbations. Monte Carlo (MC) Dropout uncertainty analysis demonstrates that the model's uncertainty flags are actionable, with high-uncertainty samples achieving 63.3% accuracy compared to 55.7% and 60.1% for XLM-RoBERTa and Multilingual Representations for Indian Languages (MuRIL). Post-hoc temperature scaling further reduces the Expected Calibration Error (ECE) from 0.0417 to 0.0324.

## 키워드

supervised contrastive learning, confidence calibration, temperature scaling, social media text

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

