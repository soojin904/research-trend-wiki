---
title: "Metrics for Cultural Semantic Integrity in LLMs: A Low-Resource Perspective"
authors: []
year: 2026
venue: "RESEARCH RESULT Theoretical and Applied Linguistics"
tags: ['Natural Language Processing Techniques', 'Topic Modeling', 'Semantic Web and Ontologies']
source: raw/applied/applied_2026_Metrics_for_Cultural_Sema_2313_8912_2026_12_1_0_5.md
---

# Metrics for Cultural Semantic Integrity in LLMs: A Low-Resource Perspective
**제목(한글)**: LLM의 문화적 의미론적 정체성 측정을 위한 지표: 저자원 언어 관점

**저자**: 
**출처**: RESEARCH RESULT Theoretical and Applied Linguistics, Vol.12
**발행일**: 2026-03-30
**DOI**: https://doi.org/10.18413/2313-8912-2026-12-1-0-5

## 한국어 요약

**연구질문**: 영어 중심으로 편향된 다국어 LLM 학습 환경에서, 영어 매개 번역 및 텍스트 생성이 저자원 언어(예: 링갈라어)의 고유한 문화적·의미론적 구조를 왜곡시키는 현상을 어떻게 계량 측정할 수 있는가?

**방법론**:
- 영어 매개 역번역(Back-translation)을 진단 프로브로 삼아 고자원 러시아어와 저자원 링갈라(Lingala)어를 대비 분석
- 의미적 정체성을 평가하기 위해 3가지 다차원 지표(의미론적 자가 유사도 SSI, 이웃 보존 스코어 NPS, 특정 도덕 축 기준 의미 표상 드리프트) 설계 및 임베딩 공간 매핑

**주요 결과**:
- 러시아어는 표면 유사성(SSI)은 높으나 이웃 관계 안정성(NPS)에 부분 왜곡이 일어난 반면, 저자원 링갈라어는 SSI와 NPS가 모두 크게 망가지며 의미 구조가 붕괴됨을 식별
- 기존의 단순 표면 유사도 평가지표가 저자원 언어의 의미론적 손실 및 영어 편향 왜곡 현상을 심각하게 과소평가하고 있음을 증명하고, 이를 정량 진단할 고도화된 계량 툴킷을 개발함


## 초록 (원문)

Multilingual large language models (LLMs) are predominantly trained and evaluated within English-centric pipelines.However, the semantic consequences of English-language mediation at the level of textual representations remain poorly understood beyond surface-level similarity measures.This paper puts forward a metricbased approach to evaluating the cultural and semantic integrity of texts produced using multilingual large language models (LLMs), with a specific focus on low-resource languages.We set forth a set of complementary embedding-based metrics designed to diagnose how English mediation reshapes textual semantic representations at multiple levels.Using English-mediated back-translation via an LLM as a controlled diagnostic probe, we compare a high-resource language (Russian) with a low-resource language (Lingala).Texts are embedded into a shared semantic space, and semantic integrity is assessed using three metrics: Semantic Self-Similarity (SSI), capturing local semantic recognizability; Neighborhood Preservation Score (NPS), measuring the stability of local semantic relations; and axis-based drift, quantifying directional semantic bias along an interpretable semantic opposition.The results reveal a pronounced cross-linguistic asymmetry.Russian texts maintain high semantic self-similarity, indicating strong surface-level semantic preservation, but display only moderate neighborhood preservation, reflecting nontrivial structural reorganization.In contrast, Lingala texts show severe degradation in both semantic self-similarity and neighborhood preservation, indicating a collapse of relational semantic structure under English mediation.Additionally, Lingalabut not Russianexhibits a small yet systematic directional drift along the examined semantic axis.What is of importance is that this directional bias is independent of structural instability, which is indicative of multiple, distinct mechanisms of English-centric effect.These findings indicate that surface similarity metrics considerably underestimate semantic disruption, particularly for low-resource languages.The suggested framework provides a scalable diagnostic toolkit for assessing semantic integrity in multilingual LLM representations and is directly applicable to the analysis and evaluation of LLMgenerated texts beyond translation-based scenarios.Although we are validating the Litvinova Tatiana A., Zavarzina Galina A. Metrics for Cultural Semantic Integrity in LLMs: A Low-Resource . A., . A. -

## 키워드

Perspective (graphical), Data integrity, Semantics (computer science), Interpretation (philosophy), Context (archaeology), Feature (linguistics)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]
- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모

