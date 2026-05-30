---
title: "A Multi-Stage Heuristic Filtering Pipeline for Refining a Spanish Legal Corpus for Natural Language Processing"
authors: ['Nikolai Tiurin', 'Xavier Blanco']
year: 2025
venue: "Langues & Parole"
tags: ['Text Readability and Simplification', 'Topic Modeling', 'Natural Language Processing Techniques']
source: raw/applied/applied_2025_A_MultiStage_Heuristic_Fi_languesparole_153.md
---

# A Multi-Stage Heuristic Filtering Pipeline for Refining a Spanish Legal Corpus for Natural Language Processing

**제목(한글)**: 자연어 처리(Natural Language Processing)를 위한 스페인어 법률 말뭉치(Corpus) 정제를 위한 다단계 휴리스틱 필터링 파이프라인

## 한국어 요약

**연구질문**: 자연어 처리 작업을 위해 잡음이 많은 스페인어 법률 말뭉치를 어떻게 효과적으로 정제할 수 있는가?

**방법론**:
- 다단계 휴리스틱 파이프라인 (Multi-Stage Heuristic Pipeline)
- 텍스트 정규화 (Text Normalization): 문자 단위 오류 수정 및 하이픈 교정
- 정량적 측정 기반 필터링 (Filtering based on Quantifiable Metrics): 개행 문자 비율, 비알파벳 문자 수, 오타 단어 비율 등 활용
- 결합 경계 점수 (Combined Borderline Score, CBS)를 통한 한계 세그먼트 식별 및 제거

**주요 결과**:
- OCR 오류 및 비텍스트 요소 등 잡음이 제거된, 현저히 더 깨끗한 스페인어 법률 텍스트 말뭉치 생성.
- 자동 텍스트 단순화(automatic text simplification)와 같은 모델 훈련을 위한 고품질 기반 제공.
- 다른 크고 다양한 법률 텍스트를 정제하는 데 재사용 가능한 방법론 제시.

**저자**: Nikolai Tiurin; Xavier Blanco
**출처**: Langues & Parole, Vol.10, pp.37-56
**발행일**: 2025-12-17
**DOI**: https://doi.org/10.5565/rev/languesparole.153

## 초록 (원문)

This research presents a multi-stage heuristic pipeline to refine the Spanish Boletín Oficial del Estado (BOE) corpus for Natural Language Processing tasks. Raw legal corpora are often filled with noise, including OCR errors, lists, tables, and non-textual placeholders, making them unsuitable for training language models. Our methodology first normalizes the text by correcting character-level errors and repairing hyphenation. Subsequently, it applies a series of filters based on quantifiable metrics, such as newline character ratios, non-alphabetic character counts, and misspelled word percentages, to detect and discard structurally and semantically unsuitable segments. A key contribution is the novel Combined Borderline Score (CBS), which identifies and removes marginal segments that are close to multiple failure thresholds. The result is a significantly cleaner corpus of legal texts, providing a high-quality foundation for training models for tasks like automatic text simplification and offering a reusable methodology for cleaning other large and diverse legal texts.

## 키워드

Pipeline (software), Heuristic, Character (mathematics), Natural language, Word (group theory), Key (lock), Refining (metallurgy), Language model

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

