# Screen Demo Pack: AI-19 L15 Capstone Part 1: Build Your Detection App

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-19-computer-vision-essentials_L15_screen_1.mp4`
- **Target length:** about 21 seconds

**Steps**

1. In Colab, run !pip install ultralytics gradio
2. Upload best.pt
3. Scroll through the cell: the count function with the RGB to BGR flips, and gr.Interface with gr.Image, gr.Slider and gr.Number

**Narration over this clip (for pacing)**

> In Colab, he installs Ultralytics and Gradio, and uploads his trained model file. His counting function flips the colour order, runs the model, counts the juice cartons, and flips the annotated picture back. The interface has an image input, a confidence slider, the annotated picture and the count.

## Clip 2: scene 10

- **Filename:** `ai-19-computer-vision-essentials_L15_screen_2.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Run the cell and open the temporary link that Gradio prints
2. Upload a shelf photo and move the confidence slider
3. Point to the count and to the missed carton behind the price label

**Narration over this clip (for pacing)**

> He runs the cell and opens the temporary link. He uploads a shelf photo with fourteen cartons, and moves the slider. You'll see something like count thirteen. A carton behind a price label is missed, just as in training. He notes it for the next lesson.

## Clip 3: scene 11

- **Filename:** `ai-19-computer-vision-essentials_L15_screen_3.mp4`
- **Target length:** about 25 seconds

**Steps**

1. On huggingface.co, create a new Space with the Gradio SDK and free CPU hardware
2. Upload app.py, best.pt and requirements.txt listing ultralytics and gradio

**Narration over this clip (for pacing)**

> To keep the app running, he creates a new Space on Hugging Face, with Gradio and free CPU hardware. He uploads three files. The app code, the model file, and a requirements file that lists Ultralytics and Gradio. Free Space hardware has no GPU and has limits, so he uses the smallest model and keeps any videos short.

## Clip 4: scene 12

- **Filename:** `ai-19-computer-vision-essentials_L15_screen_4.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Wait for the Space build to finish
2. Upload a new shelf photo and show the result

**Narration over this clip (for pacing)**

> When the build finishes, he tests the Space with a new photo. Before he makes it public, he checks two things. The app shows no people, and the detector's licence allows public use. Remember, the Ultralytics YOLO licence must be checked before commercial use.

## Production notes for this lesson

- [VERSION] Hugging Face Spaces free hardware and Space creation steps; the Gradio interface (gr.Interface, gr.Image(type="numpy"), gr.Slider, gr.Number) and temporary link; ultralytics treating NumPy input as BGR and Results.plot() returning BGR. Gradio is not in the brief's tool list; content.md uses it as the interface layer. Code was checked for syntax only.
- [VERIFY] Ultralytics licence (content.md: AGPL-3.0 with a separate commercial licence, and what it may require for a public Space [VERIFY]). The voiceover makes no legal claim and does not name the licence; it says Karim checks that the detector's licence allows public use, and that the Ultralytics YOLO licence must be checked before commercial use. General guidance, not legal advice.
- [VERSION] Google Colab free resources and session limits are not guaranteed.
- Run outputs: content.md gives 'Count: 13' for a photo with 14 cartons only as example output. The voiceover says 'you'll see something like' before it. If the recorded run differs, show the real count and keep the wording.
- Footage: shelf photos show only products, with no people and no real brand names or logos. The Casablanca and Manila use cases and Karim El Amrani are hypothetical.
- Screen recording: clean browser profile, no account names, tokens or other tabs visible, including on huggingface.co.
