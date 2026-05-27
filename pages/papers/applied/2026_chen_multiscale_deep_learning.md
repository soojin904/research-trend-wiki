---
title: "A Multi-Scale Deep Learning Architecture for Psychological State Recognition and Early Risk Warning from Social Media Text"
authors: ['Yufei Chen', 'Kai Chen']
year: 2026
venue: "Tehnicki vjesnik - Technical Gazette"
tags: ['Mental Health via Writing', 'Sentiment Analysis and Opinion Mining', 'Mental Health Research Topics']
source: raw/applied/applied_2026_A_MultiScale_Deep_Learnin_tv_20251208003192.md
---

# A Multi-Scale Deep Learning Architecture for Psychological State Recognition and Early Risk Warning from Social Media Text
**제목(한글)**: 소셜 미디어 텍스트 기반의 심리 상태 인식 및 조기 위험 경보를 위한 다중 스케일 딥러닝 아키텍처

**저자**: Yufei Chen; Kai Chen
**출처**: Tehnicki vjesnik - Technical Gazette, Vol.33
**발행일**: 2026-05-01
**DOI**: https://doi.org/10.17559/tv-20251208003192

## 한국어 요약

**연구질문**: 소셜 미디어의 다양한 언어적 층위(문자 변이, 단어 의미론, 문장 구조 등)에 흩어진 미세한 신호를 종합하여 심리 상태를 정확히 인식하고 조기 경보를 제공할 수 있는 모델 아키텍처는 무엇인가?

**방법론**:
- 문자 레벨과 단어 레벨 표현을 통합하는 다중 스케일 딥러닝 아키텍처 제안
- 국소적 의미 추출을 위한 다중 스케일 합성곱(CNN) 모듈, 어텐션 기반 전역 의미 모델링, 교차 스케일 특징 융합 기법 적용
- 다중 클래스 정신건강 텍스트 데이터셋을 사용하여 기존 머신러닝, 일반 딥러닝 및 어텐션 기반 베이스라인 모델들과 성능 비교
- 모델 출력을 시계열 위험 신호로 변환하여 누적 및 가속화되는 심리적 위험 패턴 탐지 기능 검증

**주요 결과**:
- 제안된 다중 스케일 모델은 정확도, 정밀도, 재현율, F1-score 모든 지표에서 기존 베이스라인 모델들을 일관되게 상회함
- 텍스트에서 도출된 시간적 위험 분석을 통해 점진적으로 쌓이고 악화되는 위험 상태를 성공적으로 판별해냄으로써 예방적 시스템의 실용적 토대를 구축함


## 초록 (원문)

Social media has become an important channel for expressing emotional experiences and potential psychological distress, making automated psychological state recognition a key technical challenge for early risk warning systems. Psychological signals in text are distributed across multiple linguistic levels, ranging from character-level expressive variations to word-level semantics and sentence-level psychological structure, which limits the effectiveness of single-scale models. This paper proposes a multi-scale deep learning architecture for psychological state recognition from social media text. The approach integrates character-level and word-level representations, multi-scale convolutional modules for local semantic extraction, attention-based global semantic modeling, and cross-scale feature fusion. By jointly capturing fine-grained linguistic cues and global psychological context, the proposed model enhances the discriminative power of psychological representations. Experiments conducted on a multi-class mental health text dataset demonstrate that the proposed method consistently outperforms traditional machine learning models, conventional deep learning architectures, and attention-enhanced baselines in terms of accuracy, precision, recall, and F1-score. Furthermore, the model outputs are transformed into temporal risk signals, enabling the identification of weak, accumulating, and accelerating psychological risk patterns. The results indicate that multi-scale text modeling provides an effective technical solution for psychological state recognition and establishes a practical basis for the development of early psychological risk warning systems.

## 키워드

Discriminative model, Deep learning, Social media, Identification (biology), Key (lock), Semantics (computer science), Convolutional neural network, Feature (linguistics)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]
- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모

