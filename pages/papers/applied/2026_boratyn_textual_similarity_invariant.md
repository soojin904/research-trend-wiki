---
title: "Is Textual Similarity Invariant under Machine Translation? Evidence Based on the Political Manifesto Corpus"
authors: ['Daria Boratyn', 'Damian Brzyski', 'Albert Leśniak', 'Wojciech Łukasik', 'Maciej Rapacz', 'Jan Rybicki', 'Wojciech Słomczyński', 'Dariusz Stolicki']
year: 2026
venue: "arXiv (Cornell University)"
tags: ['Computational and Text Analysis Methods', 'Topic Modeling', 'Language and cultural evolution']
source: raw/applied/applied_2026_Is_Textual_Similarity_Inv_nodoi.md
---

# Is Textual Similarity Invariant under Machine Translation? Evidence Based on the Political Manifesto Corpus
**제목(한글)**: 기계 번역 하에서 텍스트 유사도는 불변인가? 정치 선언문 코퍼스를 기반으로 한 실증 연구

## 한국어 요약

**연구질문**: 28개 언어로 구성된 정치 정당 강령 코퍼스를 기계 번역할 때 문단 임베딩(Embedding) 간 코사인 유사도(Cosine Similarity) 관계가 얼마나 안정적으로 유지되는가?

**방법론**:
- EU eTranslation 서비스를 통해 28개 언어를 영어로 번역한 2,800여 개 정치 정당 강령(Manifesto Corpus) 활용
- 번역 유도 의미적 변이를 직접 측정하지 않고 여러 임베딩 모델 간 쌍별 유사도 관계의 안정성 측정
- 원문 텍스트에서의 모델 간 불일치를 보정된 불변성 임계값으로 활용하는 언어별 비열등성 검정 프레임워크 설계

**주요 결과**:
- 10개 언어는 번역 불변성(translation invariance)이 확인된 반면, 4개 언어는 탐지 가능한 왜곡 발생
- 나머지 언어들은 가용 증거만으로 판정 불가 — 번역 전 언어별 불변성 검증의 필요성 제시

**저자**: Daria Boratyn; Damian Brzyski; Albert Leśniak; Wojciech Łukasik; Maciej Rapacz; Jan Rybicki; Wojciech Słomczyński; Dariusz Stolicki
**출처**: arXiv (Cornell University), Vol.None
**발행일**: 2026-05-01
**DOI**: 

## 초록 (원문)

We investigate the extent to which cosine similarity between paragraph embeddings is invariant under machine translation, using the Manifesto Corpus of over 2,800 political party platforms in 28 languages translated to English via the EU eTranslation service. Rather than measuring translation-induced semantic shift directly we measure the stability of pairwise similarity relationships across embedding models, and use inter-model disagreement on original-language text as a calibrated invariance threshold. This yields a per-language non-inferiority test for four hypotheses about how translation interacts with embedding choice, with verdicts that distinguish languages where translation demonstrably preserves semantic structure from those where it demonstrably degrades it and from those where the available evidence does not resolve the question. The framework is corpus- and pipeline-agnostic and extends naturally to downstream tasks. Applied to our data, it identifies ten languages with translation invariance and four with detectable distortion.

## 키워드

Manifesto, Pairwise comparison, Embedding, Invariant (physics), Similarity (geometry), Cosine similarity

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

