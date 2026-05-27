---
title: "MultiModal Explainable AI and Blockchain Integration for Automated Halal Verification of Cosmetic Products"
authors: ['Endang Supriyati', 'Mohammad Iqbal', 'Tri Listyorini']
year: 2026
venue: "IIUM Engineering Journal"
tags: ['Halal products and consumer behavior', 'Sentiment Analysis and Opinion Mining', 'Identification and Quantification in Food']
source: raw/applied/applied_2026_MultiModal_Explainable_AI_iiumej_v27i2_4059.md
---

# MultiModal Explainable AI and Blockchain Integration for Automated Halal Verification of Cosmetic Products
**제목(한글)**: 화장품의 자동 할랄 검증을 위한 멀티모달 설명가능한 AI 및 블록체인 통합 시스템

**저자**: Endang Supriyati; Mohammad Iqbal; Tri Listyorini
**출처**: IIUM Engineering Journal, Vol.27, pp.175-188
**발행일**: 2026-05-10
**DOI**: https://doi.org/10.31436/iiumej.v27i2.4059

## 한국어 요약

**연구질문**: 소비자 신뢰를 높이기 위해 화장품 성분 표기 이미지 및 텍스트 데이터로부터 할랄(Halal) 인증 여부를 실시간 자동 심사하고, 결과를 무단 조작할 수 없게 보존할 방법은 무엇인가?

**방법론**:
- 화장품 라벨 이미지 OCR 텍스트와 수동 텍스트 데이터를 동시 수집
- 멀티모달 설명가능한 AI(MXAI)를 도입하여 제품 성분 분석 및 제로샷 분류(할랄, 하람, 슈바트 판별) 알고리즘 수행
- 결과 판단 근거(SHAP 기여값)를 확보하고, 최종 검증 문서를 SHA-256 해시로 변환하여 블록체인 머클 트리(Merkle root)에 기록하고 사용자에게 QR코드 다운로드 제공

**주요 결과**:
- 5분할 교차 검증 평가 결과, 제안하는 하이브리드 검증 모델이 할랄 분류 성분 테스트에서 정확도 94.5%를 획득하여 baseline 모델 성능을 3.3% 상회함
- 공급망 전반에 걸쳐 조작 불가능하고 투명한 자동 할랄 공인 검증 인프라 구축의 실현 가능성을 증명함


## 초록 (원문)

This research develops a framework that integrates blockchain technology and MXAI (Multimodal Explainable Artificial Intelligence) to automate the authentication and verification of halal cosmetic products. Two data sources were used: text extracted by OCR (Optical Character Recognition) and text manually input from cosmetic labels. After the pre-processing stage, the text data are analyzed using zero-shot classification to determine the inspection results, namely halal, haram, or syubhat. The inspection is conducted using MXAI, with decisions based on confidence scores and SHAP values. The inspection results are converted into digital reports as SHA-256 hashes and stored as Merkle roots on the blockchain, allowing users to download certificates as QR codes. The halal status experiment on the cosmetics dataset achieved an accuracy of 94.5% for classification, with a 3.3% improvement over baseline models, evaluated using stratified 5-fold cross-validation. This system enhances transparency, accountability, and public trust in automated halal certification. The contribution of this research is the integration of MXAI and blockchain technology into a single intelligent halal verification system, which can be extended to other supply chain sectors. ABSTRAK: Kajian ini menggabungkan teknologi rantaian blok dan MXAI (Kecerdasan Buatan Penjelasan Multimodal) bagi automasi dan jaminan pengesahan produk kosmetik halal. Dua sumber data digunakan: teks yang diekstrak oleh OCR (Pengesahan Optik Karakter) dan teks yang dimasukkan secara manual daripada label kosmetik. Selepas peringkat pra-pemprosesan, data teks dianalisis menggunakan klasifikasi sifar-tembakan bagi menentukan keputusan pemeriksaan, iaitu halal, haram, atau syubhat. Pemeriksaan dijalankan menggunakan MXAI, dengan keputusan berdasarkan skor keyakinan dan nilai SHAP. Keputusan pemeriksaan ditukar menjadi laporan digital dalam bentuk hash SHA-256 dan disimpan sebagai punca Merkle pada rantaian blok, membolehkan pengguna memuat turun sijil dalam bentuk kod QR. Eksperimen status halal pada set data kosmetik menunjukkan ketepatan 94.5% untuk prestasi pengelasan, dengan peningkatan 3.3% berbanding model asas, dinilai menggunakan pengesahan silang 5-lipatan berstrata. Sistem ini meningkatkan ketelusan, akauntabiliti, dan kepercayaan awam dalam pensijilan halal automatik. Sumbangan penyelidikan ini ialah melalui integrasi MXAI dan teknologi rantaian blok dalam satu sistem pengesahan halal pintar tunggal, yang boleh diperluas kepada sektor rantaian bekalan lain.

## 키워드

Hash function, Blockchain, MD5, Authentication (law), Download, Font

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

