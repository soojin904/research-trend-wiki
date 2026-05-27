---
title: "Analisis Tingkat Sentimen Opini Publik Terhadap Kebijakan TV Digital di Platform X Menggunakan Multinomial Naïve Bayes"
authors: ['Asep Arwan Sulaeman', 'Candra Naya', 'Muhtajuddin Danny', 'Makmun Effendi']
year: 2026
venue: "Bulletin of Computer Science Research"
tags: ['Sentiment Analysis and Opinion Mining', 'Multimedia Learning Systems', 'Data Mining and Machine Learning Applications']
source: raw/applied/applied_2026_Analisis_Tingkat_Sentimen_bulletincsr_v6i2_951.md
---

# Analisis Tingkat Sentimen Opini Publik Terhadap Kebijakan TV Digital di Platform X Menggunakan Multinomial Naïve Bayes
**제목(한글)**: 다항 나이브 베이즈를 활용한 X 플랫폼 상의 디지털 TV 정책에 대한 대중 감성 분석

**저자**: Asep Arwan Sulaeman; Candra Naya; Muhtajuddin Danny; Makmun Effendi
**출처**: Bulletin of Computer Science Research, Vol.6, pp.753-762
**발행일**: 2026-02-25
**DOI**: https://doi.org/10.47065/bulletincsr.v6i2.951

## 한국어 요약

**연구질문**: 인도네시아의 아날로그-디지털 텔레비전 방송 전환 정책에 관한 대중들의 여론 방향(긍정/부정)과 불만을 X(구 트위터) 텍스트 마이닝을 통해 어떻게 통계적으로 판별할 수 있는가?

**방법론**:
- X 플랫폼에서 키워드 "tv digital"을 활용해 크롤링한 뒤 최종 789건의 정제된 트윗 데이터셋 구성
- TF-IDF 단어 벡터 특징 추출을 거쳐 지도 기계학습 모델인 다항 나이브 베이즈(Multinomial Naive Bayes) 알고리즘 학습
- Model performance evaluation shows an accuracy of 79.21%, precision of 82.45%, and recall of 85.06%, indicating that the model performs well and consistently in classifying sentiment.

**주요 결과**:
- 긍정적인 여론이 60.58%(478건)로 부정적 여론인 39.42%(311건)에 비해 우세한 경향을 보임을 도출
- 나이브 베이즈 모델이 79.21%의 무난한 정확도와 85.06%의 재현율을 기록하여 소셜 미디어를 기반으로 국가 정책의 만족도 변화를 상시 추적할 수 있음을 검증함


## 초록 (원문)

The migration from analog to digital television broadcasting is part of the transformation of the broadcasting system aimed at improving broadcast quality and spectrum efficiency. However, the implementation of the digital television policy has generated diverse public responses, ranging from support to criticism. This study aims to analyze public opinion on the digital television policy in Indonesia using social media data from platform X. A quantitative approach was employed using text mining and supervised machine learning techniques. Data were collected through a crawling process using the keyword “tv digital”, resulting in 1,855 tweets. After data selection and cleaning, 789 tweets were obtained as the final dataset. The analysis stages included text preprocessing, feature extraction using Term Frequency–Inverse Document Frequency (TF–IDF), and sentiment classification using the Multinomial Naïve Bayes algorithm. The results indicate that positive sentiment dominates public opinion, with 478 tweets (60.58%), while negative sentiment accounts for 311 tweets (39.42%). Model performance evaluation shows an accuracy of 79.21%, precision of 82.45%, and recall of 85.06%, indicating that the model performs well and consistently in classifying sentiment. These findings demonstrate that social media–based sentiment analysis can serve as an empirical approach to understanding public perceptions of digital television policy.

## 키워드

Broadcasting (networking), Social media, Precision and recall, Digital television, Naive Bayes classifier, Process (computing), Sentiment analysis, Feature selection

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

