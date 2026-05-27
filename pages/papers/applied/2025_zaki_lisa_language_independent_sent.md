---
title: "LISA: language independent sentiment analysis using graph neural networks"
authors: ['Mohamed Zaki', 'Basheer Youssef', 'Salwa El-Gamal', 'Mohamed Abd-Elrahem']
year: 2025
venue: "Complex & Intelligent Systems"
tags: ['Sentiment Analysis and Opinion Mining', 'Big Data and Digital Economy', 'Topic Modeling']
source: raw/applied/applied_2025_LISA_language_independent_s40747_025_02145_8.md
---

# LISA: language independent sentiment analysis using graph neural networks

**제목(한글)**: LISA: 그래프 신경망을 사용한 언어 독립적 감성 분석

## 한국어 요약

**연구질문**: 다국어 자연어 처리에서 발생하는 언어별 표현 차이 문제를 극복하고 언어에 독립적인 감성 분석을 수행하기 위해 그래프 신경망을 어떻게 활용할 수 있는가?

**방법론**:
- 입력 텍스트를 그래프로 변환하여 다국어 표현 차이를 우회하는 텍스트-그래프 변환 모듈 구현
- 그래프 합성곱 네트워크(GCN)와 그래프 어텐션 네트워크(GAT) 두 가지 그래프 신경망 유형 비교 실험
- Word2vec 임베딩과 연결하여 아마존 리뷰, 트윗의 두 가지 다국어 데이터셋으로 평가

**주요 결과**:
- LISA의 정확도, F1-스코어, 혼동 행렬이 최신 기준(SOTA) 프레임워크와 동등한 수준임을 확인
- 어텐션이 감성 분석에 미치는 효과를 GCN과 GAT 비교를 통해 규명

**저자**: Mohamed Zaki; Basheer Youssef; Salwa El-Gamal; Mohamed Abd-Elrahem
**출처**: Complex & Intelligent Systems, Vol.12
**발행일**: 2025-12-29
**DOI**: https://doi.org/10.1007/s40747-025-02145-8

## 초록 (원문)

Abstract This paper presents LISA as a Language Independent Sentiment Analysis tool that exploits Graph Neural Networks, GNN, for sentiment analysis, SA, applications. To build up that analyzer two types of GNN are examined. These types are: (1) Graph convolutional Networks, GCN, and (2) Graph Attention Networks, GAT. The input text is transformed to a corresponding graph to bypass the multilingual differential representations between Natural Languages, NL. Accordingly, LISA includes input steam of text (e.g. tweets, reviews…), followed by a text to graph module which is connected to a tokenizer to determine the correct tokens and pass them to Word2vec embedding. The corresponding graph of the underlying text enters the GNN which has been implemented by either GCN or GAT to generate the output sentiment polarity (+ ve/−ve). The two GNN models are compared to explore the effect of attention on a SA. In addition, LISA performance is evaluated (using two multilingual datasets: amazon reviews, tweets). It has been found that its accuracy, F1 score and confusion matrices are in the same range of the state of the art (SOTA) framework.

## 키워드

Graph, Word2vec, Sentiment analysis, Convolutional neural network, Confusion, Artificial neural network, Polarity (international relations)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

