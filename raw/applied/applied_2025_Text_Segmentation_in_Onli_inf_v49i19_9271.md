---
title: "Text Segmentation in Online Health Consultation Using Multi Layer Perceptron with Sentence Embedding and Sentence Features"
authors: ['Yunianita Rahmawati', 'Daniel Siahaan', 'Diana Purwitasari']
year: 2025
publication_date: 2025-12-15
venue: "Informatica"
volume: "49"
issue: "19"
pages: ""
doi: "https://doi.org/10.31449/inf.v49i19.9271"
oa_status: "diamond"
openalex_id: "https://openalex.org/W4417320654"
query_keyword: "text analysis"
tags: ['Topic Modeling', 'Health Literacy and Information Accessibility', 'Machine Learning in Healthcare']
keywords: ['Sentence', 'Segmentation', 'Embedding', 'Perceptron', 'Function (biology)', 'Structuring', 'Layer (electronics)']
source: openalex-keyword
---

# Text Segmentation in Online Health Consultation Using Multi Layer Perceptron with Sentence Embedding and Sentence Features

**저자**: Yunianita Rahmawati; Daniel Siahaan; Diana Purwitasari
**출처**: Informatica, Vol.49 No.19
**발행일**: 2025-12-15
**DOI**: https://doi.org/10.31449/inf.v49i19.9271
**수집 키워드**: text analysis

## 초록

The six aspects of doctor-patient communication are universal and relevant to various medical contexts and are the basis for structuring and analyzing doctors' answer texts in online health care. Identifying each aspect of communication in the doctor's answers is important to ensure effective communication. There are three critical challenges in segmenting the doctor’s answers, i.e. limited public dataset, extreme imbalance data, and implicit semantic variations between aspects. This study proposed a novel approach to text segmentation, focusing on communication aspects, particularly doctor-patient interactions. Unlike classical segmentation methods, which relied on topic similarity, the proposed method segmented text based on the communicative function of each sentence, offering a more accurate reflection of the interaction structure in Online Health Consultation (OHC). The model developed, MLPSentFeat, integrated sentence features directly into its architecture and demonstrated effectiveness in handling data with highly imbalanced label distributions without the need for synthetic data or complex balancing techniques.Sentence features were formed using a combined approach: the Likelihood Ratio (LR) algorithm filtered words relevant to a label, and Information Gain (InfoGain) selected the most informative features. Experimental results showed that integrating these sentence features significantly enhanced the model's sensitivity to variations in linguistic structure, especially in recognizing non-standard sentence types, such as questions, which were prevalent in the information-gathering aspect of medical communication.The best model produced, MLPSentFeat+DS2+Features3, was optimized to achieve the lowest segment error percentage of 8.18%, despite a slight performance decline in some labels after optimization. The use of text normalization, along with appropriate data size, cleanliness, and alignment of sentence features with the sentences' semantic structure, proved crucial in preventing overfitting. The MLPSentFeat model was successfully applied across various domains, demonstrating cross-domain adaptability, including in doctor's answer in online medical consultation systems, with potential for further development to identify questions with diverse sentence structures.

## 키워드

Sentence, Segmentation, Embedding, Perceptron, Function (biology), Structuring, Layer (electronics)

## 주제 분류 (OpenAlex Topics)

- Topic Modeling (score: 0.666)
- Health Literacy and Information Accessibility (score: 0.073)
- Machine Learning in Healthcare (score: 0.057)

## 메모

