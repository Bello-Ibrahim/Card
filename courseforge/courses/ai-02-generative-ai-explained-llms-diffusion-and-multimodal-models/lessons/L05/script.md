# L05 How Diffusion Models Create Images | Presenter Script

Course: AI-02 · Video: 5 min · Words: 689

## Hook
Think of the grey snow on an old television with no signal. Many image generators start from this kind of randomness. A few seconds later, you have a detailed picture of a lighthouse at sunset. How does noise become a picture?

## Explain
Welcome to Module two. So far, we have looked at language models. Now we turn to images, and to one common type of image generator, the diffusion model. What follows is a simplified picture. We look at training first, and then at generating.

In simple terms, training works like this. The model sees a huge number of images, each with a text description. Random noise is added to each image a little at a time, until only noise is left.

The model's task is to look at a noisy image and work out what noise was added, so that it can remove it and make the image a little clearer. Because it also sees the description, it learns what words like cat, watercolour or evening light usually look like.

Now, generating. When you type a prompt, the model starts from pure random noise. It removes noise in many small steps. At each step, your prompt steers the result, so the image looks more like your description. Early steps decide the large shapes. Later steps add details like texture and edges.

You can picture a photo slowly coming into focus in a darkroom. At first, the paper shows only grey shapes. Step by step, the details appear. Here, the prompt decides what the photo shows.

But the picture has one limit. In a real darkroom, the photo already exists on the film. A diffusion model creates a new picture that never existed before.

This matters for you in two ways. Every image starts from different random noise, so the same prompt gives a different image each time. And the prompt guides, but it does not control every detail. Anything you do not describe is filled in with typical patterns from training.

So if something matters to you, like the colour, the angle or the time of day, put it in the prompt. You will practise this in the next lesson.

## Demonstrate
Let's see this in an example. Kenji is a design student in Osaka. For a class project about local festivals, he types the same prompt into a free image generator four times. A paper lantern festival on a river at night, warm light, wide view.

First, what stays the same. All four images show lanterns, water and a night sky, with warm orange light. The prompt steered these things in every run. The words in the prompt acted like fixed points that every image had to follow.

Next, what changes. The number of lanterns, the position of the river, the camera angle, and whether there are people. None of these were in the prompt, so they came from the different starting noise.

And one thing goes wrong. One image has a sign on a boat, with letters that are not real words. Kenji learns that if he wants people on a bridge, or exactly five lanterns, he must describe it. Even then, exact counts and readable text may not be reliable.

A common mistake is to think an image generator searches the internet for a matching picture and edits it. A diffusion model does not search when it generates. It starts from noise and builds a new image. That is why you can ask for scenes nobody has ever photographed.

## Recap
Let's recap. First, in simple terms, a diffusion model learns by removing noise from images that were gradually covered with noise, together with their descriptions. Second, to generate, it starts from pure noise and removes it step by step, with your prompt steering each step. Third, different starting noise explains why the same prompt gives different images.

## CTA
Now try it yourself. In the exercise below, use a free image generator to create the same prompt four times. Then list what stays the same and what changes, and link it to noise and the prompt. It takes about twenty minutes. Next, we learn about guiding image generators. See you there.

## Thumbnail
Headline: From Noise to Picture
Image: Navy background, a square that fades from grey static on the left into a clear lighthouse at sunset on the right, headline in teal Inter Bold.

## Production Notes
- [VERIFY] The descriptions of diffusion training (noise added step by step, the model learns to predict and remove it, linked to text descriptions) and generation (from pure noise, step by step, steered by the prompt) are simplified on purpose. The voiceover says 'in simple terms'. A reviewer must confirm they are accurate enough for beginners.
- [VERIFY] content.md says not every image generator uses diffusion and some tools combine methods. The voiceover only calls diffusion 'one common type of image generator' and does not state the wider claim; add it only after review.
- [VERIFY] The darkroom analogy is kept with its stated limit (the darkroom photo already exists; a diffusion model creates a new one). Confirm it is not misleading.
- [VERIFY] content.md's point that generators can sometimes produce results very close to training images or known styles, raising copyright and fairness questions, is left out of the voiceover. It stays on the lesson page after review.
- [VERSION] Kenji's four lantern images for scenes 11 to 13, and the noise-to-image steps in scene 5, should be generated in Google Gemini (DECISIONS.md) with the exact prompt 'A paper lantern festival on a river at night, warm light, wide view.' Check the free limits and the licence terms for generated images before use. If none of the four shows a sign with letters that are not real words, adjust the voiceover in scene 13 or pick a run that does.
- [VERSION] The seed setting is not mentioned in the voiceover because its availability differs between tools.
- Kenji and his Osaka class project are fictional.
