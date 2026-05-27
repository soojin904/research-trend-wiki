---
title: "A Hybrid LLM and Embedding-Based Approach for Biomedical Concept Normalization in Clinical and Social Media Data"
authors: ['Iram Azam']
year: 2026
venue: "Purdue"
tags: ['Topic Modeling', 'Machine Learning in Healthcare', 'Mental Health via Writing']
source: raw/applied/applied_2026_A_Hybrid_LLM_and_Embeddin_pgs_32193870_v1.md
---

# A Hybrid LLM and Embedding-Based Approach for Biomedical Concept Normalization in Clinical and Social Media Data
**제목(한글)**: 임상 및 소셜 미디어 데이터 내 생물의학 개념 표준화를 위한 하이브리드 LLM 및 임베딩 기반 접근법

**저자**: Iram Azam
**출처**: Purdue, Vol.None
**발행일**: 2026-05-07
**DOI**: https://doi.org/10.25394/pgs.32193870.v1

## 한국어 요약

**연구질문**: 의료진용 임상 보고서의 약어와 일반 소셜 미디어 트윗의 구어체 및 오탈자가 포함된 의료 표현들을 통합 의료 언어 시스템(UMLS)의 표준 개념으로 정확하게 매핑하는 방법은 무엇인가?

**방법론**:
- SapBERT 임베딩 및 FAISS 백엔드 검색 모델 구축
- 프라이어 단계로 LLM을 사용해 구어체 텍스트를 표준 의학 용어로 가독성 정규화를 거치게 한 뒤, 매핑 모델을 수행하는 하이브리드 프레임워크 구축
- 3,144개 임상 구문 및 102개 트윗 구문으로 성능 검증

**주요 결과**:
- 임상 데이터에서 정확도 85.8%(F1=0.924)로 exact matching 기법 등을 크게 앞섬
- 소셜 미디어 트윗 데이터는 LLM 표준화 보정을 거치자 정확도가 기존 23.5%에서 98.0%로 수직 상승하여 이원화된 데이터 통합에 탁월한 해법을 제시


## 초록 (원문)

Biomedical concept normalization (BCN) is a fundamental task in natural language processing (NLP) that maps diverse health-related expressions to standardized concepts within biomedical knowledge bases such as the Unified Medical Language System (UMLS). This process is essential for supporting clinical decision-making, public health surveillance, and large-scale biomedical data integration. However, accurate normalization remains challenging due to substantial linguistic variability across data sources. Clinical text often contains domain-specific terminology and abbreviations, whereas social media data introduces informal language, misspellings, paraphrases, and metaphorical expressions that limit the effectiveness of traditional lexical approaches.This study proposes a unified hybrid framework that integrates large language models (LLMs) with biomedical embeddings to address these challenges. The approach leverages SapBERT embeddings and FAISS-based similarity search for semantic retrieval over UMLS concepts. LLMs are used to generate medically grounded preferred terms (PTs) from informal expressions, reducing linguistic variability prior to embedding-based retrieval.The framework is evaluated on COVID-19–related datasets, including free text in electronic health record (EHR) and multiple Twitter (X) datasets. For clinical normalization (3,144 phrases), the embedding-based approach achieved an accuracy of 0.858 (F1 = 0.924), outperforming exact string matching (0.679) and MetaMap Lite (0.579). For Twitter phrase-level normalization (102 phrases), performance improved from 0.235 (string matching) and 0.118 (MetaMap Lite) to as high as 0.980 accuracy and 0.990 F1 using LLM-assisted normalization.To demonstrate applicability to unstructured real-world data, the framework was extended to full tweets (600 tweets), where LLM-based symptom extraction was incorporated as a prior step, enabling biomedical entity linking (BEL). The symptom extraction component achieved micro-level F1-scores of 0.906 (exact match) and 0.930 (semantic match).Overall, the results demonstrate that embedding-based semantic retrieval improves normalization in clinical text, while LLM-assisted linguistic standardization is critical for handling informal social media expressions. The proposed hybrid framework provides an accurate and robust solution for biomedical concept normalization and entity linking across heterogeneous data sources, supporting applications in public health informatics and biomedical text analysis.

## 키워드

Unified Medical Language System, Normalization (sociology), Terminology, Social media, Named-entity recognition, Information extraction, Natural language, Biomedical text mining

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

