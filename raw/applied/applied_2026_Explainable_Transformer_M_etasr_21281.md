---
title: "Explainable Transformer Models for Insider Threat Detection in Enterprise Systems"
authors: ['Arafat Al-Dhaqm', 'Doaa M. Bamasoud', 'Rahmah Brnawy', 'Amna Bamaqa', 'Abdulrhman A. Alharbi', 'Ibrahim Aljubayri']
year: 2026
publication_date: 2026-10-02
venue: "Engineering Technology & Applied Science Research"
volume: "16"
issue: "5"
pages: "40285-40297"
doi: "https://doi.org/10.48084/etasr.21281"
oa_status: "gold"
openalex_id: "https://openalex.org/W7218562876"
query_keyword: "social network"
tags: ['Network Security and Intrusion Detection', 'Information and Cyber Security', 'Privacy-Preserving Technologies in Data']
keywords: ['insider threat detection', 'explainable AI', 'transformer models', 'user behavior analysis', 'attention-based explanations', 'SHAP', 'feature importance', 'false positive rate']
source: openalex-keyword
---

# Explainable Transformer Models for Insider Threat Detection in Enterprise Systems

**저자**: Arafat Al-Dhaqm; Doaa M. Bamasoud; Rahmah Brnawy; Amna Bamaqa; Abdulrhman A. Alharbi; Ibrahim Aljubayri
**출처**: Engineering Technology & Applied Science Research, Vol.16 No.5, pp.40285-40297
**발행일**: 2026-10-02
**DOI**: https://doi.org/10.48084/etasr.21281
**수집 키워드**: social network

## 초록

Insider threats are difficult to detect because malicious activity is embedded in otherwise legitimate user behavior, and analysts need interpretable justifications as well as accurate alerts. This paper proposes XFT, an explainable transformer framework operating on tokenized behavioral evidence from heterogeneous enterprise logs covering authentication, removable device, file, email, and web proxy events. Each user-day is a sequence of feature tokens combining a learned value embedding with a feature identity embedding, and a transformer encoder with a classification token aggregates this evidence through multi-head self-attention. A hybrid variant fuses the transformer score with a gradient boosting score using a validation-selected weight, and an explanation layer reports attention, gradient-times-input saliency, and SHAP attributions with an agreement check. On 693,649 user-day records from CERT r5.2 the hybrid model reaches an Area Under the Receiver Operating Characteristic Curve (ROC AUC) of 0.9914, detects 92.7% of malicious user-days at a 1% false-positive budget, and confirms 158 of 261 malicious test days at a false-positive rate of 0.003%, with a paired stratified bootstrap over 300 replicates confirming the gain over gradient boosting alone. On the CERT r4.2 user-level benchmark, the strongest configurations reach 97.7% accuracy with a ROC AUC up to 0.9861. Attention correlates moderately with gradient saliency but weakly with SHAP, and a deletion audit shows that removing the three features ranked highest by attention reduces the flag score by 41%, compared with 12% for random removal.

## 키워드

insider threat detection, explainable AI, transformer models, user behavior analysis, attention-based explanations, SHAP, feature importance, false positive rate

## 주제 분류 (OpenAlex Topics)

- Network Security and Intrusion Detection (score: 0.571)
- Information and Cyber Security (score: 0.189)
- Privacy-Preserving Technologies in Data (score: 0.045)

## 메모

