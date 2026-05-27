---
title: "Early Detection of Anorexia in Blog Posts Written in English"
authors: ['Yaakov HaCohen‐Kerner', 'Natan Manor', 'Michael Goldmeier', 'Eytan Bachar']
year: 2025
venue: "ACM Transactions on Knowledge Discovery from Data"
tags: ['Mental Health via Writing', 'Sentiment Analysis and Opinion Mining', 'Eating Disorders and Behaviors']
source: raw/applied/applied_2025_Early_Detection_of_Anorex_3779415.md
---

# Early Detection of Anorexia in Blog Posts Written in English

**제목(한글)**: 영문 블로그 게시물에서 신경성 식욕부진증(거식증)의 조기 탐지

## 한국어 요약

**연구질문**: 영문 소셜 미디어 텍스트에서 신경성 식욕부진증 환자의 블로그 게시물을 기계학습 기법으로 자동 분류하는 최적 특성 조합과 모델은 무엇인가?

**방법론**:
- 거식증 여성 100개, 섭식 장애가 없는 여성 100개 블로그 게시물로 구성된 데이터셋 구축 및 전문가 검증
- 5가지 기계학습 기법, 10가지 텍스트 전처리 방법, 2가지 특성 필터링 방법 실험
- 16개 특성 집합의 휴리스틱 조합과 파라미터 최적화 적용

**주요 결과**:
- 랜덤 포레스트(random forest) 방법으로 최고 정확도 91.73% 달성(기준선 87.25% 대비 4.48% 향상)
- 내용 기반 특성 10개, 스타일 기반 특성 6개, 감성 기반 특성 2개로 구성된 16개 특성 집합이 최적
- 전통적 기계학습이 딥러닝보다 우수한 성능을 보이는 반복적 현상이 다시 확인됨

**저자**: Yaakov HaCohen‐Kerner; Natan Manor; Michael Goldmeier; Eytan Bachar
**출처**: ACM Transactions on Knowledge Discovery from Data, Vol.20, pp.1-28
**발행일**: 2025-12-12
**DOI**: https://doi.org/10.1145/3779415

## 초록 (원문)

This study concentrates on identifying girls with anorexia nervosa through English social media text analysis. A dataset was created comprising 100 blog posts authored by females who have anorexia and another 100 posts written by females likely without an eating disorder. A psychology professor who is an international expert on anorexia confirmed the collected posts. We perform an in-depth series of experiments that utilize multiple sets of textual features, different text classification models, including 5 machine learning techniques, 10 basic text preprocessing methods, 2 feature filtering methods, and parameter optimization procedures. The best accuracy result of 91.73% was obtained by the random forest machine learning method using a combination of 16 feature sets derived by a heuristic process of combining feature sets and parameter tuning. This result is 4.48% higher than the baseline (87.25%). Among the 16 feature sets, 10 are content-based, containing features that, to one degree or another, describe anorexic girls. A relatively high number of feature sets (6 out of 16) were style-based, while two were sentiment-based. A notable recurring observation across various classification studies, including the present study, is that traditional machine learning techniques tend to outperform deep learning methods. We also present a comparison of the results and findings of this study in English and those of a similar study performed by us using a dataset in Hebrew.

## 키워드

Feature (linguistics), Anorexia nervosa, Preprocessor, Anorexia, Random forest, Heuristic, Feature selection

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

