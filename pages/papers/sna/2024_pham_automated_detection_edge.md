---
title: "Automated detection of edge clusters via an overfitted mixture prior"
authors: ['Hanh T. D. Pham', 'Daniel K. Sewell']
year: 2024
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'Bayesian Methods and Mixture Models', 'Advanced Clustering Algorithms Research']
source: raw/2024_openalex_Automated_detection_of_edge_clusters_via_nws_2023_22.md
---

# Automated detection of edge clusters via an overfitted mixture prior

**제목(한글)**: 과적합 혼합 사전분포를 활용한 엣지 군집 자동 탐지

**저자**: Hanh T. D. Pham; Daniel K. Sewell
**출처**: Network Science, Vol.12, pp.88–106
**발행일**: 2024-01-19
**DOI**: https://doi.org/10.1017/nws.2023.22

## 한국어 요약

**연구질문**: 클러스터 수 사전 지식 없이 네트워크 엣지 군집을 자동으로 탐지하기 위해 베이지안 프레임워크를 어떻게 활용할 수 있는가?

**방법론**:
- 잠재 공간 엣지 군집(LSEC) 모형 확장
- 희소 유한 혼합 사전분포(sparse finite mixture prior) 적용으로 군집 수 자동 선택
- 변분 베이즈 일반화 EM 알고리즘 및 해밀토니안 몬테 카를로-깁스 샘플러 개발

**주요 결과**:
- aLSEC는 기존 LSEC 대비 10~100배 이상 실행 시간 단축
- 네트워크 규모에 따라 계산 비용이 선형 증가하여 대규모 희소 네트워크에 확장 가능
- R 패키지 aLSEC로 공개 배포

## 초록 (원문)

Abstract Most community detection methods focus on clustering actors with common features in a network. However, clustering edges offers a more intuitive way to understand the network structure in many real-life applications. Among the existing methods for network edge clustering, the majority are algorithmic, with the exception of the latent space edge clustering (LSEC) model proposed by Sewell ( Journal of Computational and Graphical Statistics, 30 (2), 390–405, 2021). LSEC was shown to have good performance in simulation and real-life data analysis, but fitting this model requires prior knowledge of the number of clusters and latent dimensions, which are often unknown to researchers. Within a Bayesian framework, we propose an extension to the LSEC model using a sparse finite mixture prior that supports automated selection of the number of clusters. We refer to our proposed approach as the automated LSEC or aLSEC. We develop a variational Bayes generalized expectation-maximization approach and a Hamiltonian Monte Carlo-within Gibbs algorithm for estimation. Our simulation study showed that aLSEC reduced run time by 10 to over 100 times compared to LSEC. Like LSEC, aLSEC maintains a computational cost that grows linearly with the number of actors in a network, making it scalable to large sparse networks. We developed the R package aLSEC which implements the proposed methodology.

## 키워드

Cluster analysis, Computer science, Mixture model, Scalability, Artificial intelligence, Data mining, Machine learning

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

