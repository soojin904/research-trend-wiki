---
title: "A Two-Stage Semi-Supervised Framework for Extractive Summarization of Medical Narratives with Unsupervised Sentence Selection and Fuzzy Alignment-Based Annotation"
authors: ['Meena Elumalai', 'Sivashankari Rajadurai']
year: 2026
publication_date: 2026-01-01
venue: "IEEE Access"
volume: "None"
issue: "None"
pages: "1-1"
doi: "https://doi.org/10.1109/access.2026.3695404"
oa_status: "gold"
openalex_id: "https://openalex.org/W7161755744"
query_keyword: "text analysis"
tags: ['Topic Modeling', 'Machine Learning in Healthcare', 'Biomedical Text Mining and Ontologies']
keywords: ['Automatic summarization', 'Selection (genetic algorithm)', 'Fuzzy logic', 'Sentence', 'Annotation', 'Narrative']
source: openalex-keyword
---

# A Two-Stage Semi-Supervised Framework for Extractive Summarization of Medical Narratives with Unsupervised Sentence Selection and Fuzzy Alignment-Based Annotation

**저자**: Meena Elumalai; Sivashankari Rajadurai
**출처**: IEEE Access, pp.1-1
**발행일**: 2026-01-01
**DOI**: https://doi.org/10.1109/access.2026.3695404
**수집 키워드**: text analysis

## 초록

Purpose: Clinical narratives are frequently lengthy, repetitive, and difficult to understand, thereby diminishing their utility in downstream medical analytics and clinical decision support systems. Transforming unstructured statements into succinct and insightful summaries requires multiple stages of text analysis. However, manual analysis is labor-intensive, time-consuming, and susceptible to human error. Consequently, automated methods for summarizing clinical texts are urgently needed. This research aims to develop a robust extractive summarization framework for clinical documents that efficiently eliminates redundancy and identifies clinically significant sentences without necessitating expensive manual sentence-level annotations. Methods: The proposed approach, a two-stage hybrid extractive summarization framework, was evaluated using a curated subset of the MTSamples clinical dataset. Initially, a traditional unsupervised pipeline was employed, representing sentences using Term Frequency-Inverse Document Frequency (TF-IDF) and SBERT semantic embeddings, ranking them based on centroid similarity, and filtering them via Maximum Marginal Relevance (MMR) to balance relevance and diversity. Subsequently, this framework was transformed into a semi-supervised learning model utilizing fuzzy sentence alignment to enable automatic sentence-level labeling. ClinicalBERT contextual embeddings were combined with engineered structural, clinical, and lexical features to train a feature-augmented ClinicalBERT-BiLSTM architecture for predicting sentence salience. Fuzzy precision, recall, and F1-score at the sentence level, alongside paragraph-level data splits, were utilized to assess performance and prevent information leakage. Results: The proposed hybrid model demonstrated consistent and reliable performance across dataset splits. The model achieved an Overall Precision of 0.51, an Overall Recall of 0.32, and an Overall F1-score of 0.39 on the training set, and 0.49, 0.31, and 0.38 on the validation set. Qualitative analysis revealed that the model effectively selects diagnostically significant sentences while suppressing extraneous procedural information. Furthermore, feature augmentation and redundancy control enhanced sentence relevance recognition relative to purely lexical baselines. Conclusion: This study demonstrates that standard extractive summarization concepts can be efficiently applied to a feature-aware, semi-supervised deep learning framework for clinical material. The proposed approach achieves accurate, interpretable, and scalable extractive summarization of clinical narratives through the integration of centroid-based relevance modeling, redundancy management, and contextual neural representations. This framework is well-suited for real-world clinical applications and provides a solid foundation for future enhancements, including the incorporation of medical knowledge graphs and multi-document summarization.

## 키워드

Automatic summarization, Selection (genetic algorithm), Fuzzy logic, Sentence, Annotation, Narrative

## 주제 분류 (OpenAlex Topics)

- Topic Modeling (score: 0.789)
- Machine Learning in Healthcare (score: 0.053)
- Biomedical Text Mining and Ontologies (score: 0.042)

## 메모

