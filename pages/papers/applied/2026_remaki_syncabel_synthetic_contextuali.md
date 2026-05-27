---
title: "SynCABEL: Synthetic Contextualized Augmentation for Biomedical Entity Linking"
authors: ['Adam Remaki', 'Christel Gérardin', 'Eulàlia Farré-Maduell', 'Martin Krallinger', 'Xavier Tannier']
year: 2026
venue: "ArXiv.org"
tags: ['Machine Learning in Healthcare', 'Topic Modeling', 'Genomics and Rare Diseases']
source: raw/applied/applied_2026_SynCABEL_Synthetic_Contex_nodoi.md
---

# SynCABEL: Synthetic Contextualized Augmentation for Biomedical Entity Linking

**제목(한글)**: SynCABEL: 의생명 개체 연결(Entity Linking)을 위한 합성 문맥화 증강 프레임워크

## 한국어 요약

**연구질문**: 지도 학습 기반 의생명 개체 연결(BEL) 시스템의 핵심 병목인 전문가 어노테이션 학습 데이터 부족 문제를 LLM 기반 합성 데이터 생성을 통해 어떻게 해결할 수 있는가?

**방법론**:
- LLM을 활용하여 대상 지식베이스 내 모든 후보 개념에 대한 문맥 풍부한 합성 학습 예시 자동 생성
- 디코더 전용(Decoder-only) 모델과 유도 추론(Guided Inference)을 결합하여 영어(MedMentions), 프랑스어(QUAERO), 스페인어(SPACCC)의 3개 다국어 벤치마크에서 평가
- 전문가 레이블 데이터 없이도 신뢰성 있는 예측을 위한 LLM-as-a-judge 프로토콜 도입

**주요 결과**:
- 3개 다국어 벤치마크 모두에서 새로운 최첨단(State-of-the-art) 성능을 달성함
- 완전한 인간 레이블 감독 대비 최대 60%의 어노테이션 데이터만으로도 동등한 성능에 도달하여 전문가 레이블링 의존도를 대폭 감축함

**저자**: Adam Remaki; Christel Gérardin; Eulàlia Farré-Maduell; Martin Krallinger; Xavier Tannier
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-01-27
**DOI**: 

## 초록 (원문)

We present SynCABEL (Synthetic Contextualized Augmentation for Biomedical Entity Linking), a framework that addresses a central bottleneck in supervised biomedical entity linking (BEL): the scarcity of expert-annotated training data. SynCABEL leverages large language models to generate context-rich synthetic training examples for all candidate concepts in a target knowledge base, providing broad supervision without manual annotation. We demonstrate that SynCABEL, when combined with decoder-only models and guided inference, establishes new state-of-the-art results across three widely used multilingual benchmarks: MedMentions for English, QUAERO for French, and SPACCC for Spanish. Evaluating data efficiency, we show that SynCABEL reaches the performance of full human supervision using up to 60% less annotated data, substantially reducing reliance on labor-intensive and costly expert labeling. Finally, acknowledging that standard evaluation based on exact code matching often underestimates clinically valid predictions due to ontology redundancy, we introduce an LLM-as-a-judge protocol. This analysis reveals that SynCABEL significantly improves the rate of clinically valid predictions. Our synthetic datasets, models, and code are released to support reproducibility and future research.

## 키워드

Inference, Bottleneck, Code (set theory), Matching (statistics), Ontology, Training set, Reuse

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

