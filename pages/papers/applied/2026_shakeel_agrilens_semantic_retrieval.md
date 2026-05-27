---
title: "AgriLens: Semantic Retrieval in Agricultural Texts Using Topic Modeling and Language Models"
authors: ['Heba Shakeel', 'Tanvir Ahmad', 'Tanya Liyaqat', 'Chandni Saxena']
year: 2026
venue: "ArXiv.org"
tags: ['Computational and Text Analysis Methods', 'Topic Modeling', 'Information Retrieval and Search Behavior']
source: raw/applied/applied_2026_AgriLens_Semantic_Retriev_nodoi.md
---

# AgriLens: Semantic Retrieval in Agricultural Texts Using Topic Modeling and Language Models
**제목(한글)**: AgriLens: 토픽 모델링 및 언어 모델을 활용한 농업 텍스트의 의미론적 검색

## 한국어 요약

**연구질문**: 레이블된 데이터가 부족한 농업 도메인의 대용량 비정형 텍스트에서 해석 가능한 주제 추출, 제로샷 토픽 레이블링, 의미 기반 검색을 통합적으로 수행하는 프레임워크를 어떻게 설계할 수 있는가?

**방법론**:
- BERTopic을 활용하여 의미론적으로 일관된 토픽 추출 수행
- 각 토픽을 구조화된 프롬프트로 변환하여 언어 모델이 제로샷 방식으로 의미 있는 토픽 레이블과 요약을 생성하도록 설계
- 밀집 임베딩(Dense embedding)과 벡터 검색(Vector search)을 통한 문서 탐색 지원 및 주제 일관성과 편향 측정을 위한 전용 평가 모듈 구현

**주요 결과**:
- 레이블된 학습 데이터가 제한된 특수 도메인에서도 해석 가능하고 확장 가능한 정보 접근 방식을 실현하는 통합 프레임워크를 성공적으로 구축
- 농업 특화 텍스트에 대해 주제 일관성을 유지하면서 제로샷 레이블링이 효과적으로 작동함을 검증

**저자**: Heba Shakeel; Tanvir Ahmad; Tanya Liyaqat; Chandni Saxena
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-01-13
**DOI**: 

## 초록 (원문)

As the volume of unstructured text continues to grow across domains, there is an urgent need for scalable methods that enable interpretable organization, summarization, and retrieval of information. This work presents a unified framework for interpretable topic modeling, zero-shot topic labeling, and topic-guided semantic retrieval over large agricultural text corpora. Leveraging BERTopic, we extract semantically coherent topics. Each topic is converted into a structured prompt, enabling a language model to generate meaningful topic labels and summaries in a zero-shot manner. Querying and document exploration are supported via dense embeddings and vector search, while a dedicated evaluation module assesses topical coherence and bias. This framework supports scalable and interpretable information access in specialized domains where labeled data is limited.

## 키워드

Topic model, Coherence (philosophical gambling strategy), Scalability, Language model, Vector space model, Question answering, Semantics (computer science), Document retrieval

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]
- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모

