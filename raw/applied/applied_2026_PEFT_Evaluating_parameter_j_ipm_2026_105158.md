---
title: "PEFT: Evaluating parameter-efficient fine-tuning for clinical-note summarization across transformers and large language models"
authors: ['Aleka Melese Ayalew', 'Md Rabiul Hasan', 'Tapio Seppänen', 'Mourad Oussalah']
year: 2026
publication_date: 2026-09-18
venue: "Information Processing & Management"
volume: "64"
issue: "2"
pages: "105158-105158"
doi: "https://doi.org/10.1016/j.ipm.2026.105158"
oa_status: "hybrid"
openalex_id: "https://openalex.org/W7213547867"
query_keyword: "text analysis"
tags: ['Topic Modeling', 'Machine Learning in Healthcare', 'Biomedical Text Mining and Ontologies']
keywords: ['Transformer', 'Automatic summarization', 'Language model', 'Health care', 'Key (lock)', 'Health records']
source: openalex-keyword
---

# PEFT: Evaluating parameter-efficient fine-tuning for clinical-note summarization across transformers and large language models

**저자**: Aleka Melese Ayalew; Md Rabiul Hasan; Tapio Seppänen; Mourad Oussalah
**출처**: Information Processing & Management, Vol.64 No.2, pp.105158-105158
**발행일**: 2026-09-18
**DOI**: https://doi.org/10.1016/j.ipm.2026.105158
**수집 키워드**: text analysis

## 초록

The need to analyze and summarize critical information from electronic health records places a significant burden on clinicians. Clinical-note summaries are vital for making healthcare more efficient and helping healthcare personnel keep track of their paperwork. While transformer models and large language models (LLMs) are efficient in this task, the computational cost and stringent performance requirements in healthcare present major challenges. This work addresses these challenges by evaluating parameter-efficient fine-tuning with low-rank adaptations (LoRA) techniques for abstractive clinical-note summarization. We conducted a full evaluation on the MIMIC-IV-Ext-BHC dataset, comparing four transformer models (T5, PEGASUS-XSUM, BART, and FLAN-T5) and four LLMs (Mistral-7B, LLaMA-3-8B, Gemma-2-9B, and Falcon-7B) across zero-shot, full fine-tuning, and LoRA fine-tuning strategies. We also integrated LexRank, TextRank, LSA, and Luhn with clinical NLP functionalities from cTAKES for graph-based extractive summarization. In our investigation, LoRA achieved higher scores than full fine-tuning on key metrics while reducing the computational resource burden. Specifically, our LLaMA-3-8B model, fine-tuned with LoRA, achieved a ROUGE-1 score of 0.7022, ROUGE-2 of 0.5312, ROUGE-L of 0.6718, METEOR of 0.6787, and BERTScore F1 of 0.9180 on the test set. This represents a 2.6 × improvement in ROUGE-1 over the extractive baseline, though direct comparison is limited by fundamental differences between extractive and abstractive approaches. These results were accomplished using approximately 97%–99% fewer trainable parameters than full fine-tuning. The findings indicate that LoRA could facilitate the implementation of LLMs within resource-constrained medical environments, and has the potential to improve healthcare professionals’ access to information and support clinical decision-making processes.

## 키워드

Transformer, Automatic summarization, Language model, Health care, Key (lock), Health records

## 주제 분류 (OpenAlex Topics)

- Topic Modeling (score: 0.652)
- Machine Learning in Healthcare (score: 0.135)
- Biomedical Text Mining and Ontologies (score: 0.050)

## 메모

