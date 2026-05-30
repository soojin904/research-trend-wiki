---
title: "Predicting Stock Market Trends Through a Hybrid Machine Learning Framework That Combines Technical Indicators with News Sentiment Analysis"
authors: ['Jianjiang Li']
year: 2025
venue: "Applied and Computational Engineering"
tags: ['Stock Market Forecasting Methods', 'Sentiment Analysis and Opinion Mining', 'Financial Markets and Investment Strategies']
source: raw/applied/applied_2025_Predicting_Stock_Market_T_2026_tj30739.md
---

# Predicting Stock Market Trends Through a Hybrid Machine Learning Framework That Combines Technical Indicators with News Sentiment Analysis

**제목(한글)**: 기술적 지표와 뉴스 감성 분석을 결합한 하이브리드 머신러닝 프레임워크를 통한 주식 시장 동향 예측

## 한국어 요약

**연구질문**: 기술적 지표와 뉴스 감성 분석을 통합한 하이브리드 머신러닝 프레임워크를 통해 주식 시장 동향을 정확하게 예측할 수 있는가?

**방법론**:
- LSTM(Long Short-Term Memory)과 BERT(Bidirectional Encoder Representations from Transformers) 기반의 하이브리드 모델 제안.
- 사전 학습된 FinBERT 모델을 활용하여 공식 실적 보고서, 주류 금융 뉴스, 소셜 미디어 금융 토론 등 다중 소스 금융 데이터에서 미세 감성 특징(fine-grained sentiment features) 추출.
- 추출된 감성 특징과 이동 평균(moving averages), 상대 강도 지수(relative strength index), 거래량(trading volume) 등 과거 주가 데이터에서 파생된 주요 기술적 지표를 표준화하고 연결하여 종합 특징 벡터(comprehensive feature vector) 생성.
- 종합 특징 벡터를 2계층 LSTM 네트워크에 입력하여 시간적 종속성(temporal dependencies) 및 동적 시퀀스 예측(dynamic sequence prediction) 수행.
- S&P 500 상위 50개 주식의 5년간 데이터를 포함하는 데이터셋을 사용하여 모델 검증.

**주요 결과**:
- 제안된 하이브리드 모델은 단일 모델(LSTM, BERT, 전통적 ARIMA)보다 단기(1일 예측) 및 중기(5일 예측) 예측 정확도에서 일관되게 우수한 성능을 보였다.
- 강세장(bullish), 약세장(bearish), 변동성 시장(volatile environments) 등 다양한 시장 조건에서 일반화(generalize) 능력을 입증했다.
- 다중 소스 데이터 융합(multi-source data fusion)이 금융 예측에서 중요한 가치를 가지며, 단일 데이터 유형의 한계를 효과적으로 보완하고 모델의 시장 노이즈(market noise)에 대한 견고성(robustness)을 향상시킴을 확인했다.

**???*: Jianjiang Li
**출처**: Applied and Computational Engineering, Vol.211, pp.209-216
**발행??*: 2025-12-18
**DOI**: https://doi.org/10.54254/2755-2721/2026.tj30739

## 초록 (?문)

This paper proposes a hybrid model based on LSTM(Long Short-Term Memory)and BERT(Bidirectional Encoder Representations from Transformers)for stock market trend prediction, which innovatively integrates the quantitative analysis of technical indicators and qualitative analysis of news sentiment. The framework first utilizes a pre-trained FinBERT model--optimized for financial text processing--to extract fine-grained sentiment features from multi-source financial data, including official earnings reports, mainstream financial news, and social media financial discussions. These sentiment features, together with key technical indicators derived from historical stock price data(such as moving averages, relative strength index, and trading volume), are standardized and concatenated into a comprehensive feature vector, which is then fed into a two-layer LSTM network for capturing temporal dependencies and dynamic sequence prediction. The experimental results, derived from a dataset encompassing 50 top stocks from the S&amp;P 500 over a span of 5 years, show that the proposed hybrid model consistently surpasses single-model methods--such as standalone LSTM, BERT, and traditional ARIMA--in terms of both short-term(1-day ahead)and medium-term(5-day ahead)prediction accuracy, as well as its ability to generalize across various market conditions, including bullish, bearish, and volatile environments. This confirms the significant value of multi-source data fusion in financial forecasting, as it effectively complements the limitations of single data types and enhances the model?s robustness to market noise.

## ?워??

Sentiment analysis, Stock market, Technical analysis, Encoder, Robustness (evolution), Earnings, Financial market, Stock (firearms)

## ?키 ??

- [[pages/concepts/social_network_analysis|SNA]]

## 메모
