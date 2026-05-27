---
title: "Countering Catastrophic Forgetting of Large Language Models for Better Instruction Following via Weight-Space Model Merging"
authors: ['Mengxian Lyu', 'Cheng Peng', 'Ziyi Chen', 'Mengyuan Zhang', 'Jieting Li Lu', 'Yonghui Wu']
year: 2026
venue: "ArXiv.org"
tags: ['Machine Learning in Healthcare', 'Artificial Intelligence in Healthcare and Education', 'Topic Modeling']
source: raw/applied/applied_2026_Countering_Catastrophic_F_nodoi.md
---

# Countering Catastrophic Forgetting of Large Language Models for Better Instruction Following via Weight-Space Model Merging
**제목(한글)**: 가중치 공간 모델 병합을 통한 대형 언어 모델의 명령 수행 능력 향상을 위한 치명적 망각 대처

**저자**: Mengxian Lyu; Cheng Peng; Ziyi Chen; Mengyuan Zhang; Jieting Li Lu; Yonghui Wu
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-04-02
**DOI**: 

## 한국어 요약

**연구질문**: 의료 도메인 특화 데이터셋으로 미세 조정(fine-tuning)할 때 LLM이 명령 수행 능력을 심각하게 상실하는 치명적 망각(catastrophic forgetting) 문제를 가중치 병합(model merging)으로 어떻게 극복할 수 있는가?

**방법론**:
- 임상 기반 모델(GatorTronLlama)과 일반 명령 모델(Llama-3.1-8B-Instruct)을 보간 기반 병합 기법으로 결합
- 의료 벤치마크 및 5가지 임상 생성 태스크(영상의학 요약, 퇴원 요약 등)에서 종합 평가

**주요 결과**:
- 병합 모델이 치명적 망각을 효과적으로 완화하면서 임상 도메인 전문성과 명령 수행 능력을 동시에 유지함
- 64회 학습으로도 256회 전체 미세 조정 기준선과 유사한 성능 달성으로 자원 제약 환경에서의 확장성을 입증

## 초록 (원문)

Large language models have been adopted in the medical domain for clinical documentation to reduce clinician burden. However, studies have reported that LLMs often "forget" a significant amount of instruction-following ability when fine-tuned using a task-specific medical dataset, a critical challenge in adopting general-purpose LLMs for clinical applications. This study presents a model merging framework to efficiently adapt general-purpose LLMs to the medical domain by countering this forgetting issue. By merging a clinical foundation model (GatorTronLlama) with a general instruct model (Llama-3.1-8B-Instruct) via interpolation-based merge methods, we seek to derive a domain-adapted model with strong performance on clinical tasks while retaining instruction-following ability. Comprehensive evaluation across medical benchmarks and five clinical generation tasks (e.g., radiology and discharge summarization) shows that merged models can effectively mitigate catastrophic forgetting, preserve clinical domain expertise, and retain instruction-following ability. In addition, our model merging strategies demonstrate training efficiency, achieving performance on par with fully fine-tuned baselines under severely constrained supervision (e.g., 64-shot vs. 256-shot). Consequently, weight-space merging constitutes a highly scalable solution for adapting open-source LLMs to clinical applications, facilitating broader deployment in resource-constrained healthcare environments.

## 키워드

Forgetting, Software deployment, Merge (version control), Documentation, Scalability, Domain (mathematical analysis), Health care

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

