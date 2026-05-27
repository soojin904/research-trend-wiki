---
title: "A Directed Graph Model and Experimental Framework for Design and Study of Time-Dependent Text Visualisation"
authors: ['Songhai Fan', 'Simon D. Angus', 'Tim Dwyer', 'Ying Yang', 'Sarah Goodwin', 'Helen Purchase']
year: 2026
venue: "ArXiv.org"
tags: ['Data Visualization and Analytics', 'Computational and Text Analysis Methods', 'Digital Humanities and Scholarship']
source: raw/applied/applied_2026_A_Directed_Graph_Model_an_nodoi.md
---

# A Directed Graph Model and Experimental Framework for Design and Study of Time-Dependent Text Visualisation
**제목(한글)**: 시간 의존적 텍스트 시각화 설계와 연구를 위한 방향 그래프 모델 및 실험 프레임워크

**저자**: Songhai Fan; Simon D. Angus; Tim Dwyer; Ying Yang; Sarah Goodwin; Helen Purchase
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-03-02
**DOI**: 

## 한국어 요약

**연구질문**: 뉴스 기사 및 소셜 미디어 등 시간에 따라 변화하는 대량의 텍스트 담론을 인간이 직관적으로 이해할 수 있도록 방향 그래프 구조로 시각화하는 모델을 정의하고, 실제 사용자가 이러한 시각화에서 텍스트 관계 패턴을 정확히 식별할 수 있는가?

**방법론**:
- 시간 의존적 텍스트 시각화를 위한 방향 그래프(Directed graph) 기반 추상 모델 정의 및 가능한 텍스트 연결 패턴 모티프(motifs) 도출
- LLM을 활용해 각 패턴에 해당하는 합성 시간 의존 기사 세트를 생성하고, 30명 참가자 대상 사용자 연구(n=30) 수행

**주요 결과**:
- 사용자들이 사전 정의된 텍스트 관계 패턴 모티프를 정확히 식별하는 것이 상당히 어려운 과제임을 확인함
- LLM을 활용한 합성 데이터셋 생성 과정에서 예상치 못한 복잡성이 발생하여 실험 통제에 일부 한계가 있었으며, 텍스트 담론 시각화에서 획일적 접근보다 사용자 맞춤형 방식이 필요함을 제시함

## 초록 (원문)

Exponential growth in the quantity of digital news, social media, and other textual sources makes it difficult for humans to keep up with rapidly evolving narratives about world events. Various visualisation techniques have been touted to help people to understand such discourse by exposing relationships between texts (such as news articles) as topics and themes evolve over time. Arguably, the understandability of such visualisations hinges on the assumption that people will be able to easily interpret the relationships in such visual network structures. To test this assumption, we begin by defining an abstract model of time-dependent text visualisation based on directed graph structures. From this model we distill motifs that capture the set of possible ways that texts can be linked across changes in time. We also develop a controlled synthetic text generation methodology that leverages the power of modern LLMs to create fictional, yet structured sets of time-dependent texts that fit each of our patterns. Therefore, we create a clean user study environment (n=30) for participants to identify patterns that best represent a given set of synthetic articles. We find that it is a challenging task for the user to identify and recover the predefined motif. We analyse qualitative data to map an unexpectedly rich variety of user rationales when divergences from expected interpretation occur. A deeper analysis also points to unexpected complexities inherent in the formation of synthetic datasets with LLMs that undermine the study control in some cases. Furthermore, analysis of individual decision-making in our study hints at a future where text discourse visualisation may need to dispense with a one-size-fits-all approach and, instead, should be more adaptable to the specific user who is exploring the visualisation in front of them.

## 키워드

Visualization, Set (abstract data type), Interpretation (philosophy), Narrative, Graph, Data visualization, Text generation, Variety (cybernetics)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

