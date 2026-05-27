---
title: "Spherical Double K-Means: A Co-clustering Approach for Textual Data Analysis"
authors: ['Ilaria Bombelli', 'Domenica Fioredistella Iezzi', 'Emiliano Seri', 'Maurizio Vichi']
year: 2026
venue: "Journal of Classification"
tags: ['Computational and Text Analysis Methods', 'Complex Network Analysis Techniques', 'Advanced Clustering Algorithms Research']
source: raw/applied/applied_2026_Spherical_Double_KMeans_A_s00357_026_09544_7.md
---

# Spherical Double K-Means: A Co-clustering Approach for Textual Data Analysis
**제목(한글)**: 구형 더블 K-Means: 텍스트 데이터 분석을 위한 공동 군집화 접근법

**저자**: Ilaria Bombelli; Domenica Fioredistella Iezzi; Emiliano Seri; Maurizio Vichi
**출처**: Journal of Classification, Vol.None
**발행일**: 2026-03-06
**DOI**: https://doi.org/10.1007/s00357-026-09544-7

## 한국어 요약

**연구질문**: 문서 단어 행렬(TF-IDF 등)을 클러스터링할 때, 문서군뿐만 아니라 연관 단어군도 동시에 정밀하게 묶는 공동 군집화(Co-clustering)를 어떻게 계산 효율적으로 수행할 수 있는가?

**방법론**:
- 문서와 연관 핵심 어휘를 동시에 묶는 구형 더블 K-Means(SDKM) 알고리즘 제안
- 인공 데이터셋 및 1789~2021년 미국 대통령 취임사 코퍼스, 20 Newsgroups 벤치마크 코퍼스로 유효성 검증

**주요 결과**:
- SDKM이 토픽 식별과 키워드 추출 성능을 대폭 개선하고 시계열적 주제 변동을 효과적으로 포착함을 증명
- 텍스트 데이터 이면에 숨겨진 단어-문서 결합 패턴 구조를 발견하여 학술 문서에 대한 해석적 이해도를 제고


## 초록 (원문)

Abstract In text analysis, spherical k-means (SKM) is a specialized k-means clustering algorithm widely utilized for grouping documents represented in high-dimensional, sparse term-document matrices, often normalized using techniques like TF-IDF. Researchers frequently seek to cluster not only documents but also the terms associated with them into coherent groups. To address this dual clustering requirement, we introduce spherical double k-means (SDKM), a novel methodology that simultaneously clusters documents and terms. This methodology offers several advantages, such as enabling more effective topic identification and keyword extraction, enhancing interpretability, computational efficiency, and efficiency in capturing dynamic changes in thematic content over time. It also facilitates the uncovering of nuanced patterns and structures of textual data. We apply SDKM to simulated and real data. The real data applications are on the corpus of US presidential inaugural addresses, spanning from George Washington in 1789 to Joe Biden in 2021, and to the 20 Newsgroups corpus. Our analysis reveals distinct clusters of words and documents that correspond to significant themes and periods, showcasing the method’s ability to facilitate a deeper understanding of the data. Our findings demonstrate the efficacy of SDKM in uncovering underlying patterns in textual data.

## 키워드

Cluster analysis, Identification (biology), George (robot), Thematic map, Cluster (spacecraft), Document clustering, Dual (grammatical number)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

