---
title: "Learning to count: A deep learning framework for graphlet count estimation"
authors: ['Xutong Liu', 'Yu-Zhen Janice Chen', 'John C. S. Lui', 'Konstantin Avrachenkov']
year: 2020
venue: "Network Science"
tags: ['Advanced Graph Neural Networks', 'Complex Network Analysis Techniques', 'Bayesian Modeling and Causal Inference']
source: raw/2020_openalex_Learning_to_count_A_deep_learning_nws_2020_35.md
---

# Learning to count: A deep learning framework for graphlet count estimation
**제목(한글)**: 세는 법 학습: 그래플릿 개수 추정을 위한 딥러닝 프레임워크

**저자**: Xutong Liu; Yu-Zhen Janice Chen; John C. S. Lui; Konstantin Avrachenkov
**출처**: Network Science, Vol.9, pp.S23–S60
**발행일**: 2020-09-11
**DOI**: https://doi.org/10.1017/nws.2020.35

## 한국어 요약

**연구질문**: 과거 그래프 데이터로부터 학습하여 새로운 그래프의 그래플릿 개수를 효율적으로 추정하는 딥러닝 프레임워크를 어떻게 구축할 수 있는가?

**방법론**:
- 그래플릿 개수 학습(GCL) 문제 정식화
- 두 가지 합성곱 신경망(CNN) 모델 및 데이터 전처리 기법 포함 딥러닝 프레임워크
- 합성 및 실제 그래프에서 3-, 4-, 5-노드 그래플릿 대상 실험

**주요 결과**:
- 합성 그래프에서 기존 방법 대비 최대 100배 속도 향상
- 실제 그래프에서도 유사한 속도와 경쟁력 있는 정확도 달성
- 반복 등장하는 유사 그래프 구조 재활용으로 계산 효율 대폭 개선


## 초록 (원문)

Abstract Graphlet counting is a widely explored problem in network analysis and has been successfully applied to a variety of applications in many domains, most notatbly bioinformatics, social science, and infrastructure network studies. Efficiently computing graphlet counts remains challenging due to the combinatorial explosion, where a naive enumeration algorithm needs O( N k ) time for k -node graphlets in a network of size N . Recently, many works introduced carefully designed combinatorial and sampling methods with encouraging results. However, the existing methods ignore the fact that graphlet counts and the graph structural information are correlated. They always consider a graph as a new input and repeat the tedious counting procedure on a regular basis even if it is similar or exactly isomorphic to previously studied graphs. This provides an opportunity to speed up the graphlet count estimation procedure by exploiting this correlation via learning methods. In this paper, we raise a novel graphlet count learning (GCL) problem: given a set of historical graphs with known graphlet counts, how to learn to estimate/predict graphlet count for unseen graphs coming from the same (or similar) underlying distribution. We develop a deep learning framework which contains two convolutional neural network models and a series of data preprocessing techniques to solve the GCL problem. Extensive experiments are conducted on three types of synthetic random graphs and three types of real-world graphs for all 3-, 4-, and 5-node graphlets to demonstrate the accuracy, efficiency, and generalizability of our framework. Compared with state-of-the-art exact/sampling methods, our framework shows great potential, which can offer up to two orders of magnitude speedup on synthetic graphs and achieve on par speed on real-world graphs with competitive accuracy.

## 키워드

Preprocessor, Computer science, Enumeration, Artificial intelligence, Machine learning, Graph, Convolutional neural network, Theoretical computer science

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

