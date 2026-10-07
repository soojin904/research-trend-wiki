---
title: "Timepop a posting time aware deep model for short video popularity prediction"
authors: ['Di Wu', 'Yanfei Zhou', 'Hailong Li', 'Dou Li']
year: 2026
venue: "Discover Artificial Intelligence"
tags: ['Sentiment Analysis and Opinion Mining', 'Complex Network Analysis Techniques', 'Mental Health via Writing']
source: raw/applied/applied_2026_Timepop_a_posting_time_aw_s44163_026_02322_9.md
---

# Timepop a posting time aware deep model for short video popularity prediction

**저자**: Di Wu; Yanfei Zhou; Hailong Li; Dou Li
**출처**: Discover Artificial Intelligence, Vol.6
**발행일**: 2026-09-27
**DOI**: https://doi.org/10.1007/s44163-026-02322-9

## 초록 (원문)

SShort-video platforms have experienced explosive growth, making automated popularity prediction one of the core challenges in social media analytics and recommender systems. Existing methods predominantly focus on visual content or social network features, while systematically neglecting the temporal signal embedded in the video posting time—a signal with strong prior predictive value. To address this gap, we propose TimePop, a posting-time-aware deep learning framework for short-video popularity prediction. The core innovation of TimePop lies in a dedicated Temporal Embedding Module (TEM): multi-granularity temporal attributes of the posting moment (hour, weekday, month) are encoded into a 14-dimensional continuous vector via sinusoidal-cosinusoidal cyclic encoding, effectively preserving the circular continuity of temporal signals. Building upon this, a feature-wise gating fusion mechanism is designed to dynamically weight and fuse temporal embeddings with social features and textual features, constructing an end-to-end four-dimensional joint popularity prediction model (play count, like count, comment count, share count). On a self-collected TikTok dataset of 2200 videos from 15 creators (June 2019–February 2022), where interaction counts were collected at the time of metadata retrieval, TimePop achieves leading performance across all five evaluation metrics against seven baseline methods: compared with the best-performing baseline Transformer, MAPE decreases from 40.94 to 33.47% ( $$\downarrow $$ 7.47 percentage points), $$R^{2}$$ improves from 0.6401 to 0.7512 ( $$\uparrow $$ 0.1111), and training time (198.4 s) is lower than that of Transformer (312.8 s). Ablation experiments confirm that TEM is the most critical performance source (removing TEM causes $$R^{2}$$ $$\downarrow $$ 0.0789), and the $$R^{2}$$ gain of sinusoidal-cosinusoidal cyclic encoding over linear encoding reaches 0.0531. Stratified analysis reveals that TimePop reduces MAPE by 12.3 percentage points relative to the baseline in the high-popularity segment (play count >10 M), demonstrating the particularly strong discriminative value of temporal embedding features for predicting highly viral videos. Leave-one-creator-out cross-validation further confirms that TimePop’s advantage over the Transformer baseline is maintained across unseen creators ( $$R^2$$ : 0.681 vs. 0.587), demonstrating cross-creator generalization beyond a single random split. Using only lightweight metadata as input, this study provides a practically meaningful time-aware prediction paradigm for content creator posting-time analysis, platform metadata-based recommendation support, and predictive advertising placement.

## 키워드

Popularity, Metadata, Baseline (sea), Social media, Deep learning, Predictive modelling, Embedding, Analytics

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

