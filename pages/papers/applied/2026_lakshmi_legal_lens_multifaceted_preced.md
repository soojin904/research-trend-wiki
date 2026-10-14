---
title: "Legal Lens: Multi-Faceted Precedent Retrieval and Case Similarity for Indian Supreme Court Jurisprudence"
authors: ['R N Srija Lakshmi', 'V. S. Anita Sofia', 'R. Kumuthaveni']
year: 2026
venue: "International Journal of Scientific Research in Science Engineering and Technology"
tags: ['Artificial Intelligence in Law', 'Information Retrieval and Search Behavior', 'Topic Modeling']
source: raw/applied/applied_2026_Legal_Lens_MultiFaceted_P_ijsrset2613523.md
---

# Legal Lens: Multi-Faceted Precedent Retrieval and Case Similarity for Indian Supreme Court Jurisprudence

**저자**: R N Srija Lakshmi; V. S. Anita Sofia; R. Kumuthaveni
**출처**: International Journal of Scientific Research in Science Engineering and Technology, Vol.13, pp.271-282
**발행일**: 2026-10-11
**DOI**: https://doi.org/10.32628/ijsrset2613523

## 초록 (원문)

The growing volume of Indian Supreme Court judgments makes manual precedent discovery increasingly difficult. Legal researchers may know the factual circumstances, statutory provision, or legal issue involved in a matter without knowing the exact terminology or case name used in earlier judgments. Conventional keyword retrieval can therefore return many superficially related documents while missing cases expressed using different language. This paper presents Legal Lens, a multi-faceted legal information retrieval system designed to retrieve and rank relevant Indian Supreme Court precedents from natural-language queries. The system uses a two-stage architecture. Candidate judgments are first retrieved using TF-IDF, BM25, and a 100-dimensional Latent Semantic Analysis representation. The retrieved candidates are then represented using 13 features covering semantic similarity, lexical similarity, BM25 score, legal issue similarity, Act similarity, section similarity, factual similarity, procedural similarity, passage similarity, title similarity, and three chunk-level similarity measures. A supervised Logistic Regression model with feature standardization is used for relevance reranking, followed by probability calibration to produce an interpretable Similarity Score. The system also provides evidence-oriented explanations through matched Acts, statutory sections, legal issues, factual and procedural patterns, and relevant passages. The deployed corpus contains 26,690 Indian Supreme Court judgments covering 1950–2025. Academic evaluation is performed using the FIRE AILA 2019 Task 1 benchmark containing 50 queries, 2,914 candidate documents, and 195 official relevance pairs. Legal Lens achieves 90.00% Top-1 accuracy, 100.00% Top-5 accuracy, 100.00% Top-10 accuracy, MRR of 0.9367, NDCG@10 of 0.8361, P@5 of 0.4400, P@10 of 0.2820, Recall@5 of 0.7761, and Recall@10 of 0.8811. The results show that combining complementary retrieval and legal-context signals can substantially improve precedent retrieval over the simpler baselines evaluated in this study. The system is intended as a research-support tool and does not predict judicial outcomes or replace professional legal judgment.

## 키워드

legal information retrieval, case similarity, natural language queries, explainable retrieval, legal research support

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

