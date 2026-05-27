---
title: "Prophetic Authorial Style Modeling for Detecting Fabricated Hadiths Using AraBERT"
authors: ['Mohammed Shaaban', 'Ayman Elshenawy', 'Shehab Gamal el-Din']
year: 2026
venue: "Journal of Computing & Biomedical Informatics"
tags: ['Text and Document Classification Technologies', 'Topic Modeling', 'Sentiment Analysis and Opinion Mining']
source: raw/applied/applied_2026_Prophetic_Authorial_Style_1315.md
---

# Prophetic Authorial Style Modeling for Detecting Fabricated Hadiths Using AraBERT
**제목(한글)**: AraBERT를 활용한 위조 하디스 감지를 위한 예언자 저술 스타일 모델링

**저자**: Mohammed Shaaban; Ayman Elshenawy; Shehab Gamal el-Din
**출처**: Journal of Computing & Biomedical Informatics, Vol.10
**발행일**: 2026-03-01
**DOI**: https://doi.org/10.56979/1002/2026/1315

## 한국어 요약

**연구질문**: 구전 전승자 계보(Isnad)에 의존하지 않고, 예언자의 고유 문체(Kalām al-Nabī) 텍스트 자체만을 딥러닝 분석하여 위조된 하디스(Hadith, 예언자의 언행록)를 판별할 수 있는가?

**방법론**:
- 신뢰성 있는 진본(Sahih)과 위조본(Mawdu) 하디스 텍스트로 구성된 균형 잡힌 학습 데이터셋 수집
- 아랍어 자연어 처리에 고도화된 AraBERT 모델을 기반으로 하디스 본문(Matn)만을 학습시키는 문체 분석 미세 조정 수행
- ROC-AUC 등의 지표로 분류 성능 평가

**주요 결과**:
- 텍스트 문체 모델 분석만으로도 위조 하디스를 87%의 높은 정확도와 ROC-AUC 0.92라는 신뢰도 높은 판별력을 보이며 검출에 성공
- 향후 이 딥러닝 문체 모델이 전통적인 고증 연구를 보조하는 실무적 인공지능 검증 보조 도구로 유용하게 기능할 수 있음을 규명


## 초록 (원문)

Identifying the authenticity of the Hadiths attributed to the Messenger of Allah (ﷺ) is a science, known as "The Science of Hadith Terminology" (ʿIlm Muṣṭalaḥ al-Ḥadīth), This science establishes the principles and rules used to evaluate Prophetic Hadiths in terms of authenticity and acceptability by examining both the chain of narration (Isnad) and the text of the Hadith (Matn), as well as the reliability and qualifications of narrators, This research presents a deep learning–based approach for detecting fabricated (Mawdu’) Hadiths using Matn-only analysis without dependence on narrators’ chains, Our methodology focuses exclusively on the Prophetic speech (Kalām al-Nabī) (ﷺ) within the text, We fine-tune a pre-trained Arabic language model (AraBERT) on a carefully curated and balanced dataset of authentic (Sahih) and fabricated (Mawḍūʿ) Hadith texts. Experimental results show that the proposed approach succeeds in detecting fabricated hadith with an accuracy of 87%, and ROC-AUC of 0.92. This work emphasizes that the model is intended as an auxiliary analytical aid, and not a replacement for traditional scholarly verification.

## 키워드

Reliability (semiconductor), Narrative, Style (visual arts), Arabic, Work (physics)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

