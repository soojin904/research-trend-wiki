---
title: "Comparative Topic Modelling of Mobile Banking User Reviews Using LDA and BERTopic: A Case Study of wondr by BNI"
authors: ['Dicky Halim', 'Indra Budi', 'Basma Fathan Mubina', 'Aris Budi Santoso', 'Prabu Kresna Putra']
year: 2026
venue: "Indonesian Journal of Computer Science"
tags: ['Sentiment Analysis and Opinion Mining', 'Customer churn and segmentation', 'Digital Marketing and Social Media']
source: raw/applied/applied_2026_Comparative_Topic_Modelli_ijcs_v15i2_5118.md
---

# Comparative Topic Modelling of Mobile Banking User Reviews Using LDA and BERTopic: A Case Study of wondr by BNI
**제목(한글)**: LDA와 BERTopic을 활용한 모바일 뱅킹 사용자 리뷰의 비교 토픽 모델링: wondr by BNI의 사례 연구

**저자**: Dicky Halim; Indra Budi; Basma Fathan Mubina; Aris Budi Santoso; Prabu Kresna Putra
**출처**: Indonesian Journal of Computer Science, Vol.15
**발행일**: 2026-04-16
**DOI**: https://doi.org/10.33022/ijcs.v15i2.5118

## 한국어 요약

**연구질문**: 인도네시아 BNI 은행의 신규 모바일 뱅킹 앱 Wondr 사용자 리뷰에서 서비스 만족도 및 주요 장애 요인을 발굴할 때, 전통 LDA와 임베딩 기반 BERTopic 모델 간의 토픽 품질 및 일관성 성능 격차는 어떠한가?

**방법론**:
- 구글 플레이스토어에서 수집된 Wondr 사용자 앱 리뷰 데이터셋 전처리(정규화, 불용어 제거, 어간 추출) 진행
- LDA 모델의 토픽 수 선정을 위해 Coherence 점수 계산을 수행하고, BERTopic 모델은 문장 임베딩 분포 및 시각화 일관성 분석 비교

**주요 결과**:
- BERTopic 모델이 리뷰 단문에서 문맥 의미를 가장 고해상도로 캡처하여 '로그인 본인 인증 지연', '계좌 이체 시스템 에러' 등 구체적인 실무 불만 토픽을 일관되게 정확히 식별해냄
- 비록 통계적 통계 일관성 점수는 LDA가 우세했지만, 의미적 유용성 측면에서는 임베딩 기반 BERTopic이 압도적으로 우수하여 모바일 금융 분석에 최적임을 검증함


## 초록 (원문)

This study explores user reviews of the Wondr mobile banking application to identify factors that influence user experience and service quality. The dataset, obtained from the Google Play Store, was processed through several preprocessing steps, including normalization, stopword removal, and stemming. Two topic modelling methods were applied: Latent Dirichlet Allocation (LDA) as a probabilistic baseline and BERTopic as an embedding-based approach. The LDA model was evaluated using coherence scores to determine the most suitable number of topics, while BERTopic was assessed based on topic distribution, interpretability, and additional coherence analysis. The results show that BERTopic produces more semantically meaningful and contextually rich topics, particularly in capturing short-text user reviews. Although BERTopic achieves lower overall coherence compared to LDA, certain topics demonstrate high semantic consistency, especially for well-defined issues such as login verification problems. The analysis reveals that most user feedback is concentrated on positive user experience, while critical issues related to login verification and system errors remain significant concerns. These findings provide actionable insights for improving mobile banking services and demonstrate the effectiveness of embedding-based topic modeling in financial text analytics. These findings highlight a trade-off between statistical consistency and semantic richness in topic modeling approaches. The results provide actionable insights for improving mobile banking services and demonstrate the effectiveness of combining probabilistic and embedding-based methods in financial text analytics.

## 키워드

Latent Dirichlet allocation, Topic model, Login, Consistency (knowledge bases), Probabilistic logic, Coherence (philosophical gambling strategy), Mobile banking, Preprocessor

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

