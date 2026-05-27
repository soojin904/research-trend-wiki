---
title: "Sentiment Analysis of User Texts with Machine Learning Methods"
authors: ['E. A. Gorbunova', 'R. A. Kochkarov', 'E. A. Okuneva']
year: 2026
venue: "Digital Solutions and Artificial Intelligence Technologies"
tags: ['Sentiment Analysis and Opinion Mining', 'Mental Health via Writing', 'Computational and Text Analysis Methods']
source: raw/applied/applied_2026_Sentiment_Analysis_of_Use_3033_7097_2025_1_4_16_25.md
---

# Sentiment Analysis of User Texts with Machine Learning Methods
**제목(한글)**: 머신러닝 방법을 활용한 사용자 텍스트의 감성 분석

**저자**: E. A. Gorbunova; R. A. Kochkarov; E. A. Okuneva
**출처**: Digital Solutions and Artificial Intelligence Technologies, Vol.1, pp.16-25
**발행일**: 2026-01-23
**DOI**: https://doi.org/10.26794/3033-7097-2025-1-4-16-25

## 한국어 요약

**연구질문**: 러시아 대표 소셜 네트워크인 VKontakte(VK) API로 수집한 대규모 대중 포스트 및 댓글 텍스트에 대해 실시간 감성 분류를 자동화할 수 있는 최적의 머신러닝/딥러닝 파이프라인은 무엇인가?

**방법론**:
- VK API를 통해 수집된 포스트 및 댓글 텍스트 전처리(정제, 표제어 추출, 불용어 제거 및 TF-IDF 벡터화) 수행
- Logistic Regression, Random Forest, Naïve Bayes 클래식 머신러닝 분류기와 LSTM, RuBERT 트랜스포머 딥러닝 분류기를 비교 실험

**주요 결과**:
- Naïve Bayes 분류기가 재현율(recall) 및 다중 클래스 성능 밸런스 측면에서 가장 우수한 감성 탐지 효율을 보임
- 수집된 VK 텍스트의 대부분은 중립적이거나 긍정적인 반면 부정적 톤은 극소수임을 시각화 통계 분석으로 밝힘으로써 러시아어권 소셜 미디어 분석에서의 클래식 머신러닝의 견고함을 입증함


## 초록 (원문)

This paper explores the application of machine learning methods for sentiment analysis of user-generated texts in the Russian social network VKontakte. The sentiments of millions of users could be monitored and analyzed in real time, that facilitates prompt decision making and forecasting of social processes. Textual data, including posts and comments, were collected via the VK API. The preprocessing pipeline involved text cleaning, lemmatization, stop-word removal, and TFIDF vectorization. Several classification models were tested, including logistic regression, random forest, and naïve Bayes, as well as deep learning models such as LSTM and Transformers (RuBERT). The naïve Bayes classifier demonstrated the best performance in terms of recall and overall metric balance. Sentiment analysis results revealed that the majority of user texts were neutral or positive, with only a small portion being negative. The paper includes visualizations and statistical summaries of sentiment distribution. The study confirms the effectiveness of classical machine learning methods for processing and analyzing textual data in Russian social networks.

## 키워드

Sentiment analysis, Naive Bayes classifier, Preprocessor, Random forest, Precision and recall, Classifier (UML), Data pre-processing, Stop words

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

