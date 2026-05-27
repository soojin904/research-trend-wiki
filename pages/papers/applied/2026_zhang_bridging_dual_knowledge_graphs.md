---
title: "Bridging dual knowledge graphs for multi-hop question answering in construction safety"
authors: ['Yuxin Zhang', 'Xi Wang', 'Mo Hu', 'Zhenyu Zhang']
year: 2026
venue: "Automation in Construction"
tags: ['Topic Modeling', 'Advanced Graph Neural Networks', 'Biomedical Text Mining and Ontologies']
source: raw/applied/applied_2026_Bridging_dual_knowledge_g_j_autcon_2026_106794.md
---

# Bridging dual knowledge graphs for multi-hop question answering in construction safety
**제목(한글)**: 건설 안전 분야의 멀티홉(Multi-hop) 질의응답을 위한 이중 지식 그래프 연계 기술

**저자**: Yuxin Zhang; Xi Wang; Mo Hu; Zhenyu Zhang
**출처**: Automation in Construction, Vol.183, pp.106794-106794
**발행일**: 2026-01-26
**DOI**: https://doi.org/10.1016/j.autcon.2026.106794

## 한국어 요약

**연구질문**: 복잡한 건설 안전 관련 법률 및 규정 텍스트에서 여러 조항에 걸친 논리 합성이 필요한 멀티홉 질의응답의 정확도를 높이기 위해 언어 관계와 문서 구조를 모두 결합할 수 있는가?

**방법론**:
- 개체(Entity) 그래프와 문서(Document) 구조 그래프를 통합한 이중 그래프 기반의 RAG 시스템인 BifrostRAG 설계
- 그래프 탐색(traversal)과 벡터 공간 내 시맨틱 매칭을 결합한 하이브리드 정보 검색 메커니즘 구축
- 미 노동안전보건청(OSHA) 규정 관련 멀티홉 질의 데이터셋을 활용한 실험

**주요 결과**:
- BifrostRAG 모델이 OSHA 멀티홉 질의 테스트에서 정밀도 92.8%, 재현율 85.5%, F1-Score 87.3%를 달성하여 기존 RAG 모델 성능을 대폭 능가
- 복잡한 공학 및 도메인 기술 규제 문서를 탐색하는 LLM 기반 자동 적합성 평가의 효과적인 표준 청사진(blueprint) 제공


## 초록 (원문)

Information retrieval and question answering from safety regulations are essential for automated construction compliance checking but are hindered by the linguistic and structural complexity of regulatory text. Many queries are multi-hop, requiring synthesis across interlinked clauses. To address the challenge, this paper introduces BifrostRAG, a dual-graph retrieval-augmented generation (RAG) system that models both linguistic relationships and document structure. The proposed architecture supports a hybrid retrieval mechanism that combines graph traversal with vector-based semantic search, enabling large language models to reason over both the content and the structure of the text. On a multi-hop question dataset, BifrostRAG achieves 92.8% precision, 85.5% recall, and an F1 score of 87.3%. These results significantly outperform vector-only and graph-only RAG baselines, establishing BifrostRAG as a robust knowledge engine for LLM-driven compliance checking. The dual-graph, hybrid retrieval mechanism presented in this paper offers a transferable blueprint for navigating complex technical documents across knowledge-intensive engineering domains. • BifrostRAG unifies Entity and Document graphs for multi-hop regulatory QA. • Hybrid retrieval couples semantic search with structural traversal. • An LLM-assisted pipeline builds dual graphs with an incremental entity refiner. • BifrostRAG achieved 92.8% P, 85.5% R, 87.3% F1 on OSHA multi-hop questions.

## 키워드

Bridging (networking), Question answering, Blueprint, Dual (grammatical number), Pipeline (software), Tree traversal, Scheme (mathematics), Natural language

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

