---
title: "Weaving Embeddings: A Fine-Tune-Free LLM Fusion Framework for Efficient Health and Safety Text Analysis"
authors: ['Jian Chen', 'Jinbao Tian', 'Wangdong Xu', 'Wenbo Xia', 'Li Zhou']
year: 2025
venue: ""
tags: ['Biomedical Text Mining and Ontologies', 'Topic Modeling', 'Machine Learning in Healthcare']
source: raw/applied/applied_2025_Weaving_Embeddings_A_Fine_bibm66473_2025_11356911.md
---

# Weaving Embeddings: A Fine-Tune-Free LLM Fusion Framework for Efficient Health and Safety Text Analysis

**저자**: Jian Chen; Jinbao Tian; Wangdong Xu; Wenbo Xia; Li Zhou
**출처**: , Vol.None, pp.6676-6683
**발행일**: 2025-12-15
**DOI**: https://doi.org/10.1109/bibm66473.2025.11356911

## 초록 (원문)

The analysis of unstructured text, such as clinical notes and public health reports, is a fundamental challenge in biomedical and health informatics (BHI). Occupational health informatics, a vital sub-domain of BHI, relies on analyzing injury narratives to prevent workplace accidents, which constitute a significant public health burden. While Large Language Models (LLMs) offer a promising direction, their practical deployment in health-related applications is often hindered by the prohibitive computational costs of fine-tuning and the unreliability of prompt-based methods. To address these limitations, we propose an efficient, fine-tune-free, and lightweight fusion framework for robust text classification. Our framework introduces a primary-auxiliary architecture that harnesses diverse semantic embeddings from multiple off-the-shelf LLMs. By modeling the second-order interactions between these embeddings via a cooccurrence mechanism, our approach generates a powerful, composite feature representation for a simple downstream classifier. We empirically validate our framework on a public benchmark of occupational injury reports from the U.S. Occupational Safety and Health Administration (OSHA), where the framework achieves a state-of-the-art weighted-F1 score of <tex xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xlink="http://www.w3.org/1999/xlink">$\mathbf{6 8. 2 0 \%}$</tex>. Notably, our framework outperforms a purpose-built, fine-tuned LLM of the same scale while demonstrating a 4.4-fold improvement in computational efficiency. The code is publicly available at: https://github.com/nxcc-lab/LLM-Fusion-Framework.

## 키워드

Benchmark (surveying), Health informatics, Weaving, Benchmarking, eHealth, Software deployment, Representation (politics), Feature (linguistics)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

