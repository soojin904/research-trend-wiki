---
title: "Cascaded Signal Refinement: A Three-Layer Architecture for Cost-Efective Text Analysis with Small Language Models"
authors: ['del Amor Herrera Miguel']
year: 2026
venue: "Zenodo (CERN European Organization for Nuclear Research)"
tags: ['Natural Language Processing Techniques', 'Authorship Attribution and Profiling', 'Topic Modeling']
source: raw/applied/applied_2026_Cascaded_Signal_Refinemen_zenodo_19263702.md
---

# Cascaded Signal Refinement: A Three-Layer Architecture for Cost-Efective Text Analysis with Small Language Models
**제목(한글)**: 종속 신호 정제(CSR): 소형 언어 모델을 활용한 비용 효율적인 대규모 텍스트 분석용 3레이어 아키텍처

**저자**: del Amor Herrera Miguel
**출처**: Zenodo (CERN European Organization for Nuclear Research), Vol.None
**발행일**: 2026-03-27
**DOI**: https://doi.org/10.5281/zenodo.19263702

## 한국어 요약

**연구질문**: 상용 소비자 하드웨어에서 동작하는 소형 언어 모델(SLM)을 사용해 대규모 텍스트 코퍼스 분석을 정밀하면서도 저비용으로 수행할 수 있는 아키텍처는 어떻게 설계하는가?

**방법론**:
- 종속 신호 정제(Cascaded Signal Refinement, CSR) 3단계 아키텍처 설계
  - Layer 1: 결정론적 필터링(어휘 감지, 시맨틱 클러스터링, 슬라이딩 윈도우 스코어링)
  - Layer 2: 빠른 LLM 스크리닝(이진 분류)
  - Layer 3: 깊은 LLM 분석(도메인 지식이 주입된 구조적 정보 추출)
- 로컬 llama.cpp 환경의 4B 매개변수 모델 및 27,020개 다국어 메시지 코퍼스를 통한 컴플라이언스 모니터링 실증 테스트

**주요 결과**:
- Layer 1 단계에서 코퍼스 후보를 1초 이내에 11.4% 수준으로 축소함
- Layer 2 단계에서 후보 중 73%를 거부하여, 최종 비싼 Layer 3가 원래 코퍼스의 단 2.9%만 분석하게 해 토큰을 96.9% 절감함
- 지능적 사전 필터링을 통해 소형 모델로도 프론티어(초거대) 모델에 필적하는 고정밀 텍스트 분석 성능을 달성할 수 있음을 규명함


## 초록 (원문)

We present Cascaded Signal Re nement (CSR), a three-layer architecture for analyzing large text corpora using small language models (18B parameters) runningon consumer hardware. CSR combines a zero-cost deterministic layer (lexical detection, semantic clustering, sliding-window co-occurrence scoring) with a fast LLM screening layer (binary classi cation) and a deep LLM analysis layer (structured extraction with domain-injected context). We evaluate CSR on a compliance monitoring task: a 27,020 message multilingual corporate communications corpus processed by a 4B-parameter model with 48K context running locally via llama.cpp. Layer 1 reduces the corpus to 89 candidate blocks covering 11.4% of messages in under 1 second. Layer 2 screening rejects 73.0% of candidates, and the expensive Layer 3 deep analysis ultimately processes only 2.9% of the original corpus (776 messages), achieving a 96.9% token reduction while producing 22 con rmed ndings with 17 additional deterministic safety-net detections in 17 APIcalls totaling 98.7 seconds. The core contribution is demonstrating that intelligent pre-filtering makes small models competitive with frontier models for needle-in-haystack text analysis

## 키워드

Layer (electronics), Security token, Context (archaeology), SIGNAL (programming language), Text corpus, Language model, Context model, Frame (networking)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

