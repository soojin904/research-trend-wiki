---
title: "Detecting Basic Values in A Noisy Russian Social Media Text Data: A Multi-Stage Classification Framework"
authors: ['Maria Milkova', 'Maksim Rudnev']
year: 2026
venue: "ArXiv.org"
tags: ['Sentiment Analysis and Opinion Mining', 'Computational and Text Analysis Methods', 'Misinformation and Its Impacts']
source: raw/applied/applied_2026_Detecting_Basic_Values_in_nodoi.md
---

# Detecting Basic Values in A Noisy Russian Social Media Text Data: A Multi-Stage Classification Framework

**저자**: Maria Milkova; Maksim Rudnev
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-03-19
**DOI**: 

## 초록 (원문)

This study presents a multi-stage classification framework for detecting human values in noisy Russian language social media, validated on a random sample of 7.5 million public text posts. Drawing on Schwartz's theory of basic human values, we design a multi-stage pipeline that includes spam and nonpersonal content filtering, targeted selection of value relevant and politically relevant posts, LLM based annotation, and multi-label classification. Particular attention is given to verifying the quality of LLM annotations and model predictions against human experts. We treat human expert annotations not as ground truth but as an interpretative benchmark with its own uncertainty. To account for annotation subjectivity, we aggregate multiple LLM generated judgments into soft labels that reflect varying levels of agreement. These labels are then used to train transformer based models capable of predicting the probability of each of the ten basic values. The best performing model, XLM RoBERTa large, achieves an F1 macro of 0.83 and an F1 of 0.71 on held out test data. By treating value detection as a multi perspective interpretive task, where expert labels, GPT annotations, and model predictions represent coherent but not identical readings of the same texts, we show that the model generally aligns with human judgments but systematically overestimates the Openness to Change value domain. Empirically, the study reveals distinct patterns of value expression and their co-occurrence in Russian social networks, contributing to a broader research agenda on cultural variation, communicative framing, and value based interpretation in digital environments. All models are released publicly.

## 키워드

Value (mathematics), Social media, Selection (genetic algorithm), Perspective (graphical), Ground truth, Pipeline (software), Benchmark (surveying), Quality (philosophy)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

