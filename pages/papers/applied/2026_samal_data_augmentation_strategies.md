---
title: "Data augmentation strategies in transfer learning for large language models for enhancing clinical text analysis"
authors: ['Apurba Kumar Samal', 'V. Subramaniyam', 'Tarun Mathur', 'Anand Kiran', 'Pankaj Tyagi', 'Uma Shanker Tiwary', 'Pritish Kumar Varadwaj']
year: 2026
venue: "Intelligent Data Analysis"
tags: ['Topic Modeling', 'Biomedical Text Mining and Ontologies', 'Machine Learning in Healthcare']
source: raw/applied/applied_2026_Data_augmentation_strateg_1088467x261433365.md
---

# Data augmentation strategies in transfer learning for large language models for enhancing clinical text analysis
**제목(한글)**: 임상 텍스트 분석 성능 향상을 위한 거대 언어 모델 전이 학습 내 데이터 증강 전략

**저자**: Apurba Kumar Samal; V. Subramaniyam; Tarun Mathur; Anand Kiran; Pankaj Tyagi; Uma Shanker Tiwary; Pritish Kumar Varadwaj
**출처**: Intelligent Data Analysis, Vol.None
**발행일**: 2026-04-01
**DOI**: https://doi.org/10.1177/1088467x261433365

## 한국어 요약

**연구질문**: 의학 용어의 복잡성과 임상 레이블 데이터 부족 한계를 극복하고, 임상 문헌에서 유용한 비정형 데이터를 정밀하게 추출하기 위해 데이터 증강 전략을 결합한 LLM 전이 학습을 어떻게 최적화할 수 있는가?

**방법론**:
- 임상 전문 도메인의 의미적 네트워크 규격(UMLS)을 준수하는 텍스트 증강 프레임워크 구축
- 사전 정의된 추출 규칙 없이 기계 학습을 수행하기 위해 LLM 기반 전이학습(Transfer Learning) 설계 및 고유 의학 전문 용어 코퍼스 적용
- 텍스트 증강 전후의 관계 정보 추출 모델 F1 점수 비교 평가

**주요 결과**:
- 데이터 증강 전략을 융합한 LLM 전이학습 모델이 수동 규칙 생성 모델을 대체할 수 있을 정도로 높은 정보 추출 정확도를 확보
- 소규모 임상 텍스트 데이터셋에서도 관계 정밀도와 F1 스코어가 대폭 개선되어 임상 문헌 통합 분석의 자동화 수준을 제고함


## 초록 (원문)

The vast volume and complexity of clinical research articles make it challenging for individuals to efficiently access and analyze the data. To tackle this issue, Artificial Intelligence (AI) and Natural Language Processing (NLP) are becoming invaluable for managing unstructured data. The primary obstacles are the scarcity of high-quality labeled data and the specialized terminology in healthcare, which differs significantly from Standard English. Historically, conventional healthcare information extraction systems have heavily relied on human involvement to manually establish extraction rules or create tagged training examples. However, given the enormous amount of data available online and the extensive and ambiguous relationships of interest, it has become essential to move away from models dependent on predefined relationships and high-quality labeled data for information extraction. This proposed study implements a framework based on an AI and NLP large language model with data augmentation strategies while adhering to the semantic network of the healthcare domain. The models demonstrate a substantial improvement in the F1-score.

## 키워드

Terminology, Language model, Information extraction, Natural language, Transfer of learning, Key (lock), Semantics (computer science), Unified Medical Language System

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]
- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모

