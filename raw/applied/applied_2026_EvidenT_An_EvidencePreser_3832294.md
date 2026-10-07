---
title: "EvidenT: An Evidence-Preserving Framework for Iterative System-Level Package Repair"
authors: ['Chenyu Zhao', 'Minghua Ma', 'Shenglin Zhang', 'Zeshun Huang', 'Yongqian Sun', 'Chetan Bansal', 'Saravan Rajmohan', 'Dan Pei']
year: 2026
publication_date: 2026-10-01
venue: "Proceedings of the ACM on software engineering."
volume: "3"
issue: "ISSTA"
pages: "4653-4673"
doi: "https://doi.org/10.1145/3832294"
oa_status: "hybrid"
openalex_id: "https://openalex.org/W7160904034"
query_keyword: "social network"
tags: ['Software Engineering Research', 'Software Testing and Debugging Techniques', 'Software System Performance and Reliability']
keywords: ['evidence preservation', 'iterative repair', 'failure localization']
source: openalex-keyword
---

# EvidenT: An Evidence-Preserving Framework for Iterative System-Level Package Repair

**저자**: Chenyu Zhao; Minghua Ma; Shenglin Zhang; Zeshun Huang; Yongqian Sun; Chetan Bansal; Saravan Rajmohan; Dan Pei
**출처**: Proceedings of the ACM on software engineering., Vol.3 No.ISSTA, pp.4653-4673
**발행일**: 2026-10-01
**DOI**: https://doi.org/10.1145/3832294
**수집 키워드**: social network

## 초록

Frequent toolchain updates and the expanding diversity of instruction set architectures (ISAs) have made large-scale system-level software package repair a critical task. Diagnosing and repairing build failures remains challenging due to heterogeneous failure evidence, complex dependency constraints, and architecture-specific build conventions. While recent LLM-based repair methods have shown promise for project-level source code fixes, they struggle with system-level repair where failures involve multi-language artifacts (e.g., build recipes, scripts, and source archives) and require iterative validation through external build services. In this paper, we first conduct a systematic empirical study of real-world system-level build failures. Our findings reveal that 72% of successful repairs primarily involve adjustments to build configurations, dependencies, or environment settings rather than isolated source-code modifications, suggesting that effective repair must prioritize packaging logic and iterative feedback. Motivated by these insights, we propose EvidenT, an evidence-preserving repair framework that decouples iteration-aware evidence management from tool execution. EvidenT comprises (1) an external Build Service for reproducible build execution and feedback; (2) an Evidence-Preserving Repair Controller that performs cross-modal fusion of repair history, knowledge context, and build artifacts; and (3) an automated Repair Orchestrator that executes a suite of modular tools for failure localization and system-level repair actions within a closed-loop validation environment. We evaluate EvidenT on a benchmark of 219 real-world RISC-V package build failures. EvidenT successfully repairs 118 packages (53.88%), substantially outperforming state-of-the-art agentic baselines (20.55%) and direct LLM-based repair (1.83%). To demonstrate its architectural generality, we extend EvidenT to other ISAs by updating only ISA-specific knowledge context. In preliminary experiments, it achieves success rates of 41.77% on aarch64 and 46.99% on x86_64, showcasing its robustness across diverse hardware ecosystems.

## 키워드

evidence preservation, iterative repair, failure localization

## 주제 분류 (OpenAlex Topics)

- Software Engineering Research (score: 0.614)
- Software Testing and Debugging Techniques (score: 0.355)
- Software System Performance and Reliability (score: 0.008)

## 메모

