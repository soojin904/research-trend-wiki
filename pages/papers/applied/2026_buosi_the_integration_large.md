---
title: "The integration of large language models in clinical text analysis: A case study on dialysis vascular access descriptions"
authors: ['Samuele Buosi', 'Finn Krewer', 'Luke Harris', 'Harsha Deswani', 'Harry Creagh', 'Maya Ganesan', 'George Mellotte', 'Prof. Joe Eustace', 'Conor Judge', 'Edward Curry']
year: 2026
venue: "Intelligence-Based Medicine"
tags: ['Central Venous Catheters and Hemodialysis', 'Artificial Intelligence in Healthcare and Education', 'Topic Modeling']
source: raw/applied/applied_2026_The_integration_of_large__j_ibmed_2026_100428.md
---

# The integration of large language models in clinical text analysis: A case study on dialysis vascular access descriptions

**저자**: Samuele Buosi; Finn Krewer; Luke Harris; Harsha Deswani; Harry Creagh; Maya Ganesan; George Mellotte; Prof. Joe Eustace; Conor Judge; Edward Curry
**출처**: Intelligence-Based Medicine, Vol.15, pp.100428-100428
**발행일**: 2026-07-11
**DOI**: https://doi.org/10.1016/j.ibmed.2026.100428

## 초록 (원문)

Structured data extraction is a key application of Large language Models (LLMs) which can enable quality improvement initiatives and answer research questions from routinely collected clinical data. We evaluated a pretrained LLM (Meta-Llama-3.1-8B-Instruct) for classifying vascular access routes from free text unstructured dialysis notes into either Central Venous Catheter (CVC) use and ArterioVenous Fistula (AVF), both or neither. Two independent binary tasks were defined on 1,990 clinician-annotated reports (AVF prevalence 11.7%; CVC 27.1%). We compared four prompting strategies—zero-shot, 4-shot, a recall-oriented “sensitive” structured question (SEN), and a precision-oriented “specific” structured question (SPE)—and measured accuracy, precision, recall, F1, and specificity. For CVC, zero-shot achieved F1 = 77.05% and 4-shot F1 = 79.85%. SEN increased recall (80.37%; precision 63.82%; F1 = 71.15%), whereas SPE achieved the highest precision (95.00%; recall 49.26%; F1 = 64.88%). For AVF, zero-shot yielded F1 = 55.40%; 4-shot raised recall (89.56%) with lower precision (25.43%; F1 = 39.62%); SPE provided the best balance (precision 81.36%; recall 62.07%; F1 = 70.42%). These results show that even smaller domain-agnostic LLMs can extract clinically meaningful signals from free text without fine-tuning, and that prompt design affords controllable sensitivity–specificity trade-offs aligned to different clinical objectives (e.g., case-finding vs registry curation). Prospective, multi-site validation and careful integration into clinical workflows are warranted to ensure safe and reliable deployment.

## 키워드

Recall, Dialysis, Workflow, Precision and recall, Key (lock), Language model, Vascular access, Text messaging

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

