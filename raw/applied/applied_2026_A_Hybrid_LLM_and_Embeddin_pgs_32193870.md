---
title: "A Hybrid LLM and Embedding-Based Approach for Biomedical Concept Normalization in Clinical and Social Media Data"
authors: ['Iram Azam']
year: 2026
publication_date: 2026-05-07
venue: "Purdue"
volume: "None"
issue: "None"
pages: ""
doi: "https://doi.org/10.25394/pgs.32193870"
oa_status: "green"
openalex_id: "https://openalex.org/W7160548299"
query_keyword: "text analysis"
tags: ['Topic Modeling', 'Machine Learning in Healthcare', 'Mental Health via Writing']
keywords: ['Unified Medical Language System', 'Normalization (sociology)', 'Terminology', 'Social media', 'Named-entity recognition', 'Information extraction', 'Natural language', 'Biomedical text mining']
source: openalex-keyword
---

# A Hybrid LLM and Embedding-Based Approach for Biomedical Concept Normalization in Clinical and Social Media Data

**저자**: Iram Azam
**출처**: Purdue
**발행일**: 2026-05-07
**DOI**: https://doi.org/10.25394/pgs.32193870
**수집 키워드**: text analysis

## 초록

Biomedical concept normalization (BCN) is a fundamental task in natural language processing (NLP) that maps diverse health-related expressions to standardized concepts within biomedical knowledge bases such as the Unified Medical Language System (UMLS). This process is essential for supporting clinical decision-making, public health surveillance, and large-scale biomedical data integration. However, accurate normalization remains challenging due to substantial linguistic variability across data sources. Clinical text often contains domain-specific terminology and abbreviations, whereas social media data introduces informal language, misspellings, paraphrases, and metaphorical expressions that limit the effectiveness of traditional lexical approaches.This study proposes a unified hybrid framework that integrates large language models (LLMs) with biomedical embeddings to address these challenges. The approach leverages SapBERT embeddings and FAISS-based similarity search for semantic retrieval over UMLS concepts. LLMs are used to generate medically grounded preferred terms (PTs) from informal expressions, reducing linguistic variability prior to embedding-based retrieval.The framework is evaluated on COVID-19–related datasets, including free text in electronic health record (EHR) and multiple Twitter (X) datasets. For clinical normalization (3,144 phrases), the embedding-based approach achieved an accuracy of 0.858 (F1 = 0.924), outperforming exact string matching (0.679) and MetaMap Lite (0.579). For Twitter phrase-level normalization (102 phrases), performance improved from 0.235 (string matching) and 0.118 (MetaMap Lite) to as high as 0.980 accuracy and 0.990 F1 using LLM-assisted normalization.To demonstrate applicability to unstructured real-world data, the framework was extended to full tweets (600 tweets), where LLM-based symptom extraction was incorporated as a prior step, enabling biomedical entity linking (BEL). The symptom extraction component achieved micro-level F1-scores of 0.906 (exact match) and 0.930 (semantic match).Overall, the results demonstrate that embedding-based semantic retrieval improves normalization in clinical text, while LLM-assisted linguistic standardization is critical for handling informal social media expressions. The proposed hybrid framework provides an accurate and robust solution for biomedical concept normalization and entity linking across heterogeneous data sources, supporting applications in public health informatics and biomedical text analysis.

## 키워드

Unified Medical Language System, Normalization (sociology), Terminology, Social media, Named-entity recognition, Information extraction, Natural language, Biomedical text mining, String searching algorithm

## 주제 분류 (OpenAlex Topics)

- Topic Modeling (score: 0.618)
- Machine Learning in Healthcare (score: 0.250)
- Mental Health via Writing (score: 0.026)

## 메모

