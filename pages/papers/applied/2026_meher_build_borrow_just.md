---
title: "Build, Borrow, or Just Fine-Tune? A Political Scientist's Guide to Choosing NLP Models"
authors: ['Shreyas Meher']
year: 2026
venue: "ArXiv.org"
tags: ['Computational and Text Analysis Methods', 'Terrorism, Counterterrorism, and Political Violence', 'Misinformation and Its Impacts']
source: raw/applied/applied_2026_Build_Borrow_or_Just_Fine_nodoi.md
---

# Build, Borrow, or Just Fine-Tune? A Political Scientist's Guide to Choosing NLP Models

**제목(한글)**: 구축, 차용, 또는 미세 조정? 정치학자를 위한 NLP 모델 선택 가이드

## 한국어 요약

**연구질문**: 정치학자들이 NLP 모델을 선택할 때 성능, 비용, 전문성 간의 트레이드오프를 어떻게 탐색해야 하는가? 연구 질문에 따라 특화된 모델이 필요한 시점과 미세 조정된 일반 모델로 충분한 시점은 언제인가?

**방법론**:
- 갈등 사건 분류(conflict event classification)를 테스트 케이스로 활용
- ModernBERT를 Global Terrorism Database(GTD)에 미세 조정(fine-tune)하여 Confli-mBERT 생성
- 도메인 특화 사전 훈련 모델인 ConfliBERT와 Confli-mBERT의 성능 비교

**주요 결과**:
- Confli-mBERT의 정확도(75.46%)는 ConfliBERT(79.34%)보다 낮음.
- 폭탄 테러/폭발 및 납치 등 빈번한 사건 유형에서는 두 모델의 성능 차이가 미미함.
- 성능 차이는 전체 사건의 2% 미만을 차지하는 희귀 사건 범주에서 주로 나타남.
- 모델 선택은 클래스 유병률(class prevalence), 오류 허용치(error tolerance), 가용 자원(available resources)의 교차점에 따라 달라짐.

**저자**: Shreyas Meher
**출처**: ArXiv.org, Vol.None
**발행일**: 2026-03-10
**DOI**: 

## 초록 (원문)

Political scientists increasingly face a consequential choice when adopting natural language processing tools: build a domain-specific model from scratch, borrow and adapt an existing one, or simply fine-tune a general-purpose model on task data? Each approach occupies a different point on the spectrum of performance, cost, and required expertise, yet the discipline has offered little empirical guidance on how to navigate this trade-off. This paper provides such guidance. Using conflict event classification as a test case, I fine-tune ModernBERT on the Global Terrorism Database (GTD) to create Confli-mBERT and systematically compare it against ConfliBERT, a domain-specific pretrained model that represents the current gold standard. Confli-mBERT achieves 75.46% accuracy compared to ConfliBERT's 79.34%. Critically, the four-percentage-point gap is not uniform: on high-frequency attack types such as Bombing/Explosion (F1 = 0.95 vs. 0.96) and Kidnapping (F1 = 0.92 vs. 0.91), the models are nearly indistinguishable. Performance differences concentrate in rare event categories comprising fewer than 2% of all incidents. I use these findings to develop a practical decision framework for political scientists considering any NLP-assisted research task: when does the research question demand a specialized model, and when does an accessible fine-tuned alternative suffice? The answer, I argue, depends not on which model is "better" in the abstract, but on the specific intersection of class prevalence, error tolerance, and available resources. The model, training code, and data are publicly available on Hugging Face.

## 키워드

Event (particle physics), Intersection (aeronautics), Task (project management), Politics, Point (geometry), Class (philosophy), Face (sociological concept), Terrorism

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

