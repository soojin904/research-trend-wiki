---
title: "FINENZO: Financial Sentiment Based Analysis System"
authors: ['Prof. Yogita Chavan', 'Jeet Gor', 'Rahul Jalora', 'Omik Vichare']
year: 2026
venue: "Iconic Research and Engineering Journals"
tags: ['Stock Market Forecasting Methods', 'Financial Distress and Bankruptcy Prediction', 'Sentiment Analysis and Opinion Mining']
source: raw/applied/applied_2026_FINENZO_Financial_Sentime_irev9i10_1716388.md
---

# FINENZO: Financial Sentiment Based Analysis System
**제목(한글)**: FINENZO: 금융 감성 기반 분석 시스템

**저자**: Prof. Yogita Chavan; Jeet Gor; Rahul Jalora; Omik Vichare
**출처**: Iconic Research and Engineering Journals, Vol.9
**발행일**: 2026-04-14
**DOI**: https://doi.org/10.64388/irev9i10-1716388

## 한국어 요약

**연구질문**: 상장 기업들이 공시하는 복잡하고 방대한 10-K 연례 보고서에서 투자자들이 정보 왜곡 없이 신속하게 핵심 경영 상태를 정량화할 수 있는 자동화 시스템은 무엇인가?

**방법론**:
- SEC EDGAR 데이터베이스로부터 실시간 10-K 보고서를 수집하고 텍스트 전처리 및 TF-IDF 피처 추출 구현
- 금융 전용 감성 사전을 구축하여 경영진의 어조를 정량 감성 스코어로 환산하고 재무 지표와 결합

**주요 결과**:
- 비정형 텍스트 보고서를 실시간 정량 지수로 가공하는 확장성 높은 금융 전용 분석 시스템 'Finenzo' 구현 및 투자 의사결정 효율화 실증


## 초록 (원문)

Financial reports such as 10-K reports contain extensive information about a company’s financial performance, risks, and operations. However, these documents are often lengthy and complex, making manual analysis difficult and time-consuming for investors and analysts. Traditional methods struggle to efficiently extract meaningful insights from unstructured financial text, leading to challenges in effective decision-making. To address these limitations, Finenzo is proposed as a system that utilizes Natural Language Processing (NLP) techniques to analyze financial statements and extract useful insights. The system retrieves 10-K reports from the SEC EDGAR database, performs text preprocessing, and applies TF-IDF for feature extraction. A financial sentiment dictionary is used to identify sentiment patterns and generate quantitative scores from textual data. These insights are combined with financial indicators to support better evaluation of company performance and assist in data-driven decision-making. By converting unstructured financial data into structured information, the system improves analysis efficiency and provides a scalable approach for financial analysis.

## 키워드

Sentiment analysis, Financial analysis, Financial ratio, Scalability, Feature (linguistics), Financial market, Unstructured data

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

