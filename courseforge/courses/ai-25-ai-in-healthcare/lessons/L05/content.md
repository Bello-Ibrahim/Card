# L05 Levels of Evidence: From Study to Real-World Use

Course: AI-25 · Module: M1 · Objectives: O2, O5 · Video: 5 min

## Hook
Two suppliers show you the same sensitivity figure. One measured it on old images from a single hospital. The other measured it in a trial where patients' care was actually affected. Are these two claims equally strong? No, and knowing why is one of the most useful skills in this course.

## Explanation
Evidence for a clinical AI tool builds up in stages. Each stage answers a harder and more important question.

1. **Retrospective study, single site.** The model is tested on past data from the same source it was trained on. Question answered: *Can the model find the pattern at all?* Weakness: the test data looks very like the training data, so results are often too optimistic.
2. **External validation.** The model is tested on past data from other hospitals, devices or countries. Question answered: *Does the performance hold in new settings?* This often shows a drop in performance.
3. **Prospective study.** The tool runs on new patients as they arrive, often in "silent mode" where clinicians do not see the output, or with its output shown alongside usual care. Question answered: *Does it work in real time, in the real workflow, with real data quality?*
4. **Randomised controlled trial (RCT) or similar comparative study.** Patients or sites are randomly assigned to care with or without the tool. Question answered: *Does using the tool improve outcomes that matter to patients, such as faster treatment, fewer missed diagnoses or less harm, compared with current practice?*

Higher accuracy is not the same as better care. A tool can find more cases and still not improve outcomes if clinicians ignore its alerts, if it delays other work, or if the extra cases found would not have caused harm.

Why does accuracy in one study often fail to carry over to a new hospital? Common reasons are different patient populations, different devices and settings, different disease prevalence (which changes PPV, as in L04), and different workflows.

Reporting guidelines exist to help authors describe AI studies completely and help readers judge them. Examples include TRIPOD+AI for prediction model studies, SPIRIT-AI for trial protocols and CONSORT-AI for trial reports [VERIFY]. When you read a study, a statement that it followed such a guideline is a good sign, but you still need to read what it did.

**Analogy:** A new medicine is not trusted on laboratory results alone. It must show that it is safe and helps real patients in careful clinical studies before it is used widely. An AI tool that has only passed a retrospective test is at the "laboratory result" stage.

## Worked Example
Dr. Olusegun Adeyemi chairs a hypothetical digital health committee at a teaching hospital in Nigeria. Three suppliers present tools that flag possible sepsis for rapid clinical review. Olusegun's committee sorts the evidence.

- **Supplier 1** reports high sensitivity on 20,000 past records from one hospital abroad. Level: retrospective, single site. The committee notes that the patients, laboratory tests and nursing observation schedules may differ from its own.
- **Supplier 2** reports results on past records from five hospitals in three countries, with a lower but stable sensitivity. Level: external validation. This is stronger, but the committee still asks whether any site resembles theirs.
- **Supplier 3** reports a prospective study in two hospitals, where the tool ran silently for six months and its alerts were compared with later confirmed diagnoses. Level: prospective, silent mode. This shows real-time performance, but not whether patient outcomes improve.

None of the suppliers has a randomised trial. The committee does not reject all three. It decides that Supplier 3's tool is the best candidate for a local silent-mode evaluation (see L14), with a decision point before any clinician sees the alerts. It asks all suppliers whether their studies followed a recognised reporting guideline.

## Common Mistake
Many people treat a large, retrospective study as strong evidence because the numbers are big. The size of a dataset does not change the level of evidence. A retrospective study on one million past images still only shows that the model can find a pattern in data like its training data. It does not show that it works in your hospital or that it improves care. Look at the study design first, then at the size.

## Key Takeaways
1. Evidence for AI tools builds from retrospective single-site studies, to external validation, to prospective studies, to randomised or comparative trials of patient outcomes.
2. Performance often falls in new settings because of different patients, devices, prevalence and workflows.
3. Reporting guidelines for AI studies help you judge completeness, but you must still read the study design and setting.

## Hands-on Exercise
**Task:** Rank 4 hypothetical evidence summaries from weakest to strongest and explain what extra evidence each would need before clinical use.
**Tools:** Pen and paper or any notes app.
**Steps:**
1. Read these hypothetical summaries for tools that flag possible diabetic eye disease for specialist review:
   (a) "Randomised trial in 12 primary care clinics: patients in the tool group were referred earlier than those in usual care."
   (b) "Tested on 50,000 past retinal photographs from the developer's own hospital."
   (c) "Ran silently on all new screening photographs in 3 clinics for 4 months; flags compared with specialist grading."
   (d) "Tested on past photographs from 4 hospitals in 3 countries using 2 camera types."
2. Rank them from weakest to strongest.
3. For each one, write the next piece of evidence you would need before clinical use in your own setting.
4. For the strongest one, write one question you would still ask, for example about the patients or the cameras used.
**What good looks like:** The ranking is b, d, c, a. Each summary has a realistic "next evidence" note, for example external validation for b, a prospective study for d, and an outcome study for c. For a, the learner still asks whether the trial clinics resemble their own setting.
**Time:** about 20 minutes

## Review Flags
- [VERIFY] Names, scope and current versions of AI reporting guidelines (TRIPOD+AI, SPIRIT-AI, CONSORT-AI) must be confirmed against the guideline publications before recording.
