---
title: "MLCL: LVLM-guided multi-level contrastive learning for fake news detection"
authors: ['Jun Li', 'L. Yan', 'Qingxue Liu', 'Suli Zhang']
year: 2026
publication_date: 2026-10-01
venue: "Scientific Reports"
volume: "None"
issue: "None"
pages: ""
doi: "https://doi.org/10.1038/s41598-026-73360-7"
oa_status: "gold"
openalex_id: "https://openalex.org/W7215038639"
query_keyword: "social network"
tags: ['Misinformation and Its Impacts', 'Multimodal Machine Learning Applications', 'Digital Media Forensic Detection']
keywords: ['fake news detection', 'disinformation', 'multimodal contrastive learning', 'large vision-language models', 'cross-modal alignment', 'InfoNCE loss', 'triplet loss', 'multimodal fusion']
source: openalex-keyword
---

# MLCL: LVLM-guided multi-level contrastive learning for fake news detection

**저자**: Jun Li; L. Yan; Qingxue Liu; Suli Zhang
**출처**: Scientific Reports
**발행일**: 2026-10-01
**DOI**: https://doi.org/10.1038/s41598-026-73360-7
**수집 키워드**: social network

## 초록

Abstract The widespread dissemination of multi-modal disinformation on social media platforms poses a serious threat to public safety and social stability, elevating the need for automated detection of such content. Although existing studies have started to incorporate multimodal data, effectively modeling cross-modal interactions remains difficult, often leading to insufficient mining of information within individual modalities. To address this issue, this paper proposes a novel LVLM-Guided multi-level contrastive learning network (MLCL). Within the textual modality, BERT and CLIP encoders extract features at varying granularities, while ResNet and CLIP encoders capture visual representations. Additionally, a Large Vision-Language Model is leveraged to derive text-based representations that reflect both local details and global contexts from images. We further introduce a multi-level alignment strategy: inside each modality, a normalized InfoNCE loss aligns features from the two encoders to reduce redundancy. Before cross-modal fusion, we jointly align the three modality-level features using both InfoNCE loss and batch-hard triplet loss, thereby explicitly modeling their consistency and relative distance. A modality-wise attention module is also incorporated to adaptively reweight and aggregate features. Experiments on two real-world datasets show that our approach outperforms existing methods, achieving overall accuracy improvements of 2.2% on Weibo and 1.5% on Gossipcop. The source code is publicly available at https://github.com/Ylh-s/MLCL .

## 키워드

fake news detection, disinformation, multimodal contrastive learning, large vision-language models, cross-modal alignment, InfoNCE loss, triplet loss, multimodal fusion, social media

## 주제 분류 (OpenAlex Topics)

- Misinformation and Its Impacts (score: 0.996)
- Multimodal Machine Learning Applications (score: 0.002)
- Digital Media Forensic Detection (score: 0.001)

## 메모

