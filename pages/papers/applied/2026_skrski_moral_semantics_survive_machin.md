---
title: "Moral Semantics Survive Machine Translation: Cross-Lingual Evidence from Moral Foundations Corpora"
authors: ['Maciej Skórski']
year: 2026
venue: "ArXiv.org"
tags: ['Hate Speech and Cyberbullying Detection', 'Psychology of Moral and Emotional Judgment', 'Computational and Text Analysis Methods']
source: raw/applied/applied_2026_Moral_Semantics_Survive_M_nodoi.md
---

# Moral Semantics Survive Machine Translation: Cross-Lingual Evidence from Moral Foundations Corpora
**제목(한글)**: 도덕적 의미론은 기계 번역을 통해 살아남는가: 도덕성 기반 코퍼스의 교차 언어적 근거

## 한국어 요약

**연구질문**: 영어 전용 도덕 감성 주석 코퍼스를 LLM 기반 번역을 통해 다른 언어(폴란드어)로 활용할 때, 번역 과정에서 미묘한 도덕적 단서들이 충분히 보존되어 교차 언어적 기계 학습에 활용 가능한가?

**방법론**:
- 다양한 주제의 소셜 미디어 게시글 약 5만 건의 도덕 감성 주석 데이터를 대상으로 4단계 검증 파이프라인 구성
- LaBSE 교차 언어 임베딩 유사도, 중심 커널 정렬(CKA), LLM 심판 평가(LLM-as-judge), 딥러닝 분류기 동등성 검증을 병행 적용

**주요 결과**:
- 속어, 비속어, 문화적으로 특수한 표현 처리의 한계에도 불구하고, 직접 번역이 도덕적 단서를 보존하여 평균 코사인 유사도 0.86을 기록하고 AUC 격차가 0.01~0.02 수준에 그침
- 언어 모델 미세 조정을 통해 격차가 더 좁혀지며, 기계 번역이 도덕 가치 연구의 실용적이고 비용 효율적인 교차 언어 확장 경로임을 실증

**저자**: Maciej Skórski
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-05-21
**DOI**: 

## 초록 (원문)

Moral language is subtle and culturally variable, making it difficult to translate faithfully across languages. Idiomatic expressions, slang, and cultural references introduce hard-to-avoid translation artifacts. Yet automated moral values classification depends on language-specific annotated corpora that exist almost exclusively in English. We investigate whether LLM-based translation can bridge this gap, taking Polish as a test case. Using $\sim$50k morally-annotated social media posts from a diverse range of topics, we apply a principled four-method validation pipeline: LaBSE cross-lingual embedding similarity, Centered Kernel Alignment (CKA), LLM-as-judge evaluation, and deep learning classifier parity tests. We show that despite shortcomings in handling slang, vulgarity, and culturally-loaded expressions, direct translation preserves subtle moral cues well enough to be harvested by cross-lingual machine learning -- with mean cosine similarity of 0.86 and AUC gaps of 0.01--0.02 across all foundations closing further under fine-tuning of language models. These results demonstrate that machine translation is a practical and cost-effective path to moral values research in languages currently under-resourced in this domain. We demonstrate this for Polish as a representative Slavic language, with expected generalisation to related languages.

## 키워드

Classifier (UML), Cosine similarity, Language understanding, Semantics (computer science), Similarity (geometry), Machine translation, Language translation

## 위키 연관

- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모

