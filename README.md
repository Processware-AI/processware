# 전사 표준 프로세스 구축 하네스 (Claude Code + Obsidian)

국제/국내 표준(ISO·IEC·KS 등)을 **하나씩 순차 편입**하여 전사 표준 프로세스 체계를 MD로 구축하고, Obsidian 볼트로 관리하는 에이전트 하네스.

## 특징
- **8종 문서 유형 체계**: POL / PRO / WI / TMP / EX / REC / MAT / REF
- **유형별 엄격한 분리**: 템플릿↔기록↔예시 분리, 정책↔절차↔지침 분리
- **통합 MAT 5종**: 문서관리대장·규제대조표·산출물목록·RACI통합·심사증적
- **표준-프로세스 양방향 추적성** + `source_citation` 기반 감사증적
- **Claude Code subagent 파이프라인** + Obsidian 볼트 자동 구성
- **체크포인트/재개** (`_state.yaml`): 실패 지점부터 이어 실행
- **자가수정 루프**: QA Fail → 담당 에이전트 자동 재호출 (max 3 attempts)
- **골든샘플**: POL/PRO/WI 품질 하한선 참조

## 디렉터리 구조
```
Standard_Process/
├── README.md
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
    ├── 00_공통관리/                 ← 문서체계·번호체계·용어집
    ├── 00_MOC/                      ← 인덱스(Map of Content)
    ├── 01_구성원칙/                 ← 최상위 기준
    ├── 02_표준/                     ← 표준별 작업 공간(개요·요구사항분해·작업노트)
    ├── 03_POL_정책/                 ← POL-*
    ├── 04_PRO_절차/                 ← PRO-*
    ├── 05_WI_업무지침/              ← WI-*
    ├── 06_TMP_템플릿/               ← TMP-*
    ├── 07_EX_작성예시/              ← EX-*
    ├── 08_REC_기록/                 ← REC-* (운영 단계 생성)
    ├── 09_REF_참고자료/             ← REF-*
    ├── 90_MAT_통합매핑/             ← MAT-001~010 (현 6종) + 표준별 추적성 (MAT-011~)
    ├── 99_템플릿/                   ← Obsidian Templates (T03~T13)
    └── 99_폐기_보관/                ← 만료/폐지 문서 아카이브
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
┌──────────────────┐   POL / PRO
│ process-designer │─────────────────────────────────▶ 03_POL_정책/, 04_PRO_절차/
└──────────────────┘
        │
        ▼
┌──────────────────┐   WI / TMP / EX + MAT-001 등록
│  wi-tmp-writer   │─────────────────────────────────▶ 05_WI/, 06_TMP/, 07_EX/
└──────────────────┘
        │
        ▼
┌──────────────────┐   표준별 추적성 + MAT-001~006 갱신
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

## 파일명 규칙
```
[유형]-[식별번호]_[문서명]_v[버전].md
```
예: `POL-QMS-001_품질방침_v1.0.md`, `PRO-ISMS-101_정보보안_총괄_절차_v1.0.md`

상세: `vault/00_공통관리/02_문서번호체계.md`

## 권장 Obsidian 플러그인
- Templates (코어) → `vault/99_템플릿/` 지정
- Dataview → MAT-001 문서관리대장 자동 수집
- Graph view → POL-PRO-WI-TMP 연결 시각화
