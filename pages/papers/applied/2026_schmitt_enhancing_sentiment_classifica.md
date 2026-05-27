---
title: "Enhancing Sentiment Classification and Irony Detection in Large Language Models through Advanced Prompt Engineering Techniques"
authors: ['Marvin Schmitt', 'Anne Schwerk', 'Sebastian Lempert']
year: 2026
venue: "ArXiv.org"
tags: ['Sentiment Analysis and Opinion Mining', 'Topic Modeling', 'Stock Market Forecasting Methods']
source: raw/applied/applied_2026_Enhancing_Sentiment_Class_nodoi.md
---

# Enhancing Sentiment Classification and Irony Detection in Large Language Models through Advanced Prompt Engineering Techniques
**제목(한글)**: 고급 프롬프트 엔지니어링 기법을 통한 거대 언어 모델의 감성 분류 및 반어법 감지 향상

## 한국어 요약

**연구질문**: GPT-4o-mini 및 gemini-1.5-flash 등의 LLM에서 퓨샷 학습, 연쇄적 사고(Chain-of-Thought), 자기 일관성(Self-Consistency) 등 고급 프롬프트 기법이 감성 분류와 반어법 감지 성능을 어떻게 향상시키는가?

**방법론**:
- GPT-4o-mini와 gemini-1.5-flash 두 모델에 기본 베이스라인, 퓨샷 학습, CoT 프롬프팅, 자기 일관성 등 여러 프롬프팅 전략을 체계적으로 비교 평가
- 감성 분류, 측면 기반 감성 분석(ABSA), 반어법 감지 등 세 가지 세부 태스크에서 정확도, 재현율, 정밀도, F1 점수로 성능 측정

**주요 결과**:
- 고급 프롬프팅 기법이 전반적으로 감성 분석 성능을 향상시켰으며, GPT-4o-mini는 퓨샷 접근법, gemini-1.5-flash는 CoT 프롬프팅이 반어법 감지에서 최대 46%까지 성능을 끌어올림
- 프롬프팅 전략의 효과가 모델 구조와 태스크 의미론적 복잡도에 따라 달라지므로, 모델 아키텍처와 과제 특성에 맞춰 맞춤형 전략을 설계해야 함을 강조

**저자**: Marvin Schmitt; Anne Schwerk; Sebastian Lempert
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-01-13
**DOI**: 

## 초록 (원문)

This study investigates the use of prompt engineering to enhance large language models (LLMs), specifically GPT-4o-mini and gemini-1.5-flash, in sentiment analysis tasks. It evaluates advanced prompting techniques like few-shot learning, chain-of-thought prompting, and self-consistency against a baseline. Key tasks include sentiment classification, aspect-based sentiment analysis, and detecting subtle nuances such as irony. The research details the theoretical background, datasets, and methods used, assessing performance of LLMs as measured by accuracy, recall, precision, and F1 score. Findings reveal that advanced prompting significantly improves sentiment analysis, with the few-shot approach excelling in GPT-4o-mini and chain-of-thought prompting boosting irony detection in gemini-1.5-flash by up to 46%. Thus, while advanced prompting techniques overall improve performance, the fact that few-shot prompting works best for GPT-4o-mini and chain-of-thought excels in gemini-1.5-flash for irony detection suggests that prompting strategies must be tailored to both the model and the task. This highlights the importance of aligning prompt design with both the LLM's architecture and the semantic complexity of the task.

## 키워드

Irony, Sentiment analysis, Key (lock), Boosting (machine learning), Language model

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

