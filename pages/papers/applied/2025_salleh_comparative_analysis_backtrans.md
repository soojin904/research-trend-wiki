---
title: "COMPARATIVE ANALYSIS OF BACK-TRANSLATION MODELS FOR NORMALIZATION MOBILE APP USER REVIEWS"
authors: ['Amran Salleh', 'Mohd Hafeez Osman', 'Sa’adah Hassan', 'Mar Yah Said']
year: 2025
venue: "International Journal of Computer Systems & Software Engineering"
tags: ['Sentiment Analysis and Opinion Mining', 'Spam and Phishing Detection', 'Authorship Attribution and Profiling']
source: raw/applied/applied_2025_COMPARATIVE_ANALYSIS_OF_B_ijsecs_11_2_2025_10_0142.md
---

# COMPARATIVE ANALYSIS OF BACK-TRANSLATION MODELS FOR NORMALIZATION MOBILE APP USER REVIEWS

**저자**: Amran Salleh; Mohd Hafeez Osman; Sa’adah Hassan; Mar Yah Said
**출처**: International Journal of Computer Systems & Software Engineering, Vol.11, pp.124-136
**발행일**: 2025-12-18
**DOI**: https://doi.org/10.15282/ijsecs.11.2.2025.10.0142

## 초록 (원문)

The increase of mobile apps has led to an exponential growth of user-generated reviews, which are often noisy, informal, and linguistically diverse, thereby posing significant challenges for automated analysis in requirements engineering. This study evaluates whether back-translation (BT) can normalize informal reviews while preserving meaning, and which model (Google Translate vs Facebook M2M100_418M) offers better semantic preservation, grammatical quality, and lexical alignment. We collected 323 Google Play reviews (667 sentences) from three Malaysian government apps. Texts were cleaned, expanded for colloquial forms, and then BT was applied using Malay as an intermediate language. Evaluation used four metrics which are semantic similarity (Sentence-BERT), grammar error count (LanguageTool), BLEU (NLTK), and perplexity (GPT-2). Models differences were tested with paired t-tests and Wilcoxon signed- rank tests, while paired scatterplots showed distributional patterns. Google was significantly better on semantic similarity (t(322)=5.38, p&lt;.001), grammar errors (t(322)=3.66, p&lt;.001), and BLEU (t(322)=2.99, p=.003); effect sizes were small to moderate. Perplexity differences were not significant, indicating comparable sentence-level fluency. Visualizations confirmed Google’s steadier performance with fewer extreme outliers. BT is a practical normalization step for noisy reviews. For the English–Malay pipeline studied here, Google provides more reliable semantic preservation and grammatical quality, while both systems are similar in fluency. However, the generalizability of these results are constrained by the relatively modest sample size (323 reviews, 667 sentences), and future work should validate results on large datasets and explore hybrid strategies combining strengths of both models.

## 키워드

Perplexity, Normalization (sociology), Generalizability theory, Semantic similarity, Grammar, Latent semantic analysis, Bridging (networking), Vocabulary

## 위키 연관

- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모

