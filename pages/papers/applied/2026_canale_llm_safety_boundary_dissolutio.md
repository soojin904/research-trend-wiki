---
title: "LLM Safety Boundary Dissolution"
authors: ['Giuseppe Canale']
year: 2026
venue: "Open MIND"
tags: ['Adversarial Robustness in Machine Learning', 'Topic Modeling', 'Ethics and Social Impacts of AI']
source: raw/applied/applied_2026_LLM_Safety_Boundary_Disso_ts7b9.md
---

# LLM Safety Boundary Dissolution
**제목(한글)**: LLM 안전 경계 용해

**저자**: Giuseppe Canale
**출처**: Open MIND, Vol.None
**발행일**: 2026-01-01
**DOI**: https://doi.org/10.17605/osf.io/ts7b9

## 한국어 요약

**연구질문**: 대형 언어 모델에 Refusal Refinement를 하였음에도 불구하고, 적대적 입력으로 인해 Refusal 임계치를 뛰어넘는 안전 경계 용해가 일어나는 텍스트 특성을 실시간 분류하는 프레임워크는 무엇인가?

**방법론**:
- 입력 패턴 7개 범주, 텍스트 가독성/엔트로피 문맥 7개 지표, Refusal 붕괴 출력 지표 7개 군을 결합한 3D 7x7x7 분류 프레임워크 설계
- 200턴 이상의 공격적 대화 데이터셋을 적용해 실시간 텍스트 상태 추적 타당성 검증

**주요 결과**:
- 공격 턴수와 무관하게 모델의 어텐션 필터를 강탈하는 특정 입력이 Refusal boundary를 실시간으로 해제시킴을 입증
- 공격적 문맥의 보안 붕괴 심도를 실시간 평가하는 Refusal 붕괴 지수화에 최초 성공


## 초록 (원문)

Large Language Models are fixed mathematical functions: during inference, their weights do not change, and their output is a probability distribution over tokens conditioned on context. Safety training (RLHF, Constitutional AI) modifies these weights to make refusal tokens more probable for harmful requests, but this statistical bias competes with other learned biases—helpfulness, pattern continuation, expertise matching—within the same computation. When adversarial input activates the competing biases more strongly than the safety bias, the output distribution shifts toward compliance. We present the first text-based classification framework for real-time detection of this safety boundary dissolution in LLMs. Unlike existing taxonomies that catalog static vulnerabilities (OWASP, MITRE ATLAS) or temporal attack sequences, our 7×7×7 framework classifies patterns in text—analyzing input patterns, measurable context properties, and output indicators simultaneously. The framework comprises 7 input pattern categories that shift the output distribution, 7 measurable context properties estimable from text, and 7 output indicators of boundary dissolution, yielding 343 possible Configurations. Critically, this framework is turn-agnostic—a sophisticated single prompt can induce immediate dissolution, while naive attacks may fail after hundreds of turns, because the relevant variable is which attention patterns the input activates, not how many turns have elapsed. Empirical validation across 200+ turns of adversarial dialogue shows the framework successfully identifies dissolution configurations such as (M2-Authority, S1-High-α, F2-Deference) = “Authority Capture” or (M3-Entropy, S2-Critical-H, F5-Output-Control-Failure) = “Safety Signal Dilution.” This work provides the first operational framework for real-time monitoring of LLM output distribution state through text analysis alone, addressing a critical gap in AI safety: existing frameworks tell us what can go wrong, but only our taxonomy tells us where we are right now.

## 키워드

Adversarial system, Context (archaeology), Boundary (topology), Distribution (mathematics), State (computer science), Work (physics)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

