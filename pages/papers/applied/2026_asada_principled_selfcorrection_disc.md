---
title: "Principled Self-Correction in Discrete Diffusion: A UCB-Guided Framework for Text Generation"
authors: ['Masaki Asada', 'Makoto Miwa']
year: 2026
venue: ""
tags: ['Natural Language Processing Techniques', 'Topic Modeling', 'Digital Humanities and Scholarship']
source: raw/applied/applied_2026_Principled_SelfCorrection_2026_eacl_long_314.md
---

# Principled Self-Correction in Discrete Diffusion: A UCB-Guided Framework for Text Generation
**제목(한글)**: 이산 확산 모델에서의 원칙적인 자가 정정: 텍스트 생성을 위한 UCB 가이드 프레임워크

**저자**: Masaki Asada; Makoto Miwa
**출처**: , Vol.None, pp.6678-6692
**발행일**: 2026-01-01
**DOI**: https://doi.org/10.18653/v1/2026.eacl-long.314

## 한국어 요약

**연구질문**: 이산 확산(Discrete Diffusion) 기반 텍스트 생성 모델에서 훈련 시 정답 데이터 노이즈와 추론 시 자가 생성 데이터 노이즈 간의 불일치를 해소하고 생성 신뢰도를 높이는 방법은 무엇인가?

**방법론**:
- 다단계 훈련 과정에서 중간 출력물을 스스로 디노이징하게 학습시키는 DSP(Deeper Self-Prediction) 학습 설계
- 토큰 재마스킹 결정을 멀티암드 밴딧 문제로 수립하여 UCB 지표에 따라 탐색과 탐리를 조율하는 UCB 가이드 디코딩 알고리즘 구현

**주요 결과**:
- 제안 프레임워크가 자동 평가 및 LLM-as-a-Judge 지표 모두에서 기존 확산 생성 모델 대비 생성 텍스트의 Faithful(충실성)과 Coherence(일관성)를 크게 향상시킴을 실증


## 초록 (원문)

Inspired by their success in image synthesis, diffusion models offer a flexible, iterative alternative to rigid left-to-right text generation.However, a fundamental training-inference discrepancy hinders their performance: models are trained on corrupted ground-truth tokens, but at inference time they must denoise inputs corrupted from their own predictions.To bridge this gap, we propose a unified framework.First, Deeper Self-Prediction (DSP) is a multi-step training objective that teaches robust self-correction by forcing the model to denoise its own intermediate outputs.Second, UCB-guided Decoding is a principled inference algorithm that frames token re-masking as a multi-armed bandit problem, using the Upper Confidence Bound (UCB) to balance exploration and exploitation.Experiments on text generation tasks demonstrate consistent improvements over existing diffusion baselines.The framework achieves higher faithfulness and coherence according to both automatic metrics and LLM-as-a-Judge evaluations.

## 키워드

Feature (linguistics), Identification (biology), Context (archaeology), Sequence (biology)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

