---
title: "Local Large Language Models in R with Ollama"
authors: ['Martin Schweinberger']
year: 2026
venue: "Zenodo (CERN European Organization for Nuclear Research)"
tags: ['Computational and Text Analysis Methods', 'Authorship Attribution and Profiling', 'Language and cultural evolution']
source: raw/applied/applied_2026_Local_Large_Language_Mode_zenodo_19332921.md
---

# Local Large Language Models in R with Ollama
**제목(한글)**: R과 Ollama를 활용한 로컬 거대 언어 모델 분석법

**저자**: Martin Schweinberger
**출처**: Zenodo (CERN European Organization for Nuclear Research), Vol.None
**발행일**: 2026-03-27
**DOI**: https://doi.org/10.5281/zenodo.19332921

## 한국어 요약

**연구질문**: 민감한 텍스트 데이터 노출 없이 독립된 연구용 로컬 환경(R 프로그램) 내에서 Ollama 플랫폼을 이용해 텍스트 요약, 분류 및 질문 답변 분석을 수행하는 방법은 무엇인가?

**방법론**:
- R 환경에서 `ollamar` 패키지와 Ollama 플랫폼의 로컬 모델 구동 엔진 설정 절차 정립
- 로컬 생성 함수(`generate()`)와 대화 함수(`chat()`)를 통한 자연어 처리 작업 및 프롬프트 엔지니어링 사례 실습 구성

**주요 결과**:
- 클라우드 API 전송을 거치지 않아 연구 보안성이 유지되는 상태에서 대용량 언어 텍스트 데이터에 LLM 기술을 안정적으로 접목시킬 수 있는 방법론 가이드라인을 제공함


## 초록 (원문)

This tutorial introduces the use of local large language models (LLMs) in R via the Ollama platform and the ollamar package, covering installation and setup, the generate() and chat() functions, and prompt engineering for text analysis tasks including summarisation, classification, and question answering. It is aimed at researchers in linguistics and digital humanities who want to apply LLMs to their data without sending sensitive information to external APIs. This tutorial is part of the Language Technology and Data Analysis Laboratory (LADAL), a free, open-access research infrastructure at the University of Queensland. LADAL provides tutorials, tools, and courses for researchers working with language data. All materials are freely available at https://ladal.edu.au and are part of the Language Data Commons of Australia (LDaCA), funded by ARDC and NCRIS.

## 키워드

Language technology, Computational linguistics, Language model, Modeling language, Language industry, Data modeling, Natural language, Information technology

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

