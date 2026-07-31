---
title: "Development of A Prototype For Detecting Sexual Harassment Speech In Instagram Comments"
authors: ['Ziyan Zatusy Syajar', 'Wiyli Yustanti', 'Benhur Ravuri']
year: 2026
venue: "Journal of Artificial Intelligence and Data Science"
tags: ['Hate Speech and Cyberbullying Detection', 'Sentiment Analysis and Opinion Mining', 'Linguistics and Language Analysis']
source: raw/applied/applied_2026_Development_of_A_Prototyp_jaids_v2i2_4.md
---

# Development of A Prototype For Detecting Sexual Harassment Speech In Instagram Comments

**저자**: Ziyan Zatusy Syajar; Wiyli Yustanti; Benhur Ravuri
**출처**: Journal of Artificial Intelligence and Data Science, Vol.2, pp.34-44
**발행일**: 2026-07-29
**DOI**: https://doi.org/10.67561/jaids.v2i2.4

## 초록 (원문)

Verbal sexual harassment in the comment sections of Instagram is an increasingly alarming issue, but currently, the platform does not have an automated detection system that can identify harassing speech at the moment of publication. This research compares nine classification models, consisting of six machine learning algorithms (Logistic Regression, Support Vector Machine, Multinomial Naive Bayes, Random Forest, K-Nearest Neighbors, and XGBoost) with Term Frequency-Inverse Document Frequency (TF-IDF) representation, and three deep learning models (Convolutional Neural Network (CNN) with FastText, IndoBERT, and IndoBERT-CNN) on a dataset of 2,000 manually labeled Indonesian Instagram comments. Hyperparameter optimization was carried out by Grid Search with 10-fold cross-validation in the framework of Knowledge Discovery in Databases (KDD). Preprocessing steps included case folding, elongation normalization, emoji removal, leetspeak normalization and cleaning text. Results indicate that deep learning models outperformed machine learning models for all evaluation metrics. Both IndoBERT and IndoBERT-CNN obtained the highest accuracy and F1-score of 0.960. The best model is IndoBERT because it has a higher recall value of 0.970 and faster training time of 111.56 seconds compared to IndoBERT-CNN with 199.62 seconds. The chosen IndoBERT model was then integrated into a web prototype based on Django. Black-box testing was performed to verify that all features worked as expected, including the automatic blocking of harassing comments with a warning message for the user.

## 키워드

Preprocessor, Normalization (sociology), Support vector machine, Hyperparameter optimization, Random forest, Artificial neural network, Recall, Deep learning

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

