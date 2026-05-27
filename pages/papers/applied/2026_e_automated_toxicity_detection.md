---
title: "Automated Toxicity Detection in Online platform"
authors: ['Reshma E']
year: 2026
venue: "International Journal for Research in Applied Science and Engineering Technology"
tags: ['Hate Speech and Cyberbullying Detection', 'Spam and Phishing Detection', 'Sentiment Analysis and Opinion Mining']
source: raw/applied/applied_2026_Automated_Toxicity_Detect_ijraset_2026_82039.md
---

# Automated Toxicity Detection in Online platform
**제목(한글)**: 온라인 플랫폼에서의 자동화된 유해성 탐지

**저자**: Reshma E
**출처**: International Journal for Research in Applied Science and Engineering Technology, Vol.14, pp.1632-1637
**발행일**: 2026-05-12
**DOI**: https://doi.org/10.22214/ijraset.2026.82039

## 한국어 요약

**연구질문**: 단순 단어 필터링 방식의 오탐률을 줄이고 실제 문맥 정보(Context)를 종합 반영하여, 소셜 미디어 상의 유해·악성 텍스트를 정확하게 실시간 자동 검출하는 모델 파이프라인은 어떻게 구성되는가?

**방법론**:
- 광학문자판독(OCR) 및 음성인식(Speech-to-Text) 모듈을 사용해 이미지와 음성 소스를 정형 텍스트로 변환하는 멀티모달 전처리 구성
- REGEX 규칙 필터링, TextBlob 기반의 감성 점수 계산 및 BERT 기반의 미세 맥락 파싱 기술을 결합하여 복합적인 유해 스코어(Toxic score) 산출 모델 개발

**주요 결과**:
- 텍스트 맥락 정보를 입체적으로 반영하는 BERT 기반 감지가 기존 단어 사전 필터링 대비 오탐률(False Positives)을 유의미하게 경감시킴을 검증함
- 대규모 실시간 온라인 커뮤니티 정화 및 사용자 보호 피드백 경고 시스템을 위한 확장성 높은 실무 모듈을 확립함


## 초록 (원문)

The growth of online communication tools has caused a rise in the number of instances of toxic, abusive and harmful content is now a real issue for the safety of users and their digital well-being. Old School moderation practices based on the use of keyword-based filtering are generally not able to identify context and therefore lead to poor identification of content. This paper discusses an automated AI-based toxicity detection system which will be able to accurately identify, in real-time, the nature of what someone is posting, taking context into account and making use of various forms of data to help make this determination possible. The proposed system uses a hybrid model of Natural Language Processing and Deep Learning techniques to analyze multi-modal sources of data; including text, image and voice. Image data and voice data are converted to text format through Optical Character Recognition (OCR) and Speech-to-Text methods. The converted data then undergoes "preprocessing" before being evaluated using multiple techniques for text analysis, i.e. REGEX rule based filtering, TextBlob (for sentiment analysis), and BERT (for context analysis). The ability to evaluate the data at multiple layers of evaluation allows for very precise toxic scoring of the data which then allows for the automated moderation of that data through content filtering, warning generation, and user feedback. The results of the experimental analysis indicate that the proposed system has improved accuracy in detecting toxicity, reduced false positives, and improved the quality of user interactions. Therefore, it can be concluded that the proposed system is a scalable, intelligent and efficient way to create safe digital environments while also addressing the shortcomings of previous moderation techniques

## 키워드

Context (archaeology), Identification (biology), Image (mathematics), Data quality, Quality (philosophy), Natural language, Deep learning

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

