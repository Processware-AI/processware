---
type: moc
title: 추적성·통합매핑 인덱스
updated: 2026-04-29
tags: [moc, traceability, mat]
---

# MOC — 추적성·통합매핑(MAT) 인덱스

> 기준: [[표준프로세스_구성원칙]] · 문서체계: [[01_문서체계]]

## 통합 MAT 6종 (전사 공통, MAT-001~006)
- [[MAT-001_문서관리대장]]
- [[MAT-002_규제요구사항_대조표]]
- [[MAT-003_산출물_목록표]]
- [[MAT-004_RACI_통합표]]
- [[MAT-005_심사증적_인덱스]]
- [[MAT-006_문서계층_추적매트릭스]]

## 표준별 추적성 매트릭스
번호는 **MAT-011 부터 순차 부여** (편입 순서). 상세: [[02_문서번호체계]] §MAT 번호 할당 원칙.

### CMMI-DEV-ML3 (편입일: 2026-04-29)
- [[MAT-011_CMMI-DEV-ML3_추적성_v1.0]] — 126 Req-ID × 5 POL × 20 PRO × 142 WI × 14 TMP × 14 EX
  - ✅ 18 / 🟡 108 / ⛔ 0 (Req-ID 단위)
  - 출처: [[01_CMMI-DEV-ML3_요구사항분해]] (ISACA paraphrase only)

### 후속 표준 (예상)
- (예약) `[[MAT-012_ISO9001_추적성]]`
- (예약) `[[MAT-013_ISO27001_추적성]]`
- ...

## 교차 매핑 (Cross-Standard)
- HLS 공통 조항 → 통합 경영 프로세스(PRO-MGT-*)
- ISO 9001 §8 ↔ ISO 27001 §8 ↔ ISO 20000 §8 (운영 통합)
- ISO 27001 ↔ 27701 (정보보호 ↔ 개인정보)
- **CMMI-DEV-ML3 GOV/OT/SAM ↔ ISO 9001 §5/§7.2/§8.4** (interface_only — 상세: MAT-011 §4)
- **CMMI-DEV-ML3 CM/RDM/VV/PI ↔ ASPICE SUP.8/SYS.1/SYS.4-5/SWE.4-5** (PA 매핑 — 상세: MAT-011 §4)
