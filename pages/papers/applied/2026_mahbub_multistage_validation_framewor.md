---
title: "A Multi-Stage Validation Framework for Trustworthy Large-scale Clinical Information Extraction using Large Language Models"
authors: ['Maria Mahbub', 'Gregory M. Dams', 'Josh A. Arnold', 'Caitlin Rizy', 'Sudarshan Srinivasan', 'Elliot M. Fielstein', 'Minu A. Aghevli', 'Kamonica Craig', 'Elizabeth M. Oliva', 'Joseph Erdos', 'Jodie Trafton', 'Ioana Danciu']
year: 2026
venue: "arXiv (Cornell University)"
tags: ['Topic Modeling', 'Biomedical Text Mining and Ontologies', 'Machine Learning in Healthcare']
source: raw/applied/applied_2026_A_MultiStage_Validation_F_nodoi.md
---

# A Multi-Stage Validation Framework for Trustworthy Large-scale Clinical Information Extraction using Large Language Models

**저자**: Maria Mahbub; Gregory M. Dams; Josh A. Arnold; Caitlin Rizy; Sudarshan Srinivasan; Elliot M. Fielstein; Minu A. Aghevli; Kamonica Craig; Elizabeth M. Oliva; Joseph Erdos; Jodie Trafton; Ioana Danciu
**출처**: arXiv (Cornell University), Vol.None
**발행일**: 2026-04-07
**DOI**: 

## 초록 (원문)

Large language models (LLMs) show promise for extracting clinically meaningful information from unstructured health records, yet their translation into real-world settings is constrained by the lack of scalable and trustworthy validation approaches. Conventional evaluation methods rely heavily on annotation-intensive reference standards or incomplete structured data, limiting feasibility at population scale. We propose a multi-stage validation framework for LLM-based clinical information extraction that enables rigorous assessment under weak supervision. The framework integrates prompt calibration, rule-based plausibility filtering, semantic grounding assessment, targeted confirmatory evaluation using an independent higher-capacity judge LLM, selective expert review, and external predictive validity analysis to quantify uncertainty and characterize error modes without exhaustive manual annotation. We applied this framework to extraction of substance use disorder (SUD) diagnoses across 11 substance categories from 919,783 clinical notes. Rule-based filtering and semantic grounding removed 14.59% of LLM-positive extractions that were unsupported, irrelevant, or structurally implausible. For high-uncertainty cases, the judge LLM's assessments showed substantial agreement with subject matter expert review (Gwet's AC1=0.80). Using judge-evaluated outputs as references, the primary LLM achieved an F1 score of 0.80 under relaxed matching criteria. LLM-extracted SUD diagnoses also predicted subsequent engagement in SUD specialty care more accurately than structured-data baselines (AUC=0.80). These findings demonstrate that scalable, trustworthy deployment of LLM-based clinical information extraction is feasible without annotation-intensive evaluation.

## 키워드

Medical diagnosis, Matching (statistics), Subject-matter expert, Scalability, Information extraction, Comparability, Population, Trustworthiness

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

