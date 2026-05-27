---
title: "Comparison of proprietary and fine-tuned large language models for multi-label classification of billing codes from radiology reports"
authors: ['Kamyar Arzideh', 'Henning Schäfer', 'Ahmad Idrissi-Yaghir', 'Bahadır Eryılmaz', 'Sina Warmer', 'Eva Maria Hartmann', 'Katarzyna Borys', 'Cynthia Sabrina Schmidt', 'Johannes Haubold', 'Lale Umutlu', 'Michael Forsting', 'Felix Nensa', 'René Hosch']
year: 2026
venue: "European Radiology"
tags: ['Topic Modeling', 'Machine Learning in Healthcare', 'Text and Document Classification Technologies']
source: raw/applied/applied_2026_Comparison_of_proprietary_s00330_026_12445_3.md
---

# Comparison of proprietary and fine-tuned large language models for multi-label classification of billing codes from radiology reports
**제목(한글)**: 방사선 보고서의 진료 코드 다중 레이블 분류를 위한 상용 및 미세조정 대규모 언어 모델 비교

**저자**: Kamyar Arzideh; Henning Schäfer; Ahmad Idrissi-Yaghir; Bahadır Eryılmaz; Sina Warmer; Eva Maria Hartmann; Katarzyna Borys; Cynthia Sabrina Schmidt; Johannes Haubold; Lale Umutlu; Michael Forsting; Felix Nensa; René Hosch
**출처**: European Radiology, Vol.None
**발행일**: 2026-03-14
**DOI**: https://doi.org/10.1007/s00330-026-12445-3

## 한국어 요약

**연구질문**: 방사선과 판독 판결문에서 진료수가 청구용 코드(GOÄ)를 자동으로 추출하여 청구 정확성을 높이는 업무에 대해 상용 LLM과 특정 영역 미세조정(Fine-tuned) 모델의 성능 차이는 어떠한가?

**방법론**:
- 기 주석화된 499,601개의 판독 보고서(12만 여명 환자)의 179.9만 개 GOÄ 코드를 그라운드 트루스로 활용
- MediPhi-Instruct 4B 모델을 미세조정하고 GPT-5, Gemini 2.5, DeepSeek-R1 등 대형 상용 모델과의 Zero-shot/Few-shot 성능 비교 검증

**주요 결과**:
- 미세조정 모델이 F1-스코어 87.79%를 달성하여 상용 경량 모델인 Gemini 2.5 Flash를 유의미하게 압도함을 밝힘
- 단, 정제 데이터셋에서는 GPT-5가 F1-스코어 89.51%로 최고 성능을 내어, 의료 정보 청구에 있어 도메인 특화 경량 미세조정 모델이 실무적 대체재가 될 수 있음을 증명


## 초록 (원문)

OBJECTIVES: While large language models (LLMs) have shown promise in medical text analysis, their application in automated medical billing code extraction remains underexplored, particularly for the German medical fee schedule system (GOÄ). Therefore, an LLM was fine-tuned to perform multi-label classification of GOÄ codes from radiology reports automatically, and its performance was compared with state-of-the-art commercial and open-source LLMs. MATERIALS AND METHODS: Following ethics committee approval, we analyzed 499,601 radiology reports from 124,497 patients, containing 1,799,971 manually identified GOÄ codes as ground truth. The MediPhi-Instruct 4B model was fine-tuned using five-fold cross-validation. Performance was evaluated on the hold-out test set and compared against GPT-5, GPT-4.1, GPT-oss, Kimi-K2, Deepseek-R1, Deepseek-V3, Gemini 2.5, Llama-70B, and Qwen-3 LLMs on a subset of 500 anonymized and 350 cleaned reports using zero-shot and few-shot prompting techniques. RESULTS: The fine-tuned model achieved an accuracy of 77.15% ± 0.47% and a micro-average F1-score of 87.79% ± 0.31% on the hold-out test set. On a subset of 500 real-world samples, our models outperformed the best-performing LLM, Gemini 2.5 Flash, with an F1-score of 70.32% ± 1.54% compared to 58.22% ± 1.50% (p < 0.001). For the cleaned dataset of 350 samples, GPT-5 achieved the best F1-score of 89.51 ± 1.52% and outperformed the fine-tuned models (p < 0.001). CONCLUSIONS: Fine-tuned LLMs can effectively automate GOÄ code classification from radiology reports, with the potential of outperforming commercial LLMs. This approach shows promise for improving billing efficiency and accuracy in healthcare settings, though manual verification is still recommended. KEY POINTS: Question LLMs with high parameters possess medical knowledge, but how effective are they at predicting billing codes from radiology reports compared to smaller, fine-tuned models? Finidngs A fine-tuned ensemble model achieved competitive results and can outperform larger, proprietary LLMs. Clinical relevance Smaller, fine-tuned models offer an efficient alternative to proprietary LLMs in generating billing codes and can be integrated to assist clinical coding. This technology has the potential to transform clinical billing procedures, but its use should be overseen by qualified professional personnel.

## 키워드

Test (biology), Schedule, Set (abstract data type), Code (set theory), Test set, Interventional radiology, Ground truth, Diagnosis code

## 위키 연관

- [[pages/concepts/causal_inference_networks|인과 추론과 네트워크]]

## 메모

