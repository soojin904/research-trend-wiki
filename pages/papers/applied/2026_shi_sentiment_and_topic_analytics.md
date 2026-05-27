---
title: "Sentiment and Topic Analytics for Electric Vehicle User Reviews"
authors: ['Yingxuan Shi', 'Tao Yang', 'Ruixue Zhang']
year: 2026
venue: "Sustainability"
tags: ['Electric Vehicles and Infrastructure', 'Sentiment Analysis and Opinion Mining', 'Vehicle emissions and performance']
source: raw/applied/applied_2026_Sentiment_and_Topic_Analy_su18094484.md
---

# Sentiment and Topic Analytics for Electric Vehicle User Reviews
**제목(한글)**: 전기차 사용자 리뷰에 대한 감성 및 토픽 분석

**저자**: Yingxuan Shi; Tao Yang; Ruixue Zhang
**출처**: Sustainability, Vol.18, pp.4484-4484
**발행일**: 2026-05-02
**DOI**: https://doi.org/10.3390/su18094484

## 한국어 요약

**연구질문**: 중국 내 다수의 전기차 후기 텍스트 데이터로부터 사용자의 감성과 세부 주제를 정량 추출하기 위해, 문맥 파악 및 장기 의존성 분석을 융합한 딥러닝 모델의 성능과 시계열적 리스크 인자는 무엇인가?

**방법론**:
- 중국 Autohome, Yiche, 국가품질감독원 리뷰 데이터베이스 수집 및 전처리
- 사전학습 임베딩(BERT), 장기 메모리 모델(Bi-xLSTM) 및 어텐션 레이어를 결합한 BERT-Bi-xLSTM-Attention 모델 설계 및 학습
- '감성-토픽' 융합 프레임워크를 기반으로 긍정 5대 테마, 부정 4대 테마 추출 및 2021~2024년 트렌드 추적

**주요 결과**:
- 제안하는 융합 모델이 정확도 93.23% 및 F1 93.28%를 획득하여 전통 baseline 모델들 대비 분류 성능을 크게 경신
- 사용자들은 전반적으로 자율주행 및 주행감에 만족하나, 차량용 스마트 시스템의 하드웨어/소프트웨어 신뢰성 및 가동 결함에 대한 부정적인 추이가 매년 증가하고 있음을 규명함


## 초록 (원문)

With the advancement of the “dual carbon” goals, the electric vehicle market has experienced explosive growth, and user review mining has become key data support for industrial quality improvement and low-carbon transportation transition. Addressing the limitations of existing sentiment classification methods in long-distance feature capture, cross-sentence semantic association, and emotional feature focus, this study proposes a BERT-Bi-xLSTM-Attention fusion model: BERT pre-trained semantic representation extracts deep contextual information, Bi-xLSTM models long-range dependency relationships, and the Attention mechanism locates sentiment-critical markers. Based on multi-platform review data from Chinese Autohome, Yiche, and China Quality Inspection Network, experiments show that the model achieves Accuracy, Recall, Precision, and F1 values of 0.9323, 0.9326, 0.9321, and 0.9328, significantly outperforming baseline models. A “sentiment-topic” fusion analysis framework is constructed, identifying five positive themes and four negative themes, revealing the dual emotional characteristics of range, driving experience, and smart features. Temporal analysis finds that negative attention to intelligent system reliability has continued to rise from 2021 to 2024, becoming an emerging user pain point. Combined with the above findings, it is recommended that consumers comprehensively evaluate multi-attribute experiences when purchasing; manufacturers prioritize optimizing user-concerned attributes; and policymakers improve industrial standards and regulatory mechanisms. This promotes high-quality development of electric vehicles, contributes to the realization of carbon neutrality goals in the transportation sector, and facilitates sustainable transportation development.

## 키워드

Sentiment analysis, Quality (philosophy), Dependency (UML), Reliability (semiconductor), Baseline (sea), Electric vehicle, Key (lock), Big data

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

