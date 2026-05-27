---
title: "The Moral Foundations Reddit Corpus"
authors: ['Jackson Trager', 'Alireza S. Ziabari', 'Elnaz Rahmati', 'Aida Mostafazadeh Davani', 'Preni Golazizian', 'Farzan Karimi-Malekabadi', 'Ali S. Omrani', 'Zhihe Li', 'Brendan Kennedy', 'Georgios Chochlakis', 'Nils Karl Reimer', 'Melissa Reyes', 'Kelsey Cheng', 'Mellow Wei', 'Christina Merrifield', 'Arta Khosravi', 'Evans Alvarez', 'Morteza Dehghani']
year: 2026
venue: ""
tags: ['Hate Speech and Cyberbullying Detection', 'Sentiment Analysis and Opinion Mining', 'Misinformation and Its Impacts']
source: raw/applied/applied_2026_The_Moral_Foundations_Red_2b6xmbq3kphf.md
---

# The Moral Foundations Reddit Corpus
**제목(한글)**: 도덕성 기반 레딧(Reddit) 코퍼스 데이터셋

**저자**: Jackson Trager; Alireza S. Ziabari; Elnaz Rahmati; Aida Mostafazadeh Davani; Preni Golazizian; Farzan Karimi-Malekabadi; Ali S. Omrani; Zhihe Li; Brendan Kennedy; Georgios Chochlakis; Nils Karl Reimer; Melissa Reyes; Kelsey Cheng; Mellow Wei; Christina Merrifield; Arta Khosravi; Evans Alvarez; Morteza Dehghani
**출처**: , Vol.None, pp.6383-6407
**발행일**: 2026-04-30
**DOI**: https://doi.org/10.63317/2b6xmbq3kphf

## 한국어 요약

**연구질문**: 온라인 상의 주관적인 도덕 프레임과 감성 어조를 기계학습으로 고밀도 판별하기 위해, 기존 트위터 데이터셋의 한계를 넘어 대화 맥락이 풍부한 레딧 데이터셋을 어떻게 설계하는가?

**방법론**:
- 12개 다양한 레딧 서브레딧 커뮤니티에서 추출한 16,123개의 영어 댓글 수집
- 3인의 훈련된 코더를 투입해 도덕성 기반 이론(MFT)의 8대 핵심 가치(돌봄, 비례성, 평등, 성결, 충성 등)에 맞춰 교차 어노테이션 수행
- Llama3-8B 및 Ministral-8B 등의 생성형 모델 퓨샷 성능과 인코더 전용 버트(BERT) 미세 조정 모델의 성능 비교

**주요 결과**:
- 주관성과 함축적 뉘앙스가 가득한 도덕 분류 태스크에서, 최신 LLM들이 미세 조정된 BERT 기반 인코더 성능에 여전히 뒤처짐을 통계 규명하여 도덕 지향 AI 얼라인먼트 검증 데이터로서의 독보적 가치를 확립


## 초록 (원문)

Moral framing and sentiment can affect a variety of online and offline behaviors, including donation, environmental action, political engagement, and protest. Various computational methods in Natural Language Processing (NLP) have been used to detect moral sentiment from textual data, but achieving strong performance in such subjective tasks requires large, hand-annotated datasets. Previous corpora annotated for moral sentiment have proven valuable, and have generated new insights both within NLP and across the social sciences, but have been limited to Twitter. To facilitate improving our understanding of the role of moral rhetoric, we present the Moral Foundations Reddit Corpus, a collection of 16,123 English Reddit comments that have been curated from 12 distinct subreddits, hand-annotated by at least three trained annotators for 8 categories of moral sentiment (i.e., Care, Proportionality, Equality, Purity, Authority, Loyalty, Thin Morality, Implicit/Explicit Morality) based on the updated Moral Foundations Theory (MFT) framework. We evaluate baselines using large language models (Llama3-8B, Ministral-8B) in zero-shot, few-shot, and PEFT (Parameter-Efficient Fine-Tuning) settings, comparing their performance to fine-tuned encoder-only models like BERT (Bidirectional Encoder Representations from Transformers). The results show that LLMs continue to lag behind fine-tuned encoders on this subjective task, underscoring the ongoing need for human-annotated moral corpora for AI alignment evaluation. Keywords: moral sentiment annotation, moral values, moral foundations theory, multi-label text classification, large language models, benchmark dataset, evaluation and alignment resource

## 키워드

Morality, Framing (construction), Sentiment analysis, Computer science, Social media, Loyalty, Rhetoric, Politics

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

