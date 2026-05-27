---
title: "Sentiment Analysis of User Reviews for AI Applications: Evaluating SVM, Logistic Regression, and Random Forest"
authors: ['Rivana Dwi Cahyani', 'Putri Taqwa Prasetyaningrum']
year: 2026
venue: "Journal of Information Systems and Informatics"
tags: ['Sentiment Analysis and Opinion Mining', 'Spam and Phishing Detection', 'Information Retrieval and Data Mining']
source: raw/applied/applied_2026_Sentiment_Analysis_of_Use_journalisi_v8i1_1366.md
---

# Sentiment Analysis of User Reviews for AI Applications: Evaluating SVM, Logistic Regression, and Random Forest
**제목(한글)**: AI 애플리케이션 사용자 리뷰의 감성 분석: SVM, 로지스틱 회귀, 랜덤 포레스트의 평가

**저자**: Rivana Dwi Cahyani; Putri Taqwa Prasetyaningrum
**출처**: Journal of Information Systems and Informatics, Vol.8, pp.1-27
**발행일**: 2026-02-10
**DOI**: https://doi.org/10.63158/journalisi.v8i1.1366

## 한국어 요약

**연구질문**: 최신 인공지능 모바일 앱의 인도네시아어 사용자 플레이스토어 리뷰에 대해 긍정/부정/중립 감성을 정확히 예측하는 최적의 머신러닝 분류 알고리즘은 무엇인가?

**방법론**:
- 3,500개의 인도네시아어 사용자 리뷰 데이터셋 활용
- TF-IDF 텍스트 벡터화와 감성 사전을 결합한 하이브리드 피처 추출 방법을 적용하고, Random Forest, SVM, Logistic Regression 세 가지 모델 비교 학습

**주요 결과**:
- 세 모델 모두 96% 이상의 양호한 정확도를 보였으며, 특히 랜덤 포레스트가 99.62%의 압도적이고 안정적인 최고 분류 정확도를 획득함을 확인
- SVM은 중립 감성의 모호성 부근에서 오탐이 빈번했던 한계를 밝혀 개발자 피드백 자동화에 활용 가치를 제시


## 초록 (원문)

The rapid growth of AI applications such as CICI, GROK, and Gemini has resulted in a large volume of user reviews on platforms like the Google Play Store, making sentiment analysis a critical tool for understanding user perceptions. This study compares the performance of three machine learning models: Random Forest, Support Vector Machine (SVM), and Logistic Regression in classifying sentiments in 3,500 Indonesian-language reviews. A hybrid feature extraction approach, combining sentiment lexicons with TF-IDF, was applied to improve sentiment classification accuracy. The models were evaluated based on accuracy, precision, recall, and F1-score. Results indicated that all models achieved an accuracy greater than 96%, with Random Forest providing the most consistent and accurate results, achieving an overall accuracy of 99.62%. While SVM excelled in classifying positive and negative sentiments, it faced challenges with neutral reviews due to the ambiguity and overlap in sentiment expression. Logistic Regression also showed strong performance, especially on structured reviews. The findings suggest that Random Forest is the most robust and reliable model for sentiment analysis, particularly in handling diverse AI application reviews. These results offer practical insights for developers seeking to improve application performance by leveraging sentiment analysis on user feedback.

## 키워드

Random forest, Sentiment analysis, Ambiguity, Support vector machine, Logistic regression, Feature (linguistics)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

