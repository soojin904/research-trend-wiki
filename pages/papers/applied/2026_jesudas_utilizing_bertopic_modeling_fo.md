---
title: "Utilizing BERTopic modeling for concept discovery in the domain of gerotranscendence and solitude"
authors: ['B. Damayanthi Jesudas', 'Finn Wilson', 'Rachel A. Mavrovich', 'Sean Kindya', 'Feng-Yu Yeh', 'Sam Smith', 'Jeremy Ravenel', 'Jie Zheng', 'Yongqun Oliver He', 'Hollen N. Reischer', 'Julie C. Bowker', 'John Beverley', 'William D. Duncan']
year: 2026
venue: "Journal of Biomedical Semantics"
tags: ['Biomedical Text Mining and Ontologies', 'Computational and Text Analysis Methods', 'Mental Health via Writing']
source: raw/applied/applied_2026_Utilizing_BERTopic_modeli_s13326_026_00348_7.md
---

# Utilizing BERTopic modeling for concept discovery in the domain of gerotranscendence and solitude

**저자**: B. Damayanthi Jesudas; Finn Wilson; Rachel A. Mavrovich; Sean Kindya; Feng-Yu Yeh; Sam Smith; Jeremy Ravenel; Jie Zheng; Yongqun Oliver He; Hollen N. Reischer; Julie C. Bowker; John Beverley; William D. Duncan
**출처**: Journal of Biomedical Semantics, Vol.17
**발행일**: 2026-09-01
**DOI**: https://doi.org/10.1186/s13326-026-00348-7

## 초록 (원문)

BACKGROUND: Ontology development is a complex, iterative process that traditionally requires extensive collaboration between ontology developers and subject matter experts. While effective, this manual approach is time-consuming, labor-intensive, and prone to cognitive bias. To streamline early-stage ontology development and uncover concepts that might be overlooked through manual review alone, we applied automated topic modeling with BERTopic to extract topics, keywords, topic labels, and summaries from The Handbook of Solitude: Psychological Perspectives on Social Isolation, Social Withdrawal, and Being Alone and Gerotranscendence: A Developmental Theory of Positive Aging. The extracted topic labels after review were used as candidate concepts for the Promoting Healthy Aging through Semantic Enrichment of Solitude Research (PHASES) Ontology. METHODS: We implemented and compared two BERTopic pipelines: (1) the default pipeline and (2) a custom preprocessing pipeline incorporating part-of-speech filtering and n-gram tuning. The pipeline is customized to flexibly extract any specified number of topics and keywords based on user-defined parameters. To compare and merge topic modeling outputs across solitude and gerotranscendence, we used semantic embeddings of topic labels, keywords, and summaries from the custom pipeline. Cosine similarity identified semantically matched topic pairs above a set threshold, enabling categorization and integration into a merged conceptual framework that bridges both domains. RESULTS: From the solitude corpus, BERTopic generated 244 initial topics, which, after SMEs review, were refined to 32 high-quality topics with the custom pipeline and 46 with the default pipeline. For the gerotranscendence corpus, the pipeline produced 172 initial topics, refined to 33 with the custom pipeline and 32 with the default pipeline. Across both corpora, BERTopic contributed 90 ontology terms, 52 from the solitude corpus and 38 from the gerotranscendence corpus. Visual evaluations, including keyword score bar charts, hierarchical clustering dendrograms, and BART-generated summaries, revealed that the custom pipeline produced more fine-grained, domain-specific topics, while the default pipeline offered broader thematic coverage and clearer labels. Certain theory-laden concepts, however, required interpretive input from SMEs. CONCLUSIONS: BERTopic provided an efficient, semi-automated approach for identifying candidate ontology terms from domain literature, supporting both breadth and specificity in concept capture. The topics produced by BERTopic modeling uncover underlying latent concepts, serving as a link between raw text data and structured ontology classes. By facilitating the formation of the hierarchical relationships, it exposes a layered semantic structure that is essential for ontology development. Further, integrating semantic similarity analysis across thematic domains revealed conceptual intersections and overlaps, enhancing the semantic foundation of the PHASES Ontology and offering a replicable method for cross-domain ontology development.

## 키워드

BERTopic, topic modeling, ontology construction, gerotranscendence, solitude, social isolation, social withdrawal, semantic embeddings

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]
- [[pages/methods/semantic_network_analysis|의미연결망]]

## 메모

