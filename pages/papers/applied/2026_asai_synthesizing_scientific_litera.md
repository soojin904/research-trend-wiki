---
title: "Synthesizing scientific literature with retrieval-augmented language models"
authors: ['Akari Asai', 'Jacqueline He', 'Rulin Shao', 'Weijia Shi', 'Amanpreet Singh', 'Joseph Chee Chang', 'Kyle Shih-Huang Lo', 'Luca Soldaini', 'Sergey Feldman', 'Mike D’Arcy', 'David Wadden', 'Matt Latzke', 'Jenna Sparks', 'Jena D. Hwang', 'Varsha Kishore', 'Minyang Tian', 'Pan Ji', 'Shengyan Liu', 'Hao Tong', 'Bohao Wu', 'Yanyu Xiong', 'Luke Zettlemoyer', 'Graham Neubig', 'Daniel S. Weld', 'Doug Downey', 'Wen-tau Yih', 'Pang Wei Koh', 'Hannaneh Hajishirzi']
year: 2026
venue: "Nature"
tags: ['Artificial Intelligence in Healthcare and Education', 'Biomedical Text Mining and Ontologies', 'Topic Modeling']
source: raw/applied/applied_2026_Synthesizing_scientific_l_s41586_025_10072_4.md
---

# Synthesizing scientific literature with retrieval-augmented language models
**제목(한글)**: 검색 증강 언어 모델을 활용한 과학 문헌 종합

**저자**: Akari Asai; Jacqueline He; Rulin Shao; Weijia Shi; Amanpreet Singh; Joseph Chee Chang; Kyle Shih-Huang Lo; Luca Soldaini; Sergey Feldman; Mike D’Arcy; David Wadden; Matt Latzke; Jenna Sparks; Jena D. Hwang; Varsha Kishore; Minyang Tian; Pan Ji; Shengyan Liu; Hao Tong; Bohao Wu; Yanyu Xiong; Luke Zettlemoyer; Graham Neubig; Daniel S. Weld; Doug Downey; Wen-tau Yih; Pang Wei Koh; Hannaneh Hajishirzi
**출처**: Nature, Vol.650, pp.857-863
**발행일**: 2026-02-04
**DOI**: https://doi.org/10.1038/s41586-025-10072-4

## 한국어 요약

**연구질문**: 대형 언어 모델(LLMs)을 활용해 4,500만 개 이상의 개방형 과학 논문들로부터 신뢰할 수 있는 학술 답변을 찾아내고 출처(Citation)를 정확하게 표기하는 방법은 무엇인가?

**방법론**:
- 4,500만 개의 논문 Passages를 인덱싱한 데이터 저장소와 검색 루프를 연동한 검색 증강 언어 모델 'OpenScholar' 설계
- 4개 도메인의 고난도 전문가 작성 쿼리 2,967개로 구성된 신규 평가 벤치마크 'ScholarQABench' 구축 및 GPT-4o 등과의 비교 평가

**주요 결과**:
- OpenScholar-8B 모델이 다중 논문 종합 태스크에서 GPT-4o를 6.1% 앞서는 정확도를 나타냄
- 특히 GPT-4o가 78~90%의 빈도로 출처를 왜곡하는 한계를 보인 것과 대조적으로 OpenScholar는 전문가 수준의 출처 표기 정확성을 확보함을 검증


## 초록 (원문)

Scientific progress depends on the ability of researchers to synthesize the growing body of literature. Can large language models (LLMs) assist scientists in this task? Here we introduce OpenScholar, a specialized retrieval-augmented language model (LM)1 that answers scientific queries by identifying relevant passages from 45 million open-access papers and synthesizing citation-backed responses. To evaluate OpenScholar, we develop ScholarQABench, the first large-scale multi-domain benchmark for literature search, comprising 2,967 expert-written queries and 208 long-form answers across computer science, physics, neuroscience and biomedicine. Despite being a smaller open model, OpenScholar-8B outperforms GPT-4o by 6.1% and PaperQA2 by 5.5% in correctness on a challenging multi-paper synthesis task from the new ScholarQABench. Although GPT-4o hallucinates citations 78–90% of the time, OpenScholar achieves citation accuracy on par with human experts. OpenScholar’s data store, retriever and self-feedback inference loop improve off-the-shelf LMs: for instance, OpenScholar-GPT-4o improves the correctness of GPT-4o by 12%. In human evaluations, experts preferred OpenScholar-8B and OpenScholar-GPT-4o responses over expert-written ones 51% and 70% of the time, respectively, compared with 32% for GPT-4o. We open-source all artefacts, including our code, models, data store, datasets and a public demo. A specialized, open-source, retrieval-augmented language model is introduced for answering scientific queries and synthesizing literature, the responses of which are shown to be preferred by human evaluations over expert-written answers.

## 키워드

Correctness, Inference, Benchmark (surveying), Language model, Task (project management), Citation

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

