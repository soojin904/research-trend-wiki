---
title: "TajikNLP: An Open-Source Toolkit for Comprehensive Text Processing of Tajik (Cyrillic Script)"
authors: ['Mullosharaf K. Arabov']
year: 2026
venue: "ArXiv.org"
tags: ['Natural Language Processing Techniques', 'Mathematics, Computing, and Information Processing', 'Topic Modeling']
source: raw/applied/applied_2026_TajikNLP_An_OpenSource_To_nodoi.md
---

# TajikNLP: An Open-Source Toolkit for Comprehensive Text Processing of Tajik (Cyrillic Script)

**제목(한글)**: TajikNLP: 타지크어(키릴 문자) 종합 텍스트 처리를 위한 오픈소스 툴킷

## 한국어 요약

**연구질문**: 타지크어(키릴 문자)의 언어 연구 및 응용 개발을 저해하는 NLP 툴킷 부족 문제를 어떻게 해결할 수 있는가?

**방법론**:
- 오픈소스 Python 라이브러리(TajikNLP) 개발
- 통합 Doc 객체 기반의 모듈식 텍스트 처리 파이프라인 구현
- 새로운 통합 형태소 분석 엔진 도입
- 어휘 기반 감성 분석 및 사전 학습된 임베딩(Word2Vec/FastText) 활용

**주요 결과**:
- 타지크어(키릴 문자) 텍스트 처리를 위한 최초의 포괄적인 파이프라인 제공
- 타지크어의 복잡한 형태론적 특성(교착적 명사 및 동사 굴절) 처리 능력 대폭 개선
- 연구 재현성 및 활용을 위한 4가지 언어학적 데이터셋(POS 태그 코퍼스, 감성 어휘집 등) 공개
- 저자원 키릴 문자 환경에서 타지크어 NLP의 학술 및 산업적 적용 장벽 완화 및 기반 기술 인프라 구축

**저자**: Mullosharaf K. Arabov
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-05-06
**DOI**: 

## 초록 (원문)

The Tajik language, written in Cyrillic script, remains severely under-resourced in terms of publicly available natural language processing (NLP) toolkits, hindering both linguistic research and applied development. This paper introduces TajikNLP, an open-source Python library that provides the first comprehensive pipeline for processing authentic Tajik text while preserving the original Cyrillic orthography. The library implements a modular architecture centered around a unified Doc object, enabling sequential application of components for cleaning, normalization, tokenization (including subword BPE), morphemic segmentation, part-of-speech tagging, stemming, lemmatization, and sentence splitting. A novel unified morphology engine is introduced, offering controlled and deep analysis modes that significantly improve handling of Tajik's agglutinative nominal and verbal inflections. The release further incorporates a lexicon-based sentiment analyser and pre-trained Word2Vec/FastText embeddings loaded directly from the Hugging Face Hub. To ensure reproducibility and facilitate future research, four accompanying linguistic datasets -- a POS-tagged corpus (52.5k entries), a sentiment lexicon (3.5k entries), a toponym gazetteer (5.6k entries), and a personal names dataset (3.8k entries) -- have been openly published under permissive licenses. The library's reliability is validated by an extensive test suite of 616 automated tests achieving 93% source code coverage. TajikNLP thus establishes a foundational technological infrastructure for Tajik language processing, lowering the barrier to entry for both academic and industrial applications in low-resource Cyrillic-script environments.

## 키워드

Lexicon, Text processing, Python (programming language), Unicode, Lemmatisation, Morpheme, Lexical analysis, Sentence

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

