---
title: "Explainable machine learning models for AI enabled credit scoring and financial inclusion in emerging markets"
authors: ['Yazan Taher Shawabkeh', 'Anas Ahmad Bani Atta', 'Khaled Aldarabah', 'Ahmad Marei', "Atef Badri  Al-Qur'an", 'Rana Alofishat']
year: 2026
publication_date: 2026-10-09
venue: "Discover Artificial Intelligence"
volume: "6"
issue: "1"
pages: ""
doi: "https://doi.org/10.1007/s44163-026-02392-9"
oa_status: "gold"
openalex_id: "https://openalex.org/W7221101554"
query_keyword: "social network"
tags: ['Microfinance and Financial Inclusion', 'Financial Distress and Bankruptcy Prediction', 'Explainable Artificial Intelligence (XAI)']
keywords: ['explainable machine learning', 'credit scoring', 'financial inclusion', 'microfinance', 'loan default prediction', 'algorithmic fairness', 'SHAP', 'CatBoost']
source: openalex-keyword
---

# Explainable machine learning models for AI enabled credit scoring and financial inclusion in emerging markets

**저자**: Yazan Taher Shawabkeh; Anas Ahmad Bani Atta; Khaled Aldarabah; Ahmad Marei; Atef Badri  Al-Qur'an; Rana Alofishat
**출처**: Discover Artificial Intelligence, Vol.6 No.1
**발행일**: 2026-10-09
**DOI**: https://doi.org/10.1007/s44163-026-02392-9
**수집 키워드**: social network

## 초록

This study examines whether explainable machine-learning approaches can support more inclusive credit scoring while maintaining acceptable predictive performance, transparency, and fairness in an emerging-market microfinance setting. We analyzed a de-identified dataset of 2500 resolved loan applications obtained from participating microfinance institutions in the MENA region during 2022–2023. Nine supervised algorithms were compared, spanning classical benchmarks (Logistic Regression, Decision Tree, Random Forest, Gradient Boosting, Support Vector Machine, K-Nearest Neighbors) and modern gradient-boosting frameworks (XGBoost, LightGBM, CatBoost). Default (90 + days past due) was modeled as the positive class. Performance was evaluated on a held-out test set using ROC-AUC and PR-AUC with bootstrap confidence intervals, supported by repeated stratified cross-validation and DeLong tests. Interpretability was assessed with SHAP, including stability and cross-model consistency checks, and fairness was evaluated using disparate impact, equal opportunity, predictive parity, group-level calibration, and intersectional analysis. An ablation design isolated the incremental contribution of non-traditional indicators. CatBoost achieved the highest test-set discrimination (ROC-AUC = 0.783, 95% CI [0.741, 0.825]; PR-AUC = 0.506) but was statistically indistinguishable from regularized Logistic Regression (ROC-AUC = 0.780; DeLong p = .59), and no gradient-boosting model significantly outperformed the logistic benchmark. SHAP analysis identified Credit Score Category, Utility Payment Behavior, and Repayment History as the dominant predictors, with rankings highly stable under resampling (Spearman ρ = 0.999) and consistent across model families (ρ = 0.95–0.98 among tree ensembles). Adding non-traditional indicators produced a positive but statistically non-significant incremental gain (ΔAUC = + 0.008, 95% CI [− 0.010, 0.027]). Disparate impact ratios exceeded the 0.80 heuristic for Gender (0.956), Geographic Region (0.961), and all gender-by-region intersections (0.881), with small equal-opportunity and predictive-parity gaps, although rural applicants experienced a higher false-positive rate than urban applicants (0.680 vs. 0.492). In this microfinance context, transparent and well-calibrated models matched the discrimination of complex ensembles, non-traditional indicators carried weak evidence of incremental predictive value despite meaningful within-model signal but limited incremental discrimination, and headline parity metrics coexisted with subgroup error-rate asymmetries. These findings support explainability- and governance-centered model selection for inclusive credit scoring, while underscoring the need for multi-metric fairness auditing, external validation, and continued monitoring in operational deployment.

## 키워드

explainable machine learning, credit scoring, financial inclusion, microfinance, loan default prediction, algorithmic fairness, SHAP, CatBoost, gradient boosting, model calibration, intersectional analysis, emerging markets, utility payments

## 주제 분류 (OpenAlex Topics)

- Microfinance and Financial Inclusion (score: 0.571)
- Financial Distress and Bankruptcy Prediction (score: 0.330)
- Explainable Artificial Intelligence (XAI) (score: 0.076)

## 메모

