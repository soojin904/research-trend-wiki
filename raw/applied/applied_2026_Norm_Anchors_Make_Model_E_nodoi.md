---
title: "Norm Anchors Make Model Edits Last"
authors: ['Mingda Liu', 'Zhenghan Zhu', "Ze'an Miao", 'Katsuki Fujisawa']
year: 2026
publication_date: 2026-01-30
venue: "arXiv (Cornell University)"
volume: "None"
issue: "None"
pages: ""
doi: ""
oa_status: "green"
openalex_id: "https://openalex.org/W7127740317"
query_keyword: "text analysis"
tags: ['Model-Driven Software Engineering Techniques', 'Topic Modeling', 'Natural Language Processing Techniques']
keywords: ['Norm (philosophy)', 'Code (set theory)', 'Exponential growth', 'Scaling', 'Sequence (biology)', 'Point (geometry)']
source: openalex-keyword
---

# Norm Anchors Make Model Edits Last

**저자**: Mingda Liu; Zhenghan Zhu; Ze'an Miao; Katsuki Fujisawa
**출처**: arXiv (Cornell University)
**발행일**: 2026-01-30
**DOI**: 
**수집 키워드**: text analysis

## 초록

Model editing has emerged as a practical approach for mitigating factual errors and outdated knowledge in large language models (LLMs). Among existing methods, the Locate-and-Edit (L&E) paradigm is the dominant framework: it locates MLP parameters implicated in expressing a target fact, and then performs a localized update to rewrite that fact. However, long sequences of edits often trigger abrupt model collapse in L&E beyond a critical point. We empirically identify a strong correlation between collapse and explosive growth of edited MLP weight norms, and formally prove that commonly used L&E update rules can induce exponential norm growth across sequential edits in the absence of explicit norm control. To address this issue, we propose Norm-Anchor Scaling NAS, a plug-and-play norm-constrained strategy. Across extensive experiments, NAS delays the collapse point of representative L&E algorithms by more than 4 times and yields a 72.2% average relative gain in editing performance, requiring only a single additional line of code and incurring negligible computational overhead.

## 키워드

Norm (philosophy), Code (set theory), Exponential growth, Scaling, Sequence (biology), Point (geometry)

## 주제 분류 (OpenAlex Topics)

- Model-Driven Software Engineering Techniques (score: 0.867)
- Topic Modeling (score: 0.032)
- Natural Language Processing Techniques (score: 0.019)

## 메모

