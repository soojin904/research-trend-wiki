---
title: "Reliability-Aware Multilingual Sentiment Analytics for Agricultural Market Intelligence"
authors: ['Jantima Polpinij', 'Christopher S. G. Khoo', 'Wei-Ning Cheng', 'Thananchai Khamket', 'Chumsak Sibunruang', 'Manasawee Kaenampornpan']
year: 2026
venue: "Mathematics"
tags: ['Sentiment Analysis and Opinion Mining', 'Text and Document Classification Technologies', 'Stock Market Forecasting Methods']
source: raw/applied/applied_2026_ReliabilityAware_Multilin_math14071220.md
---

# Reliability-Aware Multilingual Sentiment Analytics for Agricultural Market Intelligence
**제목(한글)**: 농업 시장 지능화(Intelligence)를 위한 신뢰성 인식 다국어 감성 분석 기술

**저자**: Jantima Polpinij; Christopher S. G. Khoo; Wei-Ning Cheng; Thananchai Khamket; Chumsak Sibunruang; Manasawee Kaenampornpan
**출처**: Mathematics, Vol.14, pp.1220-1220
**발행일**: 2026-04-05
**DOI**: https://doi.org/10.3390/math14071220

## 한국어 요약

**연구질문**: 가격 예측이 불가능하고 변동성이 심한 농업 원자재 시장에서, 소셜 미디어와 기사에 실린 다국어(태국어 및 영어) 텍스트의 노이즈와 편향성을 걸러내고 신뢰성 있는 시장 정보로 수렴할 감성 마이닝 프레임워크는 무엇인가?

**방법론**:
- 태국어 및 영어 농업 커모디티 관련 대규모 텍스트 데이터셋 수집
- 약지도 학습(Weakly Supervised) 기반 다국어 트랜스포머 모델 설계
- 노이즈 제거를 위해 의사 레이블 필터링(pseudo-label filtering), 데이터 소스 간 교차 일치성 정제, 전문가 보정 메커니즘 융합

**주요 결과**:
- 신뢰성 가중 필터링을 도입함으로써 기존의 표준 다국어 트랜스포머 베이스라인 대비 감성 지수의 시장 동향 예측율을 유의미하게 향상시킴을 확인함
- 농가 및 원자재 유통 기업을 위해 데이터 소스 격차와 다국어 표기 한계를 극복하고 시계열 가격 동향 감시의 효율성을 검증함


## 초록 (원문)

Public opinion on online platforms now plays an important role in agricultural markets, which have always been unpredictable. Although sentiment analysis has been widely applied to agricultural texts, most existing studies typically focus only on classification accuracy without connecting results to actual market intelligence systems, especially in multilingual contexts. This paper introduces a reliability-aware transformer-based framework for analyzing sentiment in agricultural market intelligence across multiple languages. The framework leverages weakly supervised multilingual transformers to extract sentiment signals from large-scale unlabeled Thai and English texts about major agricultural commodities found online. To enhance robustness under weak supervision, the framework incorporates reliability-aware mechanisms, including confidence-based pseudo-label filtering, cross-source consistency refinement, and expert-guided calibration to reduce noise and account for bias between different data sources. Sentiment predictions are further aligned with market intelligence objectives through reliability-weighted aggregation, yielding interpretable sentiment indices that enable cross-lingual and cross-source comparability. We tested the framework extensively using a multilingual agricultural corpus derived from social media and news coverage of agriculture. The results show consistent improvements over both classical machine learning approaches and standard multilingual transformer baselines. Additional ablation studies and sensitivity analyses confirmed that reliability-aware mechanisms, particularly confidence thresholding, play a crucial role in getting the right balance between label quality and data coverage. Overall, the results indicate that reliability-aware multilingual sentiment analytics provide robust and actionable insights for agricultural market monitoring and policy analysis.

## 키워드

Sentiment analysis, Market intelligence, Robustness (evolution), Analytics, Social media, Data quality, Supervised learning, Transformer

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

