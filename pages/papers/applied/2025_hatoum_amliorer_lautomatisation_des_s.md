---
title: "Améliorer l'automatisation des soins de santé grâce à une meilleure qualité des données et à des approches basées sur la pertinence sémantique"
authors: ['Monah Bou Hatoum']
year: 2025
venue: "HAL (Le Centre pour la Communication Scientifique Directe)"
tags: ['Machine Learning in Healthcare', 'Biomedical Text Mining and Ontologies', 'Topic Modeling']
source: raw/applied/applied_2025_Amliorer_lautomatisation__nodoi.md
---

# Améliorer l'automatisation des soins de santé grâce à une meilleure qualité des données et à des approches basées sur la pertinence sémantique

**제목(한글)**: 데이터 품질 향상과 의미론적 관련성 기반 접근법을 통한 의료 자동화 개선

## 한국어 요약

**연구질문**: 임상 텍스트 전처리와 ICD-10 코드 예측 표현 방식을 개선함으로써 의료 자동 코딩 시스템의 정확도와 임상적 유용성을 어떻게 높일 수 있는가?

**방법론**:
- EMTE(Enhanced Medical Terms Extractor): 패턴 매칭 기반 의료 개념 추출 및 부정어 보존
- UTP(Unified Term Presentation): 임상 용어 표준화, 약어 확장, 검사값 정규화
- NNBSVR(Neural Network-Based Semantic Vector Representations): ICD-10 코드 간 계층적 관계·의미 유사도 포착 벡터화
- 957만 건 이상의 임상 기록과 9,278개 ICD-10 코드를 포함한 실제 데이터셋 평가

**주요 결과**:
- 기존 방법 대비 F1-score 최대 18.6% 향상, 전문가 검증 정확도 92.58%
- 어휘 규모 43.92% 감소로 효율성 개선
- 의미적으로 유관한 예측에 부분 점수를 부여하는 맞춤형 손실 함수 설계

**저자**: Monah Bou Hatoum
**출처**: HAL (Le Centre pour la Communication Scientifique Directe), Vol.None
**발행일**: 2025-12-12
**DOI**: 

## 초록 (원문)

The increasing digitization of healthcare data presents unprecedented opportunities for applying machine learning to improve clinical outcomes, but significant challenges remain in processing unstructured medical text and evaluating prediction accuracy. This thesis addresses these fundamental challenges through an integrated framework that enhances both the quality of input data and the evaluation of output predictions.We first tackle the problem of clinical text preprocessing with two novel approaches: EMTE (Enhanced Medical Terms Extractor), which uses pattern-matching rules to accurately extract medical concepts and preserve critical negations; and UTP (Unified Term Presentation), which standardizes clinical terminology, expands abbreviations, and normalizes investigation values. Together, these contributions significantly improve text quality while preserving essential clinical information that standard preprocessing methods often discard.We then revolutionize how ICD-10 code predictions are represented and evaluated through NNBSVR (Neural Network-Based Semantic Vector Representations), a novel vectorization technique that captures hierarchical relationships, semantic similarities, and usage constraints between medical codes. Building upon this foundation, we develop custom loss functions that incorporate clinical relevance during model training, allowing partial credit for predictions that are semantically related to the ground truth.Extensive evaluations on real-world clinical datasets (involving over 9.57 million clinical records and 9,278 unique ICD-10 codes) demonstrate the superiority of our approaches, with performance improvements of up to 18.6% in F1-score compared to traditional methods, achieving 92.58% expert validation accuracy and 43.92% vocabulary reduction. Beyond metric improvements, our framework enhances clinical utility by producing predictions that align more closely with medical practice, where related diagnoses often have similar implications for patient care.This research represents a significant advancement toward more accurate, reliable, and clinically meaningful automated coding systems, with potential impacts on healthcare documentation, administrative efficiency, clinical decision support, and ultimately patient outcomes.

## 키워드

Preprocessor, Unified Medical Language System, Medical diagnosis, Metric (unit), Quality (philosophy), Digitization, Vocabulary, Relevance (law)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

