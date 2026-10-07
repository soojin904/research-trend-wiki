---
title: "Knowledge-enhanced LLMs for multilingual biomedical concept normalization: a multilingual benchmarking and behavioral analysis"
authors: ['Hossein Rouhizadeh', 'Anthony Yazdani', 'Boya Zhang', 'David Vicente Alvarez', 'Matthias Hüser', 'Alexandre Vanobberghen', 'Rui Yang', 'Huitao Li', 'Nan Liu', 'Andreas Walter', 'Douglas Teodoro']
year: 2026
venue: "npj Digital Medicine"
tags: ['Biomedical Text Mining and Ontologies', 'Topic Modeling', 'Machine Learning in Healthcare']
source: raw/applied/applied_2026_Knowledgeenhanced_LLMs_fo_s41746_026_03224_x.md
---

# Knowledge-enhanced LLMs for multilingual biomedical concept normalization: a multilingual benchmarking and behavioral analysis

**저자**: Hossein Rouhizadeh; Anthony Yazdani; Boya Zhang; David Vicente Alvarez; Matthias Hüser; Alexandre Vanobberghen; Rui Yang; Huitao Li; Nan Liu; Andreas Walter; Douglas Teodoro
**출처**: npj Digital Medicine, Vol.None
**발행일**: 2026-09-16
**DOI**: https://doi.org/10.1038/s41746-026-03224-x

## 초록 (원문)

Abstract Biomedical concept normalization (BCN)—mapping clinical terms to standardized concepts in biomedical terminologies—is a key bottleneck for semantic interoperability across health information systems, particularly in multilingual settings and when terms appear with minimal surrounding context, as is common in coded fields of real-world electronic health record databases. Large language models (LLMs) offer new opportunities to automate BCN, yet their behavior under these conditions remains poorly understood. This study introduces MedLexAlign, a multilingual benchmark comprising 52,011 unique terms mapped to 22,787 biomedical concepts across five European languages (English, French, German, Spanish, and Turkish). It proposes a knowledge-enhanced retrieve-then-rerank pipeline employing discriminative LLMs as dense retrievers and generative LLMs as rerankers, augmented with structured knowledge from the Unified Medical Language System (UMLS). We evaluate eight discriminative LLMs as dense retrievers and six generative LLMs (8B–32B parameters; across different reasoning modes) as rerankers, examining abbreviation handling, synonym sensitivity, and positional bias. The best-performing dense retriever, nemotron, achieved R@1 of 0.57 and R@10 of 0.80, outperforming kalm-gemma (R@1 = 0.56, R@10 = 0.78; p -value = 0.02). For reranking, UMLS-based knowledge enrichment yielded consistent gains: qwen3-32b-r achieved ΔR@1 of +0.10 with enrichment versus +0.05 without ( p -value < 0.001). However, LLMs exhibited sensitivity to lexical surface forms, handled synonymous representations inconsistently, and showed strong primacy bias toward earlier-ranked candidates. These findings demonstrate that structured knowledge enrichment is critical for effective LLM-based multilingual concept normalization, while surface-form sensitivity and positional biases remain important challenges for fully automated clinical pipelines.

## 키워드

Discriminative model, Benchmarking, Generative grammar, Concatenation (mathematics), Bottleneck, Bridging (networking), Interoperability

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

