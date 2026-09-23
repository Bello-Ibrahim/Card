# Capstone Rubric: Build an Object Detection and Counting App

## Task
Build an object detection app for one real-world use case, such as counting stock on shop shelves or counting vehicles on a road, using pre-trained models in Google Colab. Then evaluate it, make one improvement, and judge whether it is fit for real use. You build the app in L15 (capstone step 1) and evaluate, improve and present it in L16 (capstone step 2). Use scenes with objects and vehicles. Do not include identifiable people without their consent, blur any people who appear, and do not upload personal or confidential images to online tools.

## Deliverables
- A working app (a Colab notebook with a Gradio interface, or a Hugging Face Space) that takes an image or short video, detects the target objects, draws boxes and shows a total count.
- A short use-case note: target objects, scene, the number the user needs, the model used (pre-trained or fine-tuned) and the licence of every model and dataset.
- If you fine-tuned: your dataset description (number of images and classes), training results (mAP50 and mAP50-95) and 3 failure cases.
- A test table with at least 20 new images or clips that were not used for training or tuning, showing the condition, the true count, the app's count and the error for each item.
- A before-and-after comparison for one improvement, measured on the same test set.
- A half-page fitness check with the headings Accuracy, Speed, Privacy, Licence and Decision.
- A 3-minute demo video that shows the app working, at least one failure and your decision.

## Criteria
| Criterion | Objective | Excellent | Good | Developing | Not yet | Points |
|---|---|---|---|---|---|---|
| Working detection and counting app | O3, O7 | App runs on new inputs, shows clear boxes and a correct total, handles colour order correctly, and has a simple, clear interface for a narrow, well-defined use case. | App runs on new inputs and shows boxes and a total, with small issues in the interface or use-case definition. | App runs only in the notebook, or the count or boxes are often wrong for reasons not explained. | No working app. | 25 |
| Model choice, configuration and fine-tuning | O4 | Model choice is justified for the use case; threshold chosen on separate images; if fine-tuned, labels are complete, splits are separated by session, and mAP and 3 failure cases are reported. | Reasonable model and threshold; fine-tuning (if used) is complete with mAP reported, but the justification or failure cases are thin. | Default settings used with no justification, or fine-tuning has clear labelling or split problems. | No evidence of how the model was chosen or trained. | 15 |
| Evaluation with the right metrics | O5 | At least 20 new test items covering real conditions; mean absolute count error overall and per condition; precision, recall or mAP where boxes are labelled; failures grouped by cause such as lighting, angle, image quality or unbalanced data. | At least 20 new test items with overall and per-condition errors and some analysis of failures. | Fewer than 20 items, errors only overall, or test items overlap with training or tuning data. | No evaluation results. | 20 |
| One measured improvement | O5, O4 | One targeted change based on the failure analysis, applied alone, measured on the same test set, and reported honestly, including any condition that became worse. | One change measured before and after on the same test set, with a short explanation. | A change was made but not measured fairly, or several changes were mixed together. | No improvement attempted. | 15 |
| Fitness check: accuracy, speed, privacy and licence | O6 | Uses the learner's own measured numbers; covers speed, privacy steps (blurring, storage limits, local rules) and the licence of every component, including the YOLO licence terms; ends with a clear, limited decision on where the app is and is not fit for use. | Covers all four areas with a clear decision, but some points are general rather than based on the learner's own results. | Covers only some areas, or the decision is missing or unclear. | No fitness check. | 15 |
| Demo and presentation | O7 | Clear 3-minute demo that shows the problem, the app working, results, at least one failure and the decision; easy to follow for a non-technical manager. | Clear demo with most parts present, slightly long or short. | Demo is hard to follow, or hides failures. | No demo. | 10 |

Total: 100

## Submission Checklist
- My app takes a new image or short video and shows boxes and a total count.
- My use-case note names the target objects, the model and the licence of every model and dataset.
- If I fine-tuned, I reported mAP50, mAP50-95 and 3 failure cases.
- My test set has at least 20 new images or clips that I did not use for training or tuning.
- My test table shows the condition, true count, app count and error for each item.
- I made one improvement and measured it on the same test set, and I reported the result honestly.
- My fitness check covers accuracy, speed, privacy and licence and ends with a clear decision.
- I checked the current YOLO licence terms before any commercial or public use.
- No identifiable people appear in my app, test images or demo without consent, and any people are blurred.
- My demo is about 3 minutes long and shows at least one failure.
