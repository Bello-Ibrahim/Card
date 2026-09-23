# L01 How AI Image Generators Work | Presenter Script

Course: AI-20 · Video: 5 min · Words: 694

## Hook
You type a red bicycle leaning against a blue wall. A few seconds later, you see a picture that never existed before. Nobody searched the internet for it, and nobody drew it. So where did it come from?

## Explain
Hi, and welcome to AI Image Generation and Visual Design. In this first lesson, we look at what happens between your words and the finished image.

An AI image generator is a computer program that creates a new picture from a written description. First, it goes through training. During training, it studies a very large collection of images, together with short texts that describe them.

It does not store the pictures like a photo album. Instead, it learns patterns. What red usually looks like. How light falls on a wall. What shapes make a bicycle.

When you use the tool, a useful way to picture it is this. The image is built step by step from random noise. Noise looks like the grey, grainy static on an old television. At each step, the system removes a little noise and moves the picture closer to your words.

Think of a photograph appearing slowly in a darkroom tray. At first the paper is almost blank. Then soft shapes appear, then edges, then details. In an image generator, your words decide what the photograph becomes.

You will meet five key terms in every lesson. The prompt is the text you write. The model is the trained system that creates the image. The seed is a number that sets the starting noise. Because that starting noise is random, the same prompt normally gives a different picture each time. This is not an error. It is how the tool offers you choices.

The aspect ratio is the shape of the image. One to one is square, sixteen to nine is wide like a screen, and nine to sixteen is tall like a phone story. And a reference image is a picture you upload to guide the style or colours. You will use that in lesson six.

## Demonstrate
Let's see this in action. Lucía runs a small flower shop in Montevideo, Uruguay. She needs a picture for a spring sale poster, so she opens Gemini in her web browser and writes a short, simple prompt.

Her prompt asks for a bunch of yellow tulips in a glass jar on a wooden table. She generates it three times.

Every result shows yellow tulips in a glass jar on a wooden table, because those words are clear. But other things change. In one image the jar is round, in another it is tall and thin. The background is white, then green, then dark. The number of tulips changes, and the light comes from a different side each time.

Lucía understands what happened. The words she wrote were kept. The details she did not describe were filled in by the model, differently each time, because each generation started from different random noise. If she wants a white background and soft morning light every time, she must write those details in the prompt.

A common mistake is to think the generator finds a picture online and changes it a little. It does not work like a search engine. It creates a new picture from patterns it learned.

That is also why it can make mistakes no photograph would contain, like a hand with six fingers, or letters that are not real words. And a different result does not mean you did something wrong. Variation is normal. Generate several versions and choose the best one.

## Recap
Let's recap. First, an image generator learns patterns from many images and their descriptions, then builds a new image. Second, prompt, model, seed, aspect ratio and reference image are the basic controls in this course. Third, details you describe tend to stay the same, while details you leave out change each time.

## CTA
Now it is your turn. In the exercise below this video, you will generate one simple prompt three times in Gemini, then list what changed and what stayed the same. It takes about fifteen minutes. In the next lesson, we look at the anatomy of a strong prompt. See you there.

## Thumbnail
Headline: From Noise to Picture
Image: Navy background, a square card that fades from grey static on the left to a clear red bicycle against a blue wall on the right, headline in teal Inter Bold.

## Production Notes
- [VERIFY] content.md flags the description of diffusion and the note that some newer tools use other methods. The voiceover presents step-by-step building from noise only as 'a useful way to picture it' and does not say how many tools use it. A reviewer must confirm before recording.
- [VERSION] Gemini and Google AI Studio access, free-tier image limits and the regenerate option change often. Check the live tool before generating the example images.
- All example images on slides are generated in Gemini by the team from the prompts shown. No real people, logos or copyrighted characters in any image.
- Lucía and her Montevideo flower shop are fictional; stock footage must not show a real shop name or logo.
- No hero B-roll: generated example images on slides carry the visuals.
