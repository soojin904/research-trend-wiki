---
title: "Sentiment Analyzer: A Multi-Method Sentiment Analysis System"
authors: ['Anshu Verma', 'Anup Kumar Choudhary', 'Jyotiraditya Kathua', 'Mohit Sharma']
year: 2026
venue: "Open MIND"
tags: ['Sentiment Analysis and Opinion Mining', 'Mental Health via Writing', 'Hate Speech and Cyberbullying Detection']
source: raw/applied/applied_2026_Sentiment_Analyzer_A_Mult_zenodo_19940789.md
---

# Sentiment Analyzer: A Multi-Method Sentiment Analysis System
**제목(한글)**: 감성 분석기: 다중 방법론 감성 분석 시스템

**저자**: Anshu Verma; Anup Kumar Choudhary; Jyotiraditya Kathua; Mohit Sharma
**출처**: Open MIND, Vol.None
**발행일**: 2026-01-01
**DOI**: https://doi.org/10.5281/zenodo.19940789

## 한국어 요약

**연구질문**: 사전 기반 방법, 머신러닝 분류기, 앙상블 기법을 통합하여 정확하고 강인한 감성 및 감정 탐지를 수행하는 모듈형 시스템을 구축할 수 있는가?

**방법론**:
- 다중 방법론 통합(VADER/TextBlob 사전 기반 + Logistic Regression/Naive Bayes/SVM 머신러닝)
- FastAPI 기반 REST API 및 Streamlit 기반 대시보드 구축
- SST-2 벤치마크 데이터셋을 이용한 성능 평가 및 성능 측정(단일 텍스트 및 배치 처리 속도)

**주요 결과**:
- 앙상블 분류 방식이 91.3%의 정확도를 기록하여, 단일 VADER(71.3%) 및 로지스틱 회귀(81.2%) 대비 성능 대폭 개선
- 텍스트 전처리, 감성 및 감정 분석, 이모지 분석, 시각화를 지원하는 모듈형 아키텍처 구현
- API 단일 분석 속도 50ms 미만, 100건 배치 처리 450ms 미만의 효율적인 응답 속도 확인


## 초록 (원문)

Sentiment analysis has emerged as a critical application of natural language processing (NLP) in the digita l age. This paper presents Sentiment Analyzer, a comprehensive multi-method sentiment analysis system that combines lexicon-based methods (VADER, TextBlob), machine learning (ML) classifiers, and ensemble techniques to provide accurate and robust sentiment detection. The system implements a modular architecture with components for text preprocessing, sentiment analysis, emotion detection, emoji analysis, and result visualization. A FastAPI-based REST API enables programmatic access, while an interactive Streamlit dashboard provides a user-friendly interface. The ML pipeline employs TF-IDF vectorization with Logistic Regression, Naive Bayes, and Support Vector Machine classifiers. Experimental evaluation on the SST-2 benchmark demonstrates ensemble classification accuracy of 91.3%, outperforming standalone VADER (71.3%) and basic Logistic Regression (81.2%). API endpoints respond in under 50 ms for single-text analysis, and batch processing of 100 texts completes in under 450 ms.

## 키워드

Sentiment analysis, Pipeline (software), Benchmark (surveying), Support vector machine, Modular design, Random forest, Ensemble forecasting

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

