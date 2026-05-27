---
title: "Investigating the impacts of missing data mechanims and treatments with latent space models"
authors: ['Tracy M. Sweet', 'Xin Qiao', 'Ashani Jayasekera', 'Yishan Ding']
year: 2026
venue: "Social Networks"
tags: ['Mental Health Research Topics', 'Statistical Methods and Bayesian Inference', 'Functional Brain Connectivity Studies']
source: raw/2026_openalex_Investigating_the_impacts_of_missing_data_j_socnet_2026_01_002.md
---

# Investigating the impacts of missing data mechanims and treatments with latent space models

**제목(한글)**: 잠재 공간 모델에서 결측 데이터 메커니즘과 처리 방식이 미치는 영향

**저자**: Tracy M. Sweet; Xin Qiao; Ashani Jayasekera; Yishan Ding
**출처**: Social Networks, Vol.86, pp.42–61
**발행일**: 2026-02-02
**DOI**: https://doi.org/10.1016/j.socnet.2026.01.002

## 한국어 요약

**연구질문**: 다양한 결측 데이터 메커니즘과 대체(imputation) 방법이 잠재 공간 모델(Latent Space Model)의 추론 및 네트워크 회복에 어떤 영향을 미치는가?

**방법론**:
- 잠재 공간 모델(Hoff et al., 2002)을 기반으로 결측 데이터 시뮬레이션 연구 수행
- 완전 사례 분석, 베이즈 추정, 회귀 대체, 다중 대체 등 다양한 처리 방법 비교
- 실제 데이터셋에 결측치를 인위적으로 부여하여 추론 정확도 평가

**주요 결과**:
- 노드 공변량이 네트워크 연결 여부를 예측하는 경우의 결측이 가장 문제적
- 완전 사례 분석과 베이즈 추정이 대체로 다른 방법과 동등하거나 우수한 성능
- 회귀 대체·다중 대체는 기대보다 낮은 성능을 보임

## 초록 (원문)

Studies on missing network data have largely focused on the impact of missing data on network structure rather than inference from a statistical model. In particular, there has very little research on the impact of missing data when fitting latent variable network models, so we examined the impact of common missing data mechanisms and subsequent missingness treatment and imputation methods when working with latent variable network models, focusing on the latent space model (Hoff et al., 2002). By removing the common definitions of missingness, our simulation study found large differences in inference, parameter, and network feature recovery based on the missingness mechanism and treatment method. In addition, we induced missingness using a real-world dataset and explored how treatment methods impacted subsequent inference and network recovery. We found that missingness based on a node covariate that also predicted network ties was the most problematic form of missingness and that complete case analysis and Bayesian estimation generally worked as well or better than other methods. • Missing data in latent space models has been studied in depth. • We explored the effects of missing data mechanisms and the treatment method. • Bayesian estimation had the lowest regression coefficient bias. • Regression imputation and multiple imputation produced worse results than expected. • We recommend multiple treatment methods when estimating models with missingness.

## 키워드

Missing data, Imputation (statistics), Covariate, Inference, Latent variable, Bayesian probability, Regression analysis, Statistical inference

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

