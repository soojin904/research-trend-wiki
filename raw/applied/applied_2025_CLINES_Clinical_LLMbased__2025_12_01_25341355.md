---
title: "CLINES: Clinical LLM-based Information Extraction and Structuring Agent"
authors: ['Zongxin Yang', 'Hongyi Yuan', 'Raheel Sayeed', 'Amelia Li Min Tan', 'Enci Cai', 'Michele Moro', 'Xiudi Li', 'Huaiyuan Ying', 'Nicholas Brown', 'Griffin M. Weber', 'Sheng Yu', 'Isaac S. Kohane', 'Tianxi Cai']
year: 2025
publication_date: 2025-12-02
venue: "medRxiv"
volume: "None"
issue: "None"
pages: ""
doi: "https://doi.org/10.64898/2025.12.01.25341355"
oa_status: "green"
openalex_id: "https://openalex.org/W4417152296"
query_keyword: "text analysis"
tags: ['Topic Modeling', 'Biomedical Text Mining and Ontologies', 'Machine Learning in Healthcare']
keywords: ['Transformer', 'Assertion', 'Modular design', 'Electronic health record', 'Medical record', 'Recall', 'Normalization (sociology)', 'Inference']
source: openalex-keyword
---

# CLINES: Clinical LLM-based Information Extraction and Structuring Agent

**저자**: Zongxin Yang; Hongyi Yuan; Raheel Sayeed; Amelia Li Min Tan; Enci Cai; Michele Moro; Xiudi Li; Huaiyuan Ying; Nicholas Brown; Griffin M. Weber; Sheng Yu; Isaac S. Kohane; Tianxi Cai
**출처**: medRxiv
**발행일**: 2025-12-02
**DOI**: https://doi.org/10.64898/2025.12.01.25341355
**수집 키워드**: text analysis

## 초록

Abstract Background Clinical narratives in electronic health records (EHRs) contain essential diagnostic, therapeutic, and temporal information that is often missing from structured fields, leaving manual chart review as the de facto standard for high-quality labels, but slow, costly, and variable, thereby constraining accurate cohort construction for clinical trials, large-scale epidemiologic studies, and the development of robust machine-learning models. Methods We developed CLINES, a modular agentic pipeline that extracts and structures clinical concepts: semantic chunking of long notes; extraction by reasoningcapable large language models; assignment of attributes (assertion/experiencer, numerical values with SI units); normalization to the Unified Medical Language System (UMLS); resolution of explicit and relative dates; and aggregation into an i2b2-style schema. Zero-shot evaluation was conducted on de-identified EHR: MIMIC-III notes, 4CE notes, and CORAL oncology reports (breast, pancreas). Comparators included rule/lexicon systems, transformer encoders, and single-prompt LLM baselines. Outcomes were F1 scores for entity extraction, assertion status, value&amp;unit extraction, and date processing. Findings Across all datasets, CLINES led every baseline. F1 scores (entity / assertion / value&amp;unit / date) were: MIMIC-III 0.69 / 0.93 / 0.90 (date not evaluated); 4CE 0.87 / 0.88 / 0.79 / 0.79; CORAL–Breast 0.81 / 0.84 / 0.77 / 0.73; CORAL–Pancreas 0.85 / 0.87 / 0.90 / 0.78. Gains over the strongest single-prompt LLM were +0.21–0.38 across tasks, and transformer encoders trailed by +0.28–0.68 F1 on entity extraction. Performance remained stable across note-length quantiles, while transformer baselines lost recall as notes lengthened. Interpretation CLINES translates narrative text from electronic health records into ontology-grounded, auditable, and schema-ready data, offering a practical route to scale chart-review-like extraction for cohort discovery and real-world evidence. CLINES is model agnostic–different open and close models can be substituted to achieve specific cost, performance, and privacy goals. Future work aims to quantify inter-annotator agreements and explore adaptive feedback and domain-specific fine-tuning.

## 키워드

Transformer, Assertion, Modular design, Electronic health record, Medical record, Recall, Normalization (sociology), Inference, Information extraction, Parsing

## 주제 분류 (OpenAlex Topics)

- Topic Modeling (score: 0.375)
- Biomedical Text Mining and Ontologies (score: 0.313)
- Machine Learning in Healthcare (score: 0.167)

## 메모

