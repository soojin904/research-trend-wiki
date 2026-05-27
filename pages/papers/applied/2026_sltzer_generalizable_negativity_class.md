---
title: "Generalizable Negativity: Classifying Negative Campaigning across German Elections"
authors: ['Marius Sältzer', 'Corinna Oschatz', 'Sebastian Stier']
year: 2026
venue: ""
tags: ['Sentiment Analysis and Opinion Mining', 'Social Media and Politics', 'Hate Speech and Cyberbullying Detection']
source: raw/applied/applied_2026_Generalizable_Negativity__n3yvc_v1.md
---

# Generalizable Negativity: Classifying Negative Campaigning across German Elections
**제목(한글)**: 일반화 가능한 네거티브 선거전: 독일 선거 데이터에 기반한 네거티브 캠페인 분류

**저자**: Marius Sältzer; Corinna Oschatz; Sebastian Stier
**출처**: , Vol.None
**발행일**: 2026-02-20
**DOI**: https://doi.org/10.31235/osf.io/n3yvc_v1

## 한국어 요약

**연구질문**: 정당 구도와 핵심 이슈가 다른 다차원 다당제 선거 판도에서, 소셜 미디어 텍스트로부터 네거티브 캠페인(NC) 전략을 포착하는 분류기가 타 선거 환경에도 우수한 일반화 성능을 유지하는가?

**방법론**:
- 2013~2021년 독일 연방 및 주 의회 선거에 참여한 후보자들의 소셜 미디어 게시물 40,000건 수집 및 수동 코딩
- 트랜스포머 기반 텍스트 분류 모델 학습 및 교차 선거 데이터 간 검증을 위한 Leave-one-out 선거 예측 검증 패러다임 도입

**주요 결과**:
- 훈련 과정에서 한 번도 노출되지 않은 주/연방 선거 데이터에 대해서도 트랜스포머 분류 모델이 안정적인 정밀도로 네거티브 캠페인을 감지하는 일반화 복원력을 입증
- 선거 단위별 이질적 맥락에서도 범용적으로 작동하는 정치 텍스트 탐지기 설계 및 검증 가이드라인을 제공함


## 초록 (원문)

Negative campaigning (NC) has become a prevalent campaign strategy in recent years, especially in interactive media such as Facebook, Twitter/X or Instagram where politicians can communicate without any mediation by gatekeepers like journalists. Even though the identification of NC is a crucial precondition for understanding modern election campaigns, the automated identification of NC is still in its infancy, even with state-of-the-art text analysis methods. Especially when researchers want to identify NC across elections and different levels of a polity, they need to develop and validate specific classifiers. As actor constellations and topics vary considerably across different elections, applying automated measures to lower-level elections requires a thorough validation of how well trained models generalize across contexts. Using several federal and state level elections as a test case, this paper investigates the generalizability of transformer models for text classification in the complex German multilevel and multiparty system. Based on over 40,000 social media posts of candidates in eight state and federal elections between 2013 and 2021 that were annotated by human coders, the classifier can identify negative campaigning across space and time. A leave-one-out classification shows that the model can accurately predict data even for unknown elections with moderately sized training data. We demonstrate how a classifier for a demanding theoretical concept can be trained and validated in multidimensional contexts and provide orientation for similar projects.

## 키워드

Generalizability theory, German, Classifier (UML), Social media, Identification (biology), Precondition

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

