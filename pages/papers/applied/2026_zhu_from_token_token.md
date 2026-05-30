---
title: "From Token to Token Pair: Efficient Prompt Compression for Large Language Models in Clinical Prediction"
authors: ['Mingcheng Zhu', 'Zhiyao Luo', 'Yu Liu', 'Tingting Zhu']
year: 2026
venue: "ArXiv.org"
tags: ['Machine Learning in Healthcare', 'Artificial Intelligence in Healthcare and Education', 'Topic Modeling']
source: raw/applied/applied_2026_From_Token_to_Token_Pair_nodoi.md
---

# From Token to Token Pair: Efficient Prompt Compression for Large Language Models in Clinical Prediction

**제목(한글)**: 토큰에서 토큰 쌍으로: 임상 예측을 위한 대규모 언어 모델의 효율적인 프롬프트 압축

## 한국어 요약

**연구질문**: 전자 건강 기록(EHR)을 자연어 시퀀스로 처리하여 사망률 예측 및 표현형 분석과 같은 임상 예측 작업에서 대규모 언어 모델(LLM)의 잠재력을 향상시키기 위해, 추가 비용이나 성능 손실 없이 토큰 시퀀스의 무손실 압축을 달성하는 방법을 제안한다.

**방법론**:
- EHR 시퀀스에 대한 표준 토큰화를 확장하는 계층형 방법인 의료 토큰 쌍 인코딩(MedTPE)을 제안한다.
- MedTPE는 자주 함께 발생하는 의료 토큰 쌍을 복합 토큰으로 병합하여 종속성을 인식하는 대체 전략을 통해 계산 복잡성을 유지하면서 무손실 압축을 제공한다.
- LLM 매개변수의 0.5-1.0%에 불과한 새로 도입된 토큰의 임베딩만 자체 지도 학습을 통해 미세 조정된다.

**주요 결과**:
- 두 가지 임상 시나리오에 대한 실제 데이터셋 실험에서 MedTPE가 입력 토큰 길이를 최대 31%, 추론 지연 시간을 34-63% 단축하며, 여러 LLM 및 4가지 임상 예측 작업 전반에 걸쳐 예측 성능과 출력 형식 규정 준수를 유지하거나 향상시킨다.
- MedTPE는 다양한 입력 컨텍스트 길이 전반에 걸쳐 견고성을 입증하고 과학 및 금융 도메인과 다양한 언어에 대한 일반화 가능성을 보여준다.

**저자**: Mingcheng Zhu; Zhiyao Luo; Yu Liu; Tingting Zhu
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-05-12
**DOI**: 

## 초록 (원문)

By processing electronic health records (EHRs) as natural language sequences, large language models (LLMs) have shown potential in clinical prediction tasks such as mortality prediction and phenotyping. However, longitudinal or highly frequent EHRs often yield excessively long token sequences that result in high computational costs and even reduced performance. Existing solutions either add modules for compression or remove less important tokens, which introduce additional inference latency or risk losing clinical information. To achieve lossless compression of token sequences without additional cost or loss of performance, we propose Medical Token-Pair Encoding (MedTPE), a layered method that extends standard tokenisation for EHR sequences. MedTPE merges frequently co-occurring medical token pairs into composite tokens, providing lossless compression while preserving the computational complexity through a dependency-aware replacement strategy. Only the embeddings of the newly introduced tokens of merely 0.5-1.0% of the LLM's parameters are fine-tuned via self-supervised learning. Experiments on real-world datasets for two clinical scenarios demonstrate that MedTPE reduces input token length by up to 31% and inference latency by 34-63%, while maintaining or even improving both predictive performance and output format compliance across multiple LLMs and four clinical prediction tasks. Furthermore, MedTPE demonstrates robustness across different input context lengths and generalisability to scientific and financial domains and different languages.

## 키워드

Security token, Lossless compression, Inference, Latency (audio), Robustness (evolution), Context (archaeology), Data compression, Encoding (memory)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

