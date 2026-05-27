---
title: "Penerapan SVM dan Regresi untuk Prediksi Intensitas Sentimen Pemilu Presiden Indonesia"
authors: ['Valen Rionald', 'Syafrial Fachri Pane', 'Muhammad Yusril Helmi Setyawan']
year: 2026
venue: "InComTech Jurnal Telekomunikasi dan Komputer"
tags: ['Multimedia Learning Systems', 'Data Mining and Machine Learning Applications', 'Sentiment Analysis and Opinion Mining']
source: raw/applied/applied_2026_Penerapan_SVM_dan_Regresi_incomtech_v15i3_28525.md
---

# Penerapan SVM dan Regresi untuk Prediksi Intensitas Sentimen Pemilu Presiden Indonesia
**제목(한글)**: 인도네시아 대통령 선거의 감성 강도 예측을 위한 SVM 및 회귀분석 적용

**저자**: Valen Rionald; Syafrial Fachri Pane; Muhammad Yusril Helmi Setyawan
**출처**: InComTech Jurnal Telekomunikasi dan Komputer, Vol.15, pp.186-204
**발행일**: 2026-01-02
**DOI**: https://doi.org/10.22441/incomtech.v15i3.28525

## 한국어 요약

**연구질문**: 인도네시아 대선 기간 중 트위터 상에서 발생하는 대중의 감성 반응과 감정의 강도를 BERT 모델, SVM, 릿지 회귀를 결합한 하이브리드 방식으로 어떻게 정확하게 분류하고 정량화할 수 있는가?

**방법론**:
- 인도네시아 대선 관련 트위터 데이터를 수집하고 텍스트 정제 및 정규화 수행
- 클래스 불균형 문제를 해소하기 위해 SMOTE 오버샘플링을 적용하였으며, BERT의 텍스트 특징 표상 추출 성능에 SVM과 릿지 회귀(Ridge Regression)를 결합하여 감성 강도를 분석

**주요 결과**:
- 하이브리드 모델이 클래스 불균형 하에서도 높은 정확도, 정밀도, 재현율, F1 점수를 보임을 확인
- 세 후보(아니스 바스웨단 53.1%, 프라보워 수비안토 63.5%, 간자르 프라노워 62.9%)에 대해 공통적으로 중립적인 감성 비중이 가장 높게 분석됨


## 초록 (원문)

Dalam konteks pemilihan umum presiden Indonesia, analisis sentimen publik melalui media sosial merupakan alat yang penting untuk memahami persepsi dan reaksi masyarakat terhadap calon presiden dan kebijakan mereka. Studi ini mengembangkan model hybrid yang mengintegrasikan Support Vector Machine (SVM) dan Ridge Regression, menggunakan library BERT untuk memprediksi intensitas sentimen dari data Twitter. Pendekatan ini dirancang untuk mengatasi tantangan variabilitas ekspresi dan ambiguitas bahasa, yang sering kali mempersulit interpretasi data sentimen dengan tepat. Penelitian ini menggunakan teknik preprocessing yang komprehensif, termasuk pembersihan teks dan normalisasi data, serta penerapan teknik Synthetic Minority Over-sampling Technique (SMOTE) untuk menangani ketidakseimbangan kelas dalam dataset. Hasil dari penelitian ini menunjukkan bahwa model hybrid dapat mencapai tingkat akurasi, presisi, recall, dan F1-Score yang tinggi dengan tiga rasio yang berbeda, menegaskan keefektifan model dalam mengklasifikasikan dan mengukur intensitas sentimen. Temuan menunjukkan bahwa kombinasi SVM dan regresi, didukung dengan analisis BERT, efektif dalam mengklasifikasikan dan mengukur intensitas sentimen secara akurat. Hasil intensitas yang dijelaskan pada gambar 11 untuk kandidat Anies Baswedan mayoritas sentimen adalah netral sebesar 53.1%. Selanjutnya, pada gambar 12 untuk kandidat Prabowo Subianto netral sebesar 63.5% dan gambar 13 untuk kandidat Ganjar Pranowo dengan 62.9%.

## 키워드

Population

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

