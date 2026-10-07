---
title: "An optimization and deployment framework for efficient BERT-based paraphrase detection"
authors: ['Bonthu Chandra Praveen', 'K. Sivasankaran']
year: 2026
venue: "Array"
tags: ['Natural Language Processing Techniques', 'Topic Modeling', 'Speech Recognition and Synthesis']
source: raw/applied/applied_2026_An_optimization_and_deplo_j_array_2026_101288.md
---

# An optimization and deployment framework for efficient BERT-based paraphrase detection

**저자**: Bonthu Chandra Praveen; K. Sivasankaran
**출처**: Array, Vol.None, pp.101288-101288
**발행일**: 2026-09-01
**DOI**: https://doi.org/10.1016/j.array.2026.101288

## 초록 (원문)

Paraphrase identification is an important application in Natural Language Processing (NLP) and plays a significant role in large-scale and real-time text analysis. Although transformer-based models such as Bidirectional Encoder Representations from Transformers (BERT) achieve high accuracy, for these applications their computational complexity and memory requirements face challenges for deploying in edge and real-time environments. This work presents an integrated multi-stage optimization and deployment workflow for a BERT-based sentence pair classification model using the ONNX Runtime, OpenVINO, Neural Network Compression Framework (NNCF)-based INT8 quantization, and heterogeneous CPU-FPGA execution using the Intel FPGA AI Suite. Experimental results on the Microsoft Research Paraphrase Corpus (MRPC) benchmark show that the proposed framework increases the inference throughput from 16.74 FPS for the PyTorch FP32 baseline to 149.81 FPS and reduces the inference latency from 142.13 ms to 6.64 ms using INT8 quantization. Although INT8 quantization reduces the classification accuracy from 90.45% to 88.33%, significant improvements in inference throughput and latency are achieved. Heterogeneous CPU-FPGA deployment further increases the throughput to 584.74 FPS on the Agilex 7 platform. The model size is also reduced from 417.70 MB to 127.88 MB. These results demonstrate that combining software-level optimization with hardware acceleration provides an effective approach for deploying transformer-based models in real-time and edge applications.

## 키워드



## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

