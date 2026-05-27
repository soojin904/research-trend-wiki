---
title: "EnvScaler: Scaling Tool-Interactive Environments for LLM Agent via Programmatic Synthesis"
authors: ['Xiaoshuai Song', 'Haofei Chang', 'Guanting Dong', 'Yutao Zhu', 'Zhicheng Dou', 'Ji-Rong Wen']
year: 2026
venue: "ArXiv.org"
tags: ['Topic Modeling', 'Multimodal Machine Learning Applications', 'Artificial Intelligence in Healthcare and Education']
source: raw/applied/applied_2026_EnvScaler_Scaling_ToolInt_nodoi.md
---

# EnvScaler: Scaling Tool-Interactive Environments for LLM Agent via Programmatic Synthesis
**제목(한글)**: EnvScaler: 프로그래밍 방식 합성을 통한 LLM 에이전트의 도구 상호작용 환경 확장

## 한국어 요약

**연구질문**: 실제 시스템 접근 제한, LLM 시뮬레이션의 환각 문제, 수동 구축의 확장성 한계를 극복하여 LLM 에이전트 학습에 필요한 다양하고 풍부한 도구 상호작용 샌드박스 환경을 자동으로 생성하는 방법은 무엇인가?

**방법론**:
- 토픽 마이닝, 논리 모델링, 품질 평가를 통해 다양한 환경 골격(Skeleton)을 구성하는 SkelBuilder와 각 환경에 대해 다중 태스크 시나리오 및 규칙 기반 궤적 검증 함수를 생성하는 ScenGenerator로 구성된 EnvScaler 프레임워크 제안
- 191개 환경과 약 7,000개 시나리오를 합성하여 Qwen3 시리즈 모델의 지도 미세 조정(SFT) 및 강화 학습(RL)에 적용

**주요 결과**:
- 세 가지 벤치마크에서 EnvScaler가 LLM의 다중 턴, 다중 도구 상호작용이 포함된 복잡한 환경의 태스크 해결 능력을 대폭 향상시킴을 확인
- 프로그래밍 방식 합성 접근법이 수동 구축 없이도 고품질의 다양한 도구 상호작용 환경을 효율적으로 확장할 수 있음을 입증

**저자**: Xiaoshuai Song; Haofei Chang; Guanting Dong; Yutao Zhu; Zhicheng Dou; Ji-Rong Wen
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-01-09
**DOI**: 

## 초록 (원문)

Large language models (LLMs) are expected to be trained to act as agents in various real-world environments, but this process relies on rich and varied tool-interaction sandboxes. However, access to real systems is often restricted; LLM-simulated environments are prone to hallucinations and inconsistencies; and manually built sandboxes are hard to scale. In this paper, we propose EnvScaler, an automated framework for scalable tool-interaction environments via programmatic synthesis. EnvScaler comprises two components. First, SkelBuilder constructs diverse environment skeletons through topic mining, logic modeling, and quality evaluation. Then, ScenGenerator generates multiple task scenarios and rule-based trajectory validation functions for each environment. With EnvScaler, we synthesize 191 environments and about 7K scenarios, and apply them to Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) for Qwen3 series models. Results on three benchmarks show that EnvScaler significantly improves LLMs' ability to solve tasks in complex environments involving multi-turn, multi-tool interactions. We release our code and data at https://github.com/RUC-NLPIR/EnvScaler.

## 키워드

Scalability, Task (project management), Process (computing), Reinforcement learning, Code (set theory), Trajectory, Scale (ratio), Quality (philosophy)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

