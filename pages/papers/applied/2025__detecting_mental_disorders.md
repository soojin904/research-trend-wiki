---
title: "Detecting Mental Disorders in Social Media Using a Transformer-Based Ensemble of Binary Classifiers"
authors: ['О. В. Овчарук', 'Olexander Mazurets', 'МАРИНА МОЛЧАНОВА', 'Alexander Kirpich', 'Pavel Skums', 'Олена Собко', 'Olexander Barmak', 'Юрий Крак', 'Sergiy Yakovlev']
year: 2025
venue: "medRxiv"
tags: ['Mental Health via Writing', 'Digital Mental Health Interventions', 'Sentiment Analysis and Opinion Mining']
source: raw/applied/applied_2025_Detecting_Mental_Disorder_2025_12_16_25342390.md
---

# Detecting Mental Disorders in Social Media Using a Transformer-Based Ensemble of Binary Classifiers

## 한국어 요약

[내용을 작성하십시오.]


**저자**: О. В. Овчарук; Olexander Mazurets; МАРИНА МОЛЧАНОВА; Alexander Kirpich; Pavel Skums; Олена Собко; Olexander Barmak; Юрий Крак; Sergiy Yakovlev
**출처**: medRxiv, Vol.None
**발행일**: 2025-12-18
**DOI**: https://doi.org/10.64898/2025.12.16.25342390

## 초록 (원문)

Abstract This study introduces a novel transformer-based ensemble framework for the multi-label detection of mental health disorders from social media posts. Unlike traditional multi-class approaches that often struggle with comorbidity, the proposed method employs a binary relevance strategy using fine-tuned DistilBERT models to identify co-occurring conditions, including depression, anxiety, and narcissistic personality disorder. To address class imbalance and optimize decision boundaries, the framework integrates a composite loss function (focal, dice, and log loss) and utilizes Youden’s J statistic for threshold calibration. Validation on textual datasets demonstrates the efficacy of this approach, with an overall F 1 -score of 0.930 and AUC values exceeding 0.89. Comparative analysis suggests that decomposing complex diagnostic tasks into independent binary problems significantly reduces inter-class confusion relative to standard multi-class baselines. Furthermore, a qualitative error analysis highlights specific linguistic challenges, such as contextual polarity shifting, metaphorical ambiguity, and colloquial usage, that impact model specificity. The findings demonstrate the potential of the proposed framework as a robust screening tool for online mental health monitoring, while underscoring the necessity of human oversight to mitigate linguistic misinterpretations. Author summary Mental health disorders such as depression, anxiety, and narcissistic personality disorder represent a major global health challenge. This work proposes a method that employs transformer-based deep learning models to analyze social media posts for mental health assessment. A significant hurdle in automated diagnosis is that these conditions often occur together (comorbidity), whereas many existing Artificial Intelligence (AI) systems are designed to detect only a single disorder at a time. This study proposes a solution using a “multi-label” deep learning framework. Rather than relying on a single multi-class classifier, the approach utilizes an ensemble of specialized binary models, each trained to detect indicators of a specific disorder. This design reduces classification confusion between clinically similar conditions, such as depression and anxiety. The method was evaluated on publicly available datasets, had an F 1 -score of 0.930 which outperformed the existing approaches. The presented approach demonstrated high effectiveness, achieving better separation between clinically similar disorders compared to traditional methods. Crucially, the detailed investigation beyond the standard statistical metrics was performed which looked into specific models mistakes. It was found that, while the presented AI model is highly sensitive, it can be confused by the specifics of the language such as metaphors (e.g., “feeling like a pressure cooker”), negations (e.g., “I am not worried”), and the colloquial clinical terms. These results highlight that AI is a powerful tool which can be used for early screening and continuous monitoring on social media, while it still requires careful calibration and human oversight to distinguish between genuine symptoms and everyday emotional expression. The findings demonstrate that analyzing social media texts with advanced machine learning techniques can serve as a powerful complementary tool to clinical diagnostics. While not intended to completely replace professional evaluation, the proposed approach can help identify potential risks, promote earlier detection of mental health disorders, support preventive interventions, and ultimately improve access to care.

## 키워드

Relevance (law), Mental health, Social media, Narcissistic personality disorder, Binary classification, Binary number, Personality, Statistic

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

