---
title: "Smart Journal Finder: A Web-Based Scientific Article Categorization Using Jaccard Similarity"
authors: ['Rodiah Rodiah']
year: 2026
venue: "ILKOM Jurnal Ilmiah"
tags: ['Edcuational Technology Systems', 'Topic Modeling', 'Text and Document Classification Technologies']
source: raw/applied/applied_2026_Smart_Journal_Finder_A_We_ilkom_v18i1_2814_17_29.md
---

# Smart Journal Finder: A Web-Based Scientific Article Categorization Using Jaccard Similarity
**제목(한글)**: 스마트 저널 파인더: 자카드 유사도를 이용한 웹 기반 과학 논문 분류 시스템

**저자**: Rodiah Rodiah
**출처**: ILKOM Jurnal Ilmiah, Vol.18, pp.17-29
**발행일**: 2026-04-20
**DOI**: https://doi.org/10.33096/ilkom.v18i1.2814.17-29

## 한국어 요약

**연구질문**: 급증하는 과학 논문들 사이에서 연구자가 본인의 원고 제목, 초록, 키워드를 입력해 적절한 학술지를 자동으로 매칭받을 수 있는 자카드 유사도 기반의 추천 웹 시스템을 어떻게 설계할 수 있는가?

**방법론**:
- 논문 제목, 초록, 키워드 데이터를 입력받아 텍스트 정제, 불용어 제거, Nazief-Adriani 알고리즘을 이용한 어간 추출 및 중복 단어 제거 수행
- 전처리된 단어 집합 간의 합집합 및 교집합 비율을 계산하는 자카드 유사도(Jaccard Similarity) 알고리즘을 적용해 연관 저널의 우선순위를 랭킹화하고 데이터베이스 구축

**주요 결과**:
- 인도네시아어로 작성된 학술지를 대상으로 한 매칭 실험에서, 입력된 원고의 주요 어휘와 기존 저널 간의 유사도를 성공적으로 연산하여 맞춤형 저널 메타데이터를 유효하게 랭킹 형태로 추천함
- 다만 현재 모델은 시맨틱(의미론적) 유사도와 다국어 처리가 제한되므로 향후 인공지능 기반 임베딩 모델의 통합 필요성을 제안


## 초록 (원문)

The rapid growth of scientific publications presents challenges for researchers in identifying appropriate journals for manuscript submission. With an overwhelming number of journals across diverse disciplines, manually matching a manuscript to a suitable journal becomes inefficient and prone to misclassification. This study proposes the Smart Journal Finder, a web-based system designed to recommend relevant scientific journals by analyzing textual similarities between user-submitted manuscripts and indexed journal articles. The system processes input data including the title, abstract, keywords, and field of study through several stages: preprocessing, stop word removal, stemming using the Nazief-Adriani algorithm, and duplicate term elimination. Similarity scoring is performed using the Jaccard Similarity algorithm, followed by ranking the results and displaying journal metadata such as subject, publisher, and citation metrics. Results show that the system accurately transforms and filters input text, effectively calculates similarity scores, and successfully matches manuscripts to appropriate journals. By automating this process, the Smart Journal Finder enhances the efficiency of journal selection, improves the relevance of publication targets, and supports researchers in increasing the visibility and impact of their work. However, the current implementation is limited to Indonesian-language journals and does not yet incorporate semantic similarity or multilingual processing. Future work will focus on expanding coverage across disciplines and integrating more advanced similarity models.

## 키워드

Jaccard index, Similarity (geometry), Categorization, Metadata, Ranking (information retrieval), Field (mathematics), Relevance (law), Bibliometrics

## 위키 연관

- [[pages/concepts/personal_network|퍼스널 네트워크]]
- [[pages/methods/mixed_methods|복합 방법론]]

## 메모

