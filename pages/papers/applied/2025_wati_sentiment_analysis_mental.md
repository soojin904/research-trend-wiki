---
title: "SENTIMENT ANALYSIS OF MENTAL HEALTH REVIEWS USING MACHINE LEARNING ALGORITHMS"
authors: ['Risa Wati', 'Siti Ernawati']
year: 2025
venue: "Jurnal Riset Informatika"
tags: ['Mental Health via Writing', 'Sentiment Analysis and Opinion Mining', 'Edcuational Technology Systems']
source: raw/applied/applied_2025_SENTIMENT_ANALYSIS_OF_MEN_jri_v8i1_422.md
---

# SENTIMENT ANALYSIS OF MENTAL HEALTH REVIEWS USING MACHINE LEARNING ALGORITHMS

**제목(한글)**: 머신러닝 알고리즘을 활용한 정신건강 리뷰 감성 분석

## 한국어 요약

**연구질문**: 정신건강 관련 온라인 리뷰 데이터에서 우울증과 자살 관련 감성을 분류하는 데 있어 SVM, K-NN, 나이브 베이즈, 로지스틱 회귀, 의사결정트리, 랜덤포레스트 중 어떤 알고리즘이 가장 우수한 성능을 보이는가?

**방법론**:
- Kaggle에서 수집한 20,364개 정신건강 관련 리뷰 데이터셋 활용
- 우울증(depression)과 자살감시(suicidewatch) 두 범주로 분류 후 전처리 및 TF-IDF 가중치 적용
- 훈련:테스트 80:20 분할 후 6가지 분류 알고리즘 비교 평가

**주요 결과**:
- SVM 알고리즘이 RBF 커널과 C 파라미터=15 설정에서 정확도 72.09%, F1-스코어 72.09%로 다른 방법론을 능가
- 기계학습 기반 감성 분석이 공중 심리 상태 파악 및 정신건강 이해 지원에 유효함을 확인

**저자**: Risa Wati; Siti Ernawati
**출처**: Jurnal Riset Informatika, Vol.8, pp.149-157
**발행일**: 2025-12-15
**DOI**: https://doi.org/10.34288/jri.v8i1.422

## 초록 (원문)

Mental health is a significant issue in the modern era due to lifestyle changes, social pressures, and technological advancements that introduce new challenges. These problems affect various aspects of life, including education, employment, social relationships, and overall quality of life. Technological development enables the use of machine learning to automatically classify large amounts of data. This study aims to analyze and compare the performance of Support Vector Machines (SVM), K-Nearest Neighbor (K-NN), Naïve Bayes (NB), Logistic Regression (LR), Decision Tree (DT), and Random Forest (RF) in sentiment classification on mental health issues, while simultaneously contributing to scientific development and supporting the understanding of public psychological conditions. The dataset used in this research was obtained from Kaggle and consists of 20,364 mental health–related reviews in .CSV format, processed using Google Colab with the Python programming language. The data were categorized into two groups—depression and suicidewatch—and then underwent preprocessing, data splitting into training and testing sets with an 80:20 ratio, and TF-IDF weighting. The results indicate that the SVM algorithm outperforms the other methods. Using an RBF kernel and a C parameter of 15, SVM achieved an accuracy of 72.09%, a precision of 72.11%, a recall of 72.09%, and an F1-score of 72.09%. This study not only provides scientific contributions but also supports efforts to better understand the psychological conditions experienced by society.

## 키워드

Support vector machine, Naive Bayes classifier, Random forest, Decision tree, Mental health, Sentiment analysis, Statistical classification, Precision and recall

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

