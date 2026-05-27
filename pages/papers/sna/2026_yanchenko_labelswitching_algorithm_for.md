---
title: "A label-switching algorithm for fast core-periphery identification"
authors: ['Eric Yanchenko', 'Srijan Sengupta']
year: 2026
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'Advanced Graph Neural Networks', 'Graph theory and applications']
source: raw/2026_openalex_A_labelswitching_algorithm_for_fast_coreperiphery_nws_2026_10023.md
---

# A label-switching algorithm for fast core-periphery identification

**제목(한글)**: 고속 핵심-주변부(core-periphery) 구조 식별을 위한 레이블 전환 알고리즘

**저자**: Eric Yanchenko; Srijan Sengupta
**출처**: Network Science, Vol.14
**발행일**: 2026-01-01
**DOI**: https://doi.org/10.1017/nws.2026.10023

## 한국어 요약

**연구질문**: Borgatti & Everett(2000)의 핵심-주변부(CP) 지표를 기반으로, 기존보다 빠르고 정확하게 CP 구조를 탐지하는 알고리즘을 어떻게 설계할 수 있는가?

**방법론**:
- CP 지표의 수학적 재공식화를 통해 연산량을 대폭 줄이는 탐욕적 레이블 전환(greedy label-switching) 알고리즘 설계
- 합성 네트워크에서 분류 정확도와 실행 시간을 경쟁 방법과 비교
- 단조 상승(monotonic ascent) 및 지역 최적값 수렴 수학적 증명

**주요 결과**:
- 기존 구현 대비 연산 횟수 약 1/10 수준으로 감소 (order-of-magnitude improvement)
- 소규모 네트워크에서 전역 최적값의 90% 이내 해 일관 도출
- 실제 네트워크에서 경쟁 방법 대비 340배 빠른 실행 속도 달성

## 초록 (원문)

Abstract Core-periphery (CP) structure is frequently observed in networks where the nodes form two distinct groups: a small, densely interconnected core and a sparse periphery. Borgatti and Everett (Borgatti, S. P., &amp; Everett M. G. (2000). Models of core/periphery structures. Social Networks, 21(4), 375–395.) proposed one of the most popular methods to identify and quantify CP structure by comparing the observed network with an “ideal” CP structure. While this metric has been widely used, an improved algorithm is still needed. In this work, we detail a greedy, label-switching algorithm to identify CP structure that is both fast and accurate. By leveraging a mathematical reformulation of the CP metric, our proposed heuristic offers an order-of-magnitude improvement on the number of operations compared to a naive implementation. We prove that the algorithm monotonically ascends to a local maximum while consistently yielding solutions within 90% of the global optimum on small toy networks. On synthetic networks, our algorithm exhibits superior classification accuracies and run-times compared to a popular competing method, and on one-real- world network, it is 340 times faster.

## 키워드

Core (optical fiber), Metric (unit), Monotonic function, Heuristic, Identification (biology), Network structure

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

