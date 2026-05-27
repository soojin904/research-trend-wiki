---
title: "Public Discussion of DeepSeek Large Language Model on Twitter: A Mixed-Methods Sentiment and Topic Modeling"
authors: ['Wei Chien Ng', 'Shiwen Chen', 'Qiuqing Ang', 'Yu Qing Soong']
year: 2026
venue: "Artificial Intelligence and Applications"
tags: ['Sentiment Analysis and Opinion Mining', 'Computational and Text Analysis Methods', 'Misinformation and Its Impacts']
source: raw/applied/applied_2026_Public_Discussion_of_Deep_bonviewaia62027447.md
---

# Public Discussion of DeepSeek Large Language Model on Twitter: A Mixed-Methods Sentiment and Topic Modeling
**제목(한글)**: 트위터에 나타난 딥시크(DeepSeek) 대형 언어 모델에 관한 대중적 논의: 감성 분석 및 토픽 모델링 혼합 연구

**저자**: Wei Chien Ng; Shiwen Chen; Qiuqing Ang; Yu Qing Soong
**출처**: Artificial Intelligence and Applications, Vol.None
**발행일**: 2026-03-25
**DOI**: https://doi.org/10.47852/bonviewaia62027447

## 한국어 요약

**연구질문**: 트위터(X) 플랫폼에서 글로벌 신흥 모델인 딥시크(DeepSeek) LLM에 대한 대중의 감성 반응과 주요 핵심 주제는 어떻게 분포하며, 사건 발생 시점별로 주제별 태도가 어떻게 변화했는가?

**방법론**:
- 공개된 영어 트윗 데이터셋 수집 및 정제
- 사전식 감성 사전을 활용하는 VADER 알고리즘을 이용해 감성 레이블링 수행
- VADER 레이블에 기반한 층화 표본 추출(stratified sampling)로 5,000건의 분석 데이터 확보
- 잠재 디리클레 할당(LDA) 토픽 모델링 및 일관성(coherence) 스코어 검증 수행

**주요 결과**:
- 대중들의 딥시크 모델에 대한 전체적인 감성 온도는 우호적/긍정적 여론이 우세함을 확인함
- 기술 성능, 경제적 비용 파장, 문화적/정치적 환경, 국가 간 AI 기술 경쟁 구도를 아우르는 10개의 최적 토픽을 추출하여 비즈니스 인텔리전스적 대안을 제시함


## 초록 (원문)

Artificial intelligence (AI) has moved from research laboratories into everyday tools used by millions worldwide. In recent years, advances in natural language AI systems have sparked extensive public exploration and discussion. This study investigates overall public sentiment and key discussion topics related to the DeepSeek large language model (LLM) on Twitter (now rebranded as X) and examines sentiment differences across discussion topics during various DeepSeek-related events. After data collection, Python was used to perform preliminary cleaning and screening of English-language tweets. The Valence Aware Dictionary and Sentiment Reasoner (VADER) sentiment analysis tool was applied to classify tweet sentiment. Based on the VADER labels, the dataset was stratified to obtain a high-quality sample of 5000 tweets while preserving the original sentiment distribution. To further explore discussion themes, latent Dirichlet allocation combined with coherence score evaluation was employed for topic modeling. Topic-level sentiment analysis was then conducted across different DeepSeek-related events to assess public attitudes toward each discussion topic. Results indicate that overall public sentiment toward DeepSeek LLM is predominantly positive. Topic modeling identified 10 optimal discussion topics, covering areas such as technical performance, economic impact, political and cultural context, and international competition. The findings also reveal significant differences in sentiment distribution across topics, demonstrating the practical value of combining sentiment analysis and topic modeling for business intelligence and AI product optimization. Received: 29 August 2025 | Revised: 26 December 2026 | Accepted: 11 March 2026 Conflicts of Interest The authors declare that they have no conflicts of interest to this work. Data Availability Statement The data that support the findings of this study are openly available in Kaggle at https://www.kaggle.com/datasets/bwandowando/tweets-and-reaction-on-deepseek-models and https://www.kaggle.com/datasets/datatattle/covid-19-nlp-text-classification. Author Contribution Statement Wei Chien Ng: Conceptualization, Methodology, Resources, Writing – original draft, Supervision, Project administration, Funding acquisition. Shiwen Chen: Methodology, Software, Formal analysis, Investigation, Data curation, Writing – original draft. Quan Kai Ang: Writing – review &amp; editing, Visualization. Yu Qing Soong: Validation, Writing – review &amp; editing.

## 키워드

Sentiment analysis, Topic model, Latent Dirichlet allocation, Language model, Python (programming language), Coherence (philosophical gambling strategy), Natural language understanding, Big data

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

