# 보건환경종합정보시스템 고도화 SI 프로젝트 — 업무 흐름 시각화

> 본 파일은 `business_flow.yaml` 의 시각화 동반본입니다. 정식 데이터는 YAML 을 기준으로 합니다.
>
> - **데이터**: `inputs/06_목표흐름/business_flow.yaml`
> - **시각화**: 본 파일 (Markdown + Mermaid)
> - **표준 기반**: `inputs/04_AsIs/SI_Project/` (RFP — 대구광역시 보건환경연구원)

---

## 1. 전체 라이프사이클 — 시나리오 그룹

6 그룹 / 17 시나리오. 핵심 단계는 좌→우, 횡단(프로젝트관리) 그룹은 점선으로 모든 단계에 결합.

```mermaid
flowchart LR
    classDef mainGroup fill:#dbeafe,stroke:#1e40af,stroke-width:1.5px,color:#1e3a8a
    classDef supportGroup fill:#fef3c7,stroke:#b45309,stroke-width:1.5px,color:#78350f
    classDef scenario fill:#ffffff,stroke:#475569,color:#0f172a

    subgraph SG1 ["SG-1 사업기획·착수"]
        SC001["SC-001<br/>사업 착수·계획 수립"]:::scenario
    end

    subgraph SG2 ["SG-2 분석·설계"]
        SC002["SC-002<br/>요구사항 분석·확정"]:::scenario
        SC003["SC-003<br/>아키텍처·DB 설계"]:::scenario
        SC004["SC-004<br/>화면·기능 설계"]:::scenario
    end

    subgraph SG3 ["SG-3 개발·구현"]
        SC005["SC-005<br/>LIMS 핵심 기능 개발"]:::scenario
        SC006["SC-006<br/>보안·인증 구현"]:::scenario
        SC007["SC-007<br/>데이터 마이그레이션"]:::scenario
        SC008["SC-008<br/>시스템 연계 구현"]:::scenario
    end

    subgraph SG4 ["SG-4 시험·검수"]
        SC009["SC-009<br/>단위·통합 테스트"]:::scenario
        SC010["SC-010<br/>보안 취약점 점검"]:::scenario
        SC011["SC-011<br/>사용자 인수·검수"]:::scenario
    end

    subgraph SG5 ["SG-5 안정화·이행"]
        SC012["SC-012<br/>시스템 오픈·이행"]:::scenario
        SC013["SC-013<br/>교육·기술이전"]:::scenario
        SC014["SC-014<br/>하자보수·운영전환"]:::scenario
    end

    subgraph SG6 ["SG-6 프로젝트 관리 (횡단)"]
        SC015["SC-015<br/>통제·진척"]:::scenario
        SC016["SC-016<br/>보안·인력 관리"]:::scenario
        SC017["SC-017<br/>품질보증·산출물"]:::scenario
    end

    SC001 --> SC002
    SC002 --> SC003
    SC002 --> SC004
    SC003 --> SC005
    SC003 --> SC007
    SC004 --> SC005
    SC004 --> SC008
    SC005 --> SC006
    SC005 --> SC009
    SC006 --> SC009
    SC007 --> SC009
    SC008 --> SC009
    SC009 --> SC010
    SC010 --> SC011
    SC011 --> SC012
    SC012 --> SC013
    SC012 --> SC014

    SG6 -.횡단 통제.-> SG1
    SG6 -.횡단 통제.-> SG2
    SG6 -.횡단 통제.-> SG3
    SG6 -.횡단 통제.-> SG4
    SG6 -.횡단 통제.-> SG5

    class SG1,SG2,SG3,SG4,SG5 mainGroup
    class SG6 supportGroup
```

---

## 2. 단계별 게이트 (간소 뷰)

180일 사업 기간 동안의 큰 게이트 흐름.

```mermaid
flowchart LR
    A([계약 체결]) --> B[착수·계획]
    B --> C[분석·설계 완료<br/>베이스라인]
    C --> D[개발 완료<br/>단위시험]
    D --> E[통합·성능·보안<br/>점검 완료]
    E --> F[발주자 승인검사·UAT]
    F --> G[완료보고·최종 검수<br/>14일 이내]
    G --> H([시스템 오픈])
    H --> I[안정화·교육]
    I --> J([하자담보 운영 1년])

    style A fill:#dcfce7,stroke:#166534
    style H fill:#dcfce7,stroke:#166534
    style J fill:#fef3c7,stroke:#b45309
```

---

## 3. 카테고리(요구사항) 커버리지 매핑

11개 RFP 카테고리가 17 시나리오에 어떻게 분산되는지.

```mermaid
flowchart LR
    classDef cat fill:#fce7f3,stroke:#9d174d,color:#831843
    classDef sc fill:#e0f2fe,stroke:#075985,color:#0c4a6e

    ECR[ECR 4건]:::cat --> SC003
    ECR --> SC012
    SFR[SFR 20건]:::cat --> SC002
    SFR --> SC004
    SFR --> SC005
    SFR --> SC006
    PER[PER 2건]:::cat --> SC004
    PER --> SC009
    SIR[SIR 4건]:::cat --> SC004
    SIR --> SC008
    DAR[DAR 8건]:::cat --> SC003
    DAR --> SC007
    DAR --> SC012
    TER[TER 3건]:::cat --> SC002
    TER --> SC009
    TER --> SC011
    SER[SER 5건]:::cat --> SC006
    SER --> SC010
    QUR[QUR 2건]:::cat --> SC001
    QUR --> SC002
    QUR --> SC012
    QUR --> SC015
    QUR --> SC017
    COR[COR 8건]:::cat --> SC001
    COR --> SC003
    COR --> SC005
    COR --> SC016
    PMR[PMR 16건]:::cat --> SC001
    PMR --> SC002
    PMR --> SC011
    PMR --> SC015
    PMR --> SC016
    PMR --> SC017
    PSR[PSR 6건]:::cat --> SC013
    PSR --> SC014
    PSR --> SC017

    class SC001,SC002,SC003,SC004,SC005,SC006,SC007,SC008,SC009,SC010,SC011,SC012,SC013,SC014,SC015,SC016,SC017 sc
```

---

## 4. 시나리오별 상세 흐름

각 시나리오 내부 노드는 `business_flow.yaml` 의 `mermaid` 필드를 그대로 옮긴 것입니다.

### SC-001 · 사업 착수·계획 수립

```mermaid
flowchart LR
    K[착수 보고] --> P[사업수행계획서]
    P --> S[일정·WBS]
    P --> W[작업장소 협의]
    P --> SC[하도급 계획]
    S --> A[계획서 승인]
    W --> A
    SC --> A
```

매핑 요구사항: PMR-001, PMR-013, PMR-014, PMR-015, QUR-001, COR-004, COR-005

### SC-002 · 요구사항 분석·확정

```mermaid
flowchart LR
    A[현행 HEIS 분석] --> E[요구사항 청취]
    E --> S[요구사항정의서]
    S --> T[추적표]
    T --> B[베이스라인 확정]
```

매핑 요구사항: QUR-002, PMR-016, TER-001, SFR-001~020

### SC-003 · 아키텍처·DB 설계

```mermaid
flowchart LR
    A[아키텍처] --> D[DBMS 도입]
    A --> L[논리모델]
    L --> P[물리모델]
    L --> S[데이터표준]
    P --> R[모델 검증]
    S --> R
```

매핑 요구사항: COR-001, COR-002, COR-003, ECR-001~004, DAR-002, DAR-005, DAR-006, DAR-008, SIR-004

### SC-004 · 화면·기능 설계

```mermaid
flowchart LR
    U[UI 컨셉] --> S[화면설계서]
    S --> F[기능정의서]
    F --> I[인터페이스 설계]
    F --> P[성능 설계]
    I --> R[설계 검토]
    P --> R
```

매핑 요구사항: SIR-001~004, SFR-001, SFR-002, SFR-014, SFR-015, PER-001, PER-002

### SC-005 · LIMS 핵심 업무 기능 개발

```mermaid
flowchart LR
    E[개발환경] --> R[의뢰·접수]
    E --> M[마스터·자원]
    E --> A[시스템관리]
    R --> T[시험·결과]
    T --> RP[성적서 발급]
    RP --> Q[조회·통계]
    M --> U[단위시험]
    Q --> U
    A --> U
```

매핑 요구사항: SFR-003 ~ SFR-019

### SC-006 · 보안·인증 구현

```mermaid
flowchart LR
    E[보안교육] --> L[로그인]
    E --> A[접근통제]
    L --> A
    A --> C[암호화]
    C --> CL[클라우드 보안]
    CL --> R[코드리뷰]
```

매핑 요구사항: SFR-001, SFR-002, SER-001, SER-003, SER-005

### SC-007 · 데이터 마이그레이션

```mermaid
flowchart LR
    P[이관 계획] --> C[정제·규칙]
    C --> E[이관 실행]
    E --> V[데이터 검증]
    V --> B[백업·복구 구성]
```

매핑 요구사항: DAR-001, DAR-003, DAR-004, DAR-007, ECR-001
> Oracle HEIS DB → 대구시 D-클라우드 오픈소스 DB

### SC-008 · 시스템 연계 구현

```mermaid
flowchart LR
    S[연계 명세] --> L[식약처 LIMS]
    S --> O[온나라]
    L --> T[연계 시험]
    O --> T
```

매핑 요구사항: SFR-020, SIR-003, SIR-004

### SC-009 · 단위·통합 테스트

```mermaid
flowchart LR
    P[테스트 계획] --> S[시나리오·데이터]
    S --> U[단위시험]
    U --> I[통합시험]
    I --> PT[성능시험]
    PT --> D[결함 조치]
    D --> I
```

매핑 요구사항: TER-001, TER-002, PER-001, PER-002

### SC-010 · 보안 취약점 점검

```mermaid
flowchart LR
    P[점검 계획] --> SC[소스코드 진단]
    P --> PT[모의해킹]
    P --> I[인프라 점검]
    SC --> R[취약점 조치]
    PT --> R
    I --> R
```

매핑 요구사항: SER-002, SER-003, SER-004, SER-005

### SC-011 · 사용자 인수 테스트·검수

```mermaid
flowchart LR
    P[UAT 계획] --> D[데이터 준비]
    D --> E[승인검사]
    E --> F[하자 보완]
    F --> E
    F --> C[완료보고]
    C --> I[최종 검수]
```

매핑 요구사항: TER-003, PMR-016
> 발주자 승인검사 후 완료보고 → 14일 이내 최종 검수

### SC-012 · 시스템 오픈·이행

```mermaid
flowchart LR
    D[운영 배포] --> C[컷오버]
    C --> S[안정화]
    C --> B[백업 검증]
    B --> S
```

매핑 요구사항: ECR-001~004, QUR-001, DAR-003, DAR-004

### SC-013 · 교육·기술이전

```mermaid
flowchart LR
    P[교육계획] --> U[사용자 교육]
    P --> T[기술이전]
    T --> E[EA 현행화]
```

매핑 요구사항: PSR-003, PSR-004, PSR-005

### SC-014 · 하자보수·운영전환

```mermaid
flowchart LR
    W[하자보수 계획] --> D[하자 조치]
    W --> F[기능점수 제출]
    W --> Q[품질보증 인계]
```

매핑 요구사항: PSR-001, PSR-002, PSR-006
> 1년 하자담보 운영 + 기능점수 산정자료 제출

### SC-015 · 프로젝트 통제·진척 관리 (횡단)

```mermaid
flowchart LR
    W[정기보고] --> R[위험관리]
    W --> S[일정통제]
    R --> C[변경관리]
    C --> S
    S --> A[수시보고]
```

매핑 요구사항: PMR-001~004, PMR-013, PMR-016, QUR-002

### SC-016 · 보안·인력 관리 (횡단)

```mermaid
flowchart LR
    P[보안 계획] --> H[인원 보안]
    P --> D[문서 보안]
    P --> O[사무실 보안]
    P --> M[장비·매체]
    P --> N[네트워크]
    D --> I[산출물·IP]
```

매핑 요구사항: PMR-006~012, COR-004~008

### SC-017 · 품질보증·산출물 관리 (횡단)

```mermaid
flowchart LR
    P[QA 계획] --> A[QA 활동]
    A --> D[산출물 관리]
    D --> C[변경관리 대장]
    A --> V[가용성 점검]
```

매핑 요구사항: QUR-001, QUR-002, PMR-005, PSR-001

---

## 5. 렌더링 방법

| 환경 | 방법 |
|---|---|
| GitHub | `.md` 파일 자동 렌더링 (네이티브 지원) |
| VS Code | "Markdown Preview Mermaid Support" 확장 설치 후 미리보기 (`Ctrl+Shift+V`) |
| Obsidian | 기본 지원 — 본 vault 안에서 그대로 렌더링 |
| 단일 다이어그램 추출 | mermaid 코드블록 내용을 [mermaid.live](https://mermaid.live) 에 붙여넣기 |

---

## 6. 다음 단계

- 본 흐름이 RFP 요구사항을 충분히 커버하면 → `/process-plan "SI_Project 보건환경종합정보시스템 고도화 사업 표준 프로세스"` 실행
- 시나리오 추가/수정이 필요하면 → `business_flow.yaml` 직접 편집 후 본 `.md` 파일 재생성 (또는 자동 동기화 도구 활용)
