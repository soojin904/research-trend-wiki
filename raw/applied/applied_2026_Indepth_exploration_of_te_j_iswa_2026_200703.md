---
title: "In-depth exploration of text similarity calculation based on improved VSM and DeepSeek"
authors: ['Huifang Wu', 'Meng Guo', '郭庆琳']
year: 2026
publication_date: 2026-07-09
venue: "Intelligent Systems with Applications"
volume: "31"
issue: "None"
pages: "200703-200703"
doi: "https://doi.org/10.1016/j.iswa.2026.200703"
oa_status: "gold"
openalex_id: "https://openalex.org/W7167823659"
query_keyword: "text analysis"
tags: ['Topic Modeling', 'Big Data and Digital Economy', 'Advanced Text Analysis Techniques']
keywords: ['Similarity (geometry)', 'Pattern recognition (psychology)', 'Sequence (biology)', 'Identification (biology)', 'Set (abstract data type)']
source: openalex-keyword
---

# In-depth exploration of text similarity calculation based on improved VSM and DeepSeek

**저자**: Huifang Wu; Meng Guo; 郭庆琳
**출처**: Intelligent Systems with Applications, Vol.31, pp.200703-200703
**발행일**: 2026-07-09
**DOI**: https://doi.org/10.1016/j.iswa.2026.200703
**수집 키워드**: text analysis

## 초록

With the explosive growth of big data texts, document similarity calculation serves as a core supporting technology for information retrieval, plagiarism detection and intelligent recommendation. Traditional Vector Space Model (VSM) features ultra-high computing efficiency but suffers severe semantic comprehension defects; existing large language models represented by DeepSeek possess powerful deep semantic capture capacity yet are plagued by excessive computational overhead, and current research fails to organically balance semantic accuracy and inference speed. To address this critical contradiction, this paper proposes a novel dual-branch text similarity calculation fusion framework integrating improved VSM and DeepSeek MoE large model, which is the first to realize parallel extraction of statistical word frequency features and deep contextual semantic features for long professional texts. Firstly, an optimized TF-IDF feature weighting mechanism based on feature selection weight transfer is designed to strengthen the domain term discrimination ability of traditional VSM. Secondly, we adopt DeepSeek’s sparse attention MoE architecture to extract multi-granularity semantic vectors and solve the long text truncation limitation of classic Transformer models. Finally, a document-length-aware dynamic weight fusion strategy is constructed to adaptively balance the contribution of statistical features and deep semantic features, breaking the fixed-weight fusion bottleneck of prior hybrid models. We conduct comprehensive validation on medical, legal and technical report datasets. Compared with the pure DeepSeek baseline model, our fusion method boosts accuracy by 8% and recall by 14% while retaining lightweight inference efficiency; against state-of-the-art Sentence-BERT, our model achieves 2–3% higher F1 scores across all test domains, especially showing dominant advantages in processing ultra-long professional documents. This work delivers an innovative balanced technical paradigm for text similarity computation, and provides solid theoretical support and practical engineering solutions for multi-domain intelligent text analysis.

## 키워드

Similarity (geometry), Pattern recognition (psychology), Sequence (biology), Identification (biology), Set (abstract data type)

## 주제 분류 (OpenAlex Topics)

- Topic Modeling (score: 0.072)
- Big Data and Digital Economy (score: 0.058)
- Advanced Text Analysis Techniques (score: 0.040)

## 메모

