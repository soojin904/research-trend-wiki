---
title: "Comparison of proprietary and fine-tuned large language models for multi-label classification of billing codes from radiology reports"
authors: ['Kamyar Arzideh', 'Henning Schäfer', 'Ahmad Idrissi-Yaghir', 'Bahadır Eryılmaz', 'Sina Warmer', 'Eva Maria Hartmann', 'Katarzyna Borys', 'Cynthia Sabrina Schmidt', 'Johannes Haubold', 'Lale Umutlu', 'Michael Forsting', 'Felix Nensa', 'René Hosch']
year: 2026
publication_date: 2026-03-14
venue: "European Radiology"
volume: "None"
issue: "None"
pages: ""
doi: "https://doi.org/10.1007/s00330-026-12445-3"
oa_status: "hybrid"
openalex_id: "https://openalex.org/W7135406814"
query_keyword: "text analysis"
tags: ['Topic Modeling', 'Machine Learning in Healthcare', 'Text and Document Classification Technologies']
keywords: ['Test (biology)', 'Schedule', 'Set (abstract data type)', 'Code (set theory)', 'Test set', 'Interventional radiology', 'Ground truth', 'Diagnosis code']
source: openalex-keyword
---

# Comparison of proprietary and fine-tuned large language models for multi-label classification of billing codes from radiology reports

**저자**: Kamyar Arzideh; Henning Schäfer; Ahmad Idrissi-Yaghir; Bahadır Eryılmaz; Sina Warmer; Eva Maria Hartmann; Katarzyna Borys; Cynthia Sabrina Schmidt; Johannes Haubold; Lale Umutlu; Michael Forsting; Felix Nensa; René Hosch
**출처**: European Radiology
**발행일**: 2026-03-14
**DOI**: https://doi.org/10.1007/s00330-026-12445-3
**수집 키워드**: text analysis

## 초록

OBJECTIVES: While large language models (LLMs) have shown promise in medical text analysis, their application in automated medical billing code extraction remains underexplored, particularly for the German medical fee schedule system (GOÄ). Therefore, an LLM was fine-tuned to perform multi-label classification of GOÄ codes from radiology reports automatically, and its performance was compared with state-of-the-art commercial and open-source LLMs. MATERIALS AND METHODS: Following ethics committee approval, we analyzed 499,601 radiology reports from 124,497 patients, containing 1,799,971 manually identified GOÄ codes as ground truth. The MediPhi-Instruct 4B model was fine-tuned using five-fold cross-validation. Performance was evaluated on the hold-out test set and compared against GPT-5, GPT-4.1, GPT-oss, Kimi-K2, Deepseek-R1, Deepseek-V3, Gemini 2.5, Llama-70B, and Qwen-3 LLMs on a subset of 500 anonymized and 350 cleaned reports using zero-shot and few-shot prompting techniques. RESULTS: The fine-tuned model achieved an accuracy of 77.15% ± 0.47% and a micro-average F1-score of 87.79% ± 0.31% on the hold-out test set. On a subset of 500 real-world samples, our models outperformed the best-performing LLM, Gemini 2.5 Flash, with an F1-score of 70.32% ± 1.54% compared to 58.22% ± 1.50% (p < 0.001). For the cleaned dataset of 350 samples, GPT-5 achieved the best F1-score of 89.51 ± 1.52% and outperformed the fine-tuned models (p < 0.001). CONCLUSIONS: Fine-tuned LLMs can effectively automate GOÄ code classification from radiology reports, with the potential of outperforming commercial LLMs. This approach shows promise for improving billing efficiency and accuracy in healthcare settings, though manual verification is still recommended. KEY POINTS: Question LLMs with high parameters possess medical knowledge, but how effective are they at predicting billing codes from radiology reports compared to smaller, fine-tuned models? Finidngs A fine-tuned ensemble model achieved competitive results and can outperform larger, proprietary LLMs. Clinical relevance Smaller, fine-tuned models offer an efficient alternative to proprietary LLMs in generating billing codes and can be integrated to assist clinical coding. This technology has the potential to transform clinical billing procedures, but its use should be overseen by qualified professional personnel.

## 키워드

Test (biology), Schedule, Set (abstract data type), Code (set theory), Test set, Interventional radiology, Ground truth, Diagnosis code

## 주제 분류 (OpenAlex Topics)

- Topic Modeling (score: 0.496)
- Machine Learning in Healthcare (score: 0.119)
- Text and Document Classification Technologies (score: 0.051)

## 메모

