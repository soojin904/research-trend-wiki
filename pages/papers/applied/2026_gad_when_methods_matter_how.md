---
title: "When methods matter: how implementation choices shape topic discovery in financial text"
authors: ['Mahmoud Gad', 'Gitae Park', 'Sam Rawsthorne', 'Steven Young']
year: 2026
venue: "Accounting and Business Research"
tags: ['Advanced Text Analysis Techniques', 'Sentiment Analysis and Opinion Mining', 'Computational and Text Analysis Methods']
source: raw/applied/applied_2026_When_methods_matter_how_i_00014788_2026_2625716.md
---

# When methods matter: how implementation choices shape topic discovery in financial text
**제목(한글)**: 방법론이 중요할 때: 구현 단계의 선택이 금융 텍스트 내 토픽 발굴을 결정하는 방식

**저자**: Mahmoud Gad; Gitae Park; Sam Rawsthorne; Steven Young
**출처**: Accounting and Business Research, Vol.None, pp.1-40
**발행일**: 2026-04-20
**DOI**: https://doi.org/10.1080/00014788.2026.2625716

## 한국어 요약

**연구질문**: 영국 FTSE350 지수 편입 기업들의 연례 보고서 내 리스크 공시 데이터에 LDA 토픽 모델링을 적용할 때, 전처리, 다중어 표현 및 레이블링 등의 구현 결정이 연구 도출 결과 및 해석 가능성에 어떤 영향을 주는가?

**방법론**:
- FTSE350 연례 보고서 코퍼스를 사용하여 전처리 결정, 다중어 표현(multiword expressions) 및 토픽 레이블링 전략이 해석도에 미치는 영향 분석
- 계층선형모델(HLM)을 통해 광범위한 토픽(27%)과 세부적 토픽(75%) 하에서의 기업 내 토픽 변이 수준을 검정
- 토픽 명명 작업에 GPT 모델을 활용하는 파이프라인과 BERT 등 임베딩 기반 최신 토픽 모델의 성능을 LDA와 비교

**주요 결과**:
- 연구자의 전처리 및 파라미터 선택에 따라 도출되는 토픽의 입도(granularity)와 개별 기업 특화 리스크의 묘사 비중이 심각하게 달라져, LDA의 무조건적 객관성 주장에 한계가 있음을 밝힘
- 임베딩 기반 토픽 모델이 일관성(coherence) 측면에서 우수하지만 이 역시 도메인 전문가의 정성적 조율과 결정이 필수적임을 입증함


## 초록 (원문)

This paper examines the application of LDA topic modelling to risk disclosures in FTSE350 firms’ annual reports. We show that LDA implementation choices significantly impact topic representations and subsequent inferences. Using a corpus of FTSE350 annual reports, we show that preprocessing decisions, multiword expressions and labelling strategies materially affect topic interpretability and granularity. Our analysis reveals that while risk reporting addresses key business risks at an aggregate level, the degree of firm-specific commentary is sensitive to topic granularity. Hierarchical linear modelling suggests that 27% of topic variation is within firms for broad topics, increasing to 75% for granular topics. We leverage GPT to enhance topic labelling, showcasing the potential of LLMs in financial text analysis. We also compare LDA to modern embedding-based topic models, finding that while they often generate more coherent topics, they introduce a new set of critical implementation choices and do not eliminate the need for researcher discretion. These findings challenge the claims of LDA objectivity and highlight the importance of domain expertise. We propose a practical checklist for LDA implementation in accounting and finance research emphasising transparency and robustness checks.

## 키워드

Key (lock), Topic model

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

