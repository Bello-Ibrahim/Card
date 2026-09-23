# L03 How a Language Model Is Trained | Presenter Script

Course: AI-02 · Video: 5 min · Words: 689

## Hook
A language model can write a polite email, explain a science topic, and refuse to help with something harmful. Nobody typed those answers in for it. So where does this behaviour come from? The answer is in how the model was trained.

## Explain
In the last lesson, you saw that a model writes by predicting the next token. Today we ask how it learns to do that well. Training usually happens in stages. What you will see is a simplified picture. Providers use different methods, and they combine these stages in their own ways.

Stage one is pre-training. The model sees a very large collection of text, such as books, articles, websites and computer code. Its only task is next-token prediction. It sees some text, predicts the next token, checks the real one, and adjusts itself a tiny bit.

After a huge number of these small adjustments, the model has learned grammar, common facts and styles of writing. It is good at continuing text. But it is not yet a helpful assistant. Ask it a question, and it might just continue with more questions.

Stage two is fine-tuning. The model trains further on a much smaller set of carefully prepared conversations. A request, followed by a helpful, clear and safe answer. From these, it learns how an assistant behaves. Answer the question, follow instructions, use a helpful tone.

Stage three is adjustment from human feedback. People compare different answers from the model and rate which ones are better, more accurate or safer. The ratings are used to adjust the model, so it gives the preferred kind of answer more often. Some providers also use other methods here.

Here is a way to picture it. A trainee chef first reads thousands of recipes. Then the trainee practises under a head chef. Finally, the trainee improves from customer feedback, and makes the popular dishes more often.

This simplified picture has real effects for you. The model learned from text up to a certain date. It learned patterns, not a database of checked facts. Its tone and caution come mostly from stages two and three. And it does not normally learn from your chat in real time.

## Demonstrate
Let's see this in practice. Aroha is an administrator at a health clinic in Wellington. She asks a chatbot about new clinic opening-hour rules that her regional health office announced last month. The chatbot gives a confident answer, with exact times.

Aroha uses the three stages to think it through. Pre-training: the announcement was local and recent, so it was probably not in the training text. The model knows general patterns about opening hours, so it produced something that sounds likely.

Fine-tuning: the model learned to give helpful, complete answers, so it answered instead of saying I don't know. Human feedback: good training usually rewards honesty about uncertainty, but this does not work every time.

So Aroha concludes that the answer is probably invented. She checks the real announcement on the health office website instead. She also remembers not to paste patient details into the chatbot.

A common mistake is to believe that a chatbot learns from each conversation, and remembers what you taught it yesterday. In most cases, the core model does not change when you chat. Some apps have a memory feature that saves notes about you, and some may use chats to train future models. That is not live learning. Check each tool's settings.

## Recap
Let's recap. First, in simple terms, a language model is trained in stages. Pre-training on lots of text, fine-tuning on good answers, and adjustment from human feedback. Second, pre-training gives general knowledge and language skills, while the later stages shape tone and behaviour. Third, a model can be out of date, or confidently wrong about rare or recent topics.

## CTA
Your turn. In the exercise below, ask a free chatbot what it cannot know or do because of how it was trained. Then link each point to one of the three stages. It takes about twenty minutes. Next, we look at context windows, knowledge cut-offs and hallucinations. See you there.

## Thumbnail
Headline: Read, Practise, Improve
Image: Navy background, three teal steps rising left to right with a book, a chef's hat and a star rating icon, headline in teal Inter Bold.

## Production Notes
- [VERIFY] The three-stage training description (pre-training, fine-tuning, adjustment from human feedback) is a simplification. The voiceover says so twice (scenes 2 and 8). A reviewer must confirm the wording is accurate enough for beginners and not tied to one provider.
- [VERIFY] content.md adds that some providers use written principles or other AI systems in the feedback stage. The voiceover only says 'some providers also use other methods here'; keep that wording unless the reviewer approves more detail.
- [VERSION] Free tiers of Claude and ChatGPT, and their memory and data-use settings for training, change over time. The voiceover avoids specifics and tells learners to check each tool's settings. Check before recording.
- No provider or model names in the voiceover. Aroha and the Wellington clinic are fictional; stock footage must not show real patient data or a real clinic name.
