---
title: "TTSR: Test-Time Self-Reflection for Continual Reasoning Improvement"
authors: ['Haoyang He', 'Zihua Rong', 'Liangjie Zhao', 'Yunjia Zhao', 'Lan Yang (457660)', 'Honggang Zhang']
year: 2026
publication_date: 2026-02-06
venue: "arXiv (Cornell University)"
volume: "None"
issue: "None"
pages: ""
doi: ""
oa_status: "green"
openalex_id: "https://openalex.org/W7134016865"
query_keyword: "text analysis"
tags: ['Topic Modeling', 'Multimodal Machine Learning Applications', 'Intelligent Tutoring Systems and Adaptive Learning']
keywords: ['Process (computing)', 'Test (biology)', 'Case-based reasoning', 'Adaptation (eye)', 'Model-based reasoning', 'Reasoning system', 'Adaptive reasoning', 'Non-monotonic logic']
source: openalex-keyword
---

# TTSR: Test-Time Self-Reflection for Continual Reasoning Improvement

**저자**: Haoyang He; Zihua Rong; Liangjie Zhao; Yunjia Zhao; Lan Yang (457660); Honggang Zhang
**출처**: arXiv (Cornell University)
**발행일**: 2026-02-06
**DOI**: 
**수집 키워드**: text analysis

## 초록

Test-time Training enables model adaptation using only test questions and offers a promising paradigm for improving the reasoning ability of large language models (LLMs). However, it faces two major challenges: test questions are often highly difficult, making self-generated pseudo-labels unreliable, and existing methods lack effective mechanisms to adapt to a model's specific reasoning weaknesses, leading to inefficient learning. To address these issues, we propose \textbf{TTSR}, a self-reflective test-time self-evolving training framework. TTSR employs a single pretrained language model that alternates between the roles of a \textit{Student} and a \textit{Teacher} at test time. The Student focuses on solving problems and learning from synthesized variant questions, while the Teacher analyzes the Student's failed reasoning trajectories, summarizes recurring reasoning weaknesses, and synthesizes targeted variant questions accordingly. This process guides the model to improve within a learnable regime through a continual self-evolving loop. Experimental results on multiple challenging mathematical reasoning benchmarks show that TTSR consistently improves reasoning performance and generalizes well across different model backbones and general-domain reasoning tasks. These findings suggest that teacher-mediated self-reflection provides an effective pathway for stable and continual reasoning improvement at test time.

## 키워드

Process (computing), Test (biology), Case-based reasoning, Adaptation (eye), Model-based reasoning, Reasoning system, Adaptive reasoning, Non-monotonic logic

## 주제 분류 (OpenAlex Topics)

- Topic Modeling (score: 0.560)
- Multimodal Machine Learning Applications (score: 0.059)
- Intelligent Tutoring Systems and Adaptive Learning (score: 0.056)

## 메모

