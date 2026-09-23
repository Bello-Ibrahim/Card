# L20 Capstone Step 3: Document Your Experiments | Presenter Script

Course: AI-13 · Video: 5 min · Words: 698

## Hook
Imagine a colleague opens your capstone notebook six months from now. Can they tell what the model is for, what data it learned from, how you chose it, and where it fails? If not, it is much less useful than its score suggests.

## Explain
This final step turns your experiments into something other people can trust and repeat. Your report follows the style of a model card, a short, structured document that travels with a model. It has eight sections, in this order.

First, the summary and intended use. The task, the classes, and who might use it for what. Also state what it is not for, such as medical or legal decisions. Second, the data. Its name, source, licence, split sizes, class balance, how labels were made, and known gaps, such as one region or one camera type.

Third, the method. The baseline and the final architecture, the pretrained checkpoint and its licence, and the full training setup. Fourth, the experiments table, with one row per run, the validation metric with mean and spread, and whether the hypothesis was supported. Fifth, the results. The final validation score, the single test score, and a confusion matrix.

Sixth, error analysis, with the main error patterns and two or three short, non-personal examples. Seventh, limitations and risks. Where the model is likely to fail, possible bias, and what to check before real use. Eighth, reproducibility. Library versions, how to run the notebook from the start, where the checkpoint is, and the expected runtime.

A model card is like the leaflet inside a medicine box. It says what the medicine is for, how it was tested, the dose, the side effects, and who should not take it. Nobody would trust a medicine without one.

## Demonstrate
Elif is an engineer at a carpet manufacturer in Gaziantep, Türkiye. Her capstone classifies weaving defects from public textile images with a confirmed licence. Her first draft has a strong results section, but only one sentence on data, and nothing on limits.

She revises it section by section. In the data section, she adds that all images come from one type of camera and lighting, and that one defect class has far fewer examples.

In the experiments section, she pastes her results table. The baseline CNN, the frozen ResNet, the fine-tuned ResNet, and the fine-tuned model with a schedule, each with validation macro F1 over three seeds.

Her error analysis shows that most errors are between two defect types that look similar at low resolution. And under limitations, she writes that the model has not been tested on photos from factory cameras, and should not reject products without human review.

Before sharing, she restarts the runtime and runs every cell from the top. There are no secret keys in the code. A colleague then runs it on a CPU with the small subset, and gets a validation score within the seed range in her table.

Optionally, you can share your model and its card on the Hugging Face Hub. Upload steps change, so follow the current Hub documentation, and upload only models trained on data whose licence allows it.

A common mistake is writing the report as a success story, with only the final score, no failed runs and no limits. That makes the work less credible, not more. Reviewers trust a report that shows what did not work, and why the final choice was made. And always test your shared notebook with restart and run all.

## Recap
Let's recap. First, structure the report like a model card, with intended use, data, method, experiments, results, error analysis, limitations and reproducibility. Second, take every number from your results table or notebook outputs, and include failed runs and known limits. Third, share a notebook that runs from the start with no secrets in the code, and check licences before any public upload.

## CTA
Congratulations. You have gone from tensors to a fine-tuned, documented neural network. For capstone step three, write your experiment report and share your notebook so someone else can run it from the start. It takes about an hour. Then check the rubric, and submit your capstone on the course page. Well done, and good luck.

## Thumbnail
Headline: Write the Model Card
Image: Navy background, a clean document card with eight short section lines and a small medicine-leaflet icon, headline in teal Inter Bold.

## Production Notes
- L20 is not a screen-demo lesson: Elif's report is shown with slides only.
- [VERSION] Hugging Face Hub upload steps (push_to_hub, login methods, repository settings) and Colab's secrets feature must be checked against current documentation before recording. The voiceover says only that the steps change and to follow the current Hub documentation.
- Elif's experiments table shows run names only; no scores are stated (content.md gives none). If the slide shows example values, label them 'illustrative'.
- The capstone rubric (capstone_rubric.md) and the submission link should be shown on the course page under this video.
- Elif and the Gaziantep carpet manufacturer are hypothetical; stock footage must not show a real company name or logo.
