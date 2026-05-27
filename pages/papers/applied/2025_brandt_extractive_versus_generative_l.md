---
title: "Extractive versus Generative Language Models for Political Conflict Text Classification"
authors: ['Patrick T. Brandt', 'Sultan Alsarra', 'Vito D’Orazio', 'Dagmar Heintze', 'Latifur Khan', 'Shreyas Meher', 'Javier Osorio', 'Marcus Sianan']
year: 2025
venue: "Political Analysis"
tags: ['Computational and Text Analysis Methods', 'Hate Speech and Cyberbullying Detection', 'Sentiment Analysis and Opinion Mining']
source: raw/applied/applied_2025_Extractive_versus_Generat_pan_2025_10027.md
---

# Extractive versus Generative Language Models for Political Conflict Text Classification

**제목(한글)**: 정치 갈등 텍스트 분류를 위한 추출적 대 생성적 언어 모델 비교

## 한국어 요약

**연구질문**: 정치·폭력 텍스트 분류에서 도메인 특화 파인튜닝 모델(ConfliBERT)이 범용 대형 언어 모델(LLM)보다 우수한가?

**방법론**:
- ConfliBERT(파인튜닝)와 Gemma 2, Llama 3.1, Qwen 2.5 비교
- BBC, re3d, Global Terrorism Database 텍스트 평가
- 정확도·정밀도·재현율·처리 속도 비교

**주요 결과**:
- ConfliBERT가 관련 도메인에서 범용 LLM보다 정확도·정밀도·재현율 모두 우수
- 범용 LLM 대비 수백 배 빠른 처리 속도
- 오픈소스 파인튜닝 모델이 비용·효율 면에서 강력한 대안

**저자**: Patrick T. Brandt; Sultan Alsarra; Vito D’Orazio; Dagmar Heintze; Latifur Khan; Shreyas Meher; Javier Osorio; Marcus Sianan
**출처**: Political Analysis, Vol.None, pp.1-29
**발행일**: 2025-12-31
**DOI**: https://doi.org/10.1017/pan.2025.10027

## 초록 (원문)

Abstract We review our recent ConfliBERT language model (Hu et al . 2022 [ConfliBERT: A Pre-Trained Language Model for Political Conflict and Violence]) to process political and violence-related texts. When fine-tuned, results show that ConfliBERT has superior performance in accuracy, precision, and recall over other large language models (LLMs) like Google’s Gemma 2 (9B), Meta’s Llama 3.1 (7B), and Alibaba’s Qwen 2.5 (14B) within its relevant domains. It is also hundreds of times faster than these more generalist LLMs. These results are illustrated using texts from the BBC, re3d, and the Global Terrorism Database. We demonstrate that open, fine-tuned models can outperform the more general models in terms of accuracy, precision, and recall, and at a fraction of the cost.

## 키워드

Generative grammar, Recall, Language model, Politics, Terrorism, Generative model

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

