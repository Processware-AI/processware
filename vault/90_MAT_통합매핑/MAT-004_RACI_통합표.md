---
type: MAT
doc_id: MAT-004
title: RACI 통합표
version: "0.1"
owner: "QMR"
status: draft
created: 2026-04-16
updated: 2026-04-16
retention: "상시"
tags: [MAT, raci]
---

# MAT-004 RACI 통합표

> 전사 PRO 별 책임 분담을 단일 표로 집계. 역할 중복·공백 탐지용.

## 역할 리스트
- 경영진(CEO/CISO/CPO 등)
- 프로세스 오너
- 담당자
- 내부심사팀
- 외부 이해관계자

## RACI 매트릭스

| PRO | 활동 | CEO | 경영진 | PCB | SEPG | PO | 담당 | QA |
|---|---|---|---|---|---|---|---|---|

---

## VCSMS (ISO/SAE 21434) RACI

> 영역코드 VCSMS / interface_only. 13 PRO 공통 역할: **R**=Cybersecurity Manager(CSM, owner) / **C**=Process Control Board(PCB, reviewer) / **A**=Top Management(경영진, approver). WI 단계 승인자(HITL)는 각 WI §2 에 따라 CSM 또는 TARA/Assessor 로 위임. 상세 RACI: 각 PRO §3.
>
> **Accountable 무결성 점검**: 13 PRO 전건 A=Top Management 단일 지정. **Accountable 누락 0 / 중복(복수 A) 0.** 단일 책임자 원칙 충족.

| PRO | 활동 영역 | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|---|
| PRO-VCSMS-01-01 | 조직 거버넌스 운영(정책·책임·문화·정보공유·도구) | CSM | 경영진 | PCB | 전 부서·내부심사팀 |
| PRO-VCSMS-01-02 | 독립 조직 사이버보안 감사 | CSM(감사 독립인) | 경영진 | PCB | 피감 프로세스 오너 |
| PRO-VCSMS-01-03 | 지속활동·취약점 관리 | CSM | 경영진 | PCB, 보안설계자 | 사고대응팀·공급자 |
| PRO-VCSMS-01-04 | 사이버보안 사고 대응 | CSM(IR 리더) | 경영진 | PCB, 법무/홍보 | 규제기관·고객 |
| PRO-VCSMS-02-01 | 프로젝트 사이버보안 관리 | CSM | 경영진 | PCB, 프로젝트 매니저 | 개발팀 |
| PRO-VCSMS-02-02 | 케이스·평가·릴리스 | CSM | 경영진 | 독립 Assessor, PCB | 프로젝트팀 |
| PRO-VCSMS-02-03 | TARA(횡단) | CSM | 경영진 | TARA 분석가·안전담당 | 컨셉/개발팀 |
| PRO-VCSMS-02-04 | 컨셉 엔지니어링 | CSM | 경영진 | PCB, 보안설계자 | 개발팀 |
| PRO-VCSMS-02-05 | 제품개발 엔지니어링 | CSM | 경영진 | PCB, 개발 리드 | 검증팀 |
| PRO-VCSMS-02-06 | 차량 수준 검증 | CSM | 경영진 | PCB, 검증 엔지니어 | 케이스 담당 |
| PRO-VCSMS-02-07 | 생산 사이버보안 통제 | CSM | 경영진 | PCB, 생산기술 | 양산 라인 |
| PRO-VCSMS-02-08 | 분산활동·공급망 | CSM | 경영진 | PCB, 구매·공급자 | 프로젝트팀 |
| PRO-VCSMS-02-09 | 운영·업데이트·폐기 | CSM | 경영진 | PCB, 업데이트팀 | 고객·서비스 |

## 개정 이력
| 버전 | 일자 | 변경내용 | 승인자 |
|---|---|---|---|
| 0.1 | 2026-06-14 | VCSMS 13 PRO RACI 추가. Accountable 단일성 점검 통과(누락 0/중복 0) (trace phase) | (미승인) |
