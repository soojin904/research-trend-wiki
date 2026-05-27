---
title: "Techniques for blocking the propagation of two simultaneous contagions over networks using a graph dynamical systems framework"
authors: ['Henry L. Carscadden', 'Chris J. Kuhlman', 'Madhav Marathe', 'S. S. Ravi', 'Daniel J. Rosenkrantz']
year: 2022
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'Opinion Dynamics and Social Influence', 'COVID-19 epidemiological studies']
source: raw/2022_openalex_Techniques_for_blocking_the_propagation_of_nws_2022_18.md
---

# Techniques for blocking the propagation of two simultaneous contagions over networks using a graph dynamical systems framework
**제목(한글)**: 그래프 동적 시스템 프레임워크를 이용한 두 가지 동시 전염의 네트워크 전파 차단 기법

**저자**: Henry L. Carscadden; Chris J. Kuhlman; Madhav Marathe; S. S. Ravi; Daniel J. Rosenkrantz
**출처**: Network Science, Vol.10, pp.234–260
**발행일**: 2022-08-30
**DOI**: https://doi.org/10.1017/nws.2022.18


## 한국어 요약

**연구질문**: 소셜 네트워크에서 두 가지 전염병이 동시에 확산될 때, 제한된 예방 접종 예산 내에서 신규 감염자 수를 최소화하는 최적 전략은 무엇인가?

**방법론**:
- 임계값 모델(threshold model)과 이산 동적 시스템(discrete dynamical systems) 프레임워크 활용
- 정수 선형 프로그래밍(ILP) 공식화로 최적 해 도출
- 집합 커버 일반화 기반 휴리스틱 알고리즘 개발 및 비교 평가

**주요 결과**:
- NP-난해한 최적화 문제를 ILP로 정확하게 풀 수 있으나 계산 비용이 높음
- 제안된 휴리스틱이 최적 해와 근사하면서 ILP보다 수십 배 빠름
- 민감도 분석을 통해 휴리스틱의 강건성 확인


## 초록 (원문)

Abstract We consider the simultaneous propagation of two contagions over a social network. We assume a threshold model for the propagation of the two contagions and use the formal framework of discrete dynamical systems. In particular, we study an optimization problem where the goal is to minimize the total number of new infections subject to a budget constraint on the total number of available vaccinations for the contagions. While this problem has been considered in the literature for a single contagion, our work considers the simultaneous propagation of two contagions. This optimization problem is NP-hard. We present two main solution approaches for the problem, namely an integer linear programming (ILP) formulation to obtain optimal solutions and a heuristic based on a generalization of the set cover problem. We carry out a comprehensive experimental evaluation of our solution approaches using many real-world networks. The experimental results show that our heuristic algorithm produces solutions that are close to the optimal solution and runs several orders of magnitude faster than the ILP-based approach for obtaining optimal solutions. We also carry out sensitivity studies of our heuristic algorithm.

## 키워드

Heuristic, Mathematical optimization, Computer science, Generalization, Set (abstract data type), Dynamical systems theory, Integer programming, Graph

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

