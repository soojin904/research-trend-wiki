---
title: "A Comparative Analysis of Decision Tree, Logistic Regression, and Support Vector Machine Algorithms in Sentiment Analysis of Threads App Reviews"
authors: ['Rahmat Hidayat', 'Farhan Aminulhaq']
year: 2025
venue: "Intechno Journal."
tags: ['Sentiment Analysis and Opinion Mining', 'Internet of Things and AI', 'Scientific and Engineering Research Topics']
source: raw/applied/applied_2025_A_Comparative_Analysis_of_intechnojournal_2025v7i2_.md
---

# A Comparative Analysis of Decision Tree, Logistic Regression, and Support Vector Machine Algorithms in Sentiment Analysis of Threads App Reviews

**제목(한글)**: Threads 앱 리뷰 감성 분석에서 의사결정 트리, 로지스틱 회귀, 서포트 벡터 머신 알고리즘의 비교 분석

## 한국어 요약

**연구질문**: Threads 애플리케이션에 대한 사용자 감성을 분류할 때 의사결정 트리, 로지스틱 회귀, SVM 중 어떤 기계학습 모델이 가장 높은 정확도를 보이는가?

**방법론**:
- 구글 플레이 스토어에서 수집한 사용자 리뷰 3,000건 데이터셋 활용
- 소음 제거, 토큰화, 불용어 제거, 어간 추출 등 텍스트 마이닝 전처리 수행
- TF-IDF(단어 빈도-역문서 빈도) 특성 추출 및 K-겹 교차 검증(K-Fold Cross Validation) 평가

**주요 결과**:
- SVM이 평균 정확도 88.18%, 최대 92.69%로 가장 우수한 성능을 달성함
- 로지스틱 회귀와 의사결정 트리는 고차원 텍스트 데이터 처리에서 낮은 정확도와 불안정성을 보임
- TF-IDF 가중치와 SVM을 결합하면 소셜 미디어 리뷰의 단문 감성 탐지 정확도가 크게 향상됨

**저자**: Rahmat Hidayat; Farhan Aminulhaq
**출처**: Intechno Journal., Vol.7, pp.45-55
**발행일**: 2025-12-31
**DOI**: https://doi.org/10.24076/intechnojournal.2025v7i2.2497

## 초록 (원문)

Purpose: This study aims to analyze user sentiment regarding the Threads application by comparing the performance of different machine learning models. As a relatively new social media platform, understanding user feedback is crucial for identifying service gaps and improving user retention. The research seeks to determine which algorithm provides the highest precision in classifying user reviews into positive and negative sentiments. Methods: The research utilized a dataset of 3,000 user reviews scraped fromthe Google Play Store. The methodology followed a systematic text mining workflow, including preprocessing stages such as noise removal, tokenization, stopword removal, and stemming. Feature extraction was performed using the Term Frequency-Inverse Document Frequency (TF IDF) method. Three machine learning algorithms—Support Vector Machine (SVM), Decision Tree, and Logistic Regression—were implemented and evaluated using K-Fold Cross Validation to ensure statistical reliability. Result: The experimental results indicate that the Support Vector Machine (SVM) consistently outperformed the other two models. SVM achieved a superior average accuracy of 88.18%, with a peak performance reaching 92.69% during K-Fold testing. Logistic Regression and Decision Tree showed lower accuracy and less stability in handling the high-dimensional text data. These figures confirm that SVM is the most effective model for analyzing the linguistic nuances found in Threads app reviews. Novelty/Originality/Value: This research contributes to the field of software evaluation by providing an empirical comparison of classification algorithms specifically for newly launched social media platforms like Threads. The findings offer practical value for developers to automate the monitoring of user satisfaction. The study demonstrates that integrating rigorous TF-IDF weighting with SVM significantly enhances the accuracy of sentiment detection in short-form mobile application reviews.

## 키워드

Support vector machine, Decision tree, Preprocessor, Weighting, Social media, Sentiment analysis, Field (mathematics), tf–idf

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

