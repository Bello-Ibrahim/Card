# L01 How AI Image Generators Work

Course: AI-20 · Module: M1 · Objectives: O1 · Video: 5 min

## Hook
You type "a red bicycle leaning against a blue wall" and, a few seconds later, you see a picture that never existed before. Nobody searched the internet for it and nobody drew it. Where did it come from? This lesson explains what happens between your words and the finished image.

## Explanation
An AI image generator is a computer program that creates a new picture from a written description. To do this, it first goes through **training**. During training, the system studies a very large collection of images together with short texts that describe them. It does not store the pictures like a photo album. Instead, it learns patterns: what "red" usually looks like, how light falls on a wall, what shapes make a "bicycle".

When you use the tool, most current generators build the image **step by step from random noise**. Noise looks like the grey, grainy static on an old television. The system removes a little noise at each step and moves the picture closer to something that matches your words. After many small steps, a clear image appears. This family of methods is often called **diffusion**. Some newer tools use other methods, but the basic idea of building an image gradually from a description is a useful mental model. [VERIFY]

**Analogy:** Think of a photograph appearing slowly in a darkroom tray. At first the paper is almost blank. Then soft shapes appear, then edges, then details. In an AI generator, your words decide what the photograph becomes as it appears.

Five key terms appear in every lesson of this course:

- **Prompt:** the text you write to describe the image you want.
- **Model:** the trained system that creates the image. Different tools use different models, and each model has its own strengths.
- **Seed:** a number that sets the starting noise. The same prompt with a different seed gives a different image. Some tools let you see or fix the seed; many hide it.
- **Aspect ratio:** the shape of the image, written as width to height. 1:1 is square, 16:9 is wide like a screen, and 9:16 is tall like a phone story.
- **Reference image:** a picture you upload to guide the style, colours or layout of the new image. You will use this in L06.

Because the starting noise is random, the same prompt normally gives a different picture each time. This is not an error. It is how the tool offers you choices.

## Worked Example
Lucía runs a small flower shop in Montevideo, Uruguay. She needs a picture for a spring sale poster. She opens Gemini and writes a short prompt:

```text
A bunch of yellow tulips in a glass jar on a wooden table
```

She generates it three times. Every result shows yellow tulips in a glass jar on a wooden table, because these words are clear. But other things change each time. In one image the jar is round; in another it is tall and thin. The background is white in one, green in another and dark in the third. The number of tulips changes, and the light comes from a different side each time.

Lucía understands what happened. The words she wrote were kept. The details she did not describe were filled in by the model, differently each time, because each generation started from different random noise. If she wants a white background and soft morning light every time, she must write those details in the prompt. You will learn how to do this in L02.

## Common Mistake
Many beginners think the generator finds an existing picture online and changes it a little. It does not work like a search engine. It creates a new arrangement of pixels based on patterns it learned. This is also why it can make mistakes that no photograph would contain, such as a hand with six fingers or letters that are not real words. The model knows what things usually look like, but it does not understand them in the way a person does.

A second mistake is to think a different result means you did something wrong. Variation is normal. Use it: generate several versions and choose the best one.

## Key Takeaways
1. An AI image generator learns patterns from many images and their descriptions, then builds a new image step by step from random noise.
2. The prompt, model, seed, aspect ratio and reference image are the basic controls you will use throughout this course.
3. Details you describe tend to stay the same between generations; details you leave out are filled in differently each time.

## Hands-on Exercise
**Task:** Generate the same simple prompt 3 times in Gemini, then write down what changed between the results and what stayed the same.
**Tools:** Gemini (free, with a Google account) or Google AI Studio as an alternative; a notes app or paper. [VERSION]
**Steps:**
1. Open Gemini and start a new chat. Do not paste any personal or confidential information into the chat.
2. Write this prompt, or a similar short one for your own business idea: "A ceramic teapot on a kitchen shelf".
3. Generate the image. Then ask for it again in a new chat, or use the option to regenerate, until you have 3 results. [VERSION]
4. Save or screenshot all 3 images.
5. Make a two-column table: "Stayed the same" and "Changed". Write at least 3 items in each column.
6. Next to each "Changed" item, write the words you could add to the prompt to control it.
**What good looks like:** A table showing that the subject in the prompt stayed the same, while unlisted details (background, angle, colours, light, number of objects) changed. Each changed item has a suggested prompt word, such as "white background" or "seen from the side".
**Time:** about 15 minutes

## Review Flags
- [VERIFY] The description of diffusion as the method used by most current generators, and the note that some newer tools use other methods, should be checked by a reviewer before recording.
- [VERSION] Gemini and Google AI Studio access, free-tier image limits and the regenerate option change often and must be checked against the live tools.
