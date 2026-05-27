---
title: "Predicting Stock Market Trends Through a Hybrid Machine Learning Framework That Combines Technical Indicators with News Sentiment Analysis"
authors: ['Jianjiang Li']
year: 2025
venue: "Applied and Computational Engineering"
tags: ['Stock Market Forecasting Methods', 'Sentiment Analysis and Opinion Mining', 'Financial Markets and Investment Strategies']
source: raw/applied/applied_2025_Predicting_Stock_Market_T_2026_tj30739.md
---

# Predicting Stock Market Trends Through a Hybrid Machine Learning Framework That Combines Technical Indicators with News Sentiment Analysis

**저자**: Jianjiang Li
**출처**: Applied and Computational Engineering, Vol.211, pp.209-216
**발행일**: 2025-12-18
**DOI**: https://doi.org/10.54254/2755-2721/2026.tj30739

## 초록 (원문)

This paper proposes a hybrid model based on LSTM(Long Short-Term Memory)and BERT(Bidirectional Encoder Representations from Transformers)for stock market trend prediction, which innovatively integrates the quantitative analysis of technical indicators and qualitative analysis of news sentiment. The framework first utilizes a pre-trained FinBERT model--optimized for financial text processing--to extract fine-grained sentiment features from multi-source financial data, including official earnings reports, mainstream financial news, and social media financial discussions. These sentiment features, together with key technical indicators derived from historical stock price data(such as moving averages, relative strength index, and trading volume), are standardized and concatenated into a comprehensive feature vector, which is then fed into a two-layer LSTM network for capturing temporal dependencies and dynamic sequence prediction. The experimental results, derived from a dataset encompassing 50 top stocks from the S&amp;P 500 over a span of 5 years, show that the proposed hybrid model consistently surpasses single-model methods--such as standalone LSTM, BERT, and traditional ARIMA--in terms of both short-term(1-day ahead)and medium-term(5-day ahead)prediction accuracy, as well as its ability to generalize across various market conditions, including bullish, bearish, and volatile environments. This confirms the significant value of multi-source data fusion in financial forecasting, as it effectively complements the limitations of single data types and enhances the model’s robustness to market noise.

## 키워드

Sentiment analysis, Stock market, Technical analysis, Encoder, Robustness (evolution), Earnings, Financial market, Stock (firearms)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

