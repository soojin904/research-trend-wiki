---
title: "The development and evaluation of agricultural question-answering systems based on large language models"
authors: ['Ayşe Eldem', 'Hüseyin Eldem']
year: 2026
venue: "Scientific Reports"
tags: ['Topic Modeling', 'Expert finding and Q&A systems', 'Educational Technology and Assessment']
source: raw/applied/applied_2026_The_development_and_evalu_s41598_026_35003_9.md
---

# The development and evaluation of agricultural question-answering systems based on large language models
**제목(한글)**: 대형 언어 모델 기반 농업 분야 질의응답 시스템의 개발 및 평가

**저자**: Ayşe Eldem; Hüseyin Eldem
**출처**: Scientific Reports, Vol.16, pp.5357-5357
**발행일**: 2026-02-09
**DOI**: https://doi.org/10.1038/s41598-026-35003-9

## 한국어 요약

**연구질문**: 농업 전문가(엔지니어, 기술자)의 의사결정을 돕기 위해, GPT-4o 및 Gemini 2.0 모델 상에서 다양한 프롬프트 엔지니어링 기술을 활용한 농업 전문 질의응답의 정확도와 신뢰성을 극대화하는 방안은 무엇인가?

**방법론**:
- 일반 농학, 원예학, 작물 생산의 3대 범주와 3개 난이도로 구성된 다지선다형 농업 전문 문제 데이터셋 구축
- GPT-4o 및 Gemini-2.0-Flash 모델을 대상으로 Zero-Shot, CoT, Self-Consistency, ToT 프롬프트 전략 적용 및 APE(자동프롬프트엔지니어링) 최적화 파이프라인 가동
- 부트스트랩 신뢰구간, ANOVA, t-test, Cohen's d/h 효과 크기를 사용하여 결과 통계 평가

**주요 결과**:
- LLM은 농업 질문 해결에서 전반적으로 우수한 성과를 보였으나 모델 종류와 프롬프트 전략에 따라 정답률 편차가 크게 나타남
- APE로 튜닝된 자동 최적화 프롬프트가 모델의 의미 추론력을 보완해 정답의 일관성과 정확성을 획기적으로 개선함을 정량 규명하여 실무 농업 가이드 어플리케이션의 가능성을 입증함


## 초록 (원문)

Large language models (LLMs) show superior performance in different fields. However, the applications of these models, which have shown superior performance in many studies, are still limited and incomplete in agriculture. In this study, a comprehensive evaluation has been made the use of LLMs in the field of agriculture. A set of multiple-choice questions was developed, covering three topics (General, Horticulture, Crop Production) and three difficulty levels (Easy, Medium, Difficult). For each question, answers were generated using GPT-4o and Gemini-2.0-flash LLMs. Zero-Shot, Chain-of-Thought (CoT), Self-Consistency, and Tree-of-Thought (ToT) techniques were preferred as prompt strategies. An automatically optimized prompting pipeline was also applied using Automatic Prompt Engineering (APE) to improve reasoning ability in agricultural question answering. Furthermore, the effect of the prompt methods used on both the accuracy and consistency of the answers was examined. In this study applied in the field of agriculture, the general success of question-answering systems (QAs) was evaluated and the effect of optimized prompts on system success was examined. The findings revealed that LLMs were generally successful, but their results varied significantly depending on the preferred LLM and prompt strategy. The results obtained were analyzed in detail statistically using bootstrap confidence intervals, paired t-tests, ANOVA, and effect size measures (Cohen's h and d) within the scope of the LLM model, prompt method, difficulty levels, and category-based format. This study introduces one of the first domain-specific question answering systems powered by LLMs, tailored for agricultural experts such as engineers and technicians, and presents an innovative approach by creating an infrastructure for smart digital applications in the field of agriculture.

## 키워드

Consistency (knowledge bases), Field (mathematics), Scope (computer science), Pipeline (software), Set (abstract data type), Agriculture

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

