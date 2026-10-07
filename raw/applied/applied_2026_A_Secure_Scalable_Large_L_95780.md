---
title: "A Secure, Scalable Large Language Model–Based System (CIDER) for High-Throughput Clinical Data Extraction From Medical Reports: Retrospective Validation Study"
authors: ['Máté Posta', 'Aida Figler', 'Zsofia Dobolyi', 'Balázs Győrffy']
year: 2026
publication_date: 2026-09-02
venue: "Journal of Medical Internet Research"
volume: "28"
issue: "None"
pages: "e95780-e95780"
doi: "https://doi.org/10.2196/95780"
oa_status: "gold"
openalex_id: "https://openalex.org/W7206210363"
query_keyword: "text analysis"
tags: ['Biomedical Text Mining and Ontologies', 'Topic Modeling', 'Artificial Intelligence in Healthcare and Education']
keywords: ['Scalability', 'Biobank', 'Robustness (evolution)', 'Data extraction', 'Data collection', 'Inference', 'SNOMED CT', 'Information extraction']
source: openalex-keyword
---

# A Secure, Scalable Large Language Model–Based System (CIDER) for High-Throughput Clinical Data Extraction From Medical Reports: Retrospective Validation Study

**저자**: Máté Posta; Aida Figler; Zsofia Dobolyi; Balázs Győrffy
**출처**: Journal of Medical Internet Research, Vol.28, pp.e95780-e95780
**발행일**: 2026-09-02
**DOI**: https://doi.org/10.2196/95780
**수집 키워드**: text analysis

## 초록

Background A substantial proportion of clinically relevant information remains locked in unstructured narrative documents, creating a bottleneck for clinical research, biobank annotation, registry development, and real-world evidence generation. While large language models (LLMs) enable advanced clinical text mining, adoption is constrained by concerns regarding data security, multilingual performance, and reproducibility. Manual data abstraction remains predominant for registry curation and retrospective research, despite being labor intensive, costly, and prone to variability. Objective We developed and validated CIDER (Clinical Data Extractor), a secure, institutionally deployable, LLM-based pipeline for automated structured data extraction from routine clinical reports. We assessed the potential utility of the system for improving the completeness of clinical research datasets. Methods CIDER uses an asynchronous FastAPI-based architecture with a locally deployed vLLM inference engine running Qwen3-VL-32B-Instruct-FP8 model in an institution-controlled environment. The system was validated on 2073 real-world Hungarian-language histopathology reports (a challenging non-English setting), using a manually curated structured database as the reference standard. Seven variables were evaluated (sex, surgery year, T stage, N stage, organ, histology, and size). Extraction performance was assessed using exact-match accuracy, weighted F1-scores, Cohen κ statistics, and tolerance-based agreement thresholds for tumor size. Robustness was evaluated across temperatures from 0 to 2.0, and technical reproducibility was assessed at a temperature of 0.1 across 3 independent runs. Results The validation dataset comprised stand-alone native-text PDF pathology reports originating from multiple Hungarian oncology centers. Input document length showed a median of 3926 (mean 4258, SD 1057, IQR 3490-4688) tokens, while generated outputs contained a median of 63 (mean 62.5, SD 8.2, IQR 56-66) tokens. At a temperature of 0.1, CIDER achieved near-human agreement with expert-curated reference database, with exact-match accuracies of 99.5% for sex, 98.1% for surgery year, 95.8% for organ, 95.6% for T stage, 92.4% for N stage, 87.5% for histology, and 78.1% for tumor size. Weighted F1-scores ranged from 0.87 for histology to 0.995 for sex, while Cohen κ values ranged from 0.85 for N stage to 0.99 for sex. For tumor size extraction, 83.5% to 85.3% and 87.3% to 88.7% of predictions were within 5 mm and 10 mm of the manually curated values, respectively. CIDER additionally generated candidate extractions for variables omitted during manual curation, including 62.8% (713/1136) of missing T stages and 91.5% (289/316) of tumor size values. Sensitivity testing revealed high robustness, with negligible variance at temperature=0.1 and stable performance at high temperatures (temperature=2.0). Conclusions CIDER demonstrates that locally deployed open-weight LLMs can reliably extract structured clinical data from complex pathology reports while preserving institutional control over sensitive data. These findings support the feasibility of secure, institutionally deployable, LLM-based extraction systems for generating research-ready datasets, facilitating clinical registry development, improving dataset completeness, and enabling scalable reuse of unstructured clinical documentation.

## 키워드

Scalability, Biobank, Robustness (evolution), Data extraction, Data collection, Inference, SNOMED CT, Information extraction, Bottleneck, Data quality

## 주제 분류 (OpenAlex Topics)

- Biomedical Text Mining and Ontologies (score: 0.705)
- Topic Modeling (score: 0.199)
- Artificial Intelligence in Healthcare and Education (score: 0.008)

## 메모

