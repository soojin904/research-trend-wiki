---
title: "Unsupervised Cross-Lingual Part-of-Speech Tagging with Monolingual Corpora Only"
authors: ['Jianyu Zheng']
year: 2026
venue: "ArXiv.org"
tags: ['Natural Language Processing Techniques', 'Topic Modeling', 'Speech Recognition and Synthesis']
source: raw/applied/applied_2026_Unsupervised_CrossLingual_nodoi.md
---

# Unsupervised Cross-Lingual Part-of-Speech Tagging with Monolingual Corpora Only

**제목(한글)**: 단일 언어 코퍼스만을 활용한 비지도 교차 언어 품사 태깅

## 한국어 요약

**연구질문**: 병렬 코퍼스 부족 문제를 해결하고, 단일 언어 코퍼스만으로 비지도 교차 언어 품사(Part-of-Speech, POS) 태깅을 효과적으로 수행하는 방법은 무엇인가?

**방법론**:
- 비지도 신경망 기계 번역(UNMT) 시스템을 활용하여 의사 병렬 문장 쌍 구축
- 단어 정렬 기반의 표준 투영(projection) 절차를 따라 목표 언어 품사 태거 훈련
- 투영된 품사 태그를 보정하기 위한 다중 소스 투영 기법 제안

**주요 결과**:
- 제안하는 방법은 병렬 코퍼스를 사용하는 기존 교차 언어 품사 태거와 비교하여 유사하거나 특정 언어에서는 더 우수한 성능을 달성함.
- 제안된 다중 소스 투영 기법은 기존 방법 대비 평균 1.3%의 성능 향상을 가져옴.

**저자**: Jianyu Zheng
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-02-10
**DOI**: 

## 초록 (원문)

Due to the scarcity of part-of-speech annotated data, existing studies on low-resource languages typically adopt unsupervised approaches for POS tagging. Among these, POS tag projection with word alignment method transfers POS tags from a high-resource source language to a low-resource target language based on parallel corpora, making it particularly suitable for low-resource language settings. However, this approach relies heavily on parallel corpora, which are often unavailable for many low-resource languages. To overcome this limitation, we propose a fully unsupervised cross-lingual part-of-speech(POS) tagging framework that relies solely on monolingual corpora by leveraging unsupervised neural machine translation(UNMT) system. This UNMT system first translates sentences from a high-resource language into a low-resource one, thereby constructing pseudo-parallel sentence pairs. Then, we train a POS tagger for the target language following the standard projection procedure based on word alignments. Moreover, we propose a multi-source projection technique to calibrate the projected POS tags on the target side, enhancing to train a more effective POS tagger. We evaluate our framework on 28 language pairs, covering four source languages (English, German, Spanish and French) and seven target languages (Afrikaans, Basque, Finnis, Indonesian, Lithuanian, Portuguese and Turkish). Experimental results show that our method can achieve performance comparable to the baseline cross-lingual POS tagger with parallel sentence pairs, and even exceeds it for certain target languages. Furthermore, our proposed multi-source projection technique further boosts performance, yielding an average improvement of 1.3% over previous methods.

## 키워드

Projection (relational algebra), Sentence, Word (group theory), Baseline (sea), Parallel corpora, Language model, Natural language

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

