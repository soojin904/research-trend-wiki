---
title: "Leveraging large language models and embedding representations for enhanced word similarity computation"
authors: ['Xiaohong Peng', 'Hongbin Jiang', 'Jing Chen', 'Mingxin Liu', 'Xiao Chen']
year: 2025
venue: "Scientific Reports"
tags: ['Topic Modeling', 'Sentiment Analysis and Opinion Mining', 'Natural Language Processing Techniques']
source: raw/applied/applied_2025_Leveraging_large_language_s41598_025_31102_1.md
---

# Leveraging large language models and embedding representations for enhanced word similarity computation

**제목(한글)**: LLM과 임베딩 표현을 결합한 향상된 단어 유사도 계산 프레임워크

## 한국어 요약

**연구질문**: LLM의 의미 생성 능력과 임베딩 기반 벡터 표현을 통합하면 단어 유사도 계산의 정확도를 향상시킬 수 있는가?

**방법론**:
- WSLE 프레임워크 제안: LLM 의미 생성 + 딥 시맨틱 임베딩 모듈 통합
- 품사 편향, 중복 예시, 의미적 모호성, 정보 중복성 등 4가지 LLM 한계 해결
- RG65, MC30, YP130, MED38 벤치마크 데이터셋에서 피어슨·스피어먼 상관계수로 평가

**주요 결과**:
- WSLE가 기존 유사도 계산 방법 대비 정확도·강인성에서 유의한 우위
- LLM의 의미 표현 생성 시 발생하는 품사 편향 등 4가지 문제 효과적 완화
- 맥락적으로 풍부한 의미 표현을 통한 단어 유사도 측정 품질 향상

**저자**: Xiaohong Peng; Hongbin Jiang; Jing Chen; Mingxin Liu; Xiao Chen
**출처**: Scientific Reports, Vol.16, pp.1494-1494
**발행일**: 2025-12-08
**DOI**: https://doi.org/10.1038/s41598-025-31102-1

## 초록 (원문)

Current mainstream methods for computing word similarity often struggle to precisely capture the fine-grained semantics of words across different contexts. Particularly, generative semantic representations typically suffer from issues such as part-of-speech bias, semantic ambiguity, redundant exemplars, and informational redundancy, all of which compromise the accuracy of similarity measurements. To address these problems, this paper proposes WSLE, a word similarity computation framework integrating the semantic generation capabilities of large language models (LLMs) with embedding-based vector representations. First, WSLE addresses four common challenges encountered in generating semantic representations using LLMs-part-of-speech bias, redundant exemplars, semantic ambiguity, and informational redundancy. By applying constraints to lexical items, grammatical categories, semantic descriptions, and prompt length, WSLE effectively mitigates these issues, thus enabling LLMs to generate coherent, precise, and contextually rich semantic representations. Second, these generated semantic representations are transformed into high-dimensional vector embeddings via a deep semantic embedding module, facilitating quantitative assessment of semantic similarity between words. Finally, the effectiveness of WSLE is rigorously evaluated through analyses based on Pearson's correlation coefficient (r) and Spearman's rank correlation coefficient (ρ). Experimental results on benchmark datasets, including RG65, MC30, YP130, and MED38, demonstrate that the proposed WSLE framework significantly outperforms existing similarity computation methods, exhibiting notable advantages in accuracy and robustness for word similarity measurement tasks.

## 키워드

Semantic similarity, Word embedding, Similarity (geometry), Semantics (computer science), Word (group theory), Distributional semantics, Embedding, Semantic computing

## 위키 연관

- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모

