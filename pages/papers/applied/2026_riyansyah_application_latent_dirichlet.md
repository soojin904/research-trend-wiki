---
title: "Application of Latent Dirichlet Allocation (LDA) and BERTopic Algorithms for Headline and Topic Analysis of Palestine–Israel Conflict News in Indonesian Online Media"
authors: ['Raden Gumilar Riyansyah', 'Sajarwo Anggai', 'Tukiyat Tukiyat']
year: 2026
venue: "Jurnal Impresi Indonesia"
tags: ['Sentiment Analysis and Opinion Mining', 'Edcuational Technology Systems', 'Computational and Text Analysis Methods']
source: raw/applied/applied_2026_Application_of_Latent_Dir_jii_v5i1_7395.md
---

# Application of Latent Dirichlet Allocation (LDA) and BERTopic Algorithms for Headline and Topic Analysis of Palestine–Israel Conflict News in Indonesian Online Media
**제목(한글)**: 인도네시아 온라인 미디어의 팔레스타인-이스라엘 갈등 뉴스 헤드라인 및 토픽 분석을 위한 LDA와 BERTopic 알고리즘 적용

**저자**: Raden Gumilar Riyansyah; Sajarwo Anggai; Tukiyat Tukiyat
**출처**: Jurnal Impresi Indonesia, Vol.5, pp.97-114
**발행일**: 2026-01-09
**DOI**: https://doi.org/10.58344/jii.v5i1.7395

## 한국어 요약

**연구질문**: 인도네시아 뉴스 미디어에 게재된 방대하고 상이한 필체의 팔레스타인-이스라엘 갈등 보도로부터 핵심적인 의미론적 토픽 구조를 도출하기 위해 전통적 통계 모델(LDA)과 최신 트랜스포머 기반 모델(BERTopic)을 어떻게 효과적으로 결합 및 비교할 수 있는가?

**방법론**:
- 온라인 뉴스 데이터를 스크랩하여 텍스트 정제, 토큰화, 정규화, 어간 추출 등 전처리 적용
- LDA 모델은 일관성 점수(Coherence Score) 및 복잡도(Perplexity)를 기준으로 튜닝하고, BERTopic 모델은 트랜스포머 임베딩과 UMAP 차원 축소 및 HDBSCAN 군집화를 조합하여 비교 검증

**주요 결과**:
- BERTopic 모델이 최고의 일관성 점수인 0.99를 획득하여 가장 정교한 세부 의미 구조를 구축했으나, 전체적인 확률 모델링의 안정성 면에서는 여전히 LDA가 효과적임을 식별
- 최종적으로 가자지구 폭격, 인도네시아의 외교 정책, 국제사회의 지지, 인도주의적 지원, 글로벌 정세 등 5대 메인 토픽 맵을 안정적으로 추출


## 초록 (원문)

The news coverage of the Palestine–Israel conflict has become one of the most dominant international issues in Indonesian online media, necessitating a systematic analysis to understand the topic structures formed from the intensity and variation of the narratives presented. The main challenges arise from the high volume of text, differences in writing styles across media outlets, and the diversity of terminology, all of which hinder consistent and manual topic identification. To address these challenges, this study proposes a combined and comparative approach using two topic modeling algorithms, LDA and BERTopic, to obtain a more accurate, structured, and interpretable topic mapping. The modeling process begins with data collection through web scraping, followed by a preprocessing stage consisting of cleansing, case folding, tokenization, normalization, filtering, and stemming. The LDA model is developed by determining the optimal number of topics based on Coherence Score and Perplexity, whereas BERTopic leverages transformer-based embeddings, UMAP dimension reduction, and HDBSCAN clustering. Evaluation is conducted using Coherence Score, Perplexity, Silhouette Score, and visualizations such as Intertopic Distance Maps and Word Clouds to assess topic quality. The results show that BERTopic achieves the highest coherence score of 0.99 and lower perplexity, producing semantically cohesive topics. Meanwhile, LDA remains advantageous in providing a stable and measurable probabilistic structure. The combination of both models yields a mapping of five main topics: attacks in Gaza, Indonesian diplomacy, international support, humanitarian issues, and global political dynamics. These findings demonstrate that integrating LDA and BERTopic enhances the quality of topic analysis on complex issues

## 키워드

Topic model, Latent Dirichlet allocation, Headline, Automatic summarization, Coherence (philosophical gambling strategy), Tag cloud, Preprocessor, Social media

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

