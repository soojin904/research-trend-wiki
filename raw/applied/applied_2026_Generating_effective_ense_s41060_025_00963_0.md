---
title: "Generating effective ensembles for sentiment analysis"
authors: ['Itay Etelis', 'Avi Rosenfeld', 'Abraham Itzhak Weinberg', 'David Sarne']
year: 2026
publication_date: 2026-03-14
venue: "International Journal of Data Science and Analytics"
volume: "22"
issue: "1"
pages: ""
doi: "https://doi.org/10.1007/s41060-025-00963-0"
oa_status: "hybrid"
openalex_id: "https://openalex.org/W7135411810"
query_keyword: "social network"
tags: ['Sentiment Analysis and Opinion Mining', 'Emotion and Mood Recognition', 'Stock Market Forecasting Methods']
keywords: ['Transformer', 'Benchmark (surveying)', 'Ensemble forecasting', 'Ensemble learning', 'Sentiment analysis', 'Language model', 'Natural language understanding']
source: openalex-keyword
---

# Generating effective ensembles for sentiment analysis

**저자**: Itay Etelis; Avi Rosenfeld; Abraham Itzhak Weinberg; David Sarne
**출처**: International Journal of Data Science and Analytics, Vol.22 No.1
**발행일**: 2026-03-14
**DOI**: https://doi.org/10.1007/s41060-025-00963-0
**수집 키워드**: social network

## 초록

Abstract In recent years, transformer models have revolutionized Natural Language Processing (NLP), achieving exceptional results across various tasks, including sentiment analysis (SA). While current state-of-the-art approaches for SA predominantly rely on transformer achieving impressive accuracy levels on benchmark datasets, we hypothesize that strategically combining transformers with traditional NLP models can yield superior performance. In this paper, we introduce the hierarchical ensemble construction (HEC) algorithm, a novel greedy-based ensemble method that differs from traditional approaches (e.g., bagging, boosting, stacking) by iteratively building ensembles from scratch using simulated annealing to escape local optima. The key innovation of HEC lies in its empirically driven approach to ensemble construction. Through systematic experimentation, we discovered that selective inclusion of heterogeneous models outperforms traditional methods that assume all available models contribute positively to ensemble performance. Unlike conventional methods that use all available base-learners with different weights, HEC selectively identifies a minimal subset of complementary models that maximizes ensemble performance. Our empirical evaluation across eight widely-used SA datasets (including SST-2, IMDB, and YELP) demonstrates that HEC-based ensembles achieve a mean accuracy of 95.71%, yielding a statistically significant improvement ( $$p &lt; 0.05$$ <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"> <mml:mrow> <mml:mi>p</mml:mi> <mml:mo>&lt;</mml:mo> <mml:mn>0.05</mml:mn> </mml:mrow> </mml:math> ) over both transformer-only ensembles and traditional ensemble methods. Specifically, HEC reduces 26.61% of the performance gap between the best individual model and perfect classification, compared to only 11.02% for traditional methods. Additionally, we provide a comparative analysis with GPT-4 using zero-shot prompting, demonstrating that HEC outperforms GPT-4 in six out of eight datasets. Our results suggest that leveraging the complementary strengths of diverse model types through intelligent ensemble construction can advance the state-of-the-art in sentiment analysis.

## 키워드

Transformer, Benchmark (surveying), Ensemble forecasting, Ensemble learning, Sentiment analysis, Language model, Natural language understanding

## 주제 분류 (OpenAlex Topics)

- Sentiment Analysis and Opinion Mining (score: 0.709)
- Emotion and Mood Recognition (score: 0.016)
- Stock Market Forecasting Methods (score: 0.016)

## 메모

