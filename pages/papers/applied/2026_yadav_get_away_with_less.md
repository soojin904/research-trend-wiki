---
title: "Get away with less: Need of source side data curation to build parallel corpus for low resource Machine Translation"
authors: ['Saumitra Yadav', 'Manish Shrivastava']
year: 2026
venue: "ArXiv.org"
tags: ['Natural Language Processing Techniques', 'Topic Modeling', 'Text Readability and Simplification']
source: raw/applied/applied_2026_Get_away_with_less_Need_nodoi.md
---

# Get away with less: Need of source side data curation to build parallel corpus for low resource Machine Translation
**제목(한글)**: 더 적은 데이터로도 충분: 저자원 기계 번역을 위한 병렬 말뭉치 구축에서 소스 측 데이터 큐레이션의 필요성

## 한국어 요약

**연구질문**: 저자원(low-resource) 언어 기계 번역 시스템 훈련을 위한 병렬 말뭉치 구축 시, 소스 문장 선택 전략이 번역 품질에 미치는 영향은 무엇이며, 적은 데이터로도 최적의 성능을 달성할 수 있는 방법은 무엇인가?

**방법론**:
- 어휘·언어학적 특성을 기반으로 소스 문장을 선별하는 LALITA(Lexical And Linguistically Informed Text Analysis) 프레임워크 개발
- 기존 및 합성 데이터셋에서 복잡한 문장 위주로 훈련하는 전략 검증
- 영어-힌디어를 포함한 힌디어, 오디아어, 네팔어, 노르웨이 뉘노르스크어, 독일어 등 다수 언어 쌍에서 50K~800K 문장 규모로 성능 평가

**주요 결과**:
- LALITA가 여러 언어에 걸쳐 훈련 데이터 요구량을 절반 이상 감소시키면서 번역 품질 향상 달성
- 복잡한 소스 문장 중심 훈련이 번역 품질 향상에 효과적임을 모든 데이터 크기에서 확인

**저자**: Saumitra Yadav; Manish Shrivastava
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-01-13
**DOI**: 

## 초록 (원문)

Data curation is a critical yet under-researched step in the machine translation training paradigm. To train translation systems, data acquisition relies primarily on human translations and digital parallel sources or, to a limited degree, synthetic generation. But, for low-resource languages, human translation to generate sufficient data is prohibitively expensive. Therefore, it is crucial to develop a framework that screens source sentences to form efficient parallel text, ensuring optimal MT system performance in low-resource environments. We approach this by evaluating English-Hindi bi-text to determine effective sentence selection strategies for optimal MT system training. Our extensively tested framework, (Lexical And Linguistically Informed Text Analysis) LALITA, targets source sentence selection using lexical and linguistic features to curate parallel corpora. We find that by training mostly on complex sentences from both existing and synthetic datasets, our method significantly improves translation quality. We test this by simulating low-resource data availabilty with curated datasets of 50K to 800K English sentences and report improved performances on all data sizes. LALITA demonstrates remarkable efficiency, reducing data needs by more than half across multiple languages (Hindi, Odia, Nepali, Norwegian Nynorsk, and German). This approach not only reduces MT systems training cost by reducing training data requirement, but also showcases LALITA's utility in data augmentation.

## 키워드

Machine translation, Training set, Sentence, Selection (genetic algorithm), Translation (biology), Resource (disambiguation), Data modeling, Computational linguistics

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

