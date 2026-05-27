---
title: "Feasibility of Using Large Language Models for Structured Medication Extraction from Clinical Text: A Comparative Analysis of Zero-Shot and Few-Shot Paradigms"
authors: ['Evan Jacob Schulte', 'Mohamed Abusharkh', 'Kushal Dahal', 'Michael E. Klepser', 'Minji Sohn']
year: 2026
venue: "Applied Sciences"
tags: ['Topic Modeling', 'Biomedical Text Mining and Ontologies', 'Pharmacovigilance and Adverse Drug Reactions']
source: raw/applied/applied_2026_Feasibility_of_Using_Larg_app16052300.md
---

# Feasibility of Using Large Language Models for Structured Medication Extraction from Clinical Text: A Comparative Analysis of Zero-Shot and Few-Shot Paradigms
**제목(한글)**: 임상 텍스트로부터 구조화된 약물 정보 추출을 위한 거대 언어 모델의 유효성: 제로샷과 퓨샷 패러다임의 비교 분석

**저자**: Evan Jacob Schulte; Mohamed Abusharkh; Kushal Dahal; Michael E. Klepser; Minji Sohn
**출처**: Applied Sciences, Vol.16, pp.2300-2300
**발행일**: 2026-02-27
**DOI**: https://doi.org/10.3390/app16052300

## 한국어 요약

**연구질문**: 비정형 임상 서술 기록 문서에서 정확한 약물 투여량 정보(용량, 빈도, 기간 등)를 구조적으로 추출하는 작업에 대해 LLM의 성능 신뢰도 및 프롬프트 패러다임별 효과는 무엇인가?

**방법론**:
- CHARM 레지스트리에서 유래한 외래 환자 항생제 임상 기록 활용
- 5가지 오픈 가중치 모델(GPT-OSS:20B, Gemma 2:9B, Mistral 7B, Qwen3:14B, Llama 3.2)을 대상 모델로 선정
- 제로샷(Zero-shot)과 RAG 기반 퓨샷(Few-shot) 프롬프트 구조에 맞춰 약물 개체명 및 처방전 정보 추출 정확도 비교

**주요 결과**:
- 추론 최적화 모델인 GPT-OSS:20B는 제로샷 설정(F1 > 0.90)에서 두각을 보였으나, 지시 튜닝된 Gemma 2:9B는 퓨샷 설정에서 예시 가이드라인을 효과적으로 활용해 최고 정확도(F1 ~ 0.99)를 기록하는 아키텍처별 트레이드오프 발견
- Mistral, Llama 등 소형 모델은 환각 현상(Hallucination)이 잦아 실무 적용이 위험하며, 불규칙 단위 및 복잡한 시점 분석 예외 처리에 RAG 전략이 보완되어야 함을 제시


## 초록 (원문)

The digitization of healthcare has been accompanied by a rapid expansion of electronic health records (EHRs); however, a significant proportion of critical patient data, specifically medication regimens, remains entrapped within unstructured clinical narratives. The inability to seamlessly compute this data hinders advancements in pharmacovigilance, clinical decision support, and population health management. This study presents a comprehensive, rigorous evaluation of the feasibility of deploying Large Language Models (LLMs) to automate the extraction of structured dosage information (Dose, Daily Frequency, Duration) from outpatient antimicrobial clinical notes sourced from the Collaboration to Harmonize Antimicrobial Registry Measures (CHARM) registry. We scrutinized the performance of five distinct open-weight architectures, namely GPT-OSS:20B, Gemma 2:9B, Mistral 7B, Qwen3:14B and Llama 3.2, across both Zero-Shot and Retrieval Augmented Generation (RAG)-based Few-Shot prompting paradigms. Our analysis reveals a fundamental architectural trade-off: the reasoning-optimized GPT-OSS:20B dominates the zero-shot landscape (F1 &gt; 0.90) by leveraging abstract schema understanding, whereas the instruction-tuned Gemma 2:9B excels in the few-shot setting (F1 ~ 0.99), effectively utilizing examples as guardrails to surpass larger models. Conversely, smaller models (Mistral, Llama) exhibit a prohibitive “hallucination barrier,” rendering them unsafe for unsupervised clinical application. Furthermore, we identify “Inconsistent Unit Handling” and “Complex Temporal Logic” as persistent failure modes that resist simple scaling laws. This report provides a definitive framework for selecting model architectures based on the availability of few-shot examples and highlights the necessity of dynamic RAG strategies to achieve production-grade reliability in medical informatics.

## 키워드

Schema (genetic algorithms), Population, Data extraction, Reliability (semiconductor), Bridging (networking), Health care, Data reliability, Rendering (computer graphics)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

