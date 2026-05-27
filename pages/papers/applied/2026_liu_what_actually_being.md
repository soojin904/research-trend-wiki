---
title: "What Is Actually Being Annotated? Inter-Prompt Reliability as a Measurement Problem in LLM-Based Social Science Labeling"
authors: ['Jingyuan Liu']
year: 2026
venue: "arXiv (Cornell University)"
tags: ['Computational and Text Analysis Methods', 'Explainable Artificial Intelligence (XAI)', 'Sentiment Analysis and Opinion Mining']
source: raw/applied/applied_2026_What_Is_Actually_Being_An_nodoi.md
---

# What Is Actually Being Annotated? Inter-Prompt Reliability as a Measurement Problem in LLM-Based Social Science Labeling
**제목(한글)**: 실제로 무엇이 어노테이션되고 있는가? LLM 기반 사회과학 레이블링에서 프롬프트 간 신뢰도(IPR)의 측정 문제

**저자**: Jingyuan Liu
**출처**: arXiv (Cornell University), Vol.None
**발행일**: 2026-04-02
**DOI**: 

## 한국어 요약

**연구질문**: LLM 기반 어노테이션이 의미론적으로 동등하지만 언어적으로 다양한 프롬프트에 걸쳐 얼마나 안정적인가? 프롬프트 변형이 측정의 신뢰도에 미치는 영향은 어떻게 정량화할 수 있는가?

**방법론**:
- 프롬프트 간 신뢰도(Inter-Prompt Reliability, IPR) 프레임워크를 제안하고, 쌍별 일치율(PAR)로 측정
- TREC(해석적 태스크)와 Politifact(지식 기반 태스크) 두 가지 어노테이션 태스크에서 평가

**주요 결과**:
- 해석적 태스크에서 LLM 어노테이션이 상당한 확률적 변동을 보인 반면, 지식 기반 태스크에서는 상대적으로 안정적임
- 프롬프트 다수결 투표가 재현성을 크게 향상시키고 분산을 감소시킴

## 초록 (원문)

Large language models (LLMs) are increasingly used for annotation in computational social science, yet their methodological reliability under prompt variation remains unclear. This paper introduces Inter-Prompt Reliability (IPR), a framework for evaluating the stability of LLM outputs across semantically equivalent but linguistically varied prompts. Drawing on Inter-Rater Reliability, IPR is measured by Pairwise Agreement Rate (PAR) and its distribution to capture both consistency and stochasticity in model behavior. We evaluate this framework on two tasks with distinct properties: TREC (interpretative) and Politifact (knowledge-anchored). Results show that LLM annotation exhibits substantial stochastic variation in interpretative tasks, while appearing more stable in knowledge-based tasks. We further show that majority voting across prompts significantly improves reproducibility and reduces variance. These findings suggest that LLM prompt acts as an instrumental measurement while its wording exhibits methodological uncertainty. For future LLM-based CSS studies, we suggest that researchers move beyond single-prompt evaluation toward distributional stability and prompt aggregation within our IPR framework.

## 키워드

Reliability (semiconductor), Pairwise comparison, Consistency (knowledge bases), Variation (astronomy), Stability (learning theory), Annotation

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

