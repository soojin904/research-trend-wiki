---
title: "Emoj-Based Sentiment Analysis System"
authors: []
year: 2026
venue: "International Research Journal of Modernization in Engineering Technology and Science"
tags: ['Sentiment Analysis and Opinion Mining', 'Emotion and Mood Recognition', 'Mental Health via Writing']
source: raw/applied/applied_2026_EmojBased_Sentiment_Analy_irjmets98695.md
---

# Emoj-Based Sentiment Analysis System
**제목(한글)**: 이모지 기반 감성 분석 시스템

**저자**: 
**출처**: International Research Journal of Modernization in Engineering Technology and Science, Vol.None
**발행일**: 2026-05-24
**DOI**: https://doi.org/10.56726/irjmets98695

## 한국어 요약

**연구질문**: 텍스트 어구와 이모지가 혼용된 소셜 미디어 및 상품 후기 데이터에서, 이모지가 전달하는 고밀도 정서 정보를 활용하여 감성 분류 정확도를 극대화할 수 있는가?

**방법론**:
- Flask 기반의 백엔드와 SQLAlchemy 데이터베이스(PostgreSQL/MySQL 호환)를 갖춘 웹 애플리케이션 구축
- 사전 기반 VADER, 극성 분석 TextBlob 및 이모지 전용 감성 어휘집(Emoji Sentiment Lexicon)을 통합하는 하이브리드 감성 점수화 알고리즘 설계
- 이모지 밀도(Density)에 따라 이모지 기여 가중치를 최대 40%까지 동적으로 조절하는 하이브리드 가중치 수식 모델링 수행

**주요 결과**:
- 단어에만 의존하는 종래의 감성 분석 분류기보다 이모지 가중 결합 모델의 감성 분류 정확도가 대폭 상승함을 검증
- 일반 사용자는 후기 감성을 등록 추적하고, 관리자는 대용량 CSV 감성을 벌크 분석할 수 있는 안정적인 이중 대시보드 플랫폼을 구현함


## 초록 (원문)

The Emoji-Based Sentiment Analysis System represents an innovative approach to understanding human emotions and sentiments expressed in digital communication by combining traditional natural language processing techniques with modern emoji interpretation.In today's digital age, emojis have become an integral part of online communication, serving as powerful emotional indicators that often convey sentiments more effectively than words alone.This project addresses the growing need for highly developing sentiment analysis tools that can accurately interpret the nuanced combination of textual content and emoji usage in product reviews and social media communications.The system employs a hybrid methodology that integrates VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis, TextBlob polarity detection, and a comprehensive emoji sentiment lexicon to provide accurate sentiment classification.The implementation utilizes Flask web framework for the backend, SQLAlchemy for database management with support for both PostgreSQL and MySQL databases, and incorporates user authentication with role-based access control distinguishing between regular users and administrators.The system features a dual-dashboard architecture where users can submit and track their product reviews while administrators can monitor platform-wide analytics, manage users, and perform bulk sentiment analysis through CSV dataset uploads.The hybrid sentiment scoring algorithm dynamically adjusts weights based on emoji density, assigning up to 40% weight to emoji sentiment when multiple emojis are present, while maintaining a 60-40 ratio between VADER and TextBlob for text analysis.

## 키워드

Emoji, Sentiment analysis, Lexicon, Social media, Product (mathematics), Web application, Word (group theory)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

