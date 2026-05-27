---
title: "LawLLM-DS: A Two-Stage LoRA Framework for Multi-Label Legal Judgment Prediction with Structured Label Dependencies"
authors: ['Pengcheng Zhao', 'Chengcheng Han', 'Kun Han']
year: 2026
venue: "Symmetry"
tags: ['Artificial Intelligence in Law', 'Topic Modeling', 'Explainable Artificial Intelligence (XAI)']
source: raw/applied/applied_2026_LawLLMDS_A_TwoStage_LoRA__sym18010150.md
---

# LawLLM-DS: A Two-Stage LoRA Framework for Multi-Label Legal Judgment Prediction with Structured Label Dependencies
**제목(한글)**: LawLLM-DS: 구조화된 라벨 의존성을 고려한 다중 라벨 사법 판결 예측용 2단계 LoRA 프레임워크

**저자**: Pengcheng Zhao; Chengcheng Han; Kun Han
**출처**: Symmetry, Vol.18, pp.150-150
**발행일**: 2026-01-13
**DOI**: https://doi.org/10.3390/sym18010150

## 한국어 요약

**연구질문**: 법률 판결 예측(LJP) 시 발생하는 거대 언어 모델의 대규모 메모리 점유 및 파괴적 망각을 피하면서 법률 조항 간의 결합성 및 공존성(co-occurrence)을 가볍게 학습할 수 있는가?

**방법론**:
- 1단계로 높은 학습률로 일반 법률 지식을 프리튜닝하고, 2단계로 보수적 학습률로 실제 판결 판례 관계를 미세조정하는 LawLLM-DS 프레임워크 제안
- 4비트 양자화 기법 및 Transformer 7개 투영 행렬 조정을 통해 단 0.21%의 매개변수만 학습
- 20개 사법 요소들 간의 공존 관계를 대칭 그래프 형태로 코딩하고 GNN 모델과 호환 설계

**주요 결과**:
- 5,096건의 이혼 관련 사법 판례 데이터셋 실험에서 단일 단계 LoRA 및 BERT 분류기 대비 월등한 매크로 F1 = 0.8893 및 정확도 0.8786을 달성
- 단계별 학습률 차별화 및 저차원 아답터(LoRA) 배치가 매개변수 고효율 사법 판결 시스템 구축의 효과적인 대안임을 입증


## 초록 (원문)

Legal judgment prediction (LJP) increasingly relies on large language models whose full fine-tuning is memory-intensive and susceptible to catastrophic forgetting. We present LawLLM-DS, a two-stage Low-Rank Adaptation (LoRA) framework that first performs legal knowledge pre-tuning with an aggressive learning rate and subsequently refines judgment relations with conservative updates, using dedicated LoRA adapters, 4-bit quantization, and targeted modification of seven Transformer projection matrices to keep only 0.21% of parameters trainable. From a structural perspective, the twenty annotated legal elements form a symmetric label co-occurrence graph that exhibits both cluster-level regularities and asymmetric sparsity patterns, and LawLLM-DS implicitly captures these graph-informed dependencies while remaining compatible with downstream GNN-based representations. Experiments on 5096 manually annotated divorce cases show that LawLLM-DS lifts macro F1 to 0.8893 and achieves an accuracy of 0.8786, outperforming single-stage LoRA and BERT baselines under the same data regime. Ablation studies further verify the contributions of stage-wise learning rates, adapter placement, and low-rank settings. These findings demonstrate that curriculum-style, parameter-efficient adaptation provides a practical path toward lightweight yet structure-aware LJP systems for judicial decision support.

## 키워드

Structured prediction, Transformer, Graph, Adapter (computing), Collision, Adaptation (eye), Projection (relational algebra)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

