---
title: "BLUEmed: Retrieval-Augmented Multi-Agent Debate for Clinical Error Detection"
authors: ['Saukun Thika You', 'Nguyen Anh Khoa Tran', 'Wesley K. Marizane', 'Hanshu Rao', 'Qiunan Zhang', 'Xiaolei Huang']
year: 2026
venue: "arXiv (Cornell University)"
tags: ['Topic Modeling', 'Biomedical Text Mining and Ontologies', 'Natural Language Processing Techniques']
source: raw/applied/applied_2026_BLUEmed_RetrievalAugmente_nodoi.md
---

# BLUEmed: Retrieval-Augmented Multi-Agent Debate for Clinical Error Detection
**제목(한글)**: BLUEmed: 임상 오류 탐지를 위한 검색 증강 다중 에이전트 토론 프레임워크

## 한국어 요약

**연구질문**: 임상 노트에서 의학 용어 대체 오류(terminology substitution error)를 자동으로 탐지하기 위해 RAG(검색 증강 생성)와 다중 에이전트 토론을 결합한 프레임워크가 단일 에이전트 방식보다 효과적인가?

**방법론**:
- 임상 노트를 서브 쿼리로 분해하고 밀집·희소·온라인 검색으로 소스 분리 증거를 검색하는 하이브리드 RAG 설계
- 두 전문가 에이전트가 독립적으로 분석한 후 의견 불일치 시 구조화된 반론 교환과 교차 소스 중재를 수행하는 다중 에이전트 토론 구조
- 임상 용어 대체 탐지 벤치마크에서 제로샷·퓨샷 프롬프팅과 여러 백본 모델로 평가

**주요 결과**:
- BLUEmed가 퓨샷 프롬프팅에서 정확도 69.13%, ROC-AUC 74.45%, PR-AUC 72.44%를 달성하여 단일 에이전트 RAG 및 토론만 수행한 기준선 모두 능가
- 검색 증강과 구조화된 토론이 상호 보완적이며, 임상 언어 이해력이 충분한 모델에서 최대 효과 확인

**저자**: Saukun Thika You; Nguyen Anh Khoa Tran; Wesley K. Marizane; Hanshu Rao; Qiunan Zhang; Xiaolei Huang
**출처**: arXiv (Cornell University), Vol.None
**발행일**: 2026-04-12
**DOI**: 

## 초록 (원문)

Terminology substitution errors in clinical notes, where one medical term is replaced by a linguistically valid but clinically different term, pose a persistent challenge for automated error detection in healthcare. We introduce BLUEmed, a multi-agent debate framework augmented with hybrid Retrieval-Augmented Generation (RAG) that combines evidence-grounded reasoning with multi-perspective verification for clinical error detection. BLUEmed decomposes each clinical note into focused sub-queries, retrieves source-partitioned evidence through dense, sparse, and online retrieval, and assigns two domain expert agents distinct knowledge bases to produce independent analyses; when the experts disagree, a structured counter-argumentation round and cross-source adjudication resolve the conflict, followed by a cascading safety layer that filters common false-positive patterns. We evaluate BLUEmed on a clinical terminology substitution detection benchmark under both zero-shot and few-shot prompting with multiple backbone models spanning proprietary and open-source families. Experimental results show that BLUEmed achieves the best accuracy (69.13%), ROC-AUC (74.45%), and PR-AUC (72.44%) under few-shot prompting, outperforming both single-agent RAG and debate-only baselines. Further analyses across six backbone models and two prompting strategies confirm that retrieval augmentation and structured debate are complementary, and that the framework benefits most from models with sufficient instruction-following and clinical language understanding.

## 키워드

Terminology, Benchmark (surveying), Domain (mathematical analysis), Substitution (logic), Error detection and correction, SNOMED CT, Adjudication

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

