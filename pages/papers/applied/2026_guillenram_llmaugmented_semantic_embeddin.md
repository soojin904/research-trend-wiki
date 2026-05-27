---
title: "LLM-augmented semantic embeddings enable Cross-Lingual mapping of medical procedure terms"
authors: ['Hugo Guillen-Ramirez', 'Karen Triep', 'Christophe Gaudet-Blavignac', 'Baljit Phull', 'GUIDO BELDI', 'Olga Endrich']
year: 2026
venue: "Scientific Reports"
tags: ['Machine Learning in Healthcare', 'Biomedical Text Mining and Ontologies', 'Topic Modeling']
source: raw/applied/applied_2026_LLMaugmented_semantic_emb_s41598_025_34778_7.md
---

# LLM-augmented semantic embeddings enable Cross-Lingual mapping of medical procedure terms
**제목(한글)**: LLM 강화 의미론적 임베딩을 통한 의료 처치 용어의 다국어 매핑

**저자**: Hugo Guillen-Ramirez; Karen Triep; Christophe Gaudet-Blavignac; Baljit Phull; GUIDO BELDI; Olga Endrich
**출처**: Scientific Reports, Vol.16, pp.4660-4660
**발행일**: 2026-01-09
**DOI**: https://doi.org/10.1038/s41598-025-34778-7

## 한국어 요약

**연구질문**: 국가나 언어권에 따라 극도로 상이하고 표준화가 어려운 비영어권 의료 처치(Surgical and interventional procedures) 분류 코드를, 기계 번역 한계를 넘어 하나의 공통 다국어 임베딩 공간으로 어떻게 정확히 자동 정렬할 수 있는가?

**방법론**:
- 대형 언어 모델(LLMs)을 활용해 다국어 임상 전문 용어 번역 및 의미 특징 추출 파이프라인(MAP-CARE) 개발
- 영어, German, 프랑스어, 이탈리아어 등 이종 언어 간 처치 카테고리 매핑 유사도(Acc@5) 정량 평가
- CSV Terminology 파일 확장성 및 실제 2개 다른 국가 간의 표준 의료 처치 코드셋 정렬 실험 수행

**주요 결과**:
- MAP-CARE 프레임워크는 유럽 주요 4개 언어 간 의료 코드 번역 매핑에서 Acc@5 = 0.90이라는 높은 정확성을 성취함
- 극도로 미세하고 의미론적 겹침이 큰 국가 간 코드 체계 정렬에서도 53.8% 이상의 정확한 일치 매칭을 보여주어 글로벌 보건 데이터 통합의 실용적 인프라를 개방형으로 구축함


## 초록 (원문)

Cross-lingual information retrieval limits global exchange of data because of the high diversity in the methods to classify, document and encode medical procedures. Traditional keyword-based or single-language systems are not able to align data from surgical and interventional procedures, especially from non-English healthcare systems. This study aims to develop a pipeline for cross-lingual retrieval and integration of medical procedures data. MAP-CARE is a novel framework that leverages Large Language Models (LLMs) for translating and transforming medical procedures into a unified multilingual embedding space. Semantic embeddings are used to enhance retrieval accuracy and interoperability across languages and healthcare systems. MAP-CARE demonstrated high accuracy in the translation and mapping of clinical terms. Its cross-language translation performance proved robust, achieving up to Acc@5 = 0.90 in translating procedure classification codes across English, German, French, and Italian. The cross-classification mapping workflow also showed high accuracy in aligning two different national procedure classifications, with exact and near matches exceeding 53.8% at the most granular level. MAP-CARE offers a flexible, scalable, and robust solution for the multilingual and cross-system integration of medical procedural data. Its innovative use of large language models (LLMs) combined with semantic embeddings sets a new standard for the accessibility and utility of multilingual medical information. The framework is designed for easy extension from a terminology file in CSV format and is publicly available.

## 키워드

Unified Medical Language System, Workflow, Interoperability, Embedding, Terminology, ENCODE, Semantic integration, Pipeline (software)

## 위키 연관

- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모

