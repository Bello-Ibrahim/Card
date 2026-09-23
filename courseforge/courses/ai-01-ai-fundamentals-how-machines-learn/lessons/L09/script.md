# L09 Generative AI and Chatbots | Presenter Script

Course: AI-01 · Video: 5 min · Words: 701

## Hook
A chatbot writes a birthday poem in seconds. Ask it for the source of a quotation, and it may give a book that does not exist, in the same confident voice. How can one system be so helpful, and so wrong?

## Explain
Welcome to the final week. In the first lesson, you saw generative AI as the smallest circle. It means systems that create new content, such as text, images or sound, instead of only choosing a label, like spam.

A chatbot is built on a language model. During training, the model reads a very large amount of text. Its job is simple. Look at the words so far, and predict the next word. After the sun rises in the, the word east is very likely.

Each time it guesses badly, its dials, the weights from lesson seven, are nudged a little. This repeats over a huge amount of text. Then, when you use the chatbot, it predicts a likely next word, adds it to the answer, and predicts the next one, until the answer is complete.

This one idea explains two things. First, fluency. The model has seen so much text that its answers follow the patterns of good writing, so they sound natural. Second, hallucination. That is an answer that sounds correct, but is false or invented.

Why does it happen? The model is trained to produce text that is likely, not text that is true. And it has no built-in sense of I do not know.

Imagine a person who has listened to many university lectures, but never checked any facts. Ask them a question, and they answer like a professor, with the right words and the right confidence. Sometimes they are right. Sometimes they fill a gap with something that only sounds right. From their voice alone, you cannot tell which.

Image generators work in a similar way. They learn patterns from many images and their descriptions, then build a new image that fits your words. They do not copy one stored picture. And they also make errors, like a hand with the wrong number of fingers.

## Demonstrate
Let's see both results in one task. Rafael is a secondary school history teacher in Porto, Portugal. He uses a chatbot to prepare a lesson about ocean trade routes.

First, he asks it to write a short, simple introduction to trade routes for thirteen year olds. The result is clear and well organised. This task needs fluent, general writing, and Rafael can check it just by reading.

Next, he asks for three books about Portuguese sea trade, with authors and page numbers for key quotations. The chatbot gives three titles, three authors and exact page numbers. It looks perfect.

Rafael checks his school library catalogue and an online bookshop. One book is real. One real author is listed with a book title that does not exist. And the third book cannot be found anywhere.

Why? A list of books with authors and page numbers is a common shape of text. The model produced that shape, without checking that each item was real. So Rafael keeps the introduction, removes the reading list, and builds his own list from the library catalogue.

A common mistake is to think that a chatbot is a smarter search engine. It generates text from patterns. Some chatbots can also search the web, but the final answer is still generated. A confident tone is not evidence. Treat any fact, number, name or source as a claim to check.

## Recap
Let's recap. First, a language model is trained to predict the next word, and a chatbot builds its answer one predicted word at a time. Second, this explains both fluency and hallucination. The model produces text that is likely, which is not always true. Third, use chatbots for drafting and explaining, and always check facts, names, numbers and sources.

## CTA
Now it is your turn. In the exercise below this video, ask ChatGPT or Claude three factual questions that you can check. Verify each answer in a reliable source, and record any errors. In the next lesson, we look at where AI goes wrong for whole groups of people, in Bias, Data and the Limits of AI. See you there.

## Thumbnail
Headline: Likely Is Not True
Image: Navy background, a chat bubble with a glowing next-word suggestion and a small teal question mark over a book icon, headline in teal Inter Bold.

## Production Notes
- No facts to verify: Rafael's case is hypothetical and no model names or figures are used (content.md Review Flags: None). The next-word explanation is intentionally simplified for beginners.
- Scenes 10 and 11: the chatbot answers are mock-ups on slides. Use invented book titles and author names that are clearly fictional; do not show a real author with a fake title.
- Show a generic chat interface, not the branded interface of any real chatbot.
- Rafael and his school in Porto are fictional; stock footage must not show a real school name or logo.
