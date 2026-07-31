---
title: "A Hybrid Generative Adversarial Network and Random Forest Architecture for Enhanced Fraud Detection in Unified Payments Interface (UPI) Systems"
authors: ['Hiteshkumar M. Nimbark', 'Hansiniba P. Jadeja', 'Evan Habibani']
year: 2026
publication_date: 2026-07-26
venue: "DMPedia Lecture Notes in Computer Science & Engineering"
volume: "None"
issue: "None"
pages: "1-12"
doi: "https://doi.org/10.65890/dmp-lncse.iciccs26.181"
oa_status: "hybrid"
openalex_id: "https://openalex.org/W7171332501"
query_keyword: "social network"
tags: ['Imbalanced Data Classification Techniques', 'Electricity Theft Detection Techniques', 'Financial Distress and Bankruptcy Prediction']
keywords: ['Random forest', 'Adversarial system', 'Oversampling', 'Classifier (UML)', 'Payment', 'USable', 'Hyperparameter', 'Database transaction']
source: openalex-keyword
---

# A Hybrid Generative Adversarial Network and Random Forest Architecture for Enhanced Fraud Detection in Unified Payments Interface (UPI) Systems

**저자**: Hiteshkumar M. Nimbark; Hansiniba P. Jadeja; Evan Habibani
**출처**: DMPedia Lecture Notes in Computer Science & Engineering, pp.1-12
**발행일**: 2026-07-26
**DOI**: https://doi.org/10.65890/dmp-lncse.iciccs26.181
**수집 키워드**: social network

## 초록

Financial fraud in digital payment systems is a major cybersecurity issue. Global losses exceed $32 billion each year, and fraud-detection methods are constantly improving to keep pace with increasingly complex attack patterns. One significant challenge in fraud analytics is the severe class imbalance. Fraudulent transactions make up a very small fraction of total transaction volume. This study introduces a new detection framework that combines Generative Adversarial Networks (GANs) for synthesising minority classes with Random Forest (RF) ensemble learning for strong classification. The GAN part is based on adversarial training methods introduced earlier, with improved stabilisation techniques from recent studies and tabular data modelling strategies from previous research. The Random Forest classifier uses the ensemble approach first defined in earlier work. In this paper, a synthetic dataset featuring 20,000 transactions and 20 engineered features is presented. This set includes transactional, behavioural, device-based, and contextual information. The GAN uses a 100-dimensional latent-space generator and a binary discriminator, trained for 1,000 epochs with the Adam optimiser. We tuned the hyperparameters of the RF classifier using GridSearchCV with 5-fold cross-validation, resulting in the best parameters: n_estimators=100, max_depth=20, and min_samples_split=5. These experiments show an overall accuracy of 97.09%, with balanced precision and recall metrics at 0.97. This outperforms the baseline RF (96.75%), SMOTE-RF (96.82%), and XGBoost (96.91%). Adding 5,000 GAN-synthesised minority samples, generated using adversarial oversampling techniques, increased validation accuracy to 97.12% (p &lt; 0.05, McNemar’s test). Analysis of feature importance showed that geo-location anomaly flags (24.95%) and previous fraudulent behaviour indicators (20.41%) were the most distinguishing attributes. The proposed hybrid GAN-RF framework effectively addresses class imbalance while maintaining computational efficiency and model interpretability. It shows strong promise for use in real-time fraud detection in Unified Payments Interface (UPI) environments.

## 키워드

Random forest, Adversarial system, Oversampling, Classifier (UML), Payment, USable, Hyperparameter, Database transaction, Generative grammar, Binary classification

## 주제 분류 (OpenAlex Topics)

- Imbalanced Data Classification Techniques (score: 0.830)
- Electricity Theft Detection Techniques (score: 0.019)
- Financial Distress and Bankruptcy Prediction (score: 0.016)

## 메모

