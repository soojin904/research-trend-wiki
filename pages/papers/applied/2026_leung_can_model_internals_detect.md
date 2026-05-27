---
title: "Can Model Internals Detect MCP Tool Poisoning That Text Analysis Cannot?"
authors: ['Wan Sheng Leung']
year: 2026
venue: "Open MIND"
tags: ['Natural Language Processing Techniques', 'Academic integrity and plagiarism', 'Topic Modeling']
source: raw/applied/applied_2026_Can_Model_Internals_Detec_zenodo_19990741.md
---

# Can Model Internals Detect MCP Tool Poisoning That Text Analysis Cannot?
**제목(한글)**: 모델의 내부 활성화 분석이 텍스트 스캔으로 잡지 못하는 MCP 도구 오염을 감지할 수 있는가?

**저자**: Wan Sheng Leung
**출처**: Open MIND, Vol.None
**발행일**: 2026-05-03
**DOI**: https://doi.org/10.5281/zenodo.19990741

## 한국어 요약


## 초록 (원문)

I investigate whether looking inside a model's activations can catch poisoned MCP tool descriptions better than text scanning. On a dataset where safe and malicious descriptions cover the same topics with heavily overlapping vocabulary, text classifiers top out at 72-79%. A simple logistic regression trained on GPT-2's internal activations hits 97-98.5% and stays at 97% even after removing the effect of text length. Statistically significant (p=0.005). But this is GPT-2, not Claude, and 200 LLM-generated samples, not production data. The next step is SAE analysis on a real model.

## 키워드

Logistic regression, Text messaging, Production (economics), Cover (algebra), Simple (philosophy), Text mining

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

