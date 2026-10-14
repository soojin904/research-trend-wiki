---
title: "Explainable detection of depression in Arabic tweets: identifying clinically meaningful linguistic markers using SHAP"
authors: ['Erfan Salehi', 'Maryam Raissi', 'Amirhossein Rasouli', 'Wajdi Zaghouani']
year: 2026
venue: "Frontiers in Artificial Intelligence"
tags: ['Mental Health via Writing', 'Sentiment Analysis and Opinion Mining', 'Artificial Intelligence in Healthcare']
source: raw/applied/applied_2026_Explainable_detection_of__frai_2026_1917139.md
---

# Explainable detection of depression in Arabic tweets: identifying clinically meaningful linguistic markers using SHAP

**저자**: Erfan Salehi; Maryam Raissi; Amirhossein Rasouli; Wajdi Zaghouani
**출처**: Frontiers in Artificial Intelligence, Vol.9
**발행일**: 2026-10-07
**DOI**: https://doi.org/10.3389/frai.2026.1917139

## 초록 (원문)

Background Depression detection models for Arabic social-media text often achieve high predictive accuracy but operate as black boxes, limiting their acceptability in clinical and public-health contexts. This study aimed to develop and evaluate an explainable machine learning framework capable of identifying clinically meaningful linguistic markers of depression in Arabic tweets. Methods We used the ArabMindGuard dataset (3,079 manually annotated tweets; 21.4% Depressed). Tweets were processed through a standard Arabic NLP pipeline and represented using TF-IDF vectorization (unigrams and bigrams). We compared six classification pipelines (Logistic Regression, Random Forest with three imbalance-handling strategies, SVM, and XGBoost) using 5-fold stratified cross-validation with TF-IDF and resampling strictly inside each fold. The primary model, Random Forest with SMOTE, was selected for its compatibility with exact TreeSHAP computations. To assess generalizability, we externally validated the model on the independent Nassar corpus ( N = 10,000). TreeSHAP was applied for interpretability, and a systematic error analysis was conducted on all false negatives and false positives. Results The RF + SMOTE model achieved an AUC-ROC of 0.80 on the held-out test set and a weighted F1-score of 0.79, with SMOTE improving depressed recall from 0.38 to 0.57 (CV recall = 0.59 ± 0.05). SHAP analysis identified مافيني (lack of energy), نفسيتي (psychological distress), خمول (lethargy), ضيقه (distress) and طاقة مافيني (I have no energy) as the most influential predictors, aligning with DSM-5 symptom domains. External validation on Nassar yielded an AUC of 0.752, with 80% (16/20) of top SHAP features overlapping across datasets. Systematic error analysis of 58 false negatives and 67 false positives revealed that false negatives consistently lacked these prototypical markers, confirming the model's interpretable decision logic. Conclusion By combining a transparent classifier with SHAP-based interpretation and cross-dataset validation, this study provides a replicable framework for surfacing clinically meaningful linguistic markers of depression in Arabic text. The approach is intended to support, rather than replace, clinical judgment, and offers a methodological template for transparent digital mental health screening tools in under-resourced languages.

## 키워드

depression detection, Arabic tweets, TreeSHAP, explainable machine learning, SMOTE, class imbalance, random forest, digital mental health

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

