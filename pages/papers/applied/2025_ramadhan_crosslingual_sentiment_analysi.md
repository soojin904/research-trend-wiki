---
title: "Cross-Lingual Sentiment Analysis for Indonesian Monetary Policy"
authors: ['Akbar Rahmat Ramadhan', 'Umar Zaky']
year: 2025
venue: "Journal of Scientific Research Education and Technology (JSRET)"
tags: ['Sentiment Analysis and Opinion Mining', 'Stock Market Forecasting Methods', 'Data Mining and Machine Learning Applications']
source: raw/applied/applied_2025_CrossLingual_Sentiment_An_jsret_v4i4_943.md
---

# Cross-Lingual Sentiment Analysis for Indonesian Monetary Policy

**제목(한글)**: 인도네시아 통화 정책에 대한 교차언어(Cross-Lingual) 감성 분석

## 한국어 요약

**연구질문**: 교차언어 자동 레이블링 파이프라인(RoBERTa-IndoBERT)은 저자원 환경에서 인도네시아어 감성 분석의 정확도를 향상시킬 수 있는가?

**방법론**:
- '번역 후 분류(translate-then-classify)' 파이프라인: 인도네시아어 게시물 → 영어 번역 → 성숙한 영어 RoBERTa 모델 자동 레이블링 → IndoBERT 미세조정
- 역번역(back-translation) 증강 포함/미포함 교차언어 접근법 vs. 기준 인도네시아 전용 모델 비교

**주요 결과**:
- 완전 모델(IndoBERT + CL + BT)의 Macro-F1 98.1%, 기준 모델(95.3%) 대비 2.8%p 향상
- 교차언어 모델이 극단적 극성 전환에 더 안정적이고 암묵적 감성 탐지 우수
- 저자원 시나리오의 인도네시아어 감성 분석에서 효율적·강인한 해결책 입증

**저자**: Akbar Rahmat Ramadhan; Umar Zaky
**출처**: Journal of Scientific Research Education and Technology (JSRET), Vol.4, pp.2588-2601
**발행일**: 2025-12-04
**DOI**: https://doi.org/10.58526/jsret.v4i4.943

## 초록 (원문)

This research develops a cross-lingual sentiment analysis system (RoBERTa-IndoBERT) to monitor public opinion on Bank Indonesia’s 2025 monetary policy from X (Twitter), addressing the scarcity of Indonesian labels and noisy social media text. We introduce a "translate-then-classify" pipeline: Indonesian posts are translated into English, auto-labeled by a mature English RoBERTa model, and these labels are used to fine-tune IndoBERT on the original texts. We compare this cross-lingual (CL) approach, with and without back-translation (BT) augmentation, against a baseline Indo-only model. Performance measured by Accuracy and Macro-F1 indicates the CL pipeline is substantially better than the baseline. The complete model (IndoBERT + CL + BT) yields a Macro-F1 of 98.1%, a 2.8 percentage point (pp) improvement over the baseline (95.3%). Qualitative error analysis corroborates the CL model is more stable, less prone to extreme polarity flips, and better at detecting implicit sentiment. This research demonstrates that a CL auto-labeling pipeline is an efficient and resilient solution for Indonesian sentiment analysis in low-resource scenarios.

## 키워드

Indonesian, Pipeline (software), Baseline (sea), Sentiment analysis, Point (geometry), Qualitative analysis, Monetary policy

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

