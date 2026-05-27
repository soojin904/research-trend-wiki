---
title: "Beyond Single Topics: Quantifying Information Loss by Comparing GPT-Based Aspect Sentiment Analysis With LDA in Hospital Reviews (Preprint)"
authors: ['Jung-Tang Hsueh', 'Sheng-Hsun Hsu', 'Shwu-Fen Chiu']
year: 2026
venue: ""
tags: ['Patient Satisfaction in Healthcare', 'Sentiment Analysis and Opinion Mining', 'Social Media in Health Education']
source: raw/applied/applied_2026_Beyond_Single_Topics_Quan_preprints_92325.md
---

# Beyond Single Topics: Quantifying Information Loss by Comparing GPT-Based Aspect Sentiment Analysis With LDA in Hospital Reviews (Preprint)
**제목(한글)**: 단일 토픽을 넘어서: 병원 고객 리뷰에서 GPT 기반 양상 감성 분석과 LDA 비교를 통한 정보 손실 정량화

**저자**: Jung-Tang Hsueh; Sheng-Hsun Hsu; Shwu-Fen Chiu
**출처**: , Vol.None
**발행일**: 2026-03-08
**DOI**: https://doi.org/10.2196/preprints.92325

## 한국어 요약

**연구질문**: 병원 고객 만족도 리뷰 데이터 분석 시, 문서를 단일 지배 토픽으로 축약하는 고전 LDA 모델이 버리는 환자의 미세 만족도 정보 손실률은 얼마나 되며, 임상 치료(기술)와 행정 접수(기능) 간의 혼합 만족 양상은 어떻게 나타나는가?

**방법론**:
- 대만 내 24개 대형 상급 종합병원들의 Google Reviews 5,467건 수집
- 동일 데이터를 대상으로 LDA 모델링(K=7)과 사전 정의된 7대 의료 품질 영역에 대한 GPT 기반의 세부 양상 감성 분석(ABSA)을 동시에 수행해 정보 손실 계수 비교
- Jaccard 유사도를 기반으로 평점별 만족 요인의 공동 발생 네트워크 매핑 분석

**주요 결과**:
- 환자들은 한 리뷰당 평균 2.05개 이상의 상이한 서비스 품질을 동시에 언급하고 있어, LDA와 같은 단일 토픽 할당 시 무려 51.2%의 중대한 고객 의견 정보 손실이 강제 발생함을 입증함
- 의료진의 뛰어난 임상 기술은 극찬하면서도 불친절한 수납 절차를 비판하는 '기술-기능 인지 괴리(Technical–Functional Divergence)' 현상이 다중 감성 표출 리뷰의 49.9%를 차지함을 밝히며, 병원 대시보드 구축 시 임상 만족과 운영 만족을 필히 분리해 평가할 것을 제안함


## 초록 (원문)

<sec> <title>BACKGROUND</title> Healthcare service quality is inherently multidimensional, yet document-level text analysis methods such as Latent Dirichlet Allocation (LDA) force patient reviews into single dominant topics. This simplification may systematically discard evaluative information when patients discuss multiple service dimensions with varying sentiments within the same review. </sec> <sec> <title>OBJECTIVE</title> This study compared document-level topic modeling (LDA) with GPT-based aspect-level sentiment analysis (ABSA) to address three research questions: (1) How much information is lost when collapsing multi-aspect reviews to single topics? (2) How prevalent are mixed-sentiment reviews, and what quality tensions do they reveal—both cross-aspect trade-offs and within-aspect ambivalence? (3) Do positive and negative reviews exhibit different structural patterns in aspect co-occurrence? </sec> <sec> <title>METHODS</title> We analyzed 2024 Google Reviews from 24 medical centers in Taiwan. Both LDA (K=7 topics) and GPT-based ABSA were applied to the same 5,467 reviews, ensuring fair comparison on identical data. The ABSA design employed structured prompts to extract aspects from seven predefined quality dimensions. Quality validation achieved Cohen κ=.82 against human annotation. Mixed-sentiment reviews were identified as those containing both positive and negative aspect evaluations, and cross-polarity couplings were analyzed to identify recurring trade-off patterns. Rating-stratified network analysis compared aspect co-occurrence patterns between positive reviews and negative reviews using Jaccard similarity. </sec> <sec> <title>RESULTS</title> Reviews discussed an average of 2.05 distinct aspects (SD=0.97), producing 51.2% information loss under LDA's single-topic assignment. Among multi-aspect reviews, 11.0% exhibited cross-aspect mixed sentiment, with Technical–Functional Divergence—praising Professional Quality while criticizing functional dimensions—appearing in 49.9% of these mixed-sentiment cases. Network analysis revealed differential bundling: operational dimensions co-occurred more strongly in negative reviews, whereas clinical dimensions co-occurred more strongly in positive reviews. </sec> <sec> <title>CONCLUSIONS</title> Document-level topic modeling discards more than half of the evaluative information patients provide. Our findings reveal that patients cognitively decouple clinical competence from service delivery—Technical–Functional Divergence appeared in half of mixed-sentiment cases—and that positive and negative reviews organize quality dimensions differently. We recommend a complementary approach: topic modeling for exploratory discovery and ABSA for diagnostic assessment. For healthcare quality improvement, hospitals should separate clinical signals from operational signals in feedback dashboards. </sec>

## 키워드

Latent Dirichlet allocation, Topic model, Sentiment analysis, Quality (philosophy), Jaccard index, Service (business), Service quality, Information quality

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

