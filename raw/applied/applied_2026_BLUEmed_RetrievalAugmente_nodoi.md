---
title: "BLUEmed: Retrieval-Augmented Multi-Agent Debate for Clinical Error Detection"
authors: ['Saukun Thika You', 'Nguyen Anh Khoa Tran', 'Wesley K. Marizane', 'Hanshu Rao', 'Qiunan Zhang', 'Xiaolei Huang']
year: 2026
publication_date: 2026-04-12
venue: "arXiv (Cornell University)"
volume: "None"
issue: "None"
pages: ""
doi: ""
oa_status: "green"
openalex_id: "https://openalex.org/W7154539492"
query_keyword: "text analysis"
tags: ['Topic Modeling', 'Biomedical Text Mining and Ontologies', 'Natural Language Processing Techniques']
keywords: ['Terminology', 'Benchmark (surveying)', 'Domain (mathematical analysis)', 'Substitution (logic)', 'Error detection and correction', 'SNOMED CT', 'Adjudication']
source: openalex-keyword
---

# BLUEmed: Retrieval-Augmented Multi-Agent Debate for Clinical Error Detection

**저자**: Saukun Thika You; Nguyen Anh Khoa Tran; Wesley K. Marizane; Hanshu Rao; Qiunan Zhang; Xiaolei Huang
**출처**: arXiv (Cornell University)
**발행일**: 2026-04-12
**DOI**: 
**수집 키워드**: text analysis

## 초록

Terminology substitution errors in clinical notes, where one medical term is replaced by a linguistically valid but clinically different term, pose a persistent challenge for automated error detection in healthcare. We introduce BLUEmed, a multi-agent debate framework augmented with hybrid Retrieval-Augmented Generation (RAG) that combines evidence-grounded reasoning with multi-perspective verification for clinical error detection. BLUEmed decomposes each clinical note into focused sub-queries, retrieves source-partitioned evidence through dense, sparse, and online retrieval, and assigns two domain expert agents distinct knowledge bases to produce independent analyses; when the experts disagree, a structured counter-argumentation round and cross-source adjudication resolve the conflict, followed by a cascading safety layer that filters common false-positive patterns. We evaluate BLUEmed on a clinical terminology substitution detection benchmark under both zero-shot and few-shot prompting with multiple backbone models spanning proprietary and open-source families. Experimental results show that BLUEmed achieves the best accuracy (69.13%), ROC-AUC (74.45%), and PR-AUC (72.44%) under few-shot prompting, outperforming both single-agent RAG and debate-only baselines. Further analyses across six backbone models and two prompting strategies confirm that retrieval augmentation and structured debate are complementary, and that the framework benefits most from models with sufficient instruction-following and clinical language understanding.

## 키워드

Terminology, Benchmark (surveying), Domain (mathematical analysis), Substitution (logic), Error detection and correction, SNOMED CT, Adjudication

## 주제 분류 (OpenAlex Topics)

- Topic Modeling (score: 0.474)
- Biomedical Text Mining and Ontologies (score: 0.451)
- Natural Language Processing Techniques (score: 0.010)

## 메모

