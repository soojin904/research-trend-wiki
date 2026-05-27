---
title: "Support Vector Machine Algorithm Optimization for Sentiment Analysis using Bayesian Optimization"
authors: ['Muhammad Resa Arif Yudianto', 'Masduki Zakariah', 'Nadhir Fachrul Rozam', 'Dzul Fadli Rahman', 'Tika Novita Sari', 'Zaenal Mustofa']
year: 2025
venue: "Jurnal Teknik Informatika dan Sistem Informasi"
tags: ['Stock Market Forecasting Methods', 'Sentiment Analysis and Opinion Mining', 'Advanced Technologies in Various Fields']
source: raw/applied/applied_2025_Support_Vector_Machine_Al_jutisi_v11i3_11524.md
---

# Support Vector Machine Algorithm Optimization for Sentiment Analysis using Bayesian Optimization

**제목(한글)**: 베이지안 최적화를 사용한 감성 분석을 위한 서포트 벡터 머신 알고리즘 최적화

## 한국어 요약

**연구질문**: 베이지안 최적화(Bayesian Optimization)가 보로부두르 사원 고객 리뷰의 측면 기반 감성 분석(ABSA) 모델에서 SVM의 분류 정확도, 계산 효율성, 환경 지속가능성을 어떻게 향상시키는가?

**방법론**:
- 보로부두르 사원 관련 988개 고객 리뷰(매력성, 시설, 접근성, 시각적 이미지, 가격, 인적자원 6개 차원 분류) 데이터셋 활용
- 기준 SVM과 베이지안 최적화(BO) 강화 SVM을 비교하며 정확도, 계산 시간, 에너지 사용, 탄소 배출 지표 측정

**주요 결과**:
- BO가 시설(0.7294→0.8682)·가격(0.8047→0.9576) 등 어려운 측면에서 정확도를 크게 향상시키고 훈련 시간과 에너지 소비를 감소
- 선형 커널은 단순 작업에, 다항식·시그모이드 커널은 복잡한 측면에서 우수하며 BO가 SVM 기준선의 한계를 실질적으로 해소

**저자**: Muhammad Resa Arif Yudianto; Masduki Zakariah; Nadhir Fachrul Rozam; Dzul Fadli Rahman; Tika Novita Sari; Zaenal Mustofa
**출처**: Jurnal Teknik Informatika dan Sistem Informasi, Vol.11, pp.383-393
**발행일**: 2025-12-15
**DOI**: https://doi.org/10.28932/jutisi.v11i3.11524

## 초록 (원문)

This study examines the effect of Bayesian Optimization in improving the performance, computational efficiency, and sustainability of Aspect-Based Sentiment Analysis models using Support Vector Machine (SVM). A dataset consisting of 988 customer reviews about Borobudur Temple, classified into six dimensions: Attractiveness, Facilities, Accessibility, Visual Image, Price, and Human Resources is used to compare two scenarios, namely Baseline SVM and SVM enhanced with Bayesian Optimization (BO). Important metrics used include accuracy, computational duration, energy usage, and carbon emissions. The results show that BO significantly improves accuracy, especially on difficult aspects such as Facilities (from 0.7294 to 0.8682) and Price (from 0.8047 to 0.9576). The most complicated aspect, namely visual image due to the very minimal number of datasets (unbalanced), achieved an increase in accuracy from 0.6729 to 0.72. In addition, BO reduces training time, especially for resource-intensive tasks such as the visual image aspect, reducing training time from 13.04 seconds to 9.4 seconds. Substantial reductions in energy consumption and CO₂ emissions are seen in line with sustainable machine learning principles. The hyperparameter adaptability of SVM, with linear kernels performing well in simpler tasks, while polynomial and sigmoid kernels improve performance for more complex parts. BO substantially alleviates the limitations of Baseline SVM, offering a robust, efficient, and environmentally friendly solution for ABSA. Future research can explore more enhancements for complex tasks to improve performance and efficiency.

## 키워드

Support vector machine, Hyperparameter, Baseline (sea), Adaptability, Hyperparameter optimization, Bayesian probability, Sigmoid function, Time complexity

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

