---
title: "ESG-SASB Label Stability: A Curated Benchmark and Reproducible Pipeline for Reusing Sentence-Level Sustainability Disclosure Labels"
authors: ['Yufei Li', 'Tianhao Chen', 'Wei Ke', 'Patrick Cheong‐Iao Pang']
year: 2026
venue: "Informatics"
tags: ['Computational and Text Analysis Methods', 'Sentiment Analysis and Opinion Mining', 'Green IT and Sustainability']
source: raw/applied/applied_2026_ESGSASB_Label_Stability_A_informatics13070106.md
---

# ESG-SASB Label Stability: A Curated Benchmark and Reproducible Pipeline for Reusing Sentence-Level Sustainability Disclosure Labels

**저자**: Yufei Li; Tianhao Chen; Wei Ke; Patrick Cheong‐Iao Pang
**출처**: Informatics, Vol.13, pp.106-106
**발행일**: 2026-07-03
**DOI**: https://doi.org/10.3390/informatics13070106

## 초록 (원문)

Annotated text datasets are increasingly reused as classifier targets, annotation candidates, and inputs to aggregate profiles, yet their labels often circulate without enough information about how they were produced. This article presents a reproducible benchmark and validation workflow for the public SASB-Aligned ESG Sentences corpus, a sentence-level sustainability disclosure dataset organized around standards-based categories such as those used in Sustainability Accounting Standards Board (SASB) analytics. Using the downloaded 6460-row version of the corpus, we construct fixed train/validation/test splits, map released child labels to parent categories, and evaluate label reuse through supervised classifiers, prompted GPT-4o classification, blind and candidate-visible Claude annotation, and Monte Carlo aggregation into ESG/Non-ESG category profiles. The reproducibility artifacts provide split metadata, label mappings, prompt templates, model predictions, LLM annotation outputs, profile sensitivity outputs, figure inputs, and scripts for reproducing the reported tables and figures. Results show that label reproduction is strongest at coarser label levels, blind annotation flags 40.3% of held-out sentences as ambiguous, candidate-visible annotation increases agreement while changing the task format, and aggregate profiles remain sensitive to label source. The benchmark supports transparent reuse of sentence-level ESG labels by reporting label source, annotation condition, prompt family, and aggregation level.

## 키워드

Annotation, Pipeline (software), Benchmark (surveying), Workflow, Reuse, Scripting language, Precision and recall

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

