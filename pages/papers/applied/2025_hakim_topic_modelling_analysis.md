---
title: "Topic modelling analysis of public policy narratives on prabowo-gibran in national news"
authors: ['Lukmanul Hakim', 'Anggi Yudistira Aditya', 'Muharman Lubis']
year: 2025
venue: "Journal of Soft Computing Exploration"
tags: ['Computational and Text Analysis Methods', 'Misinformation and Its Impacts', 'Media Influence and Politics']
source: raw/applied/applied_2025_Topic_modelling_analysis__joscex_v6i4_632.md
---

# Topic modelling analysis of public policy narratives on prabowo-gibran in national news

**제목(한글)**: 인도네시아 전국 뉴스의 프라보워-기브란 공공 정책 서사에 대한 토픽 모델링 분석

## 한국어 요약

**연구질문**: 인도네시아 프라보워-기브란 행정부와 관련된 공공 정책 주제를 온라인 뉴스 미디어에 LDA 및 NMF 토픽 모델링을 적용하여 어떻게 파악할 수 있으며, 취임 전후에 어떤 변화가 있는가?

**방법론**:
- 파이썬 URL 수집으로 신뢰도 높은 뉴스 기사 200편 수집
- 텍스트 정제, 토큰화, 바이그램·트라이그램 구성 등 전처리
- LDA(잠재 디리클레 할당) 및 NMF(비음수 행렬 분해) 비지도 학습 모델 적용 및 토픽 일관성 평가
- 취임일 기준 전후 비교 및 코사인 유사도로 토픽 유사성 측정

**주요 결과**:
- NMF의 토픽 일관성(0.68)이 LDA(0.3709)보다 높음
- 취임 전후 가장 유사한 토픽 쌍의 코사인 유사도 0.663
- 토픽 모델링이 대규모 비구조적 뉴스 데이터에서 미디어 담화의 진화적 추세를 파악하는 데 효과적임을 입증

**저자**: Lukmanul Hakim; Anggi Yudistira Aditya; Muharman Lubis
**출처**: Journal of Soft Computing Exploration, Vol.6, pp.266-273
**발행일**: 2025-12-31
**DOI**: https://doi.org/10.52465/joscex.v6i4.632

## 초록 (원문)

The rapid acceleration of digital transition has become an inevitable reality of the modern era. The proliferation of online communication platforms, news portals, and heterogeneous data formats has substantially increased big data volumes, leading to large-scale collections of unstructured data. This study aims to analyze dominant public policy–related topics concerning the Prabowo–Gibran administration by applying topic modeling techniques to national online news media. Latent Dirichlet Allocation (LDA) and Non-negative Matrix Factorization (NMF) were employed as unsupervised learning approaches to extract latent semantic structure from a corpus of 200 credible news articles collected through URL fetching using Python 3. Data preprocessing included text cleaning, tokenization, bigram and trigram construction, and the development of a dictionary and corpus. Model performance was evaluated using topic coherence metrics, yielding scores of 0.3709 for LDA and 0.68 for NMF. To examine temporal dynamics, the dataset was divided based on the official inauguration date of the president and vice president, enabling a comparative analysis of dominant topics before and after the inauguration. Topic similarity across both periods was measured using cosine similarity, with the highest similarity score of 0.663 observed between Topic 4 in the pre-inauguration period and Topic 1 in the post-inauguration period. The findings provide insights into evolving media discourse and policy-related topic trends across the two periods, demonstrating the potentials of topic modeling in analyzing large-scale unstructured news data for diverse purposes to bridge computational science and empirical evidence of social science.

## 키워드

Topic model, Latent Dirichlet allocation, Headline, Big data, Trigram, Latent semantic analysis, British National Corpus, Social media

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]
- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모

