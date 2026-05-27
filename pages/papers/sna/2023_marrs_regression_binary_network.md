---
title: "Regression of binary network data with exchangeable latent errors"
authors: ['Frank W. Marrs', 'Bailey K. Fosdick']
year: 2023
venue: "Network Science"
tags: ['Complex Network Analysis Techniques', 'Opinion Dynamics and Social Influence', 'Electoral Systems and Political Participation']
source: raw/2023_openalex_Regression_of_binary_network_data_with_nws_2023_12.md
---

# Regression of binary network data with exchangeable latent errors
**제목(한글)**: 교환 가능한 잠재 오차를 가진 이진 네트워크 데이터의 회귀 분석

**저자**: Frank W. Marrs; Bailey K. Fosdick
**출처**: Network Science, Vol.11, pp.502–535
**발행일**: 2023-07-03
**DOI**: https://doi.org/10.1017/nws.2023.12

## 한국어 요약

**연구질문**: 이진 무방향 네트워크 데이터에서 행위자 내 의존성을 효율적으로 처리하면서 공변량 효과를 추정하는 방법은 무엇인가?

**방법론**:
- 교환 가능성(exchangeability) 가정 기반의 프로빗 교환 가능 모형(PX 모형) 제안
- EM 알고리즘을 활용한 근사 최대우도 추정으로 계산 효율성 달성
- 시뮬레이션 연구로 기존 잠재변수 네트워크 모형 대비 성능 비교
- 정치 성향 도서 구매 네트워크 데이터에 실증 적용

**주요 결과**:
- PX 모형이 기존 잠재변수 네트워크 모형보다 회귀 계수 추정 정확도 향상
- 실행 시간을 대폭 단축하면서 예측 성능 유지
- 정치 성향 도서 구매에서 정치적 양극화 패턴 확인

## 초록 (원문)

Abstract Undirected, binary network data consist of indicators of symmetric relations between pairs of actors. Regression models of such data allow for the estimation of effects of exogenous covariates on the network and for prediction of unobserved data. Ideally, estimators of the regression parameters should account for the inherent dependencies among relations in the network that involve the same actor. To account for such dependencies, researchers have developed a host of latent variable network models; however, estimation of many latent variable network models is computationally onerous and which model is best to base inference upon may not be clear. We propose the probit exchangeable (PX) model for undirected binary network data that is based on an assumption of exchangeability, which is common to many of the latent variable network models in the literature. The PX model can represent the first two moments of any exchangeable network model. We leverage the EM algorithm to obtain an approximate maximum likelihood estimator of the PX model that is extremely computationally efficient. Using simulation studies, we demonstrate the improvement in estimation of regression coefficients of the proposed model over existing latent variable network models. In an analysis of purchases of politically aligned books, we demonstrate political polarization in purchase behavior and show that the proposed estimator significantly reduces runtime relative to estimators of latent variable network models, while maintaining predictive performance.

## 키워드

Estimator, Latent variable, Inference, Computer science, Leverage (statistics), Probit model, Latent variable model, Regression analysis

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

