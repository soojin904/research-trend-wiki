---
title: "Dual-BERT adversarial learning for Hausa user-generated text normalization"
authors: ['Sulaimon Adebayo Bashir', 'Abubakar Ahmad Aliero', 'Amina Gogo Tafida', 'Mukhtar Ibrahim Hussaini', 'Nur Syadhila Che Lah', 'Maged Nasser', 'Yunusa Adamu Bena']
year: 2026
venue: "Frontiers in Artificial Intelligence"
tags: ['Sentiment Analysis and Opinion Mining', 'Hate Speech and Cyberbullying Detection', 'Authorship Attribution and Profiling']
source: raw/applied/applied_2026_DualBERT_adversarial_lear_frai_2026_1905680.md
---

# Dual-BERT adversarial learning for Hausa user-generated text normalization

**저자**: Sulaimon Adebayo Bashir; Abubakar Ahmad Aliero; Amina Gogo Tafida; Mukhtar Ibrahim Hussaini; Nur Syadhila Che Lah; Maged Nasser; Yunusa Adamu Bena
**출처**: Frontiers in Artificial Intelligence, Vol.9
**발행일**: 2026-09-18
**DOI**: https://doi.org/10.3389/frai.2026.1905680

## 초록 (원문)

Text normalization (TN) is a crucial preprocessing task in Natural Language Processing (NLP) that enables the conversion of noisy, informal texts into standardized forms suitable for downstream applications, such as machine translation, speech recognition, text-to-speech systems, sentiment analysis, and information retrieval. User-Generated Content (UGC) from social media and messaging platforms often contains irregularities such as abbreviations, phonetic spellings, code-switching, and orthographic inconsistencies. These irregularities have significant implications, especially for low-resourced languages like Hausa, which have limited annotated corpora and computational resources. Existing rule-based and statistical methods struggle in their performance with Hausa text because of spelling variations, code-mixing, abbreviations, and contextual ambiguities. In contrast, neural networks like transformers require a large dataset for efficient training; however, the lack of specialized resources like a parallel corpus further worsens the inefficiency of current models in handling Hausa UGC. To address these gaps, two corpora were developed: a Hausa UGC corpus collected from Twitter and WhatsApp, and a standard Hausa corpus consisting of 27,847 sentences each. The UGC corpus was analyzed to identify Out-of-Vocabulary (OOV) words, their features, and usage patterns. A Dual-BERT Adversarial Network model was then designed and trained to map non-standard Hausa words into their canonical forms accurately. The developed model integrates dual-BERT within an adversarial learning framework, enabling it to capture both the semantic and contextual relationships between informal and standard text. One BERT processes noisy, user-generated Hausa input, while the other learns from standard Hausa sentences, allowing the system to model bidirectional correspondences between the two linguistic forms. Their representations are fused and refined through a generator-discriminator architecture, where the generator produces normalized outputs and the discriminator enforces contextual correctness by distinguishing genuine standard text from generated ones. This adversarial dual-BERT design enhances robustness, contextual awareness, and generalization, making the model highly effective for transforming inconsistent Hausa UGC into standardized text suitable for downstream NLP applications. Experimental results demonstrate that the proposed model achieved an Exact Match Accuracy of 83.99%, BLEU score of 0.7534, WER of 12.02%, and CER of 7.03%, outperforming the evaluated baseline models across all reported metrics. Qualitative analysis further shows that the model effectively normalizes abbreviations, phonetic spellings, character elongations, and many Hausa-English code-mixed expressions, while insertion and deletion errors remain comparatively more challenging. The primary contributions of this work are (i) the construction of a manually annotated parallel corpus for Hausa user-generated text normalization, (ii) the development of a Dual-BERT adversarial framework for context-aware normalization in a low-resource setting, and (iii) a comprehensive evaluation demonstrating the effectiveness of the proposed approach for improving the quality of Hausa user-generated text and supporting downstream NLP applications.

## 키워드

Hausa, Normalization (sociology), Preprocessor, Transformer, Adversarial system, Text processing

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

