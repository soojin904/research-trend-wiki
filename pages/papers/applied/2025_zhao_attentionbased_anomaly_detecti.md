---
title: "Attention-Based Anomaly Detection in Dynamic Network"
authors: ['Yiming Zhao', 'W. Wang', 'Nannan Wu', 'Liu Jilei', 'Ying Sun', 'Wei Yu', 'Quannan Zu']
year: 2025
venue: "Big Data Mining and Analytics"
tags: ['Anomaly Detection Techniques and Applications', 'Software System Performance and Reliability', 'Advanced Graph Neural Networks']
source: raw/applied/applied_2025_AttentionBased_Anomaly_De_bdma_2025_9020033.md
---

# Attention-Based Anomaly Detection in Dynamic Network

**제목(한글)**: 동적 네트워크에서의 어텐션 기반 이상 탐지

## 한국어 요약

**연구질문**: 소셜 네트워크, 사이버 보안 등 실세계 동적 네트워크에서 지속적으로 진화하는 다양한 이상 유형을 효과적으로 탐지하기 위한 엔드투엔드 프레임워크를 어떻게 구현할 수 있는가?

**방법론**:
- 어텐션 메커니즘으로 다양한 타임스탬프에서 노드 속성(개인 특성)과 구조적 특징(집단 패턴) 간 복잡한 상호작용을 포착하는 AADDN(Attention-based Anomaly Detection In Dynamic Network) 프레임워크 개발
- 잠재 공간에서 포괄적 표현을 학습하는 이중 오토인코더(dual autoencoder) 아키텍처 활용

**주요 결과**:
- AADDN이 시간적·구조적·속성 정보의 통합 학습을 강조하여 동적 네트워크 환경에서 개별 및 집단 이상 모두에 대한 탐지 능력이 기존 방법론을 능가
- 휴리스틱 규칙에 의존하는 기존 방법 대비 더 포괄적인 이상 탐지 역량을 입증

**저자**: Yiming Zhao; W. Wang; Nannan Wu; Liu Jilei; Ying Sun; Wei Yu; Quannan Zu
**출처**: Big Data Mining and Analytics, Vol.9, pp.70-86
**발행일**: 2025-12-09
**DOI**: https://doi.org/10.26599/bdma.2025.9020033

## 초록 (원문)

Detecting anomalies in dynamic networks is essential for a range of real-world applications, such as social networks and cybersecurity. However, it encounters substantial challenges due to the diverse and ever-evolving nature of these anomalies. We present Attention-based Anomaly Detection In Dynamic Network (AADDN), an innovative end-to-end anomaly detection framework that utilizes attention mechanisms to capture the complex interactions between node attributes (individual characteristics) and structural features (collective patterns) across various time stamps. Unlike traditional methods that depend on heuristic rules with limited scope, AADDN employs a dual autoencoder architecture to learn comprehensive representations in the latent space, allowing the model to more effectively identify both individual and collective anomalies. By emphasizing the integrated learning of temporal, structural, and attribute information, our approach surpasses existing methods, showcasing superior anomaly detection capabilities in dynamic network environments.

## 키워드

Anomaly detection, Autoencoder, Heuristic, Dynamic network analysis, Anomaly (physics), Node (physics), Dual (grammatical number)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

