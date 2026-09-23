# L13 Risk Assessment for an AI Health Tool

Course: AI-25 · Module: M3 · Objectives: O4, O5, O6 · Video: 5 min

## Hook
Every AI health tool has risks. A good evaluation does not pretend they are absent. It names them, judges how serious they are, and gives each one a mitigation and a person who owns it.

## Explanation
A structured risk review looks at six areas. Each one links to an earlier lesson.

1. **Clinical safety:** missed cases, false alarms, and harm from delay or over-treatment (L04, L10).
2. **Bias and equity:** lower performance or less benefit for some patient groups or settings (L09).
3. **Privacy:** misuse, over-collection or exposure of health data (L02, L11).
4. **Security:** unauthorised access, data breaches, or changes to the tool or its inputs.
5. **Workflow:** automation bias, alert fatigue, outputs reaching the wrong person, extra workload (L10).
6. **Accountability:** unclear responsibility for decisions, for monitoring, and for reporting incidents (L01, L11).

For each risk, record:

- **Description:** what could happen, to whom.
- **Likelihood:** low, medium or high.
- **Severity:** low, medium or high, based on the worst realistic harm to a patient.
- **Mitigation:** what will reduce the likelihood or the harm.
- **Owner:** a named role responsible for the mitigation.

A simple rule: any risk with high severity needs a mitigation that is in place **before** use, even if its likelihood is low.

**Who to include.** Risks look different from different positions. Include:
- **Clinicians** who will use the tool, and those who receive its outputs.
- **Patients and community representatives**, especially from groups who may be affected differently. They often see risks professionals miss, such as language barriers or distrust of automated messages.
- **Data protection, IT security and quality or safety staff.**

You can run a short workshop, a structured interview, or a patient panel review of a draft risk table.

**Analogy:** A risk review is like a pre-flight check. The crew does not ask "Is the aircraft safe?" in general. They go through a list, system by system, and each item has a person who confirms it. The list makes it harder to forget something important.

## Worked Example
Dr. Putri Wulandari leads quality improvement at a hypothetical district hospital in Indonesia. The hospital is considering a triage-support tool for the emergency department. It suggests a triage category from vital signs and the presenting complaint; the triage nurse makes the final decision. Putri holds two workshops: one with emergency nurses and doctors, and one with community health volunteers and two patient representatives.

| Area | Risk | Likelihood | Severity | Mitigation | Owner |
|---|---|---|---|---|---|
| Clinical safety | Tool under-triages a patient with atypical symptoms | Medium | High | Nurse decides; tool cannot lower a category the nurse has chosen; weekly review of under-triage cases | Emergency nursing lead |
| Bias and equity | Lower performance for older patients and patients who speak regional languages, whose complaints are recorded less fully | Medium | High | Check performance by age group and language in silent mode before use | Quality lead (Putri) |
| Privacy | Triage data sent to a supplier's cloud outside policy | Low | High | Data processing agreement; data protection review before pilot | Data protection officer |
| Security | Unauthorised access to the triage system | Low | High | Access control, audit logs, security testing | IT security manager |
| Workflow | Nurses accept tool suggestions without assessment at busy times | High | High | Training; suggestion shown only after nurse's own initial category is entered; audit | Emergency nursing lead |
| Accountability | Unclear who reviews incidents involving the tool | Medium | Medium | Add tool to the hospital's incident reporting categories; governance group reviews monthly | Medical director |

The patient representatives raised the language risk; the clinicians had not listed it. The nurses suggested showing the tool's suggestion only after their own assessment, to reduce automation bias.

## Common Mistake
Many risk tables list risks but give mitigations like "staff will be careful" and no owner. That is not a mitigation; it is a hope. A real mitigation is a specific action or design change, such as a training session, an audit or an interface change, and it has a named role responsible for it.

## Key Takeaways
1. A structured risk review covers clinical safety, bias and equity, privacy, security, workflow and accountability.
2. Each risk needs a likelihood, a severity, a specific mitigation and a named owner; high-severity risks need mitigations before use.
3. Clinicians, patients and community voices find different risks, so include them all.

## Hands-on Exercise
**Task:** Capstone step 2: complete the risk section of your evaluation, with at least one mitigation and one owner for each risk.
**Tools:** Your capstone document; a table in Google Docs, Sheets, Word or Excel. Optional: Claude or ChatGPT (free plan) to suggest risks you may have missed; do not enter confidential or patient information.
**Steps:**
1. Create a risk table with the columns: area, risk, likelihood, severity, mitigation, owner.
2. Write at least one risk for each of the six areas, specific to your tool and its intended use.
3. Rate likelihood and severity, and write one sentence explaining your highest severity rating.
4. Add a specific mitigation and a named role as owner for every risk.
5. Complete the data and privacy, bias and equity, and workflow and accountability sections of your template, using your table.
6. Write two sentences on how you would include patients or community representatives in reviewing this table.
**What good looks like:** At least six specific risks covering all areas, sensible ratings, concrete mitigations (not "be careful"), a named owner for each, at least one equity risk tied to a named patient group or setting, and a realistic plan for patient or community input.
**Time:** about 45 minutes

## Review Flags
- None. The triage-support tool, hospital and risk ratings are hypothetical illustrations, and no specific facts or rules are stated.
