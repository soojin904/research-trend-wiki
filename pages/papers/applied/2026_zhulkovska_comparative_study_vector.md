---
title: "Comparative study of vector emotion classification in multilingual intelligent systems"
authors: ['I. Zhulkovska', 'O. Zhulkovskyi', 'D. Lebedkin', 'T. Yakovenko', 'E. Riabovolenko']
year: 2026
venue: "INFORMATICS AND MATHEMATICAL METHODS IN SIMULATION"
tags: ['Emotion and Mood Recognition', 'Sentiment Analysis and Opinion Mining', 'Face and Expression Recognition']
source: raw/applied/applied_2026_Comparative_study_of_vect_imms_v16_no2_263.md
---

# Comparative study of vector emotion classification in multilingual intelligent systems
**제목(한글)**: 다국어 지능형 시스템에서 벡터 감정 분류 모델의 비교 연구

**저자**: I. Zhulkovska; O. Zhulkovskyi; D. Lebedkin; T. Yakovenko; E. Riabovolenko
**출처**: INFORMATICS AND MATHEMATICAL METHODS IN SIMULATION, Vol.16, pp.263-271
**발행일**: 2026-03-30
**DOI**: https://doi.org/10.15276/imms.v16.no2.263

## 한국어 요약

**연구질문**: 다국어 비정형 텍스트에서 감정을 판별할 때, 기존 단일 레이블에서 다중 레이블 분류(MLC) 모델로 이전하는 것과 SBERT 벡터화 기법의 성능 효과는 무엇인가?

**방법론**:
- BitFit 파라미터 튜닝 및 인간 참여형(Human-in-the-Loop) 기법을 기반으로 다국어 SBERT 임베딩 분류 파이프라인 구축
- GoEmotions 말뭉치를 학습 데이터셋으로 다중 레이블 분류(MLC) 모델 실험
- 분류 정밀도와 재현율 간의 임계값 조절 스펙트럼 분석 및 추론 시간 측정

**주요 결과**:
- 다중 레이블 분류(MLC) 방식을 도입하여 감정 레이블 밀도를 18% 증가시켜 복합적 감정 상태를 정밀 포착
- 활성화 임계값 파라미터 조절을 통해 높은 재현율(0.62)에서 고정밀 정확도(0.83)까지 지능적으로 운용 지점을 선택할 수 있음을 검증
- 0.29초 이내의 응답 속도를 기록하여 실시간 감성 모니터링 시스템 아키텍처에 적합함을 확인


## 초록 (원문)

This study presents a systematic comparative analysis of single-vector and multi-vector emotion classification approaches using the SBERT architecture, evaluating the effectiveness of transitioning from classical single-label to multi-label classification models.A computational pipeline optimized with the BitFit strategy and Human-in-the-Loop methodology was developed, enabling the identification of complex ambivalent states in a multilingual environment.Experiments conducted on the GoEmotions corpus demonstrated that the MLC approach provides an 18% increase in the emotional label density (Ld = 1.18).It was established that the proposed architecture allows for adaptive management of the precision-recall trade-off via the activation threshold : from high recall (Recall = 0.62 at = 0.1) to precision-focused accuracy (Precision = 0.83 at = 0.7).The study also highlights that, in line with the research objective of evaluating multi-vector architectures for ambivalent emotional states, model outputs are sensitive to configuration choices: secondary emotional markers, such as Annoyance, may be under-or overrepresented depending on parameter settings, illustrating the importance of careful calibration to achieve reliable emotional coverage.The engineering implementation ensures a response latency of up to 0.29 s, meeting the requirements for real-time data processing.The results demonstrate that combining deep vectorization with flexible operating point calibration effectively supports the analysis of semantically complex texts.

## 키워드

Intelligent decision support system, Feature (linguistics), Support vector machine, Field (mathematics), Key (lock)

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

