---
title: "CTI-Thinker: an LLM-driven system for CTI knowledge graph construction and attack reasoning"
authors: ['Xiuzhang Yang', 'Ruijie Zhong', 'Yuling Chen', 'Guojun Peng', 'Di Yao', 'Chaofan Chen', 'Chenyang Wang', 'Dongni Zhang', 'Yilin Zhou', 'Zixuan Yang']
year: 2026
venue: "Cybersecurity"
tags: ['Advanced Graph Neural Networks', 'Topic Modeling', 'Big Data and Digital Economy']
source: raw/applied/applied_2026_CTIThinker_an_LLMdriven_s_s42400_025_00505_y.md
---

# CTI-Thinker: an LLM-driven system for CTI knowledge graph construction and attack reasoning
**제목(한글)**: CTI-Thinker: 사이버 위협 인텔리전스 지식 그래프 구축 및 공격 추론을 위한 LLM 구동형 시스템

**저자**: Xiuzhang Yang; Ruijie Zhong; Yuling Chen; Guojun Peng; Di Yao; Chaofan Chen; Chenyang Wang; Dongni Zhang; Yilin Zhou; Zixuan Yang
**출처**: Cybersecurity, Vol.9
**발행일**: 2026-01-16
**DOI**: https://doi.org/10.1186/s42400-025-00505-y

## 한국어 요약

**연구질문**: 기존 위협 인텔리전스(CTI) 데이터의 한계인 비구조화 포맷, 지식의 단편화, 그리고 전통적 텍스트 마이닝의 문맥 인식 부실 문제를 LLM과 시맨틱 정렬을 활용해 극복할 수 있는가?

**방법론**:
- 인컨텍스트 학습(In-context learning)과 LoRA 미세조정을 통한 CTI 텍스트 내 구조화된 위협 개체 및 관계 추출
- 추출된 정보를 MITRE ATT&CK 프레임워크에 벡터 기반 정렬 기법으로 매핑하여 이종 표현 표준화 및 지식 그래프 융합
- 구축된 지식 그래프를 RAG 프레임워크와 결합한 GraphRAG 기반 공격 의도 추론 엔진 설계

**주요 결과**:
- CTI-Thinker가 신뢰성 높은 CTI 지식 그래프를 구성하고 전술적 수준의 공격 의도와 배후 세력을 정밀하게 추론함을 입증
- 기존의 최신(SOTA) 정보 추출 방식 대비 정밀도(precision), 강건성(robustness), 일반화 성능에서 우수한 지표 달성


## 초록 (원문)

Abstract With the increasing frequency of APT attacks, cyber defense urgently demands high-quality threat intelligence support. Cyber threat intelligence (CTI) knowledge graphs have demonstrated significant potential in aiding threat detection and behavioral reasoning. However, existing CTI data often suffer from unstructured formats, fragmented knowledge, a reliance on manual annotation, and limited semantic mapping to attack techniques. These limitations hinder the robustness and accuracy of downstream reasoning tasks (e.g., attack attribution and intent inference). Moreover, traditional information extraction methods struggle to generalize in scenarios involving cross-paragraph dependencies, emerging threats, and low-resource samples, exhibiting weaknesses in context awareness and sensitivity to prompt variations. To this end, we propose CTI-Thinker, a novel system that integrates large language models with semantic alignment to the ATT&amp;CK framework for CTI knowledge graph construction and threat reasoning. First, CTI-Thinker leverages in-context learning and LoRA-based fine-tuning to extract structured threat entities and relations. Then, it adopts vector-based alignment strategies to unify heterogeneous expressions, enabling entity normalization and knowledge fusion for constructing a high-quality CTI knowledge graph. Finally, a GraphRAG-based reasoning engine is built by incorporating the structured knowledge graph and external ATT&amp;CK resources into a retrieval-augmented generation (RAG) framework, enabling tactical-level inference and CTI-driven question answering. Experimental results demonstrate that CTI-Thinker accurately extracts threat entities and relations and constructs a reliable CTI knowledge graph. It also effectively infers attack intent and supports intelligent reasoning. The system outperforms state-of-the-art methods in precision, robustness, and generalizability, offering a scalable and semantically enriched solution for cyber threat analysis and defense. Graphical abstract

## 키워드

Inference, Knowledge graph, Knowledge base, Scalability, Robustness (evolution), Graph, Inference engine, Knowledge representation and reasoning

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

