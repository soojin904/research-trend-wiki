---
title: "Approaches to Analysing Historical Newspapers Using LLMs"
authors: ['Filip Dobranić', 'Tina Munda', 'Oliver Pejić', 'Vojko Gorjanc', 'Uroš Šmajdek', 'David Bordon', 'Jakob Lenardič', 'Tjaša Konovšek', 'Kristina Pahor de Maiti Tekavčič', 'Ciril Bohak', 'Darja Fišer']
year: 2026
venue: "ArXiv.org"
tags: ['Computational and Text Analysis Methods', 'Digital Humanities and Scholarship', 'Sentiment Analysis and Opinion Mining']
source: raw/applied/applied_2026_Approaches_to_Analysing_H_nodoi.md
---

# Approaches to Analysing Historical Newspapers Using LLMs
**제목(한글)**: LLM을 활용한 역사 신문 분석 방법론

## 한국어 요약

**연구질문**: 20세기 전환기 슬로베니아 역사 신문에 나타난 집단 정체성, 정치적 지향, 국가 귀속감이 공론장에서 어떻게 표상되었으며, LLM 기반 계산적 방법론으로 이를 어떻게 분석할 수 있는가?

**방법론**:
- BERTopic을 활용한 토픽 모델링으로 주요 주제 패턴 식별
- OCR 손상 역사 슬로베니아어 텍스트에 대한 네 가지 명령어 실행형(Instruction-Following) LLM의 측면 수준 감성 분석(Aspect-Level Sentiment Analysis) 평가
- 개체명 인식(NER) 그래프를 통한 집단 정체성과 장소 간 관계 네트워크 시각화
- 정량적 네트워크 분석과 비판적 담론 분석을 결합한 혼합 방법론 적용

**주요 결과**:
- 슬로베니아어에 특화된 GaMS3-12B-Instruct 모델이 역사 신문 감성 분류에 가장 적합하나, 중립 감성에서 양성·부정 감성보다 성능이 우수함을 확인
- 두 신문의 보수-가톨릭 대 자유-진보 이념 차이가 집단 정체성 표상 방식의 차이로 정량적으로 드러남

**저자**: Filip Dobranić; Tina Munda; Oliver Pejić; Vojko Gorjanc; Uroš Šmajdek; David Bordon; Jakob Lenardič; Tjaša Konovšek; Kristina Pahor de Maiti Tekavčič; Ciril Bohak; Darja Fišer
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-03-26
**DOI**: 

## 초록 (원문)

This study presents a computational analysis of the Slovene historical newspapers \textit{Slovenec} and \textit{Slovenski narod} from the sPeriodika corpus, combining topic modelling, large language model (LLM)-based aspect-level sentiment analysis, entity-graph visualisation, and qualitative discourse analysis to examine how collective identities, political orientations, and national belonging were represented in public discourse at the turn of the twentieth century. Using BERTopic, we identify major thematic patterns and show both shared concerns and clear ideological differences between the two newspapers, reflecting their conservative-Catholic and liberal-progressive orientations. We further evaluate four instruction-following LLMs for targeted sentiment classification in OCR-degraded historical Slovene and select the Slovene-adapted GaMS3-12B-Instruct model as the most suitable for large-scale application, while also documenting important limitations, particularly its stronger performance on neutral sentiment than on positive or negative sentiment. Applied at dataset scale, the model reveals meaningful variation in the portrayal of collective identities, with some groups appearing predominantly in neutral descriptive contexts and others more often in evaluative or conflict-related discourse. We then create NER graphs to explore the relationships between collective identities and places. We apply a mixed methods approach to analyse the named entity graphs, combining quantitative network analysis with critical discourse analysis. The investigation focuses on the emergence and development of intertwined historical political and socionomic identities. Overall, the study demonstrates the value of combining scalable computational methods with critical interpretation to support digital humanities research on noisy historical newspaper data.

## 키워드

Newspaper, Ideology, Interpretation (philosophy), Politics, Topic model, Discourse analysis, Thematic structure, Sentiment analysis

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

