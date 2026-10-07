---
title: "The Illusion of Success: Learning-Based Android Malware Detectors (Replicability Study)"
authors: ['Michael Tegegn', 'Julia Rubin']
year: 2026
publication_date: 2026-10-01
venue: "Proceedings of the ACM on software engineering."
volume: "3"
issue: "ISSTA"
pages: "3247-3270"
doi: "https://doi.org/10.1145/3832233"
oa_status: "hybrid"
openalex_id: "https://openalex.org/W7215063239"
query_keyword: "social network"
tags: ['Advanced Malware Detection Techniques', 'Spam and Phishing Detection', 'Security and Verification in Computing']
keywords: ['Android malware detection', 'machine learning classifiers', 'replicability', 'AndroZoo', 'malware dataset', 'F1 score', 'binary classification']
source: openalex-keyword
---

# The Illusion of Success: Learning-Based Android Malware Detectors (Replicability Study)

**저자**: Michael Tegegn; Julia Rubin
**출처**: Proceedings of the ACM on software engineering., Vol.3 No.ISSTA, pp.3247-3270
**발행일**: 2026-10-01
**DOI**: https://doi.org/10.1145/3832233
**수집 키워드**: social network

## 초록

Since 2012, hundreds of machine-learning-based classification approaches have been proposed to help separate malware from benign Android applications. These approaches typically collect a large number of applications of both types, split them into training and testing subsets, train a binary classifier on the training subset, and measure accuracy on the testing subset. They typically report very high achieved accuracy, i.e., F1-score of around 95%. Recent work has also highlighted several biases and flaws in the experimental setup and evaluation methodology of such approaches, questioning the trustworthiness of their reported results. In an effort to better understand the current status of classification-based malware detection, we first conduct a systematic literature review to extract the properties of existing tools and the datasets that they use. We then design a large-scale longitudinal study, where we evaluate the most prominent tools on a range of datasets spanning 13 years (2011-2023), which we systematically collected from the AndroZoo and VirusShare repositories while controlling for the known experimental setup biases. Our results show lower than reported classification performance, with the F1-score for a tool ranging from high 60 to low 90 percent, depending on a dataset. Moreover, even successful classification often utilizes hidden but semantically weak correlations in the data. In fact, a deliberately naïve and unreliable classifier we designed for this study, which uses application package names as features for classification, performs comparably to and sometimes even better than the state-of-the-art tools when compared under the same setup. These results challenge the claimed detection capabilities of the tools, render comparisons of reported tool accuracy (without empirical evaluation on the exact same set of applications) practically meaningless, and call for the creation of more reliable and explainable semantic malware detection tools.

## 키워드

Android malware detection, machine learning classifiers, replicability, AndroZoo, malware dataset, F1 score, binary classification

## 주제 분류 (OpenAlex Topics)

- Advanced Malware Detection Techniques (score: 1.000)
- Spam and Phishing Detection (score: 0.000)
- Security and Verification in Computing (score: 0.000)

## 메모

