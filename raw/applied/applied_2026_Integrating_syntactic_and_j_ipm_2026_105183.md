---
title: "Integrating syntactic and semantic features for dual-task extraction in Arabic aspect-based sentiment analysis using graph convolutional networks"
authors: ['Dalal Alqusair', 'Mounira Taileb', 'Awny Sayed', 'Hanan Alotaibi']
year: 2026
publication_date: 2026-09-26
venue: "Information Processing & Management"
volume: "64"
issue: "2"
pages: "105183-105183"
doi: "https://doi.org/10.1016/j.ipm.2026.105183"
oa_status: "hybrid"
openalex_id: "https://openalex.org/W7214482887"
query_keyword: "social network"
tags: ['Sentiment Analysis and Opinion Mining', 'Topic Modeling', 'Emotion and Mood Recognition']
keywords: []
source: openalex-keyword
---

# Integrating syntactic and semantic features for dual-task extraction in Arabic aspect-based sentiment analysis using graph convolutional networks

**저자**: Dalal Alqusair; Mounira Taileb; Awny Sayed; Hanan Alotaibi
**출처**: Information Processing & Management, Vol.64 No.2, pp.105183-105183
**발행일**: 2026-09-26
**DOI**: https://doi.org/10.1016/j.ipm.2026.105183
**수집 키워드**: social network

## 초록

Arabic aspect-based sentiment analysis (ABSA) remains underexplored, particularly end-to-end dual-task learning that jointly performs aspect term extraction (ATE) and aspect sentiment classification (ASC). Most existing Arabic ABSA approaches are pipeline-based or restricted to single-task identification, which weakens task synergy, constrains performance, and rarely leverages explicit syntactic structure. To address this gap, we propose a structure-aware, end-to-end model that integrates contextual semantics with linguistic structure to perform ATE and ASC tasks simultaneously. Our architecture builds on contextual representations from an Arabic BERT, augmented with token-level attention and sequential modeling via a BiLSTM. A gated fusion module then learns adaptive weights to combine these features into a unified representation. To incorporate linguistic relations, we introduce a dual-branch graph convolutional network that captures (i) dependency-based syntactic relations and (ii) part-of-speech relational patterns. Both branches use attention-weighted adjacency matrices to reduce sensitivity to parser noise and to emphasize sentiment-relevant links. The proposed model is evaluated on three Arabic ABSA datasets (Hotel, News, and HAAD). It achieves ATE and ASC accuracies of 95.29% and 90.87% on Hotel, 91.85% and 82.15% on News, and 90.96% and 75.06% on HAAD, respectively. Under strict end-to-end exact-match evaluation of aspect–sentiment pairs, the model achieves F1-scores of 71.12%, 64.98%, and 33.81% on the Hotel, News, and HAAD datasets, respectively.

## 키워드

(없음)

## 주제 분류 (OpenAlex Topics)

- Sentiment Analysis and Opinion Mining (score: 0.987)
- Topic Modeling (score: 0.002)
- Emotion and Mood Recognition (score: 0.002)

## 메모

