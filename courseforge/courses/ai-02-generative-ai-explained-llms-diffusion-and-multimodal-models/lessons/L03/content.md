# L03 How a Language Model Is Trained

Course: AI-02 · Module: M1 · Objectives: O2 · Video: 5 min

## Hook
A language model can write a polite email, explain a science topic and refuse to help with something harmful. Nobody typed those answers in for it. So where did this behaviour come from? The answer is in how the model was trained.

## Explanation
In AI Fundamentals you learned that a model learns patterns from examples. A large language model learns in the same basic way, but training usually happens in several stages. The description below is a **simplified picture**. Different providers use different methods, and they combine or change these stages in their own ways. [VERIFY]

**Stage 1: Pre-training.** The model is trained on a very large collection of text, such as books, articles, websites and computer code. Its only task is next-token prediction (L02): it sees some text, predicts the next token, checks the real next token and adjusts itself slightly. After an enormous number of these small adjustments, the model has learned grammar, facts that appear often, styles of writing and ways of reasoning that appear in text. At this point it is good at continuing text, but it is not yet a helpful assistant. If you ask it a question, it might continue with more questions instead of answering.

**Stage 2: Fine-tuning.** The model is trained further on a much smaller set of carefully prepared examples of good conversations: a request, followed by a helpful, clear and safe answer. From these examples it learns the **format and behaviour** of an assistant: answer the question, follow instructions, and use a helpful tone.

**Stage 3: Adjustment from human feedback.** People compare different answers from the model and rate which ones are better, more accurate or safer. These ratings are used to adjust the model so it gives the preferred kind of answer more often. Some providers also use written principles or other AI systems to help with this step. [VERIFY]

Training has important consequences for you as a user:

- The model learned from text collected up to a certain date. It does not know about later events unless a tool gives it new information (L04).
- The model learned patterns, not a database of checked facts. It can mix up details, especially about rare topics.
- Its tone, its caution and the things it refuses to do come mostly from stages 2 and 3.
- Training is very expensive, so a model does not normally learn from your conversation in real time.

**Analogy:** Think of a trainee chef. First the trainee reads thousands of recipes and learns how dishes are usually made (pre-training). Then the trainee practises under a head chef, who shows exactly how to prepare dishes for customers (fine-tuning). Finally, the trainee improves from customer feedback: dishes that customers prefer are made more often (human feedback). The trainee has never tasted every possible dish, so some new dishes may still go wrong.

## Worked Example
Aroha is an administrator at a hypothetical health clinic in Wellington, New Zealand. She asks a chatbot: "What were the clinic opening-hour rules that our regional health office announced last month?" The chatbot gives a confident answer with specific times.

Aroha wonders how the model could know this. She uses the three stages to think it through.

- **Pre-training:** The announcement was local, recent and probably not in the training text. The model has patterns about "clinic opening hours" in general, so it produced something that sounds likely.
- **Fine-tuning:** The model learned to give helpful, complete-looking answers, so it answered instead of saying "I don't know".
- **Human feedback:** Good training usually rewards honesty about uncertainty. However, this does not work perfectly every time.

Aroha concludes that the answer is probably invented. She checks the real announcement on the health office website instead. She also remembers not to paste patient details into the chatbot.

## Common Mistake
Many learners believe that a chatbot learns from each conversation and "remembers" what they taught it yesterday. In most cases the core model does not change when you chat with it. Some apps have a memory feature that saves notes about you, and some providers may use conversations to train future models, depending on your settings. But this is not the same as the model learning live during your chat. Check each tool's settings and privacy information. [VERSION]

## Key Takeaways
1. In simplified form, a language model is trained in stages: pre-training on a very large collection of text, fine-tuning on examples of good answers, and adjustment from human feedback.
2. Pre-training gives the model its general knowledge and language skills; fine-tuning and feedback shape its assistant behaviour and tone.
3. Because it learned patterns up to a certain date, a model can be out of date or confidently wrong about rare or recent topics.

## Hands-on Exercise
**Task:** Ask a chatbot what it cannot know or do because of how it was trained, then link each point in its answer to one of the three training stages.
**Tools:** Claude or ChatGPT (free tier) [VERSION]; a notes app.
**Steps:**
1. Open Claude or ChatGPT on a free plan.
2. Ask: "Because of how you were trained, what are the things you cannot know or cannot do well? Give a short list."
3. Copy the list into your notes. Do not share personal or confidential information in the chat.
4. Next to each point, write the stage it links to: pre-training, fine-tuning or human feedback. Some points may link to more than one stage.
5. Add one sentence about any point you think is unclear or not fully honest.
**What good looks like:** A list of 4–6 limits, each linked to a stage with a short reason, for example: "Does not know recent events: pre-training data stops at a certain date." One sentence of critical comment is included.
**Time:** about 20 minutes

## Review Flags
- [VERIFY] The three-stage training description (pre-training, fine-tuning, human feedback) is simplified. Confirm the wording is accurate enough for beginners and not tied to one provider, including the note that some providers use written principles or other AI systems in the feedback stage.
- [VERSION] Free tiers of Claude and ChatGPT, and their memory and data-use settings for training, change over time and must be checked before recording.
