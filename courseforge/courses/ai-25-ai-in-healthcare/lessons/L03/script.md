# L03 How Clinical AI Models Are Built | Presenter Script

Course: AI-25 · Video: 5 min · Words: 697

## Hook
A supplier tells you their tool was trained on one hundred thousand images. That sounds impressive. But who labelled those images? How were the right answers decided? And was the tool ever tested in a hospital like yours?

## Explain
In the last lesson, we saw how the quality of health data shapes what a model learns. Now we follow the steps behind one sentence in a supplier's brochure. A clinical AI model is built in a sequence of steps, and at almost every step, clinicians have a role that data scientists cannot fill alone.

Step one is the clinical question and intended use. What decision should the tool support, for which patients, in which setting, and by whom? Step two is data collection, with ethics approval and data protection in place. Clinicians judge whether the patients and devices in the data match real practice.

Step three is labelling. Each example needs a correct answer, called a label. The method used to decide that answer is the reference standard, for example agreement between two specialists, or a later confirmed diagnosis. Clinicians set the labelling rules and resolve disagreements. Step four splits the data into training, validation and test sets, and data from one patient must stay in one set.

Step five is training, which is mainly technical. Step six is internal testing on the held-back test set, where clinicians review errors and judge which ones are serious. Step seven is external validation on data from other hospitals, devices or populations. This is where many tools perform worse. Step eight is clinical evaluation in the real workflow, followed by monitoring.

Here is a simple way to picture it. A model in training is like a trainee who studies thousands of annotated images under supervision. The trainee is only as good as the teachers' notes. And before anyone relies on the trainee, a senior colleague checks their work, first on familiar cases, then in new settings.

A tool that has only passed the first check is still a trainee.

## Demonstrate
Let's follow one hypothetical project. Doctor Beatriz Nogueira is a cardiologist in Brazil. A health-tech team asks her to join the development of a tool that flags ECGs that may show atrial fibrillation, for specialist review.

At step one, the team's draft intended use says, diagnose arrhythmia. Beatriz changes it to: flag twelve-lead ECGs from adult outpatients for cardiologist review. This is narrower and testable, and it makes clear that a cardiologist decides.

At step three, the team planned to use the automatic interpretation printed by the ECG machine as the label. Beatriz explains that this would teach the model to copy the machine, including its mistakes. They agree that two cardiologists will label each ECG, and a third will decide when they disagree.

At step four, she asks whether ECGs from the same patient appear in both the training and test sets. They do, so the split is redone by patient. At step seven, the team only has data from one private hospital in a large city. Beatriz asks for an external test set from a public hospital with different ECG machines, before anyone discusses clinical use.

None of these points needed programming skill. All of them needed clinical knowledge. And notice a common mistake. A large dataset does not guarantee a good model. Size cannot fix poor labels, or data from only one type of hospital. Ask how the labels were made before you ask how many there are.

## Recap
Let's recap. First, clinical AI is built in a sequence: intended use, data and governance, labelling, splitting, training, internal testing, external validation, and clinical evaluation with monitoring. Second, the reference standard and the quality of labels set the upper limit on how good a model can be. Third, clinicians are needed at almost every step.

## CTA
Now it is your turn. In the exercise below this video, you will ask Claude or ChatGPT to outline the steps for a hypothetical eye-screening support tool. You will mark where clinician input is needed, and correct what the assistant gets wrong. It takes about twenty-five minutes. In the next lesson, we learn how to read performance claims. See you there.

## Thumbnail
Headline: Who Labelled the Data?
Image: Navy background, a stack of ECG strips with small teal tick labels and a clinician's hand holding a pen, headline in teal Inter Bold.

## Production Notes
- Clinical reviewer sign-off required.
- A clinical reviewer should confirm that flagging atrial fibrillation on 12-lead ECGs for cardiologist review is a reasonable illustrative use case and that no clinical advice is given (content.md Review Flags).
- Dr. Beatriz Nogueira (Brazil) and the health-tech team are hypothetical. ECG images on slides must be generic illustrations, not real patient tracings, with no readable names or dates.
- The script describes the tool as supporting review only: it never diagnoses. Keep on-screen text consistent.
