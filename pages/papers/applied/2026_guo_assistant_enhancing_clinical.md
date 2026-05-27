---
title: "Dr. Assistant: Enhancing Clinical Diagnostic Inquiry via Structured Diagnostic Reasoning Data and Reinforcement Learning"
authors: ['Yue Guo', 'Fanfu Wang', 'Jianwei Lv', 'Xincheng Shi', 'Yuchen Li', 'Youya Wang', 'Yunsheng Zeng', 'Yujing Liu', 'Yunhao Qiao', 'Gen Li', 'Junfeng Wang', 'Bo Yuan']
year: 2026
venue: "arXiv (Cornell University)"
tags: ['Clinical Reasoning and Diagnostic Skills', 'Machine Learning in Healthcare', 'Topic Modeling']
source: raw/applied/applied_2026_Dr_Assistant_Enhancing_Cl_nodoi.md
---

# Dr. Assistant: Enhancing Clinical Diagnostic Inquiry via Structured Diagnostic Reasoning Data and Reinforcement Learning
**제목(한글)**: Dr. Assistant: 구조화된 진단 추론 데이터와 강화학습을 통한 임상 진단 문의 향상

**저자**: Yue Guo; Fanfu Wang; Jianwei Lv; Xincheng Shi; Yuchen Li; Youya Wang; Yunsheng Zeng; Yujing Liu; Yunhao Qiao; Gen Li; Junfeng Wang; Bo Yuan
**출처**: arXiv (Cornell University), Vol.None
**발행일**: 2026-01-20
**DOI**: 

## 한국어 요약

**연구질문**: 자격 있는 전문가 부족으로 임상 활용이 제한된 기존 임상 의사결정 지원 시스템(CDSS)의 한계를 넘어, 실제 의사-환자 대화를 모사하는 LLM 기반 다중 에이전트 프레임워크로 진단 추론 및 문진 역량을 어떻게 향상시킬 수 있는가?

**방법론**:
- 임상 추론 논리를 포착하는 임상 진단 추론 데이터(CDRD) 구조 및 파이프라인 개발
- 지도 미세조정(SFT)과 맞춤형 보상 함수를 적용한 강화학습(RL)의 2단계 훈련 방식 적용
- 진단 추론 및 문진 능력을 평가하기 위한 벤치마크 도입

**주요 결과**:
- Dr. Assistant 모델은 오픈소스 모델들을 능가하고 클로즈드소스 모델과 경쟁력 있는 성능을 달성함
- 구조화된 진단 추론 데이터와 강화학습의 결합이 임상 진단 문의 안내를 위한 효과적인 해결책임을 입증함

## 초록 (원문)

Clinical Decision Support Systems (CDSSs) provide reasoning and inquiry guidance for physicians, yet they face notable challenges, including high maintenance costs and low generalization capability. Recently, Large Language Models (LLMs) have been widely adopted in healthcare due to their extensive knowledge reserves, retrieval, and communication capabilities. While LLMs show promise and excel at medical benchmarks, their diagnostic reasoning and inquiry skills are constrained. To mitigate this issue, we propose (1) Clinical Diagnostic Reasoning Data (CDRD) structure to capture abstract clinical reasoning logic, and a pipeline for its construction, and (2) the Dr. Assistant, a clinical diagnostic model equipped with clinical reasoning and inquiry skills. Its training involves a two-stage process: SFT, followed by RL with a tailored reward function. We also introduce a benchmark to evaluate both diagnostic reasoning and inquiry. Our experiments demonstrate that the Dr. Assistant outperforms open-source models and achieves competitive performance to closed-source models, providing an effective solution for clinical diagnostic inquiry guidance. Project information can be found at: https://github.com/YGswu/Dr.-Assistant .

## 키워드

Generalization, Model-based reasoning, Reinforcement learning, Pipeline (software), Benchmark (surveying), Case-based reasoning, Clinical Practice, Diagnostic test

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

