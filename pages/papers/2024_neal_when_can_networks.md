---
title: "When can networks be inferred from observed groups?"
authors: ['Zachary P. Neal']
year: 2024
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'Opinion Dynamics and Social Influence', 'Topological and Geometric Data Analysis']
source: raw/2024_openalex_When_can_networks_be_inferred_from_nws_2024_6.md
---

# When can networks be inferred from observed groups?

**제목(한글)**: 관찰된 집단으로부터 네트워크를 언제 추론할 수 있는가?

**저자**: Zachary P. Neal
**출처**: Network Science, Vol.12, pp.189–200
**발행일**: 2024-04-12
**DOI**: https://doi.org/10.1017/nws.2024.6

## 한국어 요약

**연구질문**: 관찰된 집단(예: 논문 공저 관계)으로부터 관심 네트워크를 정확하게 추론하기 위한 조건은 무엇인가?

**방법론**:
- 시뮬레이션을 통해 미관찰 네트워크 구조, 관찰 집단 수, 집단 멤버십과 클리크 대응 정도, 추론 방법 변수 조작
- 비가중 이중 모드 투영 방법 및 통계적 백본 추출 모형 비교

**주요 결과**:
- 적은 수의 집단 관찰 시 단순 비가중 투영으로도 정확한 추론 가능(단, 집단 멤버십이 클리크에 밀접히 대응할 때)
- 다수 집단 관찰 시 통계적 백본 추출이 집단 멤버십이 무작위여도 정확한 추론 가능
- 연구자의 집단 관찰 수와 구조에 따라 최적 추론 방법이 달라짐

## 초록 (원문)

Abstract Collecting network data directly from network members can be challenging. One alternative involves inferring a network from observed groups, for example, inferring a network of scientific collaboration from researchers’ observed paper authorships. In this paper, I explore when an unobserved undirected network of interest can accurately be inferred from observed groups. The analysis uses simulations to experimentally manipulate the structure of the unobserved network to be inferred, the number of groups observed, the extent to which the observed groups correspond to cliques in the unobserved network, and the method used to draw inferences. I find that when a small number of groups are observed, an unobserved network can be accurately inferred using a simple unweighted two-mode projection, provided that each group’s membership closely corresponds to a clique in the unobserved network. In contrast, when a large number of groups are observed, an unobserved network can be accurately inferred using a statistical backbone extraction model, even if the groups’ memberships are mostly random. These findings offer guidance for researchers seeking to indirectly measure a network of interest using observations of groups.

## 키워드

Clique, Contrast (vision), Computer science, Network analysis, Group (periodic table), Random graph, Network structure, Data mining

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

