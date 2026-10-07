---
title: "PEFT: Evaluating parameter-efficient fine-tuning for clinical-note summarization across transformers and large language models"
authors: ['Aleka Melese Ayalew', 'Md Rabiul Hasan', 'Tapio Seppänen', 'Mourad Oussalah']
year: 2026
venue: "Information Processing & Management"
tags: ['Topic Modeling', 'Machine Learning in Healthcare', 'Biomedical Text Mining and Ontologies']
source: raw/applied/applied_2026_PEFT_Evaluating_parameter_j_ipm_2026_105158.md
---

# PEFT: Evaluating parameter-efficient fine-tuning for clinical-note summarization across transformers and large language models

**저자**: Aleka Melese Ayalew; Md Rabiul Hasan; Tapio Seppänen; Mourad Oussalah
**출처**: Information Processing & Management, Vol.64, pp.105158-105158
**발행일**: 2026-09-18
**DOI**: https://doi.org/10.1016/j.ipm.2026.105158

## 초록 (원문)

The need to analyze and summarize critical information from electronic health records places a significant burden on clinicians. Clinical-note summaries are vital for making healthcare more efficient and helping healthcare personnel keep track of their paperwork. While transformer models and large language models (LLMs) are efficient in this task, the computational cost and stringent performance requirements in healthcare present major challenges. This work addresses these challenges by evaluating parameter-efficient fine-tuning with low-rank adaptations (LoRA) techniques for abstractive clinical-note summarization. We conducted a full evaluation on the MIMIC-IV-Ext-BHC dataset, comparing four transformer models (T5, PEGASUS-XSUM, BART, and FLAN-T5) and four LLMs (Mistral-7B, LLaMA-3-8B, Gemma-2-9B, and Falcon-7B) across zero-shot, full fine-tuning, and LoRA fine-tuning strategies. We also integrated LexRank, TextRank, LSA, and Luhn with clinical NLP functionalities from cTAKES for graph-based extractive summarization. In our investigation, LoRA achieved higher scores than full fine-tuning on key metrics while reducing the computational resource burden. Specifically, our LLaMA-3-8B model, fine-tuned with LoRA, achieved a ROUGE-1 score of 0.7022, ROUGE-2 of 0.5312, ROUGE-L of 0.6718, METEOR of 0.6787, and BERTScore F1 of 0.9180 on the test set. This represents a 2.6 × improvement in ROUGE-1 over the extractive baseline, though direct comparison is limited by fundamental differences between extractive and abstractive approaches. These results were accomplished using approximately 97%–99% fewer trainable parameters than full fine-tuning. The findings indicate that LoRA could facilitate the implementation of LLMs within resource-constrained medical environments, and has the potential to improve healthcare professionals’ access to information and support clinical decision-making processes.

## 키워드

Transformer, Automatic summarization, Language model, Health care, Key (lock), Health records

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

