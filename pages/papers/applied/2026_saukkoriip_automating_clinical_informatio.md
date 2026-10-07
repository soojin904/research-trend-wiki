---
title: "Automating clinical information retrieval from Finnish electronic health records using large language models"
authors: ['Mikko Saukkoriipi', 'Nicole Hernández', 'Jaakko Sahlsten', 'KIMMO KASKI', 'Otso Arponen']
year: 2026
venue: "npj Digital Medicine"
tags: ['Topic Modeling', 'Machine Learning in Healthcare', 'Electronic Health Records Systems']
source: raw/applied/applied_2026_Automating_clinical_infor_s41746_026_03282_1.md
---

# Automating clinical information retrieval from Finnish electronic health records using large language models

**저자**: Mikko Saukkoriipi; Nicole Hernández; Jaakko Sahlsten; KIMMO KASKI; Otso Arponen
**출처**: npj Digital Medicine, Vol.None
**발행일**: 2026-09-28
**DOI**: https://doi.org/10.1038/s41746-026-03282-1

## 초록 (원문)

Abstract Clinicians often need to search for patient-specific information within electronic health records (EHRs) containing years of heterogeneous longitudinal documentation, a task that can be time-consuming, cognitively demanding, and prone to oversight. We evaluated 14 locally deployable open-source large language models for structured patient-specific clinical information retrieval using a dataset comprising 1664 expert-annotated question–answer pairs from EHR-derived records of 183 Finnish patients undergoing breast cancer screening, diagnosis, or treatment under fully offline conditions. The records contained predominantly Finnish clinical text with occasional English and Latin terminology. The best-performing model, Llama-3.1-70B, achieved 95.3% accuracy and 97.3% consistency across semantically equivalent question formulations, while Qwen3-30B-A3B-2507 achieved comparable performance with lower measured memory use and latency under the standardized Transformers configuration. For the strongest models, accuracy was similar with and without predefined answer options in the prompt. Calibration varied across architectures, and 4-bit quantization reduced memory requirements while largely preserving accuracy. Medical-domain or Finnish-specialized models showed no systematic advantage over generalist models. Clinical review identified clinically significant errors in 2.9% of outputs, and semantically equivalent question formulations occasionally produced divergent clinical safety outcomes. These findings indicate that locally hosted open-source LLMs may support structured clinical information retrieval from longitudinal EHR-derived records, but clinically significant errors and sensitivity to question formulation remain limiting factors. Source attribution, prospective workflow validation, and human oversight are needed before clinical deployment.

## 키워드

medical information retrieval, electronic health records, large language models, medical question answering, open-source LLMs, Llama 3.1, Qwen3, low-precision quantization

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

