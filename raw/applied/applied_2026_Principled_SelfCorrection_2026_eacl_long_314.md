---
title: "Principled Self-Correction in Discrete Diffusion: A UCB-Guided Framework for Text Generation"
authors: ['Masaki Asada', 'Makoto Miwa']
year: 2026
publication_date: 2026-01-01
venue: ""
volume: "None"
issue: "None"
pages: "6678-6692"
doi: "https://doi.org/10.18653/v1/2026.eacl-long.314"
oa_status: "gold"
openalex_id: "https://openalex.org/W7140146919"
query_keyword: "text analysis"
tags: ['Natural Language Processing Techniques', 'Topic Modeling', 'Digital Humanities and Scholarship']
keywords: ['Feature (linguistics)', 'Identification (biology)', 'Context (archaeology)', 'Sequence (biology)']
source: openalex-keyword
---

# Principled Self-Correction in Discrete Diffusion: A UCB-Guided Framework for Text Generation

**저자**: Masaki Asada; Makoto Miwa
**출처**: , pp.6678-6692
**발행일**: 2026-01-01
**DOI**: https://doi.org/10.18653/v1/2026.eacl-long.314
**수집 키워드**: text analysis

## 초록

Inspired by their success in image synthesis, diffusion models offer a flexible, iterative alternative to rigid left-to-right text generation.However, a fundamental training-inference discrepancy hinders their performance: models are trained on corrupted ground-truth tokens, but at inference time they must denoise inputs corrupted from their own predictions.To bridge this gap, we propose a unified framework.First, Deeper Self-Prediction (DSP) is a multi-step training objective that teaches robust self-correction by forcing the model to denoise its own intermediate outputs.Second, UCB-guided Decoding is a principled inference algorithm that frames token re-masking as a multi-armed bandit problem, using the Upper Confidence Bound (UCB) to balance exploration and exploitation.Experiments on text generation tasks demonstrate consistent improvements over existing diffusion baselines.The framework achieves higher faithfulness and coherence according to both automatic metrics and LLM-as-a-Judge evaluations.

## 키워드

Feature (linguistics), Identification (biology), Context (archaeology), Sequence (biology)

## 주제 분류 (OpenAlex Topics)

- Natural Language Processing Techniques (score: 0.213)
- Topic Modeling (score: 0.188)
- Digital Humanities and Scholarship (score: 0.060)

## 메모

