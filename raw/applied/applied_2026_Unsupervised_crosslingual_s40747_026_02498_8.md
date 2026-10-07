---
title: "Unsupervised cross-lingual part-of-speech tagging with monolingual corpora only"
authors: ['Jianyu Zheng']
year: 2026
publication_date: 2026-09-09
venue: "Complex & Intelligent Systems"
volume: "None"
issue: "None"
pages: ""
doi: "https://doi.org/10.1007/s40747-026-02498-8"
oa_status: "gold"
openalex_id: "https://openalex.org/W7128631210"
query_keyword: "text analysis"
tags: ['Natural Language Processing Techniques', 'Topic Modeling', 'Speech Recognition and Synthesis']
keywords: ['Projection (relational algebra)', 'Sentence', 'Word (group theory)', 'Baseline (sea)', 'Parallel corpora', 'Language model', 'Natural language']
source: openalex-keyword
---

# Unsupervised cross-lingual part-of-speech tagging with monolingual corpora only

**저자**: Jianyu Zheng
**출처**: Complex & Intelligent Systems
**발행일**: 2026-09-09
**DOI**: https://doi.org/10.1007/s40747-026-02498-8
**수집 키워드**: text analysis

## 초록

Due to the scarcity of part-of-speech (POS) annotated data for low-resource languages, existing studies have predominantly relied on unsupervised methods. Among these methods, annotation projection transfers POS tags from a high-resource source language to a low-resource target language through word alignments derived from parallel corpora, making it particularly suitable for low-resource scenarios. However, its effectiveness depends heavily on the availability of parallel corpora, which remain scarce or entirely unavailable for many low-resource languages. To address this limitation, we propose a fully unsupervised cross-lingual POS tagging framework that relies solely on monolingual corpora and leverages an unsupervised neural machine translation (UNMT) system. Specifically, the UNMT system translates sentences from a high-resource language into a low-resource language to construct pseudo-parallel sentence pairs. A target language POS tagger is then trained based on the standard annotation projection procedure. Moreover, we introduce a multi-source projection technique to calibrate the POS tags projected on the target side, thereby improving the quality of the annotations used to train the target language POS tagger. We evaluate the proposed framework on 28 language pairs, covering four source languages (English, German, Spanish and French) and seven target languages (Afrikaans, Basque, Finnish, Indonesian, Lithuanian, Portuguese and Turkish). Experimental results show that our method achieves performance comparable to that of a baseline cross-lingual POS tagger trained on genuine parallel sentence pairs and even outperforms it for several target languages. Furthermore, the proposed multi-source projection technique further improves tagging performance, yielding an average gain of 1.3% over previous methods.

## 키워드

Projection (relational algebra), Sentence, Word (group theory), Baseline (sea), Parallel corpora, Language model, Natural language

## 주제 분류 (OpenAlex Topics)

- Natural Language Processing Techniques (score: 0.959)
- Topic Modeling (score: 0.006)
- Speech Recognition and Synthesis (score: 0.003)

## 메모

