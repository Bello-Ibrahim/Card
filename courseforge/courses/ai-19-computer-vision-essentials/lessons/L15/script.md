# L15 Capstone Part 1: Build Your Detection App | Presenter Script

Course: AI-19 · Video: 5 min · Words: 702

## Hook
A notebook that only you can run is an experiment. An app where a shop manager uploads a photo and sees fourteen cartons is a product. Today, you start building that app. And every choice you make today should serve that one number.

## Explain
This is the first of two capstone lessons. Your capstone is an object detection and counting app for one real use case. Choose one that is narrow, and that counts objects, not people. For example, stock on shop shelves in Casablanca, or vehicles on a road in Manila.

Build it in four steps. First, define the target. Count juice cartons on the drinks shelf is a good target. Count everything in any shop is not. Second, choose the model. If a pre-trained class fits, use it with a tested threshold. If not, fine-tune on your own images, and check every licence.

Third, write one counting function that returns an annotated image and the total. For video, reuse the line counting from lesson thirteen. Fourth, add a simple interface with Gradio, which builds a web page from a Python function. It runs in Colab with a temporary link, or on a free Hugging Face Space.

Watch the colour order. Gradio gives your function red, green, blue. But the Ultralytics package treats arrays as blue, green, red, like OpenCV. So convert on the way in, and convert the annotated result back on the way out.

Over this lesson and the next, you deliver five things. The working app, a test table on at least twenty new images or clips, one measured improvement, a fitness check, and a three-minute demo. The rubric scores each of these, so keep them in mind as you build.

Think of the model as the engine, and the interface as the dashboard. The driver does not need to see the engine. They need a clear speed reading and a warning light.

## Demonstrate
Karim El Amrani manages three grocery shops in Casablanca. He fine-tuned a detector on eighty labelled shelf photos, using the steps from lesson eleven. Now he wraps it in an app.

In Colab, he installs Ultralytics and Gradio, and uploads his trained model file. His counting function flips the colour order, runs the model, counts the juice cartons, and flips the annotated picture back. The interface has an image input, a confidence slider, the annotated picture and the count.

He runs the cell and opens the temporary link. He uploads a shelf photo with fourteen cartons, and moves the slider. You'll see something like count thirteen. A carton behind a price label is missed, just as in training. He notes it for the next lesson.

To keep the app running, he creates a new Space on Hugging Face, with Gradio and free CPU hardware. He uploads three files. The app code, the model file, and a requirements file that lists Ultralytics and Gradio. Free Space hardware has no GPU and has limits, so he uses the smallest model and keeps any videos short.

When the build finishes, he tests the Space with a new photo. Before he makes it public, he checks two things. The app shows no people, and the detector's licence allows public use. Remember, the Ultralytics YOLO licence must be checked before commercial use.

A common mistake is to spend capstone time on colours and extra buttons. The rubric rewards a correct count, honest evaluation and a clear fitness judgement. So get a plain interface working first. And do not forget the colour conversion.

## Recap
Let's recap. First, choose one narrow use case, with a clear target object and a number the user needs. Second, wrap one counting function in a Gradio interface, and convert between the two colour orders at the edges. Third, deploy on a free Hugging Face Space with a small model, and check licences before you go public.

## CTA
Now it is your turn. In the exercise below this video, you complete capstone step one. Build an app that takes an image or a short video, detects and counts your target objects, and shows boxes and a total. It takes about an hour. In the next lesson, Capstone Part 2: Evaluate, Improve and Present. See you there.

## Thumbnail
Headline: From Notebook to App
Image: Navy background, a simple web app window showing a shelf photo with teal boxes around juice cartons and a large count number, headline in teal Inter Bold.

## Production Notes
- [VERSION] Hugging Face Spaces free hardware and Space creation steps; the Gradio interface (gr.Interface, gr.Image(type="numpy"), gr.Slider, gr.Number) and temporary link; ultralytics treating NumPy input as BGR and Results.plot() returning BGR. Gradio is not in the brief's tool list; content.md uses it as the interface layer. Code was checked for syntax only.
- [VERIFY] Ultralytics licence (content.md: AGPL-3.0 with a separate commercial licence, and what it may require for a public Space [VERIFY]). The voiceover makes no legal claim and does not name the licence; it says Karim checks that the detector's licence allows public use, and that the Ultralytics YOLO licence must be checked before commercial use. General guidance, not legal advice.
- [VERSION] Google Colab free resources and session limits are not guaranteed.
- Run outputs: content.md gives 'Count: 13' for a photo with 14 cartons only as example output. The voiceover says 'you'll see something like' before it. If the recorded run differs, show the real count and keep the wording.
- Footage: shelf photos show only products, with no people and no real brand names or logos. The Casablanca and Manila use cases and Karim El Amrani are hypothetical.
- Screen recording: clean browser profile, no account names, tokens or other tabs visible, including on huggingface.co.
