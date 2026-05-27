---
title: "Public Sentiment Toward the Indonesian Capital Relocation Policy on X Using a BiLSTM-CNN Model"
authors: ['Wanda Nugraha', 'Mochamad Tito Julianto', 'Mohamad Khoirun Najib', 'Elis Khatizah']
year: 2026
venue: "Jurnal Telematika"
tags: ['Sentiment Analysis and Opinion Mining', 'Data Mining and Machine Learning Applications', 'Multimedia Learning Systems']
source: raw/applied/applied_2026_Public_Sentiment_Toward_t_telematika_v20i2_796.md
---

# Public Sentiment Toward the Indonesian Capital Relocation Policy on X Using a BiLSTM-CNN Model
**제목(한글)**: BiLSTM-CNN 모델을 활용한 X(구 트위터) 상의 인도네시아 수도 이전 정책에 대한 대중 감성 분석

**저자**: Wanda Nugraha; Mochamad Tito Julianto; Mohamad Khoirun Najib; Elis Khatizah
**출처**: Jurnal Telematika, Vol.20, pp.114-126
**발행일**: 2026-01-03
**DOI**: https://doi.org/10.61769/telematika.v20i2.796

## 한국어 요약

**연구질문**: 인도네시아의 신수도(IKN) 이전 정책에 대한 X(구 트위터) 플랫폼 대중의 여론 지형은 어떠하며, 감성을 정밀하게 분류해 낼 딥러닝 아키텍처 모델은 어떻게 구현하는가?

**방법론**:
- X 플랫폼에서 IKN 수도 이전 관련 대규모 소셜 데이터 수집
- 문맥 처리를 위한 양방향 LSTM(BiLSTM)과 지역 특징 추출을 위한 CNN을 결합한 하이브리드 분류 신경망 구축
- 하이퍼파라미터 튜닝 및 10배 교차 검증(10-fold Cross-validation) 수행

**주요 결과**:
- 대중 여론은 긍정 46%, 부정 30%, 중립 24%로 수도 이전에 대해 긍정적인 기대감이 다소 우세함을 확인함
- 제안된 BiLSTM-CNN 모델은 테스트 정확도 78%, 교차 검증 평균 정확도 81% (표준편차 0.006)의 안정적이고 신뢰성 높은 판별 성능을 달성함


## 초록 (원문)

The development of Indonesia's new capital city, Ibu Kota Nusantara (IKN), is an innovative government policy that has sparked diverse public responses. This study aims to explore sentiment trends on the social media platform X to understand public perceptions of the policy. Additionally, a sentiment classification model combining Bidirectional Long Short-Term Memory (BiLSTM) and Convolutional Neural Network (CNN) was developed and optimized through hyperparameter tuning. Exploratory analysis showed that positive sentiment dominated at 46%, followed by negative at 30% and neutral at 24%. The classification model achieved a test accuracy of 78% and an average accuracy of 81% across 10-fold cross-validation, with a standard deviation of 0.006. The achieved accuracy, together with the low cross-validation standard deviation, indicates that the BiLSTM-CNN model demonstrates stable and reliable performance.

## 키워드

Government (linguistics), Indonesian, Convolutional neural network, Social capital, Public policy, Sentiment analysis, Test (biology), Indonesian government

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

