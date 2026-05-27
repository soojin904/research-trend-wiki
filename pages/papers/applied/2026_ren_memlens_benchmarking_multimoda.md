---
title: "MemLens: Benchmarking Multimodal Long-Term Memory in Large Vision-Language Models"
authors: ['Xiyu Ren', 'Zhaowei Wang', 'Yiming Du', 'Zhongwei Xie', 'Chi Liu', 'Xinlin Yang', 'Haoyue Feng', 'Wenjun Pan', 'Tianshi Zheng', 'Baixuan Xu', 'Zhengnan Li', 'Yangqiu Song', 'Ginny Wong', 'Simon See']
year: 2026
venue: "ArXiv.org"
tags: ['Multimodal Machine Learning Applications', 'Topic Modeling', 'Domain Adaptation and Few-Shot Learning']
source: raw/applied/applied_2026_MemLens_Benchmarking_Mult_nodoi.md
---

# MemLens: Benchmarking Multimodal Long-Term Memory in Large Vision-Language Models

**제목(한글)**: MemLens: 대형 시각-언어 모델의 다중 모드 장기 기억 벤치마킹

## 한국어 요약

**연구질문**: 장기적 다중 모드 대화에서 요구되는 기억 능력을 평가하기 위한 체계적 벤치마크가 부재한 상황에서, 긴 문맥 LVLMs(Large Vision-Language Models)와 기억 증강 에이전트를 어떻게 객관적으로 비교 평가할 수 있는가?

**방법론**:
- 5가지 기억 능력(정보 추출, 다중 세션 추론, 시간 추론, 지식 갱신, 답변 거부)과 4가지 표준 문맥 길이(32K~256K 토큰)에 걸친 789개 질문으로 구성된 MEMLENS 벤치마크 구축
- 이미지 어블레이션 연구를 통해 시각적 증거의 필수성 검증
- 27개의 LVLMs와 7개의 기억 증강 에이전트를 대상으로 종합 평가 수행

**주요 결과**:
- 긴 문맥 LVLMs는 단기 문맥에서는 직접적 시각 근거를 통해 높은 정확도를 보이지만 대화가 길어질수록 성능이 저하됨
- 기억 증강 에이전트는 길이 안정적이나 저장 시 압축 과정에서 시각적 정보 충실도가 손상되며, 다중 세션 추론의 경우 대부분의 시스템이 30% 미만의 정확도에 머물러 두 접근법 모두의 한계를 규명함

**저자**: Xiyu Ren; Zhaowei Wang; Yiming Du; Zhongwei Xie; Chi Liu; Xinlin Yang; Haoyue Feng; Wenjun Pan; Tianshi Zheng; Baixuan Xu; Zhengnan Li; Yangqiu Song; Ginny Wong; Simon See
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-05-14
**DOI**: 

## 초록 (원문)

Memory is essential for large vision-language models (LVLMs) to handle long, multimodal interactions, with two method directions providing this capability: long-context LVLMs and memory-augmented agents. However, no existing benchmark conducts a systematic comparison of the two on questions that genuinely require multimodal evidence. To close this gap, we introduce MEMLENS, a comprehensive benchmark for memory in multimodal multi-session conversations, comprising 789 questions across five memory abilities (information extraction, multi-session reasoning, temporal reasoning, knowledge update, and answer refusal) at four standard context lengths (32K-256K tokens) under a cross-modal token-counting scheme. An image-ablation study confirms that solving MEMLENS requires visual evidence: removing evidence images drops two frontier LVLMs below 2% accuracy on the 80.4% of questions whose evidence includes images. Evaluating 27 LVLMs and 7 memory-augmented agents, we find that long-context LVLMs achieve high short-context accuracy through direct visual grounding but degrade as conversations grow, whereas memory agents are length-stable but lose visual fidelity under storage-time compression. Multi-session reasoning caps most systems below 30%, and neither approach alone solves the task. These results motivate hybrid architectures that combine long-context attention with structured multimodal retrieval. Our code is available at https://github.com/xrenaf/MEMLENS.

## 키워드

Benchmark (surveying), Benchmarking, Context (archaeology), Code (set theory), Visual reasoning, Fidelity

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

