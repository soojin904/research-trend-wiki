---
title: "Mind the Shift: Decoding Monetary Policy Stance from FOMC Statements with Large Language Models"
authors: ['Yixuan Tang', 'Yi Yang']
year: 2026
publication_date: 2026-03-15
venue: "ArXiv.org"
volume: "None"
issue: "None"
pages: ""
doi: ""
oa_status: "green"
openalex_id: "https://openalex.org/W7139145238"
query_keyword: "text analysis"
tags: ['Computational and Text Analysis Methods', 'Monetary Policy and Economic Impact', 'Stock Market Forecasting Methods']
keywords: ['Statement (logic)', 'Tone (literature)', 'Task (project management)', 'Interpretation (philosophy)', 'Treasury', 'Measure (data warehouse)', 'Inflation (cosmology)', 'Monetary policy']
source: openalex-keyword
---

# Mind the Shift: Decoding Monetary Policy Stance from FOMC Statements with Large Language Models

**저자**: Yixuan Tang; Yi Yang
**출처**: ArXiv.org
**발행일**: 2026-03-15
**DOI**: 
**수집 키워드**: text analysis

## 초록

Federal Open Market Committee (FOMC) statements are a major source of monetary-policy information, and even subtle changes in their wording can move global financial markets. A central task is therefore to measure the hawkish--dovish stance conveyed in these texts. Existing approaches typically treat stance detection as a standard classification problem, labeling each statement in isolation. However, the interpretation of monetary-policy communication is inherently relative: market reactions depend not only on the tone of a statement, but also on how that tone shifts across meetings. We introduce Delta-Consistent Scoring (DCS), an annotation-free framework that maps frozen large language model (LLM) representations to continuous stance scores by jointly modeling absolute stance and relative inter-meeting shifts. Rather than relying on manual hawkish--dovish labels, DCS uses consecutive meetings as a source of self-supervision. It learns an absolute stance score for each statement and a relative shift score between consecutive statements. A delta-consistency objective encourages changes in absolute scores to align with the relative shifts. This allows DCS to recover a temporally coherent stance trajectory without manual labels. Across four LLM backbones, DCS consistently outperforms supervised probes and LLM-as-judge baselines, achieving up to 71.1% accuracy on sentence-level hawkish--dovish classification. The resulting meeting-level scores are also economically meaningful: they correlate strongly with inflation indicators and are significantly associated with Treasury yield movements. Overall, the results suggest that LLM representations encode monetary-policy signals that can be recovered through relative temporal structure.

## 키워드

Statement (logic), Tone (literature), Task (project management), Interpretation (philosophy), Treasury, Measure (data warehouse), Inflation (cosmology), Monetary policy

## 주제 분류 (OpenAlex Topics)

- Computational and Text Analysis Methods (score: 0.184)
- Monetary Policy and Economic Impact (score: 0.117)
- Stock Market Forecasting Methods (score: 0.061)

## 메모

