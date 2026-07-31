---
title: "Attention Bidirectional Gated Fusion Based Multimodal Intent Recognition Under Uncertain Missing Modalities"
authors: ['Ling Shang', 'Zhizhong Liu', 'Yuxuan Wu', 'Xiaoyu Song', 'Jian Yu', 'Quan Z. Sheng']
year: 2026
publication_date: 2026-07-28
venue: "Information"
volume: "17"
issue: "8"
pages: "728-728"
doi: "https://doi.org/10.3390/info17080728"
oa_status: "gold"
openalex_id: "https://openalex.org/W7171536306"
query_keyword: "social network"
tags: ['Emotion and Mood Recognition', 'Topic Modeling', 'Speech Recognition and Synthesis']
keywords: ['Modalities', 'Encoder', 'Robustness (evolution)', 'Modality (human–computer interaction)', 'Transformer', 'Missing data', 'Pattern recognition (psychology)']
source: openalex-keyword
---

# Attention Bidirectional Gated Fusion Based Multimodal Intent Recognition Under Uncertain Missing Modalities

**저자**: Ling Shang; Zhizhong Liu; Yuxuan Wu; Xiaoyu Song; Jian Yu; Quan Z. Sheng
**출처**: Information, Vol.17 No.8, pp.728-728
**발행일**: 2026-07-28
**DOI**: https://doi.org/10.3390/info17080728
**수집 키워드**: social network

## 초록

Currently, uncertain missing modalities pose new challenges to multimodal intent recognition. To tackle this issue, this work proposes an Attention Bidirectional Gated Fusion Based Multimodal Intent Recognition model under Uncertain Missing Modalities (named ABGFMIR). Firstly, ABGFMIR extracts the features of each modality (text, audio, visual) with the LSTM network, respectively. Secondly, ABGFMIR narrows the distances between audio, visual and text modality based on Central Moment Discrepancy (CMD), and then performs multimodal feature fusion through an attention bidirectional gated fusion method. Then, corresponding attention level prompts are generated based on the uncertain missing modalities situations of the current sample. The fused multimodal features are then input into the Transformer encoder and decoder, and the prompts are injected into the keys and values of the multihead self-attention layer to guide the Transformer to focus on the missing modes and dynamically adjust the attention distribution, enhancing the robustness of ABGFMIR to different missing modes. Finally, the features produced by the Transformer are fed into the classification layer for intent recognition. Simultaneously, the pre-trained model (AGNN) that trained with the complete modality is employed in the classification layer to guide the main module of ABGFMIR. Two public benchmark datasets (MIntRec and EMOTyDA) are adopted for performance verification. Compared with the other five baseline models, on the MIntRec dataset, ABGFMIR improved accuracy by an average of 2.68 and improved F1 values by an average of 3.24. On the EMOTyDA dataset, ABGFMIR improved accuracy by an average of 2.28 and improved F1 values by an average of 3.44.

## 키워드

Modalities, Encoder, Robustness (evolution), Modality (human–computer interaction), Transformer, Missing data, Pattern recognition (psychology)

## 주제 분류 (OpenAlex Topics)

- Emotion and Mood Recognition (score: 0.521)
- Topic Modeling (score: 0.072)
- Speech Recognition and Synthesis (score: 0.023)

## 메모

