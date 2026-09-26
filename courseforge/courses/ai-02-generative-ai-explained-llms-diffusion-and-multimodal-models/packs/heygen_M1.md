# HeyGen Batch Pack: AI-02 M1 (How Language Models Write)

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

## L01 From Predicting to Generating

- **Filename:** `ai-02-generative-ai-explained-llms-diffusion-and-multimodal-models_M1_L01_presenter.mp4`
- **Expected length:** about 5.1 minutes (708 words). The quality gate accepts ±10%.
- **Pronunciation:** No facts to verify: content.md Review Flags say None. All examples are general or hypothetical.

```text
You ask a chatbot for a birthday poem, and it writes one in seconds. Another tool draws a cat in a spacesuit. A third listens to a voice note and replies in writing. Are these three tools doing the same thing? Not quite. Let's see why.

Hi, and welcome to Generative AI Explained: LLMs, Diffusion and Multimodal Models. In this first lesson, we draw a simple map of the tools you will meet in this course.

In AI Fundamentals, you learned that most machine learning models predict. A spam filter predicts a label, spam or not spam. A delivery app predicts a number, the minutes until your parcel arrives. The answer is small, and it comes from a limited set of options.

Generative AI is different. A generative model produces new content. A paragraph, a picture, a piece of music, a spoken sentence or a short video. This content did not exist before, and the possible outputs are almost endless.

Generative models still learn patterns from huge numbers of examples, like all machine learning models. The difference is what they do with those patterns. They use them to build something new that looks like the examples.

This course uses a map with three families. Large language models work with text. They write emails, answer questions and summarise documents. Diffusion models are a common way to create images. They start from random visual noise and slowly turn it into a picture that matches a description.

And multimodal models can take in or produce more than one type of data. They can read a photo and answer in text, or listen to speech and write it down. The borders are not always sharp. Many tools combine these families.

Here is a simple way to picture it. Think of a restaurant kitchen. A predictive model is like a cook who checks each dish and says ready or not ready. A generative model is a cook who creates a new dish.

In this kitchen, the language model writes the menu descriptions. The diffusion model arranges the food so it looks beautiful on the plate. And the multimodal model is the head chef, who can look at a photo of a dish, read the order and speak to the waiters.

Let's use the map. Mei Lin is a communications officer for an environmental charity in Kuala Lumpur. In one week she uses several AI tools, and she wants to know what type of model is behind each one.

On Monday, she asks a chatbot for three short social media posts about a beach clean-up. Text goes in, text comes out. So a language model most likely wrote them.

On Tuesday, she asks an image tool for volunteers collecting plastic on a beach at sunrise. Text goes in, and a new image comes out. So a diffusion model, or a similar image model, most likely made it.

On Wednesday, she uploads a photo of a hand-drawn chart and asks for a short summary. An image goes in, and text comes out. That means a multimodal model is involved.

And on Thursday, her email app marks a message as important. That is a label, not new content. So it is a predictive model, not generative AI. Her simple question is always the same. What goes in, and what comes out?

One common mistake is to think that generative AI searches the internet and copies an answer. Usually it does not. It builds new output from patterns it learned. That is why the output can be original. It is also why it can be wrong. It looks right, but nobody checked it.

Let's recap. First, predictive models choose a label or a number, while generative models produce new text, images, audio or video. Second, this course covers three families: language models, diffusion models and multimodal models. Third, to place a tool on the map, ask what goes in and what comes out.

Now it is your turn. In the exercise below this video, you will sort ten example outputs, from a product description to a watercolour mountain, into the three families. Then you check the answer key. It takes about fifteen minutes. In the next lesson, we look at tokens and next-token prediction. See you there.
```

## L02 Tokens and Next-Token Prediction

- **Filename:** `ai-02-generative-ai-explained-llms-diffusion-and-multimodal-models_M1_L02_presenter.mp4`
- **Expected length:** about 4.9 minutes (691 words). The quality gate accepts ±10%.

```text
When you type see you on your phone, the keyboard suggests tomorrow, or soon. A large language model does something very similar, but it can write a full report this way. How does a simple guess about the next word become a whole page?

In the last lesson, we placed language models on our map. Now let's look inside. A language model does not read text the way you do. First, it splits the text into small pieces called tokens.

A token can be a short word, like cat. It can be part of a longer word. Unbelievable might become three pieces. It can also be a number or a punctuation mark. Each token is turned into numbers the model can work with.

Different models split text in different ways. So the same sentence can have a different number of tokens in different tools.

Then the model does one job, again and again. It looks at all the tokens so far, and it calculates how likely each possible next token is. After the capital of France is, the token Paris gets a very high score.

The model chooses a token, adds it to the text, and repeats the process with the new, longer text. One token at a time, it builds sentences, paragraphs and pages.

This explains two important facts. The model writes by choosing likely text, not by looking up checked facts. And it looks at the whole conversation each time, not only the last word. That is why it can keep the same topic and style.

So it is like the suggestions on your phone keyboard, but trained on far more text. Now, the model does not always pick the most likely token. A setting called temperature controls how much variety it allows.

At a low temperature, it picks the most likely tokens almost every time. Answers are predictable, which suits summaries or extracting data. At a high temperature, less likely tokens get more chance. Answers are more varied and creative, but they can drift off topic. Think of always tapping the first suggestion, or sometimes the second or third.

Let's try it. Tomasz leads a customer support team at an online furniture shop in Kraków. He wants a model to write short replies to customers, so he tests one prompt in Google AI Studio.

He opens Google AI Studio in his browser, signs in with a Google account and starts a new prompt. On the right is the run settings panel, with the temperature control.

He sets the temperature low, near the bottom of the range. Then he pastes his prompt. Write a two-sentence reply to a customer whose sofa delivery is one day late. He runs it three times and copies each answer.

The three replies are almost the same. A polite apology, and a new delivery date. Now he moves the temperature near the top of the range and runs the same prompt three more times.

This time the replies differ more. One offers a discount code. One uses a very informal tone. And one promises a free cushion, which the shop does not offer. Tomasz decides that customer replies need a low temperature. The shop cannot promise things it does not provide.

A common mistake is to think the model knows the full answer first and then types it out. It does not. It predicts each token from what came before. So a small change can send the answer in a new direction. Fluent text is likely text, not checked text.

Let's recap. First, a language model splits text into tokens and writes by predicting the next token, again and again. Second, it chooses likely text based on the whole conversation, so fluent answers are not automatically correct. Third, temperature controls variety. Low values are more predictable, and high values are more varied.

Now you try. In the exercise below, run one prompt three times at a low temperature and three times at a high temperature in Google AI Studio. Then describe the difference in two sentences. It takes about twenty minutes. Next, we look at how a language model is trained. See you there.
```

## L03 How a Language Model Is Trained

- **Filename:** `ai-02-generative-ai-explained-llms-diffusion-and-multimodal-models_M1_L03_presenter.mp4`
- **Expected length:** about 4.9 minutes (679 words). The quality gate accepts ±10%.

```text
A language model can write a polite email, explain a science topic, and refuse to help with something harmful. Nobody typed those answers in for it. So where does this behaviour come from? The answer is in how the model was trained.

In the last lesson, you saw that a model writes by predicting the next token. Today we ask how it learns to do that well. Training usually happens in stages. What you will see is a simplified picture. Providers use different methods, and they combine these stages in their own ways.

Stage one is pre-training. The model sees a very large collection of text, such as books, articles, websites and computer code. Its only task is next-token prediction. It sees some text, predicts the next token, checks the real one, and adjusts itself a tiny bit.

After a huge number of these small adjustments, the model has learned grammar, common facts and styles of writing. It is good at continuing text. But it is not yet a helpful assistant. Ask it a question, and it might just continue with more questions.

Stage two is fine-tuning. The model trains further on a much smaller set of carefully prepared conversations. A request, followed by a helpful, clear and safe answer. From these, it learns how an assistant behaves. Answer the question, follow instructions, use a helpful tone.

Stage three is adjustment from human feedback. People compare different answers from the model and rate which ones are better, more accurate or safer. The ratings are used to adjust the model, so it gives the preferred kind of answer more often. Some providers also use other methods here.

Here is a way to picture it. A trainee chef first reads thousands of recipes. Then the trainee practises under a head chef. Finally, the trainee improves from customer feedback, and makes the popular dishes more often.

This simplified picture has real effects for you. The model learned from text up to a certain date. It learned patterns, not a database of checked facts. Its tone and caution come mostly from stages two and three. And it does not normally learn from your chat in real time.

Let's see this in practice. Aroha is an administrator at a health clinic in Wellington. She asks a chatbot about new clinic opening-hour rules that her regional health office announced last month. The chatbot gives a confident answer, with exact times.

Aroha uses the three stages to think it through. Pre-training: the announcement was local and recent, so it was probably not in the training text. The model knows general patterns about opening hours, so it produced something that sounds likely.

Fine-tuning: the model learned to give helpful, complete answers, so it answered instead of saying I don't know. Human feedback: good training usually rewards honesty about uncertainty, but this does not work every time.

So Aroha concludes that the answer is probably invented. She checks the real announcement on the health office website instead. She also remembers not to paste patient details into the chatbot.

A common mistake is to believe that a chatbot learns from each conversation, and remembers what you taught it yesterday. In most cases, the core model does not change when you chat. Some apps have a memory feature that saves notes about you, and some may use chats to train future models. That is not live learning. Check each tool's settings.

Let's recap. First, in simple terms, a language model is trained in stages. Pre-training on lots of text, fine-tuning on good answers, and adjustment from human feedback. Second, pre-training gives general knowledge and language skills, while the later stages shape tone and behaviour. Third, a model can be out of date, or confidently wrong about rare or recent topics.

Your turn. In the exercise below, ask a free chatbot what it cannot know or do because of how it was trained. Then link each point to one of the three stages. It takes about twenty minutes. Next, we look at context windows, knowledge cut-offs and hallucinations. See you there.
```

## L04 Context Windows, Knowledge Cut-offs and Hallucinations

- **Filename:** `ai-02-generative-ai-explained-llms-diffusion-and-multimodal-models_M1_L04_presenter.mp4`
- **Expected length:** about 4.9 minutes (675 words). The quality gate accepts ±10%.

```text
You paste a long document into a chatbot and ask about page one. The answer is strange, as if it never read it. Later, it tells you about a company rule that does not exist. What went wrong? Three ideas explain most of it.

In the last lesson, you saw how a model is trained. Today we look at what happens when you use it. The first idea is the context window.

A model does not remember a conversation the way a person does. Each time it answers, it looks at one block of text. Your instructions, the conversation so far, and any documents you added. This block is the context window, and it has a maximum size, measured in tokens.

Picture a desk. The model can only work with the papers on the desk. When the desk is full, older papers fall off the edge, and the model cannot see them anymore. Even on a full desk, it is easier to miss details.

The second idea is the knowledge cut-off. A model learns from text collected up to a certain date. It does not know about later events. It may still guess about them from older patterns. It is like a library that stopped buying new books.

Some tools fix part of this by searching the web or reading files, and placing the results in the context window. Then the model answers from the new text. But it can still misread it.

The third idea is hallucination. The model generates likely text, not checked facts. So it can give answers that are fluent and confident, but false. Think of invented quotes, wrong numbers, sources that do not exist, or policy rules that sound real.

Hallucinations are more likely when the answer is not in the context window, when the question assumes something false, or when you ask for exact dates, names or references. It is like a student who writes a confident paragraph, because a blank answer earns no marks.

Let's see all three ideas at work. Kwame is an HR officer at a logistics company in Accra. He gives a chatbot the company's two-page travel policy, with all staff names removed, and asks some questions.

How many days before a trip must staff send a request? The policy says five working days, and the chatbot is correct. What is the daily meal allowance? Also correct, and it quotes the right paragraph.

Then he asks: can staff book business class for flights over six hours? The policy says nothing about this. But the chatbot replies, yes, with manager approval. That is a hallucination. It sounds like a normal rule, but it is not in the text.

So Kwame asks again with a new instruction. Answer only from the policy. If the policy does not say, reply not stated. This time, the chatbot says not stated.

Kwame also notices something else. After a very long conversation, the chatbot forgets an instruction he gave at the start. It has fallen off the desk. So he starts a new chat and repeats the key instruction.

A common mistake is to think hallucinations are a rare bug that will soon disappear. They come directly from how language models work. Better tools reduce them, but a fluent answer is never proof. Give the source, ask for not stated, and check every important fact.

Let's recap. First, the context window is the amount of text a model can consider at one time. Text outside it cannot be used. Second, a knowledge cut-off means the model does not know later events, unless a tool gives it new information. Third, hallucinations are confident but false answers, so check important answers against a source.

Now it is your turn. In the exercise below, you give a free chatbot a two-page sample policy and ask five questions, including one that the policy does not answer. Then you label each answer correct, invented or honestly uncertain. It takes about twenty-five minutes. Next, we move to images, with how diffusion models create images. See you there.
```
