# HeyGen Batch Pack: AI-20 M1 (How AI Images Are Made and Prompted)

Course: AI Image Generation and Visual Design. Make one HeyGen video per lesson below, using these settings for every video.

| Setting | Value |
|---|---|
| Avatar | **Vaness** (standard avatar), ID `1bd001e7e50f421d891986aad5c8bbd2` |
| Voice | `1bd001e7e50f421d891986aad5c8bbd2` (the same ID as the avatar: if HeyGen does not list it as a voice, use Vaness's paired English voice and record its ID in DECISIONS.md) |
| Background | Solid colour **#00FF00** (pure green, no gradient, no image) |
| Resolution | 1080p (1920×1080) |
| Aspect ratio | 16:9 |
| Avatar framing | Centred, head and shoulders, same size in every lesson |
| Captions/subtitles | **Off** (captions are added in Stage 6) |
| Music | Off |
| Speed | Normal (1.0×) |

How to paste: copy the whole text block for a lesson into a single HeyGen scene. Each blank line is a natural pause. Do not add or change words, because the edit is timed to this exact narration.

Save each finished video with the exact filename shown, and upload it to `/incoming/`.

## L01 How AI Image Generators Work

- **Filename:** `ai-20-ai-image-generation-and-visual-design_M1_L01_presenter.mp4`
- **Expected length:** about 5.0 minutes (694 words). The quality gate accepts ±10%.
- **Pronunciation:** [VERIFY] content.md flags the description of diffusion and the note that some newer tools use other methods. The voiceover presents step-by-step building from noise only as 'a useful way to picture it' and does not say how many tools use it. A reviewer must confirm before recording.

```text
You type a red bicycle leaning against a blue wall. A few seconds later, you see a picture that never existed before. Nobody searched the internet for it, and nobody drew it. So where did it come from?

Hi, and welcome to AI Image Generation and Visual Design. In this first lesson, we look at what happens between your words and the finished image.

An AI image generator is a computer program that creates a new picture from a written description. First, it goes through training. During training, it studies a very large collection of images, together with short texts that describe them.

It does not store the pictures like a photo album. Instead, it learns patterns. What red usually looks like. How light falls on a wall. What shapes make a bicycle.

When you use the tool, a useful way to picture it is this. The image is built step by step from random noise. Noise looks like the grey, grainy static on an old television. At each step, the system removes a little noise and moves the picture closer to your words.

Think of a photograph appearing slowly in a darkroom tray. At first the paper is almost blank. Then soft shapes appear, then edges, then details. In an image generator, your words decide what the photograph becomes.

You will meet five key terms in every lesson. The prompt is the text you write. The model is the trained system that creates the image. The seed is a number that sets the starting noise. Because that starting noise is random, the same prompt normally gives a different picture each time. This is not an error. It is how the tool offers you choices.

The aspect ratio is the shape of the image. One to one is square, sixteen to nine is wide like a screen, and nine to sixteen is tall like a phone story. And a reference image is a picture you upload to guide the style or colours. You will use that in lesson six.

Let's see this in action. Lucía runs a small flower shop in Montevideo, Uruguay. She needs a picture for a spring sale poster, so she opens Gemini in her web browser and writes a short, simple prompt.

Her prompt asks for a bunch of yellow tulips in a glass jar on a wooden table. She generates it three times.

Every result shows yellow tulips in a glass jar on a wooden table, because those words are clear. But other things change. In one image the jar is round, in another it is tall and thin. The background is white, then green, then dark. The number of tulips changes, and the light comes from a different side each time.

Lucía understands what happened. The words she wrote were kept. The details she did not describe were filled in by the model, differently each time, because each generation started from different random noise. If she wants a white background and soft morning light every time, she must write those details in the prompt.

A common mistake is to think the generator finds a picture online and changes it a little. It does not work like a search engine. It creates a new picture from patterns it learned.

That is also why it can make mistakes no photograph would contain, like a hand with six fingers, or letters that are not real words. And a different result does not mean you did something wrong. Variation is normal. Generate several versions and choose the best one.

Let's recap. First, an image generator learns patterns from many images and their descriptions, then builds a new image. Second, prompt, model, seed, aspect ratio and reference image are the basic controls in this course. Third, details you describe tend to stay the same, while details you leave out change each time.

Now it is your turn. In the exercise below this video, you will generate one simple prompt three times in Gemini, then list what changed and what stayed the same. It takes about fifteen minutes. In the next lesson, we look at the anatomy of a strong prompt. See you there.
```

## L02 The Anatomy of a Strong Prompt

- **Filename:** `ai-20-ai-image-generation-and-visual-design_M1_L02_presenter.mp4`
- **Expected length:** about 5.0 minutes (692 words). The quality gate accepts ±10%.

```text
Two people type a coffee cup into the same tool. One gets a flat, forgettable picture. The other gets a warm image that could go on a café menu tomorrow. The tool is the same. The difference is the prompt.

In the last lesson, you saw that anything you do not describe is filled in by the model, often differently each time. A strong prompt reduces this guessing. It tells the model what matters to you.

A simple formula helps you remember what to include. Subject, action, setting, style, composition, lighting and colour. Read it as a checklist, not as a rule you must follow in exact order.

Here is each part for a cup of coffee. The subject is a white ceramic cup. The action is steam rising. The setting is a marble café counter. The style is a product photograph. Each part answers one simple question about the picture.

The composition is a close-up from slightly above. The lighting is soft morning light from a window. And the colour is warm browns and cream. You do not need all seven every time. A quick idea may need three parts. A picture for a client usually needs all of them.

Think of a prompt as instructions for a taxi driver in a city they do not know. Take me to the centre gets you somewhere. Take me to the north entrance of the central station, near the bus stop, gets you to the right door. Each extra detail removes one wrong destination.

Specific words beat long lists of adjectives. Beginners often add words like beautiful, stunning or high quality. But these words do not tell the model anything it can draw. Compare a beautiful cup with a cup with a thin gold rim. The second phrase gives the model something it can show.

So replace praise words with visible details. A material, a shape, a light direction, a colour. And keep the language plain, in short phrases or sentences. Most tools handle natural language well, so you do not need special codes.

Let's see the formula at work. Inês owns a small café in Lisbon, Portugal. She wants a photo-style image for her online menu. Her first prompt is just three words: a coffee cup.

The result is a plain cup on a grey background. It could belong to any café in the world. So she uses the formula to rewrite it.

You can read her new prompt on screen. In short, she asks for a white cup with a thin gold rim and light steam, on a pale marble counter, with custard tarts behind it. It is a close-up product photograph from slightly above, with the cup in the left third, soft morning window light, and warm cream and brown tones with a blue and white tile pattern.

Now the image looks like it belongs to her café. The tiles suggest Lisbon. The light feels like early morning. And there is empty space on the right, where she can add the price later in a design tool. Notice what she did not write. No amazing, and no masterpiece. Every word describes something the viewer can see.

A common mistake is to fix a weak result by adding more and more words. Soon the prompt is long, and details start to fight, like dark moody lighting and bright sunny day. Instead, find the part of the formula that caused the problem, and change only that part. Then generate again and compare. Changing one thing at a time shows you what each word does.

Let's recap. First, a strong prompt covers subject, action, setting, style, composition, lighting and colour, as the task needs. Second, visible details like materials, angles and light direction work better than praise words. Third, when a result is wrong, change one part at a time and compare.

Now it is your turn. In the exercise below, you will rewrite three weak prompts with the formula, generate both versions in Gemini, and compare them side by side. It takes about twenty minutes. In the next lesson, you will make your first images in Gemini and Firefly. See you there.
```

## L03 Your First Images in Gemini and Firefly

- **Filename:** `ai-20-ai-image-generation-and-visual-design_M1_L03_presenter.mp4`
- **Expected length:** about 5.2 minutes (730 words). The quality gate accepts ±10%.

```text
You now know how to write a strong prompt. Today, you will put the same prompt into two different tools, and watch them produce two different images. By the end, you will know where the main controls are.

This course uses two generators that you can start with for free: Gemini and Adobe Firefly.

Gemini is Google's AI assistant. You create images by chatting. You write a request, see the result, then ask for changes in plain language, like make the background lighter. Google AI Studio is a more technical Google workspace with more settings, and you can use it as an alternative.

Adobe Firefly is Adobe's image tool. It works more like a control panel. You write a prompt, then choose settings from menus, such as aspect ratio, content type, photo or art, and style effects. The free tier gives you a limited number of generative credits.

So what is the difference for a beginner? In Gemini, you change images through conversation, and you often ask for the aspect ratio in the prompt. In Firefly, you use buttons and menus. Each tool also has its own default look. And some tools add labels that show an image was made with AI. We come back to that in lesson ten.

Gemini is like asking a helpful assistant to draw for you, and giving feedback as you talk. Firefly is like working at a studio desk with labelled switches. Both can produce good work. They simply feel different to use.

One safety note before we start. While you practise, do not upload photos of real people, client files or anything confidential. Use your own simple prompts.

Let's make an image for Efua, who runs a small bakery in Accra, Ghana. You can read the prompt on screen. It asks for a wooden tray of sugar bread and meat pies on a bakery counter, as an eye-level product photograph with soft warm light, in golden brown and cream.

We start in Gemini. I open it in the browser and sign in with a Google account. I start a new chat, and if there is an image option in the tools menu, I select it. Then I paste the prompt and add one sentence: make it a square, one to one image.

Here is the result. Look at the details from the prompt. The tray, the loaves, the warm light from the left, and the small green plant. Now I type a follow-up. Keep everything the same, but make the background slightly darker.

The background is darker, and the bakes stand out more. That is the Gemini way. You improve the image by talking to it. When I am happy, I open the image and use the download option to save it.

Now Adobe Firefly. I open the Firefly website, sign in with a free Adobe account, and choose text to image. I paste the same prompt, but without the sentence about the aspect ratio, because here we use the settings panel instead.

In the panel, I set the aspect ratio to square, and the content type to photo. Notice the credit counter. Each generation uses credits, so plan your prompt before you click. Now I click generate.

Here are the Firefly results. I hover over the best one and download it. Now let's place both images side by side and compare.

Two differences stand out here. The lighting feels different in each image, and one tool shows more of the counter than the other. Neither is simply better. The right choice depends on what Efua's bakery needs.

A common mistake is to decide that one tool is better after one test. Every generation is random, so compare several results against your brief. And do not spend all your free credits on quick experiments.

Let's recap. First, Gemini works through conversation, while Adobe Firefly works through a panel of settings like aspect ratio and content type. Second, the same prompt gives different results in different tools, so judge them against your brief. Third, free tiers have limits that change often, so plan before you generate.

Now it is your turn. In the exercise below, you will create one image for the Accra bakery in both tools from the same prompt, and note two differences. It takes about twenty minutes. In the next lesson, we explore composition, lighting and colour words. See you there.
```

## L04 Composition, Lighting and Colour Words

- **Filename:** `ai-20-ai-image-generation-and-visual-design_M1_L04_presenter.mp4`
- **Expected length:** about 4.8 minutes (667 words). The quality gate accepts ±10%.

```text
Photographers can make the same street look calm, exciting or mysterious, without moving a single object. They do it with the camera angle, the light and the colours. You can do the same with a few well-chosen words.

In lesson two, you met the prompt formula. Today, we focus on three of its parts: composition, lighting and colour. The best words for these come from photography and design, because image models learned from many pictures described with this language.

Composition words control framing and viewpoint. A close-up fills the frame with the subject, which is good for products. A medium shot shows the subject with some surroundings. A wide shot shows the whole scene, which is good for places.

Then there is the camera angle. Eye level feels natural. A low angle looks up, so the subject feels large and strong. Top-down, or flat lay, looks straight down, which is popular for food. And you can ask for empty space on the left or right, to leave room for text later.

Lighting words control mood. Soft window light is gentle and natural. Golden hour is warm, low sunlight near sunrise or sunset. Overcast daylight is even and cool. High contrast is dramatic. And backlit means the light is behind the subject, often with a bright outline.

Colour words control the palette. A limited palette of two or three named colours keeps an image simple and on brand. Muted or pastel colours feel calm. Saturated colours feel energetic. And warm or cool tones change the feeling of the whole image.

What about brand colours? Image generators often do not follow colour codes reliably. So describe the colour in words instead, like deep ocean blue or soft sand beige. Then correct the exact colour later in a design tool, as you will do in lesson eight.

Think of a small film studio. Composition, lighting and colour are the camera, the lamps and the paint. The set can stay the same, but move the camera, change the lamps or repaint the wall, and you get a different scene.

Let's see this in practice. Haruto works for a small travel agency in Kyoto, Japan. He needs images of a quiet garden path for three different tour packages.

His prompt is on screen. It keeps the subject, the wide shot at eye level, the empty space on the right, and a palette of green, stone grey and deep red. Only the lighting changes. There is a gap where he swaps in three different lighting phrases.

First, soft overcast morning light. This gives a calm, even image for a relaxing mornings tour. Second, golden hour sunlight through the leaves. Now the light is warm with long shadows, which suits an evening walks tour.

Third, lantern light at night, high contrast. This gives a dark, dramatic image for a night lanterns tour. Because only one part changed, Haruto can see exactly what each lighting phrase does.

The three images also look related, because the subject, the composition and the palette stayed the same. And the empty space on the right is useful for the tour name and the price.

A common mistake is to mix words that contradict each other, like top-down and low angle, or golden hour and overcast. The model cannot show both, so it picks one, or gives you a confused image. Choose one term per category.

Let's recap. First, words from photography, like close-up, top-down, golden hour and high contrast, give you precise control. Second, changing one part of a prompt at a time shows you what each word does. Third, describe brand colours in words, and fix exact colour values later in a design tool.

Now it is your turn. In the exercise below, you will generate one scene in three versions that change only the angle, the lighting or the colour, and label what each word changed. It takes about twenty minutes. In the next lesson, we learn to describe a style without copying artists. See you there.
```
