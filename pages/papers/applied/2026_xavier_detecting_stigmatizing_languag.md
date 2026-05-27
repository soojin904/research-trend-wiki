---
title: "Detecting stigmatizing language with large language models: mind the settings"
authors: ['Teenu Xavier', 'Jane M. Carrington', 'Joshua Lambert W']
year: 2026
venue: "JAMIA Open"
tags: ['Health Literacy and Information Accessibility', 'Topic Modeling', 'Machine Learning in Healthcare']
source: raw/applied/applied_2026_Detecting_stigmatizing_la_ooag037.md
---

# Detecting stigmatizing language with large language models: mind the settings
**제목(한글)**: 대규모 언어 모델을 활용한 낙인 언어(Stigmatizing Language) 탐지: 최적 설정의 중요성

**저자**: Teenu Xavier; Jane M. Carrington; Joshua Lambert W
**출처**: JAMIA Open, Vol.9, pp.ooag037-ooag037
**발행일**: 2026-03-06
**DOI**: https://doi.org/10.1093/jamiaopen/ooag037

## 한국어 요약

**연구질문**: 전자의무기록(clinical documentation) 내 환자에 대한 편견이나 낙인 언어(예: 비협조적, 신뢰할 수 없음 등)를 탐지할 때, LLM의 파라미터(모델 크기, 온도, 퓨샷 예시 제공 여부)가 탐지 성능에 어떤 영향을 미치는가?

**방법론**:
- 로컬 구동 가능한 Llama-3.2(3B) 및 Llama-3.1(8B) 모델 사용
- 온도 설정(0.25, 0.5, 0.75) 및 프롬프트 내 예시(few-shot) 포함 여부 조건 조합 테스트
- 대형 대학 교육 병원으로부터 입수한 비식별 임상 기록 3,643건을 대상으로 정밀도, 진양성률(TPR), 진음성률(TNR)을 평가하고 인간의 레이블링과 비교

**주요 결과**:
- Llama 8B 모델에 낮은 온도(0.25)와 예시를 함께 주었을 때 최고의 정확도(70.2%)와 높은 진양성률(94.1%)을 기록함
- 3B 모델은 예시가 없을 때 진음성률이 99.7%에 달했으나 진양성률은 2%에 머물러 낙인 언어를 거의 잡아내지 못하는 성능 결핍을 보임
- 문서의 성격(응급의학과 기록 vs 치료 계획서)에 따라 탐지 정확도에 상당한 차이가 나며, 모델의 최적 매개변수를 맥락에 맞게 커스텀 조정할 필요성 입증


## 초록 (원문)

Background: Stigmatizing language in clinical documentation can contribute to healthcare disparities and affect patient-provider relationships. Given their strong capacity for contextual language understanding, large language models (LLMs) offer potential for detecting and reducing such language. This study evaluates the accuracy of LLMs in detecting stigmatizing language, focusing on model size, temperature settings, and the inclusion of examples. Methods: We evaluated multiple configurations of 2 local Llama-based large language models, Llama 3.2 (3B) and Llama 3.1 (8B) with varying temperature (0.25, 0.5, 0.75) and the inclusion of exemple prompts. The models were evaluated on 3643 de-identified clinical notes obtained from a tertiary care teaching hospital. Performance was assessed using accuracy, True Positive Rate (TPR), and True Negative Rate (TNR), with human annotator performance used as a benchmark. Results: The 8B model with a temperature of 0.25 and examples achieved the highest overall accuracy (70.2%), with the best TPR (94.1%), but the lowest TNR (47.4%). The 3B model without examples achieved the highest TNR (99.7%) but a very low TPR (2%). The inclusion of examples improved model accuracy across all configurations, while temperature settings had a variable impact, with smaller models benefiting from higher temperatures and larger models performing better at lower temperatures. ED provider notes showed higher accuracy (69.4%) and the plan of care was the lowest (55.8%). Conclusion: Model size, temperature, and the inclusion of examples play a critical role in optimizing open-source LLM performance. Tailoring these parameters to note types enhances effectiveness. Further research should refine these models for broader clinical application and assess their potential to reduce bias in healthcare documentation.

## 키워드

Inclusion (mineral), Affect (linguistics), Documentation, Language model, Health care, Variable (mathematics), Plan (archaeology)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

