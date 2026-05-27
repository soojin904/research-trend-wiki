---
title: "Integrating Attention Attribution and Pretrained Language Models for Transparent Discriminative Learning"
authors: ['Xiangchen Song']
year: 2026
venue: "Preprints.org"
tags: ['Explainable Artificial Intelligence (XAI)', 'Multimodal Machine Learning Applications', 'Topic Modeling']
source: raw/applied/applied_2026_Integrating_Attention_Att_preprints202602_0344_v1.md
---

# Integrating Attention Attribution and Pretrained Language Models for Transparent Discriminative Learning
**제목(한글)**: 투명한 판별 학습을 위한 어텐션 귀속(Attribution)과 사전 학습된 언어 모델의 통합

**저자**: Xiangchen Song
**출처**: Preprints.org, Vol.None
**발행일**: 2026-02-05
**DOI**: https://doi.org/10.20944/preprints202602.0344.v1

## 한국어 요약

**연구질문**: 텍스트 분류 및 판별 모델의 의사결정 블랙박스 문제를 해결하고, 모델 예측 시 어떤 단어나 단락 특징에 의존했는지 설명 가능한 투명성을 어떻게 부여할 수 있는가?

**방법론**:
- 다두 어텐션(Multi-head attention) 메커니즘을 사용해 문맥 특징을 추출하는 사전학습 기반 판별 모델 설계
- 모델 예측 시 각 토큰의 기여도를 정량 연산하는 어텐션 귀속(Attribution) 알고리즘 도입
- 학습률, 문장 순서 교란, 드롭아웃 및 클래스 불균형 등 다양한 민감도 통제 실험을 통해 일반화 성능과 강건성 검증

**주요 결과**:
- 높은 판별 성능(정밀도, F1 점수 등)을 유지하면서도 어텐션 가중치 분포를 통해 의사결정에 직관적인 해석 경로를 시각 제시하는 데 성공
- 다양한 환경 변화 속에서도 일관되고 예측 가능한 해석 신뢰성을 증명하여 투명한 의사결정이 요구되는 중요 분야에 하이브리드 분류 솔루션을 제시함


## 초록 (원문)

This paper addresses the problem of insufficient interpretability in discriminative learning and proposes an interpretable discriminative learning method based on attention attribution. The study builds on the representation power of pretrained language models and introduces a multi-head attention mechanism to capture both global and local semantic dependencies, thereby obtaining richer feature representations. On this basis, attention attribution is used to calculate the importance scores of input features during prediction, and the attribution distribution reveals the core semantic cues relied upon by the model in discrimination, which enhances the transparency of the decision process. The framework consists of input embedding, contextual modeling, attribution feature extraction, and a classification layer, enabling the model to provide clear explanatory paths while maintaining high discriminative accuracy. The method is systematically validated under multiple single-factor sensitivity settings, including the effects of learning rate, sentence order disruption, dropout rate, and class imbalance on model performance and robustness. Experimental results show that the method achieves stability and superiority in metrics such as accuracy, precision, recall, and F1-score, maintaining strong discriminative ability and consistent interpretability under different conditions. Overall, by integrating attention mechanisms with attribution methods, this paper achieves a balance between performance and interpretability and provides an effective solution for discriminative learning in complex contexts.

## 키워드

Interpretability, Discriminative model, Feature learning, Sentence, Representation (politics), Feature (linguistics), Attribution, Stability (learning theory)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

