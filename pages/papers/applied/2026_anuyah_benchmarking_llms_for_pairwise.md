---
title: "Benchmarking LLMs for Pairwise Causal Discovery in Biomedical and Multi-Domain Contexts"
authors: ['Sydney Anuyah', 'Sneha Shajee-Mohan', 'Ankit-Singh Chauhan', 'Sunandan Chakraborty']
year: 2026
venue: "ArXiv.org"
tags: ['Biomedical Text Mining and Ontologies', 'Topic Modeling', 'Artificial Intelligence in Healthcare and Education']
source: raw/applied/applied_2026_Benchmarking_LLMs_for_Pai_nodoi.md
---

# Benchmarking LLMs for Pairwise Causal Discovery in Biomedical and Multi-Domain Contexts

**제목(한글)**: 생물의학 및 다중 도메인 맥락에서 쌍별 인과 관계 발견을 위한 LLM 벤치마킹

## 한국어 요약

**연구질문**: 대규모 언어 모델(LLM)이 생물의학 및 다중 도메인 텍스트에서 쌍별 인과 관계 발견(PCD)이라는 근본적인 작업을 얼마나 잘 수행하며, 그 인과적 추론 능력은 어느 정도인가?

**방법론**:
- 13개의 오픈소스 LLM을 대상으로 테스트 진행
- 12개 데이터셋 기반의 벤치마크를 활용하여 인과 관계 탐지(Causal Detection) 및 인과 관계 추출(Causal Extraction) 능력 평가
- 제로샷(zero-shot), CoT(Chain-of-Thought), FICL(Few-shot In-Context Learning) 등 다양한 프롬프트 기법 사용
- 높은 주석자 간 일치도($κ\ge 0.758$)로 검증된 데이터셋 기반의 통합 평가 프레임워크 구축

**주요 결과**:
- 현재 LLM 모델들의 인과적 추론 능력에 심각한 결함이 발견됨. 인과 관계 탐지 및 추출 최고 모델은 각각 49.57%, 47.12%의 평균 점수를 기록.
- 모델은 단순하고 명시적이며 단일 문장으로 된 관계에서 가장 좋은 성능을 보임.
- 암묵적 관계, 다중 문장에 걸친 연결, 여러 인과 쌍을 포함하는 텍스트 등 복잡한 경우 성능이 급격히 저하됨.

**저자**: Sydney Anuyah; Sneha Shajee-Mohan; Ankit-Singh Chauhan; Sunandan Chakraborty
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-01-21
**DOI**: 

## 초록 (원문)

The safe deployment of large language models (LLMs) in high-stakes fields like biomedicine, requires them to be able to reason about cause and effect. We investigate this ability by testing 13 open-source LLMs on a fundamental task: pairwise causal discovery (PCD) from text. Our benchmark, using 12 diverse datasets, evaluates two core skills: 1) \textbf{Causal Detection} (identifying if a text contains a causal link) and 2) \textbf{Causal Extraction} (pulling out the exact cause and effect phrases). We tested various prompting methods, from simple instructions (zero-shot) to more complex strategies like Chain-of-Thought (CoT) and Few-shot In-Context Learning (FICL). The results show major deficiencies in current models. The best model for detection, DeepSeek-R1-Distill-Llama-70B, only achieved a mean score of 49.57\% ($C_{detect}$), while the best for extraction, Qwen2.5-Coder-32B-Instruct, reached just 47.12\% ($C_{extract}$). Models performed best on simple, explicit, single-sentence relations. However, performance plummeted for more difficult (and realistic) cases, such as implicit relationships, links spanning multiple sentences, and texts containing multiple causal pairs. We provide a unified evaluation framework, built on a dataset validated with high inter-annotator agreement ($κ\ge 0.758$), and make all our data, code, and prompts publicly available to spur further research. \href{https://github.com/sydneyanuyah/CausalDiscovery}{Code available here: https://github.com/sydneyanuyah/CausalDiscovery}

## 키워드

Pairwise comparison, Benchmarking, Causality (physics), Causation, Best practice, Causal model, Core (optical fiber)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]
- [[pages/concepts/causal_inference_networks|인과 추론과 네트워크]]

## 메모

