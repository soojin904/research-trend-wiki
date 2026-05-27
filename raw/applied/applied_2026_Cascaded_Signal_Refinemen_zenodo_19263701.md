---
title: "Cascaded Signal Refinement: A Three-Layer Architecture for Cost-Efective Text Analysis with Small Language Models"
authors: ['del Amor Herrera Miguel']
year: 2026
publication_date: 2026-03-27
venue: "Zenodo (CERN European Organization for Nuclear Research)"
volume: "None"
issue: "None"
pages: ""
doi: "https://doi.org/10.5281/zenodo.19263701"
oa_status: "green"
openalex_id: "https://openalex.org/W7141652489"
query_keyword: "text analysis"
tags: ['Natural Language Processing Techniques', 'Authorship Attribution and Profiling', 'Topic Modeling']
keywords: ['Layer (electronics)', 'Security token', 'Context (archaeology)', 'SIGNAL (programming language)', 'Text corpus', 'Language model', 'Context model', 'Frame (networking)']
source: openalex-keyword
---

# Cascaded Signal Refinement: A Three-Layer Architecture for Cost-Efective Text Analysis with Small Language Models

**저자**: del Amor Herrera Miguel
**출처**: Zenodo (CERN European Organization for Nuclear Research)
**발행일**: 2026-03-27
**DOI**: https://doi.org/10.5281/zenodo.19263701
**수집 키워드**: text analysis

## 초록

We present Cascaded Signal Re nement (CSR), a three-layer architecture for analyzing large text corpora using small language models (18B parameters) runningon consumer hardware. CSR combines a zero-cost deterministic layer (lexical detection, semantic clustering, sliding-window co-occurrence scoring) with a fast LLM screening layer (binary classi cation) and a deep LLM analysis layer (structured extraction with domain-injected context). We evaluate CSR on a compliance monitoring task: a 27,020 message multilingual corporate communications corpus processed by a 4B-parameter model with 48K context running locally via llama.cpp. Layer 1 reduces the corpus to 89 candidate blocks covering 11.4% of messages in under 1 second. Layer 2 screening rejects 73.0% of candidates, and the expensive Layer 3 deep analysis ultimately processes only 2.9% of the original corpus (776 messages), achieving a 96.9% token reduction while producing 22 con rmed ndings with 17 additional deterministic safety-net detections in 17 APIcalls totaling 98.7 seconds. The core contribution is demonstrating that intelligent pre-filtering makes small models competitive with frontier models for needle-in-haystack text analysis

## 키워드

Layer (electronics), Security token, Context (archaeology), SIGNAL (programming language), Text corpus, Language model, Context model, Frame (networking), Core (optical fiber)

## 주제 분류 (OpenAlex Topics)

- Natural Language Processing Techniques (score: 0.132)
- Authorship Attribution and Profiling (score: 0.118)
- Topic Modeling (score: 0.110)

## 메모

