---
title: "Political DEBATE: Efficient Zero-Shot and Few-Shot Classifiers for Political Text"
authors: ['Michael Burnham', 'Kayla Kahn', 'Ryan Yang Wang', 'Rachel X. Peng']
year: 2025
venue: "Political Analysis"
tags: ['Computational and Text Analysis Methods', 'Misinformation and Its Impacts', 'Sentiment Analysis and Opinion Mining']
source: raw/applied/applied_2025_Political_DEBATE_Efficien_pan_2025_10028.md
---

# Political DEBATE: Efficient Zero-Shot and Few-Shot Classifiers for Political Text

**제목(한글)**: Political DEBATE: 정치 텍스트를 위한 효율적인 제로샷·퓨샷 분류기

## 한국어 요약

**연구질문**: 오픈소스 정치 도메인 특화 기반 모델(DEBATE)이 대규모 범용 LLM과 유사한 제로샷·퓨샷 분류 성능을 보이면서도 훨씬 효율적일 수 있는가?

**방법론**:
- BERT 기반 DEBATE 언어 모델(제로샷·퓨샷·지도 학습 분류)
- PolNLI 데이터셋(20만+ 정치 문서, 800개 이상 분류 태스크) 구축
- 기존 지도 학습 분류기 및 생성 LLM과 비교

**주요 결과**:
- DEBATE가 제로샷에서 최고 수준 LLM과 동등 성능이며 수십 배 더 효율적·완전 오픈소스
- 퓨샷(10~25개 문서)으로 수백~수천 문서 훈련 지도 분류기 능가
- 공개 과학 표준에 부합하는 정치 텍스트 분류 솔루션 제시

**저자**: Michael Burnham; Kayla Kahn; Ryan Yang Wang; Rachel X. Peng
**출처**: Political Analysis, Vol.None, pp.1-15
**발행일**: 2025-12-15
**DOI**: https://doi.org/10.1017/pan.2025.10028

## 초록 (원문)

Abstract Social scientists have quickly adopted large language models (LLMs) for their ability to annotate documents without supervised training, an ability known as zero-shot classification. However, due to their computational demands, cost, and often proprietary nature, these models are frequently at odds with open science standards. This article introduces the Political Domain Enhanced BERT-based Algorithm for Textual Entailment (DEBATE) language models: Foundation models for zero-shot, few-shot, and supervised classification of political documents. As zero-shot classifiers, the models are designed to be used for common, well-defined tasks, such as topic and opinion classification. When used in this context, the DEBATE models are not only as good as state-of-the-art LLMs at zero-shot classification, but are orders of magnitude more efficient and completely open source. We further demonstrate that the models are effective few-shot learners. With a simple random sample of 10–25 documents, they can outperform supervised classifiers trained on hundreds or thousands of documents and state-of-the-art generative models. Additionally, we release the PolNLI dataset used to train these models—a corpus of over 200,000 political documents with highly accurate labels across over 800 classification tasks.

## 키워드

Generative grammar, Politics, Odds, Supervised learning, Simple (philosophy), Generative model, Language model

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

