# HeyGen Batch Pack: AI-25 M1 (AI Across the Health System)

Course: AI in Healthcare. Make one HeyGen video per lesson below, using these settings for every video.

| Setting | Value |
|---|---|
| Avatar | **Vaness** (standard avatar), ID `1bd001e7e50f421d891986aad5c8bbd2` |
| Voice | `1bd001e7e50f421d891986aad5c8bbd2` (the same ID as the avatar: if HeyGen does not list it as a voice, use Vaness's paired English voice and record its ID in DECISIONS.md) |
| Background | Solid colour **#00FF00** (pure green, no gradient, no image) |
| Resolution | 1080p (1920×1080) |
| Aspect ratio | 16:9 |
| Avatar framing | Centred, head and shoulders, same size in every lesson |
| Captions/subtitles | **Off** (captions are added in Stage 6) |
| Music | Off |
| Speed | Normal (1.0×) |

How to paste: copy the whole text block for a lesson into a single HeyGen scene. Each blank line is a natural pause. Do not add or change words, because the edit is timed to this exact narration.

Save each finished video with the exact filename shown, and upload it to `/incoming/`.

## L01 The Landscape of AI in Healthcare

- **Filename:** `ai-25-ai-in-healthcare_M1_L01_presenter.mp4`
- **Expected length:** about 5.1 minutes (704 words). The quality gate accepts ±10%.

```text
A nurse opens the morning list and sees that a software tool has moved three patients to the top. Who decided that they should be seen first? The software, the nurse, or the doctor on duty? In healthcare, the answer must always be clear.

Hello, and welcome to AI in Healthcare. You already work in or near healthcare, so you know that care depends on data, people and processes. AI is now used in all three. In this first lesson, we map where it is used, and we set the one rule that runs through the whole course.

It helps to group the uses into four areas, because each area uses different data and carries different risks. The first area is diagnostic support. These tools help clinicians read images, signals or test results. For example, a tool may highlight a possible abnormality on a scan, or flag a worrying pattern in vital signs.

The second area is operations. These tools help the organisation run, for example scheduling, predicting missed appointments, planning beds and supplies, and drafting documents for staff to review. The third area is patient engagement. These tools talk to patients through reminders, health education and information services in several languages.

The fourth area is public health. These tools look at populations rather than individuals. For example, they spot unusual rises in reported symptoms, or help plan vaccination outreach. They use surveillance reports, surveys, and anonymised or grouped records.

Now the core principle of this course. AI supports decisions, and a qualified person remains responsible for them. A diagnostic tool can suggest, but a clinician decides. An operations tool can predict, but a manager decides what to do with the prediction. This course never gives clinical advice, and it never treats AI as a replacement for clinical judgement.

Here is a simple way to picture it. Think of AI as a well-read assistant who works very fast, but has never met the patient. The assistant can point out things worth checking, and prepare drafts. The senior clinician still examines the patient, weighs the context, and signs the decision.

Let's look at three hypothetical settings. None of them describes a real organisation. First, a district hospital in Ghana. Doctor Kwame Asante leads the outpatient department. A diagnostic support tool marks chest X-rays that may need urgent review, so radiology staff can look at those first.

The tool does not write the report. The radiologist reads every image, and remains accountable for the result. Second, a clinic network in India. Priya Raghunathan manages twelve primary care clinics. A prediction tool estimates which booked patients are likely to miss their appointment.

Priya's team uses these predictions to send extra reminders and offer phone consultations, not to cancel bookings. The clinic manager is accountable for how the predictions are used.

Third, a telehealth service in Chile. Valentina Soto coordinates a service that answers patient questions by text message. An AI assistant drafts answers to general questions, using content that clinicians have approved. Any message that mentions chest pain, breathing problems or thoughts of self-harm goes straight to a nurse. The clinical lead is accountable for the approved content and the escalation rules.

One common mistake is to think that a highly accurate tool can decide by itself, and the clinician only checks the difficult cases. This is not safe. Even an accurate tool makes errors, often in cases that look easy to the tool. And accountability cannot pass to software. Design every use so that a named person makes, or clearly approves, each decision.

Let's recap. First, AI in healthcare falls into four main areas: diagnostic support, operations, patient engagement and public health, and each uses different data. Second, AI supports decisions, and a qualified person remains responsible for every one. Third, for any tool, ask what decision it supports, who makes that decision, and how errors would be noticed.

Now it is your turn. In the exercise below this video, you will sort eight AI health applications into the four areas, and name the person who is accountable for each final decision. It takes about fifteen minutes. In the next lesson, we look at health data: its types, its quality, and its privacy. See you there.
```

## L02 Health Data: Types, Quality and Privacy

- **Filename:** `ai-25-ai-in-healthcare_M1_L02_presenter.mp4`
- **Expected length:** about 5.2 minutes (727 words). The quality gate accepts ±10%.

```text
An AI tool is only as good as the data it learned from. If blood pressure was missing for half of the older patients in the training data, what has the tool really learned about older patients?

In the last lesson, we mapped four areas of AI in healthcare. Every one of them runs on data. So in this lesson, we look at the main types of health data, the quality problems they bring, and why they need extra privacy protection.

Health AI uses six main types of data. Electronic health records are rich, but often incomplete, and recorded for care or billing, not research. Images depend on the device and the person taking them. Laboratory results are well structured, but units and methods differ between laboratories.

Wearables give continuous readings, but the people who own them are often younger and wealthier than the general population. Claims data is large and consistent, but shows what was paid for, not always what happened. Surveys reach people who do not use health services, but depend on memory and honest answers.

Three quality problems appear again and again. First, missing values. Data is rarely missing at random. A test may be missing because the clinician thought it was not needed, and that is information too. Second, different coding systems. Combining hospitals that record diagnoses differently creates errors. Third, unrepresentative samples. A model may work less well for groups that are rare in its data.

Health data can reveal illness, pregnancy, mental health or genetic information. Exposure can lead to discrimination, stigma or loss of work. Here is a simple way to think about it. A patient record is like a diary. In the hands of the patient's care team, it helps. In the wrong hands, it can cause real harm.

So treat every dataset as someone's diary, even when it looks like a table of numbers. In this course, you only use public or synthetic data. Synthetic data is made by a computer to look realistic, but it describes no real person. And never paste identifiable patient data into a public AI tool.

Let's see this with an example. Nguyen Thi Lan is a public health researcher in Vietnam. She is given a synthetic dataset of five hundred adult clinic patients, to plan an analysis of blood pressure control. Before any modelling, she explores it.

She lists the variables: age, sex, district, body mass index, systolic blood pressure, smoking status, HbA1c, and the date of the last visit. Then she counts the missing values. Remember, all of these numbers are synthetic. Smoking status is missing for thirty-one percent of patients. HbA1c for fifty-eight percent. Body mass index for twelve percent. Systolic blood pressure for four percent.

HbA1c is missing for more than half of the patients. Lan checks, and sees that it is recorded mostly for patients who already have a diabetes diagnosis. A model trained on this data might learn that HbA1c present means diabetes. That is a pattern in the recording process, not in the patients.

She also sees that eighty percent of rows come from two urban districts. She writes a note: results may not apply to rural districts. Finally, she asks the privacy question. If this data were real, could a person be identified? District, exact age and a rare diagnosis together could point to one person in a small district.

For real data, she would group ages into bands, remove exact dates, and follow her institution's data protection rules. This links to a common mistake. Many people believe data is anonymous once names are removed. In health data, this is often false. Treat de-identified data as still sensitive.

Let's recap. First, health AI uses records, images, laboratory results, wearables, claims and surveys, and each type has its own gaps and biases. Second, missing values, different coding systems and unrepresentative samples can teach a model patterns from the recording process, not from patients. Third, health data needs extra privacy protection, and identifiable data never goes into public AI tools.

Now it is your turn. In the exercise below this video, you will open the course's synthetic patient dataset, list its variables, count the missing values, and describe one privacy risk if the data were real. It takes about twenty-five minutes. In the next lesson, we look at how clinical AI models are built. See you there.
```

## L03 How Clinical AI Models Are Built

- **Filename:** `ai-25-ai-in-healthcare_M1_L03_presenter.mp4`
- **Expected length:** about 5.0 minutes (692 words). The quality gate accepts ±10%.

```text
A supplier tells you their tool was trained on one hundred thousand images. That sounds impressive. But who labelled those images? How were the right answers decided? And was the tool ever tested in a hospital like yours?

In the last lesson, we saw how the quality of health data shapes what a model learns. Now we follow the steps behind one sentence in a supplier's brochure. A clinical AI model is built in a sequence of steps, and at almost every step, clinicians have a role that data scientists cannot fill alone.

Step one is the clinical question and intended use. What decision should the tool support, for which patients, in which setting, and by whom? Step two is data collection, with ethics approval and data protection in place. Clinicians judge whether the patients and devices in the data match real practice.

Step three is labelling. Each example needs a correct answer, called a label. The method used to decide that answer is the reference standard, for example agreement between two specialists, or a later confirmed diagnosis. Clinicians set the labelling rules and resolve disagreements. Step four splits the data into training, validation and test sets, and data from one patient must stay in one set.

Step five is training, which is mainly technical. Step six is internal testing on the held-back test set, where clinicians review errors and judge which ones are serious. Step seven is external validation on data from other hospitals, devices or populations. This is where many tools perform worse. Step eight is clinical evaluation in the real workflow, followed by monitoring.

Here is a simple way to picture it. A model in training is like a trainee who studies thousands of annotated images under supervision. The trainee is only as good as the teachers' notes. And before anyone relies on the trainee, a senior colleague checks their work, first on familiar cases, then in new settings.

A tool that has only passed the first check is still a trainee.

Let's follow one hypothetical project. Doctor Beatriz Nogueira is a cardiologist in Brazil. A health-tech team asks her to join the development of a tool that flags ECGs that may show atrial fibrillation, for specialist review.

At step one, the team's draft intended use says, diagnose arrhythmia. Beatriz changes it to: flag twelve-lead ECGs from adult outpatients for cardiologist review. This is narrower and testable, and it makes clear that a cardiologist decides.

At step three, the team planned to use the automatic interpretation printed by the ECG machine as the label. Beatriz explains that this would teach the model to copy the machine, including its mistakes. They agree that two cardiologists will label each ECG, and a third will decide when they disagree.

At step four, she asks whether ECGs from the same patient appear in both the training and test sets. They do, so the split is redone by patient. At step seven, the team only has data from one private hospital in a large city. Beatriz asks for an external test set from a public hospital with different ECG machines, before anyone discusses clinical use.

None of these points needed programming skill. All of them needed clinical knowledge. And notice a common mistake. A large dataset does not guarantee a good model. Size cannot fix poor labels, or data from only one type of hospital. Ask how the labels were made before you ask how many there are.

Let's recap. First, clinical AI is built in a sequence: intended use, data and governance, labelling, splitting, training, internal testing, external validation, and clinical evaluation with monitoring. Second, the reference standard and the quality of labels set the upper limit on how good a model can be. Third, clinicians are needed at almost every step.

Now it is your turn. In the exercise below this video, you will ask Claude or ChatGPT to outline the steps for a hypothetical eye-screening support tool. You will mark where clinician input is needed, and correct what the assistant gets wrong. It takes about twenty-five minutes. In the next lesson, we learn how to read performance claims. See you there.
```

## L04 Reading Performance Claims

- **Filename:** `ai-25-ai-in-healthcare_M1_L04_presenter.mp4`
- **Expected length:** about 5.0 minutes (695 words). The quality gate accepts ±10%.

```text
A brochure says a tool is ninety percent accurate. You use it on a thousand patients in a screening clinic, and for every correct alert, there are about eleven false ones. Nobody lied. This lesson explains how that happens.

In the last lesson, we followed how a clinical model is built and tested. Now we learn to read the numbers that come out of that testing. Every result from a yes or no tool falls into one of four boxes, called a confusion matrix.

From these four boxes come the measures in performance claims. Sensitivity asks: of the people who have the condition, what share does the tool find? Specificity asks: of the people who do not have it, what share does the tool correctly clear? Positive predictive value asks: when the tool says positive, how often is it right?

Sensitivity and specificity describe the tool. But predictive values depend on the tool and on how common the condition is in the people tested. This is called prevalence. When a condition is rare, even a small false positive rate produces many false alarms, compared with the few true cases. A single accuracy number can hide this.

When a condition is rare, a tool that says negative for everyone can have very high accuracy, and still miss every case.

Here is a simple way to picture it. Think of a smoke alarm. A sensitive alarm rarely misses a fire. But in a kitchen where people cook every day, it will often sound for toast. Real fires are rare, so most alarms are false, even though the alarm works exactly as designed.

Let's work through an example. All the numbers here are synthetic, created for teaching. Doctor Aigerim Seitkali, a hospital physician in Kazakhstan, is reviewing a hypothetical tool that flags a condition for specialist review. The supplier states a sensitivity of ninety percent and a specificity of ninety percent. She works through a thousand synthetic patients in two settings.

Setting one is a specialist clinic, where the prevalence is ten percent. So one hundred of the thousand patients have the condition. The tool finds ninety of them, and misses ten. Of the nine hundred without the condition, it wrongly flags ninety.

So when the tool says positive, it is right ninety times out of one hundred and eighty. The positive predictive value is fifty percent. Half of the flags are real cases. And when it says negative, it is right ninety-eight point eight percent of the time.

Setting two is general screening, where the prevalence is one percent. Now only ten of the thousand patients have the condition. The tool finds nine and misses one. But of the nine hundred and ninety without the condition, it wrongly flags ninety-nine.

Sensitivity is still ninety percent, and specificity is still ninety percent. But the positive predictive value falls to eight point three percent, while the negative predictive value is ninety-nine point nine percent. Only about one in twelve flags is a true case, and specialists would review about eleven false alarms for each real one.

The tool is identical in both settings. Aigerim concludes that it may be useful in the specialist clinic, but needs a careful review of workload and harm before any use in screening. A common mistake is to read sensitivity as the chance that a positive result is correct. That is positive predictive value, and it falls sharply when a condition is rare.

Let's recap. First, sensitivity and specificity describe how the tool behaves in people with and without the condition, while predictive values tell you how far to trust a result. Second, positive predictive value depends on prevalence, so the same tool gives many more false alarms when a condition is rare. Third, check any real figure against its published source and setting.

Now it is your turn. In the exercise below this video, you will use a synthetic results table to calculate sensitivity, specificity and positive predictive value at two prevalence levels, and explain the difference in two sentences. It takes about twenty minutes. In the next lesson, we look at levels of evidence, from study to real-world use. See you there.
```

## L05 Levels of Evidence: From Study to Real-World Use

- **Filename:** `ai-25-ai-in-healthcare_M1_L05_presenter.mp4`
- **Expected length:** about 5.2 minutes (729 words). The quality gate accepts ±10%.

```text
Two suppliers show you the same sensitivity figure. One measured it on old images from a single hospital. The other measured it in a trial where patients' care was actually affected. Are these claims equally strong? No, and knowing why is a vital skill.

In the last lesson, we learned to read performance numbers. Now we ask a different question. How strong is the study behind those numbers? Evidence for a clinical AI tool builds up in stages, and each stage answers a harder and more important question.

The first stage is a retrospective study at a single site. The model is tested on past data from the same source it was trained on. It answers the question: can the model find the pattern at all? But the test data looks very like the training data, so results are often too optimistic.

The second stage is external validation. The model is tested on past data from other hospitals, devices or countries. It asks: does the performance hold in new settings? This often shows a drop. The third stage is a prospective study. The tool runs on new patients as they arrive, often in silent mode, where clinicians do not see its output.

The fourth stage is a randomised controlled trial, or a similar comparative study. Patients or sites are randomly assigned to care with or without the tool. It asks the most important question: does using the tool improve outcomes that matter to patients, compared with current practice?

Higher accuracy is not the same as better care. A tool can find more cases and still not help, if clinicians ignore its alerts, or if it delays other work. And accuracy in one study often falls in a new hospital, because of different patients, devices, prevalence and workflows.

Here is a simple way to picture it. A new medicine is not trusted on laboratory results alone. It must show that it is safe and helps real patients in careful clinical studies. An AI tool that has only passed a retrospective test is still at the laboratory stage.

Reporting guidelines also exist to help authors describe AI studies completely, and help readers judge them. A statement that a study followed one is a good sign, but you still need to read what the study actually did.

Let's see this in practice. Doctor Olusegun Adeyemi chairs a hypothetical digital health committee at a teaching hospital in Nigeria. Three suppliers present tools that flag possible sepsis for rapid clinical review. The committee sorts the evidence.

Supplier one reports high sensitivity on twenty thousand past records from one hospital abroad. That is a retrospective, single-site study. The committee notes that the patients, laboratory tests and nursing observation schedules may differ from its own.

Supplier two reports results on past records from five hospitals in three countries, with a lower but stable sensitivity. That is external validation, which is stronger. Supplier three reports a prospective study in two hospitals, where the tool ran silently for six months, and its alerts were compared with later confirmed diagnoses.

That shows real-time performance, but not whether patient outcomes improve. None of the suppliers has a randomised trial. The committee does not reject all three. It picks supplier three's tool for a local silent-mode evaluation, with a decision point before any clinician sees the alerts. It also asks all suppliers whether they followed a recognised reporting guideline.

A common mistake is to treat a large retrospective study as strong evidence because the numbers are big. A study on one million past images still only shows that the model can find a pattern in data like its training data. Look at the study design first, then at the size.

Let's recap. First, evidence builds from retrospective single-site studies, to external validation, to prospective studies, to randomised or comparative trials of patient outcomes. Second, performance often falls in new settings because of different patients, devices, prevalence and workflows. Third, reporting guidelines help you judge a study, but you must still read its design and setting.

Now it is your turn. In the exercise below this video, you will rank four hypothetical evidence summaries from weakest to strongest, and write what extra evidence each would need before clinical use. It takes about twenty minutes. This completes week one. Next week, we start with AI for hospital and clinic operations. See you there.
```
