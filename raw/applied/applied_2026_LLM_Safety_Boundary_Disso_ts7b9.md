---
title: "LLM Safety Boundary Dissolution"
authors: ['Giuseppe Canale']
year: 2026
publication_date: 2026-01-01
venue: "Open MIND"
volume: "None"
issue: "None"
pages: ""
doi: "https://doi.org/10.17605/osf.io/ts7b9"
oa_status: "green"
openalex_id: "https://openalex.org/W7128717961"
query_keyword: "text analysis"
tags: ['Adversarial Robustness in Machine Learning', 'Topic Modeling', 'Ethics and Social Impacts of AI']
keywords: ['Adversarial system', 'Context (archaeology)', 'Boundary (topology)', 'Distribution (mathematics)', 'State (computer science)', 'Work (physics)']
source: openalex-keyword
---

# LLM Safety Boundary Dissolution

**저자**: Giuseppe Canale
**출처**: Open MIND
**발행일**: 2026-01-01
**DOI**: https://doi.org/10.17605/osf.io/ts7b9
**수집 키워드**: text analysis

## 초록

Large Language Models are fixed mathematical functions: during inference, their weights do not change, and their output is a probability distribution over tokens conditioned on context. Safety training (RLHF, Constitutional AI) modifies these weights to make refusal tokens more probable for harmful requests, but this statistical bias competes with other learned biases—helpfulness, pattern continuation, expertise matching—within the same computation. When adversarial input activates the competing biases more strongly than the safety bias, the output distribution shifts toward compliance. We present the first text-based classification framework for real-time detection of this safety boundary dissolution in LLMs. Unlike existing taxonomies that catalog static vulnerabilities (OWASP, MITRE ATLAS) or temporal attack sequences, our 7×7×7 framework classifies patterns in text—analyzing input patterns, measurable context properties, and output indicators simultaneously. The framework comprises 7 input pattern categories that shift the output distribution, 7 measurable context properties estimable from text, and 7 output indicators of boundary dissolution, yielding 343 possible Configurations. Critically, this framework is turn-agnostic—a sophisticated single prompt can induce immediate dissolution, while naive attacks may fail after hundreds of turns, because the relevant variable is which attention patterns the input activates, not how many turns have elapsed. Empirical validation across 200+ turns of adversarial dialogue shows the framework successfully identifies dissolution configurations such as (M2-Authority, S1-High-α, F2-Deference) = “Authority Capture” or (M3-Entropy, S2-Critical-H, F5-Output-Control-Failure) = “Safety Signal Dilution.” This work provides the first operational framework for real-time monitoring of LLM output distribution state through text analysis alone, addressing a critical gap in AI safety: existing frameworks tell us what can go wrong, but only our taxonomy tells us where we are right now.

## 키워드

Adversarial system, Context (archaeology), Boundary (topology), Distribution (mathematics), State (computer science), Work (physics)

## 주제 분류 (OpenAlex Topics)

- Adversarial Robustness in Machine Learning (score: 0.863)
- Topic Modeling (score: 0.034)
- Ethics and Social Impacts of AI (score: 0.016)

## 메모

