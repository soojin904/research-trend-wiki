---
title: "Adversarial Robustness in Text Classification through Semantic Calibration with Large Language Models"
authors: ['Chihui Shao', 'Yun Zi', 'Yi Deng', 'Heyao Liu', 'Chong Zhang', 'Yinan Ni']
year: 2026
venue: "Preprints.org"
tags: ['Misinformation and Its Impacts', 'Topic Modeling', 'Hate Speech and Cyberbullying Detection']
source: raw/applied/applied_2026_Adversarial_Robustness_in_preprints202602_0617_v1.md
---

# Adversarial Robustness in Text Classification through Semantic Calibration with Large Language Models
**제목(한글)**: 거대 언어 모델 교정을 통한 의미론적 정렬 기반 텍스트 분류의 적대적 강건성

**저자**: Chihui Shao; Yun Zi; Yi Deng; Heyao Liu; Chong Zhang; Yinan Ni
**출처**: Preprints.org, Vol.None
**발행일**: 2026-02-09
**DOI**: https://doi.org/10.20944/preprints202602.0617.v1

## 한국어 요약

**연구질문**: 악의적인 텍스트 변조 및 적대적 공격(Adversarial Perturbations) 상황에서도 텍스트 분류기가 신뢰성을 유지하도록 모델의 출력 확신도(Confidence)와 의미 표상을 안정화할 수 있는가?

**방법론**:
- 다단계 의미론적 표상 및 확신도 조절 기능을 갖춘 견고한 텍스트 분류 프레임워크 제안
- 사전 학습된 인코더의 특징 추출 위에 로컬 섭동에 덜 민감하도록 돕는 온도 보정(Temperature calibration) 기법 결합
- 원본 텍스트와 노이즈가 주입된 텍스트 간 의미 정렬 상태를 유지하도록 제약조건 loss 함수 설계 및 학습 수행

**주요 결과**:
- 섭동을 가한 단어 교체, 노이즈 주입 및 불균형 클래스 환경의 세밀한 벤치마크 테스트에서도 성능 저하를 방어하며 분류 강건성을 보장
- 기존의 주요 베이스라인 분류기들과 비교했을 때, 적대적 공격에 대응하는 분류 정확도를 큰 폭으로 개선함을 실증함


## 초록 (원문)

This paper addresses the problem of text classification models being vulnerable and lacking robustness under adversarial perturbations by proposing a robust text classification method based on large language model calibration. The method builds on a pretrained language model and constructs a multi-stage framework for semantic representation and confidence regulation. It achieves stable optimization of classification results through semantic embedding extraction, calibration adjustment, and consistency constraints. First, the model uses a pretrained encoder to generate context-aware semantic features and applies an attention aggregation mechanism to obtain global semantic representations. Second, a temperature calibration mechanism is introduced to smooth the output probability distribution, reducing the model's sensitivity to local perturbations. Third, adversarial consistency constraints are applied to maintain feature alignment between original and perturbed samples in semantic space, ensuring dynamic preservation of semantic robustness. The method adopts a joint loss function to balance three optimization objectives: classification accuracy, robustness, and confidence. To verify its effectiveness, sensitivity experiments on hyperparameters, environments, and data distributions are conducted. The results show that the model maintains high performance and stability under conditions such as word substitution, noise injection, and class imbalance, significantly outperforming several mainstream baseline models. This study achieves the integration of semantic-level robustness optimization and calibration learning, providing a new approach for building highly reliable text classification systems.

## 키워드

Robustness (evolution), Encoder, Inference, Language model, Discriminative model, Adversarial system, Pattern recognition (psychology), Sensitivity (control systems)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]
- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모

