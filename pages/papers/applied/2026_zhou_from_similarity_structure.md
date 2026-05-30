---
title: "From Similarity to Structure: Training-free LLM Context Compression with Hybrid Graph Priors"
authors: ['Yitian Zhou', 'Chaoning Zhang', 'Jiaquan Zhang', 'Zhenzhen Huang', 'Jinyu Guo', 'Sung-Ho Bae', 'Lik?Hang Lee', 'Caiyan Qin', 'Yang Yang']
year: 2026
venue: "ArXiv.org"
tags: ['Natural Language Processing Techniques', 'Topic Modeling', 'Machine Learning in Healthcare']
source: raw/applied/applied_2026_From_Similarity_to_Struct_nodoi.md
---

# From Similarity to Structure: Training-free LLM Context Compression with Hybrid Graph Priors

**제목(한글)**: 유사성에서 구조로: 하이브리드 그래프 사전 지식을 활용한 훈련 없는 LLM 컨텍스트 압축

## 한국어 요약

**연구질문**: 기존 LLM 컨텍스트 압축 방식들이 토큰 예산 제약 하에 작업 관련성, 주제 범위, 문장 간 일관성을 동시에 유지하는 데 어려움을 겪는 문제를 어떻게 해결할 수 있는가?

**방법론**:
- 구조적 그래프 사전 지식에 기반한 훈련 없는 모델 불가지론적(model-agnostic) 압축 프레임워크 제안
- 상호 k-NN 의미론적 엣지와 단거리 순차적 엣지를 결합한 희소 하이브리드 문장 그래프 구축
- 클러스터링을 통한 토픽 스켈레톤 추출
- 작업 관련성, 클러스터 대표성, 브릿지 중심성, 사이클 커버리지 단서를 통합한 해석 가능한 점수를 사용하여 문장 순위화
- 중복 억제 기능을 포함한 예산 책정된 탐욕적 선택(budgeted greedy selection)을 통해 원본 순서대로 읽기 쉬운 압축된 컨텍스트 생성

**주요 결과**:
- 제안하는 접근 방식은 강력한 추출 및 요약 기준선(baselines)과 경쟁할 만한 성능을 보임.
- 특히 긴 문서 벤치마크(long-document benchmarks)에서 더 큰 개선 효과를 입증함.

**저자**: < >

## ѱ 

****: <>

****:
- <׸>

**ֿ **:
- <׸>


**저자**: Yitian Zhou; Chaoning Zhang; Jiaquan Zhang; Zhenzhen Huang; Jinyu Guo; Sung-Ho Bae; Lik?Hang Lee; Caiyan Qin; Yang Yang
**저자**: ArXiv.org, Vol.None
**저자**: 2026-04-25
**저자**: ## 초록 (원문)

Long-context large language models remain computationally expensive to run and often fail to reliably process very long inputs, which makes context compression an important component of many systems. Existing compression approaches typically rely on trained compressors, dense retrieval-style selection, or heuristic trimming, and they often struggle to jointly preserve task relevance, topic coverage, and cross-sentence coherence under a strict token budget. To address this, we propose a training-free and model-agnostic compression framework that selects a compact set of sentences guided by structural graph priors. Our method constructs a sparse hybrid sentence graph that combines mutual k-NN semantic edges with short-range sequential edges, extracts a topic skeleton via clustering, and ranks sentences using an interpretable score that integrates task relevance, cluster representativeness, bridge centrality, and a cycle coverage cue. A budgeted greedy selection with redundancy suppression then produces a readable compressed context in original order. Experimental results on four datasets show that our approach is competitive with strong extractive and abstractive baselines, demonstrating larger gains on long-document benchmarks.

## 키워드

Redundancy (engineering), Graph, Set (abstract data type), Context (archaeology), Coherence (philosophical gambling strategy), Heuristic, Data compression, Pattern recognition (psychology)

## 위키 연관

- [[pages/methods/topic_modeling|?픽모델?]

## 메모


