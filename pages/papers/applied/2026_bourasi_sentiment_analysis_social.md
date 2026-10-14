---
title: "Sentiment Analysis of Social Media Posts using FastText Embedding and a Hybrid BiLSTM-Attention-CNN Deep Learning Architecture"
authors: ['Reeta Bourasi', 'Sakshi Rai']
year: 2026
venue: "International Journal of Innovations in Science Engineering and Management."
tags: ['Sentiment Analysis and Opinion Mining', 'Topic Modeling', 'Hate Speech and Cyberbullying Detection']
source: raw/applied/applied_2026_Sentiment_Analysis_of_Soc_ijisem_2026v5i497_112.md
---

# Sentiment Analysis of Social Media Posts using FastText Embedding and a Hybrid BiLSTM-Attention-CNN Deep Learning Architecture

**저자**: Reeta Bourasi; Sakshi Rai
**출처**: International Journal of Innovations in Science Engineering and Management., Vol.None, pp.97-112
**발행일**: 2026-10-09
**DOI**: https://doi.org/10.69968/ijisem.2026v5i497-112

## 초록 (원문)

Looking into how people feel about things online now matters a lot when tracking what crowds think, how brands are seen, or spotting shifts in user actions across large groups. Most current methods lean heavily on models like BERT which are powerful at sorting sentiments yet slow to train and hungry for computing power. Instead of following that path, this study presents a simpler mix; it combines FastText with a BiLSTM layer that sees context both ways, adds a slim attention component that highlights key words, then feeds results into a CNN for final output. It grabs small word fragments with the help of FastText, tracks order in sequences using BiLSTM, uses attention to weigh meaningful parts more, while the CNN pinpoints sharp, useful patterns which others might overlook. Testing took place on two open Twitter sentiment datasets. One holds 74,682 labeled entries split into four categories: Positive, Negative, Neutral, Irrelevant. The other includes around 162,000 instances grouped under three labels: Positive, Negative, Neutral. Instead of relying on heavy transformer designs, the approach here keeps computation leaner but still matches standard accuracy levels. Performance stayed strong using a mix of BiLSTM-Attention for features and CNN for final predictions. Metrics like precision, recall, F1, accuracy, along with confusion matrices, confirmed consistency across tests. Both TensorFlowand PyTorch were used to build the system, allowing insights into differences between coding environments. Results point toward a balanced option that works well without demanding excessive resources for analyzing emotions in vast streams of social network posts.

## 키워드

sentiment analysis, social media posts, Twitter, FastText embeddings, BiLSTM, attention mechanism, convolutional neural networks, hybrid deep learning model

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

