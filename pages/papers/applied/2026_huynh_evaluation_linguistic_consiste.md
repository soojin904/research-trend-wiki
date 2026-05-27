---
title: "Evaluation of Linguistic Consistency of LLM-Generated Text Personalization Using Natural Language Processing"
authors: ['Linh Huynh', 'Danielle S. McNamara']
year: 2026
venue: "Electronics"
tags: ['Computational and Text Analysis Methods', 'Artificial Intelligence in Healthcare and Education', 'Text Readability and Simplification']
source: raw/applied/applied_2026_Evaluation_of_Linguistic__electronics15061262.md
---

# Evaluation of Linguistic Consistency of LLM-Generated Text Personalization Using Natural Language Processing
**제목(한글)**: 자연어 처리를 활용한 대형 언어 모델(LLM) 생성 개인화 텍스트의 언어적 일관성 평가

**저자**: Linh Huynh; Danielle S. McNamara
**출처**: Electronics, Vol.15, pp.1262-1262
**발행일**: 2026-03-18
**DOI**: https://doi.org/10.3390/electronics15061262

## 한국어 요약

**연구질문**: 동일한 프롬프트로 반복 생성된 LLM 출력물이 언어적 일관성을 유지하는지, 그리고 모델 버전 업데이트에 따라 언어적 특성이 유의미하게 변화하는지를 NLP 기반 평가 프레임워크로 어떻게 체계적으로 추적할 수 있는가?

**방법론**:
- Claude, Llama, Gemini, ChatGPT 4개 LLM을 활용해 10개 과학 텍스트에 대한 특정 독자 프로필 맞춤형 개인화 텍스트 10회 반복 생성(실험 1)
- GPT-4o(2024년 10월 vs 2025년 6월)와 GPT-4.1(2025년 6월) 간의 언어적 변이 비교(실험 2)
- 응집성(cohesion), 통사적 복잡도, 어휘 정교성 등 NLP 지표를 선형 혼합 효과 모델로 분석

**주요 결과**:
- 동일 모델의 단기 반복 생성 간에는 언어적 특성에 유의미한 차이가 없어 단기 일관성이 높음을 확인함
- 모델 버전 업데이트에 따른 언어적 변이는 유의미하게 나타났으며, GPT-4o(2025년 6월)는 더 간결하지만 응집력 있는 텍스트를, GPT-4.1은 더 학술적이고 통사적으로 복잡한 출력을 생성하는 것으로 규명함

## 초록 (원문)

This study proposes a Natural Language Processing (NLP)-based evaluation framework to examine the linguistic consistency of large language model (LLM)-generated personalized texts over time. NLP metrics were used to quantify and compare linguistic patterns across repeated generations produced using identical prompts. In Experiment 1, internal reliability was examined across 10 repeated generations from four LLMs (Claude, Llama, Gemini, and ChatGPT), applied to 10 scientific texts tailored for a specific reader profile. Linear mixed-effects models showed no effect of repeated generation on linguistic features (e.g., cohesion, syntactic complexity, lexical sophistication), suggesting short-term consistency across repeatedly generated outputs. Experiment 2 examined linguistic variation across model updates of GPT-4o (October 2024 vs. June 2025) and GPT-4.1 (June 2025). Significant variations were observed across outputs from different model versions. GPT-4o (June 2025) generated more concise but cohesive texts, whereas GPT-4.1 (June 2025) generated outputs that are more academic, lexically sophisticated, and complex in syntax. Given the rapid evolution of LLMs and the lack of standardized methods for tracking output consistency, the current work demonstrates one of the applications of NLP-based evaluation approaches for monitoring meaningful linguistic shifts across model updates over time.

## 키워드

Consistency (knowledge bases), Variation (astronomy), Personalization, Deep linguistic processing, Reliability (semiconductor), Lexical diversity, Linguistic analysis, Linguistic description

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

