---
title: "Explainable NLP in the Era of Large Language Models: A Unified Taxonomy, Evaluation Frameworks, and Decision Guidance"
authors: ['Hadi Mohammadi', 'Tina Shahedi']
year: 2026
venue: "Preprints.org"
tags: ['Explainable Artificial Intelligence (XAI)', 'Topic Modeling', 'Text Readability and Simplification']
source: raw/applied/applied_2026_Explainable_NLP_in_the_Er_preprints202610_0435_v1.md
---

# Explainable NLP in the Era of Large Language Models: A Unified Taxonomy, Evaluation Frameworks, and Decision Guidance

**저자**: Hadi Mohammadi; Tina Shahedi
**출처**: Preprints.org, Vol.None
**발행일**: 2026-10-07
**DOI**: https://doi.org/10.20944/preprints202610.0435.v1

## 초록 (원문)

Explanation methods for natural language processing (NLP) come from two literatures that rarely meet: feature attribution and probing for task models, and the interpretability of large language models (LLMs), from chain-of-thought reasoning to sparse autoencoder features and circuit tracing. We place both in a unified taxonomy with four dimensions: scope (local vs. global), mechanism (how the explanation is computed), model access (model-agnostic vs. model-specific), and output form (importance scores, rules, examples, counterfactuals, rationale spans, concepts, natural language). Faithfulness and plausibility come apart, and the erasure tests built for extracted rationales do not apply to a chain of thought, which is an output rather than part of the input, so chains of thought need intervention tests of their own. The access a deployment allows settles which mechanisms are usable before scope or audience matter; our practical decision frameworks start from that question and are traced through three worked deployments. In our synthesis of LLM-era interpretability, a lineage table shows that most current techniques rebuild or extend older ideas under new constraints of scale and access, while two problems are new: keeping reasoning traces monitorable under training pressure, and testing whether models can introspect. Faithfulness metrics disagree with one another, and sparse autoencoders do not yet beat simple baselines on standardized benchmarks, so evaluations should name the tests they ran instead of reporting one score. We also survey applications across healthcare, legal and financial services, social science research, content moderation, and education, and close with six open problems.

## 키워드

explainable natural language processing, explainability, large language models, health care, customer relationship management, systematic reviews, conversational AI, interpretability

## 위키 연관

- [[pages/methods/mixed_methods|복합 방법론]]

## 메모

