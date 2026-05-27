---
title: "Human Values in a Single Sentence: Moral Presence, Hierarchies, and Transformer Ensembles on the Schwartz Continuum"
authors: ['Víctor Yeste', 'Paolo Rosso']
year: 2026
venue: "arXiv (Cornell University)"
tags: ['Hate Speech and Cyberbullying Detection', 'Sentiment Analysis and Opinion Mining', 'Misinformation and Its Impacts']
source: raw/applied/applied_2026_Human_Values_in_a_Single_nodoi.md
---

# Human Values in a Single Sentence: Moral Presence, Hierarchies, and Transformer Ensembles on the Schwartz Continuum
**제목(한글)**: 단일 문장의 인간 가치관: 슈바르츠 연속체(Schwartz Continuum)에서의 도덕적 존재, 위계, 트랜스포머 앙상블

## 한국어 요약

**연구질문**: 뉴스 및 정치 선언문의 단일 문장 수준에서 슈바르츠 가치 체계의 19가지 인간 가치관을 자동으로 탐지할 수 있는 효율적인 NLP 모델을 어떻게 설계할 수 있는가?

**방법론**:
- 뉴스·정치 선언문 약 7만 4천 개 영어 문장(ValueEval'24 코퍼스)으로 도덕적 가치 존재 여부 및 19개 가치 다중 레이블 분류 수행
- 소비자 수준 GPU(8GB VRAM) 예산 내에서 DeBERTa 기반 분류기, 존재 게이트 계층 구조, 경량 보조 신호(LIWC-22, 도덕 어휘집) 및 소프트 보팅 앙상블 비교 평가
- 7~9B 규모 지시 튜닝 LLM(Gemma 2, Llama 3.1, Mistral, Qwen 2.5)의 제로샷·퓨샷 및 QLoRA 설정 벤치마크

**주요 결과**:
- DeBERTa 기반 소프트 보팅 앙상블이 19개 가치 분류에서 매크로 F1 0.332를 달성하여 ValueEval'24 최고 영어 기준선(0.28) 대비 성능 향상
- 동일 컴퓨팅 예산에서 지도학습 앙상블이 대규모 LLM 제로샷/퓨샷 설정을 능가함을 실증

**저자**: Víctor Yeste; Paolo Rosso
**출처**: arXiv (Cornell University), Vol.None
**발행일**: 2026-01-20
**DOI**: 

## 초록 (원문)

We study sentence-level detection of the 19 human values in the refined Schwartz continuum in about 74k English sentences from news and political manifestos (ValueEval'24 corpus). Each sentence is annotated with value presence, yielding a binary moral-presence label and a 19-way multi-label task under severe class imbalance. First, we show that moral presence is learnable from single sentences: a DeBERTa-base classifier attains positive-class F1 = 0.74 with calibrated thresholds. Second, we compare direct multi-label value detectors with presence-gated hierarchies in a setting where only a single consumer-grade GPU with 8 GB of VRAM is available, and we explicitly choose all training and inference configurations to fit within this budget. Presence gating does not improve over direct prediction, indicating that gate recall becomes a bottleneck. Third, we investigate lightweight auxiliary signals - short-range context, LIWC-22, and moral lexica - and small ensembles. Our best supervised configuration, a soft-voting ensemble of DeBERTa-based models enriched with such signals, reaches macro-F1 = 0.332 on the 19 values, improving over the best previous English-only baseline on this corpus, namely the best official ValueEval'24 English run (macro-F1 = 0.28 on the same 19-value test set). Methodologically, our study provides, to our knowledge, the first systematic comparison of direct versus presence-gated architectures, lightweight feature-augmented encoders, and medium-sized instruction-tuned Large Language Models (LLMs) for refined Schwartz values at sentence level. We additionally benchmark 7-9B instruction-tuned LLMs (Gemma 2 9B, Llama 3.1 8B, Mistral 8B, Qwen 2.5 7B) in zero-/few-shot and QLoRA setups, and find that they lag behind the supervised ensemble under the same compute budget. Overall, our results provide empirical guidance for building compute-efficient, value-aware NLP models.

## 키워드

Sentence, Classifier (UML), Inference, Binary number, Transformer, Binary classification, Language model, Recall

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

