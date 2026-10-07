---
title: "Chain of thought driven reinforcement alignment with KAN for multimodal sentiment analysis of tourist reviews"
authors: ['Teng Wang', 'Yin Zhang', 'Rui Cheng', 'Qi Pan']
year: 2026
publication_date: 2026-09-15
venue: "Scientific Reports"
volume: "None"
issue: "None"
pages: ""
doi: "https://doi.org/10.1038/s41598-026-71097-x"
oa_status: "gold"
openalex_id: "https://openalex.org/W7213258387"
query_keyword: "text analysis"
tags: ['Sentiment Analysis and Opinion Mining', 'Emotion and Mood Recognition', 'Multimodal Machine Learning Applications']
keywords: ['Sentiment analysis', 'Discriminative model', 'Reinforcement learning', 'Generative grammar', 'Perceptron', 'Generative model', 'Crowdsourcing', 'Feature (linguistics)']
source: openalex-keyword
---

# Chain of thought driven reinforcement alignment with KAN for multimodal sentiment analysis of tourist reviews

**저자**: Teng Wang; Yin Zhang; Rui Cheng; Qi Pan
**출처**: Scientific Reports
**발행일**: 2026-09-15
**DOI**: https://doi.org/10.1038/s41598-026-71097-x
**수집 키워드**: text analysis

## 초록

Multimodal aspect-based sentiment analysis integrates text, images, and emojis to capture fine-grained emotional tendencies, making it particularly useful for social media opinion analysis and user experience evaluation. Traditional feature-level fusion networks, however, are easily corrupted by visual noise and lack explicit explanations for their emotional logic. At the same time, generative large language models, while capable of logical reasoning, are prone to hallucinations. Moreover, the discrete symbol streams they generate autoregressively are mathematically non-differentiable, making it exceptionally difficult to combine high-precision discriminative networks with interpretable generative networks. To tackle these challenges, we propose CoT-KRA, an interpretable sentiment analysis model for tourist reviews driven by a combination of Chain-of-Thought reinforcement learning and multi-layer Kolmogorov-Arnold Networks (KAN). Our framework departs from traditional forced image-text alignment, positioning the large language model as a prior reasoning generator and leaving the final decision to a downstream classifier. Specifically, we build a supervised fine-tuning dataset using distilled text from the open-source DeepSeek-R1 model to bolster the basic expressive power of our policy backbone, Meta Llama 3 8B-Instruct. This backbone parses aspect-aware dynamic emoji attribute triplets, which are then mapped into high-dimensional continuous feature vectors via a learnable polarity modulation projection matrix. We then construct a feature collaborative encoding module based on Conditional Layer Normalization to inject high-order prior knowledge without loss. To handle distortion noise in the visual channel, we design a derivative-free visual quality evaluation operator that implements adaptive gating truncation. We also replace the traditional Multi-Layer Perceptron with a KAN prediction network, taking advantage of its edge-learnable 1D spline curve activation to achieve highly precise non-linear decision boundaries. During policy optimization, we design a Group Relative Policy Optimization (GRPO) algorithm and a multi-dimensional composite reward function, feeding back the classification accuracy of the KAN network as an advantage signal to guide the LoRA updates of the language model policy. Evaluated on a dual NVIDIA RTX 3090 hardware setup, CoT-KRA achieves advanced classification performance on social media datasets like Twitter-2015, Twitter-2017, and SemEval-2017, as well as Yelp and TripAdvisor review collections.

## 키워드

Sentiment analysis, Discriminative model, Reinforcement learning, Generative grammar, Perceptron, Generative model, Crowdsourcing, Feature (linguistics)

## 주제 분류 (OpenAlex Topics)

- Sentiment Analysis and Opinion Mining (score: 0.798)
- Emotion and Mood Recognition (score: 0.033)
- Multimodal Machine Learning Applications (score: 0.032)

## 메모

