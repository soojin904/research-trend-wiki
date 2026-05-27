---
title: "Unsupervised Cross-Lingual Part-of-Speech Tagging with Monolingual Corpora Only"
authors: ['Jianyu Zheng']
year: 2026
publication_date: 2026-02-10
venue: "ArXiv.org"
volume: "None"
issue: "None"
pages: ""
doi: ""
oa_status: "green"
openalex_id: "https://openalex.org/W7128648535"
query_keyword: "text analysis"
tags: ['Natural Language Processing Techniques', 'Topic Modeling', 'Speech Recognition and Synthesis']
keywords: ['Projection (relational algebra)', 'Sentence', 'Word (group theory)', 'Baseline (sea)', 'Parallel corpora', 'Language model', 'Natural language']
source: openalex-keyword
---

# Unsupervised Cross-Lingual Part-of-Speech Tagging with Monolingual Corpora Only

**저자**: Jianyu Zheng
**출처**: ArXiv.org
**발행일**: 2026-02-10
**DOI**: 
**수집 키워드**: text analysis

## 초록

Due to the scarcity of part-of-speech annotated data, existing studies on low-resource languages typically adopt unsupervised approaches for POS tagging. Among these, POS tag projection with word alignment method transfers POS tags from a high-resource source language to a low-resource target language based on parallel corpora, making it particularly suitable for low-resource language settings. However, this approach relies heavily on parallel corpora, which are often unavailable for many low-resource languages. To overcome this limitation, we propose a fully unsupervised cross-lingual part-of-speech(POS) tagging framework that relies solely on monolingual corpora by leveraging unsupervised neural machine translation(UNMT) system. This UNMT system first translates sentences from a high-resource language into a low-resource one, thereby constructing pseudo-parallel sentence pairs. Then, we train a POS tagger for the target language following the standard projection procedure based on word alignments. Moreover, we propose a multi-source projection technique to calibrate the projected POS tags on the target side, enhancing to train a more effective POS tagger. We evaluate our framework on 28 language pairs, covering four source languages (English, German, Spanish and French) and seven target languages (Afrikaans, Basque, Finnis, Indonesian, Lithuanian, Portuguese and Turkish). Experimental results show that our method can achieve performance comparable to the baseline cross-lingual POS tagger with parallel sentence pairs, and even exceeds it for certain target languages. Furthermore, our proposed multi-source projection technique further boosts performance, yielding an average improvement of 1.3% over previous methods.

## 키워드

Projection (relational algebra), Sentence, Word (group theory), Baseline (sea), Parallel corpora, Language model, Natural language

## 주제 분류 (OpenAlex Topics)

- Natural Language Processing Techniques (score: 0.959)
- Topic Modeling (score: 0.006)
- Speech Recognition and Synthesis (score: 0.003)

## 메모

