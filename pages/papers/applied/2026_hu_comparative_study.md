---
title: "A Comparative Study on Sentiment Classification Methods for Hotel Online Reviews Based on Machine Learning"
authors: ['Xin Hu', 'Zhaoyin Ding']
year: 2026
venue: ""
tags: ['Sentiment Analysis and Opinion Mining', 'Digital Marketing and Social Media', 'Recommender Systems and Techniques']
source: raw/applied/applied_2026_A_Comparative_Study_on_Se_3806262_3806275.md
---

# A Comparative Study on Sentiment Classification Methods for Hotel Online Reviews Based on Machine Learning
**제목(한글)**: 머신러닝 기반 호텔 온라인 리뷰의 감성 분류 방법에 관한 비교 연구

**저자**: Xin Hu; Zhaoyin Ding
**출처**: , Vol.None, pp.96-100
**발행일**: 2026-01-30
**DOI**: https://doi.org/10.1145/3806262.3806275

## 한국어 요약

**연구질문**: 디지털 관광 환경에서 폭증하는 호텔 온라인 리뷰를 효율적으로 자동 감성 분류하기 위해, 머신러닝 기반 4가지 분류 모델(로지스틱 회귀, SVM, 랜덤 포레스트, 인공신경망) 중 최적 모델은 무엇인가?

**방법론**:
- 웹 크롤러를 통해 특정 호텔 브랜드의 온라인 리뷰 데이터 수집
- 데이터 정제, 중국어 형태소 분석(word segmentation), Word2Vec 텍스트 벡터화를 포함한 전처리 수행
- 로지스틱 회귀, SVM, 랜덤 포레스트, 인공신경망(ANN) 4가지 분류 모델의 정확도, 정밀도, 재현율, F1-score, AUC 비교 평가

**주요 결과**:
- SVM 모델이 AUC 0.9416로 가장 우수한 종합 성능을 달성하여 호텔 서비스 감성 모니터링에 최적 모델로 확인됨
- 4개 모델 모두 감성 분류 과제를 성공적으로 수행하였으나, SVM이 다른 알고리즘 대비 전반적으로 우월한 성능을 보임

## 초록 (원문)

In the rapidly evolving digital tourism landscape, online reviews have become a critical determinant in consumer decision-making and a vital feedback loop for hotel service optimization. Nevertheless, the exponential growth of unstructured review data presents a significant challenge, as traditional manual processing methods are inefficient and lack objectivity. This paper addresses this issue by conducting a comparative study on automatic sentiment classification using machine learning algorithms. Taking online reviews from a specific hotel brand as the research object, this study systematically constructs a text analysis framework. The methodology involves acquiring data through web crawlers, followed by comprehensive preprocessing steps: data cleaning to eliminate noise, Chinese word segmentation, and text vectorization using the Word2Vec model to capture semantic features. Four mainstream classification models—Logistic Regression, Support Vector Machine (SVM), Random Forest, and Artificial Neural Network (ANN)—were built and evaluated. The study employs a rigorous set of performance metrics, including Accuracy, Precision, Recall, F1-score, and the Area Under the ROC Curve (AUC). Experimental results indicate that all four models can successfully perform sentiment classification tasks. However, the Support Vector Machine model distinguishes itself with the best comprehensive performance, achieving an AUC value of 0.9416, thereby outperforming the other algorithms. These findings suggest that SVM is the most suitable model for automated sentiment monitoring in this context, providing hotel managers with an effective tool for precise service improvement and offering a theoretical reference for related text mining research.

## 키워드

Word2vec, Sentiment analysis, Support vector machine, Preprocessor, Artificial neural network, Service (business), Big data, Data pre-processing

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

