---
title: "Performance Evaluation of Classical Machine Learning Models for Emotion Classification"
authors: ['Motaz Zghoul', 'Amneh Shaban']
year: 2025
venue: "International Journal of Artificial Intelligence Applications"
tags: ['Sentiment Analysis and Opinion Mining', 'Mental Health via Writing', 'Emotion and Mood Recognition']
source: raw/applied/applied_2025_Performance_Evaluation_of_ijaia_v1_i2_66.md
---

# Performance Evaluation of Classical Machine Learning Models for Emotion Classification

**제목(한글)**: 감정 분류를 위한 고전적 머신러닝 모델의 성능 평가

## 한국어 요약

**연구질문**: 11개 감정 범주의 다중 클래스 감정 분류에서 로지스틱 회귀, 랜덤포레스트, 나이브 베이즈 등 고전적 머신러닝 알고리즘의 성능은 어떻게 비교되며 어떤 모델이 가장 적합한가?

**방법론**:
- 약 106,000개 주석 문장으로 구성된 균형 데이터셋에서 TF-IDF 벡터화(트라이그램 지원, 3,000차원 특징 공간) 적용
- 로지스틱 회귀, 랜덤포레스트, 나이브 베이즈 세 가지 분류기를 5-폴드 교차검증으로 평가

**주요 결과**:
- 로지스틱 회귀가 정확도 79.90%, 정밀도 81.18%, F1-스코어 80.27%로 랜덤포레스트(75.32%) 및 나이브 베이즈(69.01%)를 능가
- 교차검증 표준편차가 0.5% 미만으로 안정적 일반화를 확인하며, 열정·사랑·중립 감정은 83% 이상 정확도로, 빈 감정·슬픔은 탐지가 어려움을 밝힘

**저자**: Motaz Zghoul; Amneh Shaban
**출처**: International Journal of Artificial Intelligence Applications, Vol.1
**발행일**: 2025-12-31
**DOI**: https://doi.org/10.71356/ijaia.v1.i2.66

## 초록 (원문)

Emotion detection in textual data represents a critical challenge in natural language processing with applications in mental health monitoring, customer sentiment analysis, and human-computer interaction. This study investigates three classical machine learning algorithms for multi-class emotion classification across eleven emotional categories using a balanced dataset of approximately 106,000 annotated sentences. The research employs Term Frequency-Inverse Document Frequency vectorization with trigram support and 3,000-dimensional feature space. Logistic Regression, Random Forest, and Naive Bayes classifiers were evaluated using comprehensive metrics including accuracy, precision, recall, F1-score, and five-fold cross-validation. Results demonstrate that Logistic Regression achieved superior performance with 79.90% accuracy, 81.18% precision, and 80.27% F1-score, substantially exceeding Random Forest at 75.32% and Naive Bayes at 69.01%. Cross-validation analysis revealed remarkable stability with standard deviations below 0.5%, confirming robust generalization. Per-class analysis identified enthusiasm, love, and neutral as most reliably detected emotions exceeding 83% accuracy, while empty and sadness presented greater challenges. The findings validate that classical machine learning approaches with proper feature engineering achieve competitive performance for fine-grained emotion detection while offering advantages in computational efficiency, interpretability, and deployment simplicity.

## 키워드

Random forest, Naive Bayes classifier, Trigram, AdaBoost, Feature (linguistics), Support vector machine, Perceptron, Stability (learning theory)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

