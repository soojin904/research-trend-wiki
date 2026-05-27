---
title: "Evaluation of a Company’s Media Reputation Based on the Articles Published on News Portals"
authors: ['Algimantas Venčkauskas', 'Vacius Jusas', 'Dominykas Barisas']
year: 2026
venue: "Applied Sciences"
tags: ['Corporate Identity and Reputation', 'Sentiment Analysis and Opinion Mining', 'Digital Marketing and Social Media']
source: raw/applied/applied_2026_Evaluation_of_a_Companys__app16041987.md
---

# Evaluation of a Company’s Media Reputation Based on the Articles Published on News Portals
**제목(한글)**: 뉴스 포털 발행 기사에 기반한 기업 미디어 평판 평가

**저자**: Algimantas Venčkauskas; Vacius Jusas; Dominykas Barisas
**출처**: Applied Sciences, Vol.16, pp.1987-1987
**발행일**: 2026-02-17
**DOI**: https://doi.org/10.3390/app16041987

## 한국어 요약

**연구질문**: 뉴스 기사 텍스트의 감성 극성 분류를 결합하여, 기업의 미디어적 평판(Media Reputation)을 단순 긍부정 비율을 넘어 통계적 오차 범위와 마진이 포함된 신뢰도 수치로 어떻게 계량 평가할 수 있는가?

**방법론**:
- 리투아니아 주요 뉴스 포털 기사를 대상으로 수집 수행
- 기사 내 개별 문장 감성을 positive, negative, neutral 3개 극성으로 판별
- 감성 극성들과 총 기사 발행량을 합성하여 0~100 스케일의 평판 점수 및 오차 마진(Margin of error)을 산출하는 하이브리드 수식 모델링 수행
- Stanford CoreNLP(Google 번역 연동) 모델과 다국어 XLM-RoBERTa 모델의 감성 분류 정밀도 비교 검증

**주요 결과**:
- 제안하는 기법이 기존의 미디어 지지율 지수(Media Endorsement)의 극단성과 미디어 호감도 지수(Favorableness)의 과도한 중립 편향을 모두 보정하여 객관적인 기업 평판 포트폴리오를 제공함을 통계적으로 증명


## 초록 (원문)

A company’s reputation is an important, intangible asset, which is heavily influenced by media reputation. We developed a method to measure a company’s reputation based on sentiments detected in online articles. The sentiment of each sentence was evaluated and categorized into one of three polarities: positive, negative, or neutral. Then, we developed another method to assess a company’s media reputation using all available online articles about the company. The company’s media reputation is presented as a tuple consisting of their media reputation on a scale from 0 to 100, the number of articles related to the company, and the margin of error. Experiments were conducted using articles written in Lithuanian published on major news portals. We used two different tools to assess the sentiments of the articles: Stanford CoreNLP v.4.5.10, combined with Google API, and the pre-trained transformer model XLM-RoBERTa. Google API was used for translation into English, as Stanford CoreNLP does not support the Lithuanian language. The results obtained were compared with those of existing methods, based on the coefficients of media endorsement and media favorableness, showing that the results of the proposed method are less moderate than the coefficient of media favorableness and less extreme than the coefficient of media endorsement.

## 키워드

Reputation, Lithuanian, Sentiment analysis, Social media, Sentence, News media

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

