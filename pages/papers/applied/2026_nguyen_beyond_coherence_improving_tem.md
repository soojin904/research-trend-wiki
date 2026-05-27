---
title: "Beyond Coherence: Improving Temporal Consistency and Interpretability in Dynamic Topic Models"
authors: ['Thanh Vinh Nguyen', 'Ngo Van Dong', 'Minh Chu Xuan', 'Tung Nguyen', 'Linh Ngo Van', 'Dinh Viet Sang', 'Trung Le']
year: 2026
venue: ""
tags: ['Computational and Text Analysis Methods', 'Data Quality and Management', 'Topic Modeling']
source: raw/applied/applied_2026_Beyond_Coherence_Improvin_2026_findings_eacl_187.md
---

# Beyond Coherence: Improving Temporal Consistency and Interpretability in Dynamic Topic Models
**제목(한글)**: 일관성을 넘어서: 동적 토픽 모델의 시간적 정합성과 해석 가능성 개선

**저자**: Thanh Vinh Nguyen; Ngo Van Dong; Minh Chu Xuan; Tung Nguyen; Linh Ngo Van; Dinh Viet Sang; Trung Le
**출처**: , Vol.None, pp.3609-3629
**발행일**: 2026-01-01
**DOI**: https://doi.org/10.18653/v1/2026.findings-eacl.187

## 한국어 요약

**연구질문**: 시간 흐름에 따른 텍스트 데이터의 변화를 분석하는 동적 토픽 모델(Dynamic Topic Model)에서, 사전학습 언어모델(PLM)의 의미 정보 반영 결여, 경직된 선형 토픽 흐름 추적, 해석 불투명성 한계를 극복할 방안은 무엇인가?

**방법론**:
- L-DNTM(LLM-Augmented Dynamic Neural Topic Model) 변분 프레임워크 제안
- PLM 의미론을 인코더에 전이하기 위한 다목적 지식 증류(distillation) 기법 적용
- 엔트로피 규제 최적 운송(optimal transport)을 통해 시간에 따른 토픽 분포를 연속적으로 정렬
- LLM을 이용하여 동적 토픽 어휘 분포 정제

**주요 결과**:
- 제안된 L-DNTM 모델이 시간에 따른 주제의 분할, 병합 등 비선형적 변화를 자연스럽게 포착하며 정합성을 높임을 규명함
- 기존의 동적 토픽 모델 대비 동적 분류 및 클러스터링 태스크와 단어 목록 해석 명료도를 대폭 향상시킴을 입증함


## 초록 (원문)

Dynamic topic models aim to reveal how themes emerge, evolve, and dissolve in timestamped corpora, but existing approaches still face three major challenges: (i) encoders capture bag-of-words statistics but fail to align with the rich semantic priors of large pretrained language models, (ii) temporal linkages are often modeled as rigid one-to-one chains, limiting the ability to track non-linear evolution such as topic splits or merges, and (iii) interpretability remains shallow, relying on noisy top-word lists that obscure thematic clarity.We propose L-DNTM (LLM-Augmented for Dynamic Neural Topic Model), a variational framework designed to capture more faithful temporal trajectories.Our model integrates three key components: multiobjective distillation to inject PLM-derived semantic knowledge into the encoder, entropyregularized optimal transport to align entire topic constellations across time for smooth yet flexible evolution, and LLM-guided refinement to sharpen topicword distributions for improved interpretability.Extensive experiments on diverse corpora show that L-DNTM yields more coherent, temporally consistent, and interpretable topic dynamics, and further enhances downstream classification and clustering tasks.

## 키워드

Interpretability, Consistency (knowledge bases), Topic model, Feature (linguistics)

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

