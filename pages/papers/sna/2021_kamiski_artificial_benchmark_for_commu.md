---
title: "Artificial Benchmark for Community Detection (ABCD)—Fast random graph model with community structure"
authors: ['Bogumił Kamiński', 'Paweł Prałat', 'François Théberge']
year: 2021
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'Opinion Dynamics and Social Influence', 'Mental Health Research Topics']
source: raw/2021_openalex_Artificial_Benchmark_for_Community_Detection_ABCDFast_nws_2020_45.md
---

# Artificial Benchmark for Community Detection (ABCD)—Fast random graph model with community structure
**제목(한글)**: 커뮤니티 탐지를 위한 인공 벤치마크(ABCD): 커뮤니티 구조를 가진 빠른 랜덤 그래프 모델

**저자**: Bogumił Kamiński; Paweł Prałat; François Théberge
**출처**: Network Science, Vol.9, pp.153–178
**발행일**: 2021-01-26
**DOI**: https://doi.org/10.1017/nws.2020.45

## 한국어 요약

**연구질문**: 기존 LFR 벤치마크의 확장성·이론적 분석 한계를 극복하면서 커뮤니티 탐지(community detection) 알고리즘 평가에 활용 가능한 새로운 합성 그래프 모델을 어떻게 설계할 수 있는가?

**방법론**:
- 커뮤니티 구조와 거듭제곱 차수 분포(power law degree distribution)를 가진 ABCD 랜덤 그래프 모델 제안
- 혼합 파라미터 ξ로 커뮤니티 강도 조절 가능
- LFR 모델과의 속도·속성 비교 실험

**주요 결과**:
- ABCD는 LFR과 유사한 네트워크 속성을 생성하면서 속도, 단순성, 확장성에서 우수
- 파라미터 ξ가 LFR의 혼합 파라미터 μ와 대응되어 직관적 해석 가능
- 독립적 커뮤니티에서 완전 무작위 그래프까지 부드럽게 전환 가능

## 초록 (원문)

Abstract Most of the current complex networks that are of interest to practitioners possess a certain community structure that plays an important role in understanding the properties of these networks. For instance, a closely connected social communities exhibit faster rate of transmission of information in comparison to loosely connected communities. Moreover, many machine learning algorithms and tools that are developed for complex networks try to take advantage of the existence of communities to improve their performance or speed. As a result, there are many competing algorithms for detecting communities in large networks. Unfortunately, these algorithms are often quite sensitive and so they cannot be fine-tuned for a given, but a constantly changing, real-world network at hand. It is therefore important to test these algorithms for various scenarios that can only be done using synthetic graphs that have built-in community structure, power law degree distribution, and other typical properties observed in complex networks. The standard and extensively used method for generating artificial networks is the LFR graph generator. Unfortunately, this model has some scalability limitations and it is challenging to analyze it theoretically. Finally, the mixing parameter μ , the main parameter of the model guiding the strength of the communities, has a non-obvious interpretation and so can lead to unnaturally defined networks. In this paper, we provide an alternative random graph model with community structure and power law distribution for both degrees and community sizes, the Artificial Benchmark for Community Detection (ABCD graph). The model generates graphs with similar properties as the LFR one, and its main parameter ξ can be tuned to mimic its counterpart in the LFR model, the mixing parameter μ . We show that the new model solves the three issues identified above and more. In particular, we test the speed of our algorithm and do a number of experiments comparing basic properties of both ABCD and LFR. The conclusion is that these models produce graphs with comparable properties but ABCD is fast, simple, and can be easily tuned to allow the user to make a smooth transition between the two extremes: pure (independent) communities and random graph with no community structure.

## 키워드

Computer science, Community structure, Benchmark (surveying), Random graph, Scalability, Graph, Theoretical computer science, Artificial intelligence

## 위키 연관

- [[pages/methods/centrality|Centrality]]

## 메모

