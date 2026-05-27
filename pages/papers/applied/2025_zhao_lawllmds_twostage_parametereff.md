---
title: "LawLLM-DS: A Two-Stage Parameter-Efficient Fine-Tuning Framework for Legal Judgment Prediction with Symmetry-Aware Label Graphs"
authors: ['Pengcheng Zhao', 'Chengcheng Han', 'Kun Han']
year: 2025
venue: "Preprints.org"
tags: ['Artificial Intelligence in Law', 'Topic Modeling', 'Explainable Artificial Intelligence (XAI)']
source: raw/applied/applied_2025_LawLLMDS_A_TwoStage_Param_preprints202512_1406_v1.md
---

# LawLLM-DS: A Two-Stage Parameter-Efficient Fine-Tuning Framework for Legal Judgment Prediction with Symmetry-Aware Label Graphs

**제목(한글)**: LawLLM-DS: 대칭 인식 레이블 그래프를 활용한 법률 판결 예측을 위한 2단계 파라미터 효율적 미세조정 프레임워크

## 한국어 요약

**연구질문**: 대형 언어 모델의 전체 미세조정이 메모리 집약적이고 파국적 망각에 취약한 문제를 해결하면서, 법률 판결 예측(Legal Judgment Prediction)에서 높은 성능을 유지하는 파라미터 효율적 방법은 무엇인가?

**방법론**:
- 공격적 학습률로 법률 지식 사전 조정 후 보수적 업데이트로 판결 관계를 정제하는 2단계 LoRA(Low-Rank Adaptation) 프레임워크 개발
- 전용 LoRA 어댑터, 4비트 양자화, 7개 트랜스포머 투영 행렬 수정으로 훈련 파라미터를 0.21%만 유지
- 5,096개 수작업 주석 이혼 사건 데이터셋에서 평가

**주요 결과**:
- LawLLM-DS가 매크로 F1 0.8893, 정확도 0.8786을 달성하여 단일 단계 LoRA 및 BERT 기준선을 능가
- 단계별 학습률·어댑터 배치·저랭크 설정의 기여를 제거 연구로 검증하며, 경량 구조 인식 법률 판결 지원 시스템으로서의 실용성을 입증

**저자**: Pengcheng Zhao; Chengcheng Han; Kun Han
**출처**: Preprints.org, Vol.None
**발행일**: 2025-12-17
**DOI**: https://doi.org/10.20944/preprints202512.1406.v1

## 초록 (원문)

Legal judgment prediction (LJP) increasingly relies on large language models whose full fine-tuning is memory-intensive and susceptible to catastrophic forgetting. We present LawLLM-DS, a two-stage Low-Rank Adaptation (LoRA) framework that first performs legal knowledge pre-tuning with an aggressive learning rate and subsequently refines judgment relations with conservative updates, using dedicated LoRA adapters, 4-bit quantization, and targeted modification of seven Transformer projection matrices to keep only 0.21% of parameters trainable. From a structural perspective, the twenty annotated legal elements form a symmetric label co-occurrence graph that exhibits both cluster-level regularities and asymmetric sparsity patterns, and LawLLM-DS implicitly captures these graph-informed dependencies while remaining compatible with downstream GNN-based representations. Experiments on 5,096 manually annotated divorce cases show that LawLLM-DS lifts macro F1 to 0.8893 and achieves an accuracy of 0.8786, outperforming single-stage LoRA and BERT baselines under the same data regime. Ablation studies further verify the contributions of stage-wise learning rates, adapter placement, and low-rank settings. These findings demonstrate that curriculum-style, parameter-efficient adaptation provides a practical path toward lightweight yet structure-aware LJP systems for judicial decision support.

## 키워드

Transformer, Graph, Knowledge graph, Structured prediction, Path (computing), Domain adaptation, Training set

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

