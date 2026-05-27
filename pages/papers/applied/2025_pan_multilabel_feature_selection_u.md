---
title: "Multilabel feature selection using graph neural networks and differential evolution optimization"
authors: ['Ning Pan']
year: 2025
venue: "Scientific Reports"
tags: ['Text and Document Classification Technologies', 'Machine Learning and Data Classification', 'Advanced Graph Neural Networks']
source: raw/applied/applied_2025_Multilabel_feature_select_s41598_025_27824_x.md
---

# Multilabel feature selection using graph neural networks and differential evolution optimization

**제목(한글)**: 그래프 신경망(GNN)과 차분 진화(Differential Evolution) 최적화를 활용한 다중 레이블 특징 선택

## 한국어 요약

**연구질문**: GNN과 차분 진화(DE) 알고리즘을 결합하면 다중 레이블 데이터의 특징 선택 문제를 효과적으로 해결할 수 있는가?

**방법론**:
- GNN으로 특징-레이블 간 복잡한 관계 및 레이블 간 상호의존성 모델링
- DE 전역 최적화로 최적 특징 부분집합 탐색
- 텍스트·이미지 도메인 6개 다양한 데이터셋에서 성능 평가

**주요 결과**:
- GNN-DE가 더 적은 특징으로 최적의 분류 성능 달성
- 복잡한 레이블 상관관계를 가진 Enron·Scene 데이터셋에서 기존 방법 대비 우수한 성능
- 계산 복잡도 감소와 함께 효율성 입증

**저자**: Ning Pan
**출처**: Scientific Reports, Vol.15, pp.44349-44349
**발행일**: 2025-12-23
**DOI**: https://doi.org/10.1038/s41598-025-27824-x

## 초록 (원문)

In recent years, the exponential growth of high-dimensional data across domains such as data mining, machine learning, bioinformatics, social network analysis, and image processing has amplified the importance of feature selection as a primary method for dimensionality reduction. High-dimensional datasets often include redundant, noisy, and irrelevant features that hinder the development of accurate, efficient, and reliable learning models. This issue becomes even more critical in multi-label scenarios, where each instance may be associated with multiple labels, creating intricate interactions between features and labels as well as interdependencies among the labels themselves. Traditional feature selection techniques, designed primarily for single-label problems, struggle to address the complexities of multi-label data. Consequently, there is a pressing need for novel approaches that can effectively capture and utilize these complexities. This study introduces a hybrid method that combines the representational power of Graph Neural Networks (GNNs) with the optimization efficiency of Differential Evolution (DE) to tackle multi-label feature selection challenges. GNNs leverage graph structures to model complex relationships between features and labels, allowing for simultaneous consideration of feature relevance and label dependencies. DE, a robust global optimization algorithm, ensures the selection of an optimal subset of features by exploring vast search spaces and avoiding local optima. The proposed method was evaluated on six diverse datasets spanning text and image domains. GNN-DE achieves optimal classification performance while selecting fewer features, demonstrating its efficiency in reducing computational complexity. For datasets with complex label correlations, such as Enron and Scene, this method outperforms existing approaches.

## 키워드

Leverage (statistics), Feature selection, Differential evolution, Curse of dimensionality, Graph, Artificial neural network, Feature (linguistics), Pattern recognition (psychology)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

