---
title: "Language Anxiety Identification in Social Media Using BERT"
authors: ['Raisa Aliya Zahra', 'Kemas Muslim Lhaksmana']
year: 2025
venue: ""
tags: ['Mental Health via Writing', 'Sentiment Analysis and Opinion Mining', 'Hate Speech and Cyberbullying Detection']
source: raw/applied/applied_2025_Language_Anxiety_Identifi_icicyta68677_2025_1136253.md
---

# Language Anxiety Identification in Social Media Using BERT

**제목(한글)**: BERT를 사용한 소셜 미디어에서의 언어 불안 식별

## 한국어 요약

**연구질문**: 인도네시아어 소셜 미디어(X 플랫폼) 게시물에서 자연어 처리 접근법으로 외국어 학습 상황에서의 언어 불안(language anxiety)을 효과적으로 식별하고 설명 가능성을 어떻게 확보할 수 있는가?

**방법론**:
- X 플랫폼 크롤링으로 수집한 3,000개 트윗을 불안(1)/비불안(0) 이진 분류로 수작업 주석 처리
- 인도네시아어 트위터 데이터로 사전학습된 트랜스포머 기반 모델인 IndoBERTweet 미세조정
- LIME(Local Interpretable Model-Agnostic Explanations)으로 모델 해석 가능성 향상

**주요 결과**:
- 제안 모델이 정확도 0.885, 매크로 F1-스코어 0.880으로 균형 잡힌 높은 성능을 달성
- LIME 설명 분석에서 두려움, 당혹감, 자기 평가 등 언어 불안의 핵심 언어·감정 지표를 성공적으로 포착함을 확인

**저자**: Raisa Aliya Zahra; Kemas Muslim Lhaksmana
**출처**: , Vol.None, pp.726-731
**발행일**: 2025-12-17
**DOI**: https://doi.org/10.1109/icicyta68677.2025.11362538

## 초록 (원문)

Language anxiety is a psychological factor that can negatively affect communication ability, confidence, and academic performance in foreign language learning. While previous studies have primarily examined language anxiety in classroom settings using questionnaires, this form of anxiety also appears in social media interactions, where users freely express their emotions and personal experiences. This study proposes a Natural Language Processing (NLP) approach with explainable AI to identify language anxiety in Indonesian social media posts using IndoBERTweet, a transformer-based model pretrained on Indonesian Twitter data, combined with Local Interpretable Model-Agnostic Explanations (LIME) to enhance interpretability. A manually annotated dataset consisting of 3,000 tweets was constructed through a data crawling process on the X platform and labeled as Anxious (1) or Non-Anxious (0). The dataset was used to fine-tune the IndoBERTweet model for binary classification. Experimental results show that the proposed model achieved an accuracy of 0.885 and a macro-F1 score of 0.880, indicating strong and balanced performance despite the relatively limited dataset size. Explainability analysis using LIME reveals that the model successfully captures key linguistic and emotional indicators of language anxiety, such as fear, embarrassment, and self-evaluation, while also recognizing positive expressions related to confidence and motivation. These findings demonstrate the effectiveness of domain-specific transformer models for analyzing psychological patterns in informal online communication. This study brings together language anxiety research and social media text analysis into a unified framework, and provides a foundation for future work involving larger datasets, multimodal signals, and cross-lingual anxiety detection.

## 키워드

Social media, Anxiety, Crawling, Identification (biology), Indonesian, Social anxiety, Affect (linguistics), Language model

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

