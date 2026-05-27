---
title: "IVCN: A Siamese Network for Quantifying the Inspirational Value of Text"
authors: ['Jie Zhang', 'Weilong Yang', 'Ye Ji']
year: 2025
venue: ""
tags: ['Topic Modeling', 'Aesthetic Perception and Analysis', 'Machine Learning in Materials Science']
source: raw/applied/applied_2025_IVCN_A_Siamese_Network_fo_aibdf67964_2025_11440887.md
---

# IVCN: A Siamese Network for Quantifying the Inspirational Value of Text

**제목(한글)**: IVCN: 텍스트의 영감적 가치를 정량화하기 위한 샴 네트워크

## 한국어 요약

**연구질문**: 과학적·분석적 텍스트의 영감적(heuristic) 가치가 내재적으로 주관적이고 주석 데이터가 희소한 상황에서, 이를 객관적이고 확장 가능하게 정량화하는 방법은 무엇인가?

**방법론**:
- 텍스트 창의성이 영감적 가치의 측정 가능한 대리 지표라는 가설을 검증하는 프록시 기반 학습 접근법 제안
- 사전학습 BERT 인코더 기반 샴 신경망(Siamese neural network)인 IVCN(Inspirational Value Comparator Network)과 기준선 비교 스코어링 메커니즘(BCSM) 구현
- CreataSet 데이터셋에서 교차 인코더 기준선 및 비지도 의미 지표와 비교

**주요 결과**:
- IVCN이 쌍별 정확도 98.89%로 교차 인코더 기준선과 Perplexity·의미 다양성 등 비지도 지표를 크게 능가
- 부트스트랩 안정성 분석으로 BCSM이 기준선 변동에 강건한 점수를 생성함을 확인

**저자**: Jie Zhang; Weilong Yang; Ye Ji
**출처**: , Vol.None, pp.819-827
**발행일**: 2025-12-26
**DOI**: https://doi.org/10.1109/aibdf67964.2025.11440887

## 초록 (원문)

Quantifying the inspirational or heuristic value of scientific and analytical texts is a crucial yet challenging task in big data analysis and artificial intelligence, hampered by inherent subjectivity and the scarcity of large-scale, annotated datasets. To address this gap, this paper proposes a novel proxy-based learning approach, validating the hypothesis that textual creativity serves as an effective measurable proxy for inspirational value. We introduce the Inspirational Value Comparator Network (IVCN), a Siamese neural network built upon a pre-trained BERT encoder. Unlike computationally expensive Cross-Encoder architectures, the IVCN offers superior inference efficiency, enabling our innovative Baseline-Comparison Scoring Mechanism (BCSM) to function as a scalable, continuous metric. Extensive experiments on the CreataSet dataset demonstrate that the IVCN achieves a state-of-the-art pairwise accuracy of 98.89%, significantly outperforming both strong Cross-Encoder baselines and traditional unsupervised semantic metrics such as Perplexity and Semantic Diversity. Furthermore, bootstrap stability analysis confirms that the BCSM generates robust scores resilient to baseline variations. This work presents a theoretically grounded and empirically validated methodology for evaluating complex semantic qualities without direct supervision, paving the way for more insightful automated text analysis.

## 키워드

Perplexity, Pairwise comparison, Inference, Task (project management), Baseline (sea), Value (mathematics), Function (biology), Artificial neural network

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

