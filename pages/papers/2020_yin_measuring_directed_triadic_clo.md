---
title: "Measuring directed triadic closure with closure coefficients"
authors: ['Hao Yin', 'Austin R. Benson', 'Johan Ugander']
year: 2020
venue: "Network Science"
tags: ['Advanced Graph Neural Networks', 'Complex Network Analysis Techniques', 'Mental Health Research Topics']
source: raw/2020_openalex_Measuring_directed_triadic_closure_with_closure_nws_2020_20.md
---

# Measuring directed triadic closure with closure coefficients
**제목(한글)**: 폐쇄 계수를 이용한 방향성 삼각 폐쇄 측정

**저자**: Hao Yin; Austin R. Benson; Johan Ugander
**출처**: Network Science, Vol.8, pp.551–573
**발행일**: 2020-06-01
**DOI**: https://doi.org/10.1017/nws.2020.20

## 한국어 요약

**연구질문**: 방향성 그래프에서 삼각 폐쇄를 시작하는 노드(initiator) 관점에서 어떻게 폐쇄를 측정할 수 있는가?

**방법론**:
- 8가지 방향성 폐쇄 계수(directed closure coefficients) 제안
- 방향성 구성 모델(directed configuration model) 이론 분석
- 실제 네트워크에서 경험적 변동 분석 및 머신러닝 예측 과제 적용

**주요 결과**:
- 기존의 중심 노드 관점 측도와 달리 시작 노드(initiator) 관점의 8개 폐쇄 계수 제안
- 계수 값과 차수 분포의 결합 모멘트 간 이론적 연결 관계 밝힘
- 이진 예측 과제에서 AUC 0.92 이상 달성, 기존 측도 대비 성능 향상


## 초록 (원문)

Abstract Recent work studying triadic closure in undirected graphs has drawn attention to the distinction between measures that focus on the “center” node of a wedge (i.e., length-2 path) versus measures that focus on the “initiator,” a distinction with considerable consequences. Existing measures in directed graphs, meanwhile, have all been center-focused. In this work, we propose a family of eight directed closure coefficients that measure the frequency of triadic closure in directed graphs from the perspective of the node initiating closure. The eight coefficients correspond to different labeled wedges, where the initiator and center nodes are labeled, and we observe dramatic empirical variation in these coefficients on real-world networks, even in cases when the induced directed triangles are isomorphic. To understand this phenomenon, we examine the theoretical behavior of our closure coefficients under a directed configuration model. Our analysis illustrates an underlying connection between the closure coefficients and moments of the joint in- and out-degree distributions of the network, offering an explanation of the observed asymmetries. We also use our directed closure coefficients as predictors in two machine learning tasks. We find interpretable models with AUC scores above 0.92 in class-balanced binary prediction, substantially outperforming models that use traditional center-focused measures.

## 키워드

Closure (psychology), Focus (optics), Node (physics), Directed graph, Binary number, Closure problem, Measure (data warehouse), Perspective (graphical)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

