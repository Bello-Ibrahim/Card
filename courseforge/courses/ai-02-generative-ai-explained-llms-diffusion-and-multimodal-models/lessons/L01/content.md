# L01 From Predicting to Generating

Course: AI-02 · Module: M1 · Objectives: O1 · Video: 5 min

## Hook
You ask a chatbot for a birthday poem and it writes one in seconds. Another tool draws a picture of a cat in a spacesuit. A third one listens to a voice note and replies in writing. Are these three tools doing the same thing? Not quite, and this course shows you why.

## Explanation
In AI Fundamentals you learned that most machine learning models **predict**. A spam filter predicts a label ("spam" or "not spam"). A delivery app predicts a number (the minutes until your parcel arrives). The output is always small and chosen from a limited set of possible answers.

**Generative AI** is different. A generative model produces **new content**: a paragraph, a picture, a piece of music, a spoken sentence or a short video. The content did not exist before, and there are almost endless possible outputs. Generative models still learn patterns from very large amounts of examples, as all machine learning models do. The difference is what they do with those patterns: they use them to build something new that looks like the examples.

This course uses a simple map with three families of generative models.

- **Large language models (LLMs)** work with text. They write emails, answer questions, summarise documents, translate and write computer code. Chatbots are the best-known example. You study them in Module 1.
- **Diffusion models** are a common way to create images. They start from random visual "noise" and slowly turn it into a picture that matches a text description. Some tools use similar ideas for audio and video. You study them in Module 2.
- **Multimodal models** can take in or produce more than one type of data. A multimodal model can read a photo and answer in text, or listen to speech and write it down. You also study them in Module 2.

The borders between the families are not always sharp. Many modern tools combine them. A chatbot may use a language model to understand your request and then call an image model to draw a picture. When you use a tool, it is useful to ask: "What type of output does this produce, and what type of model is most likely behind it?"

**Analogy:** Think of a restaurant kitchen. A predictive model is like a cook who checks each dish and says "ready" or "not ready". A generative model is like a cook who creates a new dish. A language model is the cook who writes the menu descriptions, a diffusion model is the one who arranges the food so it looks beautiful on the plate, and a multimodal model is the head chef who can look at a photo of a dish, read the order and speak to the waiters.

## Worked Example
Mei Lin works as a communications officer for a hypothetical environmental charity in Kuala Lumpur, Malaysia. In one week she uses several AI tools, and she wants to understand what type of model is behind each one.

- On Monday she asks a chatbot to write three short social media posts about a beach clean-up. The output is **text**, so a **language model** most likely produced it.
- On Tuesday she asks an image tool for a picture of volunteers collecting plastic on a beach at sunrise. The output is a **new image** made from a text description, so a **diffusion model** (or a similar image model) most likely produced it.
- On Wednesday she uploads a photo of a hand-drawn chart from a volunteer meeting and asks for a short summary. The tool reads an **image** and answers in **text**, so a **multimodal model** is involved.
- On Thursday her email app marks a message as "important". This is a **label**, not new content, so it is a predictive model, not generative AI.

By asking "what goes in, and what comes out?", Mei Lin can place each tool on the map.

## Common Mistake
Many learners think generative AI "searches the internet and copies" an answer or an image. Usually it does not. A generative model builds new output from patterns it learned during training. This is why the output can be original, and it is also why it can be wrong: the model produces something that looks right, not something it has checked. Some tools add a web search step, but the model still writes the final answer itself.

## Key Takeaways
1. Predictive models choose a label or a number, while generative models produce new text, images, audio or video.
2. This course covers three families: large language models (text), diffusion models (images) and multimodal models (more than one type of data).
3. To place a tool on the map, ask what type of data goes in and what type of content comes out.

## Hands-on Exercise
**Task:** Sort 10 example outputs by the model family that most likely produced them, then check the answer key.
**Tools:** Pen and paper or any notes app.
**Steps:**
1. Read these 10 outputs: (a) a product description for an online shop; (b) three logo ideas shown as pictures; (c) a written transcript of a voice message; (d) a two-sentence summary of a chart from a photo; (e) a translated email; (f) a poster image of a city at night; (g) an answer to "What is in this photo?"; (h) a short story for children; (i) a list of alt text for five product photos; (j) an illustration of a mountain in watercolour style.
2. Label each one "language model", "diffusion model" or "multimodal model".
3. Next to each label, write what goes in (text, image, audio) and what comes out.
4. Check your answers with the answer key on the course page.
**What good looks like:** Text-in, text-out items (a, e, h) are labelled "language model". Text-in, image-out items (b, f, j) are labelled "diffusion model". Items that read images or audio (c, d, g, i) are labelled "multimodal model". Each label has a short "in and out" reason.
**Time:** about 15 minutes

## Review Flags
- None. This lesson gives only a short recap of AI Fundamentals (the prerequisite) and uses general, hypothetical examples with no facts that need checking.
