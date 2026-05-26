---
title: "Circular specifications and “predicting” with information from the future: Errors in the empirical SAOM–TERGM comparison of Leifeld &amp; Cranmer"
authors: ['Per Block', 'James Hollway', 'Christoph Stadtfeld', 'Johan Koskinen', 'Tom A. B. Snijders']
year: 2022
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'Advanced Clustering Algorithms Research', 'Mental Health Research Topics']
source: raw/2022_openalex_Circular_specifications_and_predicting_with_information_nws_2022_6.md
---

# Circular specifications and “predicting” with information from the future: Errors in the empirical SAOM–TERGM comparison of Leifeld &amp; Cranmer
**제목(한글)**: 순환 명세와 미래 정보를 이용한 '예측': Leifeld & Cranmer의 SAOM-TERGM 실증 비교의 오류

**저자**: Per Block; James Hollway; Christoph Stadtfeld; Johan Koskinen; Tom A. B. Snijders
**출처**: Network Science, Vol.10, pp.3–14
**발행일**: 2022-03-01
**DOI**: https://doi.org/10.1017/nws.2022.6


## 한국어 요약

**연구질문**: Leifeld & Cranmer(2019)의 SAOM(확률적 행위자 지향 모델) vs. TERGM(시간적 지수 랜덤 그래프 모델) 비교 연구에서 어떤 방법론적 오류가 있으며, 그 영향은 무엇인가?

**방법론**:
- Leifeld & Cranmer(2019)의 TERGM 모델 명세(specification) 재검토
- 표본 외 예측에서 미래 관측값 사용 여부 분석
- 유대 수준 예측 정확도를 모델 비교 지표로 사용하는 적절성 논의

**주요 결과**:
- TERGM 명세 시 외인성(exogenous) 절점 속성 대신 결과 네트워크의 관측 차수를 사용해 내생성이 순환으로 전환됨
- 표본 외 예측이 미래 관측값에 의존하게 되어 결론이 동어반복적임
- 유대 예측 정확도는 내생적 네트워크 과정 모델링 목적에는 적합하지 않은 평가 지표임


## 초록 (원문)

Abstract We review the empirical comparison of Stochastic Actor-oriented Models (SAOMs) and Temporal Exponential Random Graph Models (TERGMs) by Leifeld &amp; Cranmer in this journal [Network Science 7(1):20–51, 2019]. When specifying their TERGM, they use exogenous nodal attributes calculated from the outcome networks’ observed degrees instead of endogenous ERGM equivalents of structural effects as used in the SAOM. This turns the modeled endogeneity into circularity and obtained results are tautological. In consequence, their out-of-sample predictions using TERGMs are based on out-of-sample information and thereby predict the future using observations from the future. Thus, their analysis rests on erroneous model specifications that invalidate the article’s conclusions. Finally, beyond these specific points, we argue that their evaluation metric—tie-level predictive accuracy—is unsuited for the task of comparing model performance.

## 키워드

Endogeneity, Covariate, Sample (material), Computer science, Econometrics, Specification, Mathematics, Machine learning

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

