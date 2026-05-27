---
title: "IndoBERT for educational assessment: comparative analysis of transformer models in Indonesian question generation"
authors: ['Handaru Jati', 'Yuniar Indrihapsari', 'Pradana Setialana', 'Danang Wijaya', 'Satya Adhiyaksa Ardy', 'Dhista Dwi Nur Ardiansyah']
year: 2026
venue: "IAES International Journal of Artificial Intelligence"
tags: ['Topic Modeling', 'Text Readability and Simplification', 'Sentiment Analysis and Opinion Mining']
source: raw/applied/applied_2026_IndoBERT_for_educational__ijai_v15_i2_pp1804_1813.md
---

# IndoBERT for educational assessment: comparative analysis of transformer models in Indonesian question generation
**제목(한글)**: 교육 평가를 위한 IndoBERT: 인도네시아어 질문 생성에서 트랜스포머 모델의 비교 분석

**저자**: Handaru Jati; Yuniar Indrihapsari; Pradana Setialana; Danang Wijaya; Satya Adhiyaksa Ardy; Dhista Dwi Nur Ardiansyah
**출처**: IAES International Journal of Artificial Intelligence, Vol.15, pp.1804-1804
**발행일**: 2026-04-01
**DOI**: https://doi.org/10.11591/ijai.v15.i2.pp1804-1813

## 한국어 요약


## 초록 (원문)

This study asks whether a monolingual encoder can realistically outperform multilingual and larger transformer models for Indonesian automatic question generation (AQG) when all models share the same training budget. We compare Indonesian bidirectional encoder representations from transformers (IndoBERT), multilingual BERT (mBERT), and BERT-large using a single fine-tuning pipeline with answer highlighting, applied to an Indonesian version of TyDiQA-GoldP and a 20,000 translated subset of SQuAD 2.0. We evaluate model quality using bilingual evaluation understudy score n-gram 4 (BLEU-4), metric for evaluation of translation with explicit ordering (METEOR), and ROUGE-Lincoln (ROUGE-L). IndoBERT consistently achieves the best scores on both datasets (e.g., BLEU-4 of 19.69 on TyDiQA-GoldP and 3.79 on the SQuAD 2.0 subset) while requiring less computation than mBERT and BERT-large. Our results show that language-specific pretraining gives clear advantages for Indonesian AQG, yielding higher accuracy at lower computational cost than multilingual or larger encoders. The work closes a gap in Indonesian AQG benchmarking by providing the first head-to-head comparison of IndoBERT, mBERT, and BERT-large under a shared fine-tuning and evaluation protocol. For educational assessment, the findings offer a practical recipe for building deployable AQG systems on mid-range GPUs that generate higher quality questions without prohibitive training or inference budgets.

## 키워드

Benchmarking, Transformer, Indonesian, Encoder, Inference, Computation, Metric (unit), Quality (philosophy)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

