---
title: "ELLMW: an enhanced vision–language model for reliable text extraction from manually composed scripts"
authors: ['Dhivya Venkatesh', 'Brintha Rajakumari Sivaraj']
year: 2026
venue: "International Journal of Reconfigurable and Embedded Systems (IJRES)"
tags: ['Handwritten Text Recognition Techniques', 'Topic Modeling', 'Multimodal Machine Learning Applications']
source: raw/applied/applied_2026_ELLMW_an_enhanced_visionl_ijres_v15_i1_pp194_203.md
---

# ELLMW: an enhanced vision–language model for reliable text extraction from manually composed scripts
**제목(한글)**: ELLMW: 수기 스크립트로부터 신뢰할 수 있는 텍스트 추출을 위한 고도화된 시각-언어 모델

**저자**: Dhivya Venkatesh; Brintha Rajakumari Sivaraj
**출처**: International Journal of Reconfigurable and Embedded Systems (IJRES), Vol.15, pp.194-194
**발행일**: 2026-03-01
**DOI**: https://doi.org/10.11591/ijres.v15.i1.pp194-203

## 한국어 요약

**연구질문**: 노이즈가 많고 필체가 다양한 아날로그 손글씨 시험 답안지 이미지로부터 높은 의미 일관성과 낮은 에러율로 디지털 텍스트를 정확하게 추출할 수 있는가?

**방법론**:
- 이미지 잡음 제거, 이진화 및 기울기 교정(Skew correction)을 수행하는 지능형 전처리 모듈 설계
- 필기 궤적을 딥러닝 판독하는 CNN-LSTM 모델과 판독 결과의 오타 및 레이아웃을 문맥에 맞춰 교정하는 LLM 포스트 수정기를 융합한 ELLMW 프레임워크 개발
- 손글씨 답안지(HEAS) 데이터셋을 구축하여 GCV, EasyOCR, Tesseract 등과의 텍스트 판독 정확도 및 문자 에러율(CER) 비교 검증

**주요 결과**:
- ELLMW 모델이 문자 오차율 1.04% 및 최종 정확도 97.8%를 기록하여 기존 Google Cloud Vision 및 Tesseract 등 상용 OCR 도구 성능을 압도적으로 능가함을 증명
- 훼손되거나 꼬인 필체에서도 Context-aware 구조 교정을 통해 강건하고 안정적인 판독 복원력을 입증함


## 초록 (원문)

While conventional optical character recognition (OCR) systems can digitize text, they struggle with diverse handwriting styles, noisy inputs, and unstructured layouts, limiting their effectiveness. This study proposes enhanced large language model whisperer (ELLMW), a vision–language framework for accurate text extraction (TE) from fully handwritten scripts. The methodology integrates advanced preprocessing (noise reduction, binarization, and skew correction), deep learning–based handwriting recognition convolutional neural network–long short-term memory (CNN–LSTM), and LLM-based post-correction to ensure context-aware and structurally coherent outputs. The system converts scanned images, portable document formats (PDFs), and irregularly formatted answer sheets into machine-readable text, while automatically correcting errors in spelling, grammar, and layout. Experimental evaluation on a curated dataset of handwritten examination answer scripts (HEAS) demonstrates that ELLMW achieves 97.8% accuracy, 1.04%-character error rate (CER), and 3.24%-word error rate, outperforming widely used OCR tools including Tesseract, EasyOCR, Google Cloud Vision (GCV), PaddleOCR, ABBYY FineReader, and Transym OCR. The results highlight the model’s robustness across varying handwriting styles, noisy backgrounds, and complex document structures.

## 키워드

Scripting language, Optical character recognition, Preprocessor, Robustness (evolution), Skew, Handwriting, Handwriting recognition, Convolutional neural network

## 위키 연관

- [[pages/methods/topic_modeling|토픽모델링]]

## 메모

