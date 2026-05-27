---
title: "Latent Diffusion Model for Social Recommendation"
authors: ['Qinyang He', 'Yihao Zhang', 'Kaibei Li', 'Xiaokang Li', 'Wei Zhou']
year: 2026
publication_date: 2026-02-04
venue: "IEEE Transactions on Systems Man and Cybernetics Systems"
volume: "56"
issue: "5"
pages: "3355-3369"
doi: "https://doi.org/10.1109/tsmc.2026.3657816"
oa_status: "closed"
openalex_id: "https://openalex.org/W7127602903"
query_keyword: "social network"
tags: ['Recommender Systems and Techniques', 'Complex Network Analysis Techniques', 'Advanced Graph Neural Networks']
keywords: ['Social network (sociolinguistics)', 'Cluster analysis', 'Leverage (statistics)', 'Robustness (evolution)', 'Collaborative filtering', 'Scarcity', 'Relation (database)', 'Latent variable']
source: openalex-keyword
---

# Latent Diffusion Model for Social Recommendation

**저자**: Qinyang He; Yihao Zhang; Kaibei Li; Xiaokang Li; Wei Zhou
**출처**: IEEE Transactions on Systems Man and Cybernetics Systems, Vol.56 No.5, pp.3355-3369
**발행일**: 2026-02-04
**DOI**: https://doi.org/10.1109/tsmc.2026.3657816
**수집 키워드**: social network

## 초록

Social recommendations assume that users with social networks tend to have similar pReferences and leverage the social network of users to improve personalized recommendations. However, the scarcity of interactive and social data, along with the presence of irrelevant or fake social connections, poses challenges in accurately predicting user preferences. Recent research has leveraged diffusion models to eliminate invalid social connections from the social relation graph, but this approach incurs high resource costs for large-scale item prediction. To address these issues, we propose an efficient latent space diffusion model for social recommendation named latent diffusion method for social recommendation (LDSR), which can reduce resource costs by clustering user social relationships and performing diffusion in a low-dimensional space. During the diffusion process, we inject and eliminate Gaussian noise and residuals in multiple steps, enhancing the model’s ability to recognize noise while ensuring output diversity and determinism. Additionally, we design a reconstruction strategy to capture latent social relationships, which helps to densify the social relation graph. The nonsmooth nature of the latent space can disrupt downstream task outputs, so we introduce variation constraints to smooth the latent space, reducing the impact of latent perturbations during generation. Furthermore, we incorporate user-item collaborative information to guide the reverse process, enhancing the controllability of the generated content to provide reasonable denoising. Extensive experiments on four publicly available datasets demonstrate that LDSR outperforms the state-of-the-art models, exhibiting superior training efficiency, robustness against sparsity and noise, and enhanced interpretability.

## 키워드

Social network (sociolinguistics), Cluster analysis, Leverage (statistics), Robustness (evolution), Collaborative filtering, Scarcity, Relation (database), Latent variable, Resource (disambiguation)

## 주제 분류 (OpenAlex Topics)

- Recommender Systems and Techniques (score: 0.794)
- Complex Network Analysis Techniques (score: 0.049)
- Advanced Graph Neural Networks (score: 0.028)

## 메모

