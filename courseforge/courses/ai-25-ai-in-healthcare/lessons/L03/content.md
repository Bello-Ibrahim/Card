# L03 How Clinical AI Models Are Built

Course: AI-25 · Module: M1 · Objectives: O2 · Video: 5 min

## Hook
A supplier tells you their tool "was trained on 100,000 images". That sounds impressive. But who labelled those images, how were the right answers decided, and was the tool ever tested in a hospital like yours? This lesson shows the steps behind that one sentence.

## Explanation
A clinical AI model is built in a sequence of steps. At each step, clinicians have a role that data scientists cannot fill alone.

1. **Clinical question and intended use.** What decision should the tool support, for which patients, in which setting, and by whom? "Flag ECGs that may show atrial fibrillation for cardiologist review in adult outpatients" is a clear intended use. "Detect heart disease" is not. *Clinician role:* define the question and the patients it applies to.
2. **Data collection and governance.** Gather data that matches the intended use, with ethics approval and data protection in place. *Clinician role:* judge whether the patients and devices in the data match real practice.
3. **Labelling and the reference standard.** Each example needs a correct answer, called a label. The method used to decide the correct answer is the **reference standard**, for example agreement of two specialists, a later confirmed diagnosis, or a laboratory test. *Clinician role:* set the labelling rules, label the data, and resolve disagreements.
4. **Splitting the data.** Data is divided into a training set, a validation set used to tune the model, and a test set kept apart until the end. Data from the same patient must stay in one set, or the test becomes too easy. *Clinician role:* limited, but they should know the split was done by patient.
5. **Training.** The model learns patterns that link the inputs to the labels. This is mainly technical work.
6. **Internal testing.** The model is tested on the held-back test set from the same source. *Clinician role:* review errors case by case and judge which errors are clinically serious.
7. **External validation.** The model is tested on data from other hospitals, devices or populations. This is where many tools perform worse. *Clinician role:* help choose realistic external sites and interpret the results.
8. **Clinical evaluation and monitoring.** The tool is tested in real workflow, then monitored after it goes live. *Clinician role:* run the evaluation, report problems and decide whether the tool stays in use.

**Analogy:** A model in training is like a trainee who studies thousands of annotated images under supervision. The quality of the trainee depends on the quality of the teachers' notes. And before anyone relies on the trainee's reading, a senior colleague checks their work, first on familiar cases and then in new settings. A tool that has only passed the first check is still a trainee.

## Worked Example
Dr. Beatriz Nogueira is a cardiologist in Brazil. A hypothetical health-tech team asks her to join the development of a tool that flags ECGs that may show atrial fibrillation for specialist review.

She notices problems early. At step 1, the team's draft intended use says "diagnose arrhythmia". Beatriz changes it to "flag 12-lead ECGs from adult outpatients for cardiologist review", which is narrower and testable, and makes clear that a cardiologist decides.

At step 3, the team planned to use the automatic interpretation printed by the ECG machine as the label. Beatriz explains that this would teach the model to copy the machine, including its mistakes. They agree that two cardiologists will label each ECG, and a third will decide when they disagree.

At step 4, she asks whether ECGs from the same patient appear in both training and test sets. They do, so the split is redone by patient.

At step 7, the team only has data from one private hospital in a large city. Beatriz asks for an external test set from a public hospital with different ECG machines before anyone discusses clinical use.

None of these points needed programming skill. All of them needed clinical knowledge.

## Common Mistake
Many people believe that a large training dataset guarantees a good model. Size helps, but it cannot fix poor labels, a weak reference standard or data from only one type of hospital. A smaller dataset with careful specialist labels and a clean patient-level split is often more useful than a very large one labelled by an automatic system. Ask how the labels were made before you ask how many there are.

## Key Takeaways
1. Clinical AI is built through a sequence: intended use, data and governance, labelling, splitting, training, internal testing, external validation, and clinical evaluation with monitoring.
2. The reference standard and the quality of labels set the upper limit on how good a model can be.
3. Clinicians are needed at almost every step, especially defining intended use, labelling, reviewing errors and interpreting external validation.

## Hands-on Exercise
**Task:** Ask Claude or ChatGPT to outline the development steps for a hypothetical eye-screening support tool. Mark each step where clinician input is needed and correct anything the assistant gets wrong.
**Tools:** Claude or ChatGPT (free plan). Do not enter any patient data or images.
**Steps:**
1. Enter a prompt such as: "Outline the steps to develop and validate an AI tool that supports screening of retinal photographs in adults with diabetes, for review by an eye specialist. Use numbered steps."
2. Copy the answer into a document.
3. Compare it with the eight steps in this lesson. Note any missing step, especially the reference standard, patient-level splitting and external validation.
4. Next to each step, write "clinician input needed" or "mainly technical", with a short reason.
5. Correct anything the assistant got wrong or described too simply, such as claims that the tool can diagnose or replace an eye specialist.
**What good looks like:** An annotated outline with all eight stages present, clinician roles clearly marked, and at least two corrections or additions, for example adding external validation or changing "diagnose" to "support review by an eye specialist".
**Time:** about 25 minutes

## Review Flags
- Clinical reviewer sign-off required.
- The ECG tool and the development team in the worked example are hypothetical. A clinical reviewer should confirm that atrial fibrillation on 12-lead ECG is a reasonable illustrative use case and that no clinical advice is given.
