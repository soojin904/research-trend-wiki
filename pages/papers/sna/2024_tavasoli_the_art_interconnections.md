---
title: "The art of interconnections: Achieving maximum algebraic connectivity in multilayer networks"
authors: ['Ali Tavasoli', 'Heman Shakeri', 'Ehsan Ardjmand', 'Shakil Rahman']
year: 2024
venue: "Network Science"
tags: ['Interconnection Networks and Systems', 'Low-power high-performance VLSI design', 'Advanced Optical Network Technologies']
source: raw/2024_openalex_The_art_of_interconnections_Achieving_maximum_nws_2024_9.md
---

# The art of interconnections: Achieving maximum algebraic connectivity in multilayer networks

**제목(한글)**: 상호 연결의 기술: 다층 네트워크에서 대수적 연결성 극대화

**저자**: Ali Tavasoli; Heman Shakeri; Ehsan Ardjmand; Shakil Rahman
**출처**: Network Science, Vol.12, pp.261–288
**발행일**: 2024-09-01
**DOI**: https://doi.org/10.1017/nws.2024.9

## 한국어 요약

**연구질문**: 다층 네트워크에서 총 가중치 임계값 이하로 대수적 연결성(algebraic connectivity)을 극대화하는 최적 상호 연결 설계를 어떻게 달성할 수 있는가?

**방법론**:
- 라플라시안 행렬의 두 번째 최소 고유값(Fiedler 값)을 대수적 연결성 지표로 활용
- 볼록 프레임워크 및 등가 그래프 임베딩 문제로 변환
- 개별 Fiedler 벡터를 활용한 최적 가중치 분석적 결과 도출

**주요 결과**:
- 최대 대수적 연결성의 상한은 연결 패턴과 무관하게 특정 정칙(regularity) 조건에서만 도달 가능
- 연결 제약이 없을 때 Fiedler 벡터 성분으로 최적 가중치 특성 분석적으로 규명
- 제한된 인터링크 배치를 위한 Fiedler 벡터 기반 휴리스틱 방법 제안

## 초록 (원문)

Abstract The second smallest eigenvalue of the Laplacian matrix, known as algebraic connectivity, determines many network properties. This paper investigates the optimal design of interconnections that maximizes algebraic connectivity in multilayer networks. We identify an upper bound for maximum algebraic connectivity for total weight below a threshold, independent of interconnections pattern, and only attainable with a particular regularity condition. For efficient numerical approaches in regions of no analytical solution, we cast the problem into a convex framework and an equivalent graph embedding problem associated with the optimum diffusion phases in the multilayer. Allowing more general settings for interconnections entails regions of multiple transitions, giving more diverse diffusion phases than the more studied one-toone interconnection case. When there is no restriction on the interconnection pattern, we derive several analytical results characterizing the optimal weights using individual Fiedler vectors. We use the ratio of algebraic connectivity and layer sizes to explain the results. Finally, we study the placement of a limited number of interlinks heuristically, guided by each layer’s Fiedler vector components.

## 키워드

Computer science, Algebraic number, Mathematics, Artificial intelligence

## 위키 연관

- [[pages/concepts/multilayer_network|다층 네트워크]]

## 메모

