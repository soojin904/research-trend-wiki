# 소셜 네트워크 분석 (Social Network Analysis, SNA)

개인·조직·개념 등의 관계 구조를 그래프로 모델링하고 분석하는 방법론.
사이람([[netminer\|NetMiner]])의 핵심 기술 도메인.

## 핵심 개념
- **노드(Node)**: 행위자 (사람, 조직, 키워드, 논문 등)
- **엣지(Edge)**: 관계 (친구 관계, 공저, 공출현 등)
- **방향성**: 방향 있음(directed) vs 없음(undirected)
- **가중치**: 관계의 강도

## 주요 분석 유형
| 분석 | 내용 | 관련 개념 |
|------|------|-----------|
| 중심성 분석 | 핵심 노드 탐색 | [[centrality\|centrality]] |
| 커뮤니티 탐지 | 군집 구조 발견 | community detection |
| 에고 네트워크 | 특정 노드의 지역 구조 | [[ego_network\|ego network]] |
| 이분 네트워크 | 두 유형 노드 간 관계 | bipartite network |
| 시간적 네트워크 | 시간에 따른 구조 변화 | temporal network |

## 이 위키의 SNA 응용 사례
| 논문 | SNA 응용 영역 |
|------|--------------|
| [[pages/papers/netminer/2022_jeon_social_network_health_elderly\|Jeon & Park (2022)]] | 우정 네트워크 → 건강 결과 |
| [[pages/papers/netminer/2022_park_digital_healthcare_network\|Park 외 (2022)]] | 뉴스 이해관계자 네트워크 |
| [[pages/papers/netminer/2022_morashti_sustainable_packaging\|Morashti 외 (2022)]] | 키워드 공출현 네트워크 |
| [[pages/papers/netminer/2021_kang_csr_ad_semantic_network\|강윤지 외 (2021)]] | 연구 키워드 [[semantic_network_analysis\|의미연결망]] |

## 인접 방법론
- [[topic_modeling\|토픽모델링]]: 텍스트 기반 SNA와 결합 → [[mixed_methods\|복합 방법론]]
- GNN: 딥러닝 기반 그래프 분석 (별도 페이지 필요)
- 통계 분석: SNA 지표를 독립변수로 활용

## 도구
- [[netminer\|NetMiner]]: SNA 전문 소프트웨어 (사이람)
- Gephi, UCINET, igraph (R), NetworkX (Python)
