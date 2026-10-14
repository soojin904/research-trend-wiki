---
title: "A Model-Driven Metamodel for the Systematic Design of Configurable NLP Pipelines"
authors: ['Kamal Walji', 'Allae Erraissi', 'Abdelali Zakrani', 'Mouad Banane']
year: 2026
venue: "International Journal of Advances in Soft Computing and its Applications"
tags: ['Model-Driven Software Engineering Techniques', 'Natural Language Processing Techniques', 'Software Engineering Research']
source: raw/applied/applied_2026_A_ModelDriven_Metamodel_f_ijasca_172.md
---

# A Model-Driven Metamodel for the Systematic Design of Configurable NLP Pipelines

**저자**: Kamal Walji; Allae Erraissi; Abdelali Zakrani; Mouad Banane
**출처**: International Journal of Advances in Soft Computing and its Applications, Vol.18, pp.266-295
**발행일**: 2026-10-09
**DOI**: https://doi.org/10.15849/ijasca.172

## 초록 (원문)

Natural Language Processing systems are increasingly built as configurable pipelines combining heterogeneous components, including data sources, task specifications, linguistic preprocessing, representation methods, learning models, training settings, evaluation protocols, explainability requirements, and deployment constraints. Yet these pipelines are often described either through implementation code or through informal sequences of steps, which makes their design decisions difficult to compare, reproduce, or search over automatically. Existing work at the intersection of NLP and Model-Driven Engineering has mainly used language technologies to generate UML, SysML, or DSL artifacts from textual specifications, while model-driven approaches to machine learning have addressed datasets and ML-enabled systems more broadly. This article proposes a metamodel in which the NLP pipeline itself is the modeling target. The proposed metamodel defines fifteen metaclasses organized through explicit ownership semantics, distinguishing pipeline-level, model-level, shared, and execution-generated components. It also introduces cross-cutting relations that make evaluation results traceable to the configurations that produced them. The metamodel is given a formal definition and thirteen well-formedness constraints expressed in OCL. It is instantiated on two contrasting sentiment analysis pipelines: a classical supervised configuration drawn from an executed experiment and a zero-shot configuration used as a structural test. The instantiation shows that both configurations can be represented within the same structure, that reported measurements can be traced back to their producing configurations, and that plausible malformed configurations can be rejected with an explicit diagnosis. The metamodel is intended as a foundation for NLP pipeline documentation, comparison, reproducibility, and future automatic configuration and multi-objective optimization.

## 키워드

meta-model, model-driven engineering, sentiment analysis, zero-shot learning, OCL constraints, metaclasses

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

