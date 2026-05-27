---
title: "A hybrid approach for Bangla regional text classification using region-specific lexical oversampling and BERT ensemble learning"
authors: ['Babe Sultana', 'Ohidujjaman', 'Suman Ahmmed', 'MF Uddin', 'Mohammad Nurul Huda']
year: 2026
venue: "Array"
tags: ['Text and Document Classification Technologies', 'Authorship Attribution and Profiling', 'Sentiment Analysis and Opinion Mining']
source: raw/applied/applied_2026_A_hybrid_approach_for_Ban_j_array_2026_100817.md
---

# A hybrid approach for Bangla regional text classification using region-specific lexical oversampling and BERT ensemble learning
**제목(한글)**: 지역 특화 어휘 오버샘플링 및 BERT 앙상블 학습을 이용한 벵골어 방언 텍스트 분류 하이브리드 접근법

**저자**: Babe Sultana; Ohidujjaman; Suman Ahmmed; MF Uddin; Mohammad Nurul Huda
**출처**: Array, Vol.30, pp.100817-100817
**발행일**: 2026-04-19
**DOI**: https://doi.org/10.1016/j.array.2026.100817

## 한국어 요약

**연구질문**: 표준 벵골어와 표기 및 발음 격차가 크고 데이터가 희소한 방글라데시 5대 방언(치타공, 실헤트 등) 텍스트를 정확하게 자동 분류하기 위한 하이브리드 모델 학습 구조는 무엇인가?

**방법론**:
- 4,218개의 벵골 방언 텍스트 샘플 수집 후 방언 전문가 5인의 검수를 통해 데이터 확신도에 따라 3개 티어(Tier)로 구조화
- 불균형 문제를 해소하기 위해 도메인 검증을 거친 지역 전용 특화 단어 기반 오버샘플링(Lexical Oversampling) 기법 도입
- 3종의 BERT 아키텍처(BanglaBERT, BUETBERT, DistilBERT)를 결합한 이종 앙상블 분류 네트워크 학습 및 평가

**주요 결과**:
- 고유 정제 데이터로만 평가했을 때 기존 단독 버트 모델들의 한계(F1 67%)를 극복하고, 제안한 BERT Ensemble 모델이 최종 85.17%의 높은 정확도를 기록함을 입증
- 언어 기술의 포용성과 방언 번역 정확도를 제고하는 실무 데이터 증강 모델 구축 방안을 제시함


## 초록 (원문)

Regional text analysis reflects the lived realities of diverse communities by capturing the linguistic richness and diversity present in various dialects. It bridges the gap between everyday regional usage and standardized language forms, thereby enhancing the inclusivity of language technologies. In this paper, we focus on five regional dialects in Bangladesh, namely Chittagong, Sylhet, Noakhali, Barishal, and Rangpur, using a dataset of 4218 text samples. The dataset is validated by five regional experts and categorized into three tiers based on an assigned agreement criterion. Tier 1 represents a strictly filtered, high-confidence subset and is used primarily for evaluation. A set of region-specific special words, which belong exclusively to their respective regions and are validated by domain experts, is introduced. These words are used in a linguistically informed oversampling technique to balance the dataset in both experiments. In the first experiment, we demonstrate the effectiveness of the tiered dataset structure, where Tier 2 and Tier 3 (medium- and low-confidence subsets) are used for training, and Tier 1 (high-quality subset) is used for testing. In this setting, BanglaBERT achieves the best individual performance with 67.45% accuracy and a weighted F1-score of 67.62%. In the second experiment, we focus exclusively on the Tier 1 dataset, applying a wide range of machine learning and deep learning models to assess their effectiveness. The key contribution is a heterogeneous deep ensemble technique that combines three BERT models, BanglaBERT, BUETBERT, and DistilBERT, achieving an accuracy of 85.17% and a weighted F1-score of 84.84% on the Tier 1 dataset.

## 키워드

Oversampling, Ensemble learning, Focus (optics), Set (abstract data type), Bengali, Key (lock), Domain (mathematical analysis)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

