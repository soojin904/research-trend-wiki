---
title: "A Big Data–Driven Topical Landscape Analysis of Academic Research on K-POP Idols"
authors: ['Yeun-Jeong Kim', 'Yeon-A Kim']
year: 2025
venue: "Journal of Korean Traditional Costume"
tags: ['Asian Culture and Media Studies', 'Computational and Text Analysis Methods', 'Diverse Topics in Contemporary Research']
source: raw/applied/applied_2025_A_Big_DataDriven_Topical__jktc_2025_12_28_4_45.md
---

# A Big Data–Driven Topical Landscape Analysis of Academic Research on K-POP Idols

**제목(한글)**: K-POP 아이돌 학술 연구의 빅데이터 기반 토픽 지형 분석

## 한국어 요약

**연구질문**: K-POP 아이돌 관련 국내 학술 연구의 토픽 지형은 무엇이며, 그 안에서 미용 및 패션 관련 논의는 어떻게 위치하는가?

**방법론**:
- 국내 K-POP 아이돌 학술 연구에 대한 정량적 텍스트 마이닝 분석 (quantitative text-mining analysis) 수행
- 2008년부터 2025년 11월까지 RISS(Research Information Sharing Service)에서 'K-POP 아이돌' 관련 용어가 제목 또는 초록에 포함된 학술 논문 수집
- 메타데이터가 불완전한 문헌 제외 후, 최종 326편의 논문 분석 대상으로 확정

**주요 결과**:
- (제공된 초록의 첫 부분에는 주요 결과가 명시되어 있지 않습니다.)

**저자**: Yeun-Jeong Kim; Yeon-A Kim
**출처**: Journal of Korean Traditional Costume, Vol.28, pp.45-56
**발행일**: 2025-12-31
**DOI**: https://doi.org/10.16885/jktc.2025.12.28.4.45

## 초록 (원문)

This study conducts a quantitative text-mining analysis of Korean academic research on K-POP idols to systematically identify the topical landscape and clarify how beauty- and fashion-related discussions are situated within the broader scholarly discourse. Academic papers containing terms related to “K-POP idol” in either the title or abstract were collected from the Research Information Sharing Service from 2008 to November 2025. After excluding documents with incomplete metadata, 326 papers were finalized for analysis. The preprocessing procedure included constructing a stopword dictionary, performing morphological analysis with kiwipiepy, extracting noun-type tokens, and applying a minimum length filter of 2 characters, yielding a total of 26,065 noun tokens. Methodologically, both CountVectorizer and TF-IDF were employed to extract keywords that capture both frequency and contextual rarity. A one-mode co-occurrence matrix was then constructed to generate a keyword network, and four centrality measures—degree, closeness, betweenness, and eigenvector centrality—were calculated using NetworkX. Visualization was performed using a spring-layout mapping combined with Louvain community detection to reveal meaningful sub-clusters within the semantic structure. The results indicate that “BTS,” “women,” “image,” “generation,” “global,” and “change” consistently occupy the core of the research landscape, showing high values in both TF-IDF and centrality measures. Degree and closeness centrality revealed a dense and balanced network, whereas betweenness centrality highlighted “design” and “storytelling” as conceptual hinges connecting otherwise separated thematic clusters. Eigenvector centrality further demonstrated that visuality- and identity-related terms—such as “women,” “image,” and “music video”—hold strong influence within the discourse. Longitudinal trends show a marked increase in publication volume after 2018, peaking in 2024–2025, reflecting the institutionalization of fandom-based production culture, platform-driven media structures, and the global expansion of K-POP. This study contributes methodological value by integrating TF-IDF weighting, keyword co-occurrence networks, and centrality analyses to identify both saturated areas and underexplored directions within the field. Limitations include the exclusive reliance on domestic literature and abstract-level text, which restricts the ability to capture international trends fully. Future research should expand the corpus to global academic databases, incorporate full-text analysis, and integrate social media datasets, fandom-generated content, and brand-collaboration materials to deepen the comparative and applied implications of K-POP idol studies.

## 키워드

Centrality, Betweenness centrality, Graph drawing, Thematic analysis, Social network analysis, Filter (signal processing), Big data

## 위키 연관

- [[pages/methods/centrality|Centrality]]

## 메모

