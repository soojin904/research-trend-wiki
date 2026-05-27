---
title: "Generating effective ensembles for sentiment analysis"
authors: ['Itay Etelis', 'Avi Rosenfeld', 'Abraham Itzhak Weinberg', 'David Sarne']
year: 2026
venue: "International Journal of Data Science and Analytics"
tags: ['Sentiment Analysis and Opinion Mining', 'Emotion and Mood Recognition', 'Stock Market Forecasting Methods']
source: raw/applied/applied_2026_Generating_effective_ense_s41060_025_00963_0.md
---

# Generating effective ensembles for sentiment analysis
**제목(한글)**: 감성 분석을 위한 효과적인 앙상블 생성

**저자**: Itay Etelis; Avi Rosenfeld; Abraham Itzhak Weinberg; David Sarne
**출처**: International Journal of Data Science and Analytics, Vol.22
**발행일**: 2026-03-14
**DOI**: https://doi.org/10.1007/s41060-025-00963-0

## 한국어 요약

**연구질문**: 감성 분석 영역에서 최고 정확도의 트랜스포머 단일 모델이나 단순 투표 방식의 앙상블을 넘어, 상호보완적인 이종(heterogeneous) 모델들을 그리디 방식으로 조합해 성능을 극대화하는 방법은 무엇인가?

**방법론**:
- 시뮬레이션 어닐링(Simulated Annealing)을 도입해 최적의 모델 하위 집합을 탐색하고 지역 최적해를 탈출하는 계층적 앙상블 구성(HEC) 알고리즘 제안
- SST-2, IMDB, YELP 등 8개 표준 감성 분석 데이터셋을 활용해 HEC 기반 모델과 단일 트랜스포머 앙상블, GPT-4 Zero-shot 성능 간의 비교 평가 수행

**주요 결과**:
- HEC 기반 앙상블 모델은 8개 벤치마크 데이터셋에서 평균 95.71%의 높은 정확도를 기록하며 기존 기법 대비 유의미한 성능 향상을 달성함
- 모든 모델을 결합하는 기존 방식 대신, 상호 보완적인 강점을 가진 최소한의 하위 모델만 선택적으로 결합하는 것이 효율성과 정확성 모두를 제고하는 최적 경로임을 규명함


## 초록 (원문)

Abstract In recent years, transformer models have revolutionized Natural Language Processing (NLP), achieving exceptional results across various tasks, including sentiment analysis (SA). While current state-of-the-art approaches for SA predominantly rely on transformer achieving impressive accuracy levels on benchmark datasets, we hypothesize that strategically combining transformers with traditional NLP models can yield superior performance. In this paper, we introduce the hierarchical ensemble construction (HEC) algorithm, a novel greedy-based ensemble method that differs from traditional approaches (e.g., bagging, boosting, stacking) by iteratively building ensembles from scratch using simulated annealing to escape local optima. The key innovation of HEC lies in its empirically driven approach to ensemble construction. Through systematic experimentation, we discovered that selective inclusion of heterogeneous models outperforms traditional methods that assume all available models contribute positively to ensemble performance. Unlike conventional methods that use all available base-learners with different weights, HEC selectively identifies a minimal subset of complementary models that maximizes ensemble performance. Our empirical evaluation across eight widely-used SA datasets (including SST-2, IMDB, and YELP) demonstrates that HEC-based ensembles achieve a mean accuracy of 95.71%, yielding a statistically significant improvement ( $$p &lt; 0.05$$ <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"> <mml:mrow> <mml:mi>p</mml:mi> <mml:mo>&lt;</mml:mo> <mml:mn>0.05</mml:mn> </mml:mrow> </mml:math> ) over both transformer-only ensembles and traditional ensemble methods. Specifically, HEC reduces 26.61% of the performance gap between the best individual model and perfect classification, compared to only 11.02% for traditional methods. Additionally, we provide a comparative analysis with GPT-4 using zero-shot prompting, demonstrating that HEC outperforms GPT-4 in six out of eight datasets. Our results suggest that leveraging the complementary strengths of diverse model types through intelligent ensemble construction can advance the state-of-the-art in sentiment analysis.

## 키워드

Transformer, Benchmark (surveying), Ensemble forecasting, Ensemble learning, Sentiment analysis, Language model, Natural language understanding

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

