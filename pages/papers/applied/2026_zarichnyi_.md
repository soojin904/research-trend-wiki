---
title: "РЕКОМЕНДАЦІЯ СЕРВІСУ НА ОСНОВІ ГІБРИДНОЇ МОДЕЛІ СЕМАНТИЧНОГО ПОШУКУ"
authors: ['Yaroslav Zarichnyi']
year: 2026
venue: "Системи управління навігації та зв’язку Збірник наукових праць"
tags: ['Recommender Systems and Techniques', 'Service-Oriented Architecture and Web Services', 'Sentiment Analysis and Opinion Mining']
source: raw/applied/applied_2026__sunz_2026_1_077.md
---

# РЕКОМЕНДАЦІЯ СЕРВІСУ НА ОСНОВІ ГІБРИДНОЇ МОДЕЛІ СЕМАНТИЧНОГО ПОШУКУ
**제목(한글)**: 하이브리드 시맨틱 검색 모델 기반 서비스 추천 기법 연구

**저자**: Yaroslav Zarichnyi
**출처**: Системи управління навігації та зв’язку Збірник наукових праць, Vol.1, pp.77-81
**발행일**: 2026-02-27
**DOI**: https://doi.org/10.26906/sunz.2026.1.077

## 한국어 요약

**연구질문**: 전통적 키워드 검색의 어휘적 갭(lexical gap)과 문맥 이해 결여 문제를 해결하고, 사용자 질의와 서비스 설명 간의 유사도를 정확히 계산하여 최적의 웹 서비스를 추천할 수 있는가?

**방법론**:
- 어휘적 분석을 위한 통계적 TF-IDF 기법과 문맥 시맨틱 분석을 위한 Universal Sentence Encoder 신경망 모델의 하이브리드 결합
- 어휘 및 의미적 관련성 컴포넌트 간의 가중치를 제어하는 하이브리드 적합성 계산 공식 제안
- 55개 웹 서비스 및 24개 테스트 쿼리를 포함한 데이터셋 기반 비교 실험

**주요 결과**:
- 하이브리드 접근법이 정확한 용어 매칭과 의미적 유사성 모두를 효과적으로 반영하여 단일 모델 대비 추천 품질을 크게 개선
- 정보 검색 표준 평가지표 기준 성능 향상을 검증하고 향후 추천 개인화 및 비기능적 서비스 특성 결합 방향을 식별


## 초록 (원문)

The article addresses the problem of web service recommendation in service-oriented systems. The broker in such systems plays a critical role in intelligent service discovery, maintaining a registry of available services to efficien tly respond to consumer requests. The limitations of traditional keyword-based search methods are analyzed, particularly the lexical gap problem and the lack of semantic understanding of query context. Traditional approaches fail to recognize synonyms and semantic relationships between terms, requiring exact terminology matching. A hybrid approach is proposed that combines the statistical TF-IDF method for lexical analysis with the Universal Sentence Encoder neural network model for semantic text analysis. TF-IDF provides high precision when common terms exist between queries and descriptions, while the Universal Sentence Encoder captures semantic meaning through 512-dimensional vector representations. This approach allows considering both exact term matches and semantic similarity between user queries and service descriptions. A formula for combined relevance computation with a balance parameter between lexical and semantic components is developed. Experimental evaluation was conducted on a web services dataset using standard information retrieval metrics. A formula for combined relevance computation with a balance parameter between lexical and semantic components is developed. Experimental evaluation was conducted on a dataset containing 55 web services and 24 test queries using standard information retrieval metrics. Compared to baseline methods, the hybrid approach provides significant improvement in recommendation quality. The obtained values are presented in tables and graphs. Directions for future research are identified, including recommendation personalization and integration of non-functional service characteristics.

## 키워드

Relevance (law), Encoder, Semantic similarity, Semantics (computer science), Service (business), Semantic feature, Vector space model, Semantic computing

## 위키 연관

- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모

