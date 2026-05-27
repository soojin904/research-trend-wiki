---
title: "A Text-Based Taxonomy for Real-Time Detection of LLM Safety Boundary Dissolution: The 7×7×7 Framework"
authors: ['Canale Giuseppe']
year: 2026
publication_date: 2026-02-08
venue: "Zenodo (CERN European Organization for Nuclear Research)"
volume: "None"
issue: "None"
pages: ""
doi: "https://doi.org/10.5281/zenodo.18525550"
oa_status: "green"
openalex_id: "https://openalex.org/W7128304397"
query_keyword: "text analysis"
tags: ['Adversarial Robustness in Machine Learning', 'Topic Modeling', 'Hate Speech and Cyberbullying Detection']
keywords: ['Adversarial system', 'Context (archaeology)', 'Boundary (topology)', 'Profiling (computer programming)', 'Probability distribution', 'Taxonomy (biology)', 'State (computer science)']
source: openalex-keyword
---

# A Text-Based Taxonomy for Real-Time Detection of LLM Safety Boundary Dissolution: The 7×7×7 Framework

**저자**: Canale Giuseppe
**출처**: Zenodo (CERN European Organization for Nuclear Research)
**발행일**: 2026-02-08
**DOI**: https://doi.org/10.5281/zenodo.18525550
**수집 키워드**: text analysis

## 초록

Large Language Models are fixed mathematical functions: during inference, their weights do not change, and their output is a probability distribution over tokens conditioned on context. Safety training (RLHF, Constitutional AI) modifies these weights to make refusal tokens more probable for harmful requests, but this statistical bias competes with other learned biases—helpfulness, pattern continuation, expertise matching—within the same computation. When adversarial input activates the competing biases more strongly than the safety bias, the output distribution shifts toward compliance. We present the first text-based classification framework for real-time detection of this safety boundary dissolution in LLMs. Unlike existing taxonomies that catalog static vulnerabilities (OWASP, MITRE ATLAS) or temporal attack sequences, our 7°ø7°ø7 framework classifies patterns in text—analyzing input patterns, measurable context properties, and output indicators simultaneously. The framework comprises 7 input pattern categories that shift the output distribution, 7 measurable context properties estimable from text, and 7 output indicators of boundary dissolution, yielding 343 possible configurations. Critically, this framework is turn-agnostic—a sophisticated single prompt can induce immediate dissolution, while naive attacks may fail after hundreds of turns, because the relevant variable is which attention patterns the input activates, not how many turns have elapsed. Empirical validation across 200+ turns of adversarial dialogue shows the framework successfully identifies dissolution configurations such as (M2-Authority, S1-High-α, F2-Deference) = “Authority Capture” or (M3-Entropy, S2-Critical-H, F5-Output-Control-Failure) = “Safety Signal Dilution.” This work provides the first operational framework for real-time monitoring of LLM output distribution state through text analysis alone, addressing a critical gap in AI safety: existing frameworks tell us what can go wrong, but only our taxonomy tells us where we are right now.

## 키워드

Adversarial system, Context (archaeology), Boundary (topology), Profiling (computer programming), Probability distribution, Taxonomy (biology), State (computer science)

## 주제 분류 (OpenAlex Topics)

- Adversarial Robustness in Machine Learning (score: 0.828)
- Topic Modeling (score: 0.045)
- Hate Speech and Cyberbullying Detection (score: 0.016)

## 메모

