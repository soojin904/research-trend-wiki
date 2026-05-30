---
title: "pyBiblioNet: a Python library for a comprehensive network-based bibliometric analysis"
authors: ['Mirko Lai', 'Salvatore Vilella', 'Federica Cena', 'Giancarlo Ruffo']
year: 2025
venue: "Scientometrics"
tags: ['scientometrics and bibliometrics research', 'Complex Network Analysis Techniques', 'Bioinformatics and Genomic Networks']
source: raw/applied/applied_2025_pyBiblioNet_a_Python_libr_s11192_025_05458_0.md
---

# pyBiblioNet: a Python library for a comprehensive network-based bibliometric analysis

**제목(한글)**: pyBiblioNet: 네트워크 기반 종합 서지계량 분석을 위한 파이썬 라이브러리

## 한국어 요약

**연구질문**: 기존 서지계량 분석 방법의 한계를 극복하고, 인용 네트워크·공저 네트워크·키워드 공출현 네트워크를 통합적으로 분석할 수 있는 오픈소스 도구를 어떻게 설계할 수 있는가?

**방법론**:
- OpenAlex API와 연동하여 서지 데이터를 자동 수집 및 전처리
- 인용 네트워크(Citation Network), 공저 네트워크(Co-authorship Network), 키워드 공출현 네트워크(Keyword Co-occurrence Network) 구축
- 네트워크 중심성(Centrality), 군집화(Clustering), 커뮤니티 탐지(Community Detection) 알고리즘 적용
- NLP 기법을 활용한 핵심 토픽 및 개념 분석

**주요 결과**:
- pyBiblioNet 라이브러리를 통해 서지계량 분석 전 과정(데이터 수집→전처리→시각화→분석)을 통합 수행 가능
- '15분 도시(15-minute city)' 패러다임 사례 분석으로 숨겨진 패턴과 신흥 연구 트렌드 도출
- 연구자·사서·정책입안자를 위한 데이터 기반 의사결정 지원 도구로서의 실용성 확인

**저자**: Mirko Lai; Salvatore Vilella; Federica Cena; Giancarlo Ruffo
**출처**: Scientometrics, Vol.130, pp.7139-7190
**발행일**: 2025-12-01
**DOI**: https://doi.org/10.1007/s11192-025-05458-0

## 초록 (원문)

Bibliometric analysis is a critical tool for understanding the structure, dynamics, and impact of scientific research. Traditional methods often fall short in capturing the intricate relationships and evolving trends within scientific literature. To address this gap, we present pyBiblioNet, a Python library designed to facilitate comprehensive network-based bibliometric analysis, providing insights into citation networks, co-authorship networks, and keyword co-occurrence networks. The library integrates with OpenAlex, a popular and open catalogue to the global research system, enabling users to easily preprocess, visualize, and analyse bibliometric data. Key features include topic selection, automatic data download via OpenAlex APIs, creation of the root and base sets of manuscripts to analyze, creation of the citation and co-authorship networks, network visualization tools, and a suite of algorithms for computing network centralities, clustering, and community detection, all of them tailored to the bibliometric domain. Additionally, it enables the analysis of key topics and concepts using NLP techniques. We showcase the main functions of the library by performing a bibliometric analysis on the multidisciplinary “15-minute city paradigm”, demonstrating the utility of pyBiblioNet in uncovering hidden patterns and emerging trends in various scientific domains. pyBiblioNet can empower researchers, librarians, and policymakers with a powerful, user-friendly tool for enhancing their bibliometric analyses and making data-driven decisions.

## 키워드

Python (programming language), Multidisciplinary approach, Suite, Bibliometrics, Citation, Visualization, Key (lock), Citation analysis

## 위키 연관

- [[pages/methods/mixed_methods|복합 방법론]]

## 메모

