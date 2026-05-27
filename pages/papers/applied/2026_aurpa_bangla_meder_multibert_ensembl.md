---
title: "Bangla MedER: Multi-BERT ensemble approach for the recognition of Bangla medical entity"
authors: ['Tanjim Taharat Aurpa', 'Farzana Akter', 'Md. Mehedi Hasan', 'Shakil Ahmed', 'Shifat Ara Rafiq', 'Fatema Khan', 'Md. Rubel Sheikh']
year: 2026
venue: "PLoS ONE"
tags: ['Topic Modeling', 'Machine Learning in Healthcare', 'Biomedical Text Mining and Ontologies']
source: raw/applied/applied_2026_Bangla_MedER_MultiBERT_en_journal_pone_0342558.md
---

# Bangla MedER: Multi-BERT ensemble approach for the recognition of Bangla medical entity
**제목(한글)**: Bangla MedER: 방글라데시 의료 개체명 인식을 위한 멀티 BERT 앙상블 접근법

**저자**: Tanjim Taharat Aurpa; Farzana Akter; Md. Mehedi Hasan; Shakil Ahmed; Shifat Ara Rafiq; Fatema Khan; Md. Rubel Sheikh
**출처**: PLoS ONE, Vol.21, pp.e0342558-e0342558
**발행일**: 2026-02-26
**DOI**: https://doi.org/10.1371/journal.pone.0342558

## 한국어 요약

**연구질문**: 데이터 자원이 빈약한 벵골어(Bangla) 의료 텍스트 코퍼스에서 의미론적 진료 개체명(의학 용어, 질병명 등)을 정밀하게 검출할 수 있는 NLP 아키텍처는 무엇인가?

**방법론**:
- 벵골어 전용 메디컬 개체명 인식 데이터셋을 자체 구축하고 가이드라인 마련
- BERT, DistilBERT, ELECTRA, RoBERTa의 다양한 조합을 통합한 멀티 뷰 기반의 'Multi-BERT Ensemble' 모델 제안 및 단일 성능과의 대조 평가

**주요 결과**:
- 제안된 멀티 BERT 앙상블 모델이 89.58%의 최고 검출 정확도를 획득하여 단일 레이어 모델 대비 11.80%의 비약적인 정확도 향상을 입증
- 저자원 언어 의료 NLP 연구의 기틀을 마련


## 초록 (원문)

Medical Entity Recognition (MedER) is an essential NLP task for extracting meaningful entities from the medical corpus. Nowadays, MedER-based research outcomes can remarkably contribute to the development of automated systems in the medical sector, ultimately enhancing patient care and outcomes. While extensive research has been conducted on MedER in English, low-resource languages like Bangla remain underexplored. Our work aims to bridge this gap. For Bangla medical entity recognition, this study first examined a number of transformer models, including BERT, DistilBERT, ELECTRA, and RoBERTa. We also propose a novel Multi-BERT Ensemble approach that outperformed all baseline models with the highest accuracy of 89.58%. Notably, it provides an 11.80% accuracy improvement over the single-layer BERT model, demonstrating its effectiveness for this task. A major challenge in MedER for low-resource languages is the lack of annotated datasets. To address this issue, we developed a high-quality dataset tailored for the Bangla MedER task. The dataset was used to evaluate the effectiveness of our model through multiple performance metrics, demonstrating its robustness and applicability. Our findings highlight the potential of Multi-BERT Ensemble models in improving MedER for Bangla and set the foundation for further advancements in low-resource medical NLP.

## 키워드

Bengali, Robustness (evolution), Named-entity recognition, Task (project management), Set (abstract data type), Baseline (sea)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

