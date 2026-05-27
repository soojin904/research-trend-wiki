---
title: "The Effect of Document Selection on Query-focused Text Analysis"
authors: ['Sandesh S Rangreji', 'Mian Zhong', 'Anjalie Field']
year: 2026
venue: "arXiv (Cornell University)"
tags: ['Information Retrieval and Search Behavior', 'Biomedical Text Mining and Ontologies', 'Computational and Text Analysis Methods']
source: raw/applied/applied_2026_The_Effect_of_Document_Se_arxiv_2604_12099.md
---

# The Effect of Document Selection on Query-focused Text Analysis

**제목(한글)**: 쿼리 중심 텍스트 분석에서 문서 선택 전략이 분석 결과에 미치는 영향

## 한국어 요약

**연구질문**: 연구 목적에 따라 분석 대상 문서 코퍼스를 선별할 때, 다양한 문서 선택 전략(무작위 선택부터 하이브리드 검색까지)이 토픽 모델링 결과에 어떠한 방식으로 영향을 미치는가?

**방법론**:
- 7가지 문서 선택 방법(무작위, TF-IDF 검색, 의미론적 검색, 하이브리드 검색 등) 체계적 비교 평가
- LDA, BERTopic, TopicGPT, HiCode 등 4가지 토픽 분석 방법에 적용하여 26개의 개방형 쿼리 실험 수행
- 2개의 서로 다른 데이터셋을 활용한 교차 검증

**주요 결과**:
- 의미론적 검색(Semantic Retrieval) 또는 하이브리드 검색 방식이 대부분의 설정에서 가장 안정적이고 우수한 성능을 보임
- 문서 선택은 단순한 실용적 필요가 아닌 방법론적 의사결정으로 다루어야 함을 확인하고, 이를 위한 체계적 평가 프레임워크 제시

**저자**: Sandesh S Rangreji; Mian Zhong; Anjalie Field
**출처**: arXiv (Cornell University), Vol.None
**발행일**: 2026-04-13
**DOI**: https://doi.org/10.48550/arxiv.2604.12099

## 초록 (원문)

Analyses of document collections often require selecting what data to analyze, as not all documents are relevant to a particular research question and computational constraints preclude analyzing all documents, yet little work has examined effects of selection strategy choices. We systematically evaluate seven selection methods (from random selection to hybrid retrieval) on outputs from four text analyses methods (LDA, BERTopic, TopicGPT, HiCode) over two datasets with 26 open-ended queries. Our evaluation reveals practice guidance: semantic or hybrid retrieval offer strong go-to approaches that avoid the pitfalls of weaker selection strategies and the unnecessary compute overhead of more complicated ones. Overall, our evaluation framework establishes data selection as a methodological decision, rather than a practical necessity, inviting the development of new strategies.

## 키워드

Selection (genetic algorithm), Document retrieval, Overhead (engineering), Feature selection, Semantics (computer science), Question answering

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]
- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모

