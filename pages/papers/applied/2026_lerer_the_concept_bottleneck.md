---
title: "The Concept Bottleneck as a Deterministic Evaluation Layer: Implementation of Small Concept Models for Legal Reasoning via OpenAI Structured Outputs"
authors: ['Ignacio Adrián LERER']
year: 2026
venue: "Zenodo (CERN European Organization for Nuclear Research)"
tags: ['Explainable Artificial Intelligence (XAI)', 'Artificial Intelligence in Law', 'Computational and Text Analysis Methods']
source: raw/applied/applied_2026_The_Concept_Bottleneck_as_zenodo_19373344.md
---

# The Concept Bottleneck as a Deterministic Evaluation Layer: Implementation of Small Concept Models for Legal Reasoning via OpenAI Structured Outputs
**제목(한글)**: 결정론적 평가 레이어로서의 개념 병목: OpenAI 구조화 출력을 통한 법률 추론용 소형 개념 모델 구현

**저자**: Ignacio Adrián LERER
**출처**: Zenodo (CERN European Organization for Nuclear Research), Vol.None
**발행일**: 2026-04-01
**DOI**: https://doi.org/10.5281/zenodo.19373344

## 한국어 요약


## 초록 (원문)

Large Language Models process text through statistical token prediction, producing outputs that are non-deterministic and difficult to audit. This paper presents a working implementation of the Concept Bottleneck principle applied to legal text analysis. Rather than training a specialized small model, the system forces a general-purpose LLM (GPT-4o) to project any legal text onto a fixed 24-dimensional concept space, the Universal Legal Principles of the Lerer Architecture, producing a deterministic score vector in [0,1]24 via OpenAI Structured Outputs and Zod schema validation. The implementation runs three independent evaluations in parallel (triple-run consensus), averages the resulting scores, and reports per-principle variance (confidence_spread) as a first-class output. The complete pipeline is deployed as a Model Context Protocol (MCP) server, enabling integration with any MCP-compatible client. Observations from a single-operator production deployment indicate that the triple-run consensus reduces per-principle variance by approximately 60-70% compared to single-run evaluation, and that confidence_spread values above 0.15 reliably identify semantically ambiguous texts. The paper extends the theoretical framework of Lerer (2025) with empirical observations from the running system, discusses the relationship to Meta's Large Concept Models (Barrault et al., 2024), and maps the Concept Bottleneck pattern onto five non-legal professional domains: medical triage, financial risk, corporate governance, educational assessment, and regulatory compliance. Code is available at https://github.com/adrianlerer/omnibrain-mcp under MIT license.

## 키워드

Bottleneck, Security token, Variance (accounting), Process (computing), Context (archaeology), Software deployment, Schema (genetic algorithms)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

