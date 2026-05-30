---
title: "NEPTUN: Normalization for Romanized Nepali Sentiment Analysis"
authors: ['Chandra Prakash Chaudhary', 'Basanta Joshi', 'Aman Shakya', 'Santosh Giri']
year: 2025
venue: "Journal of Himalaya College of Engineering"
tags: ['Sentiment Analysis and Opinion Mining', 'Natural Language Processing Techniques', 'Authorship Attribution and Profiling']
source: raw/applied/applied_2025_NEPTUN_Normalization_for__jhcoe_v2i1_91508.md
---

# NEPTUN: Normalization for Romanized Nepali Sentiment Analysis
**제목(한글)**: NEPTUN: 로마자 표기 네팔어 감성 분석을 위한 정규화

## 한국어 요약

**연구질문**: 비표준 로마자 표기 네팔어(Romanized Nepali)의 불일치한 철자·문법·코드 혼용 문제를 해결하는 정규화 모듈이 감성 분석 정확도를 향상시킬 수 있는가?

**방법론**:
- NEPTUN(네팔어 음성 전사 기반 통합 정규화) 모듈 설계: 음성 전자법으로 데바나가리 변환 후 네팔어 사전 검증, 재역변환
- 빈도 기반 필터링으로 일반 변형 표기 유지
- 로지스틱 회귀, 나이브 베이즈, K-최근접 이웃, BERT 분류기로 성능 평가

**주요 결과**:
- NEPTUN 전처리 적용 시 모든 분류기에서 정확도 향상
- BERT 기반 분류기가 87.56%로 최고 정확도 달성
- 저자원 언어(low-resource language)에 맞춤형 전처리의 필요성 입증

**저자**: Chandra Prakash Chaudhary; Basanta Joshi; Aman Shakya; Santosh Giri
**출처**: Journal of Himalaya College of Engineering, Vol.2, pp.19-28
**발행일**: 2025-12-01
**DOI**: https://doi.org/10.3126/jhcoe.v2i1.91508

## 초록 (원문)

The growth of e-commerce has led to rise in user-generated reviews, many of which in Nepal are written in Romanized Nepali a non-standard form with inconsistent spelling, grammar and code-switching with English. These irregularities challenge traditional sentiment analysis methods. This study presents NEPTUN (NEpali Phonetic Translation-Based Unified Normalization), a novel module for normalizing Romanized Nepali, NEPTUN uses phonetic transliteration to map Romanized words to Devnagari, verifies them via a Nepali dictionary, and then back-transliterates them into standardized Romanized forms. It also applies frequency-based filtering to retain common variants, improving consistency. While similar techniques exist for Romanized Hindi and Urdu, NEPTUN is the first tailored to Romanized Nepali. Its effectiveness was tested using various sentiment classifiers- Logistic Regression, Naive Bayes, K-Nearest Neighbors, and BERT. NEPTUN-enhanced preprocessing improved model accuracy, with BERT achieving the highest at 87.56%. These results emphasize the need for domain-specific preprocessing in low-resource language like Nepali.

## 키워드

Romanization, Preprocessor, Normalization (sociology), Nepali, Mahalanobis distance, Discriminator, Deep learning

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

