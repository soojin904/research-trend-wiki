---
title: "Sparser, Faster, Lighter Transformer Language Models"
authors: ['Edoardo Cetin', 'Stefano Peluchetti', 'Emilio Castillo', 'Akira Naruse', 'Mana Murakami', 'Llion Jones']
year: 2026
venue: "ArXiv.org"
tags: ['Topic Modeling', 'Natural Language Processing Techniques', 'Advanced Neural Network Applications']
source: raw/applied/applied_2026_Sparser_Faster_Lighter_Tr_nodoi.md
---

# Sparser, Faster, Lighter Transformer Language Models
**제목(한글)**: 더 희소하고, 빠르고, 가벼운 트랜스포머 언어 모델

## 한국어 요약

**연구질문**: 거대 언어 모델(LLM)의 막대한 연산 비용을 줄이기 위해 피드포워드 레이어의 비구조적 희소성(Unstructured Sparsity)을 어떻게 실용적으로 활용할 수 있는가?

**방법론**:
- LLM 피드포워드 레이어에 특화된 새로운 희소 패킹 형식과 CUDA 커널 개발
- L1 정규화를 통해 99% 이상의 희소성 유도 가능성 정량 연구
- 학습 및 추론 시 처리량·에너지 효율·메모리 사용량 이점을 모델 규모별로 측정

**주요 결과**:
- 단순 L1 정규화로 99% 이상의 희소성 달성이 가능하며 다운스트림 성능 손실은 무시 가능한 수준
- 개발된 희소 CUDA 커널 적용 시 모델 규모가 커질수록 처리량·에너지 효율·메모리 사용량 측면의 이익이 더욱 증가함을 확인

**저자**: Edoardo Cetin; Stefano Peluchetti; Emilio Castillo; Akira Naruse; Mana Murakami; Llion Jones
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-03-24
**DOI**: 

## 초록 (원문)

Scaling autoregressive large language models (LLMs) has driven unprecedented progress but comes with vast computational costs. In this work, we tackle these costs by leveraging unstructured sparsity within an LLM's feedforward layers, the components accounting for most of the model parameters and execution FLOPs. To achieve this, we introduce a new sparse packing format and a set of CUDA kernels designed to seamlessly integrate with the optimized execution pipelines of modern GPUs, enabling efficient sparse computation during LLM inference and training. To substantiate our gains, we provide a quantitative study of LLM sparsity, demonstrating that simple L1 regularization can induce over 99% sparsity with negligible impact on downstream performance. When paired with our kernels, we show that these sparsity levels translate into substantial throughput, energy efficiency, and memory usage benefits that increase with model scale. We will release all code and kernels under an open-source license to promote adoption and accelerate research toward establishing sparsity as a practical axis for improving the efficiency and scalability of modern foundation models.

## 키워드

Scalability, Inference, Computation, CUDA, Transformer, Set (abstract data type), Autoregressive model, Redundancy (engineering)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

