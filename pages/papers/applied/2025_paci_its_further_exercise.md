---
title: "“It’s a further exercise in futility”: implicit content detection and classification in Italian political discourse. A pilot study."
authors: ['Walter Paci']
year: 2025
venue: "AI-Linguistica Linguistic Studies on AI-Generated Texts and Discourses"
tags: ['Computational and Text Analysis Methods', 'Topic Modeling', 'Sentiment Analysis and Opinion Mining']
source: raw/applied/applied_2025_Its_a_further_exercise_in_ai_ling_v2i2_24.md
---

# “It’s a further exercise in futility”: implicit content detection and classification in Italian political discourse. A pilot study.

**제목(한글)**: 이탈리아 정치 담화에서의 함축적 내용 탐지 및 분류: 파일럿 연구

## 한국어 요약

**연구질문**: 최신 LLM은 이탈리아어 정치 발화에서 함축 내용(implicature)과 전제(presupposition)를 탐지·분류할 수 있는가?

**방법론**:
- IMPAQTS 코퍼스의 하위집합 활용
- 오픈소스 및 상용 다언어 모델 9종 평가
- 함축 내용 존재 여부 이진 탐지 및 함축/전제 이진 분류 두 가지 태스크 수행
- 6가지 프롬프팅(prompting) 기법 적용

**주요 결과**:
- 일부 상용 모델이 탐지 태스크에서 보통 수준의 성능 달성
- 분류 태스크에서는 어떤 모델도 우연 수준의 정확도를 넘지 못함
- 구조화된 프롬프팅 기법이 탐지에서 미미한 개선을 보이나 분류 정확도 향상에는 실패

**저자**: Walter Paci
**출처**: AI-Linguistica Linguistic Studies on AI-Generated Texts and Discourses, Vol.2
**발행일**: 2025-12-27
**DOI**: https://doi.org/10.62408/ai-ling.v2i2.24

## 초록 (원문)

Implicit content, such as implicatures and presuppositions, is a key feature of political discourse, allowing speakers to convey meaning indirectly and influence audience interpretation. While Large Language Models (LLMs) have demonstrated impressive capabilities in natural language understanding, their ability to process implicit meaning in real-world contexts remains an open question. This study investigates whether state-of-the-art LLMs can detect and classify implicit content in Italian political speech. Using a subset of the IMPAQTS corpus we assess nine multilingual models, both open-weight and proprietary. The study comprises two tasks: a binary detection task, where models determine whether a given sentence contains implicit content, and a binary classification task, in which models identify whether the implicit content is conveyed through implicature or presupposition. To enhance model performance, we employ six different prompting techniques. Results reveal that while some proprietary models exhibit moderate success in detecting implicit content, none surpass chance-level performance in classification. Open-weight models consistently underperform, with accuracy scores hovering near random guessing. Among prompting strategies, more structured techniques achieve marginal improvements in detection but fail to enhance classification accuracy. These findings highlight the persistent challenges LLMs face in pragmatic reasoning, defining implicit content detection and classification as unresolved tasks in NLP.

## 키워드

Meaning (existential), Politics, Feature (linguistics), Binary classification, Sentence, Content (measure theory), Face (sociological concept), Implicature

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

