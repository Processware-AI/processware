# 전사 표준 프로세스 구축 하네스 (Claude Code + Obsidian)

국제/국내 표준(ISO·IEC·KS·IATF 등)을 **하나씩 순차 편입**하여 전사 표준 프로세스 체계를 MD로 구축하고, Obsidian 볼트로 관리하는 에이전트 하네스.

## 특징
- **8종 문서 유형 체계**: POL / PRO / WI / TMP / EX / REC / MAT / REF
- **유형별 엄격한 분리**: 템플릿↔기록↔예시 분리, 정책↔절차↔지침 분리
- **계층 번호 체계**: `POL-{영역}-{###}` → `PRO-{P}{##}` → `WI-{POL}-{PRO}-{##}` 계보 추적
- **통합 MAT 6종**: 문서관리대장·규제대조표·산출물목록·RACI통합·심사증적·문서계층추적
- **표준 분류 레지스트리**: Layer(L1/L2/L3)·Structure·Integration Mode 3축 분류
- **자동차/의료기기 도메인 지원**: 8개 도메인 전용 표준 (IATF 16949, ASPICE, ISO 26262, ISO/SAE 21434, ISO 13485, ISO 14971, IEC 62304, IEC 81001-5-1)
- **표준-프로세스 양방향 추적성** + `source_citation` 기반 감사증적
- **Claude Code subagent 파이프라인** + Obsidian 볼트 자동 구성
- **체크포인트/재개** (`_state.yaml`): 실패 지점부터 이어 실행
- **자가수정 루프**: QA Fail → 담당 에이전트 자동 재호출 (max 3 attempts)
- **골든샘플**: POL/PRO/WI 품질 하한선 참조

## 디렉터리 구조
```
Standard_Process/
├── README.md
├── 전용AI에이전트_프레임워크_설계안.md  ← 독립 프레임워크 승격 설계안 (draft)
├── .claude/
│   ├── agents/                      ← Claude Code 서브에이전트
│   │   ├── standard-analyzer.md
│   │   ├── process-designer.md
│   │   ├── wi-tmp-writer.md
│   │   ├── traceability-mapper.md
│   │   └── qa-reviewer.md
│   └── commands/
│       └── build-standard.md        ← 오케스트레이터 슬래시 커맨드
└── vault/                           ← Obsidian Vault 루트
    ├── 00_공통관리/                 ← 문서체계·번호체계·용어집·레지스트리
    ├── 00_MOC/                      ← 인덱스(Map of Content)
    ├── 01_구성원칙/                 ← 최상위 기준
    ├── 02_표준/                     ← 표준별 작업 공간
    │   └── _scaffold/               ← 새 표준 편입용 스캐폴드 템플릿
    │       └── _inputs/             ← 카테고리별 입력자료 투하 폴더
    ├── 03_POL_정책/                 ← POL-*
    ├── 04_PRO_절차/                 ← PRO-*
    ├── 05_WI_업무지침/              ← WI-*
    ├── 06_TMP_템플릿/               ← TMP-*
    ├── 07_EX_작성예시/              ← EX-*
    ├── 08_REC_기록/                 ← REC-* (운영 단계 생성)
    ├── 09_REF_참고자료/             ← REF-*
    ├── 90_MAT_통합매핑/             ← MAT-001~010 전사 공통 + MAT-011~ 표준별 추적성
    ├── 99_템플릿/                   ← Obsidian Templates (T03~T15)
    │   └── _골든샘플/               ← POL/PRO/WI 품질 하한선 참조 예시
    ├── 99_폐기_보관/                ← 만료/폐지 문서 아카이브
    └── _inputs_common/              ← 복수 표준 공통 입력자료 (법규·해설서 등)
```

## 에이전트 파이프라인
```
/build-standard ISO9001
        │
        ▼
┌──────────────────┐   표준개요/요구사항분해/REF/MAT-002
│ standard-analyzer│─────────────────────────────────▶ 02_표준/, 09_REF/, 90_MAT/
└──────────────────┘
        │
        ▼
┌──────────────────┐   POL / PRO / MAT-003
│ process-designer │─────────────────────────────────▶ 03_POL_정책/, 04_PRO_절차/
└──────────────────┘
        │
        ▼
┌──────────────────┐   WI / TMP / EX + MAT-001 등록  (전수 생성 강제)
│  wi-tmp-writer   │─────────────────────────────────▶ 05_WI/, 06_TMP/, 07_EX/
└──────────────────┘
        │
        ▼
┌──────────────────┐   MAT-{011~}_{표준코드}_추적성 + MAT-001·003·004·005·006 갱신
│traceability-mapper│────────────────────────────────▶ 90_MAT_통합매핑/
└──────────────────┘
        │
        ▼
┌──────────────────┐   8종 유형 분리·링크 정합성 감사
│   qa-reviewer    │─────────────────────────────────▶ 02_표준/{코드}/99_QA리포트_*
└──────────────────┘
        │
        ▼
     MOC 갱신 + 완료 보고
```

## 사용법
1. Obsidian 에서 `vault/` 폴더를 **Open folder as vault** 로 열기.
2. **입력자료 배치 (권장)** — `vault/02_표준/{표준코드}/_inputs/` 에 표준원문·법규·해설서·As-Is 투하. 상세 규칙: `vault/00_공통관리/05_입력자료_규칙.md`
3. Claude Code 대화창에서:
   ```
   /build-standard ISO9001
   ```
4. 여러 표준 순차 편입:
   ```
   /build-standard ISO9001
   /build-standard ISO/IEC_27001
   /build-standard ISO14001
   ```
5. 교차 표준 통합 분석:
   ```
   /build-standard ISO/IEC_27001 --cross
   ```

6. 중단된 실행 이어가기:
   ```
   /build-standard ISO9001 --resume       # 현재 phase 부터 자동 재개
   /build-standard ISO9001 --from design   # design phase 부터 강제 재시작
   /build-standard ISO9001 --restart       # 기존 state 폐기하고 처음부터
   ```

7. 자가수정 루프 조정:
   ```
   /build-standard ISO9001 --max-attempts 5   # 자가수정 최대 횟수
   /build-standard ISO9001 --skip-qa          # QA·자가수정 생략
   ```

**주의**: `_inputs/` 없이 실행하면 LLM 추정 모드로 동작하여 **감사 방어력이 낮습니다**. 프로덕션 용도는 반드시 입력자료를 배치하세요.

## 체크포인트·자가수정 (자동)
각 표준 편입 시 `vault/02_표준/{표준코드}/_state.yaml` 이 자동 생성·갱신됩니다.
- phase 별 `pending → running → done` 이력
- QA Fail 시 `qa_failures[]` 에 담당 에이전트(`assigned_to`)·수정 범위(`fix_scope`) 기록
- 오케스트레이터가 담당 에이전트를 재호출하여 자동 수정 (최대 3회)
- 수동 개입 필요 시 `assigned_to: manual` 로 에스컬레이션

상세 규약: `vault/00_공통관리/06_파이프라인_상태규약.md`

## 문서 유형 8종 (상세: `vault/00_공통관리/01_문서체계.md`)
| 코드 | 유형 | 역할 |
|---|---|---|
| POL | 정책서 | 원칙·방침·책임 |
| PRO | 절차서 | 업무 흐름·관리 절차 |
| WI  | 업무지침서 | 실무 수행 상세 |
| TMP | 템플릿 | 빈 양식 |
| EX  | 작성예시 | 교육용 샘플 |
| REC | 기록본 | 실제 수행 증빙 |
| MAT | 매핑/관리대장 | 추적성·목록·대조표 |
| REF | 참고자료 | 외부 규정·가이드 요약 |

## 파일명 규칙 (상세: `vault/00_공통관리/02_문서번호체계.md`)

POL 번호를 기준으로 하위 문서가 번호를 계승하여 코드만으로 문서 계보를 추적할 수 있다.

```
POL-{영역}-{###}
 └─ PRO-{영역}-{P}{##}                         P = POL 일련번호
      └─ WI-{영역}-{POL###}-{PRO##}-{##}
           ├─ TMP-{영역}-{POL###}-{PRO##}-{WI##}
           ├─ EX-{영역}-{POL###}-{PRO##}-{WI##}
           └─ REC-{영역}-{POL###}-{PRO##}-{WI##}-{YYYY}-{##}
```

예: `POL-QMS-001_품질방침_v1.0.md` → `PRO-QMS-101_품질기획_절차_v1.0.md` → `WI-QMS-001-01-02_문서_검토_및_승인_v1.0.md`

## 통합 MAT 6종 (상세: `vault/00_공통관리/02_문서번호체계.md` §MAT 번호 할당 원칙)

| 번호 | 문서 | 역할 |
|---|---|---|
| MAT-001 | 문서관리대장 | 전사 문서 인벤토리 |
| MAT-002 | 규제요구사항 대조표 | 법규·표준 조항 매핑 |
| MAT-003 | 산출물 목록표 | 표준별 산출물 현황 |
| MAT-004 | RACI 통합표 | 역할·책임 매트릭스 |
| MAT-005 | 심사증적 인덱스 | 감사 증빙 인덱스 |
| MAT-006 | 문서 계층 추적 매트릭스 | POL→PRO→WI→TMP→EX 경로 완결성 |
| MAT-011~ | 표준별 추적성 | 표준 편입 순서대로 순차 부여 |

## 지원 표준 (상세: `vault/00_공통관리/07_표준분류레지스트리.md`)

표준은 **Layer·Structure·Integration Mode** 3축으로 분류되어 에이전트 설계 전략이 자동 결정됩니다.

| Layer | 표준 | 영역코드 | Integration Mode |
|---|---|---|---|
| **L1 경영시스템** | ISO 9001 | QMS | hls_merge |
| | ISO/IEC 27001 | ISMS | hls_merge |
| | ISO/IEC 27701 | PIMS | hls_merge |
| | ISO 14001 | EMS | hls_merge |
| | ISO 45001 | OHSMS | hls_merge |
| | ISO/IEC 20000 | ITSM | hls_merge |
| | ISO 22301 | BCMS | hls_merge |
| | ISO/IEC 42001 | AIMS | hls_merge |
| | IATF 16949 | AUTO | hls_merge (ISO 9001 확장) |
| | ISO 13485 | MDQMS | quasi_hls_merge |
| **L2 엔지니어링** | ASPICE | SPICE | interface_only |
| | ISO 26262 | FUSA | interface_only |
| | ISO/SAE 21434 | VCSMS | interface_only |
| | ISO 14971 | MDRM | interface_only |
| | IEC 62304 | MDSW | interface_only |
| | IEC 81001-5-1 | MDCS | interface_only |
| | ISO/IEC/IEEE 12207 | SWLC | interface_only |
| | ISO/IEC/IEEE 15288 | SYSLC | interface_only |
| **L3 참조** | ISO 31000 | RM | reference_only |

## 권장 Obsidian 플러그인
- Templates (코어) → `vault/99_템플릿/` 지정
- Dataview → MAT-001 문서관리대장 자동 수집
- Graph view → POL-PRO-WI-TMP 연결 시각화

## 독립 프레임워크 설계 (참고)
현재 Claude Code 하네스로 검증된 개념을 Python 기반 독립 실행 프레임워크로 승격하는 설계안이 `전용AI에이전트_프레임워크_설계안.md` 에 있습니다. Claude Agent SDK + LangGraph 하이브리드 구성을 1순위로 권장하며, 4단계 MVP 로드맵(Phase 1 : CLI 포팅 → Phase 4 : SaaS)이 제시되어 있습니다.
