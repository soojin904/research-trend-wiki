---
title: "Analysis of population functional connectivity data via multilayer network embeddings"
authors: ['James Wilson', 'Melanie Baybay', 'Rishi Sankar', 'Paul E. Stillman', 'Abbie M. Popa']
year: 2020
venue: "Network Science"
tags: ['Functional Brain Connectivity Studies', 'Neural dynamics and brain function', 'Mental Health Research Topics']
source: raw/2020_openalex_Analysis_of_population_functional_connectivity_data_nws_2020_39.md
---

# Analysis of population functional connectivity data via multilayer network embeddings
**제목(한글)**: 다층 네트워크 임베딩을 통한 모집단 기능적 연결성 데이터 분석

**저자**: James Wilson; Melanie Baybay; Rishi Sankar; Paul E. Stillman; Abbie M. Popa
**출처**: Network Science, Vol.9, pp.99–122
**발행일**: 2020-10-21
**DOI**: https://doi.org/10.1017/nws.2020.39

## 한국어 요약

**연구질문**: 다층 네트워크 임베딩 방법을 통해 개인 및 집단 간 뇌 기능적 연결성 데이터에서 신뢰할 수 있는 특성을 어떻게 추출하고 비교할 수 있는가?

**방법론**:
- 다층 네트워크 기반 multi-node2vec 임베딩 알고리즘 개발
- 74명 건강인과 60명 조현병 환자의 안정 상태 fMRI 데이터 분석
- 임베딩을 통한 시각화, 군집화, 기능 영역 분류

**주요 결과**:
- multi-node2vec가 다층 네트워크 분석에 강력하고 신뢰성 있는 방법임을 확인
- 두 집단(건강인 vs. 조현병)에서 기본 모드 네트워크(default mode network)와 현저성 네트워크(salience network)에서 유의한 차이 발견
- 삼중 네트워크 모델 이론과 일치하는 결과 도출


## 초록 (원문)

Abstract Population analyses of functional connectivity have provided a rich understanding of how brain function differs across time, individual, and cognitive task. An important but challenging task in such population analyses is the identification of reliable features that describe the function of the brain, while accounting for individual heterogeneity. Our work is motivated by two particularly important challenges in this area: first, how can one analyze functional connectivity data over populations of individuals, and second, how can one use these analyses to infer group similarities and differences. Motivated by these challenges, we model population connectivity data as a multilayer network and develop the multi-node2vec algorithm, an efficient and scalable embedding method that automatically learns continuous node feature representations from multilayer networks. We use multi-node2vec to analyze resting state fMRI scans over a group of 74 healthy individuals and 60 patients with schizophrenia. We demonstrate how multilayer network embeddings can be used to visualize, cluster, and classify functional regions of the brain for these individuals. We furthermore compare the multilayer network embeddings of the two groups. We identify significant differences between the groups in the default mode network and salience network—findings that are supported by the triple network model theory of cognitive organization. Our findings reveal that multi-node2vec is a powerful and reliable method for analyzing multilayer networks. Data and publicly available code are available at https://github.com/jdwilson4/multi-node2vec .

## 키워드

Computer science, Population, Default mode network, Scalability, Artificial intelligence, Salience (neuroscience), Network analysis, Resting state fMRI

## 위키 연관

- [[pages/concepts/multilayer_network|다층 네트워크]]

## 메모

