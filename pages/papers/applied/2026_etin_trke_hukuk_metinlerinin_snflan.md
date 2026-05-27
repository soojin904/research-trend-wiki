---
title: "Türkçe Hukuk Metinlerinin Sınıflandırılması: Gözetimli Öğrenme ve Büyük Dil Modelleri"
authors: ['Eda Çetin', 'İlayda Kaya', 'Furkan Göz']
year: 2026
venue: "Pamukkale University Journal of Engineering Sciences"
tags: ['Artificial Intelligence in Law', 'Topic Modeling', 'Authorship Attribution and Profiling']
source: raw/applied/applied_2026_Trke_Hukuk_Metinlerinin_S_pajes_1868918.md
---

# Türkçe Hukuk Metinlerinin Sınıflandırılması: Gözetimli Öğrenme ve Büyük Dil Modelleri
**제목(한글)**: 터키어 법률 문서의 분류: 지도 학습과 대형 언어 모델

**저자**: Eda Çetin; İlayda Kaya; Furkan Göz
**출처**: Pamukkale University Journal of Engineering Sciences, Vol.None
**발행일**: 2026-04-25
**DOI**: https://doi.org/10.65206/pajes.1868918

## 한국어 요약

**연구질문**: 교착어(Eklemeli)적 특성으로 형태소 분석 및 NLP 처리가 까다로운 터키어 법률 판결문 텍스트에서 범죄 유형을 고정밀도로 자동 분류하는 최적의 머신러닝/딥러닝 모델 조합과 LLM 대비 실무적 한계는 무엇인가?

**방법론**:
- 웹 스크레이핑 기법을 사용해 터키 형사법원 판결문 중 7가지 범죄 유형을 나타내는 텍스트 데이터셋을 구축 및 전처리 수행
- TF-IDF와 FastText 피처 추출법을 활용하고 SVM, BiLSTM, BERT, RoBERTa, DistilBERT 분류기들을 비교 학습
- 고성능으로 튜닝된 SVM 모델과 Few-shot 기반의 GPT-4o-mini 모델 간의 실시간 미보지 데이터 추론 정확도 및 응답 속도/비용 비교 검증

**주요 결과**:
- Geleneksel makine öğrenmesi yöntemlerinden TF-IDF + SVM, %95.71 F1 skoru ile en yüksek performansı elde etmiştir.
- 실시간 미학습 데이터 테스트에서 SVM과 GPT-4o-mini는 동일하게 85.71%의 준수한 정확도를 나타냈으나, SVM이 밀리초(ms) 단위의 신속한 응답 속도와 제로 API 비용을 달성해 실무 대규모 법률 지원 도구로서 압도적인 효율성을 가짐을 검증함


## 초록 (원문)

Arka Plan—Hukuk alanında yapay zekânın, hem mevcut kurumlara entegre edilen destekleyici sistemler hem de tamamen yapay zekâ merkezli yeni nesil hukuk teknolojisi girişimleri şeklinde geliştiği görülmektedir. Ancak Türkiye özelinde hukuk teknolojileri alanındaki çalışmaların dünya literatürüne kıyasla oldukça sınırlı olduğu görülmektedir. Bu sınırlılık, Türkçenin eklemeli yapısının NLP uygulamaları için karmaşık dilbilimsel zorluklar oluşturmasıyla ilişkilendirilmektedir. Suç türü sınıflandırması hem hukuki araştırma süreçlerini hızlandırmak hem de benzer davaların tespitini kolaylaştırmak açısından kritik bir rol oynamaktadır.Amaç—Bu çalışmanın amacı, açık kaynaklı Türkçe ceza davası karar metinlerini kullanarak klasik makine öğrenmesi ve derin öğrenme tabanlı modellerin Türkçe hukuk terminolojisi üzerindeki performanslarını karşılaştırmalı olarak analiz etmek ve otomatik metin sınıflandırması için en uygun modeli belirlemektir. Ayrıca analizler sonucunda en yüksek başarımı gösteren model kullanılarak gerçek zamanlı bir sınıflandırma sistemi geliştirip ve sistemin uygulanabilirliği test edilmektir.Yöntem— Web kazıma kullanılarak Ceza Dairesi karar metinlerinden oluşan ve yedi farklı suç türünü içeren bir veri seti oluşturulmuştur. Veri seti oluşturulurken ilk olarak web sitesinden çekilen metinler incelenmiş ve yalnızca suç türü bilgisi içerenler filtrelenmiştir. Ardından, suç türleri belirlenerek bunlara göre metinler etiketlenmiştir. Anlamsal olarak benzer olan bazı sınıflar birleştirilmiştir. Son aşamada etiketli veri seti temizlenmiş, metinlerin içerisinde yer alan etiket bilgileri çıkarılmış ve çok kısa olan metinler veri setinden kaldırılmıştır. Oluşturulan nihai veri seti, yedi farklı yapay öğrenme modeli kullanılarak eğitilmiştir. Bu modeller; TF-IDF + Naive Bayes, TF-IDF + Logistic Regression, TF-IDF + SVM, FastText + SVM, FastText + BiLSTM, BERT, RoBERTa ve DistilBERT’tir. Model performansları doğruluk ve F1-skor ölçütleri kullanılarak karşılaştırılmıştır. Elde edilen sonuçlara göre en yüksek doğruluğu sağlayan FastText + SVM modeli ile üretken yapay zeka tabanlı GPT-4o-mini modeli, eğitim veri kümesinde yer almayan veriler üzerinde gerçek zamanlı olarak test edilmiştir.Bulgular—Geleneksel makine öğrenmesi yöntemlerinden TF-IDF + SVM, %95.71 F1 skoru ile en yüksek performansı elde etmiştir. SVM'in, TF-IDF gibi terim sıklığına dayalı özellik çıkarma yöntemi karar metinlerinde sıkça yer alan ve ayırt edici gücü yüksek anahtar kelimelerin etkili biçimde temsil etmesi sayesinde derin öğrenme modellerini geride bırakmıştır. Gerçek zamanlı test aşamasında eğitilmiş TF-IDF + SVM modeli ile az örnekli öğrenme yaklaşımı kullanılan GPT-4o-mini modeli eğitim veri kümesinde yer almayan veriler üzerinde karşılaştırılmıştır. İki yaklaşım da %85.71 doğruluk ile eşdeğer performans sergilemiştir. Ancak TFIDF + SVM milisaniyeler içinde yanıt üretirken, LLM tabanlı sistemlerin yanıt süresinin daha uzun olması ve API maliyetleri, gerçek zamanlı, büyük ölçekli uygulamalar açısından önemli bir farklılık olarak öne çıkmıştır.Sonuç—Yapay öğrenme modelleri kullanılarak yapılan sınıflandırmalarda TF-IDF + SVM yönteminin, Türk dava karar metinlerindeki suç türlerini sınıflandırmada etkili olduğu gözlemlenmiştir. Bu yöntem, yapay zeka destekli hukuk sistemlerinde karar destek mekanizmalarına entegre edilebilir. Gelecekteki çalışmalar, Türk hukuk dava metinlerini kullanarak daha büyük veri setleri üzerinde ve daha geniş suç türlerini kapsayan sınıflandırma yaklaşımlarını araştırabilir.

## 키워드

International law, Criminal law

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

