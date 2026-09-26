# HeyGen Batch Pack: AI-30 M2 (Data Protection Law and AI)

Course: AI Governance, Privacy and Compliance. Make one HeyGen video per lesson below, using these settings for every video.

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

## L06 Data Protection Principles Across the AI Lifecycle

- **Filename:** `ai-30-ai-governance-privacy-and-compliance_M2_L06_presenter.mp4`
- **Expected length:** about 4.9 minutes (687 words). The quality gate accepts ±10%.

```text
You already know the data protection principles. But what does data minimisation mean when a data scientist says, the model will be better if we give it everything? Today we see how the familiar principles apply at each stage of an AI system's life.

Welcome to module two, on data protection law and AI. As always, this course is educational and is not legal advice. The GDPR and the NDPA both set out core principles. Their wording is similar, but not identical, so always check both texts.

The principles you know are lawfulness, fairness and transparency, purpose limitation, data minimisation, accuracy, storage limitation, security, and accountability. AI does not change these principles. It changes where the pressure falls.

A simple AI lifecycle has five stages. First, data collection, where data is gathered or reused from other systems. The main pressure here is purpose limitation. Data collected to handle claims is now used for a new purpose, so you must check whether that purpose is compatible or needs its own basis.

Second, training. Here the pressure is on data minimisation and fairness. Teams want more fields and more history. And some fields, such as postcode, can act as a proxy for ethnicity or income, and create unfair outcomes.

Third, testing, where the pressure is on accuracy and fairness. Test error rates for different groups, not only the overall score. Fourth, deployment, where the pressure is on transparency and security. Tell people about the processing in clear words, and protect the system against attacks.

Fifth, retirement. The pressure is on storage limitation, because old datasets, copies and models may still hold personal data long after they are needed. And accountability runs across all five stages. You must be able to show how you applied each principle.

Think of water flowing through a treatment plant. The safety standards are the same at every point, but each stage has its own main danger: dirt at the intake, chemicals at treatment, leaks in the pipes. Inspectors check where the danger is greatest. The principles work the same way.

Let's see data minimisation in action. Youssef Benali is the data protection officer at a fictional insurer in Casablanca, Morocco, which also sells travel insurance to customers in France. So the GDPR may apply, alongside Moroccan law.

The claims team wants to train a model to flag possibly fraudulent claims, using ten years of claim files. Youssef asks: does the model need all ten years? Fraud patterns change, and older files reflect products the company no longer sells. The team agrees to test whether five years give similar results.

Next, the fields. The files contain names, ID numbers, medical notes from travel claims and free-text comments. The team replaces names and ID numbers with codes before training. Medical notes are health data, a special category, so they are left out unless a clear need and a valid condition are shown.

For testing, the team checks whether the model flags claims from some nationalities more often. And for retirement, it sets a rule to delete the training copy when the model is retrained. The result is a smaller dataset, with a documented reason for each field.

A common mistake is to think that removing names makes data anonymous. Coded, or pseudonymised, data is still personal data if someone can link it back to a person. True anonymisation is hard. So treat pseudonymisation as a security control, not as a way to leave data protection law behind.

Let's recap. First, the same data protection principles apply at every AI stage: collection, training, testing, deployment and retirement. Second, each stage has a main pressure point, such as purpose limitation at collection and storage limitation at retirement. Third, pseudonymised data is still personal data.

In the exercise below this video, you will draw the five stages of an AI lifecycle. For each stage, write the one principle most at risk, and one control that protects it. Use the principles as written in the official texts of both laws.

In the next lesson, we look at one principle more closely: the lawful basis for AI processing. See you there.
```

## L07 Lawful Basis for AI Processing

- **Filename:** `ai-30-ai-governance-privacy-and-compliance_M2_L07_presenter.mp4`
- **Expected length:** about 4.9 minutes (675 words). The quality gate accepts ±10%.

```text
A retailer says, customers accepted our terms, so we can use their data to train our AI. Is that enough? Often it is not, because training a model and using it are different processing activities, and each one needs its own lawful basis.

Last time, we followed the principles across the AI lifecycle. Now we focus on lawfulness. Remember, this course is educational and is not legal advice. The GDPR and the NDPA both list lawful bases. The lists are similar, but check the exact wording and conditions in each.

Under the GDPR, the lawful bases are consent, contract, legal obligation, vital interests, public task and legitimate interests. The NDPA contains a comparable list. For private-sector AI, three bases come up most often.

Consent must be freely given, specific, informed and unambiguous, and easy to withdraw. That makes it hard to use for training, because withdrawal may mean removing a person's data from a model. Contract covers only what is genuinely necessary to deliver a contract with the person. Training a general model usually is not.

Legitimate interests needs a three-part test. Is the purpose legitimate? Is the processing necessary for that purpose? And in a balancing test, are the organisation's interests overridden by the person's interests, rights and freedoms? Regulators have published guidance on using this basis for AI.

So split your AI processing into separate activities, such as collecting data, training the model and using the model on a person. Each activity needs a basis, and the answer may be different for each one.

Special category data, such as health data, biometric data used for identification, ethnic origin or religion, needs a lawful basis and an extra condition, such as explicit consent. And AI can infer special category data from ordinary data, which may bring it into scope.

Think of a lawful basis as a ticket for a specific train. A ticket from Warsaw to Kraków does not let you continue to Vienna. If you want to take the data further, to a new purpose, check whether your ticket covers that journey, or whether you need a new one.

Let's see this in practice. Magdalena Nowak is a privacy lawyer for a fictional online fashion retailer in Poznań, Poland. The retailer wants an AI system that recommends products based on browsing and purchase history.

Magdalena separates two activities: training the model on past purchases, and showing recommendations to a logged-in customer. For both, contract is weak, and consent is possible but hard to manage in a trained model. Legitimate interests looks possible, if the balancing test is met.

So she runs the test. The purpose, relevant product suggestions, is legitimate. For necessity, history in the retailer's own shop is needed, but data bought from third parties is not. For balancing, customers would reasonably expect some suggestions from a shop they use.

But risks rise if the model infers sensitive facts, such as pregnancy or health conditions. Her controls: exclude sensitive product categories from training, give a simple opt-out and explain it clearly in the privacy notice. She records her conclusion and marks it for review against regulator guidance.

A common mistake is to choose consent to be safe. Consent is not safer if people cannot really refuse, or if you cannot honour a withdrawal. And if consent is withdrawn, you usually cannot simply switch to another basis. Choose the most suitable basis at the start, and document why.

Let's recap. First, every processing activity needs a lawful basis, and training a model may need a different basis from using it. Second, legitimate interests needs a documented three-part test: purpose, necessity and balancing, with controls that protect people. Third, special category data needs an extra condition, and AI may infer it.

In the exercise below this video, you will take three fictional AI processing activities and choose the most suitable lawful basis for each, under the GDPR and under the NDPA. Justify each choice in two sentences.

In the next lesson, we turn to Nigeria: the NDPA's structure and key duties. See you there.
```

## L08 Nigeria's NDPA: Structure and Key Duties

- **Filename:** `ai-30-ai-governance-privacy-and-compliance_M2_L08_presenter.mp4`
- **Expected length:** about 4.9 minutes (685 words). The quality gate accepts ±10%.

```text
Many AI governance courses stop at the EU. But if your organisation processes personal data of people in Nigeria, the NDPA has its own structure, its own regulator and its own duties. How does it apply when a Nigerian fintech uses AI to decide who gets credit?

In the last lesson, we compared lawful bases under both laws. Now we look at the NDPA on its own terms. This lesson is educational and is not legal advice. Nigerian rules are developing, and implementing guidance may add detail, so check every point against current official sources.

GDPR professionals will recognise the structure. First, the Act sets up a national regulator, with powers to issue regulations and guidance, investigate complaints and impose sanctions. Its guidance can add practical duties, so read it alongside the Act.

Duties fall on data controllers and data processors. The principles are similar to the GDPR, from lawful, fair and transparent processing to accountability. There is a comparable list of lawful bases, with extra conditions for sensitive personal data.

People have rights such as information, access, correction, erasure and objection, and protections about automated decisions, which we cover in the next lesson. These rights still apply when the data sits inside an AI system.

Controllers must apply appropriate security measures and handle personal data breaches, including notification in some cases. And processing likely to create a high risk to people requires a data protection impact assessment.

Transfers of personal data out of Nigeria are allowed only on permitted grounds, such as adequate protection in the receiving country or other recognised safeguards. AI projects often send data abroad, for example to cloud hosting or model providers, so this duty matters.

Finally, the regulator can classify some organisations as being of greater importance, which may bring extra duties, such as registration, a data protection officer, or regular filings. The classification criteria and the sanctions for breaches must be checked in the relevant provisions.

Think of driving in a new country. The steering wheel, pedals and main road signs are familiar. But the speed limits, licence rules and the police who enforce them are local. The NDPA is familiar in shape, but its local rules must be learned on their own terms.

Hauwa Bello is head of compliance at a fictional fintech in Abuja. It plans to use an AI model to score applicants for small business loans, using bank statements, mobile phone usage data and information from applicants.

Hauwa lists the duties that are likely to apply. First, choose and record a lawful basis for training and for scoring, and explain the AI scoring in plain words in the privacy notice. Second, if loans are refused without human involvement, apply the automated decision protections, including a way to ask for human review.

Third, credit scoring with new data types is likely high risk, so a DPIA should be completed before launch. Fourth, the model is hosted by a cloud provider outside Nigeria, so a valid transfer ground must be confirmed and recorded. Fifth, the fintech must check whether it falls into a category with extra duties.

She adds one more point. The mobile usage data may reveal sensitive facts, so she asks the data team to justify each field.

A common mistake is to assume that complying with the GDPR means complying with the NDPA. The principles overlap, but local duties such as registration, filings, transfer grounds and the regulator's guidance can differ. Keep a separate NDPA column in your compliance map.

Let's recap. First, the NDPA sets up a national regulator and places duties on data controllers and processors, in a structure similar to the GDPR. Second, key duties cover principles, lawful bases, rights, security, impact assessments and cross-border transfers. Third, some organisations may carry extra duties, depending on their classification.

In the exercise below this video, you will read an official NDPA summary or guidance note from the regulator, and list five duties that would apply to a fictional fintech in Abuja using AI for credit scoring.

In the next lesson, we look at data subject rights and automated decisions. See you there.
```

## L09 Data Subject Rights and Automated Decisions

- **Filename:** `ai-30-ai-governance-privacy-and-compliance_M2_L09_presenter.mp4`
- **Expected length:** about 4.9 minutes (686 words). The quality gate accepts ±10%.

```text
A customer writes: your system refused my loan in two seconds. Why? And I want a real person to look at it. Your team has a response deadline, and a trained model that nobody can easily explain. What do you do first?

Last time, we looked at the NDPA's structure. Today, we look at people's rights under both data protection laws, and at automated decisions. As always, this lesson is educational and is not legal advice.

You know the main rights already: information, access, correction, erasure, restriction, objection and portability. AI makes some of them harder. For access, people can ask for their data, including the inputs used about them, outputs such as a score, and meaningful information about the logic involved.

If input data is wrong, correct it, and consider whether the decision must be made again. Erasure is harder. Deleting a record from a database is simple. Removing its influence from a trained model is not. So decide in advance how you will respond, for example by removing the data from future training sets.

Both laws include protections for decisions based solely on automated processing that have legal or similarly significant effects, such as refusing credit. These decisions are allowed only in certain situations, and people usually have safeguards: the right to human intervention, to express their point of view and to contest the decision.

And human review must be meaningful. A reviewer who simply approves every AI output does not make the decision any less automated. The reviewer needs authority to change the outcome, access to the relevant information, and enough time and training to use them.

Think of a ticket machine that rejects your payment with no staff nearby. The right to human intervention puts a person next to the machine, who can look at your case, explain what happened and override the machine if it made a mistake.

Let's follow one request. Funmilayo Adeyemi applies online for a personal loan from a fictional digital lender in Lagos. The AI system refuses her in seconds. She writes asking why, and asks for a human review.

The lender's data protection officer follows its procedure. First, the request is logged with the date received, and her identity is confirmed using details the lender already holds. Second, the team identifies the rights: an access request, and a request for human intervention in a solely automated decision.

Third, the team gathers the facts: the input data, her score and the main factors, such as a short credit history and many recent applications. Fourth, it checks the data. Funmilayo says one recorded loan was repaid. The record is out of date, so the team corrects it.

Fifth, a trained credit officer with authority to change the outcome reviews the application with the corrected data and her comments. The officer approves a smaller loan.

Sixth, the lender replies within the legal time limit, in a plain-language letter that explains the main factors, the correction and the new decision, and how to complain to the regulator. Seventh, the officer reports the out-of-date data source for a wider check.

A common mistake is to think that explaining an AI decision means publishing the model's code or maths. People rarely need that. A meaningful explanation describes the main factors behind this person's outcome, in words they understand, and what they could do differently. Another mistake is to treat any human involvement as enough.

Let's recap. First, rights such as access, correction, erasure and objection still apply to AI, but are harder to honour inside a trained model, so plan your responses in advance. Second, both laws protect people from solely automated decisions with significant effects. Third, human review must be meaningful, with authority, information and training.

In the exercise below this video, you will write a step-by-step internal procedure for a fictional AI system. It should cover two requests: an access request, and a request for human review of an automated decision. Keep it practical, so that a new team member could follow it.

In the next lesson, we look at impact assessments: DPIAs and AI risk assessments. See you there.
```

## L10 Impact Assessments: DPIAs and AI Risk Assessments

- **Filename:** `ai-30-ai-governance-privacy-and-compliance_M2_L10_presenter.mp4`
- **Expected length:** about 4.9 minutes (677 words). The quality gate accepts ±10%.

```text
A project team says, the system is ready, we just need you to sign the DPIA by Friday. If the assessment starts when the system is finished, it can only describe risks, not prevent them. So when should it start?

In the last lesson, we handled rights requests. Today, we look at impact assessments, and how to judge whether the remaining risk is acceptable. This lesson is educational and is not legal advice. When each assessment is required, and what it must contain, must be checked for each law.

Under both the GDPR and the NDPA, a data protection impact assessment, or DPIA, is required when processing is likely to result in a high risk to people's rights and freedoms. Many AI uses meet that test, because they often involve new technology, large-scale data, profiling, automated decisions, sensitive data or monitoring.

A DPIA usually has four parts. First, a description of the processing, its purpose, data, people affected and recipients. Second, necessity and proportionality: why the processing is needed, its lawful basis and how rights are respected. Third, the risks to people, rated by likelihood and severity.

Fourth, the measures that reduce each risk, and the residual risk that remains after them. If high residual risk remains, you may need to consult the regulator before you start.

The EU AI Act adds its own assessment. Some deployers of high-risk systems must carry out a fundamental rights impact assessment before use. It looks wider than privacy, at issues like non-discrimination and access to services. It can build on an existing DPIA, and many organisations combine both in one process.

To judge residual risk, ask three questions. After the controls, is the remaining risk low enough, given the benefit? Is it within the organisation's risk appetite? Are the people affected protected by meaningful safeguards? Then record who made the judgement, and why.

Think of an architect's structural review, done while the plans are still on paper. Moving a wall at the drawing stage costs little. Moving it after the building is finished is expensive, and sometimes impossible. So start the assessment while the design can still change.

Let's look at a short DPIA. Thandiwe Mokoena is privacy manager for a fictional company whose office in Johannesburg plans a facial-recognition entry system to replace staff access cards. Local data protection law must also be checked.

Description: cameras match the faces of about three hundred staff against enrolled templates, which is biometric data used for identification. Necessity: cards work but are often shared. Would a card plus a PIN be enough? And staff may feel they cannot refuse their employer.

Risks: leaked biometric templates, which is high severity. False rejections that affect some groups more than others. And function creep, such as using the cameras to track attendance.

Measures: a card-plus-PIN alternative with no disadvantage, encrypted templates stored on-site and deleted when staff leave, error-rate tests across groups, and a written ban on using the system for attendance. With these, Thandiwe rates the residual risk as medium, and recommends a volunteer pilot with a review after three months.

A common mistake is to treat a DPIA as a form to complete at the end. Its value is in the changes it causes. Another mistake is to rate risks to the organisation, such as fines, instead of risks to people. A DPIA must focus on the people affected.

Let's recap. First, a DPIA is required when processing is likely to result in high risk to people, and many AI uses meet that test. Second, some deployers of high-risk AI systems must also carry out a fundamental rights impact assessment, which can be combined with the DPIA. Third, start early, focus on people, and record who judged the residual risk acceptable.

In the exercise below this video, you will complete a free DPIA template for a fictional AI chatbot that handles customer complaints. Then judge whether the remaining risk is acceptable, and explain why.

That completes module two. In the next lesson, we start building: designing an AI governance framework. See you there.
```
