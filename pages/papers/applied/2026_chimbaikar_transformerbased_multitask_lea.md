---
title: "A Transformer-Based Multi-Task Learning Framework for Sentiment, Emotion, and Sarcasm Analysis"
authors: ['Rohan Rajendra Chimbaikar']
year: 2026
venue: "INTERANTIONAL JOURNAL OF SCIENTIFIC RESEARCH IN ENGINEERING AND MANAGEMENT"
tags: ['Sentiment Analysis and Opinion Mining', 'Text and Document Classification Technologies', 'Emotion and Mood Recognition']
source: raw/applied/applied_2026_A_TransformerBased_MultiT_ijsrem55929.md
---

# A Transformer-Based Multi-Task Learning Framework for Sentiment, Emotion, and Sarcasm Analysis
**제목(한글)**: 감성, 감정, 반어법 분석을 위한 트랜스포머 기반의 다중 작업 학습 프레임워크

**저자**: Rohan Rajendra Chimbaikar
**출처**: INTERANTIONAL JOURNAL OF SCIENTIFIC RESEARCH IN ENGINEERING AND MANAGEMENT, Vol.10, pp.1-9
**발행일**: 2026-01-09
**DOI**: https://doi.org/10.55041/ijsrem55929

## 한국어 요약

**연구질문**: 텍스트의 정서적 의도를 종합 판별하기 위해 긴밀히 연관된 세 가지 작업(감성 분류, 감정 인식, 반어법 탐지)을 단일 모델로 결합하여 성능과 효율성을 높일 수 있는가?

**방법론**:
- 감성(Sentiment), 세부 감정(Emotion), 반어법(Sarcasm) 분석을 공동 수행하는 트랜스포머 기반 다중 작업 학습(Multi-task Learning) 프레임워크 설계
- 공유된 RoBERTa 인코더 구조에 각 분석 작업별 전용 분류 헤드를 연결하여 맥락 정보와 미세한 언어 단서를 융합

**주요 결과**:
- 제안된 다중 작업 학습 모델은 세 가지 세부 영역 모두에서 균형 잡힌 견고한 성능을 확보하여 개별 모델 구현 대비 연산 비용을 축소하고 텍스트의 종합 분석 수준을 향상시킴
- 소셜 미디어 분석 및 고객 피드백 정교화 등 현실 서비스 활용 가능성을 확인


## 초록 (원문)

Abstract - A major challenge in natural language processing is determining the emotional intent of text because sentiment, emotion, and sarcasm all work together. Most contemporary methods deal with these tasks individually, which leads to incomplete representations and greater computational costs. This study provides a transformer-based multitask learning system that jointly performs sentiment classification, fine-grained emotion recognition, and sarcasm detection within a single architecture. The framework uses a shared RoBERTa-based encoder with task-specific classification heads to capture the contextual dependencies and subtle linguistic cues. Experimental results reveal that the proposed multitask technique delivers a robust and balanced performance across all tasks, highlighting its efficacy for comprehensive affective text analysis in real-world applications such as social media monitoring and customer feedback analysis. Key Words: Sentiment Analysis; Emotion Recognition; Sarcasm Detection; Transformer Models; Multi-Task Learning

## 키워드

Sarcasm, Sentiment analysis, Key (lock), Computational linguistics, Multi-task learning, Transformer, Social media, Cognition

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

