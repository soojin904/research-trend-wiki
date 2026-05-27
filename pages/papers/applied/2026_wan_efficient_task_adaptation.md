---
title: "Efficient Task Adaptation in Large Language Models via Selective Parameter Optimization"
authors: ['Weijie Wan', 'Jiangjiang Zhao']
year: 2026
venue: "ArXiv.org"
tags: ['Topic Modeling', 'Machine Learning in Healthcare', 'Domain Adaptation and Few-Shot Learning']
source: raw/applied/applied_2026_Efficient_Task_Adaptation_nodoi.md
---

# Efficient Task Adaptation in Large Language Models via Selective Parameter Optimization
**제목(한글)**: 선택적 파라미터 최적화를 통한 대규모 언어 모델의 효율적 태스크 적응

## 한국어 요약

**연구질문**: 사전 학습된 LLM을 특정 도메인 태스크에 파인튜닝할 때 발생하는 치명적 망각(catastrophic forgetting) 문제를 파라미터 중요도 구분을 통해 어떻게 완화할 수 있는가?

**방법론**:
- 파라미터를 범용 언어 능력에 핵심적인 "코어 파라미터"와 특정 태스크에 민감한 "비코어 파라미터"로 구분하는 중요도 평가 방법 제안
- 파인튜닝 시 코어 파라미터는 고정하고 비코어 파라미터만 갱신하는 선택적 최적화 전략 적용
- GPT-J 및 LLaMA-3 모델로 과학, 의료, 물리학 도메인 태스크에서 검증

**주요 결과**:
- 제안 방법이 치명적 망각을 완화하면서 도메인 특화 태스크 적응력을 동시에 향상시킴을 실험적으로 입증
- 전체 파라미터 공간을 훈련하는 전통적 파인튜닝 대비 범용성과 전이 가능성 보존 효과 확인

**저자**: Weijie Wan; Jiangjiang Zhao
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-04-18
**DOI**: 

## 초록 (원문)

Large Language Models (LLMs) have demonstrated excellent performance in general language understanding, generation and other tasks. However, when fine-tuning for specific domain tasks, the general knowledge accumulated in the pre-training phase is often partially overwritten or forgotten due to parameter updates, which severely limits the generalization ability and transferability of LLMs. Traditional fine-tuning strategies mostly train on the entire parameter space, ignoring the heterogeneity of model parameters, that is, some parameters are extremely important for general tasks, while other parameters are more sensitive to specific tasks. To alleviate the above problems, this paper innovatively proposes a parameter element importance evaluation method, which divides parameters into "core parameters" and "non-core parameters" by distinguishing the importance of parameters for general language ability tasks and specific domain tasks, and fixes the core parameters during fine-tuning, and only fine-tunes the non-core parameters. Extensive experiments on scientific, medical and physical tasks using GPT-J and LLaMA-3 show that our method can mitigate catastrophic forgetting while enhancing the adaptability of the model.

## 키워드

Domain adaptation, Forgetting, Adaptability, Generalization, Task (project management), Language model, Adaptation (eye), Domain (mathematical analysis)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

