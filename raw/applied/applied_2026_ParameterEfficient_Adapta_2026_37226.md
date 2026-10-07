---
title: "Parameter-Efficient Adaptation of Modern Pretrained Encoders for Low-Resource Entity-Level Financial Sentiment Classification"
authors: ['Xiang Peng']
year: 2026
publication_date: 2026-09-22
venue: "Applied and Computational Engineering"
volume: "268"
issue: "1"
pages: "None-None"
doi: "https://doi.org/10.54254/2755-2721/2026.37226"
oa_status: "hybrid"
openalex_id: "https://openalex.org/W7213977715"
query_keyword: "text analysis"
tags: ['Sentiment Analysis and Opinion Mining', 'Stock Market Forecasting Methods', 'Topic Modeling']
keywords: ['Encoder', 'Transformer', 'Adaptation (eye)', 'Representation (politics)', 'Domain adaptation', 'Training set', 'Pattern recognition (psychology)']
source: openalex-keyword
---

# Parameter-Efficient Adaptation of Modern Pretrained Encoders for Low-Resource Entity-Level Financial Sentiment Classification

**저자**: Xiang Peng
**출처**: Applied and Computational Engineering, Vol.268 No.1, pp.None-None
**발행일**: 2026-09-22
**DOI**: https://doi.org/10.54254/2755-2721/2026.37226
**수집 키워드**: text analysis

## 초록

Financial news may express different sentiments towards the entities it mentions, while labelled examples for entity-level classification are often limited. This study compares the adaptation of three pretrained encoders to this task on FinEntity: FinBERT, a model based on Bidirectional Encoder Representations from Transformers (BERT) and further pretrained on financial text; DeBERTa-v3-base, the base-sized third version of Decoding-enhanced BERT with disentangled attention; and ModernBERT-base, a modern bidirectional Transformer encoder. Term frequency–inverse document frequency (TF-IDF) features with a linear support vector machine (SVM) serve as the traditional baseline. The pretrained encoders use explicit target-entity markers and a representation combining global and entity information. Three adaptation strategies are considered: full fine-tuning, a frozen encoder and low-rank adaptation (LoRA). Evaluation covers overall classification performance, trainable parameter counts, learning with reduced training data, variation across random seeds, entity representation and transfer to another dataset. In the overall comparison, FinBERT and DeBERTa-v3-base outperform the traditional baseline, whereas ModernBERT-base does not. DeBERTa-v3-base obtains the highest macro-averaged F1 score (Macro-F1) in this comparison. FinBERT performs better at the smallest training budget and produces more consistent results across the tested seeds, indicating that the preferred encoder depends on the evaluation setting. LoRA achieves competitive classification scores with only a small proportion of parameters updated, although this reduction does not shorten training time in the reported experiments. Combining global and target-entity representations improves performance for both encoders evaluated in the ablation study. Without further fine-tuning, the two LoRA models also achieve Macro-F1 scores above 0.70 on SEntFiN, but both score lower than on FinEntity. The results support parameter-efficient adaptation for this task while showing that performance under limited data, consistency across runs and transfer to another dataset require separate consideration.

## 키워드

Encoder, Transformer, Adaptation (eye), Representation (politics), Domain adaptation, Training set, Pattern recognition (psychology)

## 주제 분류 (OpenAlex Topics)

- Sentiment Analysis and Opinion Mining (score: 0.546)
- Stock Market Forecasting Methods (score: 0.190)
- Topic Modeling (score: 0.058)

## 메모

