---
title: "Hybrid Model for Authorship attribution of English-language texts"
authors: ['В.М. Бадзь', 'В.М. Теслюк']
year: 2026
publication_date: 2026-03-28
venue: "COMPUTER-INTEGRATED TECHNOLOGIES EDUCATION SCIENCE PRODUCTION"
volume: "None"
issue: "62"
pages: "118-123"
doi: "https://doi.org/10.36910/6775-2524-0560-2026-62-13"
oa_status: "diamond"
openalex_id: "https://openalex.org/W7144380070"
query_keyword: "text analysis"
tags: ['Authorship Attribution and Profiling', 'Hate Speech and Cyberbullying Detection', 'Topic Modeling']
keywords: ['Discriminative model', 'Robustness (evolution)', 'Stylometry', 'Punctuation', 'Feature learning', 'Natural language understanding', 'Computational linguistics', 'Authorship attribution']
source: openalex-keyword
---

# Hybrid Model for Authorship attribution of English-language texts

**저자**: В.М. Бадзь; В.М. Теслюк
**출처**: COMPUTER-INTEGRATED TECHNOLOGIES EDUCATION SCIENCE PRODUCTION No.62, pp.118-123
**발행일**: 2026-03-28
**DOI**: https://doi.org/10.36910/6775-2524-0560-2026-62-13
**수집 키워드**: text analysis

## 초록

Authorship attribution is a critical task in computational linguistics, digital forensics, and information security, particularly in the context of rapidly growing digital textual data. Traditional stylometric approaches rely on handcrafted linguistic features such as lexical richness, syntactic patterns, and punctuation statistics. Although these methods are interpretable and computationally efficient, they often fail to capture deeper semantic and contextual properties of texts. Transformer-based models, including BERT and RoBERTa, have demonstrated significant improvements in natural language processing tasks due to their ability to model contextual dependencies; however, they often produce embeddings that are insufficiently discriminative for fine-grained authorship attribution, especially in low-resource and cross-domain scenarios. This paper presents a hybrid model for authorship attribution of English-language texts that integrates RoBERTa embeddings, stylometric features, and supervised contrastive learning. The developed architecture constructs unified authorial representations in a latent feature space, where contrastive learning enforces intra-author compactness and inter-author separability. Stylometric features complement transformer-based embeddings by capturing stylistic and structural characteristics of texts, which enhances robustness and interpretability. The fusion of heterogeneous features is performed through a projection network that maps the combined representation into a discriminative latent space. Experimental evaluation was conducted on synthetic benchmark datasets simulating multiple authors and genres. The created hybrid model significantly outperformed baseline models based on stylometry and transformer fine-tuning. The hybrid model achieved an accuracy of 0.91 and a macro-averaged F1-score of 0.90, demonstrating improved robustness under limited training data conditions. The results confirm that contrastive learning substantially improves the separability of author classes in the embedding space. The developed model can be applied in plagiarism detection systems, forensic linguistic analysis, and digital authorship verification in information systems.

## 키워드

Discriminative model, Robustness (evolution), Stylometry, Punctuation, Feature learning, Natural language understanding, Computational linguistics, Authorship attribution, Representation (politics)

## 주제 분류 (OpenAlex Topics)

- Authorship Attribution and Profiling (score: 0.994)
- Hate Speech and Cyberbullying Detection (score: 0.001)
- Topic Modeling (score: 0.001)

## 메모

