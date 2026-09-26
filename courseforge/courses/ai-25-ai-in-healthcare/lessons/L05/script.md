# L05 Levels of Evidence: From Study to Real-World Use | Presenter Script

Course: AI-25 · Video: 5 min · Words: 733

## Hook
Two suppliers show you the same sensitivity figure. One measured it on old images from a single hospital. The other measured it in a trial where patients' care was actually affected. Are these claims equally strong? No, and knowing why is a vital skill.

## Explain
In the last lesson, we learned to read performance numbers. Now we ask a different question. How strong is the study behind those numbers? Evidence for a clinical AI tool builds up in stages, and each stage answers a harder and more important question.

The first stage is a retrospective study at a single site. The model is tested on past data from the same source it was trained on. It answers the question: can the model find the pattern at all? But the test data looks very like the training data, so results are often too optimistic.

The second stage is external validation. The model is tested on past data from other hospitals, devices or countries. It asks: does the performance hold in new settings? This often shows a drop. The third stage is a prospective study. The tool runs on new patients as they arrive, often in silent mode, where clinicians do not see its output.

The fourth stage is a randomised controlled trial, or a similar comparative study. Patients or sites are randomly assigned to care with or without the tool. It asks the most important question: does using the tool improve outcomes that matter to patients, compared with current practice?

Higher accuracy is not the same as better care. A tool can find more cases and still not help, if clinicians ignore its alerts, or if it delays other work. And accuracy in one study often falls in a new hospital, because of different patients, devices, prevalence and workflows.

Here is a simple way to picture it. A new medicine is not trusted on laboratory results alone. It must show that it is safe and helps real patients in careful clinical studies. An AI tool that has only passed a retrospective test is still at the laboratory stage.

Reporting guidelines also exist to help authors describe AI studies completely, and help readers judge them. A statement that a study followed one is a good sign, but you still need to read what the study actually did.

## Demonstrate
Let's see this in practice. Doctor Olusegun Adeyemi chairs a hypothetical digital health committee at a teaching hospital in Nigeria. Three suppliers present tools that flag possible sepsis for rapid clinical review. The committee sorts the evidence.

Supplier one reports high sensitivity on twenty thousand past records from one hospital abroad. That is a retrospective, single-site study. The committee notes that the patients, laboratory tests and nursing observation schedules may differ from its own.

Supplier two reports results on past records from five hospitals in three countries, with a lower but stable sensitivity. That is external validation, which is stronger. Supplier three reports a prospective study in two hospitals, where the tool ran silently for six months, and its alerts were compared with later confirmed diagnoses.

That shows real-time performance, but not whether patient outcomes improve. None of the suppliers has a randomised trial. The committee does not reject all three. It picks supplier three's tool for a local silent-mode evaluation, with a decision point before any clinician sees the alerts. It also asks all suppliers whether they followed a recognised reporting guideline.

A common mistake is to treat a large retrospective study as strong evidence because the numbers are big. A study on one million past images still only shows that the model can find a pattern in data like its training data. Look at the study design first, then at the size.

## Recap
Let's recap. First, evidence builds from retrospective single-site studies, to external validation, to prospective studies, to randomised or comparative trials of patient outcomes. Second, performance often falls in new settings because of different patients, devices, prevalence and workflows. Third, reporting guidelines help you judge a study, but you must still read its design and setting.

## CTA
Now it is your turn. In the exercise below this video, you will rank four hypothetical evidence summaries from weakest to strongest, and write what extra evidence each would need before clinical use. It takes about twenty minutes. This completes week one. Next week, we start with AI for hospital and clinic operations. See you there.

## Thumbnail
Headline: Same Number, Different Evidence
Image: Navy background, a four-step staircase labelled with small study icons rising left to right, the top step glowing teal, headline in teal Inter Bold.

## Production Notes
- [VERIFY] content.md names TRIPOD+AI, SPIRIT-AI and CONSORT-AI as examples of AI reporting guidelines. The voiceover and slides refer to 'reporting guidelines for AI studies' without names; add the names on screen only after confirming names, scope and current versions against the guideline publications.
- Dr. Olusegun Adeyemi, his committee in Nigeria and the three suppliers are hypothetical. No real product, company or study is shown.
- The sepsis example is about judging evidence only; the script gives no advice on sepsis care or on using any real tool.
