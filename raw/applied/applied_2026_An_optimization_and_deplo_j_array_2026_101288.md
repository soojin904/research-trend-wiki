---
title: "An optimization and deployment framework for efficient BERT-based paraphrase detection"
authors: ['Bonthu Chandra Praveen', 'K. Sivasankaran']
year: 2026
publication_date: 2026-09-01
venue: "Array"
volume: "None"
issue: "None"
pages: "101288-101288"
doi: "https://doi.org/10.1016/j.array.2026.101288"
oa_status: "gold"
openalex_id: "https://openalex.org/W7214789138"
query_keyword: "text analysis"
tags: ['Natural Language Processing Techniques', 'Topic Modeling', 'Speech Recognition and Synthesis']
keywords: []
source: openalex-keyword
---

# An optimization and deployment framework for efficient BERT-based paraphrase detection

**저자**: Bonthu Chandra Praveen; K. Sivasankaran
**출처**: Array, pp.101288-101288
**발행일**: 2026-09-01
**DOI**: https://doi.org/10.1016/j.array.2026.101288
**수집 키워드**: text analysis

## 초록

Paraphrase identification is an important application in Natural Language Processing (NLP) and plays a significant role in large-scale and real-time text analysis. Although transformer-based models such as Bidirectional Encoder Representations from Transformers (BERT) achieve high accuracy, for these applications their computational complexity and memory requirements face challenges for deploying in edge and real-time environments. This work presents an integrated multi-stage optimization and deployment workflow for a BERT-based sentence pair classification model using the ONNX Runtime, OpenVINO, Neural Network Compression Framework (NNCF)-based INT8 quantization, and heterogeneous CPU-FPGA execution using the Intel FPGA AI Suite. Experimental results on the Microsoft Research Paraphrase Corpus (MRPC) benchmark show that the proposed framework increases the inference throughput from 16.74 FPS for the PyTorch FP32 baseline to 149.81 FPS and reduces the inference latency from 142.13 ms to 6.64 ms using INT8 quantization. Although INT8 quantization reduces the classification accuracy from 90.45% to 88.33%, significant improvements in inference throughput and latency are achieved. Heterogeneous CPU-FPGA deployment further increases the throughput to 584.74 FPS on the Agilex 7 platform. The model size is also reduced from 417.70 MB to 127.88 MB. These results demonstrate that combining software-level optimization with hardware acceleration provides an effective approach for deploying transformer-based models in real-time and edge applications.

## 키워드

(없음)

## 주제 분류 (OpenAlex Topics)

- Natural Language Processing Techniques (score: 0.540)
- Topic Modeling (score: 0.230)
- Speech Recognition and Synthesis (score: 0.036)

## 메모

