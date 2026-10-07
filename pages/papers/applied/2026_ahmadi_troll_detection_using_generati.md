---
title: "Troll detection using generative adversarial network (GAN) based on social network features"
authors: ['Alireza Ahmadi', 'Mohammad Khansari']
year: 2026
venue: "Scientific Reports"
tags: ['Misinformation and Its Impacts', 'Hate Speech and Cyberbullying Detection', 'Spam and Phishing Detection']
source: raw/applied/applied_2026_Troll_detection_using_gen_s41598_026_72755_w.md
---

# Troll detection using generative adversarial network (GAN) based on social network features

**저자**: Alireza Ahmadi; Mohammad Khansari
**출처**: Scientific Reports, Vol.None
**발행일**: 2026-09-27
**DOI**: https://doi.org/10.1038/s41598-026-72755-w

## 초록 (원문)

Abstract A troll is an online user who deliberately disrupts discussions, spreads misleading or provocative messages, and incites conflict or disorder in digital interactions. Troll detection based on behavior change is one of the new methods of research in this field. The feedback-oriented nature of GANs, coupled with the relational insights from social network analysis, allows for effective simulation and identification of behavioral changes, resulting in improved detection performance across diverse trolling strategies. In this paper, we utilize Generative Adversarial Network (GAN) as a new semi-supervised method from the deep learning approach to detect troll behavior changes. The suggested approach comprises three elements: a Generator, a Discriminator, and a Classifier. These components collaborate not only to classify troll opinions but also to produce samples closely resembling the training dataset. This Method operates by leveraging two neural networks engaged in a min-max adversarial framework. In this process, the Discriminator is responsible for distinguishing between real and synthetic samples, while the Generator aims to create realistic fake samples to deceive the Discriminator. A key aspect of this method is the integration of the Generator and Classifier through an LSTM layer, which serves as a shared channel between them. The proposed approach is compared with LSTM and logistic regression on two Twitter troll datasets, including a small-scale labeled dataset of 14,940 instances and a large-scale corpus comprising approximately three million Russian troll-related tweets. Accuracy and F1-score are used for performance evaluation. The results indicate that the proposed TrollGAN model achieves higher accuracy and more robust generalization than baseline methods, while maintaining stable discriminative behavior under increased data scale and behavioral complexity. These findings highlight the suitability of adversarial learning for large-scale and dynamic troll detection tasks.

## 키워드

Discriminator, Adversarial system, Classifier (UML), Generator (circuit theory), Key (lock), Generative grammar, Generalization, Artificial neural network

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

