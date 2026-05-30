---
title: "The extraction of a brief summary from scientific documents using machine learning methods"
authors: ['Gulden Murzabekova', 'Galiya Mukhamedrakhimova', 'Zhazira Taszhurekova', 'Yerbol Yerbayev', 'Жанагул Доумчариева', 'Valentina Мakhatova', 'Moldir Tolganbaeva', 'Sandugash Serikbayeva']
year: 2025
venue: "Bulletin of Electrical Engineering and Informatics"
tags: ['Biomedical Text Mining and Ontologies', 'Advanced Text Analysis Techniques', 'Topic Modeling']
source: raw/applied/applied_2025_The_extraction_of_a_brief_eei_v14i6_10660.md
---

# The extraction of a brief summary from scientific documents using machine learning methods

**제목(한글)**: 기계 학습 방법을 이용한 과학 문서의 간략한 요약 추출

## 한국어 요약

**연구질문**: 과학 문서에서 효과적인 자동 요약을 위해 기계 학습 기반 접근 방식을 어떻게 개발하고 평가할 수 있는가?

**방법론**:
- 기계 학습 기반 접근 방식 (Machine Learning-based approach)
- 미세 조정된 DistilBART 모델 (Fine-tuned DistilBART model) 활용
- arXiv 리포지토리에서 수집된 12,540개의 과학 논문 대규모 코퍼스 학습
- 토큰화, 불용어 제거, 어간 추출 등의 고급 텍스트 전처리 기법 통합

**주요 결과**:
- 미세 조정된 DistilBART 모델이 높은 요약 성능 달성 (ROUGE-2=0.472, ROUGE-L=0.602)
- 기준 트랜스포머 기반 모델(baseline transformer-based models)을 능가하는 성능
- 학술 연구 외 기술 문서 자동 색인, 디지털 라이브러리 메타데이터 추출, 임베디드 NLP 시스템 실시간 텍스트 처리 등 다양한 분야에 적용 가능성 확인
- 트랜스포머 기반 요약이 과학 지식 발견을 가속화하고 정보 검색 효율성을 향상시킬 잠재력 제시

**저자**: Gulden Murzabekova; Galiya Mukhamedrakhimova; Zhazira Taszhurekova; Yerbol Yerbayev; Жанагул Доумчариева; Valentina Мakhatova; Moldir Tolganbaeva; Sandugash Serikbayeva
**출처**: Bulletin of Electrical Engineering and Informatics, Vol.14, pp.4812-4822
**발행일**: 2025-12-01
**DOI**: https://doi.org/10.11591/eei.v14i6.10660

## 초록 (원문)

This study proposes a machine learning-based approach for automatic summarization of scientific documents using a fine-tuned DistilBART model a lightweight and efficient version of the bidirectional and auto-regressive transformers (BART) architecture. The model was trained on a large corpus of 12,540 scientific articles (2015–2023) collected from the arXiv repository, enabling it to effectively capture domain-specific terminology and structural patterns. The proposed pipeline integrates advanced text preprocessing techniques, including tokenization, stopword removal, and stemming, to enhance the quality of semantic representation. Experimental evaluation demonstrates that the fine-tuned DistilBART achieves high summarization performance, with ROUGE-2=0.472 and ROUGE-L=0.602, outperforming baseline transformer-based models. Unlike conventional approaches, the method shows strong applicability beyond academic research, including automated indexing of technical documentation, metadata extraction in digital libraries, and real-time text processing in embedded natural language processing (NLP) systems. The results highlight the potential of transformer-based summarization to accelerate scientific knowledge discovery and improve the efficiency of information retrieval across various domains.

## 키워드

Automatic summarization, Metadata, Search engine indexing, Preprocessor, Information extraction, Terminology, Pipeline (software), Automatic indexing

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

