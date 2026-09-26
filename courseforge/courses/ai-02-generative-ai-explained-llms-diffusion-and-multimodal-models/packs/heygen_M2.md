# HeyGen Batch Pack: AI-02 M2 (Images, Audio and Multimodal Models)

Course: Generative AI Explained: LLMs, Diffusion and Multimodal Models. Make one HeyGen video per lesson below, using these settings for every video.

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

## L05 How Diffusion Models Create Images

- **Filename:** `ai-02-generative-ai-explained-llms-diffusion-and-multimodal-models_M2_L05_presenter.mp4`
- **Expected length:** about 4.9 minutes (689 words). The quality gate accepts ±10%.

```text
Think of the grey snow on an old television with no signal. Many image generators start from this kind of randomness. A few seconds later, you have a detailed picture of a lighthouse at sunset. How does noise become a picture?

Welcome to Module two. So far, we have looked at language models. Now we turn to images, and to one common type of image generator, the diffusion model. What follows is a simplified picture. We look at training first, and then at generating.

In simple terms, training works like this. The model sees a huge number of images, each with a text description. Random noise is added to each image a little at a time, until only noise is left.

The model's task is to look at a noisy image and work out what noise was added, so that it can remove it and make the image a little clearer. Because it also sees the description, it learns what words like cat, watercolour or evening light usually look like.

Now, generating. When you type a prompt, the model starts from pure random noise. It removes noise in many small steps. At each step, your prompt steers the result, so the image looks more like your description. Early steps decide the large shapes. Later steps add details like texture and edges.

You can picture a photo slowly coming into focus in a darkroom. At first, the paper shows only grey shapes. Step by step, the details appear. Here, the prompt decides what the photo shows.

But the picture has one limit. In a real darkroom, the photo already exists on the film. A diffusion model creates a new picture that never existed before.

This matters for you in two ways. Every image starts from different random noise, so the same prompt gives a different image each time. And the prompt guides, but it does not control every detail. Anything you do not describe is filled in with typical patterns from training.

So if something matters to you, like the colour, the angle or the time of day, put it in the prompt. You will practise this in the next lesson.

Let's see this in an example. Kenji is a design student in Osaka. For a class project about local festivals, he types the same prompt into a free image generator four times. A paper lantern festival on a river at night, warm light, wide view.

First, what stays the same. All four images show lanterns, water and a night sky, with warm orange light. The prompt steered these things in every run. The words in the prompt acted like fixed points that every image had to follow.

Next, what changes. The number of lanterns, the position of the river, the camera angle, and whether there are people. None of these were in the prompt, so they came from the different starting noise.

And one thing goes wrong. One image has a sign on a boat, with letters that are not real words. Kenji learns that if he wants people on a bridge, or exactly five lanterns, he must describe it. Even then, exact counts and readable text may not be reliable.

A common mistake is to think an image generator searches the internet for a matching picture and edits it. A diffusion model does not search when it generates. It starts from noise and builds a new image. That is why you can ask for scenes nobody has ever photographed.

Let's recap. First, in simple terms, a diffusion model learns by removing noise from images that were gradually covered with noise, together with their descriptions. Second, to generate, it starts from pure noise and removes it step by step, with your prompt steering each step. Third, different starting noise explains why the same prompt gives different images.

Now try it yourself. In the exercise below, use a free image generator to create the same prompt four times. Then list what stays the same and what changes, and link it to noise and the prompt. It takes about twenty minutes. Next, we learn about guiding image generators. See you there.
```

## L06 Guiding Image Generators

- **Filename:** `ai-02-generative-ai-explained-llms-diffusion-and-multimodal-models_M2_L06_presenter.mp4`
- **Expected length:** about 4.9 minutes (683 words). The quality gate accepts ±10%.

```text
You type bread into an image generator and get a plain loaf on a white table. It is not wrong, but it is not what you imagined. The model filled every gap with the most typical choice. So how do you guide it?

In the last lesson, you saw that the prompt steers every step, and that the model fills in anything you do not describe. So a better prompt does not need magic words. It simply gives clearer guidance on the details that matter to you.

A useful checklist has six parts. The subject, meaning what is in the image. Say round loaves and small rolls, not just bread. The setting, meaning where it is. And the style, for example a realistic photograph, a flat illustration or a watercolour painting.

Then the composition, meaning how the image is arranged. A close-up, a wide view, or empty space at the top for a title. The lighting, like soft morning sunlight or warm evening light. And the aspect ratio, the shape of the image. Many tools set this with a menu, not in the prompt.

Some generators also offer extra settings, such as the number of images, a style preset, or a list of things to avoid. These differ between tools, so look around the settings before you start.

Two more tips. Change one or two things at a time, so you can see which change caused which effect. And do not ask for exact text inside the image. Image models often get letters wrong. Add the text later in a design tool.

Think of it like briefing a photographer you cannot speak to again. If you only say, take a photo of bread, they choose the place, the angle and the light themselves. A clear brief brings the result much closer to what you had in mind.

Let's try it. Wanjiru runs a small bakery in Nairobi. She wants a poster image of fresh bread on a market stall, to advertise her weekend stall. We will use the Gemini app, but any free image generator works.

First, she opens the image generator and chooses a tall, portrait shape, because the poster is tall. Then she types her first version. Bread on a market stall.

The result shows a generic loaf on a grey table, in a dark setting. It does not look fresh, local or inviting. Four words left almost everything to the model. So she adds the subject, the setting and the lighting.

Version two looks fresh and warm. Much better. But the image is full to the edges, and there is no space for the poster title. So she adds style and composition. A realistic photograph, a close-up, baskets in the lower half, and plain light sky in the upper half for a title.

Now she compares all three side by side. Each change fixed one problem. Version three has empty sky at the top, ready for the bakery name and opening hours, which she adds later in a design tool so the letters are correct.

Before printing, she checks the image closely for strange details. She also checks the tool's terms, to confirm she may use the image in advertising.

A common mistake is to add words like amazing, ultra-detailed and masterpiece, hoping for better quality. They rarely help, and very long prompts can confuse the model. Describe the six parts clearly, and use the tool's settings instead.

Let's recap. First, the model fills every gap with typical patterns, so a clear prompt gives better guidance. Second, describe subject, setting, style, composition and lighting, and choose the aspect ratio in the settings when you can. Third, improve in small steps, and add exact text in a design tool, not in the prompt.

Your turn. In the exercise below, write three versions of an image prompt for a business of your choice, such as a tea stall or a language school. Then generate each one, and note what each change improved. It takes about twenty-five minutes. Next, we look at multimodal models, with text, images and audio together. See you there.
```

## L07 Multimodal Models: Text, Images and Audio Together

- **Filename:** `ai-02-generative-ai-explained-llms-diffusion-and-multimodal-models_M2_L07_presenter.mp4`
- **Expected length:** about 4.9 minutes (687 words). The quality gate accepts ±10%.

```text
You take a photo of a handwritten note, and seconds later the text appears neatly typed on your screen. You speak a question, and get a written answer. One tool understood a picture, a voice and a sentence. What kind of model does that?

In the last two lessons, we worked with images. Most models so far use one type of data. A language model takes in text and gives text. A diffusion model takes in text and gives images. Each type of data, such as text, images, audio or video, is called a modality.

A multimodal model can take in, and sometimes produce, more than one modality. You upload a photo, chart or screenshot, and it describes it or copies out the text. You speak, and it writes down what you said. It can read its answer aloud. Or you give a photo and a question together, and it uses both.

These tools are very useful for turning messy real-world input into clean text. Think of a helpful colleague who can read your notes, look at your photos and listen to your voice messages, and then write a summary.

The colleague is fast and usually right, but sometimes misreads untidy handwriting. You would not send their summary to a client without checking it. Multimodal tools make typical mistakes too. They misread small, blurred or handwritten characters. They confuse numbers like one and seven. They skip a row, or fill in text that looks likely but is not there.

So you must check every value against the original. And think about safety. Photos often contain more personal information than you notice, such as names, addresses, card numbers or faces. Crop or cover these first, or use a sample document.

Let's see it in action. Diego owns a small hardware shop in Lima. His price list is handwritten on paper, and he wants a clean table he can paste into a spreadsheet.

First, he takes a clear photo in good light, straight from above, and crops out everything that is not the list. Then he opens Google AI Studio and starts a new chat. Claude or ChatGPT would also work.

He uses the upload button to add the photo. Then he types his request. Copy this price list into a table with the columns item, unit and price. And one important line. Do not guess. If a value is unclear, write unclear. That line gives the model permission to say it is not sure, instead of inventing a value.

He sends it, and a neat fifteen-row table comes back. It looks complete. But Diego does not trust the look. He places the table next to the photo and checks every row, one line at a time.

He finds two problems. A price of seventeen is really eleven in his handwriting. And one item is missing, because it was written at the edge of the paper. One value is marked unclear, which is helpful. He fixes them all.

Then he copies the corrected table into his spreadsheet. The task took minutes instead of an hour of typing. But it only worked because he checked it.

A common mistake is to trust a table because it looks neat and complete. A neat format says nothing about the values. The model predicts likely text from what it sees, so it can turn an unclear seven into a one. Ask it to mark unclear values, and check every one.

Let's recap. First, a multimodal model can take in or produce more than one type of data, such as images, speech and text. Second, it can turn photos, charts and recordings into clean text or tables, but it can misread small or unclear details. Third, check every value against the original, and remove personal details before you upload.

Now it is your turn. In the exercise below, upload a photo of a receipt, a timetable or a chart, ask for a table, and check every value against the original. Remember to cover any personal details first. It takes about twenty minutes. Next, we look at where each model type fails. See you there.
```

## L08 Where Each Model Type Fails

- **Filename:** `ai-02-generative-ai-explained-llms-diffusion-and-multimodal-models_M2_L08_presenter.mp4`
- **Expected length:** about 5.0 minutes (701 words). The quality gate accepts ±10%.

```text
A chatbot gives you a perfect-looking reference to a report that does not exist. An image generator draws a person with six fingers. A photo reader turns one point five kilos into fifteen. Each tool failed differently. If you know why, you know where to check.

In the last lesson, Diego caught two errors in his table. Today we look at the typical failures of all three families. Each one comes from how the model works. Start with language models.

Language models generate likely text, token by token. So they can invent facts and sources, like names, numbers, quotes or references that sound real but are not. And because of the knowledge cut-off, their answers can be out of date.

Image models build pictures from learned patterns. They can struggle with hands and fingers, which vary a lot and are small in most images. They can produce letters that are not real words, because they learned what text looks like, not how to spell.

They may not follow exact counts or positions, like exactly seven chairs. And if you ask for a doctor, you may get a very typical-looking person, because the model fills gaps with common patterns.

Multimodal models read images and audio and answer in text. They can misread small, blurred or handwritten details. They can miss parts, like a skipped row or quiet speech. And they can fill gaps with likely values that are not in the input.

Bias affects all three families. Models learn from huge collections of human-made text and images. If some groups, languages or places are missing or stereotyped in that data, the model can repeat it. In a chatbot's words, in the people an image model draws, or in how well a speech tool understands accents.

There is one more risk. Realistic generated audio and video make it easier for someone to fake a voice message or a video of a person saying something they never said. Here the problem is not a model mistake. It is a person using the output to deceive.

Think of three skilled workers. The writer is fluent, but sometimes invents a quote. The painter makes beautiful scenes, but struggles with small hands and signs. The typist is fast, but misreads untidy handwriting. A good manager knows where each one goes wrong and checks there first.

Let's see how this works in a newsroom. Farida is an editor at a news website in Casablanca. Her team uses three types of AI tool, and she writes a simple checking guide for her staff.

A reporter's AI draft includes a quote from a ministry spokesperson that nobody can find. Rule one: check every quote, number and source against an original document.

A designer's market illustration shows signs with letters that are not real words. Rule two: add real text in a design tool, and label AI images as illustrations, not photos. An intern turns a photo of a printed table into text, and one row is missing. Rule three: count the rows and check every number.

Farida adds a hypothetical case. A staff member gets a voice message that sounds exactly like Farida, asking for an urgent payment to a new supplier. It is fake. Rule four: for unusual requests about money or private data, confirm through a second, known channel, like calling back on a saved number.

A common mistake is to think a newer or more expensive model has no failures. It may fail less often, but the causes remain. So learn each family's typical failures, and check those points every time.

Let's recap. First, language models can invent facts and sources, image models can struggle with hands, text and counts, and multimodal models can misread details. Second, all three can repeat bias from their training data. Third, realistic generated audio and video increase the risk of deception, so confirm unusual requests another way.

Your turn. In the exercise below, collect one failure from a text tool, one from an image tool and one from a multimodal tool. For each, write one sentence about the likely cause. It takes about twenty-five minutes. Next week, we start choosing tools, with matching the task to the model. See you there.
```
