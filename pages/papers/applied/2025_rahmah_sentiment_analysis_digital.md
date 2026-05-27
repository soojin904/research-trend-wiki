---
title: "Sentiment Analysis of Digital Ethics in YouTube Islamic Preaching Videos Using Support Vector Machine"
authors: ['Arizka Sabilah Rahmah', 'Awang Andhyka', 'Rizky Aditya Nugroho']
year: 2025
venue: "Applied Technology and Computing Science Journal"
tags: ['Sentiment Analysis and Opinion Mining', 'Media, Religion, Digital Communication', 'Hate Speech and Cyberbullying Detection']
source: raw/applied/applied_2025_Sentiment_Analysis_of_Dig_atcsj_v8i2_8422.md
---

# Sentiment Analysis of Digital Ethics in YouTube Islamic Preaching Videos Using Support Vector Machine

**제목(한글)**: SVM을 활용한 유튜브 이슬람 설교 영상 댓글의 디지털 윤리 감성 분석

## 한국어 요약

**연구질문**: SVM과 TF-IDF 특징 표현을 활용하면 이슬람 설교 영상 댓글에서 디지털 윤리에 관한 감성 패턴을 효과적으로 식별할 수 있는가?

**방법론**:
- YouTube 댓글 수집 후 텍스트 정제, 대소문자 정규화, 토큰화, 불용어 제거, 어간 추출(stemming) 전처리
- TF-IDF 특징 표현 + SVM 분류 모델
- 긍정·부정·중립 세 가지 감성 범주로 수동 레이블링

**주요 결과**:
- SVM 모델 정확도 77.27%, 중립 범주에서 가장 높은 성능
- 데이터 불균형과 종교 담화의 언어 변이가 긍정·부정 범주 오분류 주요 원인
- 디지털 이슬람 설교 연구에서 디지털 윤리 연구의 초기 통찰 제공

**저자**: Arizka Sabilah Rahmah; Awang Andhyka; Rizky Aditya Nugroho
**출처**: Applied Technology and Computing Science Journal, Vol.8, pp.119-132
**발행일**: 2025-12-31
**DOI**: https://doi.org/10.33086/atcsj.v8i2.8422

## 초록 (원문)

The rapid expansion of Islamic preaching in the digital sphere, particularly through YouTube, calls for a deeper understanding of communication ethics as reflected in user responses. This study analyzes the sentiments expressed in comments on Islamic preaching videos to identify patterns of digital ethics within online communities. The research employs a Support Vector Machine (SVM) classification model with TF-IDF feature representation. Data were collected from YouTube comments and processed through several preprocessing stages, including text cleaning, case normalization, tokenization, stopword removal, and stemming, before being manually labeled into three sentiment categories: positive, negative, and neutral. Testing on 22 data samples shows that the SVM model achieved an accuracy of 77.27%, with the highest performance observed in the neutral category. Misclassification in the positive and negative categories was mainly influenced by data imbalance and linguistic variations commonly found in religious discourse. These findings indicate that SVM combined with TF-IDF is reasonably effective for sentiment analysis in the context of digital Islamic preaching; however, improvements in data balance and the incorporation of contextual features are necessary to enhance classification performance. Overall, this study provides an initial insight into audience response patterns toward digital Islamic preaching and contributes to the development of digital ethics research in Islamic communication studies.

## 키워드

Islam, Support vector machine, Preprocessor, Context (archaeology), Sentiment analysis, Data pre-processing, Balance (ability)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

