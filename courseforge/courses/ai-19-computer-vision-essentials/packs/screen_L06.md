# Screen Demo Pack: AI-19 L06 Classifying Images with Hugging Face Models

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-19-computer-vision-essentials_L06_screen_1.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Open a new Colab notebook and upload 10 furniture photos with no people in them
2. Run the pipeline cell on the first photo
3. Show the top 3 labels and scores

**Narration over this clip (for pacing)**

> He opens a new Colab notebook, uploads the photos and runs the pipeline on the first one. You'll see something like this. Rocking chair at zero point seven one, folding chair at zero point one two, and park bench at zero point zero four.

## Clip 2: scene 10

- **Filename:** `ai-19-computer-vision-essentials_L06_screen_2.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Loop over all 10 photos with top_k=3
2. Collect results in a pandas DataFrame with columns file, label_1, score_1, label_2, label_3
3. Display the DataFrame

**Narration over this clip (for pacing)**

> Next, a short loop runs all ten photos and collects the results in a table, with the file name and the top three labels. Most chairs, tables and wardrobes get sensible labels.

## Clip 3: scene 11

- **Filename:** `ai-19-computer-vision-essentials_L06_screen_3.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Open the model card on the Hugging Face Hub in a new tab
2. Scroll to the training data section
3. Scroll to the label list

**Narration over this clip (for pacing)**

> He opens the model card in a new tab and scrolls to the training data and the label list. This is where he learns what the model can and cannot say.

## Clip 4: scene 12

- **Filename:** `ai-19-computer-vision-essentials_L06_screen_4.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Sort the DataFrame by score_1
2. Display the two photos with the lowest top score next to their labels

**Narration over this clip (for pacing)**

> Then he shows the two photos with the lowest top score. In his test, a sofa bed was labelled studio couch, which is close, but not one of his categories. And a shelf photographed from above was labelled crossword puzzle, probably because its grid looks like a familiar pattern.

## Production notes for this lesson

- [VERSION] Hugging Face transformers pipeline task name (image-classification), the top_k argument, the model ID google/vit-base-patch16-224 and the Hub model card layout must be checked at recording time. Install transformers with pip if it is missing in Colab.
- [VERIFY] The training data and number of labels on the chosen model's card (content.md mentions ImageNet-style data with about 1,000 classes [VERIFY]). The voiceover does not state the dataset or the number of labels; it only tells learners to read the card.
- Run outputs: content.md marks the printed labels and scores as example output (code checked for syntax only). The voiceover therefore says 'you'll see something like' before rocking chair 0.71, folding chair 0.12, park bench 0.04, and describes the 'studio couch' and 'crossword puzzle' errors as what happened in Tomasz's test. If the recorded run gives different labels, keep the 'something like' wording and show the real output; re-record the error scene if the two wrong labels do not appear.
- Privacy: the 10 furniture photos contain no people and no private documents. Do not use the online demo widget on the model page with photos of people.
- Tomasz Nowak and his Gdańsk marketplace are fictional; no real marketplace name or logo on screen.
- Screen recording: clean browser profile, no account names or other tabs visible.
