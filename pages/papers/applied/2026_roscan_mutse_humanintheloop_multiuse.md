---
title: "MuTSE: A Human-in-the-Loop Multi-use Text Simplification Evaluator"
authors: ['Rares-Alexandru Roscan', 'Gabriel Petre1', 'Adrian-Marius Dumitran', 'Angela-Liliana Dumitran']
year: 2026
venue: "arXiv (Cornell University)"
tags: ['Text Readability and Simplification', 'Topic Modeling', 'Second Language Acquisition and Learning']
source: raw/applied/applied_2026_MuTSE_A_HumanintheLoop_Mu_nodoi.md
---

# MuTSE: A Human-in-the-Loop Multi-use Text Simplification Evaluator

**제목(한글)**: MuTSE: 인간 참여형(Human-in-the-Loop) 다목적 텍스트 단순화 평가 도구

## 한국어 요약

**연구질문**: LLM이 생성한 텍스트 단순화 결과물을 다양한 프롬프팅 전략과 모델 구성에 걸쳐 체계적으로 비교 평가할 구조화된 시각적 프레임워크가 없는 상황에서, 연구자와 교육자 모두를 위한 인터랙티브 평가 플랫폼을 어떻게 설계할 수 있는가?

**방법론**:
- P×M 프롬프트-모델 조합의 동시 실행 및 실시간 비교 행렬 생성을 지원하는 웹 애플리케이션 개발
- 선형성 편향 휴리스틱(λ)으로 보강된 계층적 의미 정렬 엔진 구현
- CEFR 숙련도 수준을 대상으로 LLM 생성 텍스트 단순화의 원문-변환문 시각적 매핑

**주요 결과**:
- 다양한 프롬프트-모델 조합의 동시 비교를 통해 질적 분석에 따른 인지적 부담을 줄이고 재현 가능한 구조화 어노테이션을 지원함
- NLP 연구용 데이터셋 구축과 지능형 튜터링 시스템(ITS) 개발에 활용 가능한 실용적 평가 인프라를 제공함

**저자**: Rares-Alexandru Roscan; Gabriel Petre1; Adrian-Marius Dumitran; Angela-Liliana Dumitran
**출처**: arXiv (Cornell University), Vol.None
**발행일**: 2026-04-10
**DOI**: 

## 초록 (원문)

As Large Language Models (LLMs) become increasingly prevalent in text simplification, systematically evaluating their outputs across diverse prompting strategies and architectures remains a critical methodological challenge in both NLP research and Intelligent Tutoring Systems (ITS). Developing robust prompts is often hindered by the absence of structured, visual frameworks for comparative text analysis. While researchers typically rely on static computational scripts, educators are constrained to standard conversational interfaces -- neither paradigm supports systematic multi-dimensional evaluation of prompt-model permutations. To address these limitations, we introduce \textbf{MuTSE}\footnote{The project code and the demo have been made available for peer review at the following anonymized URL. https://osf.io/njs43/overview?view_only=4b4655789f484110a942ebb7788cdf2a, an interactive human-in-the-loop web application designed to streamline the evaluation of LLM-generated text simplifications across arbitrary CEFR proficiency targets. The system supports concurrent execution of $P \times M$ prompt-model permutations, generating a comprehensive comparison matrix in real-time. By integrating a novel tiered semantic alignment engine augmented with a linearity bias heuristic ($λ$), MuTSE visually maps source sentences to their simplified counterparts, reducing the cognitive load associated with qualitative analysis and enabling reproducible, structured annotation for downstream NLP dataset construction.

## 키워드

Heuristic, Annotation, Code (set theory), Source code, Semantics (computer science), Software, Semantic Web

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]
- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모

