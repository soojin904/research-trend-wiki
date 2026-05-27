---
title: "Data-Driven Cross-Lingual Anomaly Detection via Self-Supervised Representation Learning"
authors: ['Mengdi Wang', 'Nuo Wang', 'Li Mei', 'Yuan Li', 'Xinyang Liu', 'Surui Hua', 'Manzhou Li']
year: 2026
venue: "Electronics"
tags: ['Anomaly Detection Techniques and Applications', 'Imbalanced Data Classification Techniques', 'Topic Modeling']
source: raw/applied/applied_2026_DataDriven_CrossLingual_A_electronics15010212.md
---

# Data-Driven Cross-Lingual Anomaly Detection via Self-Supervised Representation Learning
**제목(한글)**: 자기 지도 표현 학습을 활용한 데이터 구동형 다국어 이상거래 탐지 기술

**저자**: Mengdi Wang; Nuo Wang; Li Mei; Yuan Li; Xinyang Liu; Surui Hua; Manzhou Li
**출처**: Electronics, Vol.15, pp.212-212
**발행일**: 2026-01-02
**DOI**: https://doi.org/10.3390/electronics15010212

## 한국어 요약

**연구질문**: 라벨링 데이터가 부족하고 의미적 불일치가 높은 다국어 금융 환경에서 텍스트와 이력 거래 데이터를 결합해 고성능의 다국어 이상징후(Anomaly)를 효과적으로 탐지할 수 있는가?

**방법론**:
- 다국어 이상거래 탐지 프레임워크(LR-SSAD) 구축: 교차 언어 마스크 예측 모듈을 통한 의미 공간 정렬
- 맘바(Mamba) 기반의 시퀀스 재구성 모듈을 활용하여 선형 계산 복잡도(O(N)) 조건하에 대규모 금융 트랜잭션 모델링
- 소음이 포함된 데이터를 정제하기 위한 노이즈 인지적 의사 라벨 정제 메커니즘 도입 및 120만 개 다국어 텍스트와 42만 개 거래 내역 테스트

**주요 결과**:
- 정확도 0.932, 정밀도 0.914, 재현율 0.891, F1-Score 0.902, AUC 0.948을 달성하여 기존 베이스라인 대비 괄목할 만한 성능 향상 달성
- 기존 트랜스포머 기반 어텐션 구조의 계산 병목 문제를 극복하여 장기 시퀀스의 효율적인 분석 기능 확보
- 금융 도메인 등 실제 로우리소스(low-resource) 다국어 이상거래 모니터링 환경에 적용 가능한 확장 가능한 해결책 제시


## 초록 (원문)

Deep anomaly detection in multilingual environments remains challenging due to limited labeled data, semantic inconsistency across languages, and the unstable distribution of rare abnormal patterns. These challenges are particularly severe in low-resource scenarios—characterized by scarce labeled anomaly data and non-standardized terminology—where conventional supervised or transfer-based models suffer from semantic drift and feature mismatch. To address these limitations, a data-driven cross-lingual anomaly detection framework, LR-SSAD, is proposed. Targeting paired text and behavioral data without requiring parallel translation corpora, the framework is built upon the joint optimization of complementary self-supervised objectives. A cross-lingual masked prediction module is designed to capture language-invariant semantic structures to align semantic spaces, while a Mamba-based sequence reconstruction module leverages its linear computational complexity (O(N)) to efficiently model long-range dependencies in transaction histories, overcoming the computational bottlenecks of quadratic attention mechanisms. To further enhance robustness under noisy supervision, a noise-aware pseudo-label refinement mechanism is introduced. Evaluated on a newly constructed real-world financial dataset (spanning January–June 2023) comprising 1.2 million multilingual texts and 420,000 transaction sequences, experimental results demonstrate that LR-SSAD achieves substantial improvements over state-of-the-art baselines. The model achieves an accuracy of 0.932, a precision of 0.914, a recall of 0.891, and an F1-score of 0.902, with the Area Under the Curve (AUC) reaching 0.948. The proposed framework provides a scalable and data-efficient solution for anomaly detection in real-world multilingual environments.

## 키워드

Anomaly detection, Scalability, Robustness (evolution), Precision and recall, Leverage (statistics), Anomaly (physics), Computational complexity theory, Pattern recognition (psychology)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

