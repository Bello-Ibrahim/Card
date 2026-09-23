# L20 Capstone Step 3: Document Your Experiments

Course: AI-13 · Module: M4 · Objectives: O7 · Video: 5 min

## Hook
Imagine a colleague opens your capstone notebook six months from now. Can they tell what the model is for, what data it learned from, how you chose it, and where it fails? If not, the model is much less useful than its test score suggests. This final step turns your experiments into something other people can trust and repeat.

## Explanation
Your report follows the style of a **model card**: a short, structured document that travels with a model. Use these sections, in this order.

1. **Summary and intended use.** One paragraph: the task, the classes, who might use it and for what. Also state **out-of-scope uses**, for example "not for medical or legal decisions".
2. **Data.** The dataset name, source, licence, size of each split, class balance, how labels were made, and any preprocessing or augmentation. Mention known gaps, such as one region, language or camera type.
3. **Method.** The baseline and the final architecture, the pretrained checkpoint and its licence, and the training setup: optimiser, learning rate, schedule, batch size, epochs, regularisation and seeds.
4. **Experiments table.** One row per run from your results table: the change, the validation metric (with mean and spread where you ran several seeds) and whether the hypothesis was supported.
5. **Results.** The final validation result, the single test result, and a confusion matrix.
6. **Error analysis.** The main error patterns from misclassified validation examples, with 2–3 short, non-personal examples (L14).
7. **Limitations and risks.** Where the model is likely to fail, possible bias from the data, and what should be checked before real use.
8. **Reproducibility.** Library versions, how to run the notebook from the start, where the checkpoint is stored, and the expected runtime on GPU and on CPU.

Keep numbers consistent: every number in the report must come from your results table or a notebook output, not from memory. Write in plain language; a reader who knows scikit-learn but not your project should follow it.

**Sharing the notebook.** Before you share it, restart the runtime and run all cells from the top. Remove any secret keys, and do not print them. If a cell needs a token, read it from Colab's secrets feature or a login prompt instead of typing it into the code. [VERSION]

**Optional: share on the Hugging Face Hub.** You can upload your model and a model card to a Hub repository with the `push_to_hub` methods or the web interface, after logging in. Upload steps, login methods and repository settings change, so follow the current Hub documentation. [VERSION] Upload only models trained on data whose licence allows it.

**Analogy:** A model card is like the leaflet inside a medicine box. It says what the medicine is for, how it was tested, the correct dose, the side effects and who should not take it. Nobody would trust a medicine that came without one.

## Worked Example
Elif is an ML engineer at a hypothetical carpet manufacturer in Gaziantep, Türkiye. Her capstone classifies weaving defects from public textile-image data with a confirmed licence. Her first draft has a strong results section but only one sentence on data and nothing on limits.

She revises it using the eight sections. In **Data**, she adds that all images come from one type of camera and lighting, and that one defect class has far fewer examples. In **Experiments**, she pastes her results table: baseline CNN, frozen ResNet-18, fine-tuned ResNet-18, and fine-tuned with a schedule, each with its validation macro F1 over 3 seeds. In **Error analysis**, she shows that most errors are between two defect types that look similar at low resolution. In **Limitations**, she states that the model has not been tested on photos from factory cameras, and should not be used to reject products without human review.

Finally, she asks a colleague to run the shared notebook from the start on a CPU runtime with the small subset option. It runs to the end, and the colleague's validation score for the chosen model is within the seed range in her table.

## Common Mistake
Many learners write the report as a success story: only the final score, no failed runs, and no limits. This makes the work less credible, not more. Reviewers trust a report that shows what did not work and why the final choice was made. Another mistake is sharing a notebook that only runs on the author's session, because it depends on files that are not in Drive or on cells run out of order. Always test with "restart and run all".

## Key Takeaways
1. Structure the report like a model card: intended use, data, method, experiments, results, error analysis, limitations and reproducibility.
2. Take every number from your results table or notebook outputs, and include failed runs and known limits.
3. Share a notebook that runs from the start without secrets in the code, and check licences before any public upload.

## Hands-on Exercise
**Task:** Capstone step 3: write the experiment report and share the notebook so that someone else can run it from the start.
**Tools:** Google Docs, a Markdown cell in Colab, or any editor (free); your Colab notebook and results table. Optional: a free Hugging Face account for Hub sharing.
**Steps:**
1. Create the report with the eight sections above.
2. Paste your results table and add a one-line conclusion for each run.
3. Add the confusion matrix, 2–3 non-personal error examples, and your limitations.
4. Restart your notebook and run all cells; fix anything that fails.
5. Check that no keys, tokens or personal data appear in the notebook or report.
6. Share the notebook with view access, and ask a peer to run it and confirm the result.
7. Optional: upload the model and card to the Hub, following current documentation. [VERSION]
**What good looks like:** A complete report of about 2–4 pages in which every number matches the notebook, limits are specific, and a peer can run the notebook from the start and reach a result within your reported range.
**Time:** about 60 minutes

## Review Flags
- [VERSION] Hugging Face Hub upload steps (`push_to_hub`, login methods, repository settings) and Colab's secrets feature must be checked against current documentation before recording.
