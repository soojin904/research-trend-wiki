---
title: "Text–relation joint modeling improves the robustness of Chinese social bot detection against paraphrasing attacks"
authors: ['Shuaifeng Guo', 'Yunqian Zhou']
year: 2026
publication_date: 2026-10-01
venue: "Scientific Reports"
volume: "16"
issue: "1"
pages: ""
doi: "https://doi.org/10.1038/s41598-026-68571-x"
oa_status: "gold"
openalex_id: "https://openalex.org/W7215068288"
query_keyword: "social network"
tags: ['Spam and Phishing Detection', 'Adversarial Robustness in Machine Learning', 'Misinformation and Its Impacts']
keywords: ['social bot detection', 'paraphrasing attacks', 'adversarial robustness', 'heterogeneous graph attention network', 'MacBERT', 'fast gradient method', 'lexical substitution', 'Weibo']
source: openalex-keyword
---

# Text–relation joint modeling improves the robustness of Chinese social bot detection against paraphrasing attacks

**저자**: Shuaifeng Guo; Yunqian Zhou
**출처**: Scientific Reports, Vol.16 No.1
**발행일**: 2026-10-01
**DOI**: https://doi.org/10.1038/s41598-026-68571-x
**수집 키워드**: social network

## 초록

Generative language models have made paraphrasing a low-cost and practical evasion strategy against social bot detectors, especially on Chinese platforms where textual content is a major detection signal. We introduce TRJD-AT, a text-relation joint framework that combines a Chinese MacBERT encoder, a two-layer heterogeneous graph attention network over user-post publication and user-user follow relations, a lightweight gated fusion module, and Fast Gradient Method (FGM) training on input embeddings. We further define a three-tier paraphrasing protocol - lexical substitution, sentence-level rewriting, and benign-token insertion - with explicit attack budgets and automatic semantic-preservation constraints, while separating post-level attack construction from account-level evaluation. On the Chinese Weibo Social Bot dataset, TRJD-AT obtains a clean macro-F1 of 0.891. Under the default Tier 2 condition (semantic-similarity threshold 0.80), it obtains a macro-F1 of 0.835, corresponding to a 5.6-percentage-point reduction, whereas the MacBERT + MLP text-only baseline obtains 0.733, corresponding to a 13.4-point reduction. Clean performance and adversarial degradation are reported as distinct quantities. Ablation results indicate that the observed robustness is mainly associated with relational modeling; FGM improves clean performance in this setting but does not provide an independent gain in attacked macro-F1. A density-based analysis further identifies reduced relational benefit for accounts with sparse interaction histories.

## 키워드

social bot detection, paraphrasing attacks, adversarial robustness, heterogeneous graph attention network, MacBERT, fast gradient method, lexical substitution, Weibo, Chinese social media

## 주제 분류 (OpenAlex Topics)

- Spam and Phishing Detection (score: 0.718)
- Adversarial Robustness in Machine Learning (score: 0.240)
- Misinformation and Its Impacts (score: 0.028)

## 메모

