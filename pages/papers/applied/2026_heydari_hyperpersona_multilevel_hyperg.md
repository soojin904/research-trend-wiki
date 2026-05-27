---
title: "HyperPersona: A Multi-Level Hypergraph Framework for Text-Based Automatic Personality Prediction"
authors: ['Sina Heydari', 'Majid Ramezani']
year: 2026
venue: "ArXiv.org"
tags: ['Mental Health via Writing', 'Personality Traits and Psychology', 'Topic Modeling']
source: raw/applied/applied_2026_HyperPersona_A_MultiLevel_nodoi.md
---

# HyperPersona: A Multi-Level Hypergraph Framework for Text-Based Automatic Personality Prediction
**제목(한글)**: HyperPersona: 텍스트 기반 자동 성격 예측을 위한 다단계 하이퍼그래프 프레임워크

**저자**: Sina Heydari; Majid Ramezani
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-05-17
**DOI**: 

## 한국어 요약

**연구질문**: 텍스트가 지닌 문서·문장·단어의 계층적 구조를 무시하는 기존 얕은(shallow) 또는 단일 수준 표현 방식을 극복하여, 다단계 텍스트 계층 구조를 하이퍼그래프로 명시적으로 모델링함으로써 자동 성격 예측(APP) 정확도를 향상시킬 수 있는가?

**방법론**:
- 문서·문장·단어의 3계층을 하이퍼그래프로 표현하는 HyperPersona 프레임워크 설계(문서·문장은 하이퍼에지, 단어는 노드)
- 트랜스포머 기반 그래프 인코더를 활용해 언어 계층 내·간 상호작용 학습 및 문맥 민감 특징 표현 생성
- Big Five 성격 차원 데이터셋을 사용한 성능 평가

**주요 결과**:
- HyperPersona는 텍스트만 활용하면서도 다단계 언어 단서를 효과적으로 통합하여 최신 기준 모델들보다 우수한 성격 예측 성능을 달성함
- 자연어에서 인간과 유사한 성격 추론을 위해 텍스트 계층 구조의 명시적 모델링이 핵심 역할을 함을 실증함

## 초록 (원문)

As a modern commodity, language has become a vast repository of socially and psychologically significant traits and concepts, reflecting the ways people encode pattern of thoughts, behaviors, and emotions into words. Text-based Automatic Personality Prediction (APP), seeks to infer personality from linguistic behavior, offering a scalable alternative to traditional psychometric assessments. Although text is inherently hierarchical, with the document-level capturing global features, the sentence-level encoding local semantics, and the word-level providing fine-grained lexical information, most existing approaches rely on shallow, sequential, or single-level representations that ignore the multi-level structure of written language. To address this, we propose HyperPersona, a framework that explicitly models the hierarchical organization of text (document, sentence, and word) through hypergraph structure, where a document and its sentences are represented as hyperedges, and the words are represented as nodes, enabling joint modeling of global, local, and lexical dependencies of text. Followed by a transformer-based graph encoder that learns interactions within and across these linguistic layers, yielding context-sensitive and structurally grounded feature representations for personality prediction. Experiments on the Big Five personality dimensions show that, while relying solely on text, HyperPersona effectively integrates multi-level linguistic cues, achieving superior performance compared to state-of-the-art baselines. These findings underscore the critical role of textual hierarchy in advancing human-like personality inference from natural language.

## 키워드

Personality, Inference, Hierarchy, Hypergraph, Big Five personality traits, ENCODE, Feature (linguistics), Encoder

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

