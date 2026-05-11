# CMMI-DEV V1.3 — Clauses (Backbone Extract)

> **Source**: CMU/SEI-2010-TR-033, *CMMI for Development, Version 1.3*, November 2010
> **Publisher**: Software Engineering Institute, Carnegie Mellon University
> **PDF SHA-256**: `96eba600c648f547cbe66eb6bacd6f5ce89020ddf4895e0a2350b1035ac8554b`
> **Total pages (physical)**: ~480 (i-x roman + 1-450+ arabic)
> **Extraction mode**: backbone first-pass (structure + sample verbatim)

이 문서는 `requirements.yaml` 의 출처를 추적하기 위한 raw 추출 노트다. 전체 본문 verbatim 보존이 목적이 아니라, 각 요건 항목과 PDF 페이지 간 매핑의 근거 텍스트를 보존하는 것이 목적이다.

---

## Part One — About CMMI for Development

### Chapter 2 — Process Area Components (p.9-19)

**Required / Expected / Informative Component 3-tier 정의**

- **Required components** — process improvement에 essential. 가시적으로 구현되어야 한다. CMMI의 required components는 **specific goals (SG)** 과 **generic goals (GG)** 이다.
- **Expected components** — required component 달성을 위한 활동. SP/GP 가 여기 해당. 단, 동등한 대안(equivalent practice) 사용 가능.
- **Informative components** — model 이해를 돕는 informative material. subpractices, notes, examples, references, elaborations.

**Components Associated with Part Two** (각 PA 내부 구성요소):
- Purpose Statement
- Introductory Notes
- Related Process Areas
- Specific Goals (SG) — required
- Generic Goals (GG) — required (인용: GG 1, GG 2, GG 3)
- Specific Goal and Practice Summaries
- Specific Practices (SP) — expected
- Example Work Products
- Subpractices
- Generic Practices (GP) — expected
- Generic Practice Elaborations
- Additions

**Numbering Scheme** (p.15):
> Specific and generic goals are numbered sequentially. Each specific goal begins with the prefix "SG" (e.g., SG 1). Each generic goal begins with the prefix "GG" (e.g., GG 2).
>
> Specific and generic practices are also numbered sequentially. Each specific practice begins with the prefix "SP," followed by a number in the form "x.y" (e.g., SP 1.1). The x is the same number as the goal to which the specific practice maps.
>
> Each generic practice begins with the prefix "GP," followed by a number in the form "x.y" (e.g., GP 1.1).

### Chapter 3 — Tying It All Together (p.21-37)

**Capability Levels (Continuous)** — applies to individual PAs
- Level 0: Incomplete
- Level 1: Performed
- Level 2: Managed
- Level 3: Defined

**Maturity Levels (Staged)** — applies across multiple PAs
- Level 1: Initial
- Level 2: Managed
- Level 3: Defined
- Level 4: Quantitatively Managed
- Level 5: Optimizing

**Table 3.2 — Process Areas, Categories, Maturity Levels** (p.33):

| PA | Category | ML |
|---|---|---|
| Causal Analysis and Resolution (CAR) | Support | 5 |
| Configuration Management (CM) | Support | 2 |
| Decision Analysis and Resolution (DAR) | Support | 3 |
| Integrated Project Management (IPM) | Project Management | 3 |
| Measurement and Analysis (MA) | Support | 2 |
| Organizational Process Definition (OPD) | Process Management | 3 |
| Organizational Process Focus (OPF) | Process Management | 3 |
| Organizational Performance Management (OPM) | Process Management | 5 |
| Organizational Process Performance (OPP) | Process Management | 4 |
| Organizational Training (OT) | Process Management | 3 |
| Product Integration (PI) | Engineering | 3 |
| Project Monitoring and Control (PMC) | Project Management | 2 |
| Project Planning (PP) | Project Management | 2 |
| Process and Product Quality Assurance (PPQA) | Support | 2 |
| Quantitative Project Management (QPM) | Project Management | 4 |
| Requirements Development (RD) | Engineering | 3 |
| Requirements Management (REQM) | Project Management | 2 |
| Risk Management (RSKM) | Project Management | 3 |
| Supplier Agreement Management (SAM) | Project Management | 2 |
| Technical Solution (TS) | Engineering | 3 |
| Validation (VAL) | Engineering | 3 |
| Verification (VER) | Engineering | 3 |

---

## Part Two — Generic Goals/Practices + 22 Process Areas

### Generic Goals and Generic Practices (p.65-126)

**Process Institutionalization** (p.65):
> Institutionalization is an important concept in process improvement. When mentioned in the generic goal and generic practice descriptions, institutionalization implies that the process is ingrained in the way the work is performed and there is commitment and consistency to performing (i.e., executing) the process.

**Table 6.1 Generic Goals and Process Names** (p.65):
- GG 1 — Performed process
- GG 2 — Managed process
- GG 3 — Defined process

**GG 1 Achieve Specific Goals** (p.68):
> The specific goals of the process area are supported by the process by transforming identifiable input work products into identifiable output work products.

  **GP 1.1 Perform Specific Practices** (p.68):
  > Perform the specific practices of the process area to develop work products and provide services to achieve the specific goals of the process area.

**GG 2 Institutionalize a Managed Process** (p.69):
> The process is institutionalized as a managed process.

  **GP 2.1 Establish an Organizational Policy** (p.69):
  > Establish and maintain an organizational policy for planning and performing the process.

  **GP 2.2 Plan the Process** (p.72):
  > Establish and maintain the plan for performing the process.

  > The plan for performing the process typically includes the following:
  > - Process description
  > - Standards and requirements for the work products and services of the process
  > - Specific objectives for the execution of the process and its results (e.g., quality, time scale, cycle time, use of resources)
  > - Dependencies among the activities, work products, and services of the process
  > - Resources (e.g., funding, people, tools) needed to perform the process
  > - Assignment of responsibility and authority
  > - Training needed for performing and supporting the process
  > - Work products to be controlled and the level of control to be applied
  > - Measurement requirements to provide insight into the execution of the process, its work products, and its services
  > - Involvement of relevant stakeholders
  > - Activities for monitoring and controlling the process
  > - Objective evaluation activities of the process
  > - Management review activities for the process and the work products

  **GP 2.3 Provide Resources** (p.76):
  > Provide adequate resources for performing the process, developing the work products, and providing the services of the process.

  **GP 2.4 Assign Responsibility** (p.82) — *D-2 verbatim* (see requirements.yaml CMMIDEV-GP2.4)
  **GP 2.5 Train People** (p.83) — *D-2 verbatim*
  **GP 2.6 Control Work Products** (p.88) — *D-2 verbatim*
  **GP 2.7 Identify and Involve Relevant Stakeholders** (p.93) — *D-2 verbatim*
  **GP 2.8 Monitor and Control the Process** (p.100) — *D-2 verbatim*
  **GP 2.9 Objectively Evaluate Adherence** (p.106) — *D-2 verbatim*
  **GP 2.10 Review Status with Higher Level Management** (p.113) — *D-2 verbatim*
  **GP 3.1 Establish a Defined Process** (p.115) — *D-2 verbatim*
  **GP 3.2 Collect Process Related Experiences** (p.115) — *D-2 verbatim*

### Requirements Management (REQM) — p.341-348 (Sample PA, partial)

**SP 1.4 Maintain Bidirectional Traceability of Requirements** (p.345-346, tail):
> Requirements traceability also covers relationships to other entities such as intermediate and final work products, changes in design documentation, and test plans. Traceability can cover horizontal relationships, such as across interfaces, as well as vertical relationships.

  Example Work Products:
  1. Requirements traceability matrix
  2. Requirements tracking system

  Subpractices:
  1. Maintain requirements traceability to ensure that the source of lower level (i.e., derived) requirements is documented.
  2. Maintain requirements traceability from a requirement to its derived requirements and allocation to work products.
  3. Generate a requirements traceability matrix.

**SP 1.5 Ensure Alignment Between Project Work and Requirements** (p.346):
> Ensure that project plans and work products remain aligned with requirements.
>
> This specific practice finds inconsistencies between requirements and project plans and work products and initiates corrective actions to resolve them.

  Example Work Products:
  1. Documentation of inconsistencies between requirements and project plans and work products, including sources and conditions
  2. Corrective actions

  Subpractices:
  1. Review project plans, activities, and work products for consistency with requirements and changes made to them.
  2. Identify the source of the inconsistency (if any).
  3. Identify any changes that should be made to plans and work products resulting from changes to the requirements baseline.
  4. Initiate any necessary corrective actions.

### Risk Management (RSKM) — p.349-356 (Sample PA, partial)

**Purpose** (p.349):
> The purpose of Risk Management (RSKM) is to identify potential problems before they occur so that risk handling activities can be planned and invoked as needed across the life of the product or project to mitigate adverse impacts on achieving objectives.

**Specific Goal and Practice Summary** (p.350):
- SG 1 Prepare for Risk Management
  - SP 1.1 Determine Risk Sources and Categories
  - SP 1.2 Define Risk Parameters
  - SP 1.3 Establish a Risk Management Strategy
- SG 2 Identify and Analyze Risks
  - SP 2.1 Identify Risks
  - SP 2.2 Evaluate, Categorize, and Prioritize Risks
- SG 3 Mitigate Risks
  - SP 3.1 Develop Risk Mitigation Plans
  - SP 3.2 Implement Risk Mitigation Plans

**SG 1 Prepare for Risk Management** (p.350):
> Preparation for risk management is conducted.

  **SP 1.1 Determine Risk Sources and Categories** (p.351):
  > Determine risk sources and categories.

  **SP 1.2 Define Risk Parameters** (p.352):
  > Define parameters used to analyze and categorize risks and to control the risk management effort.

  Parameters for evaluating, categorizing, and prioritizing risks:
  - Risk likelihood (i.e., probability of risk occurrence)
  - Risk consequence (i.e., impact and severity of risk occurrence)
  - Thresholds to trigger management activities

  **SP 1.3 Establish a Risk Management Strategy** (p.353):
  > Establish and maintain the strategy to be used for risk management.

**SG 2 Identify and Analyze Risks** (p.354):
> Risks are identified and analyzed to determine their relative importance.

  **SP 2.1 Identify Risks** (p.354):
  > Identify and document risks.

---

## Other 20 PAs (CAR, CM, DAR, IPM, MA, OPD, OPF, OPM, OPP, OT, PI, PMC, PP, PPQA, QPM, RD, SAM, TS, VAL, VER)

**Backbone pass에서 본문 verbatim 미추출**. SG/SP 구조는 canonical CMMI-DEV V1.3 카탈로그 기준으로 `structure.yaml` / `requirements.yaml` 에 보존. 다음 pass에서 페이지 범위 단위로 추출 예정.

각 PA 페이지 시작점:
- CAR p.127, CM p.137, DAR p.149, IPM p.157, MA p.175, OPD p.191, OPF p.203, OPM p.217, OPP p.235, OT p.247, PI p.257, PMC p.271, PP p.281, PPQA p.301, QPM p.307, RD p.325, SAM p.363, TS p.373, VAL p.393, VER p.401

---

## Part Three — Appendices (p.413-end)

- Appendix A: References (p.415)
- Appendix B: Acronyms (p.421)
- Appendix C: CMMI Version 1.3 Project Participants (p.425)
- Appendix D: Glossary (p.433-468) — **definitions.yaml 227건 verbatim 추출** *(D-3 완료)*

---

## Part One Ch 4-5 (D-4 pass) — informative content

본 섹션은 **informative** 콘텐츠로 requirements.yaml 에 새 entry 를 추가하지 않습니다. 대신 별도 YAML 파일로 정리:

### Ch 4. Relationships Among Process Areas (p.39-53)

PA 카테고리별 Basic/Advanced 구분 + 인터-PA 데이터 흐름 → **pa_relationships.yaml**

| 카테고리 | Basic PAs | Advanced PAs | 핵심 흐름 |
|---|---|---|---|
| Process Management (5) | OPD, OPF, OT | OPP, OPM | OPF↔OPD↔OT → 모든 PA / OPP→OPM |
| Project Management (7) | PP, PMC, REQM, SAM | IPM, QPM, RSKM | PP→PMC / REQM→Engineering / BPM enables APM |
| Engineering (5) | (전체 5개 동일) | — | Customer needs → RD → TS → PI → Customer (VER/VAL 피드백) |
| Support (5) | CM, MA, PPQA | CAR, DAR | CM/MA/PPQA → 모든 PA / CAR→OSSP 개선 / DAR→formal evaluation |

**Recursion vs Iteration** (p.50):
- *Recursion*: 시스템 구조의 successive level 에 같은 프로세스 적용 (예: verification 이 전체 product → 컴포넌트 → 컴포넌트의 컴포넌트로 점진 적용)
- *Iteration*: 같은 시스템 level 에서 프로세스 반복 (예: RD ↔ TS 사이의 정보 피드백 루프)

### Ch 5. Using CMMI Models (p.55-61)

CMMI 모델 채택·평가 가이드 → **adoption_guide.yaml**

핵심 요소:
- **Adopting CMMI**: 시니어 매니지먼트 sponsorship + process group + IDEAL 모델
- **Three Selections**: 조직 부분 / 모델(DEV/ACQ/SVC) / 표현(continuous/staged)
- **Agile interpretation** (p.58): 10 PAs (CM, PI, PMC, PP, PPQA, RD, REQM, RSKM, TS, VER) 에 "In Agile environments" 노트 포함
- **Appraisals**:
  - ARC (Appraisal Requirements for CMMI) → Class A/B/C
  - SCAMPI A (공식 benchmark) / B / C
- **Appraisal principles** (p.61): senior mgmt sponsorship, business focus, confidentiality, documented method, reference model, collaborative team, action focus
- **Training**: SEI Introduction to CMMI for Development + advanced training

이 정보는 차원 1 (Plan) 의 process-designer / wi-tmp-writer 가 PA 간 의존성·tailoring 가이드·Agile 적용 시 참고할 수 있는 informative reference 입니다.
