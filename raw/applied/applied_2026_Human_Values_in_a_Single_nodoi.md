---
title: "Human Values in a Single Sentence: Moral Presence, Hierarchies, and Transformer Ensembles on the Schwartz Continuum"
authors: ['Víctor Yeste', 'Paolo Rosso']
year: 2026
publication_date: 2026-01-20
venue: "arXiv (Cornell University)"
volume: "None"
issue: "None"
pages: ""
doi: ""
oa_status: "green"
openalex_id: "https://openalex.org/W7125351122"
query_keyword: "text analysis"
tags: ['Hate Speech and Cyberbullying Detection', 'Sentiment Analysis and Opinion Mining', 'Misinformation and Its Impacts']
keywords: ['Sentence', 'Classifier (UML)', 'Inference', 'Binary number', 'Transformer', 'Binary classification', 'Language model', 'Recall']
source: openalex-keyword
---

# Human Values in a Single Sentence: Moral Presence, Hierarchies, and Transformer Ensembles on the Schwartz Continuum

**저자**: Víctor Yeste; Paolo Rosso
**출처**: arXiv (Cornell University)
**발행일**: 2026-01-20
**DOI**: 
**수집 키워드**: text analysis

## 초록

We study sentence-level detection of the 19 human values in the refined Schwartz continuum in about 74k English sentences from news and political manifestos (ValueEval'24 corpus). Each sentence is annotated with value presence, yielding a binary moral-presence label and a 19-way multi-label task under severe class imbalance. First, we show that moral presence is learnable from single sentences: a DeBERTa-base classifier attains positive-class F1 = 0.74 with calibrated thresholds. Second, we compare direct multi-label value detectors with presence-gated hierarchies in a setting where only a single consumer-grade GPU with 8 GB of VRAM is available, and we explicitly choose all training and inference configurations to fit within this budget. Presence gating does not improve over direct prediction, indicating that gate recall becomes a bottleneck. Third, we investigate lightweight auxiliary signals - short-range context, LIWC-22, and moral lexica - and small ensembles. Our best supervised configuration, a soft-voting ensemble of DeBERTa-based models enriched with such signals, reaches macro-F1 = 0.332 on the 19 values, improving over the best previous English-only baseline on this corpus, namely the best official ValueEval'24 English run (macro-F1 = 0.28 on the same 19-value test set). Methodologically, our study provides, to our knowledge, the first systematic comparison of direct versus presence-gated architectures, lightweight feature-augmented encoders, and medium-sized instruction-tuned Large Language Models (LLMs) for refined Schwartz values at sentence level. We additionally benchmark 7-9B instruction-tuned LLMs (Gemma 2 9B, Llama 3.1 8B, Mistral 8B, Qwen 2.5 7B) in zero-/few-shot and QLoRA setups, and find that they lag behind the supervised ensemble under the same compute budget. Overall, our results provide empirical guidance for building compute-efficient, value-aware NLP models.

## 키워드

Sentence, Classifier (UML), Inference, Binary number, Transformer, Binary classification, Language model, Recall, Benchmark (surveying)

## 주제 분류 (OpenAlex Topics)

- Hate Speech and Cyberbullying Detection (score: 0.395)
- Sentiment Analysis and Opinion Mining (score: 0.188)
- Misinformation and Its Impacts (score: 0.081)

## 메모

