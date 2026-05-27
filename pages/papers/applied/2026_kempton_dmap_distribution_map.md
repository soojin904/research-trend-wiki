---
title: "DMAP: A Distribution Map for Text"
authors: ['Tom Kempton', 'Julia Rozanova', 'Parameswaran Kamalaruban', 'Maeve Madigan', 'Karolina Wresilo', 'Yoann L. Launay', 'David Sutton', 'Stuart Burrell']
year: 2026
venue: "ArXiv.org"
tags: ['Authorship Attribution and Profiling', 'Handwritten Text Recognition Techniques', 'Topic Modeling']
source: raw/applied/applied_2026_DMAP_A_Distribution_Map_f_nodoi.md
---

# DMAP: A Distribution Map for Text
**제목(한글)**: DMAP: 텍스트를 위한 분포 지도

**저자**: Tom Kempton; Julia Rozanova; Parameswaran Kamalaruban; Maeve Madigan; Karolina Wresilo; Yoann L. Launay; David Sutton; Stuart Burrell
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-02-12
**DOI**: 

## 한국어 요약

**연구질문**: 다음 토큰 예측 확률 분포가 지닌 풍부한 정보를 어떻게 효율적이고 모델 독립적인 방식으로 텍스트 분석에 활용할 수 있는가?

**방법론**:
- 언어 모델을 통해 텍스트를 단위 구간(unit interval) 내 샘플 집합으로 매핑하는 DMAP 방법론 제안
- 생성 매개변수 검증, 기계 생성 텍스트 탐지, 합성 데이터 후처리 흔적 분석 등 세 가지 사례 연구 수행

**주요 결과**:
- DMAP가 순위(rank)와 확률 정보를 동시에 인코딩하여 통합적인 통계적 텍스트 뷰를 제공함
- 소비자용 하드웨어에서 간단하게 계산 가능하며, 합성 데이터로 훈련된 다운스트림 모델에서 통계적 핑거프린트를 탐지할 수 있음

## 초록 (원문)

Large Language Models (LLMs) are a powerful tool for statistical text analysis, with derived sequences of next-token probability distributions offering a wealth of information. Extracting this signal typically relies on metrics such as perplexity, which do not adequately account for context; how one should interpret a given next-token probability is dependent on the number of reasonable choices encoded by the shape of the conditional distribution. In this work, we present DMAP, a mathematically grounded method that maps a text, via a language model, to a set of samples in the unit interval that jointly encode rank and probability information. This representation enables efficient, model-agnostic analysis and supports a range of applications. We illustrate its utility through three case studies: (i) validation of generation parameters to ensure data integrity, (ii) examining the role of probability curvature in machine-generated text detection, and (iii) a forensic analysis revealing statistical fingerprints left in downstream models that have been subject to post-training on synthetic data. Our results demonstrate that DMAP offers a unified statistical view of text that is simple to compute on consumer hardware, widely applicable, and provides a foundation for further research into text analysis with LLMs.

## 키워드

Probability distribution, Representation (politics), Conditional probability, Set (abstract data type), Statistical model, Range (aeronautics), Rank (graph theory), Interval (graph theory)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

