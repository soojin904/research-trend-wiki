---
title: "HIF: The hypergraph interchange format for higher-order networks"
authors: ['Martín Coll', 'Cliff Joslyn', 'Nicholas Landry', 'Quintino Francesco Lotito', 'Audun Myers', 'Joshua Pickard', 'Brenda Praggastis', 'Przemysław Szufel']
year: 2025
venue: "Network Science"
tags: ['Advanced Optical Network Technologies', 'Interconnection Networks and Systems', 'Advanced MRI Techniques and Applications']
source: raw/2025_openalex_HIF_The_hypergraph_interchange_format_for_nws_2025_10018.md
---

# HIF: The hypergraph interchange format for higher-order networks
**제목(한글)**: HIF: 고차 네트워크를 위한 하이퍼그래프 교환 형식

**저자**: Martín Coll; Cliff Joslyn; Nicholas Landry; Quintino Francesco Lotito; Audun Myers; Joshua Pickard; Brenda Praggastis; Przemysław Szufel
**출처**: Network Science, Vol.13
**발행일**: 2025-01-01
**DOI**: https://doi.org/10.1017/nws.2025.10018

## 한국어 요약

**연구질문**: 다양한 프로그래밍 언어로 작성된 하이퍼그래프(hypergraph) 소프트웨어 패키지 간 데이터를 원활하게 교환하기 위한 표준화된 형식을 어떻게 설계할 수 있는가?

**방법론**:
- HIF(Hypergraph Interchange Format) JSON 스키마 설계 및 명세 작성
- 비방향 하이퍼그래프, 방향 하이퍼그래프, 추상 단체 복합체(abstract simplicial complex) 지원
- 노드·에지·인시던스 관련 메타데이터 속성 지원 및 주요 소프트웨어 패키지 호환성 시연

**주요 결과**:
- JSON 기반 표준화 형식(HIF)으로 다양한 고차 네트워크 분석 소프트웨어 간 상호운용성 확보
- HIF 준수 예시 데이터셋 및 튜토리얼 제공
- 멀티플렉스·시계열·순서 있는 하이퍼그래프 확장 가능성 탐색 중

## 초록 (원문)

Abstract Many empirical systems contain complex interactions of arbitrary size, representing, for example, chemical reactions, social groups, co-authorship relationships, and ecological dependencies. These interactions are known as higher-order interactions, and the collection of these interactions comprise a higher-order network, or hypergraph. Hypergraphs have established themselves as a popular and versatile mathematical representation of such systems, and a number of software packages written in various programming languages have been designed to analyze these networks. However, the ecosystem of higher-order network analysis software is fragmented due to specialization of each software’s programming interface and compatible data representations. To enable seamless data exchange between higher-order network analysis software packages, we introduce the Hypergraph Interchange Format (HIF), a standardized format for storing higher-order network data. HIF supports multiple types of higher-order networks, including undirected hypergraphs, directed hypergraphs, and abstract simplicial complexes, while actively exploring extensions to represent multiplex hypergraphs, temporal hypergraphs, and ordered hypergraphs. To accommodate the wide variety of metadata used in different contexts, HIF also includes support for attributes associated with nodes, edges, and incidences. This initiative is a collaborative effort involving authors, maintainers, and contributors from prominent hypergraph software packages. This project introduces a JSON schema with corresponding documentation and unit tests, example HIF-compliant datasets, and tutorials demonstrating the use of HIF with several popular higher-order network analysis software packages.

## 키워드

Hypergraph, JSON, Software, Metadata, Documentation, Application programming interface, Software framework, Component-based software engineering

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

