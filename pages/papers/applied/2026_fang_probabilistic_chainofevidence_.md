---
title: "Probabilistic Chain-of-Evidence: Enhancing Factual Accuracy and Uncertainty Reasoning in Large Language Models via Prompt Engineering"
authors: ['Jiing Fang', 'Wei "Wayne\\', ' Chen']
year: 2026
venue: "Preprints.org"
tags: ['Topic Modeling', 'Artificial Intelligence in Healthcare and Education', 'Multimodal Machine Learning Applications']
source: raw/applied/applied_2026_Probabilistic_ChainofEvid_preprints202601_1471_v1.md
---

# Probabilistic Chain-of-Evidence: Enhancing Factual Accuracy and Uncertainty Reasoning in Large Language Models via Prompt Engineering
**제목(한글)**: 확률적 증거 사슬: 프롬프트 엔지니어링을 통한 대형 언어 모델의 사실적 정확성 및 불확실성 추론 향상

**저자**: Jiing Fang; Wei "Wayne\;  Chen
**출처**: Preprints.org, Vol.None
**발행일**: 2026-01-20
**DOI**: https://doi.org/10.20944/preprints202601.1471.v1

## 한국어 요약

**연구질문**: 파라미터 튜닝 없이 정교한 프롬프트 엔지니어링 설계만으로, LLM이 추론 과정에서 사실 정보와 단순 가정/불확실한 정보를 명확히 구별하여 환각(Hallucination) 현상을 차단할 수 있는가?

**방법론**:
- 메타인지 추론 파이프라인(증거 식별 -> 확률 평가 -> 가중 추론)으로 LLM을 안내하는 PCE(Probabilistic Chain-of-Evidence) 프롬프트 구조 설계
- 모호성이 높은 사실 질문(QA), 의료 영상 판독문 해석, 법률 조항 코딩 분석 등 오답 위험이 높은 복잡한 환경에 대한 성능 비교 실험 진행

**주요 결과**:
- 제안된 PCE 기법은 기존 Chain-of-Thought(CoT) 프롬프트 대비 사실 한계선 인지 정확도와 답변의 정밀성을 획기적으로 개선하며, 오답 및 환각 발생 빈도를 유의미하게 경감시킴
- 불확실성이 내재한 정보 환경에서도 가장 보수적인 최저선 확률을 누적 전파하는 추론 가이드가 모델의 정서적 일관성과 신뢰도를 동시에 확보함을 실증함


## 초록 (원문)

Large Language Models (LLMs) frequently struggle with factual accuracy and the precise handling of uncertain information, often leading to hallucinations or misinterpretations. Existing methods like Chain-of-Thought (CoT) prompting fail to explicitly distinguish between facts and assumptions within complex contexts. To address these challenges, we introduce the Probabilistic Chain-of-Evidence (PCE) method, a novel prompt engineering strategy designed to enhance LLMs' Factual Boundary Recognition and Uncertainty Reasoning Accuracy. PCE guides LLMs through a meta-cognitive process comprising Evidence Identification, Probabilistic Assessment, and Weighted Inference, enabling explicit quantification and integration of evidence certainty throughout reasoning. Implemented purely through sophisticated prompt design without model modifications, PCE was rigorously evaluated across diverse tasks including Factual Question Answering with Ambiguity, Medical Report Interpretation, and Legal Text Analysis. Our experiments demonstrate that PCE consistently and significantly outperforms traditional CoT prompting, achieving substantial improvements in Factual Boundary Recognition Accuracy and Uncertainty Expression Precision, while drastically reducing the Hallucination Rate. Human evaluations further corroborate these findings, indicating superior Overall Answer Quality. An ablation study confirms the crucial contribution of each PCE stage, and an analysis highlights the efficacy of a conservative "minimum" approach for robust uncertainty propagation. PCE offers a highly adaptable and practical solution for generating more reliable, transparent, and trustworthy responses from LLMs in complex, ambiguous information environments.

## 키워드

Probabilistic logic, Certainty, Process (computing), Trustworthiness, Uncertainty quantification, Boundary (topology)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

