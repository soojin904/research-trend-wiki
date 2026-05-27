---
title: "Topic counts and quality in topic models for historic corpora"
authors: ['M. G. Hall', 'Marcel Mernitz', 'Alexander Rensch']
year: 2026
venue: "Open Research Online (The Open University)"
tags: ['Computational and Text Analysis Methods', 'Topic Modeling', 'Sentiment Analysis and Opinion Mining']
source: raw/applied/applied_2026_Topic_counts_and_quality__nodoi.md
---

# Topic counts and quality in topic models for historic corpora
**제목(한글)**: 역사 코퍼스를 위한 토픽 모델에서의 토픽 수와 품질

**저자**: M. G. Hall; Marcel Mernitz; Alexander Rensch
**출처**: Open Research Online (The Open University), Vol.None
**발행일**: 2026-04-01
**DOI**: 

## 한국어 요약

**연구질문**: 조악한 종이 문서의 디지털화로 오염이 많은 역사 문서 코퍼스에서 토픽 모델링을 수행할 때, 가장 중요한 파라미터인 토픽 개수(Topic counts) 설정이 생성 토픽의 역사학적 품질에 어떤 영향을 미치며, 최적 파라미터를 결정하는 체계적 방법론은 무엇인가?

**방법론**:
- 서로 다른 성격의 역사 문서 코퍼스 2개를 활용해 토픽 수 변경 모델 실험 진행
- 2가지 수동 전문가 평가 기법과 1가지 컴퓨터 자동 일관성 평가 지표를 결합
- 수동 평가 부하를 최소화하면서 토픽 품질을 객관적으로 보장하는 파라미터 선정 표준 프로세스 제언

**주요 결과**:
- 설정된 토픽 수에 따른 역사 정보 유실도 및 중복 왜곡률의 임계 구간을 도출하여, 리서치 객관성과 재현성을 담보하는 통일된 평가 가이드를 확립함


## 초록 (원문)

Topic modelling methods enable the identification of potential topics within a corpus of historical texts, in particular they enable the identification of latent topics that are not described just by a single word. Like so many computational methods for the automatic processing of historical text corpora, they come with a number of parameters with which the method can be tuned and adapted. Each change in the settings of any of these parameters will generate a new set of topics that will differ in larger or smaller ways and which may be qualitatively better or worse. One of the main parameters for tuning topic models is setting the number of topics to be generated. In this paper we present an analysis of the impact of the number of topics on the quality of topic models for two historical text corpora. Two manual evaluation approaches are combined with an automated evaluation metric and based on the results we propose a formalised process for choosing the final set of parameters for a topic model. The process ensures the quality of the final model, while minimising the amount of manual evaluation work. The more structured process also allows for better documentation of the choices and in that way enables better reproducibility of any research using topic models.

## 키워드

Topic model, Identification (biology), Process (computing), Set (abstract data type), Quality (philosophy), Metric (unit)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

