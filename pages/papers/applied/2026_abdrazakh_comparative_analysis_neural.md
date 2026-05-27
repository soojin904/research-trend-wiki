---
title: "Comparative Analysis of Neural Network Architectures for Classifying Depressive Content in Social Networks"
authors: ['Yntymak Abdrazakh', 'Rita İsmailova', 'Nurseit Zhunissov', 'Arypzhan Aben', 'Anuarbek Amanov', 'Aigerim Baimakhanova']
year: 2026
venue: "International Journal of Advanced Computer Science and Applications"
tags: ['Mental Health via Writing', 'Digital Mental Health Interventions', 'Sentiment Analysis and Opinion Mining']
source: raw/applied/applied_2026_Comparative_Analysis_of_N_ijacsa_2026_0170237.md
---

# Comparative Analysis of Neural Network Architectures for Classifying Depressive Content in Social Networks
**제목(한글)**: 소셜 네트워크상 우울증 관련 콘텐츠 분류를 위한 신경망 아키텍처의 비교 분석

**저자**: Yntymak Abdrazakh; Rita İsmailova; Nurseit Zhunissov; Arypzhan Aben; Anuarbek Amanov; Aigerim Baimakhanova
**출처**: International Journal of Advanced Computer Science and Applications, Vol.17
**발행일**: 2026-01-01
**DOI**: https://doi.org/10.14569/ijacsa.2026.0170237

## 한국어 요약

**연구질문**: 소셜 미디어 플랫폼(Reddit, Twitter, Facebook) 간의 도메인 변화와 클래스 불균형이 우울증 징후 텍스트 분류 모델 선택에 어떤 영향을 미치며, 통계적 신뢰성을 확보할 수 있는 방법은 무엇인가?

**방법론**:
- CNN, LSTM 및 트랜스포머 인코더(BERT, RoBERTa, DistilBERT, MentalBERT) 아키텍처 벤치마킹
- 3개 플랫폼에서 수집된 19,800개 게시물/댓글 데이터셋에 일관된 전처리 파이프라인 적용
- (1) 단일 분할 baseline 평가 및 (2) 통계적 검정(효과 크기, 다중 비교 보정)을 포함한 5-seed 반복 실행 평가 프로토콜 수행
- 플랫폼 간 교차 도메인 전이 테스트 수행
- 학습 시간, 추론 대기 시간, 데이터 처리량 측정

**주요 결과**:
- MentalBERT가 가장 높은 분류 성능(F1 = 0.918, AUC = 0.962)을 달성하여 우울증 텍스트 분류에 탁월한 효과를 보임
- 플랫폼 간 교차 도메인 전이 시 CNN/LSTM 등 이전 아키텍처에 비해 트랜스포머 기반 모델이 더 견고함을 보였으나, 여전히 플랫폼 변화로 인한 일관된 성능 저하가 관찰됨
- 실무 모델 도입(모니터링 파이프라인, 선별 대시보드 등)에 유용한 예측 지표와 함께 계산 효율성 벤치마크 데이터를 제공


## 초록 (원문)

Depression-related language on social media provides measurable signals for population-level mental-health research, yet model selection remains sensitive to evaluation protocol, domain shift, class imbalance, and computational constraints. This study benchmarks CNN, LSTM, and transformer encoders (BERT, RoBERTa, DistilBERT, and MentalBERT) for binary depression-indicative versus control classification on a unified corpus of 19,800 English posts/comments aggregated from three platforms (Reddit, Twitter, and Facebook) under a consistent preprocessing pipeline. We report two complementary evaluation protocols: (1) a fixed-split single-run baseline for a comparable snapshot, and (2) a five-seed repeated-run protocol with statistical testing (effect sizes and multiple-comparison correction) to quantify variability and reduce sensitivity to initialization effects. Under repeated-run reporting, MentalBERT achieves the best overall performance (F1 = 0.918 ± 0.005; AUC = 0.962 ± 0.002), while CNN/LSTM baselines show lower robustness under cross-platform transfer. Cross-domain experiments reveal a consistent performance drop relative to in-domain evaluation, confirming non-trivial platform shift and motivating robustness-aware reporting for deployment-oriented settings. In addition to predictive metrics, we report training time, inference latency, and derived throughput to support practical model selection for use cases such as moderation pipelines and screening/triage dashboards.

## 키워드

Initialization, Robustness (evolution), Preprocessor, Encoder, Artificial neural network, Inference, Feature selection, Binary classification

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

