# L14 A Safe Implementation Plan

Course: AI-25 · Module: M3 · Objectives: O6 · Video: 5 min

## Hook
A tool that passed every test can still fail on its first Monday in a real clinic. A safe implementation plan assumes this can happen, finds problems early, and knows in advance when to stop.

## Explanation
A safe implementation plan has seven parts.

1. **Silent-mode testing.** The tool runs on real, current cases, but clinicians do not see its outputs, and care continues as usual. The team compares outputs with what actually happened. This checks local performance, including by patient group, without any risk to patients.
2. **A small pilot.** After silent mode, the tool is used in one ward, clinic or team for a fixed period, with extra support and close monitoring.
3. **Staff training.** Users learn what the tool is for, what it is not for, its known weaknesses, how to disagree with it, and how to report problems. Training must include automation bias (L10).
4. **A governance group.** A named group, usually including clinical, nursing, quality, IT, data protection and patient representatives, owns the tool. It reviews monitoring data and incidents and makes decisions about continuing, changing or stopping.
5. **Monitoring measures.** Decide in advance what you will measure, how often and who looks at it. Include performance (for example sensitivity or PPV, from confirmed cases), equity (the same measures by patient group and site), use (how often outputs are overridden or ignored) and outcomes (the clinical value outcome from L12).
6. **Feedback channels.** Staff and patients need an easy way to report problems, such as a simple form or a named contact, linked to the normal incident reporting system.
7. **Stop criteria and a withdrawal plan.** Write down, before launch, what would make you pause or stop: for example, sensitivity in any patient group falling below an agreed level, a serious incident linked to the tool, or a data feed failure. Also plan how you would withdraw the tool: who decides, how staff are told, and how care returns safely to the previous process.

**Analogy:** A hospital does not install a new type of infusion pump on every ward on the same day. It tests it on one ward, trains the staff, watches closely, and only then extends it. If a problem appears, only one ward is affected, and the old pumps are still available.

## Worked Example
Dr. Ayesha Siddiqui is a public health physician in Pakistan who completed her capstone on a hypothetical tool that flags chest X-rays that may show tuberculosis for clinician review in three district clinics. Her implementation plan:

- **Silent mode (3 months):** The tool reads all chest X-rays in one clinic; outputs are hidden. Results are compared with the clinician's reading and later confirmed diagnoses. Performance is reported by sex, age band, HIV status and X-ray machine.
- **Decision point:** The governance group reviews silent-mode results. The pilot starts only if sensitivity meets an agreed target in every group and the local PPV gives an acceptable review workload.
- **Pilot (6 months, one clinic):** Clinicians see the tool's flag after their own reading. A clinician reads every X-ray, and the tool never clears one alone.
- **Training:** A one-hour session plus a short guide, covering intended use, limits, automation bias and how to report problems.
- **Governance group:** The district medical officer (chair), a clinician from each clinic, the laboratory lead, a data protection officer, IT and a community representative. It meets monthly.
- **Monitoring:** Monthly sensitivity and PPV against confirmed cases, overall and by group; share of flags overridden; time from X-ray to test result, which is the clinical value outcome.
- **Feedback:** A short reporting form in each clinic, linked to the district incident system.
- **Stop criteria:** Pause if sensitivity in any group falls below the agreed target for two months, if the data feed fails for more than a day, or after any serious incident linked to the tool. Withdrawal returns clinics to the current process, which staff continue to practise.

**Recommendation:** "Proceed to silent-mode evaluation. Do not use in routine care until silent-mode results meet the agreed targets in every patient group."

## Common Mistake
Many plans stop at "launch the tool and train staff". Without stop criteria written in advance, teams tend to keep a tool running even when warning signs appear, because stopping feels like failure. Stopping a tool safely is a success of governance. Write the stop criteria and the withdrawal plan before the first patient is affected.

## Key Takeaways
1. A safe plan moves from silent-mode testing to a small pilot, with training, a governance group, monitoring and feedback channels.
2. Monitor performance, equity, use and outcomes, with named people who review the results.
3. Write stop criteria and a withdrawal plan before launch, and end your evaluation with a clear, conditional recommendation.

## Hands-on Exercise
**Task:** Capstone step 3: write the implementation plan and finish your evaluation with a clear recommendation.
**Tools:** Your capstone document; the evaluation template and capstone rubric from L12. Optional: Claude or ChatGPT (free plan) to review clarity; do not enter confidential or patient information.
**Steps:**
1. Write the silent-mode test: where, how long, what you compare, and which patient groups you check.
2. Write the decision point that must be met before a pilot starts.
3. Describe the pilot: setting, duration and how clinicians see the output.
4. List the training content, the governance group members and how often it meets.
5. List at least four monitoring measures covering performance, equity, use and outcomes.
6. Write at least three stop criteria and a short withdrawal plan.
7. Complete the regulatory questions section and write your recommendation: adopt, pilot, or do not adopt, with conditions and reasons.
8. Check the whole document against the rubric and submission checklist.
**What good looks like:** A complete plan with a silent-mode phase, a clear decision point, specific monitoring measures including at least one equity measure, measurable stop criteria, a realistic withdrawal plan, and a recommendation that follows logically from your evidence and risk sections.
**Time:** about 50 minutes

## Review Flags
- None. The implementation plan is a hypothetical illustration; no specific facts, figures or rules are stated.
