---
standard_id: AutoCyberSec
full_name: "ISO/SAE 21434:2021 — Road vehicles — Cybersecurity engineering"
version: "2021"
generated_at: "2026-06-14"
status: pending_review
---

# AutoCyberSec (ISO/SAE 21434:2021) 인제스트 검토 요청

## 요약
- 총 조항 그룹(규범): **11개** (Clause 5–15) / 요건 추출: **118건** (RQ 101 · RC 13 · PM 4)
- 용어 40 · 약어 12 · 작업산출물(WP) 42 · Annex 8(A–H, 전부 informative)
- **자동 완전성 검사 전부 통과** (ID 시퀀스 누락 0 · informative 누출 0 · 복합문 0 · 분류 미확정 0)
- 검토 필요: **6건** (모두 경미 — 누락 의심 아님)

> 본 표준은 provision 을 `[RQ/RC/PM-NN-MM]` 로 자가 번호화하므로 추출 정확도가 높고, 각 조항의 번호 시퀀스가 연속(gap 0)임이 확인되어 **누락된 규범 요건은 없습니다.** 아래 항목은 누락이 아니라 **분류·범위 판단** 성격입니다.

---

## ⚠️ 범위 판단 필요 (2건)

- [x] **입력 전제(Prerequisites) 18건을 별도 캡처할지 결정**
  → 각 조항 `X.Y.1.1 Prerequisites` 의 "The following information shall be available:" 는 상류 작업산출물(`[WP-..]`)에 대한 **입력 의존성 선언**입니다. 독립 요구사항 ID 가 없어 118건에 미포함했습니다.
  → 예: §8.3.1.1 → "rules and processes included in [WP-05-01] for the development of triggers."
  → 판단: (a) 현행 유지(요건 아님) / (b) `prerequisite_dependencies` 로 별도 추출 요청. 의존성 추적이 필요하면 (b) 선택 후 알려주세요.

- [x] **Clause 1–4 에 요건 0건 — 정상 확인**
  → Clause 1(Scope)·2(Normative references)·3(Terms)·4(General considerations)는 `[RQ]` 비태깅 도입부로 정상입니다. 누락 아님을 확인만 해주세요.

## ❓ 모호한 요구사항 (2건)

- [x] **AutoCyberSec-15-RQ-10** (`[RQ-15-10]`, p52)
  → 텍스트가 "…the attack feasibility rating shall be determined as described in" 로 끝남. 원문은 "…as described in **Table 1**." 로, 표 본문 제거 시 "Table 1" 참조가 탈락했습니다. 의무 내용은 보존됨. 필요 시 `requirements.yaml` 에서 ", as described in Table 1 (High/Medium/Low/Very low)" 보강 권장.

- [x] **PM(permission) 4건 의무 수준 확인** — `[PM-06-08] [PM-06-13] [PM-06-29] [PM-15-07]`
  → `type: permission`, `obligation: may` 로 분류(구성원칙 8종 외 확장 어휘). 후속 `/process-plan` 에서 permission 을 어떻게 다룰지(통상 선택적 통제) 확인.

## ❓ 분류 휴리스틱 검토 (2건)

- [x] **role_requirement 4건 / evidence_requirement 9건 샘플 확인**
  → content classification 은 키워드 휴리스틱입니다. role(책임·역할)·evidence(증적·문서) 분류가 적절한지 `requirements.yaml` 에서 `classification` 필드로 검색해 점검 권장. process_requirement(105건)는 기본값.

- [x] **evidence_candidates ↔ WP 매핑 적정성**
  → evidence_requirement 9건에 한해 동일 조항 그룹의 작업산출물(WP) 설명을 후보로 채웠습니다. 조항 단위 매핑이므로 1:1 정밀도는 아님. `/process-plan` 단계에서 정밀화 예정.

---

## ℹ️ 품질 정보
- 추출 실패 페이지: **없음** (88/88)
- 표 추출: Annex E/F/G/H 평가표는 셀 정렬 손실(informative, 요건 아님)
- informative 누출(NOTE/EXAMPLE/Bibliography/footnote): **0건** (다단계 필터로 제거 검증)
- 전체 추출 품질: **우수**

## 검토 방법
1. 위 체크박스를 검토 후 완료 표시
2. 필요 시 `requirements.yaml` 직접 수정 (특히 RQ-15-10, PM 분류)
3. 입력 전제 별도 캡처를 원하면 이 파일에 메모 후 재인제스트 요청
4. 완료 후 실행:
   ```
   /process-ingest --confirm AutoCyberSec
   ```

## 산출물 위치
```
inputs/01_표준원문/AutoCyberSec/
  ├── structure.yaml                      (조항 구조 + Annex)
  ├── requirements.yaml                   (요건 118건)
  ├── clauses.md                          (전문 텍스트, 페이지 앵커 포함)
  ├── definitions.yaml                    (용어 40 + 약어 12)
  ├── annexes.yaml                        (Annex A–H + WP 42)
  ├── source_map.yaml                     (요건↔원문 페이지/해시)
  ├── clause_to_requirement_matrix.yaml   (조항→요건 매트릭스)
  └── qa/
      ├── review_request.md               (본 파일)
      └── extraction_quality_report.md
```
