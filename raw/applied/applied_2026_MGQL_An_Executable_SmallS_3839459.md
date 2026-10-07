---
title: "MGQL: An Executable, Small-Step Semantics of GQL"
authors: ['Aditya Thimmaiah', 'Tong-Nong Lin', 'Milos Gligoric']
year: 2026
publication_date: 2026-10-01
venue: "Proceedings of the ACM on Programming Languages"
volume: "10"
issue: "OOPSLA2"
pages: "348-374"
doi: "https://doi.org/10.1145/3839459"
oa_status: "diamond"
openalex_id: "https://openalex.org/W7204235894"
query_keyword: "social network"
tags: ['Graph Theory and Algorithms', 'Advanced Database Systems and Queries', 'Logic, programming, and type systems']
keywords: ['graph query languages', 'operational semantics', 'small-step semantics', 'property graphs', 'bag semantics', 'type soundness', 'query correctness']
source: openalex-keyword
---

# MGQL: An Executable, Small-Step Semantics of GQL

**저자**: Aditya Thimmaiah; Tong-Nong Lin; Milos Gligoric
**출처**: Proceedings of the ACM on Programming Languages, Vol.10 No.OOPSLA2, pp.348-374
**발행일**: 2026-10-01
**DOI**: https://doi.org/10.1145/3839459
**수집 키워드**: social network

## 초록

Research and development of graph query languages has been gaining traction with the increase in popularity of graph databases, specifically due to the flexible schema and other rich semantic offerings of the latter’s most common underlying data model: the property graph. This has culminated in the standardization of the ISO Graph Query Language (GQL) as ISO/IEC 39075 in 2024, the first international standard for property graph- based graph query languages. However, ISO/IEC 39075 codifies its semantics informally across 600+ pages of prose, making it difficult to formally reason about the standard or for a standard-faithful implementation. Existing formalizations are not adequate because they either: (1) significantly reduce the semantic complexity by omitting bag semantics, schemas, and composite queries on multiple graphs; (2) or significantly reduce the syntactic complexity by only considering isolated fragments such as pattern-matching, leaving the full query pipeline unformalized. Yet it is these semantic–syntactic features that make formalizing GQL non-trivial. We present MGQL, the first mechanized, small-step operational semantics for a substantial read-only fragment of GQL that is grounded in the ISO/IEC 39075 standard. Our formalization models multi-graph property graphs with mixed edge directionality and supports a large fraction of GQL pattern constructs: quantified paths and edges, directional and undirected matching, label expressions, pattern lists, and composite queries. The semantics is supported by a schema-aware type system that refines variable types via closed-graph schemas, tracks nullability, supports multiple composite query operators, and models quantified-path bindings with list types. We prove that our type system is sound, ensuring an end-to-end guarantee of well-formed queries yielding results that conform to their declared schemas. MGQL provides the first bridge between GQL’s informal specification and a mechanized implementation, enabling formal reasoning about correctness.

## 키워드

graph query languages, operational semantics, small-step semantics, property graphs, bag semantics, type soundness, query correctness

## 주제 분류 (OpenAlex Topics)

- Graph Theory and Algorithms (score: 0.540)
- Advanced Database Systems and Queries (score: 0.267)
- Logic, programming, and type systems (score: 0.137)

## 메모

