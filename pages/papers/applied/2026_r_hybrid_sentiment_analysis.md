---
title: "Hybrid sentiment analysis on Twitter data using VADER and RoBERTa models"
authors: ['Adithi H R', 'Impana D', 'Nisarga R', 'Nishigandha S Kaniyar', 'R Nithin']
year: 2026
venue: "E3S Web of Conferences"
tags: ['Sentiment Analysis and Opinion Mining', 'Text and Document Classification Technologies', 'Spam and Phishing Detection']
source: raw/applied/applied_2026_Hybrid_sentiment_analysis_202669203008.md
---

# Hybrid sentiment analysis on Twitter data using VADER and RoBERTa models
**제목(한글)**: VADER 및 RoBERTa 모델을 이용한 트위터 데이터 하이브리드 감성 분석

**저자**: Adithi H R; Impana D; Nisarga R; Nishigandha S Kaniyar; R Nithin
**출처**: E3S Web of Conferences, Vol.692, pp.03008-03008
**발행일**: 2026-01-01
**DOI**: https://doi.org/10.1051/e3sconf/202669203008

## 한국어 요약

**연구질문**: 트위터 데이터의 정형화되지 않은 언어적 특성을 해소하고 분석 성능과 연산 속도의 트레이드오프를 맞추기 위해, 사전식 기반 모델(VADER)과 트랜스포머 모델(RoBERTa)을 융합하는 방안은 어떠한가?

**방법론**:
- VADER의 규칙 기반 분석 속도와 RoBERTa의 문맥 파악 정확도를 결합한 하이브리드 감성 분류 프레임워크 제안
- Flask 프레임워크 및 MySQL 데이터베이스를 연동하여 로그인, 필터링 및 시각화 대시보드가 구비된 대규모 텍스트 분석 플랫폼 구현
- 총 160만 건의 트위터 데이터셋을 기반으로 GPU 병렬 배치 처리 최적화 및 감성 성능 통계 검정 수행

**주요 결과**:
- 하이브리드 접근법이 감성 정확도 89.1%를 달성하여 단독 사전 기반 기법 대비 통계적으로 유의미한 성능 향상($p < 0.001$)을 기록
- 브랜드 평판 조사, 정치 여론 분석 및 대규모 소셜 미디어 분석 등 대용량 상용 감성 분석 실무 환경에 적합한 대안임을 확인


## 초록 (원문)

Twitter and other social media platforms generate large volumes of user-generated text that reflect public opinion in real time. However, sentiment analysis of Twitter data remains challenging due to informal language, abbreviations, contextual dependencies, and the frequent presence of implicit sentiment. Lexicon-based approaches such as VADER provide computational efficiency but often fail to capture contextual meaning, while transformer-based models such as RoBERTa achieve higher accuracy at the cost of increased computational requirements. This paper presents a hybrid sentiment analysis framework that integrates VADER and RoBERTa to balance accuracy and efficiency. The proposed system is implemented as a Flask-based web application with MySQL database support, enabling user authentication, keyword-based tweet filtering, and result visualization. GPU acceleration and batch processing techniques are employed to optimize performance. Experimental evaluation conducted on a dataset of 1.6 million tweets demonstrates that the hybrid approach achieves an accuracy of 89.1%, outperforming standalone lexicon-based methods. Statistical analysis confirms that the observed improvements are significant (p &lt; 0.001). The results indicate that the proposed framework is suitable for large-scale sentiment analysis applications, including brand monitoring, political opinion analysis, and market trend assessment.

## 키워드

Sentiment analysis, Social media, Public opinion, Web application, Topic model, Computational Science and Engineering

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

