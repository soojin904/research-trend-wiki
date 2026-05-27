---
title: "Walk-Independence Probabilities and WIP Centrality: A new heuristic for diffusion probabilities in networks"
authors: ['Maia King']
year: 2024
venue: "Social Networks"
tags: ['Complex Network Analysis Techniques', 'Opinion Dynamics and Social Influence', 'Peer-to-Peer Network Technologies']
source: raw/2024_openalex_WalkIndependence_Probabilities_and_WIP_Centrality_A_j_socnet_2023_11_007.md
---

# Walk-Independence Probabilities and WIP Centrality: A new heuristic for diffusion probabilities in networks

**제목(한글)**: 보행 독립 확률(WIP)과 WIP 중심성: 네트워크 확산 확률의 새로운 휴리스틱

**저자**: Maia King
**출처**: Social Networks, Vol.78, pp.173–183
**발행일**: 2024-03-01
**DOI**: https://doi.org/10.1016/j.socnet.2023.11.007

## 한국어 요약

**연구질문**: 네트워크 내 노드 간 확산 확률을 포함-배제 원리를 반영하여 보다 정확하게 계산하는 새로운 공식을 제안할 수 있는가?

**방법론**:
- 드 모르간 법칙(De Morgan's laws)을 활용한 포함-배제 원리 적용
- 보행 독립 확률(WIP: Walk-Independence Probabilities) 공식 도출
- WIP 중심성 및 차단 중심성(blocking centrality) 지표 개발

**주요 결과**:
- 기존 확산 중심성(diffusion centrality)은 확률 합산 시 포함-배제 원리를 무시해 왜곡된 결과 초래
- WIP 공식은 이 문제를 해결하는 간단하고 새로운 대안 제시
- 차단 중심성은 신호를 차단하는 노드 존재 시 활용 가능한 유도 중심성(induced centrality)

## 초록 (원문)

Calculating the true probability that a signal will be transmitted between any pair of nodes in a network is computationally hard. Diffusion centrality, which counts the expected number of times that a signal will be transmitted, is often used as a heuristic for this probability. But this formula can lead to distorted results when used in this way, because its summation of probabilities does not take account of the inclusion–exclusion principle. This paper provides a simple new formula for the probabilities of node-to-node diffusion in networks, which uses De Morgan’s laws to account for the inclusion–exclusion principle. Like diffusion centrality, this formula is based on the assumption that the probabilities of a signal travelling along each walk in a network are independent. The probabilities it calculates are therefore called Walk-Independence Probabilities (WIP). These probabilities provide two new centrality measures, WIP centrality and blocking centrality. Blocking centrality is a type of induced centrality which is calculated when some nodes block signals.

## 키워드

Centrality, Independence (probability theory), Heuristic, Computer science, Statistics, Diffusion, Econometrics, Mathematical optimization

## 위키 연관

- [[pages/methods/centrality|Centrality]]

## 메모

