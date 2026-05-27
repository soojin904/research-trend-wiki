---
title: "AgentMental: An Interactive Multi-Agent Framework for Explainable and Adaptive Mental Health Assessment"
authors: ['Jinpeng Hu', 'Ao Wang', 'Qianqian Xie', 'Zhuo Li', 'Hui Ma', 'Dan Guo']
year: 2026
venue: "Proceedings of the AAAI Conference on Artificial Intelligence"
tags: ['Mental Health via Writing', 'Topic Modeling', 'Machine Learning in Healthcare']
source: raw/applied/applied_2026_AgentMental_An_Interactiv_aaai_v40i37_40365.md
---

# AgentMental: An Interactive Multi-Agent Framework for Explainable and Adaptive Mental Health Assessment
**제목(한글)**: AgentMental: 설명 가능하고 적응적인 정신 건강 평가를 위한 대화형 멀티 에이전트 프레임워크

**저자**: Jinpeng Hu; Ao Wang; Qianqian Xie; Zhuo Li; Hui Ma; Dan Guo
**출처**: Proceedings of the AAAI Conference on Artificial Intelligence, Vol.40, pp.31050-31058
**발행일**: 2026-03-14
**DOI**: https://doi.org/10.1609/aaai.v40i37.40365

## 한국어 요약

**연구질문**: 자격 있는 전문가 부족으로 인한 전통적 임상 심리 평가의 한계를 극복하기 위해, 의사-환자 임상 대화를 시뮬레이션하는 다중 에이전트 프레임워크가 정적 텍스트 분석을 넘어 어떻게 더 깊고 정보가 풍부한 정신 건강 평가를 실현하는가?

**방법론**:
- 질문(questioning), 충분성 평가(adequacy evaluation), 점수 산정(scoring), 갱신(updating) 등의 역할을 담당하는 전문화된 에이전트로 구성된 다중 에이전트 프레임워크 설계
- 사용자 응답의 충분성을 평가하여 타겟 추가 질문을 생성하는 적응적 문진 메커니즘 도입
- 루트 노드에 기본 정보를, 자식 노드에 증상 카테고리별 핵심 정보를 조직하는 트리 구조 메모리 사용 및 DAIC-WOZ 데이터셋으로 평가

**주요 결과**:
- AgentMental은 DAIC-WOZ 데이터셋에서 기존 접근법들보다 우수한 정신 건강 평가 성능을 달성함
- 적응적 문진과 동적 메모리 갱신이 중복 질문을 줄이고 맥락 추적 능력을 향상시켜 임상 대화의 정보 추출 효율성을 높임을 입증함

## 초록 (원문)

Mental health assessment is crucial for early intervention and effective treatment, yet traditional clinician-based approaches are limited by the shortage of qualified professionals. Recent advances in artificial intelligence have sparked growing interest in automated psychological assessment, yet most existing approaches are constrained by their reliance on static text analysis, limiting their ability to capture deeper and more informative insights that emerge through dynamic interaction and iterative questioning. Therefore, in this paper, we propose a multi-agent framework for mental health evaluation that simulates clinical doctor-patient dialogues, with specialized agents assigned to questioning, adequacy evaluation, scoring, and updating. In detail, we introduce an adaptive questioning mechanism in which an evaluation agent assesses the adequacy of user responses to determine the necessity of generating targeted follow-up queries to address ambiguity and missing information. Additionally, we employ a tree-structured memory in which the root node encodes the user's basic information, while child nodes (e.g., topic and statement) organize key information according to distinct symptom categories and interaction turns. This memory is dynamically updated throughout the interaction to reduce redundant questioning and enhance the information extraction and contextual tracking capabilities. Experimental results on the DAIC-WOZ dataset illustrate the effectiveness of our proposed method, which achieves better performance than existing approaches. Our code is released at \url{https://github.com/MindIntLab-HFUT/AgentMental}.

## 키워드

Ambiguity, Key (lock), Node (physics), Mental health, Scheme (mathematics), Mechanism (biology), Limiting

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

