---
title: "Kernel Extreme Learning Machine-Based Sentiment Analysis for Social Networks"
authors: ['Janani Tamilarasu', 'Logeswari Shanmugam']
year: 2026
venue: "Tehnicki vjesnik - Technical Gazette"
tags: ['Machine Learning and ELM', 'Sentiment Analysis and Opinion Mining', 'Stock Market Forecasting Methods']
source: raw/applied/applied_2026_Kernel_Extreme_Learning_M_tv_20250320002495.md
---

# Kernel Extreme Learning Machine-Based Sentiment Analysis for Social Networks
**제목(한글)**: 소셜 네트워크 분석을 위한 커널 익스트림 러닝 머신 기반 감성 분석

**저자**: Janani Tamilarasu; Logeswari Shanmugam
**출처**: Tehnicki vjesnik - Technical Gazette, Vol.33
**발행일**: 2026-03-01
**DOI**: https://doi.org/10.17559/tv-20250320002495

## 한국어 요약

**연구질문**: 대규모 소셜 네트워크의 비정형 단문 포스트 감성을 높은 일반화 신뢰도와 연산 속도로 정확히 식별하기 위해, 신경망 기반 임베딩과 최적화 알고리즘을 어떻게 KELM과 융합할 수 있는가?

**방법론**:
- 소셜 네트워크 텍스트 정제 전처리를 거쳐 BERT(Bidirectional Encoder Representations from Transformers) 임베딩 모듈을 통한 고차원 의미 특징 추출 수행
- 고속 기계 학습과 일반화 능력이 입증된 커널 익스트림 러닝 머신(KELM) 분류기 적용
- KELM의 하이퍼파라미터 최적화를 위해 개량된 쇠똥구리 최적화(IDBO) 메타휴리스틱 알고리즘 탑재 및 벤치마크 테스트 수행

**주요 결과**:
- 제안하는 KELMSASN-IDBO 모델이 하이퍼파라미터 자율 보정을 통해 기존 일반 분류 모델들 대비 감성 예측 속도와 분류 정확도를 동시에 크게 개선함을 검증
- 복잡하고 대규모인 소셜 네트워크 빅데이터 감성을 실시간에 가깝게 추출 가능한 효율적 최적화 분류 체계를 확립함


## 초록 (원문)

The exponential growth of user-generated content on social media platforms presents both opportunities and challenges in extracting meaningful insights.Sentiment Analysis (SA), a critical component of contextual mining, enables the identification of subjective information embedded within textual data.This article proposes a novel Kernel Extreme Learning Machine-Based Sentiment Analysis of Social Networks Using Improved Dung Beetle Optimization (KELMSASN-IDBO) model, which combines advanced machine learning and nature-inspired optimization techniques to enhance sentiment classification accuracy.The model follows a structured pipeline: initially, raw textual data undergo thorough preprocessing to eliminate noise and standardize content.Subsequently, semantic features are extracted using Bidirectional Encoder Representations from Transformers (BERT) for effective word embedding.The resulting features are then classified using a Kernel Extreme Learning Machine (KELM), known for its high generalization performance and rapid learning speed.To optimize the performance of KELM, an Improved Dung Beetle Optimization (IDBO) algorithm is employed for fine-tuning hyperparameters.Experimental results demonstrate that the proposed KELMSASN-IDBO model outperforms conventional sentiment analysis techniques in terms of accuracy, efficiency, and robustness.The integration of deep contextual embeddings and hybrid optimization makes the proposed model a powerful tool for extracting sentiments from complex and large-scale social network data.

## 키워드

Sentiment analysis, Preprocessor, Data pre-processing, Component (thermodynamics), Extreme learning machine, Generalization, Deep learning, Kernel (algebra)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

