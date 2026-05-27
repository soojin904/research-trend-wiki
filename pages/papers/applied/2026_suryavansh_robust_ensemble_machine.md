---
title: "A Robust Ensemble Machine Learning Framework For Accurate Sentiment Classification Of Twitter Data"
authors: ['Ritu Suryavanshi', 'Sharad Morolia']
year: 2026
venue: "Open MIND"
tags: ['Sentiment Analysis and Opinion Mining', 'Spam and Phishing Detection', 'Text and Document Classification Technologies']
source: raw/applied/applied_2026_A_Robust_Ensemble_Machine_zenodo_19630704.md
---

# A Robust Ensemble Machine Learning Framework For Accurate Sentiment Classification Of Twitter Data
**제목(한글)**: 트위터 데이터의 정확한 감성 분류를 위한 강건한 앙상블 머신러닝 프레임워크

**저자**: Ritu Suryavanshi; Sharad Morolia
**출처**: Open MIND, Vol.None
**발행일**: 2026-01-01
**DOI**: https://doi.org/10.5281/zenodo.19630704

## 한국어 요약

**연구질문**: 이모티콘, 속어, 반어법 등이 남발되는 소셜 미디어 트위터(Twitter)의 단문 데이터로부터 대중들의 감성을 안정적으로 판별하기 위해, 다수의 머신러닝 분류기를 어떻게 결합하여 최적화할 수 있는가?

**방법론**:
- 트위터 사용자 게시글(Tweets)을 수집하고 텍스트 정제 전처리 수행
- Bag-of-Words(BoW)와 TF-IDF를 병행 적용하여 단어 빈도 및 중요도 텍스트 피처 추출
- 나이브 베이즈, 서포트 벡터 머신, 의사결정나무 등 여러 기본 분류기(Weak Classifiers)들을 학습하고 이들의 출력을 결합하는 앙상블 학습(Ensemble Learning) 모델 설계 및 평가

**주요 결과**:
- 개별 단독 모델 대비 앙상블 프레임워크가 이상치나 반어법 포함 문항에서도 예측 오차를 보완하여 성능 강건성을 향상시킴을 확인
- 소셜 여론 추이 모니터링, 신제품 만족도 진단 및 정치 감성 측정 시 노이즈에 대처할 수 있는 실무 분류 모델을 제안함


## 초록 (원문)

Social media platforms generate a massive amount of opinion-based data that reflects public attitudes toward various topics such as politics, products, and social events. Among these platforms, Twitter is widely used for expressing opinions in the form of short textual messages known as tweets. Analyzing these tweets can provide valuable insights into public sentiment. However, sentiment classification of Twitter data is challenging due to informal language, abbreviations, emojis, and sarcasm. This study proposes an ensemble learning framework to improve the accuracy of Twitter sentiment classification. The framework involves several stages, including data collection, preprocessing, feature extraction using techniques such as Bag-of-Words and TF-IDF, and training multiple machine learning classifiers. Ensemble methods combine the predictions of these classifiers to generate more reliable results. The performance of the proposed model is evaluated using metrics such as accuracy, precision, recall, and F1-score. The proposed approach aims to enhance sentiment analysis performance and provide more accurate insights from social media data.

## 키워드

Sentiment analysis, Social media, Ensemble learning, Feature (linguistics), Feature extraction, Ensemble forecasting, Training set, Labeled data

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

