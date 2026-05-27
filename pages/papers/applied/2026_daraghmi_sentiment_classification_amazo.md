---
title: "Sentiment Classification of Amazon Product Reviews Based on Machine and Deep Learning Techniques: A Comparative Study"
authors: ['Eman Daraghmi', 'Noora Zyadeh']
year: 2026
venue: "Future Internet"
tags: ['Sentiment Analysis and Opinion Mining', 'Digital Marketing and Social Media', 'Text and Document Classification Technologies']
source: raw/applied/applied_2026_Sentiment_Classification__fi18030138.md
---

# Sentiment Classification of Amazon Product Reviews Based on Machine and Deep Learning Techniques: A Comparative Study
**제목(한글)**: 머신러닝 및 딥러닝 기술 기반 아마존 제품 리뷰 감성 분류: 비교 연구

**저자**: Eman Daraghmi; Noora Zyadeh
**출처**: Future Internet, Vol.18, pp.138-138
**발행일**: 2026-03-07
**DOI**: https://doi.org/10.3390/fi18030138

## 한국어 요약

**연구질문**: 레이블 불균형 문제가 심한 아마존 고객 리뷰 데이터(Fine Food 및 Unlocked Mobile)에서 감성 분석 정확도를 극대화할 수 있는 머신러닝, 딥러닝, 트랜스포머 모델의 최적 성능 조합은 무엇인가?

**방법론**:
- 데이터 불균형 해소를 위한 오버샘플링(Oversampling) 및 언더샘플링(Undersampling) 기법 적용
- 머신러닝(Random Forest, Logistic Regression, SVM, Naïve Bayes, GBM)과 딥러닝(CNN, LSTM), 트랜스포머 기반 RoBERTa 모델 간 비교 실험 진행

**주요 결과**:
- 오버샘플링 데이터 밸런싱 작업이 감성 분류의 전체적인 성능을 유의미하게 끌어올림을 검증함
- 전통 기계학습 계열 중에서는 Random Forest가 앙상블 학습의 견고함을 통해 고차원 데이터에서 우수한 성과를 보였고, 딥러닝 영역에서는 문맥 파악력이 높은 RoBERTa 모델이 압도적으로 우수한 감성 분류 성과를 달성함


## 초록 (원문)

Sentiment classification plays a crucial role in analyzing customer feedback to identify market trends, enhance product recommendations, and improve customer satisfaction. This study focuses on sentiment analysis of Amazon reviews using two major datasets—Fine Food Reviews and Unlocked Mobile Reviews—which exhibit label imbalance. To address this challenge, both oversampling and undersampling techniques were applied to balance the datasets. Various machine learning (ML) algorithms, including Random Forest (RF), Logistic Regression (LR), Support Vector Machine (SVM), Naïve Bayes (NB), and Gradient Boosting Machine (GBM), as well as deep learning (DL) models such as Convolutional Neural Network (CNN), Long Short-Term Memory (LSTM), and transformer-based models like RoBERTa, were implemented. After data cleaning and preprocessing, models were trained, and performance was evaluated. The results indicate that oversampling significantly enhances classification accuracy, particularly for the Fine Food dataset. Among ML models, Random Forest achieved the highest accuracy due to its ensemble approach and robustness in handling high-dimensional data. DL models, particularly RoBERTa, also demonstrated superior performance owing to their capacity to capture contextual dependencies. The findings emphasize the importance of data balancing for optimal sentiment analysis and contribute valuable insights toward advancing automated opinion classification in e-commerce applications.

## 키워드

Random forest, Oversampling, Naive Bayes classifier, Support vector machine, Undersampling, Sentiment analysis, Deep learning, Boosting (machine learning)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

