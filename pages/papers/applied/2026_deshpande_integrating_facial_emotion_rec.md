---
title: "Integrating Facial Emotion Recognition, Speech to Text Transcription, and Natural Language Processing for Customer Satisfaction Analysis from Video Reviews"
authors: ['Sudhindra B. Deshpande', 'Goh Kah Ong Michael', 'Uttam U. Deshpande', 'K. S. Mathad', 'N. V. Karekar', 'Kiran K. Tangod']
year: 2026
venue: "Engineering Technology & Applied Science Research"
tags: ['Emotion and Mood Recognition', 'Sentiment Analysis and Opinion Mining', 'Gaze Tracking and Assistive Technology']
source: raw/applied/applied_2026_Integrating_Facial_Emotio_etasr_15095.md
---

# Integrating Facial Emotion Recognition, Speech to Text Transcription, and Natural Language Processing for Customer Satisfaction Analysis from Video Reviews
**제목(한글)**: 비디오 리뷰 기반 고객 만족도 분석을 위한 얼굴 감정 인식, 음성 인식 텍스트 변환 및 자연어 처리의 통합

**저자**: Sudhindra B. Deshpande; Goh Kah Ong Michael; Uttam U. Deshpande; K. S. Mathad; N. V. Karekar; Kiran K. Tangod
**출처**: Engineering Technology & Applied Science Research, Vol.16, pp.34615-34622
**발행일**: 2026-04-04
**DOI**: https://doi.org/10.48084/etasr.15095

## 한국어 요약

**연구질문**: 텍스트 위주 분석의 한계를 극복하고 동영상 리뷰 속 고객의 다차원적 정서를 종합 평가하기 위해 시각, 오디오, 텍스트의 멀티모달 융합 AI 프레임워크가 단일 모달리티 대비 얼마나 우수한 성능을 발휘하는가?

**방법론**:
- 1,000건의 동영상 제품/서비스 리뷰 데이터셋 확보
- 프레임 단위 추출, 안면 인식 및 감정 분류(Visual), 음성 인식 기반 텍스트 변환(Speech-to-Text), 텍스트 감성 분석(NLP)을 수행한 뒤 후기 융합(Late Fusion) 기법으로 멀티모달 결합 파이프라인 개발
- 만족도 지표(Porosity, F1, Accuracy) 및 요인 속성별 감성 분석 실시

**주요 결과**:
- 단일 채널 모델(시각 62.3%, 오디오 59.5%, 텍스트 72.1% 정확도)과 비교하여 제안된 멀티모달 융합 모델은 79.9% 정확도와 최고 수준의 AUC(0.86)를 보이며 성능이 획기적으로 개선됨
- 제품 만족도 속성 분석 결과 카메라 성능(+0.16)이 가장 높게 평가된 반면 앱 동작 오류(-0.33)와 배송 불만족(-0.09)이 해결 과제로 도출되었고, 시간에 따른 만족도 모니터링이 가능함을 입증함


## 초록 (원문)

Customer satisfaction is a decisive factor in the success of products and services provided, yet conventional text-based reviews often fail to capture the full spectrum of user emotions needed to assess satisfaction. On the other hand, video product or service reviews offer a more informative medium for evaluating customer satisfaction. To leverage this, the present study proposes a multimodal machine learning framework for video-based customer feedback analysis, integrating facial emotion recognition, speech-to-text transcription, and Natural Language Processing (NLP). A dataset of 1,000 video reviews was processed through a multistage pipeline that involved frame extraction, face detection, emotion classification, audio transcription, sentiment analysis, and late fusion of modalities. Experimental results highlight the limitations of unimodal models: visual-only sentiment prediction achieved 62.3% accuracy (precision = 0.61, recall = 0.63, F1-score = 0.62, Area Under Curve (AUC) = 0.65), while audio-only sentiment prediction reached 59.5% accuracy (precision = 0.58, recall = 0.59, F1-score = 0.59, AUC = 0.61). The text-based model provided a stronger baseline at 72.1% accuracy (precision = 0.70, recall = 0.72, F1-score = 0.71, AUC = 0.75). In contrast, the multimodal fusion framework substantially outperformed unimodal approaches, achieving 79.9% accuracy, precision = 0.80, recall = 0.81, F1-score = 0.80, and the highest AUC of 0.86. Additionally, aspect-level analysis revealed that camera quality (+0.16) was the most positively perceived feature, while app performance (-0.33) and delivery (-0.09) emerged as primary concerns. Temporal analysis showed satisfaction scores fluctuating between 52.1 and 63.4 (0-100 scale) over 20 weeks, underscoring the value of continuous monitoring. These findings demonstrate that multimodal video feedback analysis yields more comprehensive, reliable, and fair performance than single-channel methods.

## 키워드

Recall, Leverage (statistics), Sentiment analysis, Facial expression, Customer satisfaction, Disgust, Precision and recall, Baseline (sea)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

