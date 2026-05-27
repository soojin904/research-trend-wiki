---
title: "Machine Learning based Fake Review Detection with Price Analysis"
authors: ['D. Pradeep', 'Dharun Kanna N', 'Kavin C', 'Mithul S']
year: 2026
venue: ""
tags: ['Spam and Phishing Detection', 'Sentiment Analysis and Opinion Mining', 'Digital Marketing and Social Media']
source: raw/applied/applied_2026_Machine_Learning_based_Fa_icsadl67539_2026_11452020.md
---

# Machine Learning based Fake Review Detection with Price Analysis
**제목(한글)**: 가격 분석을 접목한 머신러닝 기반 가짜 리뷰 탐지 기술

**저자**: D. Pradeep; Dharun Kanna N; Kavin C; Mithul S
**출처**: , Vol.None, pp.390-395
**발행일**: 2026-02-18
**DOI**: https://doi.org/10.1109/icsadl67539.2026.11452020

## 한국어 요약

**연구질문**: 평점과 본문 글이 교묘하게 조작된 고도화된 가짜 리뷰(봇 작성 등)를 적발하기 위해, 텍스트 분석에 제품 '가격 메타데이터'를 융합하는 탐지 방법론의 정확성은 어떠한가?

**방법론**:
- 리뷰어 정보 및 평점 주기를 입력받는 XGBoost 분류기와 문맥 특징을 추출하는 미세조정 BERT 모델의 하이브리드 결합
- 제품 가격과 구매자 감성 간의 괴리를 추적하는 '가격 감성 불일치 지표(PSIS)' 신규 개발 및 메타 분류기(Meta-classifier) 학습

**주요 결과**:
- 텍스트나 사용자 행동 정보만을 사용하던 기존 기법 대비 가격 변수(PSIS)를 통합했을 때 가짜 리뷰 판별력이 획기적으로 개선됨을 검증함
- 전자상거래 플랫폼에서 상품 유통 신뢰도를 실시간 보호할 안정적이고 신뢰성 높은 이상 징후 필터링 모델을 제시함


## 초록 (원문)

The fast-growing e-commerce has brought an overdependence on consumers on online reviews when making purchasing decisions. The problem of fake reviews, which are purposely made or manipulated content, is a real menace to consumer confidence and product image, however. The current detection algorithms are limited to analyzing the text or behavioral patterns of the reviewers, which not always work well with advanced manipulations, e.g. sentiment-balanced reviews or bot-written ones. In this paper, a hybrid machine learning model combining deep learning text analysis with price-based metadata will be suggested to detect fraudulent reviews better. An XGBoost classifier is trained on reviewer metadata, review frequency, helpfulness ratings, verified purchase and a novel Price Sentiment Inconsistency Score (PSIS) to detect oddities in price, rating, and sentiment relationships between product price and sentiment. A refined version of BERT is used to derive semantic and contextual features of text reviews, and is trained using a reviewer metadata, review frequency and helpfulness ratings, verified purchase status, and new Price Sentiment Inconsistency Score (PSIS). The two models are combined with the help of a meta-classifier to create a powerful ensemble that is able to detect subtle strategies of review manipulation. The results of the experiment prove that the use of price-related measurements leads to the better classification performance than text-only or behavior-only approaches. The suggested solution is scalable and can be implemented in a real-life e- commerce platform to offer a feasible solution of ensuring that online reviews are not tampered with.

## 키워드

Helpfulness, Sentiment analysis, Metadata, Purchasing, Product (mathematics), Classifier (UML), Flagging, Deep learning

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

