---
title: "Large language models for pneumonia detection in radiology reports via text analysis"
authors: ['Weisheng Chen', 'Xinya Li', 'Zhongkai Qu', 'Ting Liu', 'Bo Chen', 'Liying Huang', 'Ningxia He', 'Zhigang Wang', 'Jun Lyu']
year: 2026
publication_date: 2026-09-23
venue: "PLOS Digital Health"
volume: "5"
issue: "9"
pages: "e0001104-e0001104"
doi: "https://doi.org/10.1371/journal.pdig.0001104"
oa_status: "gold"
openalex_id: "https://openalex.org/W7214071438"
query_keyword: "text analysis"
tags: ['Topic Modeling', 'COVID-19 diagnosis using AI', 'Artificial Intelligence in Healthcare and Education']
keywords: ['pneumonia detection', 'radiology reports', 'large language models', 'retrieval-augmented generation', 'MIMIC-IV', 'critical illness', 'radiographic findings', 'model parameter size']
source: openalex-keyword
---

# Large language models for pneumonia detection in radiology reports via text analysis

**저자**: Weisheng Chen; Xinya Li; Zhongkai Qu; Ting Liu; Bo Chen; Liying Huang; Ningxia He; Zhigang Wang; Jun Lyu
**출처**: PLOS Digital Health, Vol.5 No.9, pp.e0001104-e0001104
**발행일**: 2026-09-23
**DOI**: https://doi.org/10.1371/journal.pdig.0001104
**수집 키워드**: text analysis

## 초록

Pneumonia is a common infection in critically ill patients with poor outcomes, and its identification relies heavily on radiological evidence. Most MIMIC-based pneumonia studies rely on structured codes rather than radiological text, which may limit the precision of pneumonia-related case identification. This study evaluated large language models (LLMs) and retrieval-augmented generation (RAG) frameworks for automated detection of radiographic evidence of pneumonia from radiology reports. Radiological reports from the MIMIC-IV database were analyzed using pre-trained models in an inference-only setting without additional training, fine-tuning, or dataset splitting. Model performance was evaluated using accuracy, precision, sensitivity, specificity, and F1-score, with point estimates calculated from the full dataset and corresponding 95% confidence intervals estimated using 1,000 patient-level clustered bootstrap replicates. Independent evaluation was subsequently performed using a GZ dataset from a tertiary hospital in Guangzhou. RAG generally improved model performance, with gemma3-27b achieving the highest accuracy of 96.4% on the MIMIC-IV dataset and maintaining an accuracy of 87.6% on the GZ dataset. Model performance did not increase linearly with parameter size, suggesting that task-specific model suitability may be more important than parameter scale for this application. Although larger models required longer inference times, their increased computational costs did not consistently translate into proportional performance gains. Overall, LLMs demonstrated high accuracy in interpreting radiology reports for detecting radiographic evidence of pneumonia. The RAG architecture further enhanced robustness and generalizability through knowledge augmentation, providing a methodological basis for automated radiology report analysis and large-scale database curation.

## 키워드

pneumonia detection, radiology reports, large language models, retrieval-augmented generation, MIMIC-IV, critical illness, radiographic findings, model parameter size, inference latency

## 주제 분류 (OpenAlex Topics)

- Topic Modeling (score: 0.262)
- COVID-19 diagnosis using AI (score: 0.198)
- Artificial Intelligence in Healthcare and Education (score: 0.162)

## 메모

