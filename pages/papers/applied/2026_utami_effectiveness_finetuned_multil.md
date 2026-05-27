---
title: "Effectiveness Fine-Tuned Multilingual BERT Model for Sentiments Classification Toward Bali’s Cultural Attractions"
authors: ['Nengah Widya Utami', 'Amna Saad', 'Made Adi Paramartha Putra', 'I Gede Juliana Eka Putra']
year: 2026
venue: "International Journal of Advances in Data and Information Systems"
tags: ['Sentiment Analysis and Opinion Mining', 'Digital Marketing and Social Media', 'Diverse Aspects of Tourism Research']
source: raw/applied/applied_2026_Effectiveness_FineTuned_M_ijadis_v7i1_1483.md
---

# Effectiveness Fine-Tuned Multilingual BERT Model for Sentiments Classification Toward Bali’s Cultural Attractions
**제목(한글)**: 발리의 문화 관광지에 대한 감성 분류를 위한 미세 조정된 다국어 BERT 모델의 유효성

**저자**: Nengah Widya Utami; Amna Saad; Made Adi Paramartha Putra; I Gede Juliana Eka Putra
**출처**: International Journal of Advances in Data and Information Systems, Vol.7, pp.217-229
**발행일**: 2026-03-30
**DOI**: https://doi.org/10.59395/ijadis.v7i1.1483

## 한국어 요약

**연구질문**: 다국적 방문객들이 구글 지도나 트립어드바이저에 남긴 다국어 후기 텍스트로부터, 발리 문화 관광 상품 평가를 고정밀도로 자동 분류해내기 위해 mBERT 모델을 어떻게 최적화할 수 있는가?

**방법론**:
- Google Maps 및 TripAdvisor에서 수집된 7,878건의 다국어 관광 후기 데이터 활용
- 다국어 mBERT 모델을 도메인 특화 데이터로 파인튜닝 학습
- XLM-Roberta, Distil-mBERT 및 전통 머신러닝(SVM, 로지스틱 회귀 등) 분류 모델들과 정확도 및 AUC 비교 평가

**주요 결과**:
- 파인튜닝된 mBERT가 단독 기준 모델(85.45%)을 크게 상회하는 92.13%의 분류 정확도와 AUC 0.909를 달성하여 우수한 분석 신뢰성을 획득
- 관광객들은 케착 댄스 등 문화 정통성에는 열광하나, 매표 대기나 좌석 배치 등 운영상 한계에 불만이 많음을 추출하여 서비스 질 개선 데이터를 마련함


## 초록 (원문)

This study examines the performance of a fine-tuned Multilingual BERT (mBERT) model for sentiment analysis of tourist reviews on Balinese cultural attractions. A multilingual dataset comprising 7,878 user-generated reviews from Google Maps and TripAdvisor was utilized to capture diverse linguistic expressions and visitor perspectives. The research methodology includes: (1) problem formulation and literature review; (2) dataset collection, preprocessing, and tokenization; (3) model training using mBERT as the baseline; (4) fine-tuning for domain adaptation; and (5) comparative evaluation with other Transformer models (XLM-Roberta and Distil-mBERT) and classical algorithms including Logistic Regression, Support Vector Machine, and Naïve Bayes. The results demonstrate a substantial improvement after fine-tuning. The baseline mBERT achieved 85.45% accuracy, while the fine-tuned model reached 92.13% accuracy with an AUC of 0.909, confirming the effectiveness of domain-specific adaptation. Although XLM-Roberta obtained slightly higher performance (93.15% accuracy, AUC 0.946), the fine-tuned mBERT showed stable and competitive results, making it the primary model of this study. Comparisons with classical methods further indicate that Transformer-based approaches provide more balanced and reliable sentiment classification. Sentiment distribution analysis reveals that tourist perceptions are predominantly positive, particularly regarding cultural authenticity and the quality of performances such as the Kecak and Fire Dance. Negative sentiments mainly relate to operational aspects, including crowd management, seating arrangements, and ticketing processes. Overall, this study provides empirical evidence that fine-tuned mBERT can effectively support data-driven evaluation of tourist experiences and deliver actionable insights for improving service quality and sustainability of Bali’s cultural tourism

## 키워드

Visitor pattern, Tourism, Support vector machine, Service quality, Baseline (sea), Perception, Empirical research, Quality (philosophy)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

