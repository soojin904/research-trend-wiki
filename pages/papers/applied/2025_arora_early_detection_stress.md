---
title: "Early Detection of Stress and Anxiety Using NLP and Machine Learning on Social Media Data"
authors: ['Ravi Arora', 'Sathya Prasad', 'Arvind Rehalia', 'Nikhil Kaushik', 'Anil Kumar']
year: 2025
venue: "International Journal of Information Technology and Computer Science"
tags: ['Mental Health via Writing', 'Sentiment Analysis and Opinion Mining', 'Emotion and Mood Recognition']
source: raw/applied/applied_2025_Early_Detection_of_Stress_ijitcs_2025_06_04.md
---

# Early Detection of Stress and Anxiety Using NLP and Machine Learning on Social Media Data

**제목(한글)**: 소셜미디어 데이터에서 NLP와 머신러닝을 이용한 스트레스·불안 조기 탐지

## 한국어 요약

**연구질문**: 트위터 데이터와 설문 응답에서 NLP·머신러닝을 통해 스트레스·불안을 조기에 탐지할 수 있는가?

**방법론**:
- DASS-21 설문과 인도 트위터 사용자 트윗 수집
- Word2Vec 텍스트 벡터화, LDA·NMF 토픽 분석
- SVM, 랜덤 포레스트, LSTM 분류기 비교
- Streamlit 기반 대화형 애플리케이션 구현

**주요 결과**:
- 스트레스·불안과 연관된 언어 패턴 식별
- 머신러닝 모델이 소셜미디어 텍스트에서 정신건강 징후 탐지에 유효함을 확인

**저자**: Ravi Arora; Sathya Prasad; Arvind Rehalia; Nikhil Kaushik; Anil Kumar
**출처**: International Journal of Information Technology and Computer Science, Vol.17, pp.70-94
**발행일**: 2025-12-02
**DOI**: https://doi.org/10.5815/ijitcs.2025.06.04

## 초록 (원문)

Stress and anxiety are some of the most public mental health illnesses that people in the current society face. It is important to determine these conditions early to be able to effectively promote the well-being of individuals. This research work presents the possibility of identifying stress and anxiety through social media (SM) data and an anonymous survey, by machine learning (ML) and natural language processing (NLP). The paper starts with data collection, using the DASS-21 questionnaire and a sample of tweets obtained from Twitter users from India, aimed at determining which language is associated with stress and anxiety. The gathered data is pre-processed in some of the steps, such as URL removal, lower casing, punctuation removal, stop words removal, and lemmatization. After data preprocessing, the textual content is transformed into numerical form through Word2Vec to facilitate pattern analysis. To enrich the analysis of the main topics in the dataset, the Latent Dirichlet Allocation (LDA) and the Non-Negative Matrix Factorization (NMF) techniques are applied. For the classification, the work uses ML algorithms such as Support Vector Machine (SVM), Random Forest (RF), and Long Short-Term Memory (LSTM) networks. Lastly, the project involves an application created with Streamlit to allow the user to interact with the model.

## 키워드

Social media, Word2vec, Support vector machine, Punctuation, Sentiment analysis, Latent Dirichlet allocation, Stress (linguistics), Big data

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

