---
title: "Predicting Rectal Cancer Patient Survival with Dutch Radiology Reports using Natural Language Processing (NLP): The Role of Pretrained Language Models"
authors: ['Lishan Cai', 'Tianyu Zhang', 'Regina G. H. Beets‐Tan', 'Joren Brunekreef', 'Jonas Teuwen']
year: 2026
venue: "medRxiv"
tags: ['Machine Learning in Healthcare', 'Artificial Intelligence in Healthcare and Education', 'Topic Modeling']
source: raw/applied/applied_2026_Predicting_Rectal_Cancer__2026_01_23_26344428.md
---

# Predicting Rectal Cancer Patient Survival with Dutch Radiology Reports using Natural Language Processing (NLP): The Role of Pretrained Language Models
**제목(한글)**: 자연어 처리(NLP)를 이용한 네덜란드어 방사선 판독 보고서 기반 직장암 환자 생존율 예측: 사전 학습된 언어 모델의 역할

**저자**: Lishan Cai; Tianyu Zhang; Regina G. H. Beets‐Tan; Joren Brunekreef; Jonas Teuwen
**출처**: medRxiv, Vol.None
**발행일**: 2026-01-30
**DOI**: https://doi.org/10.64898/2026.01.23.26344428

## 한국어 요약

**연구질문**: 암 환자의 직장암 판독 방사선 보고서 텍스트로부터 치료 후 생존율 및 무병 생존율을 정확히 예측하기 위해 네덜란드어 특화 사전 학습 모델이 어떤 성능 특성을 보이는가?

**방법론**:
- 네덜란드어로 작성된 임상 판독 데이터셋 활용
- 공개된 RobBERT, MedRoBERTa.nl 및 자체 직장/유방암 데이터로 scratch 학습한 세 가지 언어 모델의 생존 지수 대조 평가

**주요 결과**:
- 유방암과 직장암 코퍼스를 융합하여 scratch 학습시킨 모델이 생존율 예측 C-index 0.65 및 무병 생존 예측 C-index 0.71로 최고 성능을 달성함을 증명
- 범용 네덜란드어 모델이나 일반 병원 기록 모델보다 도메인 융합 및 특화 모델이 암 환자 진단 생존 예측에 월등함을 실증


## 초록 (원문)

Summary The use of Electronic Health Records (EHRs) has increased significantly in recent years. However, a substantial portion of the clinical data remains in unstructured text formats, especially in the context of radiology. This limits the application of EHRs for automated analysis in oncology research. Pretrained language models have been utilized to extract feature embeddings from these reports for downstream clinical applications, such as treatment response and survival prediction. However, a thorough investigation into which pretrained models produce the most effective features for rectal cancer survival prediction has not yet been done. This study explores the performance of five Dutch pretrained language models, including two publicly available models (RobBERT and MedRoBERTa.nl) and three developed in-house for the purpose of this study (RecRoBERT, BRecRoBERT, and BRec2RoBERT) with training on distinct Dutch-only corpora, in predicting overall survival and disease-free survival outcomes in rectal cancer patients. Our results showed that our in-house developed BRecRoBERT, a RoBERTa-based language model trained from scratch on a combination of Dutch breast and rectal cancer corpora, delivered the best predictive performance for both survival tasks, achieving a C-index of 0.65 (0.57, 0.73) for overall survival and 0.71 (0.64, 0.78) for disease-free survival. It outperformed models trained on general Dutch corpora (RobBERT) or Dutch hospital clinical notes (MedRoBERTa.nl). BRecRoBERT demonstrated the potential capability to predict survival in rectal cancer patients using Dutch radiology reports at diagnosis. This study highlights the value of pretrained language models that incorporate domain-specific knowledge for downstream clinical applications. Furthermore, it proves that utilizing data from related domains can improve the quality of feature embeddings for certain clinical tasks, particularly in situations where domain-specific data is scarce.

## 키워드

Context (archaeology), Colorectal cancer, Feature (linguistics), Language model, Cancer, Breast cancer, Predictive modelling

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

