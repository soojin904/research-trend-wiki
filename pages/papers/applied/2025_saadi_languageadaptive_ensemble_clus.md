---
title: "A Language-Adaptive Ensemble Clustering Framework for Emotion Detection in Multilingual Social Media Text"
authors: ['Wafa Saadi', 'Fatima Zohra Laallam', 'Messaoud Mezati']
year: 2025
venue: "ECTI Transactions on Computer and Information Technology (ECTI-CIT)"
tags: ['Sentiment Analysis and Opinion Mining', 'Mental Health via Writing', 'Emotion and Mood Recognition']
source: raw/applied/applied_2025_A_LanguageAdaptive_Ensemb_ecti_cit_2026201_263493.md
---

# A Language-Adaptive Ensemble Clustering Framework for Emotion Detection in Multilingual Social Media Text

**제목(한글)**: 다국어 소셜 미디어 텍스트의 감정 탐지를 위한 언어 적응형 앙상블 군집화 프레임워크

## 한국어 요약

**연구질문**: 레이블이 없는 다국어(영어·아랍어) 소셜 미디어 데이터에서 인간 개입 없이 감정(Emotion)을 자동으로 탐지하고 레이블링하려면 어떤 비지도 학습 방법이 효과적인가?

**방법론**:
- BERT 임베딩과 PCA 차원 축소(Dimensionality Reduction)를 결합한 의미 표현 생성
- K-Means, 응집적 군집화(Agglomerative Clustering), 가우시안 혼합 모델(Gaussian Mixture Models, GMM)을 통합한 앙상블 군집화 전략 적용
- 이모지 처리 전략 3가지를 전처리에 통합하여 다양한 의미 표현 확보
- 영어 트윗 10,017건 및 아랍어 트윗 4,134건으로 실험 검증

**주요 결과**:
- 영어 데이터에서 K-Means+응집적·K-Means+GMM 앙상블 구성으로 실루엣 점수(Silhouette Score) 0.808 달성
- 아랍어 데이터에서 각각 0.728, 0.718의 실루엣 점수 획득
- 이모지 의미 통합이 앙상블 군집화 성능을 향상시키고 문맥적 모호성 해소에 기여
- 저자원 언어(Low-resource Language)를 포함한 다국어 환경에서의 확장 가능한 감정 탐지 솔루션 제시

**저자**: Wafa Saadi; Fatima Zohra Laallam; Messaoud Mezati
**출처**: ECTI Transactions on Computer and Information Technology (ECTI-CIT), Vol.20, pp.26-39
**발행일**: 2025-12-27
**DOI**: https://doi.org/10.37936/ecti-cit.2026201.263493

## 초록 (원문)

Social media platforms generate vast streams of emotionally rich textual data, offering valuable opportunities for critical applications, including mental health assessment and the analysis of collective public sentiment. However, detecting emotions in noisy and multilingual content remains challenging, particularly for under-resourced varieties such as dialects. Moreover, supervised learning techniques strongly depend on the availability of manually annotated corpora, whose creation requires substantial human effort and domain expertise. In contrast, unsupervised methods, while avoiding the need for human intervention, often lack sufficient robustness when confronted with the variability and complexity of natural language across diverse linguistic and cultural contexts. We present an ensemble clustering framework that automatically generates emotion labels from Twitter data, without human intervention. Our approach incorporates three emoji-handling strategies in the preprocessing step, enabling diverse semantic representations of emojis. We applied the BERT embeddings combined with PCA for dimensionality reduction within the same experimental framework. An ensemble clustering strategy integrating K-Means, Agglomerative clustering, and Gaussian Mixture Models (GMM) is adopted using multiple ensemble configurations. Experimental evaluation conducted on 10017 English tweets and 4134 Arabic tweets demonstrates that the proposed method achieves a silhouette score of 0.808 on English data using K-Means with Agglomerative and K-Means with GMM ensemble configurations. For Arabic data, silhouette scores of 0.728 and 0.718 are obtained using English and Arabic keywords, respectively. Emoji semantic integration enhances ensemble clustering performance, suggesting its importance for contextual disambiguation. The proposed framework provides a scalable solution for emotion detection in low-resource languages, enabling language-aware applications in multilingual contexts, particularly within linguistically diverse and multilingual populations

## 키워드

Cluster analysis, Ensemble learning, Preprocessor, Social media, Silhouette, Mixture model, Dimensionality reduction, Topic model

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

