---
title: "Integrating sentiment and contextual information for suicide ideation detection in online social networks: a BERT-BiTCN-sentiment hybrid approach"
authors: ['Fatos Orgun', 'Ümit Can']
year: 2026
venue: "PeerJ Computer Science"
tags: ['Mental Health via Writing', 'Sentiment Analysis and Opinion Mining', 'Hate Speech and Cyberbullying Detection']
source: raw/applied/applied_2026_Integrating_sentiment_and_peerj_cs_4118.md
---

# Integrating sentiment and contextual information for suicide ideation detection in online social networks: a BERT-BiTCN-sentiment hybrid approach

**저자**: Fatos Orgun; Ümit Can
**출처**: PeerJ Computer Science, Vol.12, pp.e4118-e4118
**발행일**: 2026-10-09
**DOI**: https://doi.org/10.7717/peerj-cs.4118

## 초록 (원문)

Background Worldwide, suicide ranks as one of the primary causes of mortality. Taking action and implementing measures to address suicidal thoughts is essential for the well-being of public health. Today, methodologies developed by artificial intelligence serve important functions in the medical field, both as decision-making systems and as sources of information. This observation highlights the increasing integration of machine learning and deep learning into psychiatry, complementing traditional medical practices. Digital social platforms can significantly contribute to the early diagnosis of suicidal tendencies and the implementation of preventive measures. Individuals increasingly express their thoughts and feelings on platforms such as Twitter, Facebook, Reddit, and Instagram. It has been observed that many individuals struggling with severe psychological disorders express their feelings and reactions on social media platforms. This research aims to early detect suicidal ideation by developing a hybrid model that automatically detects suicide-related posts on online social networks (OSNs). Method First, three datasets were combined to create a new dataset of 254,198 samples. Subsequently, data preprocessing techniques were implemented to diminish the dataset’s size and mitigate noise in the data. Additionally, word embedding techniques, including Term Frequency Inverse Document Frequency (TF-IDF), N-Gram-TF-IDF, and Bidirectional Encoder Representations from Transformers (BERT), were employed during the feature engineering phase. At the same time, the compound sentiment score for each post was computed for integration into the hybrid model. This study developed the BERT-Bidirectional Temporal Convolutional Network (BiTCN)-Sentiment (BERT-BiTCN-Sentiment) model by integrating BERT’s capacity to extract contextual meaning from textual data with BiTCN’s proficiency in capturing bidirectional relationships in sequential data. The BERT-BiTCN-Sentiment hybrid model proposed in this study was used for the first time to detect suicidal ideation in social networks. Results The experimental studies demonstrated that the BERT-BiTCN-Sentiment model attained superior performance, achieving an accuracy of 95.45%, precision of 95.45%, recall of 95.45%, and an F-score of 95.45%. The Multilingual BERT model achieved 94.88% accuracy, precision, recall, and F1-score, ranking second among the models. Moreover, the A Lite BERT (ALBERT), MentalBERT, BERT-Bidirectional Long Short-Term Memory (BiLSTM), BERT-Convolutional Neural Network (CNN), and BERT models attained comparable results. The TF-IDF-LightGBM model proved to be the most proficient among the machine learning models, attaining 90.60% in accuracy, precision, recall, and F-score. This study culminated in the development of a successful hybrid model capable of early detection of posts indicative of suicidal tendencies among users on online social networks.

## 키워드

suicide ideation detection, social media, social networking sites, sentiment analysis, BERT, bidirectional temporal convolutional network, hybrid model, mental health

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

