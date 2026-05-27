---
title: "Potential and Pitfalls of Audio as Data for Political Research: Alignment, Features, and Classification Models"
authors: ['Rafael Mestre', 'Matt Ryan']
year: 2026
venue: "Political Analysis"
tags: ['Computational and Text Analysis Methods', 'Sentiment Analysis and Opinion Mining', 'Explainable Artificial Intelligence (XAI)']
source: raw/applied/applied_2026_Potential_and_Pitfalls_of_pan_2025_10031.md
---

# Potential and Pitfalls of Audio as Data for Political Research: Alignment, Features, and Classification Models
**제목(한글)**: 정치학 연구를 위한 데이터로서 오디오의 가능성과 한계: 정렬, 특징 및 분류 모델

**저자**: Rafael Mestre; Matt Ryan
**출처**: Political Analysis, Vol.None, pp.1-17
**발행일**: 2026-01-30
**DOI**: https://doi.org/10.1017/pan.2025.10031

## 한국어 요약

**연구질문**: 정치학 연구에서 오디오 데이터를 텍스트 데이터와 결합하여 다중 모드(Multimodal) 분석에 활용할 때 발생하는 도전 과제와 그 해결 방안은 무엇인가?

**방법론**:
- 1960년부터 2020년까지의 미국 대통령 후보 TV 토론 오디오 데이터셋 구축
- 피치 및 에너지를 포함한 저수준 기술자(LLD), 멜 주파수 캡스트럼 계수(MFCC), Wav2Vec 등의 오디오 임베딩/인코딩 기능 분석
- 강제 정렬, 음성 특성 분석, 임베딩 기반 분류 및 감정 인식 모델 구축을 통한 4가지 응용 연구 수행

**주요 결과**:
- MFCC를 이용한 오디오-텍스트 강제 정렬과 타임스탬프 생성을 통해 화자 정보를 정밀하게 식별할 수 있음을 보임
- Wav2Vec 임베딩이 정치인의 이산적 감정 상태 및 각성도(valence-arousal dominance) 분류에 우수함을 실증함
- 초보 및 기성 정치학 연구자들의 오디오 데이터 남용을 막기 위한 해석 주의점과 기술적 대안을 정립함


## 초록 (원문)

Abstract Political science is a field rich in multimodal information sources, from televised debates to parliamentary briefings. This paper bridges a gap between computer and political science in multimodal data analysis using audio. The adoption of multimodal analyses in political science (e.g., video/audio with text-as-data approaches) has been relatively slow due to unequal distribution of computational power and skills needed. We provide solutions to challenges encountered when analyzing audio, advancing the potential for multimodal data analysis in political science. Using a dataset of all televised U.S. presidential debates from 1960 to 2020, we focus on three features encountered when analyzing audio data: low-level descriptors (LLDs), such as pitch or energy; Mel-frequency cepstral coefficients (MFCCs); and audio embeddings/encodings, like Wav2Vec. We showcase four applications: (a) forced alignment of audio text using MFCCs, time-stamping transcripts, and speaker information; (b) speech characterization using LLDs; (c) custom-made classification models with audio embeddings and MFCCs; and (d) emotional recognition models using Wav2Vec for classification of discrete emotions and their valence-arousal dominance. We provide explanations to help understand how these features can be applied for different political research questions and advice on vigilance to naive interpretation, for both experienced researchers and those who want to start working with audio.

## 키워드

Field (mathematics), Presidential system, Focus (optics), Politics, Mel-frequency cepstrum, Power (physics)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

