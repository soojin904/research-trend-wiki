---
title: "Feasibility of Using Large Language Models for Structured Medication Extraction from Clinical Text: A Comparative Analysis of Zero-Shot and Few-Shot Paradigms"
authors: ['Evan Jacob Schulte', 'Mohamed Abusharkh', 'Kushal Dahal', 'Michael E. Klepser', 'Minji Sohn']
year: 2026
publication_date: 2026-02-27
venue: "Applied Sciences"
volume: "16"
issue: "5"
pages: "2300-2300"
doi: "https://doi.org/10.3390/app16052300"
oa_status: "gold"
openalex_id: "https://openalex.org/W7131778998"
query_keyword: "text analysis"
tags: ['Topic Modeling', 'Biomedical Text Mining and Ontologies', 'Pharmacovigilance and Adverse Drug Reactions']
keywords: ['Schema (genetic algorithms)', 'Population', 'Data extraction', 'Reliability (semiconductor)', 'Bridging (networking)', 'Health care', 'Data reliability', 'Rendering (computer graphics)']
source: openalex-keyword
---

# Feasibility of Using Large Language Models for Structured Medication Extraction from Clinical Text: A Comparative Analysis of Zero-Shot and Few-Shot Paradigms

**저자**: Evan Jacob Schulte; Mohamed Abusharkh; Kushal Dahal; Michael E. Klepser; Minji Sohn
**출처**: Applied Sciences, Vol.16 No.5, pp.2300-2300
**발행일**: 2026-02-27
**DOI**: https://doi.org/10.3390/app16052300
**수집 키워드**: text analysis

## 초록

The digitization of healthcare has been accompanied by a rapid expansion of electronic health records (EHRs); however, a significant proportion of critical patient data, specifically medication regimens, remains entrapped within unstructured clinical narratives. The inability to seamlessly compute this data hinders advancements in pharmacovigilance, clinical decision support, and population health management. This study presents a comprehensive, rigorous evaluation of the feasibility of deploying Large Language Models (LLMs) to automate the extraction of structured dosage information (Dose, Daily Frequency, Duration) from outpatient antimicrobial clinical notes sourced from the Collaboration to Harmonize Antimicrobial Registry Measures (CHARM) registry. We scrutinized the performance of five distinct open-weight architectures, namely GPT-OSS:20B, Gemma 2:9B, Mistral 7B, Qwen3:14B and Llama 3.2, across both Zero-Shot and Retrieval Augmented Generation (RAG)-based Few-Shot prompting paradigms. Our analysis reveals a fundamental architectural trade-off: the reasoning-optimized GPT-OSS:20B dominates the zero-shot landscape (F1 &gt; 0.90) by leveraging abstract schema understanding, whereas the instruction-tuned Gemma 2:9B excels in the few-shot setting (F1 ~ 0.99), effectively utilizing examples as guardrails to surpass larger models. Conversely, smaller models (Mistral, Llama) exhibit a prohibitive “hallucination barrier,” rendering them unsafe for unsupervised clinical application. Furthermore, we identify “Inconsistent Unit Handling” and “Complex Temporal Logic” as persistent failure modes that resist simple scaling laws. This report provides a definitive framework for selecting model architectures based on the availability of few-shot examples and highlights the necessity of dynamic RAG strategies to achieve production-grade reliability in medical informatics.

## 키워드

Schema (genetic algorithms), Population, Data extraction, Reliability (semiconductor), Bridging (networking), Health care, Data reliability, Rendering (computer graphics)

## 주제 분류 (OpenAlex Topics)

- Topic Modeling (score: 0.266)
- Biomedical Text Mining and Ontologies (score: 0.219)
- Pharmacovigilance and Adverse Drug Reactions (score: 0.163)

## 메모

