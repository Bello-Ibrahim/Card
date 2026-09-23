# L05 How Diffusion Models Create Images

Course: AI-02 · Module: M2 · Objectives: O3 · Video: 5 min

## Hook
Think of the grey "snow" on an old television with no signal. Many image generators start from this kind of randomness. A few seconds later, you have a detailed picture of a lighthouse at sunset. How does noise become a picture?

## Explanation
A **diffusion model** is one common type of image generator. To understand it, look at two things separately: how it is trained and how it generates. The description below is simplified. [VERIFY]

**Training: learning to remove noise.** The model sees a very large number of images, each with a text description. Random noise is added a little at a time, step by step, until the image is only noise. The model's task is to look at a noisy image and predict what noise was added, so the noise can be removed and the image becomes a little clearer. Because it also sees the text description, it learns links between words and visual patterns: what "cat", "watercolour" or "evening light" usually look like. In the end, it is very good at one skill: making a noisy image a little less noisy, in the direction of a description.

**Generating: from pure noise to a picture.** When you type a prompt, the model starts from **pure random noise**. It then removes noise in many small steps. At each step, the text prompt **steers** the result: the model removes noise in a way that makes the image look more like your description. Early steps decide the large shapes and layout. Later steps add details such as texture and edges. At the end, you have a new image.

Three consequences matter for you:

- **Every image starts from different random noise.** This is why the same prompt gives a different image each time. Some tools let you fix the starting point with a setting often called a "seed", so you can repeat a result. [VERSION]
- **The prompt guides, but it does not control every detail.** Anything you do not describe is filled in with typical patterns from training.
- **The model does not copy one stored image.** It builds a new image from learned patterns. However, it can sometimes produce results that look very close to training images or to a known style, which raises questions about copyright and fairness. [VERIFY]

Not every image generator uses diffusion. Some use other methods, and some tools combine methods. For this course, diffusion is the main example because it is widely used and easy to picture. [VERIFY]

**Analogy:** Think of a photo slowly coming into focus in a darkroom. At first the paper shows only grey shapes. Step by step, the details appear. In a diffusion model, the text prompt decides what the photo will show. The analogy has one limit: in a real darkroom the photo already exists on the film, but a diffusion model creates a new picture that never existed.

## Worked Example
Kenji is a design student in Osaka, Japan. For a hypothetical class project about local festivals, he types the same prompt into a free image generator four times: "A paper lantern festival on a river at night, warm light, wide view."

- **What stays the same:** all four show lanterns, water and a night sky with warm orange light. The prompt steered these elements in every run.
- **What changes:** the number of lanterns, the position of the river, the angle of the view and whether there are people. These details were not in the prompt, so they came from the different starting noise.
- **What goes wrong:** one image has a sign on a boat with letters that are not real words.

Kenji understands that if he wants people on a bridge or exactly five lanterns, he must describe it. Even then, exact counts and readable text may not be reliable (L08).

## Common Mistake
Many learners think an image generator searches the internet for a matching picture and edits it. A diffusion model does not search for pictures when it generates. It starts from random noise and builds a new image from patterns learned in training. This is why you can ask for scenes that have never been photographed.

## Key Takeaways
1. A diffusion model is trained by learning to remove noise from images that were gradually covered with noise, together with their text descriptions.
2. To generate, it starts from pure noise and removes it step by step, with the text prompt steering each step.
3. Different starting noise explains why the same prompt gives different images; details you do not describe are filled in from typical patterns.

## Hands-on Exercise
**Task:** Using a free image generator, create the same prompt four times and describe what stays the same and what changes between the four images.
**Tools:** A free image generator of your choice [VERSION]; a notes app. Free generators and their daily limits change often, so check the course page for current suggestions.
**Steps:**
1. Open a free image generator and read its usage rules.
2. Write one simple prompt with a subject, a setting and a light condition, for example "a red bicycle in a quiet street, early morning." Do not use real people's names or photos.
3. Generate the image four times with exactly the same prompt and settings. Save all four.
4. Make two lists: "stays the same" and "changes".
5. Write two sentences linking your lists to the idea of starting noise and prompt steering.
**What good looks like:** Four saved images with the same prompt, two clear lists (for example "the bicycle is always red" vs. "the street and angle change"), and two sentences that use the words "noise" and "prompt" correctly.
**Time:** about 20 minutes

## Review Flags
- [VERIFY] Confirm the simplified description of diffusion training (predicting and removing added noise, linked to text descriptions) and generation (from pure noise, step by step, steered by the prompt) is accurate enough for beginners.
- [VERIFY] Confirm the wording that not all image generators use diffusion and that some tools combine methods, and that the darkroom analogy, with its stated limit, is not misleading.
- [VERIFY] Confirm the wording that generators can sometimes produce results very close to training images or known styles, and that this raises copyright and fairness questions.
- [VERSION] "Free image generator" is not named on purpose. A reviewer should choose specific free tools and check their current free limits, the availability of a "seed" setting, and licence terms for generated images.
