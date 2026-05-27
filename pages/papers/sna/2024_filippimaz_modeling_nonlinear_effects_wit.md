---
title: "Modeling non-linear effects with neural networks in Relational Event Models"
authors: ['Edoardo Filippi-Mazzola', 'Ernst C. Wit']
year: 2024
venue: "Social Networks"
tags: ['Simulation Techniques and Applications', 'Opinion Dynamics and Social Influence', 'Complex Network Analysis Techniques']
source: raw/2024_openalex_Modeling_nonlinear_effects_with_neural_networks_j_socnet_2024_05_004.md
---

# Modeling non-linear effects with neural networks in Relational Event Models

**제목(한글)**: 관계 이벤트 모형에서 신경망을 활용한 비선형 효과 모델링

**저자**: Edoardo Filippi-Mazzola; Ernst C. Wit
**출처**: Social Networks, Vol.79, pp.25–33
**발행일**: 2024-06-07
**DOI**: https://doi.org/10.1016/j.socnet.2024.05.004

## 한국어 요약

**연구질문**: 관계 이벤트 모형(REM)에서 비선형 효과를 효율적으로 모델링하기 위해 신경망을 어떻게 활용할 수 있는가?

**방법론**:
- 심층 관계 이벤트 가산 모형 (DREAM: Deep Relational Event Additive Model) 제안
- 신경 가산 모형(Neural Additive Models)으로 각 효과를 독립 신경망이 포착
- GPU 활용 및 메모리 관리 최적화로 대규모 네트워크(약 800만 노드·1억 이벤트) 처리

**주요 결과**:
- DREAM은 기존 REM 대비 우월한 계산 효율성 시연
- 미국 특허 인용 네트워크 분석에 적용하여 확장성 검증
- 동적 네트워크 분석의 비선형 관계 포착에 효과적인 새 프레임워크 제공

## 초록 (원문)

Dynamic networks offer an insight of how relational systems evolve. However, modeling these networks efficiently remains a challenge, primarily due to computational constraints, especially as the number of observed events grows. This paper addresses this issue by introducing the Deep Relational Event Additive Model (DREAM) as a solution to the computational challenges presented by modeling non-linear effects in Relational Event Models (REMs). DREAM relies on Neural Additive Models to model non-linear effects, allowing each effect to be captured by an independent neural network. By strategically trading computational complexity for improved memory management and leveraging the computational capabilities of graphic processor units (GPUs), DREAM efficiently captures complex non-linear relationships within data. This approach demonstrates the capability of DREAM in modeling dynamic networks and scaling to larger networks. Comparisons with traditional REM approaches showcase DREAM superior computational efficiency. The model potential is further demonstrated by an examination of the patent citation network, which contains nearly 8 million nodes and 100 million events. • We propose the Deep Relational Event Model (DREAM) to model large dynamic networks. • DREAM uses neural networks to model non-linear effects in Relational Event Models. • An extensive simulation study is conducted to validate DREAM’s performance. • DREAM’s potential is further highlighted by analyzing the US patent citation network.

## 키워드

Event (particle physics), Artificial neural network, Computer science, Linear model, Artificial intelligence, Psychology, Cognitive psychology, Machine learning

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

