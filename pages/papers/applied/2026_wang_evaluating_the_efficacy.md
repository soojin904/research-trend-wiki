---
title: "Evaluating the efficacy of large language models in cardio-oncology patient education: a comparative analysis of accuracy, readability, and prompt engineering strategies"
authors: ['Zhao Wang', 'Lin Liang', 'Hao Xu', 'Yuhui Huang', 'Chen He', 'Weiran Xu', 'Haojie Zhu']
year: 2026
venue: "Frontiers in Artificial Intelligence"
tags: ['Artificial Intelligence in Healthcare and Education', 'Text Readability and Simplification', 'Topic Modeling']
source: raw/applied/applied_2026_Evaluating_the_efficacy_o_frai_2025_1693446.md
---

# Evaluating the efficacy of large language models in cardio-oncology patient education: a comparative analysis of accuracy, readability, and prompt engineering strategies
**제목(한글)**: 심장종양학 환자 교육에서 대규모 언어 모델의 효용성 평가: 정확도, 가독성 및 프롬프트 엔지니어링 전략의 비교 분석

**저자**: Zhao Wang; Lin Liang; Hao Xu; Yuhui Huang; Chen He; Weiran Xu; Haojie Zhu
**출처**: Frontiers in Artificial Intelligence, Vol.8, pp.1693446-1693446
**발행일**: 2026-01-13
**DOI**: https://doi.org/10.3389/frai.2025.1693446

## 한국어 요약

**연구질문**: 주요 대규모 언어 모델(ChatGPT-4, Kimi, DouBao)이 심장종양학 분야 환자 교육용 의료 질의에 대해 정확하고 가독성 높은 정보를 제공할 수 있으며 프롬프트 가이드가 결과물에 어떤 영향을 미치는가?

**방법론**:
- 심장종양학 주제에 대한 20개 표준 문항을 사용해 3종의 LLM을 대상으로 프롬프트 미지정 및 언어 단순화 지시 프롬프트 적용의 두 가지 조건으로 실험(총 240개 답변 분석)
- 전문의 4인에 의한 정확성, 포괄성, 유용성, 실용성 정성 평가
- 중국어 텍스트 분석 프레임워크를 통한 가독성(난이도, 단어 수, 문장 길이) 정량 평가

**주요 결과**:
- 전체 답변의 63.3%가 '정확', 35.0%가 '부분적으로 정확', 1.7%가 '부정확' 판정을 받음 (이 중 Kimi는 부정확 답변이 전혀 없었음)
- 쉬운 설명 프롬프트를 적용하면 문장 복잡도와 가독 연령이 유의미하게 감소하였으나 동시에 포괄성과 임상적 유용성이 저하되는 경향 확인
- LLM을 환자 교육에 성공적으로 사용하기 위해서는 특화된 파인튜닝(fine-tuning)과 평가 시스템이 필수적임을 제안


## 초록 (원문)

Background The integration of large language models (LLMs) into cardio-oncology patient education holds promise for addressing the critical gap in accessible, accurate, and patient-friendly information. However, the performance of publicly available LLMs in this specialized domain remains underexplored. Objectives This study evaluates the performance of three LLMs (ChatGPT-4, Kimi, DouBao) act as assistants for physicians in cardio-oncology patient education and examines the impact of prompt engineering on response quality. Methods Twenty standardized questions spanning cardio-oncology topics were posed twice to three LLMs (ChatGPT-4, Kimi, DouBao): once without prompts and once with a directive to simplify language, generating 240 responses. These responses were evaluated by four cardio-oncology specialists for accuracy, comprehensiveness, helpfulness, and practicality. Readability and complexity were assessed using a Chinese text analysis framework. Results Among 240 responses, 63.3% were rated “correct,” 35.0% “partially correct,” and 1.7% “incorrect.” No significant differences in accuracy were observed between models ( p = 0.26). Kimi demonstrated no incorrect responses. Significant declines in comprehensiveness ( p = 0.03) and helpfulness ( p &amp;lt; 0.01) occurred post-prompt, particularly for DouBao (accuracy: 57.5% vs. 7.5%, p &amp;lt; 0.01). Readability metrics (readability age, difficulty score, total word count, sentence length) showed no inter-model differences, but prompts reduced complexity (e.g., DouBao’s readability age decreased from 12.9 ± 0.8 to 10.1 ± 1.2 years, p &amp;lt; 0.01). Conclusion Publicly available LLMs provide largely accurate responses to cardio-oncology questions, yet their utility is constrained by inconsistent comprehensiveness and sensitivity to prompt design. While simplifying language improves readability, it risks compromising clinical relevance. Tailored fine-tuning and specialized evaluation frameworks are essential to optimize LLMs for patient education in cardio-oncology.

## 키워드

Key (lock), Risk assessment, Sensitivity (control systems), Language model, Risk management

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

