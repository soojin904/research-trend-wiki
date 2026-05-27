---
title: "Comparative Study of Machine Learning Models for Textual Medical Note Classification"
authors: ['Yan Zhang', 'Huynh Trung Nguyen Le', 'Nathan Lopez', 'Kira Phan']
year: 2025
venue: "Computers"
tags: ['Machine Learning in Healthcare', 'Topic Modeling', 'Medical Coding and Health Information']
source: raw/applied/applied_2025_Comparative_Study_of_Mach_computers15010007.md
---

# Comparative Study of Machine Learning Models for Textual Medical Note Classification

**제목(한글)**: 텍스트 의료 노트 분류를 위한 머신러닝 모델 비교 연구

## 한국어 요약

**연구질문**: 신생물, 소화계·신경계·심혈관계 질환 등 4개 질병 범주의 의료 노트 다중 클래스 분류에서 전통적 머신러닝 알고리즘(랜덤포레스트, 로지스틱 회귀, 다항 나이브 베이즈, SVM)은 어떻게 비교되는가?

**방법론**:
- 9,633개 라벨링 의료 노트에 텍스트 정제·표제어 추출·불용어 제거·TF-IDF 벡터화 전처리 적용
- GridSearchCV와 5-폴드 교차검증으로 모델 최적화, 5개 독립적 층화 90-10 훈련-테스트 분할로 평가

**주요 결과**:
- 로지스틱 회귀가 평균 정확도 0.8469로 가장 우수하고, SVM과 다항 나이브 베이즈가 뒤를 이음
- 소화계와 신경계 질환 노트 간 어휘 중복으로 오분류 패턴이 발생하며, 이는 TF-IDF 표현의 심층 의미 구별 한계를 보여줌

**저자**: Yan Zhang; Huynh Trung Nguyen Le; Nathan Lopez; Kira Phan
**출처**: Computers, Vol.15, pp.7-7
**발행일**: 2025-12-23
**DOI**: https://doi.org/10.3390/computers15010007

## 초록 (원문)

The expansion of electronic health records (EHRs) has generated a large amount of unstructured textual data, such as clinical notes and medical reports, which contain diagnostic and prognostic information. Effective classification of these textual medical notes is critical for improving clinical decision support and healthcare data management. This study presents a statistically rigorous comparative analysis of four traditional machine learning algorithms—Random Forest, Logistic Regression, Multinomial Naive Bayes, and Support Vector Machine—for multiclass classification of medical notes into four disease categories: Neoplasms, Digestive System Diseases, Nervous System Diseases, and Cardiovascular Diseases. A dataset containing 9633 labeled medical notes was preprocessed through text cleaning, lemmatization, stop-word removal, and vectorization using term frequency-inverse document frequency (TF–IDF) representation. The models were trained and optimized through GridSearchCV with 5-fold cross-validation and evaluated across five independent stratified 90-10 train–test splits. Evaluation metrics, including accuracy, precision, recall, F1-score, and multiclass ROC-AUC, were used to assess model performance. Logistic Regression demonstrated the strongest overall performance, achieving an average accuracy of 0.8469 and high macro and weighted F1 scores, followed by Support Vector Machine and Multinomial Naive Bayes. Misclassification patterns revealed substantial lexical overlap between digestive and neurological disease notes, underscoring the limitations of TF–IDF representations in capturing deeper semantic distinctions. These findings confirm that traditional machine learning models remain robust, interpretable, and computationally efficient tools for textual medical note classification, and the study establishes a transparent and reproducible benchmark that provides a solid foundation for future methodological advancements in clinical natural language processing.

## 키워드

Support vector machine, Multinomial logistic regression, Multiclass classification, Benchmark (surveying), Clinical decision support system, Random forest, Unified Medical Language System, Logistic regression

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

