---
title: "Detection of Confirmation Bias in Horoscope Texts Using Support Vector Machine"
authors: ['Arun Padmanabhan', 'Dr. K. Devasenapathy']
year: 2025
venue: "International Research Journal on Advanced Science Hub"
tags: ['Topic Modeling', 'Mental Health via Writing', 'Sentiment Analysis and Opinion Mining']
source: raw/applied/applied_2025_Detection_of_Confirmation_irjash_2025_127.md
---

# Detection of Confirmation Bias in Horoscope Texts Using Support Vector Machine

**제목(한글)**: 지지 벡터 머신(SVM)을 활용한 별자리 운세 텍스트의 확증 편향 탐지

## 한국어 요약

**연구질문**: 기계학습 기법으로 별자리 운세 텍스트에서 확증 편향(confirmation bias)을 자동으로 탐지할 수 있는가?

**방법론**:
- TF-IDF 고차원 벡터화(n-gram 구조 포함)로 특징 추출
- SMOTE 오버샘플링 및 클래스 가중치 적용 SVM 분류
- 나이브 베이즈(Naive Bayes) 및 로지스틱 회귀(Logistic Regression) 기준 모델과 비교
- 특징 중요도 시각화를 통한 해석 가능성 분석

**주요 결과**:
- SVM이 불균형 분류 태스크에서 경쟁력 있는 성능 달성, 소수 편향 탐지에서 우수
- 정밀도·재현율·F1·ROC-AUC 등 다중 지표 평가로 모델 신뢰성 확인
- 편향 예측에 영향을 미치는 주요 텍스트 요소 식별

**저자**: Arun Padmanabhan; Dr. K. Devasenapathy
**출처**: International Research Journal on Advanced Science Hub, Vol.7, pp.1150-1155
**발행일**: 2025-12-26
**DOI**: https://doi.org/10.47392/irjash.2025.127

## 초록 (원문)

The study addresses the challenging task of identification of confirmation bias in horoscope texts, using machine learning techniques. Bias confirmation, a cognitive bias in which the information that confirms one's prior beliefs is preferred, is a widely used personalized media such as horoscopes and has implications for both mental health and digital content analysis. For this research, a carefully selected set of horoscope responses was compiled and annotated for the occurrence of confirmation bias or its absence. Data pre-processing included methodical text cleaning—removal of unnecessary columns, normalization, whitespace trimming, and imbalanced class analysis—to make it possible to build strong predictive models. Feature extraction involved a high-dimensional TF-IDF (Term Frequency-Inverse Document Frequency) vectorization that was able to capture relevant linguistic patterns as well as n-gram structures that are highly indicative of biased content. To address the issue of class imbalance, oversampling methods like SMOTE were used together with class weighting in the Support Vector Machine (SVM) learning framework. The SVM model was adjusted for the best kernel parameters and probabilistic output calibration, while stratified train-test data splitting was used to ensure representative evaluation across bias classes. Baseline model Naïve Bayes and Logistic Regression were also set up for comparative analysis, but SVM’s margin-based classification was able to deliver competitive performance, especially for minority bias detection. Deep emphasis was placed on the model evaluation to ensure the metrics used were appropriate for an imbalanced classification such as: accuracy, precision, recall, F1-score, and ROC-AUC, with a detailed examination through confusion matrices and threshold tuning curves. Besides, the interpretability layer was also present in the study by means of feature importance visualization, thus giving a clear indication of the textual elements that influenced bias predictions the most.

## 키워드

Support vector machine, Interpretability, Naive Bayes classifier, Classifier (UML), Probabilistic logic, Identification (biology), Feature selection, Weighting

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

