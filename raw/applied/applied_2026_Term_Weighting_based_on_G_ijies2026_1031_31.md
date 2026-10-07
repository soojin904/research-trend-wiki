---
title: "Term Weighting based on Graph Model (TWGM): A Contextual and Semantic Approach to Enhancing Text Representation"
authors: ['Ade Sutedi', 'Muljono Muljono', 'Guruh Fajar Shidik', 'Heru Agus Santoso', 'R. Rizal Isnanto', 'Deshinta Arrova Dewi']
year: 2026
publication_date: 2026-09-19
venue: "International journal of intelligent engineering and systems"
volume: "19"
issue: "10"
pages: "625-642"
doi: "https://doi.org/10.22266/ijies2026.1031.31"
oa_status: "hybrid"
openalex_id: "https://openalex.org/W7213657947"
query_keyword: "text analysis"
tags: ['Topic Modeling', 'Text and Document Classification Technologies', 'Sentiment Analysis and Opinion Mining']
keywords: ['Weighting', 'Classifier (UML)', 'Robustness (evolution)', 'Graph', 'Term (time)', 'Benchmark (surveying)']
source: openalex-keyword
---

# Term Weighting based on Graph Model (TWGM): A Contextual and Semantic Approach to Enhancing Text Representation

**저자**: Ade Sutedi; Muljono Muljono; Guruh Fajar Shidik; Heru Agus Santoso; R. Rizal Isnanto; Deshinta Arrova Dewi
**출처**: International journal of intelligent engineering and systems, Vol.19 No.10, pp.625-642
**발행일**: 2026-09-19
**DOI**: https://doi.org/10.22266/ijies2026.1031.31
**수집 키워드**: text analysis

## 초록

Term weighting plays a crucial role in text representation for classification tasks.Conventional weighting methods, such as TF-IDF and its variants, primarily rely on statistical frequency information and often overlook structural relationships among terms.To address this limitation, this study proposes the Term Weighting Graph Model (TWGM), an unsupervised graph-based framework that integrates corpus-level term importance with structural information derived from word co-occurrence relationships.TWGM models terms as nodes and co-occurrences as weighted edges, extracting relation-based term importance through five graph-based weighting variants: RB-node, RB-edge, RB-node-edge, RB-strength, and RB-PR.The effectiveness of TWGM is rigorously evaluated across diverse benchmark and real-world datasets using traditional classifiers (KNN and SVM) as well as graph-based and contextual deep learning models (GCN and BERT).Performance is assessed using Micro-F1, Macro-F1, and accuracy, with stability verified via mean and standard deviation across repeated trials.The results demonstrate that the optimal graph strategy depends on classifier architecture and dataset structure.In traditional classifiers, RB-node achieves superior robustness (Micro-F1 up to 92.16%), whereas RB-edge excels in fine-grained entity classification tasks (reaching 95.49% on Help).Crucially, integrating TWGM into deep architectures yields state-of-the-art results: the RGCN-BERT + RB-node-edge variant consistently surpasses the baseline RGCN-BERT across all benchmark datasets, achieving 98.85% on R8, 94.42% on R52, 63.25% on OH, 86.97% on MR, and 88.27% on 20NG.These findings confirm that graph-derived structural information effectively complements statistical representations and contextual embeddings, offering a highly interpretable and versatile framework for text classification.

## 키워드

Weighting, Classifier (UML), Robustness (evolution), Graph, Term (time), Benchmark (surveying)

## 주제 분류 (OpenAlex Topics)

- Topic Modeling (score: 0.474)
- Text and Document Classification Technologies (score: 0.236)
- Sentiment Analysis and Opinion Mining (score: 0.120)

## 메모

