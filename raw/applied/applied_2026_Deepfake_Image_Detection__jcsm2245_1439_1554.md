---
title: "Deepfake Image Detection Using Squeeze-and-Excitation Attention and Adaptive Threshold Optimization"
authors: ['Chaoran Li']
year: 2026
publication_date: 2026-10-02
venue: "Journal of Cyber Security and Mobility"
volume: "None"
issue: "None"
pages: ""
doi: "https://doi.org/10.13052/jcsm2245-1439.1554"
oa_status: "diamond"
openalex_id: "https://openalex.org/W7215936904"
query_keyword: "social network"
tags: ['Digital Media Forensic Detection', 'Misinformation and Its Impacts', 'Generative Adversarial Networks and Image Synthesis']
keywords: ['deepfake detection', 'squeeze-and-excitation', 'adaptive decision threshold', 'identity leakage', 'FaceForensics++', 'social media misinformation', 'distribution shift robustness', 'ResNet-18']
source: openalex-keyword
---

# Deepfake Image Detection Using Squeeze-and-Excitation Attention and Adaptive Threshold Optimization

**저자**: Chaoran Li
**출처**: Journal of Cyber Security and Mobility
**발행일**: 2026-10-02
**DOI**: https://doi.org/10.13052/jcsm2245-1439.1554
**수집 키워드**: social network

## 초록

Artificial intelligence-generated content (AIGC) has significantly improved the realism of manipulated facial images and videos, creating serious risks for social-network misinformation, content security, and digital trust. This study focuses on visual deepfake image detection rather than multimodal misinformation detection. Existing convolutional neural network (CNN)-based deepfake detectors commonly rely on a fixed decision threshold of 0.5, which may be unstable when facial images are affected by compression, cropping, noise, and distribution shifts in practical social-media environments. To improve detection reliability, this paper proposes a lightweight deepfake image detection framework that integrates a CNN backbone, a Squeeze-and-Excitation (SE) attention module, and an adaptive threshold optimization strategy. The key novelty of this work is not conventional threshold tuning alone, but a lightweight detection framework that jointly combines SE-based channel-wise feature recalibration, F1-score-driven adaptive threshold optimization, and leakage-aware group-level evaluation. Compared with post-hoc threshold tuning or calibration methods that mainly adjust the output boundary after training, the proposed framework improves both forgery-sensitive feature representation and the final classification decision mechanism. Specifically, the SE module enhances forgery-related feature representation through channel-wise feature recalibration, while the adaptive threshold is selected according to the F1-score, which is the harmonic mean of precision and recall. A group-level data split is also adopted to ensure that frames from the same video are not shared across the training, validation, and test sets, thereby reducing identity leakage. Experiments are conducted on a FaceForensics++-derived dataset using multiple CNN backbones and five-fold cross-validation. The evaluation metrics include accuracy, F1-score, the area under the receiver operating characteristic curve (ROC-AUC), and the area under the precision-recall curve (PR-AUC). The results show that threshold optimization improves the ResNet18 baseline accuracy from 0.8835 ± 0.0186 to 0.9016 ± 0.0151 and the F1-score from 0.8773 ± 0.0253 to 0.9042 ± 0.0138. Among the tested backbones, ResNet50 achieves the best cross-validation performance, with an accuracy of 0.9061 ± 0.0161 and a ROC-AUC of 0.9680 ± 0.0075. Under the strict group-level test setting, the proposed framework achieves 0.9960 accuracy and 0.9959 F1-score on the constructed test set. Compared with more complex detection pipelines. The proposed method is simple, computationally practical, and easy to integrate into common CNN-based deepfake detectors. Therefore, this work provides a practical visual security detection approach for social-media content verification and cyber-security applications.

## 키워드

deepfake detection, squeeze-and-excitation, adaptive decision threshold, identity leakage, FaceForensics++, social media misinformation, distribution shift robustness, ResNet-18, ResNet50, deepfakes

## 주제 분류 (OpenAlex Topics)

- Digital Media Forensic Detection (score: 1.000)
- Misinformation and Its Impacts (score: 0.000)
- Generative Adversarial Networks and Image Synthesis (score: 0.000)

## 메모

