---
title: "From keyword-based text measures to latent variables: confirmatory factor analysis with word embeddings"
authors: ['Artur Pokropek']
year: 2026
venue: "EPJ Data Science"
tags: ['Computational and Text Analysis Methods', 'Mental Health Research Topics', 'Data Analysis with R']
source: raw/applied/applied_2026_From_keywordbased_text_me_s13688_026_00654_1.md
---

# From keyword-based text measures to latent variables: confirmatory factor analysis with word embeddings
**제목(한글)**: 키워드 기반 텍스트 측정에서 잠재 변수로: 단어 임베딩을 활용한 확인적 요인 분석

**저자**: Artur Pokropek
**출처**: EPJ Data Science, Vol.15
**발행일**: 2026-04-14
**DOI**: https://doi.org/10.1140/epjds/s13688-026-00654-1

## 한국어 요약

**연구질문**: 대규모 텍스트 코퍼스 분석에서 전통적인 사전식 키워드 지정 측정법의 한계(신뢰성 및 측정 동질성 부재)를 극복하고, 단어 임베딩의 기하학적 분포 정보에 심리학적 확인적 요인 분석(CFA)을 결합해 신뢰성 있는 잠재 변수(Latent Variables)로 정밀화할 수 있는가?

**방법론**:
- 임베딩 공간 내 단어 벡터 간의 코사인 유사도를 요인 분석용 상관 행렬 입력값으로 변환
- 확인적 요인 분석(CFA) 프레임워크를 적용하여 적합도 지수(CFI, TLI, RMSEA, SRMR) 및 신뢰도 계수(Cronbach's alpha, Omega) 산출 방법론 개발
- 2022년 러시아의 우크라이나 침공 시기 트위터 전쟁 불안(War Anxiety) 담론 데이터셋을 활용해 실증 검증 및 몬테카를로 시뮬레이션 수행

**주요 결과**:
- 키워드의 단순 빈도 집계를 넘어 단어 간 의미론적 거리 관계를 심리 측정학 수준의 정량화된 '잠재 변수'로 신뢰도 높게 변환함을 입증함
- 시기별, 그룹별 요인 적합성 검증(measurement invariance)을 수립하여 텍스트 데이터의 심리 통계적 비교 가능성을 완성함


## 초록 (원문)

Abstract Dictionary-based text analysis, where researchers select keywords to measure constructs such as public sentiment, anxiety, or political attitudes in large text corpora, is widely used in computational social science. However, keyword selection is rarely subjected to the same psychometric scrutiny applied to survey instruments: studies seldom report reliability, evaluate internal structure, or test whether the measurement holds across subpopulations or time points. Moreover, few existing methods enable the construction of measures that reflect theoretical or expected relationships among keywords. This paper proposes a method that brings these capabilities to text analysis by applying Confirmatory Factor Analysis (CFA) to word embeddings. Keywords are treated as observed indicators of a latent construct, and their semantic relationships, operationalized as centered cosine similarities between embedding vectors, serve as the input correlation matrix for CFA estimation. The framework enables researchers to estimate factor loadings and model fit indices (CFI, TLI, RMSEA, SRMR), compute reliability coefficients (Cronbach’s alpha, Omega), and test measurement invariance across groups or time periods using multigroup models with structured means. Moreover, the method allows researchers to compare latent construct intensity across groups or time periods, transforming keyword-based text measures from descriptive indicators into formally comparable latent variables. The method is demonstrated through an empirical application of the discourse of war anxiety during Russia’s 2022 invasion of Ukraine. A Monte Carlo simulation further examines the behavior of fit indices under random keyword selection. The approach complements existing text analysis methods and can be implemented using standard software, such as the lavaan R package.

## 키워드

Operationalization, Confirmatory factor analysis, Construct (python library), Reliability (semiconductor), Word (group theory), Measure (data warehouse), Measurement invariance, Test (biology)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

