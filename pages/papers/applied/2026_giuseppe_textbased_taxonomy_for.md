---
title: "A Text-Based Taxonomy for Real-Time Detection of LLM Safety Boundary Dissolution: The 7×7×7 Framework"
authors: ['Canale Giuseppe']
year: 2026
venue: "Zenodo (CERN European Organization for Nuclear Research)"
tags: ['Adversarial Robustness in Machine Learning', 'Topic Modeling', 'Hate Speech and Cyberbullying Detection']
source: raw/applied/applied_2026_A_TextBased_Taxonomy_for__zenodo_18525550.md
---

# A Text-Based Taxonomy for Real-Time Detection of LLM Safety Boundary Dissolution: The 7×7×7 Framework
**제목(한글)**: LLM 안전성 경계 해제 실시간 탐지를 위한 텍스트 기반 분류 체계: 7×7×7 프레임워크

**저자**: Canale Giuseppe
**출처**: Zenodo (CERN European Organization for Nuclear Research), Vol.None
**발행일**: 2026-02-08
**DOI**: https://doi.org/10.5281/zenodo.18525550

## 한국어 요약

**연구질문**: LLM의 안전 가이드 훈련(RLHF 등)으로 정착된 Refusal(거절) 토큰 출력 강제 바이어스가 대화 중에 활성화되는 교묘한 유익성/패턴 복제 바이어스에 눌려 우회 당하는 '안전 경계 해제(Safety Boundary Dissolution)' 현상을 텍스트만으로 어떻게 실시간 탐지하는가?

**방법론**:
- 적대적 탈옥(Jailbreak) 시도 대화록 코퍼스 분석
- 입력 편향 조절 유도 패턴 7종, 텍스트 문맥 특징 7종, 안전 해제 경고 지표 7종을 기하 조합한 343개 안전 상태 격자 모델(7x7x7 framework) 설계
- 모델의 주의 패턴(attention patterns)을 실시간 추적하여 안전 신호 약화 수준 정량화

**주요 결과**:
- '안전 신호 희석(Safety Signal Dilution)' 등의 우회 공격 성공 유형을 실시간 텍스트 상태 추적을 통해 정확히 식별하는 데 성공함
- 본 기하학적 분류 지표를 통해 대화 턴 진행 수와 무관하게 즉각적인 LLM 가드레일 무력화 국면을 실시간 포착하여 감시하는 보완 방안을 마련함


## 초록 (원문)

Large Language Models are fixed mathematical functions: during inference, their weights do not change, and their output is a probability distribution over tokens conditioned on context. Safety training (RLHF, Constitutional AI) modifies these weights to make refusal tokens more probable for harmful requests, but this statistical bias competes with other learned biases—helpfulness, pattern continuation, expertise matching—within the same computation. When adversarial input activates the competing biases more strongly than the safety bias, the output distribution shifts toward compliance. We present the first text-based classification framework for real-time detection of this safety boundary dissolution in LLMs. Unlike existing taxonomies that catalog static vulnerabilities (OWASP, MITRE ATLAS) or temporal attack sequences, our 7°ø7°ø7 framework classifies patterns in text—analyzing input patterns, measurable context properties, and output indicators simultaneously. The framework comprises 7 input pattern categories that shift the output distribution, 7 measurable context properties estimable from text, and 7 output indicators of boundary dissolution, yielding 343 possible configurations. Critically, this framework is turn-agnostic—a sophisticated single prompt can induce immediate dissolution, while naive attacks may fail after hundreds of turns, because the relevant variable is which attention patterns the input activates, not how many turns have elapsed. Empirical validation across 200+ turns of adversarial dialogue shows the framework successfully identifies dissolution configurations such as (M2-Authority, S1-High-α, F2-Deference) = “Authority Capture” or (M3-Entropy, S2-Critical-H, F5-Output-Control-Failure) = “Safety Signal Dilution.” This work provides the first operational framework for real-time monitoring of LLM output distribution state through text analysis alone, addressing a critical gap in AI safety: existing frameworks tell us what can go wrong, but only our taxonomy tells us where we are right now.

## 키워드

Adversarial system, Context (archaeology), Boundary (topology), Profiling (computer programming), Probability distribution, Taxonomy (biology), State (computer science)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

