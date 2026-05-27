---
title: "PaSE: Prototype-aligned Calibration and Shapley-based Equilibrium for Multimodal Sentiment Analysis"
authors: ['Kang He', 'BoYu Chen', 'Yuzhe Ding', 'Fei Li', 'Chong Teng', 'Donghong Ji']
year: 2026
venue: "Proceedings of the AAAI Conference on Artificial Intelligence"
tags: ['Emotion and Mood Recognition', 'Sentiment Analysis and Opinion Mining', 'Face recognition and analysis']
source: raw/applied/applied_2026_PaSE_Prototypealigned_Cal_aaai_v40i37_40355.md
---

# PaSE: Prototype-aligned Calibration and Shapley-based Equilibrium for Multimodal Sentiment Analysis
**제목(한글)**: PaSE: 멀티모달 감성 분석을 위한 프로토타입 정렬 보정 및 섀플리 기반 균형 프레임워크

**저자**: Kang He; BoYu Chen; Yuzhe Ding; Fei Li; Chong Teng; Donghong Ji
**출처**: Proceedings of the AAAI Conference on Artificial Intelligence, Vol.40, pp.30960-30968
**발행일**: 2026-03-14
**DOI**: https://doi.org/10.1609/aaai.v40i37.40355

## 한국어 요약

**연구질문**: 멀티모달 감성 분석(MSA) 시, 정보량이 풍부한 특정 모달리티가 다른 약한 모달리티의 기여를 잠식하는 '모달리티 경쟁(Modality competition)' 오류를 해결하고 다중 신호(텍스트, 오디오, 비디오)의 상호보완적 융합을 안정화하는 방안은 무엇인가?

**방법론**:
- 각 단일 모달리티 특징을 정제하기 위해 엔트로피 최적 전송(Optimal Transport) 기반의 프로토타입 가이드 보정 학습(PCL) 기법 적용
- 모달리티별 실제 기여도에 따라 최적화 기울기 방향을 동적으로 조율하는 섀플리 기반 기울기 변조(Shapley-based Gradient Modulation, SGM) 결합
- IEMOCAP, MOSI, MOSEI 데이터셋을 사용하여 모델 학습 성능 평가

**주요 결과**:
- PaSE 프레임워크는 특정 모달리티의 지배 현상을 해소하고 균형 잡힌 다중 모달 결합을 달성하여 세 벤치마크 평가에서 최첨단 성과를 거둠


## 초록 (원문)

Multimodal Sentiment Analysis (MSA) seeks to understand human emotions by integrating textual, acoustic, and visual signals. Although multimodal fusion is designed to leverage cross-modal complementarity, real-world scenarios often exhibit modality competition: dominant modalities tend to overshadow weaker ones, leading to suboptimal performance. In this paper, we propose PaSE, a novel Prototype-aligned Calibration and Shapley-optimized Equilibrium framework, which enhances collaboration while explicitly mitigating modality competition. PaSE first applies Prototype-guided Calibration Learning (PCL) to refine unimodal representations and align them through an Entropic Optimal Transport mechanism that ensures semantic consistency. To further stabilize optimization, we introduce a Dual-Phase Optimization strategy. A prototype-gated fusion module is first used to extract shared representations, followed by Shapley-based Gradient Modulation (SGM), which adaptively adjusts gradients according to the contribution of each modality. Extensive experiments on IEMOCAP, MOSI, and MOSEI confirm that PaSE achieves the superior performance and effectively alleviates modality competition.

## 키워드

Leverage (statistics), Modality (human–computer interaction), Fusion, Calibration, Modalities, Sentiment analysis, Mechanism (biology)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

