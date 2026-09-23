# L15 Capstone Part 1: Build Your Detection App

Course: AI-19 · Module: M4 · Objectives: O3, O4, O7 · Video: 5 min (screen demo)

## Hook
A notebook that only you can run is an experiment. An app where a shop manager uploads a photo and sees "14 cartons" is a product. Today you build that app.

## Explanation
Your capstone is an object detection and counting app for one real use case. Choose a use case that is narrow and uses objects, not people. Two hypothetical examples:

- Counting stock on shop shelves in Casablanca, Morocco, so staff know when to refill.
- Counting vehicles on a road in Manila, the Philippines, to compare traffic at different times.

Build it in four steps.

**1. Define the target.** Which objects, in which scenes, and what number? "Count juice cartons on the drinks shelf" is a good target; "count everything in any shop" is not.

**2. Choose the model.** If a pre-trained class fits (car, bus, bottle), configure the pre-trained model and choose a threshold as in L10. If not, fine-tune on your own labelled images as in L11. Check the licence of every model and dataset. [VERIFY]

**3. Write one counting function** that returns an annotated image and the total. For video, reuse the line counting from L13.

**4. Add a simple interface.** **Gradio** builds a web interface from a Python function in a few lines. It runs inside Colab with a temporary public link, or permanently on a free **Hugging Face Space**. [VERSION] Free Space hardware is CPU only and has limits, so use the smallest model and keep videos short. [VERSION]

Watch the colour order. Gradio gives your function an RGB array, while the `ultralytics` package treats NumPy arrays as BGR, like OpenCV (L02). Convert on the way in, and convert the annotated result back on the way out. [VERSION]

**The capstone brief.** Over L15 and L16 you deliver the working app, a test table on at least 20 new images or clips, one measured improvement, a fitness check (L14) and a 3-minute demo. The rubric scores the app, model choice and training, evaluation, the improvement, and the fitness check with the demo.

**Analogy:** The model is the engine and the Gradio interface is the dashboard. The driver does not need to see the engine; they need a clear speed reading and a warning light.

## Worked Example
Karim El Amrani manages three grocery shops in Casablanca. He fine-tuned a detector on 80 labelled shelf photos, using the steps from L11, and now wraps it in an app.

```python
import gradio as gr
from ultralytics import YOLO

model = YOLO("best.pt")               # the model trained in L11
TARGET = "juice_carton"

def count(image, conf):
    r = model(image[:, :, ::-1], conf=conf, verbose=False)[0]  # RGB -> BGR
    names = [r.names[int(c)] for c in r.boxes.cls]
    annotated = r.plot()[:, :, ::-1]                          # BGR -> RGB
    return annotated, names.count(TARGET)

demo = gr.Interface(
    fn=count,
    inputs=[gr.Image(type="numpy"),
            gr.Slider(0.05, 0.9, value=0.25, label="Confidence")],
    outputs=[gr.Image(label="Detections"), gr.Number(label="Count")],
    title="Shelf stock counter")
demo.launch()
```

**On screen (presenter steps):**
1. In Colab, run `!pip install ultralytics gradio` and upload `best.pt`. [VERSION]
2. Run the cell, open the temporary link that Gradio prints, upload a shelf photo and move the slider.
3. On huggingface.co, create a new Space with the Gradio SDK and free CPU hardware. [VERSION]
4. Upload `app.py` (the code above), `best.pt` and a `requirements.txt` listing `ultralytics` and `gradio`.
5. When the build finishes, test the Space with a new photo.

Example result: a photo with 14 cartons shows "Count: 13"; a carton behind a price label is missed, as in training. He notes it for L16. Before making the Space public, Karim checks that the app shows no people and that the detector's licence allows public use. A public app built on AGPL-3.0 code may need its source code published. [VERIFY]

## Common Mistake
Many learners spend most of their capstone time on colours and extra buttons. The rubric rewards a correct count, honest evaluation and a clear fitness judgement, so get a plain interface working first. Another mistake is forgetting the colour conversion, which gives wrong colours in the output and can lower detection quality.

## Key Takeaways
1. Choose one narrow use case with a clear target object and a number the user needs.
2. Wrap one counting function in a Gradio interface, and convert between RGB and BGR at the boundaries.
3. Deploy on a free Hugging Face Space with a small model, and check licences before you make the app public.

## Hands-on Exercise
**Task:** Capstone step 1: build a working app that takes an image or short video, detects and counts the target objects, and shows the result with boxes and a total.
**Tools:** Google Colab [VERSION]; the `ultralytics` package [VERSION]; Gradio [VERSION]; a free Hugging Face account and Space (optional) [VERSION]; your L11 model or a pre-trained model.
**Steps:**
1. Write your use case in two sentences: target objects, scene and the number the user needs.
2. Choose a pre-trained or fine-tuned model and record its licence.
3. Write and test the counting function on 3 images in a notebook cell.
4. Wrap it in a Gradio interface with an image input, a confidence slider, an annotated output and a count.
5. Launch it in Colab and test 2 new images.
6. Optional: deploy it to a Hugging Face Space.
7. Save screenshots of two results.
**What good looks like:** An app that accepts a new image, shows boxes around the target objects and displays a total, plus a short note of the use case, the model and its licence.
**Time:** about 60 minutes

## Review Flags
- [VERSION] Curriculum flags: Hugging Face Spaces free hardware and Space creation steps; the Gradio interface (`gr.Interface`, `gr.Image(type="numpy")`, `gr.Slider`, `gr.Number`) and temporary link (Gradio is not in the brief's tool list); `ultralytics` treating NumPy input as BGR and `Results.plot()` returning BGR. Code was checked for syntax only; counts are example output.
- [VERIFY] Curriculum flag: Ultralytics licence (AGPL-3.0 with a separate commercial licence), including what it requires for a public Space; confirm before scripting.
- [VERSION] Curriculum flag: Google Colab free resources and session limits are not guaranteed.
