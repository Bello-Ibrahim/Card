# HeyGen Batch Pack: AI-01 M3 (What AI Can and Cannot Do)

Course: AI Fundamentals: How Machines Learn. Make one HeyGen video per lesson below, using these settings for every video.

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

## L09 Generative AI and Chatbots

- **Filename:** `ai-01-ai-fundamentals-how-machines-learn_M3_L09_presenter.mp4`
- **Expected length:** about 5.0 minutes (700 words). The quality gate accepts ±10%.

```text
A chatbot writes a birthday poem in seconds. Ask it for the source of a quotation, and it may give a book that does not exist, in the same confident voice. How can one system be so helpful, and so wrong?

Welcome to the final week. In the first lesson, you saw generative AI as the smallest circle. It means systems that create new content, such as text, images or sound, instead of only choosing a label, like spam.

A chatbot is built on a language model. During training, the model reads a very large amount of text. Its job is simple. Look at the words so far, and predict the next word. After the sun rises in the, the word east is very likely.

Each time it guesses badly, its dials, the weights from lesson seven, are nudged a little. This repeats over a huge amount of text. Then, when you use the chatbot, it predicts a likely next word, adds it to the answer, and predicts the next one, until the answer is complete.

This one idea explains two things. First, fluency. The model has seen so much text that its answers follow the patterns of good writing, so they sound natural. Second, hallucination. That is an answer that sounds correct, but is false or invented.

Why does it happen? The model is trained to produce text that is likely, not text that is true. And it has no built-in sense of I do not know.

Imagine a person who has listened to many university lectures, but never checked any facts. Ask them a question, and they answer like a professor, with the right words and the right confidence. Sometimes they are right. Sometimes they fill a gap with something that only sounds right. From their voice alone, you cannot tell which.

Image generators work in a similar way. They learn patterns from many images and their descriptions, then build a new image that fits your words. They do not copy one stored picture. And they also make errors, like a hand with the wrong number of fingers.

Let's see both results in one task. Rafael is a secondary school history teacher in Porto, Portugal. He uses a chatbot to prepare a lesson about ocean trade routes.

First, he asks it to write a short, simple introduction to trade routes for thirteen year olds. The result is clear and well organised. This task needs fluent, general writing, and Rafael can check it just by reading.

Next, he asks for three books about Portuguese sea trade, with authors and page numbers for key quotations. The chatbot gives three titles, three authors and exact page numbers. It looks perfect.

Rafael checks his school library catalogue and an online bookshop. One book is real. One real author is listed with a book title that does not exist. And the third book cannot be found anywhere.

Why? A list of books with authors and page numbers is a common shape of text. The model produced that shape, without checking that each item was real. So Rafael keeps the introduction, removes the reading list, and builds his own list from the library catalogue.

A common mistake is to think that a chatbot is a smarter search engine. It generates text from patterns. Some chatbots can also search the web, but the final answer is still generated. A confident tone is not evidence. Treat any fact, number, name or source as a claim to check.

Let's recap. First, a language model is trained to predict the next word, and a chatbot builds its answer one predicted word at a time. Second, this explains both fluency and hallucination. The model produces text that is likely, which is not always true. Third, use chatbots for drafting and explaining, and always check facts, names, numbers and sources.

Now it is your turn. In the exercise below this video, ask ChatGPT or Claude three factual questions that you can check. Verify each answer in a reliable source, and record any errors. In the next lesson, we look at where AI goes wrong for whole groups of people, in Bias, Data and the Limits of AI. See you there.
```

## L10 Bias, Data and the Limits of AI

- **Filename:** `ai-01-ai-fundamentals-how-machines-learn_M3_L10_presenter.mp4`
- **Expected length:** about 4.9 minutes (682 words). The quality gate accepts ±10%.

```text
Imagine a job application system that rejects people from one region more often than people from another. Nobody told it to do that. So where did the unfairness come from? Usually, from the examples it learned from.

In lesson three, you learned that the quantity, variety and quality of examples matter. Today we look at what happens when the examples are not a fair picture of the world.

Bias in AI means that a system's outputs are unfair, or less accurate, for some groups of people or some situations, again and again. The most common cause is unrepresentative data.

This can happen in three main ways. Missing groups: some people appear rarely in the training data, so the model makes more mistakes for them. Unfair past decisions: if the labels come from past human decisions that were unfair, the model learns the unfairness as if it were correct.

And proxy features. A feature can quietly stand in for something sensitive. For example, a home postcode can be linked to income or background, even when those are not in the data. Remember, a model does not know what is fair. It only finds patterns that match its labels.

Bias is not the only limit. Privacy: training data often contains information about real people. Using it without clear permission can harm them, and personal details can sometimes appear in outputs. No real-world understanding: a model finds patterns, but it does not understand causes, context or common sense.

And changing conditions. A model learns from the past. When the world changes, with new customer habits, new products or a new season, the old patterns can stop working. The model does not warn you. Its accuracy just quietly falls.

Think of a cook who learned every recipe in one small village. Give them spices they have never seen, or guests with different tastes, and the results are poor. A model trained on narrow data is the same. Skilled inside its experience, and unreliable outside it.

Here is a hypothetical case. A mid-sized bank in Malaysia wants to speed up small business loan decisions. Its data team, led by Nurul, trains a model on ten years of past loan applications.

Each example has features such as business type, years open, monthly income and location. The label is approved or rejected, taken from past decisions by loan officers. The model scores well overall. But when the team checks results by group, they find three problems.

First, missing groups. Few past applicants ran online-only businesses, so the model often rejects them, even when their income is strong. Second, unfair past decisions. In some rural branches, officers approved fewer loans for reasons that had little to do with risk, and the model copied that pattern.

Third, proxy features. The location feature lets the model treat whole districts as higher risk. That affects applicants who are, individually, reliable.

Nurul's team keeps the model, but they collect more online-only examples, review the old labels, test each group separately, and keep a human officer in charge of every rejection.

A common mistake is to think that a computer decision must be neutral. A model reflects the data and labels people chose to give it. So ask, whose examples did it learn from, and who is missing? And check accuracy for each group, not only overall. As you saw in lesson eight, a high overall score can hide poor results for a smaller group.

Let's recap. First, bias usually comes from unrepresentative data: missing groups, unfair past decisions used as labels, or proxy features. Second, other limits include privacy, no real-world understanding, and changing conditions. Third, check results separately for different groups, and keep a person responsible for important decisions.

Now it is your turn. In the exercise below this video, choose a hypothetical hiring or loan model, and list three ways its training data could be unrepresentative. For each one, name who could be treated unfairly, and one action that helps. Your capstone project starts in the next lesson, Build Your Own Image Classifier, where you train a model yourself. See you there.
```

## L11 Build Your Own Image Classifier

- **Filename:** `ai-01-ai-fundamentals-how-machines-learn_M3_L11_presenter.mp4`
- **Expected length:** about 4.9 minutes (689 words). The quality gate accepts ±10%.

```text
You have learned how machines learn from examples. Today, you will teach one yourself, in your web browser, with no code and no maths. You will build a model that recognises objects you choose, and see where it succeeds, and where it fails.

We will use Google Teachable Machine. It is a free tool that trains simple models in your browser. We will make an image project, a model that looks at a picture and predicts its class. That is supervised classification, from lesson five.

Every step in the tool matches a word you already know. The classes are your labels. The example images are your data. You do not choose the features. The model finds its own patterns, like shapes, colours and textures. Training adjusts the model's dials. And the preview is where you test it, with new images.

It is like teaching a young child to name fruit with real examples. If you only show yellow bananas on a white table, a green banana on a wooden table may confuse them. Varied examples help the child, and the model, handle new cases.

One privacy point before we start. Use objects, such as fruit, or pens and cups. Do not use photos of other people without their clear consent. And check the tool's privacy information before you begin.

Let's follow Chiamaka. She runs a small recycling project at a community centre in Enugu, Nigeria. She wants a simple demonstration that tells a plastic bottle from a metal can. Let's build it together.

First, open Teachable Machine in your browser. Start a new project, and choose a standard image project. The interface may look a little different when you try it, so follow the ideas, not the exact screen.

Next, rename the two empty classes. Chiamaka calls them plastic bottle, and metal can. These are the labels. You can add a third class if you want.

Now add the data. Use the Webcam option to record frames of each object, or the Upload option to choose image files. Chiamaka records about thirty images per class. She uses different sizes and colours, different angles, and some crushed and some whole items.

Then click Train, and keep the browser tab open until it finishes. This is the training phase. The model is nudging its dials to match the images to the labels.

Now test it in the preview area, with ten new items it has never seen. For each one, read the confidence bars. Chiamaka's model gets eight out of ten right.

It fails on a clear bottle held in front of a window, and on a very shiny can. Her training images all had dull indoor light. So the model may have learned that bright and shiny means can. She adds images taken near the window, trains again, and tests with new items. The results improve.

You do not need the advanced settings or the export options for your capstone. But before you close the tab, take two screenshots. One of your classes, and one of a test result. You will need them as evidence.

That is the full cycle. Data, labels, training, testing, and better data. And watch out for one mistake. If you test with the same objects, angles and light you trained on, the results look perfect, but they tell you almost nothing. Test with new objects, backgrounds and lighting, and record the failures honestly.

Let's recap. First, in Teachable Machine, classes are labels, your images are the data, the Train button runs training, and the preview is where the model makes predictions. Second, varied examples help the model handle new cases. Third, test with new images the model has never seen, and record every result, including the mistakes.

Now it is your turn. This is step one of your capstone. Train a classifier with at least two classes, and twenty or more varied images per class. Then test it on ten new images, and record the results in a table, with two screenshots. Keep them safe. In the last lesson, Should I Trust This AI? A Practical Checklist, you will explain your model. See you there.
```

## L12 Should I Trust This AI? A Practical Checklist

- **Filename:** `ai-01-ai-fundamentals-how-machines-learn_M3_L12_presenter.mp4`
- **Expected length:** about 5.0 minutes (692 words). The quality gate accepts ±10%.

```text
An app says a photo of your plant shows a disease. A chatbot gives you a clear summary of a new law. Should you act on either? You do not need to be an engineer to decide. You need five good questions.

You have learned how models learn from data, how they are tested, why chatbots hallucinate, and how biased data causes unfair results. You even trained your own model. In this final lesson, we turn all of that into a checklist for any AI system.

Question one. What data did it learn from? Were the examples varied, and do they represent the people and situations it will meet? If you cannot find out, treat that as a warning sign. Question two. How was it tested? On new examples it never saw? And were results checked for different groups, not only as one overall score?

Question three. Who could it fail? Think about the groups or situations that were rare in the data. Question four. Can I verify the output, against a reliable source, a second opinion, or my own knowledge? Remember, a fluent answer is not a verified answer.

Question five. What happens if it is wrong? A wrong song suggestion costs you a few minutes. A wrong medical, legal or money answer can cause real harm. The higher the cost of a mistake, the more checking and human review you need.

The aim is not to reject AI. It is to match your trust to the evidence, and to the risk.

Using the checklist is like checking a used car before you buy it. You ask where it has been driven, whether it passed an inspection, what problems it is known for, whether you can test drive it, and what a breakdown would cost you. You would not refuse every used car. You simply decide carefully.

Let's use the checklist. Sofía works for a farming cooperative in Mendoza, Argentina. Members want to use a free phone app that identifies grape leaf diseases from a photo.

Data. The app's website says it learned from leaf photos, but not which regions or grape varieties. Sofía notes this as unknown. Testing. No test results are published. So she runs a small test herself, with fifteen leaves an expert has already checked. The app is right on most healthy leaves, but misses some early disease.

Who could it fail? Local grape varieties, and leaves photographed in strong midday sun. Can members verify? Yes. They can send unclear cases to the cooperative's plant expert. And if it is wrong? A missed disease could spread across a field, so the cost is high.

Her decision. Members may use the app as a first check. But any healthy result on a leaf that looks unusual must still go to the expert. Notice that trust is not yes or no. The same system can be trustworthy for one task, and not for another. The question is how to use the output, as a draft, a first check, or a final decision.

Now use the same checklist on your own model. This is step two of your capstone. On one page, explain how your classifier learned, how you tested it, where it failed and why, your answers to the five questions, and one improvement to your data. Use the course words correctly, and write it so that a friend with no technical background can follow it.

Let's recap. First, ask five questions. What data did it learn from? How was it tested? Who could it fail? Can I verify the output? And what happens if it is wrong? Second, match your trust to the evidence, and to the cost of a mistake. Third, the same checklist helps you explain your own model in your capstone.

Congratulations. You have finished AI Fundamentals. You now know how machines learn, how to test them, and when to trust them. Your last step is the capstone. Write your one-page explanation, attach your test table and screenshots, and check your work against the rubric. It takes about forty minutes. Then submit it below this video. Well done, and thank you for learning with us.
```
