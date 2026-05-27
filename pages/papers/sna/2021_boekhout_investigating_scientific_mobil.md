---
title: "Investigating scientific mobility in co-authorship networks using multilayer temporal motifs"
authors: ['Hanjo D. Boekhout', 'Vincent Traag', 'Frank W. Takes']
year: 2021
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'scientometrics and bibliometrics research', 'Bioinformatics and Genomic Networks']
source: raw/2021_openalex_Investigating_scientific_mobility_in_coauthorship_networks_nws_2021_12.md
---

# Investigating scientific mobility in co-authorship networks using multilayer temporal motifs
**제목(한글)**: 다층 시간적 모티프를 활용한 공저 네트워크에서의 과학자 이동성 연구

**저자**: Hanjo D. Boekhout; Vincent Traag; Frank W. Takes
**출처**: Network Science, Vol.9, pp.354–386
**발행일**: 2021-09-01
**DOI**: https://doi.org/10.1017/nws.2021.12

## 한국어 요약

**연구질문**: 과학적 협력(collaboration)과 과학자 이동성(scientific mobility)은 어떻게 연관되며, 다층 시간적 모티프(multilayer temporal motif) 분석으로 분야 간 차이를 어떻게 포착할 수 있는가?

**방법론**:
- 다층 시간적 모티프: 노드-엣지의 소규모 반복 패턴 분석
- 동시 발행 논문(concurrent edges) 처리를 위한 효율적 계산 알고리즘 개발
- Web of Science 데이터: 최대 770만 노드(저자), 9,400만 엣지(협력)의 대규모 공저 네트워크

**주요 결과**:
- 국제 협력과 국제 이동성은 상호적으로 영향을 미침
- 인문사회과학(SSH) 학자들은 지리적으로 더 먼 저자와 공저하는 경향
- 수학·컴퓨터과학(M&C) 학자들은 기존 지식 네트워크 내에서 지속 협력하는 경향

## 초록 (원문)

Abstract This paper introduces a framework for understanding complex temporal interaction patterns in large-scale scientific collaboration networks. In particular, we investigate how two key concepts in science studies, scientific collaboration and scientific mobility, are related and possibly differ between fields. We do so by analyzing multilayer temporal motifs: small recurring configurations of nodes and edges. Driven by the problem that many papers share the same publication year, we first provide a methodological contribution: an efficient counting algorithm for multilayer temporal motifs with concurrent edges. Next, we introduce a systematic categorization of the multilayer temporal motifs, such that each category reflects a pattern of behavior relevant to scientific collaboration and mobility. Here, a key question concerns the causal direction: does mobility lead to collaboration or vice versa? Applying this framework to scientific collaboration networks extracted from Web of Science (WoS) consisting of up to 7.7 million nodes (authors) and 94 million edges (collaborations), we find that international collaboration and international mobility reciprocally influence one another. Additionally, we find that Social sciences &amp; Humanities (SSH) scholars co-author to a greater extent with authors at a distance, while Mathematics &amp; Computer science (M&amp;C) scholars tend to continue to collaborate within the established knowledge network and organization.

## 키워드

Data science, Computer science, Categorization, Key (lock), Network science, Theoretical computer science, World Wide Web, Artificial intelligence

## 위키 연관

- [[pages/concepts/multilayer_network|다층 네트워크]]
- [[pages/concepts/personal_network|퍼스널 네트워크]]

## 메모

