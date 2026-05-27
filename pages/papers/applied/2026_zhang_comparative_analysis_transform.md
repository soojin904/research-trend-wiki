---
title: "Comparative Analysis of Transformer-Based and Neural Network Models for Emotion Detection in Tweets"
authors: ['Bin Zhang', 'Xi Yang', 'Chen Zhang', 'Tangsen Huang']
year: 2026
venue: "Informatica"
tags: ['Emotion and Mood Recognition', 'Sentiment Analysis and Opinion Mining', 'Mental Health via Writing']
source: raw/applied/applied_2026_Comparative_Analysis_of_T_inf_v50i12_7551.md
---

# Comparative Analysis of Transformer-Based and Neural Network Models for Emotion Detection in Tweets
**제목(한글)**: 트윗 감정 탐지를 위한 트랜스포머 기반 모델 및 인공신경망 모델의 비교 분석

**저자**: Bin Zhang; Xi Yang; Chen Zhang; Tangsen Huang
**출처**: Informatica, Vol.50
**발행일**: 2026-05-13
**DOI**: https://doi.org/10.31449/inf.v50i12.7551

## 한국어 요약

**연구질문**: 트위터(Tweets)의 짧고 구어체적인 텍스트에서 감정을 판별할 때, 트랜스포머 모델과 전통적인 심층 신경망 모델들의 성능 차이 및 하드웨어적 계산 비용 수준은 어떠한가?

**방법론**:
- 트랜스포머 기반 2종(DistilBERT, ALBERT), 심층 신경망 2종(CNN, 3CNN-3LSTM), 그리고 GloVe 임베딩을 결합한 하이브리드 1종(3CNN-3LSTM-GloVe) 등 총 5개 신경망 구조 평가
- 트위터 텍스트 감정 분석 성능 지표(정확도, 정밀도, 재현율, F1) 측정 및 연산 소요 시간 분석

**주요 결과**:
- ALBERT가 86.38%로 가장 높은 정확도를 달성했으며, DistilBERT가 84.35%, 3CNN-3LSTM이 83.79%로 그 뒤를 이음
- 트랜스포머 기반 모델이 미묘하고 복잡한 감정 상태 판별 성능에서 일반 신경망 구조 대비 월등함을 검증
- 다만 트랜스포머 계열은 추론 연산 비용이 높아 실시간 마케팅이나 디지털 헬스케어 적용 시 최적화 과정이 반드시 요구됨을 지적


## 초록 (원문)

This study assesses the effectiveness of transformer-based and neural network models for detecting emotions in tweets. Five models are evaluated: two transformer-based frameworks (DistilBERT and ALBERT), two neural network architectures (CNN and 3CNN-3LSTM), and a hybrid model (3CNN- 3LSTM-GloVe 300x). The models are evaluated based on accuracy, precision, recall, and F1-score. The findings indicate that ALBERT attains the maximum accuracy at 86.38%, succeeded by DistilBERT with an accuracy of 84.35%. The 3CNN-3LSTM model exhibits an accuracy of 83.79%, whilst the CNN model demonstrates the lowest performance at 65.37%. The hybrid 3CNN-3LSTM-GloVe 300x model exhibits a performance of 75.61%. The results demonstrate that transformer-based models surpass neural network models in emotion recognition, especially in recognizing subtle emotional expressions. Nonetheless, transformer-based models demonstrate increased computational expenses, highlighting the necessity for optimization in real-time applications. This study enhances the domain of emotion detection by a comparative comparison of diverse models, emphasizing the benefits of transformers while acknowledging the computational difficulties. The results indicate significant implications for marketing, mental health, and digital communication, highlighting the need for further enhancement of transformer models for effective implementation.

## 키워드

Artificial neural network, Transformer, Emotion detection, Computational model, Network model, Deep neural networks, Domain (mathematical analysis)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

