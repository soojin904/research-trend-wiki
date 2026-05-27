---
title: "Taxonomy-Aligned Risk Extraction from 10-K Filings with Autonomous Improvement Using LLMs"
authors: ['Rian Dolphin', 'Joe Dursun', 'Jarrett Blankenship', 'Katie Adams', 'Quinton Pike']
year: 2026
venue: "ArXiv.org"
tags: ['Topic Modeling', 'Software Engineering Research', 'Advanced Text Analysis Techniques']
source: raw/applied/applied_2026_TaxonomyAligned_Risk_Extr_nodoi.md
---

# Taxonomy-Aligned Risk Extraction from 10-K Filings with Autonomous Improvement Using LLMs
**제목(한글)**: LLM을 활용한 10-K 공시 보고서의 분류체계 정합 리스크 추출 및 자율 개선

## 한국어 요약

**연구질문**: S&P 500 기업들의 10-K 공시 보고서에서 사전 정의된 계층적 리스크 분류체계에 맞는 구조화된 리스크 요인을 어떻게 자동 추출하고 품질을 자율적으로 유지할 수 있는가?

**방법론**:
- 3단계 파이프라인 구성: (1) LLM 기반 리스크 추출 및 근거 인용문 생성, (2) 임베딩(Embedding) 기반 의미적 분류체계 매핑, (3) LLM-as-a-judge 검증으로 오분류 필터링
- AI 에이전트가 평가 피드백을 분석하여 문제적 카테고리를 식별·진단하고 분류체계 개선안을 제안하는 자율 분류체계 유지관리 메커니즘 도입

**주요 결과**:
- S&P 500 기업에서 10,688개의 리스크 요인을 추출하고 산업 클러스터별 리스크 프로파일 유사도 분석
- 동일 산업 기업이 이종 산업 기업 대비 63% 높은 리스크 프로파일 유사도를 보여 분류체계가 경제적으로 의미 있는 구조를 포착함을 확인(Cohen's d=1.06, AUC 0.82)

**저자**: Rian Dolphin; Joe Dursun; Jarrett Blankenship; Katie Adams; Quinton Pike
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-01-21
**DOI**: 

## 초록 (원문)

We present a methodology for extracting structured risk factors from corporate 10-K filings while maintaining adherence to a predefined hierarchical taxonomy. Our three-stage pipeline combines LLM extraction with supporting quotes, embedding-based semantic mapping to taxonomy categories, and LLM-as-a-judge validation that filters spurious assignments. To evaluate our approach, we extract 10,688 risk factors from S&P 500 companies and examine risk profile similarity across industry clusters. Beyond extraction, we introduce autonomous taxonomy maintenance where an AI agent analyzes evaluation feedback to identify problematic categories, diagnose failure patterns, and propose refinements, achieving 104.7% improvement in embedding separation in a case study. External validation confirms the taxonomy captures economically meaningful structure: same-industry companies exhibit 63% higher risk profile similarity than cross-industry pairs (Cohen's d=1.06, AUC 0.82, p<0.001). The methodology generalizes to any domain requiring taxonomy-aligned extraction from unstructured text, with autonomous improvement enabling continuous quality maintenance and enhancement as systems process more documents.

## 키워드

Pipeline (software), Taxonomy (biology), Process (computing), Embedding, Spurious relationship, Domain (mathematical analysis)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

