---
title: "Breadth, depth, and flux of course-prerequisite networks"
authors: ['Konstantin M. Zuev', 'Pavlos Stavrinides']
year: 2025
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'Topological and Geometric Data Analysis', 'Advanced Graph Neural Networks']
source: raw/2025_openalex_Breadth_depth_and_flux_of_courseprerequisite_nws_2025_10013.md
---

# Breadth, depth, and flux of course-prerequisite networks
**제목(한글)**: 교과목 선수 네트워크의 폭, 깊이, 흐름

**저자**: Konstantin M. Zuev; Pavlos Stavrinides
**출처**: Network Science, Vol.13
**발행일**: 2025-01-01
**DOI**: https://doi.org/10.1017/nws.2025.10013

## 한국어 요약

**연구질문**: 교과목 선수 네트워크(CPN, Course-Prerequisite Network)의 거시적(macro-scale) 비교를 위한 새로운 전역 지표를 어떻게 정의하고 적용할 수 있는가?

**방법론**:
- 위상적 계층화(topological stratification) 개념에 기반한 폭(breadth)·깊이(depth)·흐름(flux) 세 가지 전역 지표 정의
- 유향 비순환 그래프(DAG)의 이행적 축소(transitive reduction) 불변 지표 설계
- 사이프러스 공과대학, 캘리포니아 공과대학, 존스홉킨스 대학 3개 실제 CPN에 적용

**주요 결과**:
- 세 지표 모두 이행적 축소에 불변하며 교과과정 거시 비교 가능
- 대학별 교과과정 구조의 차이를 세 지표로 정량화할 수 있음을 실증
- 교과과정 설계, 졸업 시간 분포 분석, 지식 흐름 강도 측정에 활용 가능

## 초록 (원문)

Abstract Course-prerequisite networks (CPNs) are directed acyclic graphs that model complex academic curricula by representing courses as nodes and dependencies between them as directed links. These networks are indispensable tools for visualizing, studying, and understanding curricula. For example, CPNs can be used to detect important courses, improve advising, guide curriculum design, analyze graduation time distributions, and quantify the strength of knowledge flow between different university departments. However, most CPN analyses to date have focused only on micro- and meso-scale properties. To fill this gap, we define and study three new global CPN measures: breadth, depth, and flux. All three measures are invariant under transitive reduction and are based on the concept of topological stratification, which generalizes topological ordering in directed acyclic graphs. These measures can be used for macro-scale comparison of different CPNs. We illustrate the new measures numerically by applying them to three real and synthetic CPNs from three universities: the Cyprus University of Technology, the California Institute of Technology, and Johns Hopkins University. The CPN data analyzed in this paper are publicly available in a GitHub repository.

## 키워드

Transitive relation, Directed acyclic graph, Curriculum, Graduation (instrument), Invariant (physics), Topological sorting, Directed graph

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

