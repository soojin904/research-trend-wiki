# -*- coding: utf-8 -*-
import os

def process_file(path, title_ko, rq, methods, results):
    with open(path, 'rb') as f:
        content = f.read().decode('utf-8')

    lines = content.split('\r\n')
    h1_idx = None
    abstract_idx = None
    has_ko = False
    for i, line in enumerate(lines):
        if line.startswith('# ') and h1_idx is None:
            h1_idx = i
        if line.strip() == '## 초록':
            abstract_idx = i
        if '## 한국어 요약' in line:
            has_ko = True

    if has_ko:
        print(f'SKIP (already has 한국어 요약): {os.path.basename(path)}')
        return False

    if h1_idx is None:
        print(f'ERROR: no H1 in {os.path.basename(path)}')
        return False

    if abstract_idx is None:
        print(f'ERROR: no abstract in {os.path.basename(path)}')
        return False

    # Build Korean section lines
    ko_section = []
    ko_section.append('')
    ko_section.append('## 한국어 요약')
    ko_section.append('')
    ko_section.append('**연구질문**: ' + rq)
    ko_section.append('')
    ko_section.append('**방법론**:')
    for m in methods:
        ko_section.append('- ' + m)
    ko_section.append('')
    ko_section.append('**주요 결과**:')
    for r in results:
        ko_section.append('- ' + r)
    ko_section.append('')

    # Reconstruct lines
    new_lines = []
    for i, line in enumerate(lines):
        if i == h1_idx:
            new_lines.append(line)
            new_lines.append('**제목(한글)**: ' + title_ko)
        elif line.strip() == '## 초록':
            for kl in ko_section:
                new_lines.append(kl)
            new_lines.append('## 초록 (원문)')
        else:
            new_lines.append(line)

    new_content = '\r\n'.join(new_lines)
    with open(path, 'wb') as f:
        f.write(new_content.encode('utf-8'))
    print(f'Done: {os.path.basename(path)}')
    return True


BASE = r'D:\soojin\wiki\pages\papers'

papers = [
    {
        'path': os.path.join(BASE, '2021_tpfer_order_recall_and.md'),
        'title_ko': '정서적 네트워크 데이터 수집에서 알터 회상 순서와 친밀감의 의미',
        'rq': '응답자들이 정서적 이름 생성기(affective name generator)를 사용할 때 어떤 순서로 알터를 회상하며, "친밀감"의 의미를 어떻게 해석하는가?',
        'methods': [
            '발성 사고법(thinking-aloud method)을 활용한 질적 분석',
            '위계적 매핑 기법(hierarchical mapping technique) 적용',
            '알터 회상 패턴 및 친밀감 해석 방식 귀납적 분류',
        ],
        'results': [
            '알터 회상 순서에서 세 가지 패턴 식별: 친밀감 우선 스키마, 역할/초점 우선 스키마, 분산 스키마',
            '친밀감의 의미는 관계 속성, 문화적 맥락, 관계 역학 등 다양하게 해석됨',
            '친밀감 해석 방식과 회상 패턴 간 유의미한 연관성 확인',
            '회상 패턴은 응답자의 사회경제적 지위에 따라 차이 발생',
        ],
    },
    {
        'path': os.path.join(BASE, '2021_keuchenius_adoption_and_adaptation.md'),
        'title_ko': '채택과 적응: 그라노베터 약한 연결 가설 확산에 관한 계산적 사례 연구',
        'rq': '그라노베터의 약한 연결 강도(Strength of Weak Ties) 가설은 학문 공동체를 통해 어떻게 확산되었으며, 서로 다른 커뮤니티들은 이 가설을 어떻게 변형·적용하였는가?',
        'methods': [
            '인용 네트워크 분석(Web of Science 데이터 기반)',
            '토픽 모델링(topic modeling)',
            '확산 네트워크 질적 정독(close reading) 결합',
        ],
        'results': [
            '약한 연결 가설은 단순 전파가 아닌 지속적 변형(adaptation) 과정을 거쳐 확산됨',
            '서로 다른 학문 커뮤니티는 가설을 상이한 방식으로 해석하고 발전시킴',
            '커뮤니티의 등장·합병·분리 과정 및 핵심 학자의 브로커 역할 추적',
            '계산적 방법과 질적 방법의 결합이 아이디어 확산 연구에 유효함을 입증',
        ],
    },
    {
        'path': os.path.join(BASE, '2021_stark_predicting_data_quality.md'),
        'title_ko': '자아 중심 네트워크 연구에서 대리 응답의 데이터 품질 예측',
        'rq': '자아 중심 네트워크 연구에서 대리 응답자(proxy respondent)가 제공하는 데이터의 품질을 어떤 요인이 예측하는가?',
        'methods': [
            '대리 응답 방식(proxy report)의 자아 중심 네트워크 설문 데이터 분석',
            '충족화(satisficing) 행동 및 인지적 부담 요인 분석',
            '독일어 설문 데이터 활용',
        ],
        'results': [
            '응답자 특성(인지 능력, 동기 등)이 대리 응답의 데이터 품질에 영향을 미침',
            '충족화 행동이 데이터 오류와 연관됨',
            '대리 응답 방식의 타당성 조건 및 한계 제시',
        ],
    },
    {
        'path': os.path.join(BASE, '2021_lerner_dynamic_network_analysis.md'),
        'title_ko': '접촉 일지의 동적 네트워크 분석',
        'rq': '접촉 일지 데이터에서 추출한 시간 스탬프 다중 행위자 이벤트를 어떻게 통계적으로 모델링하고 분석할 수 있는가?',
        'methods': [
            '관계적 하이퍼이벤트 모델(RHEM, Relational Hyperevent Models) 제안',
            '이원 행위자-이벤트 네트워크(two-mode actor-event networks)와 하이퍼그래프 대응 관계 활용',
            '마가렛 대처 내각 접촉 일지 실증 데이터 적용',
        ],
        'results': [
            '시간 스탬프 다중 행위자 이벤트 분석을 위한 새로운 RHEM 프레임워크 제안',
            '선호적 연결(preferential attachment), 친숙성(familiarity), 폐쇄성(closure) 등 네트워크 효과 추정 가능',
            '대처 내각 장관 간 비공식 그룹 형성 및 진화 과정 실증적으로 규명',
        ],
    },
    {
        'path': os.path.join(BASE, '2021_lungeanu_using_trellis_software.md'),
        'title_ko': 'Trellis 소프트웨어를 활용한 현장 고품질 대규모 네트워크 데이터 수집',
        'rq': '현지 현장 조건(도달하기 어려운 지역사회, 저문해력 집단 등)에서 Trellis 모바일 플랫폼은 어떻게 고품질 네트워크 데이터 수집을 지원하는가?',
        'methods': [
            'Trellis 모바일 플랫폼을 이용한 케냐 2개 마을 주민 1,969명 네트워크 조사',
            '이름·사진 기반 알터 식별 방식 적용',
            '조사원, 시간대, 위치 등 메타데이터 기반 수집 과정 모니터링',
        ],
        'results': [
            '저문해력 집단을 포함한 현장에서 다중 언어·다중 관계 네트워크 데이터 수집 가능성 입증',
            '메타데이터 분석을 통해 조사원별 인위적 변동성 등 데이터 품질 문제 탐지 가능',
            '오프라인/온라인 혼합 환경에서 대규모 네트워크 데이터 수집의 실용성 확인',
        ],
    },
    {
        'path': os.path.join(BASE, '2021_agneessens_collecting_surveybased_social_.md'),
        'title_ko': '직장 조직 내 설문 기반 사회 네트워크 정보 수집',
        'rq': '직장 조직에서 설문을 통해 사회 네트워크 데이터를 수집할 때 어떤 주요 요소들을 고려해야 하는가?',
        'methods': [
            '직장 조직 대상 사회 네트워크 설문 연구의 실무 경험 기반 체계적 검토',
            '4가지 핵심 요소(접근 협상, 경계 설정, 데이터 수집 방식, 피드백 제공) 분석',
        ],
        'results': [
            '조직 접근 협상, 네트워크 경계 및 샘플링 설계, 데이터 수집 접근법, 윤리적 피드백 등 4가지 핵심 요소 도출',
            '연구 목적과 각 요소 간 정합성(co-alignment)이 성공적 연구의 핵심임을 강조',
            '직장 조직 대상 네트워크 연구 설계를 위한 실용적 가이드라인 제공',
        ],
    },
    {
        'path': os.path.join(BASE, '2021_krivitsky_impact_survey_design.md'),
        'title_ko': '자아 중심 표본 ERGM 추정에 대한 설문 설계의 영향',
        'rq': '자아 중심 네트워크 표집 설계(측정 전략, 표집 전략)는 지수족 랜덤 그래프 모형(ERGM)의 통계적 추정 및 추론에 어떤 영향을 미치는가?',
        'methods': [
            '지수족 랜덤 그래프 모형(ERGM) 기반 자아 중심 네트워크 분석',
            '계층적 표집 및 연결 정도 중도 절단(degree censoring) 효과 시뮬레이션 연구',
            '에고와 알터 속성, 에고-알터 및 알터-알터 관계 측정 전략 비교',
        ],
        'results': [
            '측정 명세의 에고-알터 간 일치가 ERGM 추정의 핵심임을 확인',
            '계층적 표집은 통계적 추론의 효율성에 유의미한 영향을 미침',
            '연결 정도 중도 절단은 추정 편향을 유발하므로 설계 단계에서 고려 필요',
            '자아 중심 데이터로 전체 네트워크 특성 분포 추론 가능성 제시',
        ],
    },
    {
        'path': os.path.join(BASE, '2021_smith_network_sampling_coverage_iii.md'),
        'title_ko': '네트워크 표본 포함률 III: 다양한 네트워크 및 결측 조건에서 결측 네트워크 데이터 대체',
        'rq': '다양한 네트워크 구조 및 결측 데이터 조건에서 결측 네트워크 데이터를 대체(imputation)하는 최적 방법은 무엇인가?',
        'methods': [
            '다양한 결측 네트워크 데이터 대체(imputation) 기법 비교',
            '결측 메커니즘 및 네트워크 구조 유형에 따른 시뮬레이션 연구',
            '머신러닝 기반 방법론 포함 다양한 알고리즘 평가',
        ],
        'results': [
            '결측 비율 및 네트워크 구조 유형에 따라 최적 대체 방법이 다름',
            '특정 조건에서 머신러닝 기반 대체법이 전통적 방법보다 우수한 성능 발휘',
            '네트워크 표집 범위(coverage)에 따른 데이터 품질 저하 양상 체계적 분석',
        ],
    },
    {
        'path': os.path.join(BASE, '2021_stys_trust_quality_and_the.md'),
        'title_ko': '신뢰, 품질, 그리고 네트워크 수집 경험: 콩고민주공화국 두 연구 이야기',
        'rq': '분쟁 지역과 같이 불안정하고 민감한 맥락에서 사회 네트워크 데이터를 수집할 때 신뢰와 데이터 품질은 어떻게 상호 의존적으로 작용하는가?',
        'methods': [
            '민족지학(ethnography) 및 1차 데이터 수집 기반 질적 접근',
            '링크 추적 설계(link-tracing design)를 활용한 퍼스널 지원 네트워크 조사',
            '자아 중심 네트워크 설계(egocentric network design)를 통한 다층 관계 체인 데이터 수집',
        ],
        'results': [
            '불안정한 현장 환경에서 조사자-응답자 간 신뢰가 데이터 품질에 결정적 영향',
            '표집, 신뢰성, 타당성 등 다층적 장애물 극복 과정과 대응 전략 기술',
            '적대적 하위집단(전투원~민간인)을 포함한 지원 네트워크 구조 분석 가능성 입증',
        ],
    },
    {
        'path': os.path.join(BASE, '2021_block_statistical_model_for.md'),
        'title_ko': '가중 네트워크로서 이동성 표(mobility table) 분석을 위한 통계 모형: 교수 채용 네트워크 적용 사례',
        'rq': '이동성 표를 가중 네트워크로 분석하기 위한 통계 모형은 어떻게 구축할 수 있으며, 대학 교수 채용 네트워크에 어떻게 적용할 수 있는가?',
        'methods': [
            '가중 네트워크 기반 이동성 표 분석 통계 모형 개발',
            '지수족 랜덤 그래프 모형(ERGM) 확장 활용',
            '대학 교수 채용 네트워크 실증 데이터 적용',
        ],
        'results': [
            '이동성 표를 가중 네트워크로 분석할 수 있는 새로운 통계 프레임워크 제안',
            '교수 채용 네트워크에서 기관 간 위계 구조 및 집단화(clustering) 패턴 확인',
            '사회적 이동성 연구에 네트워크 분석 방법론 적용 가능성 확장',
        ],
    },
    {
        'path': os.path.join(BASE, '2021_juozaitien_nonparametric_estimation_recip.md'),
        'title_ko': '관계 이벤트 네트워크에서 상호성 및 삼원 효과의 비모수적 추정',
        'rq': '관계 이벤트 네트워크(relational event network)에서 상호성(reciprocity)과 삼원(triadic) 효과를 어떻게 비모수적으로 추정할 수 있는가?',
        'methods': [
            '비모수적 방법론(non-parametric estimation)을 활용한 관계 이벤트 네트워크 분석',
            '상호성 및 삼원 폐쇄(triadic closure) 효과 추정 모형 개발',
        ],
        'results': [
            '비모수적 접근법을 통해 관계 이벤트 네트워크의 상호성과 삼원 효과 추정 가능',
            '기존 모수적 모형의 가정 없이도 네트워크 역학 패턴 포착',
            '시간 경과에 따른 이벤트 강도 변화와 네트워크 효과 비모수적 검증 틀 제공',
        ],
    },
    {
        'path': os.path.join(BASE, '2021_kruse_contextualizing_oppositional_c.md'),
        'title_ko': '반학교 문화의 맥락화: 학교별 성별·민족 소수자 지위의 가변적 의의',
        'rq': '학교 맥락(자원 수준, 사회경제적 분리 구조)은 성별·민족 소수자 집단의 반학교 문화(oppositional culture) 형성에 어떤 차별적 영향을 미치는가?',
        'methods': [
            '4개 시점 네트워크 패널 설문(독일 학생 4,000명 이상)',
            '확률적 행위자 지향 모형(SAOM)을 이용한 네트워크-행동 공진화 분석',
        ],
        'results': [
            '집단 기반 반학교 문화는 전반적으로 매우 드물게 나타남',
            '학교 자원이 부족할수록 남학생들이 고성취 또래를 덜 긍정적으로 평가하는 경향 증가',
            '민족 소수자 남학생이 경제적으로 불리한 학교에서 고성취자를 덜 지지하는 패턴 확인',
        ],
    },
    {
        'path': os.path.join(BASE, '2021_schoenfeld_shortest_pathbased_centrality_.md'),
        'title_ko': '노드별 맥락 제약이 있는 속성 그래프에서 최단 경로 기반 중앙성 지표',
        'rq': '개별 노드의 맥락 제약(context constraint)이 존재하는 속성 그래프에서 최단 경로 기반 중앙성(betweenness, closeness 등)을 어떻게 재정의하고 계산할 수 있는가?',
        'methods': [
            '속성 그래프(attributed graph)에서 노드별 맥락 제약을 반영한 최단 경로 알고리즘 설계',
            '새로운 중앙성 지표 정의 및 계산 방법 제안',
        ],
        'results': [
            '노드별 맥락 제약을 반영한 새로운 최단 경로 기반 중앙성 지표 체계 제안',
            '기존 중앙성 지표(betweenness centrality 등)의 일반화 프레임워크 제공',
            '해석 가능성(interpretability) 향상을 위한 맥락 반영 중앙성 계산 방법론 정립',
        ],
    },
    {
        'path': os.path.join(BASE, '2021_stadel_balancing_bias_and_burden.md'),
        'title_ko': '퍼스널 네트워크 연구에서 편향과 응답 부담 간 균형 맞추기',
        'rq': '퍼스널 네트워크 연구에서 알터 수를 줄이거나 무작위 하위 표본을 추출하는 전략이 응답 부담 감소와 편향 증가 간 균형에 어떤 영향을 미치는가?',
        'methods': [
            '네덜란드 여성 701명 및 각 25명의 알터로 구성된 퍼스널 네트워크 데이터 분석',
            '알터 수 감소(2~24명) 및 무작위 하위표본 추출 두 가지 전략 비교 시뮬레이션',
        ],
        'results': [
            '알터 수 감소 시 네트워크 구조·구성 특성 추정에 편향이 발생하며 그 정도 정량화',
            '무작위 하위표본 추출 전략이 일부 지표에서 더 낮은 편향을 나타냄',
            '연구자가 부담 감소와 편향 최소화 간 균형을 결정하기 위한 실용적 가이드라인 제공',
        ],
    },
    {
        'path': os.path.join(BASE, '2021_kevork_bipartite_exponential_random_g.md'),
        'title_ko': '노드 임의 효과를 포함한 이분 지수족 랜덤 그래프 모형',
        'rq': '이분 네트워크(bipartite network)에서 관측되지 않은 노드별 이질성을 임의 효과로 통합한 ERGM을 어떻게 추정할 수 있는가?',
        'methods': [
            '노드 임의 효과를 포함한 이분 ERGM(Bipartite Exponential Random Graph Model) 개발',
            '임의 효과 모형 추정 알고리즘 설계',
        ],
        'results': [
            '이분 네트워크에서 관측되지 않은 노드별 이질성을 반영하는 새로운 ERGM 확장 제안',
            '임의 효과 포함 시 모형 적합도와 추정 안정성 향상',
            '이분 네트워크 분석의 통계적 추론 정확성 개선 효과 검증',
        ],
    },
    {
        'path': os.path.join(BASE, '2021_kmetty_party_nexus_position_generator.md'),
        'title_ko': '정당 연결망 위치 생성기(Party Nexus Position Generator)',
        'rq': '정치적 지인 네트워크를 측정하기 위해 기존 위치 생성기(position generator) 기법을 정당 맥락에 어떻게 적용할 수 있으며, 이 도구는 독일과 헝가리에서 어떤 타당성을 보이는가?',
        'methods': [
            '위치 생성기(position generator) 기법을 정치 네트워크 측정에 적용한 PNPG 개발',
            '독일·헝가리 두 국가 비교 설문 조사(온라인 및 대면 방식)',
        ],
        'results': [
            '정당 연결망 위치 생성기(PNPG)의 타당성을 두 국가에서 입증',
            '국가별 정치 네트워크 구성 및 정치 행동에 대한 영향 비교 분석',
            '광범위한 환경 차이가 정치 네트워크 구조와 행동 영향에 미치는 효과 확인',
        ],
    },
    {
        'path': os.path.join(BASE, '2021_light_clouding_climate_science.md'),
        'title_ko': '기후 과학 흐리기: 합의 과학자와 반합의 과학자에 대한 비교 네트워크·텍스트 분석',
        'rq': '기후 과학 합의 진영과 반합의 진영의 과학자들은 공동 저술 네트워크 구조 및 텍스트 내용 면에서 어떻게 다른가?',
        'methods': [
            '공동 저술 네트워크 분석',
            '텍스트 분석(네트워크 및 텍스트 혼합 분석)',
        ],
        'results': [
            '기후 과학 합의 진영과 반합의 진영 과학자 간 공동 저술 네트워크 구조 차이 확인',
            '두 집단의 텍스트 내용 및 주요 개념 프레이밍 방식의 체계적 차이 발견',
            '반합의 과학자들의 네트워크적 특성이 기후 과학 논쟁 형성에 미치는 영향 분석',
        ],
    },
    {
        'path': os.path.join(BASE, '2021_mcmillan_keeping_the_code.md'),
        'title_ko': '규범 지키기: 청소년 우정·연애 지역 규범이 낭만적 네트워크의 거시 구조에 미치는 영향',
        'rq': '청소년들 사이에서 "친구의 전 연인과 사귀지 않는다"는 사회 규범은 낭만적 네트워크의 거시 구조에 어떤 영향을 미치는가?',
        'methods': [
            'PEAR 연구의 12개월 낭만적 관계 데이터 활용',
            '시간적 ERGM(temporal ERGMs) 분석',
            '낭만적 네트워크 구조 변화 시뮬레이션',
        ],
        'results': [
            '전 세계적 연애 네트워크가 Bearman et al.(2004)의 체인형 스패닝 트리 구조와 유사함을 확인',
            '청소년들이 친구의 전 연인과 사귀기를 회피하는 사회 규범 존재 입증',
            '해당 규범 완화 시 낭만적 네트워크가 더 군집화되고 중복이 감소하는 시뮬레이션 결과',
        ],
    },
    {
        'path': os.path.join(BASE, '2021_kamiski_artificial_benchmark_for_commu.md'),
        'title_ko': '커뮤니티 탐지 인공 벤치마크(ABCD): 커뮤니티 구조를 가진 빠른 랜덤 그래프 모형',
        'rq': 'LFR 벤치마크의 확장성·이론적 분석 가능성 한계를 극복하면서 커뮤니티 탐지 알고리즘 평가에 활용할 수 있는 새로운 합성 랜덤 그래프 모형은 무엇인가?',
        'methods': [
            'ABCD(Artificial Benchmark for Community Detection) 랜덤 그래프 모형 개발',
            '커뮤니티 크기 및 연결 정도에 대한 멱함수(power law) 분포 적용',
            'LFR 모형과의 성능 비교 실험',
        ],
        'results': [
            'LFR 대비 생성 속도가 빠르고 이론적 분석이 용이한 ABCD 모형 제안',
            '혼합 매개변수(mixing parameter) ξ를 통해 커뮤니티 강도를 직관적으로 조절 가능',
            'ABCD와 LFR이 유사한 통계적 속성을 가지면서도 확장성 측면에서 ABCD 우수',
        ],
    },
    {
        'path': os.path.join(BASE, '2021_antunes_sampling_methods_and_estimatio.md'),
        'title_ko': '대형 네트워크에서 삼각형 수 분포의 표집 방법과 추정',
        'rq': '대형 네트워크에서 꼭짓점 및 엣지별 삼각형 수(triangle count) 분포를 표집(sampling)을 통해 어떻게 효율적으로 추정할 수 있는가?',
        'methods': [
            '삼각형 수 분포 추정을 위한 새로운 표집 방법 제안',
            '세 가지 표집 설계(네트워크 접근 시나리오 기반)',
            '역변환(inversion) 및 점근 추정 방법 개발',
        ],
        'results': [
            '꼭짓점 및 엣지별 삼각형 수 분포를 표집을 통해 전체 복원 가능한 방법론 제안',
            '다중 표본을 결합한 단일 추정 방법 도출',
            '합성 및 실세계 네트워크에서 추정 방법의 유효성 검증',
        ],
    },
    {
        'path': os.path.join(BASE, '2021_ingold_the_roles_actors_play.md'),
        'title_ko': '정책 네트워크에서 행위자들의 역할: 강하게 제도화된 분야의 중심 위치',
        'rq': '강하게 제도화된 정책 네트워크에서 어떤 유형의 행위자가 중심적 위치를 차지하며, 결합적 또는 교량적 중앙성은 시간에 따라 얼마나 안정적으로 유지되는가?',
        'methods': [
            '지수족 랜덤 그래프 모형(ERGM)을 활용한 종단적 정책 네트워크 분석',
            '결합적(bonding) 및 교량적(bridging) 중앙성 비교 분석',
        ],
        'results': [
            '극소수 행위자만이 시간에 걸쳐 중심적 위치를 유지함',
            '국가 기관이 이익집단보다 중심 위치를 더 안정적으로 유지하는 경향',
            '이전 시점의 중앙성(t1)이 다음 시점의 활동성·인기(t2)를 예측함',
        ],
    },
    {
        'path': os.path.join(BASE, '2021_wilkerson_logic_and_learning.md'),
        'title_ko': '네트워크 연쇄 반응에서의 논리와 학습',
        'rq': '선형 임계 모형(LTM, Linear Threshold Model)과 그 생물학적 변형은 논리 연산 및 통계적 학습에 얼마나 효과적인 계산 기반을 제공하는가?',
        'methods': [
            '선형 임계 모형(LTM) 기반 논리 게이트 구현 및 안정성 분석',
            '이진 분류기로서의 LTM 분석',
            '공간적 제약 조건과 임계성(criticality)의 학습 효율성 실험',
        ],
        'results': [
            'LTM이 논리 연산 및 범용 불리언 논리 계산 가능함을 이론적으로 입증',
            '공간적 제약이 학습 효율성을 크게 향상시킴',
            '임계성(criticality)이 정확도의 급격한 향상과 연관됨을 초기 실험에서 확인',
        ],
    },
    {
        'path': os.path.join(BASE, '2021_cherifi_introduction_the_special.md'),
        'title_ko': 'COMPLEX NETWORKS 2019 특별호 서문',
        'rq': 'COMPLEX NETWORKS 2019 학술대회의 주요 주제와 수록 논문들의 범위는 무엇인가?',
        'methods': [
            '특별호 편집 서문(editorial introduction)',
        ],
        'results': [
            'COMPLEX NETWORKS 2019 학술대회 특별호의 주제 범위 및 수록 논문 개요 소개',
            '복잡 네트워크 연구의 최신 동향 개관',
        ],
    },
    {
        'path': os.path.join(BASE, '2021_boekhout_investigating_scientific_mobil.md'),
        'title_ko': '다층 시간 모티프를 활용한 공동 저술 네트워크의 과학적 이동성 연구',
        'rq': '과학 분야별로 공동 저술 협력과 연구자 이동성(mobility)은 어떻게 다르게 나타나며, 이 둘의 인과적 방향은 무엇인가?',
        'methods': [
            '다층 시간 모티프(multilayer temporal motifs) 프레임워크 개발',
            '동시 엣지를 포함한 시간 모티프 효율적 계산 알고리즘 제안',
            'Web of Science 데이터 기반 770만 노드·9,400만 엣지 대규모 공동 저술 네트워크 분석',
        ],
        'results': [
            '국제 협력과 국제 이동성이 상호 영향을 주고받음(양방향 인과 관계) 확인',
            '인문·사회과학(SSH) 학자들은 원거리 저자와 더 많이 공동 저술하는 경향',
            '수학·컴퓨터 과학(M&C) 학자들은 기존 지인 네트워크 내에서 협력을 이어가는 경향',
        ],
    },
    {
        'path': os.path.join(BASE, '2021_payne_diffusion_profile_embedding.md'),
        'title_ko': '그래프 꼭짓점 유사성의 기반으로서 확산 프로파일 임베딩',
        'rq': '랜덤 워크(random walk) 기반 확산 패턴을 활용하여 그래프 꼭짓점 간 유사성을 어떻게 정의하고 측정할 수 있는가?',
        'methods': [
            '확산 유사성(diffusion similarity) 개념 및 그래프 꼭짓점 임베딩 방법 개발',
            '연속 시간 랜덤 워크 미분 방정식 해를 기반으로 한 꼭짓점 특성 벡터 구성',
            'C. elegans 신경 연결체 및 마우스 망막 뉴런 데이터 실증 적용',
        ],
        'results': [
            '랜덤 워크 발산·수렴 패턴을 결합한 새로운 꼭짓점 유사성 지표 제안',
            '커뮤니티 구조 및 이분 부분 그래프 내 계층 구조 동시 반영 가능',
            '유사성 품질 측정 도구로 불확실성 지수(uncertainty index) 도입',
        ],
    },
    {
        'path': os.path.join(BASE, '2021_ready_measuring_reciprocity_double_s.md'),
        'title_ko': '상호성 측정: 이중 표집, 일치도, 그리고 네트워크 구성',
        'rq': '동일한 관계에 대해 양방향 응답자 데이터(double-sampled data)를 어떻게 집계하느냐가 측정된 네트워크의 상호성(reciprocity) 수준에 어떤 영향을 미치는가?',
        'methods': [
            '인도 75개 마을의 사회적 지원 네트워크 이중 표집(double-sampling) 데이터 분석',
            '다층 지수족 랜덤 그래프 모형(multilevel ERGM) 적용',
            '합집합(union) 및 교집합(intersection) 집계 방식 비교',
        ],
        'results': [
            '응답자 간 일치도(concordance)가 낮아 집계 방식에 따라 관측 상호성 수준이 크게 달라짐',
            '합집합 또는 교집합 집계 모두 상호성 수준을 극적으로 높임',
            '응답자들이 동일 인물을 제공자이자 수혜자로 동시에 지명하는 경향이 맥락·관계 유형에 따라 변함',
        ],
    },
    {
        'path': os.path.join(BASE, '2021_kim_cheating_online_gaming.md'),
        'title_ko': '온라인 게임에서 속임수는 관찰과 피해를 통해 확산된다',
        'rq': '온라인 멀티플레이어 게임에서 속임수(cheating) 행동은 제3자 관찰과 직접적 피해 경험 중 어떤 경로를 통해 더 효과적으로 전파되는가?',
        'methods': [
            '100만 건 이상의 온라인 FPS 게임 매치 대규모 디지털 추적 데이터 분석',
            '관찰 및 피해 경험 후 속임수 시작 이벤트 시퀀스 식별',
            '팀·상호작용 구조를 보존한 대안적 게임플레이 시나리오 비교',
        ],
        'results': [
            '관찰과 피해를 동시에 경험한 경우에만 사회적 전염(social contagion) 효과 존재',
            '반복 또는 다중 소스 노출이 있을 때만 속임수 확산 효과 발생',
            '제3자 영향과 "보복" 상호성이 긍정적으로 상호작용하여 속임수 전파',
        ],
    },
    {
        'path': os.path.join(BASE, '2021_kevork_iterative_estimation_mixed.md'),
        'title_ko': '노드 임의 효과를 포함한 혼합 지수족 랜덤 그래프 모형의 반복 추정',
        'rq': '지수족 랜덤 그래프 모형(ERGM)에서 관측되지 않은 노드별 이질성을 임의 효과로 포함한 혼합 모형을 어떻게 안정적으로 추정할 수 있는가?',
        'methods': [
            '노드별 임의 효과를 포함한 혼합 ERGM(mixed ERGM) 개발',
            '근사 의사가능도(pseudolikelihood) 추정과 최대 가능도(MLE) 추정을 반복하는 알고리즘',
            'AIC(Akaike Information Criterion) 기반 모형 선택',
        ],
        'results': [
            '노드별 이질성 효과를 안정적으로 추정하는 반복 알고리즘 제안',
            '대규모 네트워크에서도 노드 이질성 효과 적합 가능',
            'AIC 기반 모형 선택으로 노드별 이질성 존재 여부 체계적 검증 가능',
        ],
    },
    {
        'path': os.path.join(BASE, '2021_kueffner_toward_generalized_notion.md'),
        'title_ko': '시간적 네트워크 모델링을 위한 이산 시간의 일반화된 개념을 향하여',
        'rq': '시간적 네트워크(temporal network)를 모델링할 때 이산 시간(discrete time)의 개념을 어떻게 일반화할 수 있으며, 비결정적 시간과 불완전 데이터는 어떻게 처리할 수 있는가?',
        'methods': [
            '이산 시간에 대한 일반화 프레임워크 이론적 개발',
            '비결정적 시간 및 불완전 데이터 처리 방법론 제안',
            'R 패키지 구현 및 공개',
        ],
        'results': [
            '비결정적 시간 및 불완전 데이터를 포함한 시간적 네트워크의 이산 시간 일반화 프레임워크 제안',
            '일반화된 시간 개념이 최단 시간 경로(shortest temporal path) 계산에 미치는 영향 분석',
            'R 패키지를 통해 모든 개념에 대한 프로그래밍 지원 제공',
        ],
    },
]

for paper in papers:
    process_file(paper['path'], paper['title_ko'], paper['rq'], paper['methods'], paper['results'])

print('All done!')
