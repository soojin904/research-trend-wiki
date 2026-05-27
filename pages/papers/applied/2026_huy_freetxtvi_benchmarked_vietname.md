---
title: "FreeTxt-Vi: A Benchmarked Vietnamese-English Toolkit for Segmentation, Sentiment, and Summarisation"
authors: ['Hung Nguyen Huy', 'Mo El-Haj', 'Dawn Knight', 'Paul Rayson']
year: 2026
venue: "ArXiv.org"
tags: ['Sentiment Analysis and Opinion Mining', 'Computational and Text Analysis Methods', 'Topic Modeling']
source: raw/applied/applied_2026_FreeTxtVi_A_Benchmarked_V_nodoi.md
---

# FreeTxt-Vi: A Benchmarked Vietnamese-English Toolkit for Segmentation, Sentiment, and Summarisation
**제목(한글)**: FreeTxt-Vi: 분절, 감성 분석, 요약을 위한 벤치마킹된 베트남어-영어 툴킷

**저자**: Hung Nguyen Huy; Mo El-Haj; Dawn Knight; Paul Rayson
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-03-05
**DOI**: 

## 한국어 요약

**연구질문**: NLP에서 저대표(under-represented) 언어인 베트남어의 기술적 장벽을 낮추기 위해, 프로그래밍 전문 지식 없이도 베트남어-영어 이중 언어 텍스트 데이터를 구축·분석·해석할 수 있는 통합 웹 기반 툴킷은 어떻게 설계되고 평가되는가?

**방법론**:
- VnCoreNLP와 바이트 쌍 부호화(BPE) 분절 전략을 통합한 하이브리드 베트남어-영어 NLP 파이프라인 설계
- 미세조정된 TabularisAI 감성 분류기와 Qwen2.5 기반 추상적 요약 모델 탑재
- 분절, 감성 분석, 요약의 3단계 평가를 통해 성능 검증

**주요 결과**:
- FreeTxt-Vi는 베트남어와 영어 모두에서 널리 사용되는 기준 모델들과 동등하거나 우수한 성능을 달성함
- 멀티링구얼 텍스트 분석의 기술적 장벽을 낮추어 교육, 디지털 인문학, 사회과학 등 다양한 도메인에서 재현 가능한 연구와 베트남어 언어 자원 개발을 지원함

## 초록 (원문)

FreeTxt-Vi is a free and open source web based toolkit for creating and analysing bilingual Vietnamese English text collections. Positioned at the intersection of corpus linguistics and natural language processing NLP it enables users to build explore and interpret free text data without requiring programming expertise. The system combines corpus analysis features such as concordancing keyword analysis word relation exploration and interactive visualisation with transformer based NLP components for sentiment analysis and summarisation. A key contribution of this work is the design of a unified bilingual NLP pipeline that integrates a hybrid VnCoreNLP and Byte Pair Encoding BPE segmentation strategy a fine tuned TabularisAI sentiment classifier and a fine tuned Qwen2.5 model for abstractive summarisation. Unlike existing text analysis platforms FreeTxt Vi is evaluated as a set of language processing components. We conduct a three part evaluation covering segmentation sentiment analysis and summarisation and show that our approach achieves competitive or superior performance compared to widely used baselines in both Vietnamese and English. By reducing technical barriers to multilingual text analysis FreeTxt Vi supports reproducible research and promotes the development of language resources for Vietnamese a widely spoken but underrepresented language in NLP. The toolkit is applicable to domains including education digital humanities cultural heritage and the social sciences where qualitative text data are common but often difficult to process at scale.

## 키워드

Text segmentation, Pipeline (software), Vietnamese, Computational linguistics, Natural language, Transformer, Sentiment analysis, Text corpus

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

