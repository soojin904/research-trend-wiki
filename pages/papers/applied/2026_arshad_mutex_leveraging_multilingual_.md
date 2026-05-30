---
title: "MUTEX: Leveraging Multilingual Transformers and Conditional Random Fields for Enhanced Urdu Toxic Span Detection"
authors: ['Inayat Arshad', 'Fajar Saleem', 'Ijaz Hussain']
year: 2026
venue: "ArXiv.org"
tags: ['Hate Speech and Cyberbullying Detection', 'Writing and Handwriting Education', 'Topic Modeling']
source: raw/applied/applied_2026_MUTEX_Leveraging_Multilin_nodoi.md
---

# MUTEX: Leveraging Multilingual Transformers and Conditional Random Fields for Enhanced Urdu Toxic Span Detection

**제목(한글)**: MUTEX: 향상된 우르두어 유해 스팬 탐지를 위한 다국어 트랜스포머 및 조건부 무작위장 활용

## 한국어 요약

**연구질문**: 기존 문장 수준 분류 방식의 한계를 넘어, 우르두어 텍스트 내에서 특정 유해 구간(toxic span)을 정확히 식별하고, 토큰 수준 주석 데이터 부족, 언어적 복잡성, 코드 전환, 비격식 표현, 풍부한 형태학적 변이 등의 문제점을 해결하여 유해 스팬 탐지 성능을 향상시킬 수 있는가?

**방법론**:
- MUTEX 프레임워크 (다국어 트랜스포머와 조건부 무작위장(CRF) 결합)
- 수동으로 주석 처리된 토큰 수준 유해 스팬 데이터셋 사용
- XLM RoBERTa와 CRF 레이어를 활용한 시퀀스 레이블링
- 소셜 미디어, 온라인 뉴스, YouTube 리뷰에서 추출한 다중 도메인 데이터로 평가

**주요 결과**:
- MUTEX는 60%의 토큰 수준 F1 점수를 달성하여 우르두어 유해 스팬 탐지의 최초 지도 학습 기반 성능 기준선(supervised baseline)을 제시했다.
- 트랜스포머 기반 모델이 문맥적 유해성(contextual toxicity)을 암묵적으로 포착하는 데 더 효과적이었다.
- 코드 전환(code-switching) 및 형태학적 변이(morphological variation) 문제를 다른 모델보다 잘 해결할 수 있었다.

**저자**: Inayat Arshad; Fajar Saleem; Ijaz Hussain
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-03-05
**DOI**: 

## 초록 (원문)

Urdu toxic span detection remains limited because most existing systems rely on sentence-level classification and fail to identify the specific toxic spans within those text. It is further exacerbated by the multiple factors i.e. lack of token-level annotated resources, linguistic complexity of Urdu, frequent code-switching, informal expressions, and rich morphological variations. In this research, we propose MUTEX: a multilingual transformer combined with conditional random fields (CRF) for Urdu toxic span detection framework that uses manually annotated token-level toxic span dataset to improve performance and interpretability. MUTEX uses XLM RoBERTa with CRF layer to perform sequence labeling and is tested on multi-domain data extracted from social media, online news, and YouTube reviews using token-level F1 to evaluate fine-grained span detection. The results indicate that MUTEX achieves 60% token-level F1 score that is the first supervised baseline for Urdu toxic span detection. Further examination reveals that transformer-based models are more effective at implicitly capturing the contextual toxicity and are able to address the issues of code-switching and morphological variation than other models.

## 키워드

Conditional random field, Semaphore, Transformer, Span (engineering), Life span, Named-entity recognition

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

