---
title: "The legalization of international instruments: a hybrid RAG scoring framework based on chain-of-thought prompting"
authors: ['Yan Chen', 'Zihua Zeng', 'M. S. Hassan']
year: 2026
publication_date: 2026-07-09
venue: "Frontiers in Artificial Intelligence"
volume: "9"
issue: "None"
pages: ""
doi: "https://doi.org/10.3389/frai.2026.1784200"
oa_status: "gold"
openalex_id: "https://openalex.org/W7167851908"
query_keyword: "text analysis"
tags: ['Computational and Text Analysis Methods', 'Artificial Intelligence Applications', 'Legal Language and Interpretation']
keywords: ['Legalization', 'Process (computing)', 'Ranking (information retrieval)', 'Coding (social sciences)', 'Baseline (sea)', 'Test (biology)']
source: openalex-keyword
---

# The legalization of international instruments: a hybrid RAG scoring framework based on chain-of-thought prompting

**저자**: Yan Chen; Zihua Zeng; M. S. Hassan
**출처**: Frontiers in Artificial Intelligence, Vol.9
**발행일**: 2026-07-09
**DOI**: https://doi.org/10.3389/frai.2026.1784200
**수집 키워드**: text analysis

## 초록

Introduction Accurately evaluating the degree of legalization of international instruments is analytically valuable for assessing the level of institutionalization of interstate cooperative arrangements. However, conventional assessment approaches rely heavily on specialized legal expertise, and the inherent efficiency constraints of manual analysis make systematic evaluation across large-scale instrument corpora exceedingly difficult. Methods To address the lack of automated scoring tools in this domain, this study introduces a hybrid retrieval-augmented generation (RAG) scoring framework based on chain-of-thought (CoT) prompting. Based on the legalization conceptual framework proposed by Abbott and Snidal, this study constructs a five-level coding standard that covers the three dimensions of obligation, precision, and delegation, and accordingly designs a stepwise binary decision process to develop the corresponding CoT prompt template. In parallel, this study constructs a vector-indexed clause database comprising 2,611 expert-annotated samples from the ASEAN instrument corpus, providing retrieval-augmented semantic references for the scoring task. The retrieval mechanism incorporates an adaptive quality-weighted ranking strategy and employs an additional pre-trained model to perform secondary filtering of candidate results. To evaluate the effectiveness of the scoring framework, two independent test sets were constructed from ASEAN instruments and documents from other major regional organizations, respectively, containing 254 and 255 expert-annotated samples. Results GPT-5.2 and GPT-4o, based on this architecture, significantly outperform the baseline prompting strategy, traditional machine learning methods (TF-IDF+LR), and the fine-tuned pre-trained language model (Legal-BERT) on the international instrument scoring task. Among all evaluated models, GPT-5.2 exhibits the strongest overall performance. Based on the averaged outcomes of three independent runs, the model attained QWK scores of 0.806 and 0.788, and MAE scores of 0.089 and 0.084, on the ASEAN instrument test set and the test set of other major regional organizations, respectively, demonstrating a substantially high degree of agreement with human expert ratings. Discussion These findings indicate that integrating CoT prompting with the RAG pipeline improves LLM performance in scoring the degree of legalization of international legal documents. This provides methodological and technical foundations for large-scale institutional empirical analysis in ASEAN and broader legal systems, and points toward future extensions of the framework to other regional and multilateral legal orders.

## 키워드

Legalization, Process (computing), Ranking (information retrieval), Coding (social sciences), Baseline (sea), Test (biology)

## 주제 분류 (OpenAlex Topics)

- Computational and Text Analysis Methods (score: 0.137)
- Artificial Intelligence Applications (score: 0.039)
- Legal Language and Interpretation (score: 0.022)

## 메모

