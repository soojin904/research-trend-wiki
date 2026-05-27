---
title: "A Two-Stage Semi-Supervised Framework for Extractive Summarization of Medical Narratives with Unsupervised Sentence Selection and Fuzzy Alignment-Based Annotation"
authors: ['Meena Elumalai', 'Sivashankari Rajadurai']
year: 2026
venue: "IEEE Access"
tags: ['Topic Modeling', 'Machine Learning in Healthcare', 'Biomedical Text Mining and Ontologies']
source: raw/applied/applied_2026_A_TwoStage_SemiSupervised_access_2026_3695404.md
---

# A Two-Stage Semi-Supervised Framework for Extractive Summarization of Medical Narratives with Unsupervised Sentence Selection and Fuzzy Alignment-Based Annotation
**제목(한글)**: 비지도 문장 선택 및 퍼지 정렬 기반 어노테이션을 활용한 의료 서사의 추출 요약을 위한 2단계 준지도 프레임워크

**저자**: Meena Elumalai; Sivashankari Rajadurai
**출처**: IEEE Access, Vol.None, pp.1-1
**발행일**: 2026-01-01
**DOI**: https://doi.org/10.1109/access.2026.3695404

## 한국어 요약

**연구질문**: 장황하고 전문적인 비정형 임상 기록 데이터를 고가의 레이블링 작업 없이, 중요 의료 정보를 왜곡하지 않는 핵심 핵심 문장 단위로 자동 추출·요약할 수 있는 준지도 학습 프레임워크는 어떻게 작동하는가?

**방법론**:
- MTSamples 임상 텍스트 데이터셋 활용
- 1단계: TF-IDF와 SBERT 임베딩으로 문장을 수치화하고 센트로이드(centroid) 유사도 랭킹 및 MMR(Maximal Marginal Relevance) 필터링으로 다각도 문장 선별 수행
- 2단계: 퍼지 문장 정렬 기법을 적용해 핵심 레이블을 자동 생성하고, ClinicalBERT 임베딩에 Lexical 피처를 융합한 ClinicalBERT-BiLSTM 신경망을 구현하여 문장 중요도 학습

**주요 결과**:
- 제안된 2단계 준지도 모델은 의료 차트 전반에서 불필요한 시술 절차 정보를 배제하고 임상 진단에 본질적인 주요 문장들을 정교하게 선택해냄을 입증함
- 훈련 및 검증 셋 모두에서 균형 잡힌 정밀도(0.51, 0.49) 및 재현율 성과를 도출하여 임상 데이터의 자동 정형화 및 검색 시스템 구축의 기틀을 다짐


## 초록 (원문)

Purpose: Clinical narratives are frequently lengthy, repetitive, and difficult to understand, thereby diminishing their utility in downstream medical analytics and clinical decision support systems. Transforming unstructured statements into succinct and insightful summaries requires multiple stages of text analysis. However, manual analysis is labor-intensive, time-consuming, and susceptible to human error. Consequently, automated methods for summarizing clinical texts are urgently needed. This research aims to develop a robust extractive summarization framework for clinical documents that efficiently eliminates redundancy and identifies clinically significant sentences without necessitating expensive manual sentence-level annotations. Methods: The proposed approach, a two-stage hybrid extractive summarization framework, was evaluated using a curated subset of the MTSamples clinical dataset. Initially, a traditional unsupervised pipeline was employed, representing sentences using Term Frequency-Inverse Document Frequency (TF-IDF) and SBERT semantic embeddings, ranking them based on centroid similarity, and filtering them via Maximum Marginal Relevance (MMR) to balance relevance and diversity. Subsequently, this framework was transformed into a semi-supervised learning model utilizing fuzzy sentence alignment to enable automatic sentence-level labeling. ClinicalBERT contextual embeddings were combined with engineered structural, clinical, and lexical features to train a feature-augmented ClinicalBERT-BiLSTM architecture for predicting sentence salience. Fuzzy precision, recall, and F1-score at the sentence level, alongside paragraph-level data splits, were utilized to assess performance and prevent information leakage. Results: The proposed hybrid model demonstrated consistent and reliable performance across dataset splits. The model achieved an Overall Precision of 0.51, an Overall Recall of 0.32, and an Overall F1-score of 0.39 on the training set, and 0.49, 0.31, and 0.38 on the validation set. Qualitative analysis revealed that the model effectively selects diagnostically significant sentences while suppressing extraneous procedural information. Furthermore, feature augmentation and redundancy control enhanced sentence relevance recognition relative to purely lexical baselines. Conclusion: This study demonstrates that standard extractive summarization concepts can be efficiently applied to a feature-aware, semi-supervised deep learning framework for clinical material. The proposed approach achieves accurate, interpretable, and scalable extractive summarization of clinical narratives through the integration of centroid-based relevance modeling, redundancy management, and contextual neural representations. This framework is well-suited for real-world clinical applications and provides a solid foundation for future enhancements, including the incorporation of medical knowledge graphs and multi-document summarization.

## 키워드

Automatic summarization, Selection (genetic algorithm), Fuzzy logic, Sentence, Annotation, Narrative

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

