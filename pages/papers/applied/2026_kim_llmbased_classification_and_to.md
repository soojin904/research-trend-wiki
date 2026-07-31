---
title: "LLM-Based Classification and Topic Modeling of Generative AI Ethical Risk Discourse on Social Media"
authors: ['Soyon Kim', 'Cheolhee Yoon', 'Soo Hyung Kim', 'Bong Gyou Lee']
year: 2026
venue: "Electronics"
tags: ['Computational and Text Analysis Methods', 'Misinformation and Its Impacts', 'Risk Perception and Management']
source: raw/applied/applied_2026_LLMBased_Classification_a_electronics15142994.md
---

# LLM-Based Classification and Topic Modeling of Generative AI Ethical Risk Discourse on Social Media

**저자**: Soyon Kim; Cheolhee Yoon; Soo Hyung Kim; Bong Gyou Lee
**출처**: Electronics, Vol.15, pp.2994-2994
**발행일**: 2026-07-08
**DOI**: https://doi.org/10.3390/electronics15142994

## 초록 (원문)

Identifying sparse, context-dependent target discourse such as ethical risk discourse on generative AI in noisy social media data is a long-standing challenge in computational text analysis. Beyond classification, interpreting the resulting topic structure transparently poses an additional methodological challenge. To address these problems, this study proposes a reproducible two-stage framework. First, four LLMs (GPT-4.1, GPT-3.5-turbo, Claude Sonnet 4.6, and Gemini 2.5 Pro) are compared on a human-annotated validation set using a zero-shot prompt grounded in five ethical risk categories, and the best-performing model is selected to classify the full keyword-prescreened corpus. Validity is evaluated against human annotations and supervised baselines. Second, BERTopic is applied to the classified corpus, and sub-topics are linked to higher-level categories through an explicit mapping protocol. The study draws on approximately 500,000 ChatGPT-related English-language tweets from January to March 2023. Only 36.4% of the validation sample constituted ethical risk discourse, confirming substantial pre-screening noise. GPT-4.1, selected as the final classification model, achieved the strongest performance (accuracy = 0.899, F1 = 0.859, Cohen’s κ = 0.780), significantly outperforming conventional supervised baselines. BERTopic yielded 33 non-outlier sub-topics; within this subset, Societal and democratic risks (36.16%) and Technical safety (20.90%) were the largest categories. These findings should be interpreted not as a direct measure of users’ risk perceptions in 2023, but as the category distribution within the structured subset excluding outliers, after keyword screening and classification under the current ethical risk taxonomy used in this study. Within this scope, societal and institutional concerns were at least as prominent as those related to technical failures.

## 키워드

Generative grammar, Social media, Topic model, Generative model, Set (abstract data type), Taxonomy (biology), Sample (material), Risk assessment

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

