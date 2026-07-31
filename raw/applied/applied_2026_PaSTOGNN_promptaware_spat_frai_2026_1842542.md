---
title: "PaSTO-GNN: prompt-aware spatio-temporal graph neural networks for automatic essay scoring"
authors: ['Areej Alhothali']
year: 2026
publication_date: 2026-07-08
venue: "Frontiers in Artificial Intelligence"
volume: "9"
issue: "None"
pages: "1842542-1842542"
doi: "https://doi.org/10.3389/frai.2026.1842542"
oa_status: "gold"
openalex_id: "https://openalex.org/W7167689348"
query_keyword: "text analysis"
tags: ['Writing and Handwriting Education', 'Topic Modeling', 'Mental Health via Writing']
keywords: ['Sentence', 'ENCODE', 'Node (physics)', 'Graph', 'Feature (linguistics)', 'Artificial neural network', 'Representation (politics)', 'Set (abstract data type)']
source: openalex-keyword
---

# PaSTO-GNN: prompt-aware spatio-temporal graph neural networks for automatic essay scoring

**저자**: Areej Alhothali
**출처**: Frontiers in Artificial Intelligence, Vol.9, pp.1842542-1842542
**발행일**: 2026-07-08
**DOI**: https://doi.org/10.3389/frai.2026.1842542
**수집 키워드**: text analysis

## 초록

Automatic Essay Scoring (AES) aims to evaluate the quality of written essays automatically, providing fast, consistent, and objective assessments of students' writing ability. Existing deep learning approaches-including recurrent, convolutional, and transformer-based models-primarily focus on textual semantics, yet they often overlook the spatio-temporal nature of essay composition, where meaning evolves across sentences and paragraphs through discourse progression. To address this gap, this study presents a prompt-aware Spatio-Temporal Graph Neural Network (PaSTO-GNN) for AES. In this framework, each essay is first segmented into sentences, and each sentence is represented as a node in a spatio-temporal graph. The feature representation of each node is constructed by combining contextual sentence embeddings extracted from a RoBERTa encoder adapted via Low-Rank Adaptation (LoRA), semantic embeddings obtained from Sentence-BERT (SBERT), and a learned prompt embedding that conditions scoring on the essay prompt. Spatial edges capture semantic relationships between sentences, while temporal edges encode the sequential progression of ideas throughout the essay. The resulting node representations are processed through a spatio-temporal message passing network, followed by a BiGRU layer and temporal attention pooling to obtain a global essay representation. To model the ordered nature of essay scores, prompt-specific ordinal prediction heads based on CORAL are employed, together with a per-prompt calibration step that better aligns predicted scores with human scoring distributions. Experimental results on the AES 2.0 benchmark dataset show that PaSTO-GNN achieves a Quadratic Weighted Kappa (QWK) of 0.8329 on the validation set after prompt calibration and a Pearson correlation of 0.8168, highlighting the effectiveness of combining spatio-temporal discourse modeling with prompt-aware representations for automated essay evaluation.

## 키워드

Sentence, ENCODE, Node (physics), Graph, Feature (linguistics), Artificial neural network, Representation (politics), Set (abstract data type), Meaning (existential), Benchmark (surveying)

## 주제 분류 (OpenAlex Topics)

- Writing and Handwriting Education (score: 0.335)
- Topic Modeling (score: 0.223)
- Mental Health via Writing (score: 0.171)

## 메모

