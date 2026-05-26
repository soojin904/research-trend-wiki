---
title: "Model-based clustering for network data via a latent shrinkage position cluster model"
authors: ['Xian Yao Gwee', 'Isobel Claire Gormley', 'Michael Fop']
year: 2025
venue: "Network Science"
tags: ['Bayesian Methods and Mixture Models', 'Gaussian Processes and Bayesian Inference', 'Complex Network Analysis Techniques']
source: raw/2025_openalex_Modelbased_clustering_for_network_data_via_nws_2025_10014.md
---

# Model-based clustering for network data via a latent shrinkage position cluster model
**제목(한글)**: 잠재 수축 위치 군집 모델을 이용한 네트워크 데이터의 모델 기반 군집화

**저자**: Xian Yao Gwee; Isobel Claire Gormley; Michael Fop
**출처**: Network Science, Vol.13
**발행일**: 2025-01-01
**DOI**: https://doi.org/10.1017/nws.2025.10014

## 한국어 요약

**연구질문**: 잠재 공간 차원 수와 군집 수를 동시에 자동으로 결정하는 네트워크 군집화 모델을 어떻게 구축할 수 있는가?

**방법론**:
- 잠재 수축 위치 군집 모델(LSPCM, Latent Shrinkage Position Cluster Model) 제안
- 무한 차원 잠재 공간과 베이지안 비모수 수축 사전분포(shrinkage prior) 적용
- 희소 유한 가우시안 혼합 모델(sparse finite Gaussian mixture model)로 군집 수 자동 추론
- 스포츠·정치 맥락의 실제 Twitter 네트워크 데이터에 적용

**주요 결과**:
- LSPCM이 잠재 공간 차원과 군집 수를 동시에 추론하여 여러 모델 비교 불필요
- 시뮬레이션 연구에서 성능 우수성 입증
- 오픈소스 소프트웨어 제공으로 실제 활용 가능성 확보

## 초록 (원문)

Abstract Low-dimensional representation and clustering of network data are tasks of great interest across various fields. Latent position models are routinely used for this purpose by assuming that each node has a location in a low-dimensional latent space and by enabling node clustering. However, these models fall short through their inability to simultaneously determine the latent space dimension and number of clusters. Here we introduce the latent shrinkage position cluster model (LSPCM), which addresses this limitation. The LSPCM posits an infinite-dimensional latent space and assumes a Bayesian nonparametric shrinkage prior on the latent positions’ variance parameters resulting in higher dimensions having increasingly smaller variances, aiding the identification of dimensions with non-negligible variance. Further, the LSPCM assumes the latent positions follow a sparse finite Gaussian mixture model, allowing for automatic inference on the number of clusters related to non-empty mixture components. As a result, the LSPCM simultaneously infers the effective dimension of the latent space and the number of clusters, eliminating the need to fit and compare multiple models. The performance of the LSPCM is assessed via simulation studies and demonstrated through application to two real Twitter network datasets from sporting and political contexts. Open-source software is available to facilitate widespread use of the LSPCM.

## 키워드

Cluster analysis, Mixture model, Inference, Representation (politics), Dimension (graph theory), Position (finance), Latent class model, Latent variable model

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

