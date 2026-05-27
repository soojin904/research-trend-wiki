---
title: "Latent Diffusion Model for Social Recommendation"
authors: ['Qinyang He', 'Yihao Zhang', 'Kaibei Li', 'Xiaokang Li', 'Wei Zhou']
year: 2026
venue: "IEEE Transactions on Systems Man and Cybernetics Systems"
tags: ['Recommender Systems and Techniques', 'Complex Network Analysis Techniques', 'Advanced Graph Neural Networks']
source: raw/applied/applied_2026_Latent_Diffusion_Model_fo_tsmc_2026_3657816.md
---

# Latent Diffusion Model for Social Recommendation
**제목(한글)**: 사회적 추천을 위한 잠재 디퓨전 모델

**저자**: Qinyang He; Yihao Zhang; Kaibei Li; Xiaokang Li; Wei Zhou
**출처**: IEEE Transactions on Systems Man and Cybernetics Systems, Vol.56, pp.3355-3369
**발행일**: 2026-02-04
**DOI**: https://doi.org/10.1109/tsmc.2026.3657816

## 한국어 요약

**연구질문**: 소셜 데이터의 극심한 희소성(Sparsity)과 가짜/무관한 친구 연결 관계 노이즈를 제어하면서, 대규모 사용자-아이템 협업 추천을 고효율 저비용으로 수행하는 디퓨전(Diffusion) 생성 모델은 어떻게 구축하는가?

**방법론**:
- 고차원 소셜 관계망을 클러스터링하여 저차원 잠재 공간(Latent Space)으로 축소해 디퓨전 연산을 수행하는 LDSR(Latent Diffusion for Social Recommendation) 모델 제안
- 가우시안 노이즈 주입 및 단계별 제거를 거치는 잔차 제거 기법 탑재
- 잠재 공간의 비균일성을 막기 위해 변분 제약 조건(Variation constraints)을 도입하고 사용자-아이템 협업 정보 필터 가이드를 설계

**주요 결과**:
- 4개 표준 벤치마크 데이터 실험 결과, LDSR 모델은 소셜 노이즈와 데이터 희소성이 강한 조건 하에서도 기존 최첨단 추천 모델들의 예측 정밀도를 능가함
- 저차원 잠재 공간 디퓨전을 유도함으로써 모델 학습 연산 효율하고 추천 아이템의 해석력(interpretability)을 비약적으로 개선함


## 초록 (원문)

Social recommendations assume that users with social networks tend to have similar pReferences and leverage the social network of users to improve personalized recommendations. However, the scarcity of interactive and social data, along with the presence of irrelevant or fake social connections, poses challenges in accurately predicting user preferences. Recent research has leveraged diffusion models to eliminate invalid social connections from the social relation graph, but this approach incurs high resource costs for large-scale item prediction. To address these issues, we propose an efficient latent space diffusion model for social recommendation named latent diffusion method for social recommendation (LDSR), which can reduce resource costs by clustering user social relationships and performing diffusion in a low-dimensional space. During the diffusion process, we inject and eliminate Gaussian noise and residuals in multiple steps, enhancing the model’s ability to recognize noise while ensuring output diversity and determinism. Additionally, we design a reconstruction strategy to capture latent social relationships, which helps to densify the social relation graph. The nonsmooth nature of the latent space can disrupt downstream task outputs, so we introduce variation constraints to smooth the latent space, reducing the impact of latent perturbations during generation. Furthermore, we incorporate user-item collaborative information to guide the reverse process, enhancing the controllability of the generated content to provide reasonable denoising. Extensive experiments on four publicly available datasets demonstrate that LDSR outperforms the state-of-the-art models, exhibiting superior training efficiency, robustness against sparsity and noise, and enhanced interpretability.

## 키워드

Social network (sociolinguistics), Cluster analysis, Leverage (statistics), Robustness (evolution), Collaborative filtering, Scarcity, Relation (database), Latent variable

## 위키 연관

- [[pages/concepts/social_network_analysis|SNA]]

## 메모

