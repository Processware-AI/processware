---
type: guide
doc_id: MAN-INDEX
title: "사용자 매뉴얼 — 인덱스"
version: "1.1"
status: approved
created: 2026-05-03
updated: 2026-05-05
tags: [manual, index, guide]
---

# 사용자 매뉴얼 — 4차원 PDCA 프로세스 관리 플랫폼

---

## 빠른 시작

처음이라면 **[[00_시작하기]]** 부터 읽는다. 15분이면 첫 번째 프로세스를 빌드할 수 있다.

---

## 목차

| 문서 | 내용 | 대상 |
|---|---|---|
| [[00_시작하기]] | 15분 퀵스타트 — 설치부터 첫 빌드까지 | 처음 시작하는 모든 분 |
| [[01_개념이해]] | 5단계 파이프라인, 8종 문서체계, vault 구조, 프로세스 뷔페 | 개념을 이해하고 싶은 분 |
| [[02-0_표준문서_전처리]] | `/process-ingest` 상세 — 표준 PDF 전처리·요건 패키지 생성 | 표준 분석가, 프로세스 설계자 |
| [[02_프로세스_설계]] | `/process-plan` 상세 — 입력, 단계, 플래그, 자가수정 | 프로세스 설계자 |
| [[03_프로세스_실행]] | `/process-do` 상세 — 8가지 모드, HITL 승인 흐름 | PM, 실행자 |
| [[03-1_레거시_REC_백필]] | `/process-backfill` 상세 — 레거시 문서 → REC 변환, 자동 WI 매칭, legacy_evidence | 프로세스 전환 담당자, QMR |
| [[04_프로세스_심사]] | `/process-check` 상세 — 독립성, NCR, KPI | QA, 심사원 |
| [[04-1_외부표준_GAP분석]] | `/process-audit` 상세 — 외부 표준 부합성 GAP 분석·MAT-002 갱신 | 심사원, QMR |
| [[05_프로세스_개정]] | `/process-act` 상세 — RCA, PCB 승인, 재빌드 | QMR, Process Owner |
| [[06_역할별_가이드]] | 역할(PM/QA/QMR/심사원)별 시나리오와 체크리스트 | 역할별 담당자 |
| [[07_FAQ]] | 자주 막히는 문제 해결 | 문제가 생겼을 때 |

---

## 커맨드 빠른 참조

```bash
# 표준 문서 전처리 (Ingest)
/process-ingest sources/ISO9001_2015.pdf --standard ISO9001 --version 2015
/process-ingest --confirm ISO9001   # HITL 검토 완료 후 확정

# 프로세스 설계 (Plan)
/process-plan "필요한 업무 체계 설명"
/process-plan --resume              # 중단된 빌드 재개

# 프로세스 실행 (Do)
/process-do WI-번호
/process-do --approve run-XXXX      # HITL 승인
/process-do --check-approvals       # 대기 중 승인 일괄 처리

# 레거시 REC 백필 (Backfill)
/process-backfill sources/old_docs/                      # 배치 변환
/process-backfill sources/old.docx --wi WI-번호          # 단건 (수동 WI 지정)
/process-backfill --confirm run-bXXXX                    # HITL 확정 → REC 생성

# 내부 이행 심사 (Check)
/process-check start PRO-번호 --auditor "이름"
/process-check --confirm run-XXXX   # 심사 매트릭스 확정
/process-check --kpi start 모듈코드 # KPI 측정

# 외부 표준 GAP 분석 (Audit)
/process-audit start --against ISO9001
/process-audit --confirm run-gXXXX  # GAP 초안 확정 + 보고서 발행
/process-audit --list               # 과거 GAP 분석 목록

# 프로세스 개정 (Act)
/process-act start queue-XXXX
/process-act --approve run-XXXX     # PCB 승인
/process-act --list                 # 대기 중인 act queue 확인
```

---

## 관련 문서

- [[표준_빌드_워크플로우_가이드]] — git worktree + Obsidian 설정
- [[표준_프로세스_실행_가이드]] — /process-do 심화
- [[표준_프로세스_심사_가이드]] — /process-check 심화
- [[표준_프로세스_제개정_가이드]] — /process-act 심화
