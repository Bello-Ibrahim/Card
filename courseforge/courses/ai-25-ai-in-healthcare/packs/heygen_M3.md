# HeyGen Batch Pack: AI-25 M3 (Evaluate and Implement Safely)

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

## L11 Regulation, Privacy and Ethics Frameworks

- **Filename:** `ai-25-ai-in-healthcare_M3_L11_presenter.mp4`
- **Expected length:** about 5.0 minutes (702 words). The quality gate accepts ±10%.

```text
Is your AI tool a medical device? Can patient photos leave the country? The answers depend on where you are. But the questions are almost the same everywhere. This lesson teaches the questions.

Welcome to week three, where you build your capstone. We start with the rules around AI tools. Rules differ by country and change over time. So this course teaches the common principles found in most frameworks, not the rules of one country. There are six of them.

The first is software as a medical device. In many countries, software intended to diagnose, treat, monitor or prevent disease can be regulated as a device, even with no hardware. Intended use is central. A scheduling tool is usually not a medical device. A tool that flags possible cancer on images usually is.

The second is risk-based classification. A tool that informs a serious diagnosis or drives treatment usually sits in a higher class, with stricter evidence and oversight. The third is data protection. Health data is usually a sensitive category, with rules on lawful use, collecting only what is needed, security, transfer across borders, and patients' right to access their data.

The fourth is consent. Depending on the law and the use, patients may need to consent, be informed, or be able to object. Consent for care is not automatically consent for training an AI model. The fifth is transparency. Patients and clinicians should know when AI is used, what it is for, and its limits. The sixth is accountability, meaning clear responsibility for performance, decisions and fixing problems.

International guidance brings principles like these together, and the lesson page gives examples of regulators and laws in some regions. But they are examples only. Always confirm local rules with your organisation's regulatory affairs lead or data protection officer.

Here is a simple way to picture it. Regulation is like building safety codes. The details differ from city to city. But every code asks similar questions. What is the building for? How many people will use it? What happens in a fire? And who signs off?

Let's see how to use the principles. Achieng Otieno is the product lead for a hypothetical health-tech start-up in Kenya. Her team is building a tool that suggests which antenatal patients may need earlier review, for midwives to consider. She plans to sell it in Kenya, and possibly in Europe.

She does not try to become a lawyer. Instead, she uses the six principles to prepare questions. On medical devices, she asks: our intended use is to support midwives in prioritising review. Does this make it a medical device here, and in which risk class? On data protection: is antenatal data a sensitive category, and can we store it with a cloud provider outside the country?

On consent: do we need separate consent to use past records to train the model? On transparency: what must we tell patients about the tool? And on accountability: if the tool misses a high-risk patient, who is responsible, and how do we report it? Next to every question, she writes the same words: to check locally.

She takes the list to the company's legal adviser and a data protection specialist. For Europe, she plans separate advice.

A common mistake is to believe that decision support cannot be a medical device, because a clinician makes the final decision. This is often not true. Many frameworks regulate decision support based on its intended use and risk. Do not decide this yourself. Ask your regulatory lead.

Let's recap. First, the common principles are software as a medical device, risk-based classification, data protection, consent, transparency and accountability. Second, intended use is central to whether and how a tool is regulated. Third, named laws and regulators are only examples, so always confirm local rules with your regulatory or data protection officer.

Now it is your turn. In the exercise below this video, you will choose one AI health tool category and write questions for your local regulator or data protection officer, marking each one to check locally. It takes about twenty minutes. Your answers will feed your capstone evaluation. In the next lesson, we cover choosing a tool and assessing clinical value. See you there.
```

## L12 Choosing a Tool and Assessing Clinical Value

- **Filename:** `ai-25-ai-in-healthcare_M3_L12_presenter.mp4`
- **Expected length:** about 4.9 minutes (680 words). The quality gate accepts ±10%.

```text
Our tool uses advanced AI. That is not a reason to use it in a clinic. The first question for any tool is simpler, and harder. What will be better, for which patients, compared with what we do today?

Your capstone is a written evaluation of an AI health tool. You build it in three steps, across this lesson and the next two. First, choose a tool. It can be a hypothetical tool that you describe yourself, or a real tool described only from its public documentation. Do not make claims beyond what that documentation says.

Your evaluation follows a ten-section template. It starts with the tool description and clinical value, moves through evidence, data and privacy, bias, risks, workflow and regulation, and ends with a safe implementation plan and a clear recommendation. Today, you write the first two sections.

The intended use statement is one or two sentences. It says what the tool does, for which patients, in which setting, for which user, and what decision it supports. For example, the tool flags twelve-lead ECGs from adult outpatients that may show atrial fibrillation, for review by a cardiologist, who makes the diagnosis.

Clinical value answers four questions. The problem: what current problem does the tool address? The outcome: which outcome should improve, and how will you measure it? For whom: which patients benefit, and could any benefit less? And compared with what: what is current practice, and what suggests the tool is better? Also think about hidden costs, such as staff time to review outputs.

Here is a simple way to picture it. Assessing clinical value is like deciding whether to add a new test to a care pathway. A test that is accurate, but changes no decisions, only adds cost and delay. It is worth adding only if its result leads to better care for someone.

Let's see an example. Farah Haddad is a health-tech product analyst in Jordan. For her capstone, she chooses a hypothetical tool. It flags adults with diabetes who are overdue for eye screening and more likely to miss it, so that primary care nurses can contact them.

Her intended use statement says that the tool identifies adults with diabetes in a primary care network who are overdue for retinal screening, and ranks them by how likely they are not to attend, for nurses to contact and support. And it adds one clear line. It does not diagnose eye disease.

For clinical value, she writes the problem: many patients are overdue, and nurses have limited time to contact everyone. The outcome: the share of patients screened on time, measured for all patients, and by age, sex and district. For whom: overdue adults with diabetes, with a risk that patients without a mobile phone are contacted less.

Compared with what: current practice is a monthly list sorted by date. She notes that there is no evidence yet that ranking by risk works better than contacting everyone who is overdue, so this must be tested. Her conclusion is honest. The potential value is clear, but not yet shown.

A common mistake is to describe what the tool does, such as detecting a condition with high sensitivity, and call that clinical value. Performance is not value. Value is a change in care or outcomes for patients, compared with current practice.

Let's recap. First, the capstone evaluates a hypothetical tool, or a real tool described only from its public documentation, using public or synthetic information. Second, an intended use statement names what the tool does, for whom, where, for which user, and which decision it supports. Third, clinical value means a better outcome for defined patients compared with current practice.

Now it is your turn. This exercise is capstone step one. You will write the intended use statement and the clinical value section of your evaluation, and check them against the capstone rubric. If you choose a real tool, save the links to its public documentation. It takes about forty minutes. In the next lesson, we build the risk assessment for an AI health tool. See you there.
```

## L13 Risk Assessment for an AI Health Tool

- **Filename:** `ai-25-ai-in-healthcare_M3_L13_presenter.mp4`
- **Expected length:** about 4.9 minutes (679 words). The quality gate accepts ±10%.

```text
Every AI health tool has risks. A good evaluation does not pretend they are absent. It names them, judges how serious they are, and gives each one a mitigation and a person who owns it.

In the last lesson, you wrote your tool's intended use and clinical value. Now comes capstone step two, the risk assessment. A structured risk review looks at six areas, and each one links to an earlier lesson.

The six areas are clinical safety, such as missed cases and false alarms. Bias and equity, where some groups get less benefit. Privacy, meaning misuse or exposure of health data. Security, such as unauthorised access. Workflow, including automation bias and extra workload. And accountability, where responsibility for decisions and incidents is unclear.

For each risk, record a description of what could happen and to whom. Rate the likelihood and the severity as low, medium or high, with severity based on the worst realistic harm to a patient. Then write a mitigation, and name the role that owns it. A simple rule: any high-severity risk needs a mitigation in place before use, even if it seems unlikely.

Risks look different from different positions, so include clinicians who use the tool and receive its outputs, patients and community representatives, and data protection, security and safety staff. Patients often see risks that professionals miss, such as language barriers or distrust of automated messages.

Here is a simple way to picture it. A risk review is like a pre-flight check. The crew does not ask in general whether the aircraft is safe. They go through a list, system by system, and each item has a person who confirms it.

Let's see a risk table. Doctor Putri Wulandari leads quality improvement at a hypothetical district hospital in Indonesia. The hospital is considering a triage-support tool for the emergency department. It suggests a triage category from vital signs and the presenting complaint. The triage nurse makes the final decision.

Putri holds two workshops, one with emergency nurses and doctors, and one with community health volunteers and two patient representatives. The first risk is clinical safety. The tool might under-triage a patient with unusual symptoms. The mitigation is that the nurse decides, the tool cannot lower a category the nurse has chosen, and under-triage cases are reviewed every week.

Next, bias and equity. The tool may perform worse for older patients, and for patients who speak regional languages, whose complaints are recorded less fully. The quality lead checks performance by age group and language in silent mode before use. Privacy and security risks are rated low in likelihood but high in severity, and owned by the data protection officer and the IT security manager.

The workflow risk is high in both likelihood and severity. Nurses may accept suggestions without their own assessment at busy times. So the suggestion appears only after the nurse enters their own category. Finally, accountability. Nobody clearly reviews incidents, so the tool is added to incident reporting, and the governance group reviews it monthly, owned by the medical director.

Notice two things. The patient representatives raised the language risk, which the clinicians had not listed. And the nurses suggested the design change that reduces automation bias. A common mistake is writing mitigations like staff will be careful, with no owner. That is not a mitigation. It is a hope.

Let's recap. First, a structured risk review covers clinical safety, bias and equity, privacy, security, workflow and accountability. Second, each risk needs a likelihood, a severity, a specific mitigation and a named owner, and high-severity risks need mitigations before use. Third, clinicians, patients and community voices find different risks, so include them all.

Now it is your turn. This exercise is capstone step two. You will complete the risk section of your evaluation, with at least six risks, and a mitigation and an owner for each one. Then write two sentences on how patients or community representatives would review your table. It takes about forty-five minutes. In the next and final lesson, we write a safe implementation plan. See you there.
```

## L14 A Safe Implementation Plan

- **Filename:** `ai-25-ai-in-healthcare_M3_L14_presenter.mp4`
- **Expected length:** about 4.9 minutes (676 words). The quality gate accepts ±10%.

```text
A tool that passed every test can still fail on its first Monday in a real clinic. A safe implementation plan assumes this can happen, finds problems early, and knows in advance when to stop.

In the last lesson, you built your risk table. Now comes capstone step three, the implementation plan. A safe plan has seven parts. The first is silent-mode testing. The tool runs on real, current cases, but clinicians do not see its outputs, and care continues as usual. The team compares outputs with what actually happened, including by patient group.

The second part is a small pilot in one ward, clinic or team, for a fixed period, with extra support. The third is staff training on what the tool is for, what it is not for, its weaknesses, automation bias, and how to report problems. The fourth is a governance group that owns the tool, and decides whether to continue, change or stop.

The fifth part is monitoring. Decide in advance what you measure. Include performance, equity, meaning the same measures by patient group and site, use, such as how often outputs are overridden, and the clinical value outcome from your capstone. The sixth is feedback, an easy way for staff and patients to report problems.

The seventh part is stop criteria and a withdrawal plan. Before launch, write down what would make you pause or stop, such as performance falling in any patient group, a serious incident, or a data feed failure. And plan how care returns safely to the previous process.

Here is a simple way to picture it. A hospital does not install a new type of infusion pump on every ward on the same day. It tests it on one ward, trains the staff, and watches closely. If a problem appears, only one ward is affected, and the old pumps are still available.

Let's see a finished plan. Doctor Ayesha Siddiqui is a public health physician in Pakistan. Her capstone covers a hypothetical tool that flags chest X-rays that may show tuberculosis, for clinician review, in three district clinics.

First, three months of silent mode in one clinic, with results reported by sex, age band, HIV status and X-ray machine. Then a decision point. The governance group starts a pilot only if performance meets an agreed target in every group, and the review workload is acceptable.

The pilot runs for six months in one clinic. Clinicians see the tool's flag only after their own reading, a clinician reads every X-ray, and the tool never clears one alone. Staff get a one-hour training session. A governance group, chaired by the district medical officer and including a community representative, meets monthly.

She monitors performance against confirmed cases every month, overall and by group, along with overrides and the time from X-ray to test result. She pauses the tool if performance in any group falls below target for two months, if the data feed fails for more than a day, or after any serious incident.

Her recommendation is clear and conditional. Proceed to silent-mode evaluation, and do not use in routine care until the targets are met in every patient group. Remember, stopping a tool safely is a success of governance, not a failure.

Let's recap. First, a safe plan moves from silent-mode testing to a small pilot, with training, a governance group, monitoring and feedback. Second, monitor performance, equity, use and outcomes, with named people who review the results. Third, write stop criteria and a withdrawal plan before launch, and end your evaluation with a clear recommendation.

Now it is your turn. This exercise is capstone step three, the last one. You will write your implementation plan, finish your evaluation with a recommendation, and check it against the rubric and the submission checklist. It takes about fifty minutes.

Congratulations on completing AI in Healthcare. You can now judge an AI health tool's value, evidence and risks, and plan its safe use, with clinicians always in charge. Submit your capstone evaluation when it is ready. Thank you for learning with us.
```
