---
title: "Knowledge-enhanced LLMs for multilingual biomedical concept normalization: a multilingual benchmarking and behavioral analysis"
authors: ['Hossein Rouhizadeh', 'Anthony Yazdani', 'Boya Zhang', 'David Vicente Alvarez', 'Matthias Hüser', 'Alexandre Vanobberghen', 'Rui Yang', 'Huitao Li', 'Nan Liu', 'Andreas Walter', 'Douglas Teodoro']
year: 2026
publication_date: 2026-09-16
venue: "npj Digital Medicine"
volume: "None"
issue: "None"
pages: ""
doi: "https://doi.org/10.1038/s41746-026-03224-x"
oa_status: "gold"
openalex_id: "https://openalex.org/W7213244871"
query_keyword: "text analysis"
tags: ['Biomedical Text Mining and Ontologies', 'Topic Modeling', 'Machine Learning in Healthcare']
keywords: ['Discriminative model', 'Benchmarking', 'Generative grammar', 'Concatenation (mathematics)', 'Bottleneck', 'Bridging (networking)', 'Interoperability']
source: openalex-keyword
---

# Knowledge-enhanced LLMs for multilingual biomedical concept normalization: a multilingual benchmarking and behavioral analysis

**저자**: Hossein Rouhizadeh; Anthony Yazdani; Boya Zhang; David Vicente Alvarez; Matthias Hüser; Alexandre Vanobberghen; Rui Yang; Huitao Li; Nan Liu; Andreas Walter; Douglas Teodoro
**출처**: npj Digital Medicine
**발행일**: 2026-09-16
**DOI**: https://doi.org/10.1038/s41746-026-03224-x
**수집 키워드**: text analysis

## 초록

Abstract Biomedical concept normalization (BCN)—mapping clinical terms to standardized concepts in biomedical terminologies—is a key bottleneck for semantic interoperability across health information systems, particularly in multilingual settings and when terms appear with minimal surrounding context, as is common in coded fields of real-world electronic health record databases. Large language models (LLMs) offer new opportunities to automate BCN, yet their behavior under these conditions remains poorly understood. This study introduces MedLexAlign, a multilingual benchmark comprising 52,011 unique terms mapped to 22,787 biomedical concepts across five European languages (English, French, German, Spanish, and Turkish). It proposes a knowledge-enhanced retrieve-then-rerank pipeline employing discriminative LLMs as dense retrievers and generative LLMs as rerankers, augmented with structured knowledge from the Unified Medical Language System (UMLS). We evaluate eight discriminative LLMs as dense retrievers and six generative LLMs (8B–32B parameters; across different reasoning modes) as rerankers, examining abbreviation handling, synonym sensitivity, and positional bias. The best-performing dense retriever, nemotron, achieved R@1 of 0.57 and R@10 of 0.80, outperforming kalm-gemma (R@1 = 0.56, R@10 = 0.78; p -value = 0.02). For reranking, UMLS-based knowledge enrichment yielded consistent gains: qwen3-32b-r achieved ΔR@1 of +0.10 with enrichment versus +0.05 without ( p -value < 0.001). However, LLMs exhibited sensitivity to lexical surface forms, handled synonymous representations inconsistently, and showed strong primacy bias toward earlier-ranked candidates. These findings demonstrate that structured knowledge enrichment is critical for effective LLM-based multilingual concept normalization, while surface-form sensitivity and positional biases remain important challenges for fully automated clinical pipelines.

## 키워드

Discriminative model, Benchmarking, Generative grammar, Concatenation (mathematics), Bottleneck, Bridging (networking), Interoperability

## 주제 분류 (OpenAlex Topics)

- Biomedical Text Mining and Ontologies (score: 0.487)
- Topic Modeling (score: 0.217)
- Machine Learning in Healthcare (score: 0.200)

## 메모

