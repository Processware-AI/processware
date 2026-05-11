---
type: moc
title: 추적성·통합매핑 인덱스
updated: 2026-05-11
tags: [moc, traceability, mat]
---

# MOC — 추적성·통합매핑(MAT) 인덱스

> 기준: [[표준프로세스_구성원칙]] · 문서체계: [[01_문서체계]]

## 통합 MAT 10종 (전사 공통, MAT-001~010)

> 현재 9종 파일 운영 중. MAT-010은 `/process-plan --flow` 실행 시 자동 생성.

- [[MAT-001_문서관리대장]] — 전사 문서 인벤토리 + 차원 4 §개정이력 자동 누적
- [[MAT-002_규제요구사항_대조표]] — 표준 조항 ↔ 내부 산출물 매핑
- [[MAT-003_산출물_목록표]] — 표준별 산출물 현황
- [[MAT-004_RACI_통합표]] — 역할·책임 매트릭스
- [[MAT-005_심사증적_인덱스]] — 감사 증빙 인덱스 + 차원 2 실행기록 + 차원 3 심사이력
- [[MAT-006_문서계층_추적매트릭스]] — POL→PRO→WI→TMP→EX 경로 완결성
- [[MAT-007_프로세스_카탈로그]] — 자연어 → WI 라우팅 인덱스 (차원 2 Do)
- [[MAT-008_KPI_대시보드]] — KPI 시계열·회귀 알림 + 차원 4 인계 큐 인덱스 (차원 3 Check)
- [[MAT-009_NCR_관리대장]] — NCR 발행/종결 현황 + §통계 자동 집계 (차원 3 Check)
- (MAT-010: 프로세스 플로우 맵 — PRO 선후관계 + WI 시퀀스, `/process-plan --flow` 실행 시 생성)

## 표준별 추적성 매트릭스
번호는 **MAT-011 부터 순차 부여** (편입 순서). 상세: [[02_문서번호체계]] §MAT 번호 할당 원칙.

### CMMI-DEV-ML3-V1.3 (편입일: 2026-05-11 — v1.3 빌드로 재구성)
- [[MAT-011_CMMI-DEV-ML3-V1.3_추적성_v0.1]] — 216 Req-ID × 5 POL × 18 PRO × 60 WI × 117 TMP × 117 EX
  - ✅ 215 / 🟡 1 (RSKM SG1 ingest 누락) / ⛔ 0 (Req-ID 단위)
  - 출처: `inputs/01_표준원문/CMMI-DEV/requirements.yaml` (CMU/SEI-2010-TR-033 verbatim 100%)
  - 모드: interface_only (HLS POL/PRO 미통합)

### 후속 표준 (예상)
- (예약) `[[MAT-012_ISO9001_추적성]]`
- (예약) `[[MAT-013_ISO27001_추적성]]`
- ...

---

## 개정 이력

| 버전 | 일자 | 변경 내용 |
|---|---|---|
| — | 2026-04-29 | 최초 작성 — 통합 MAT 6종 목록, CMMI-DEV-ML3 MAT-011 등록, 교차 매핑 |
| — | 2026-05-06 | "통합 MAT 6종" → 10종 체계(9종 운영+MAT-010 예약) 정정, MAT-007~010 링크 및 역할 설명 추가 |
| — | 2026-05-11 | MAT-011 CMMI-DEV-ML3 v1.0 → v1.3 빌드로 교체 — 216 Req × 5 POL × 18 PRO × 60 WI × 117 TMP × 117 EX, interface_only 모드, verbatim 출처 100% (traceability-mapper Phase 4) |

## 교차 매핑 (Cross-Standard)
- HLS 공통 조항 → 통합 경영 프로세스(PRO-MGT-*)
- ISO 9001 §8 ↔ ISO 27001 §8 ↔ ISO 20000 §8 (운영 통합)
- ISO 27001 ↔ 27701 (정보보호 ↔ 개인정보)
- **CMMI-DEV-ML3 GOV/OT/SAM ↔ ISO 9001 §5/§7.2/§8.4** (interface_only — 상세: MAT-011 §4)
- **CMMI-DEV-ML3 CM/RDM/VV/PI ↔ ASPICE SUP.8/SYS.1/SYS.4-5/SWE.4-5** (PA 매핑 — 상세: MAT-011 §4)
