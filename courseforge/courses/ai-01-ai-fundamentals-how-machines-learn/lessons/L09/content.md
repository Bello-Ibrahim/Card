# L09 Generative AI and Chatbots

Course: AI-01 · Module: M3 · Objectives: O1, O6 · Video: 5 min

## Hook
A chatbot writes a birthday poem in seconds. Ask it for the source of a quotation, and it may give a book title that does not exist, in the same confident voice. How can one system be so helpful and so wrong at the same time? The answer is in how it learned.

## Explanation
In L01 you saw generative AI as the smallest circle. It means systems that create new content, such as text, images or sound, instead of only choosing a label like "spam".

A chatbot is built on a **language model**. During training, the model reads a very large amount of text. Its job is simple: look at the words so far and predict the **next word**. After "The sun rises in the", "east" is very likely. Each time it guesses badly, its dials (the weights from L07) are nudged a little. This repeats over a huge amount of text.

When you use the chatbot, the model predicts a likely next word, adds it to the answer, then predicts the next one, until the answer is complete. As you learned in L04, it does not "look up" answers. It uses learned patterns.

This one idea explains two things:

- **Fluency.** The model has seen so much text that its predictions follow the patterns of good writing, so the answer sounds natural.
- **Hallucination.** A hallucination is an answer that sounds correct but is false or invented. The model is trained to produce text that is *likely*, not text that is *true*. If a false sentence looks like the kind of sentence that usually appears there, the model can produce it. It has no built-in sense of "I do not know".

**Analogy:** Imagine a person who has listened to many university lectures but never checked any facts. Ask them a question, and they answer like a professor: the right words and the right confidence. Sometimes the answer is correct, because they remember the pattern well. Sometimes they fill a gap with something that only *sounds* right. From their voice alone, you cannot tell which is which.

Image generators work in a similar way. They learn patterns from many images and their descriptions, then build a new image that fits your words. They do not copy one stored picture, and they also make errors, such as a hand with the wrong number of fingers.

## Worked Example
Rafael is a secondary-school history teacher in Porto, Portugal. He uses a chatbot to prepare a lesson about ocean trade routes.

First he asks it to "write a short, simple introduction to trade routes for 13-year-olds." The result is clear and well organised. This task needs fluent, general writing, and Rafael can check it by reading.

Next he asks for "three books about Portuguese sea trade, with authors and page numbers for key quotations." The chatbot gives three titles, three authors and exact page numbers. Rafael checks his school library catalogue and an online bookshop. One book is real. One real author is listed with a book title that does not exist. The third book cannot be found anywhere.

A list of books with authors and page numbers is a common *shape* of text, so the model produced that shape without checking that each item was real. He keeps the introduction, removes the reading list, and builds his own list from the library catalogue.

## Common Mistake
Many learners think a chatbot is a smarter search engine. It generates text from learned patterns. Some chatbots can also search the web or read your files, but the final answer is still generated, so it can still contain mistakes. A confident tone is not evidence. Treat any fact, number, name or source from a chatbot as a claim to check, not as a finished answer.

## Key Takeaways
1. A language model is trained to predict the next word, and a chatbot builds its answer one predicted word at a time.
2. This explains both fluency and hallucination: the model produces text that is likely, which is not always text that is true.
3. Use chatbots for drafting and explaining, and always verify facts, names, numbers and sources against a reliable source.

## Hands-on Exercise
**Task:** Ask a chatbot 3 factual questions you can check, verify each answer, and record any errors.
**Tools:** ChatGPT or Claude (free tier); a reliable source to check against, such as an encyclopedia, an official website or a textbook; pen and paper or a notes app.
**Steps:**
1. Choose 3 questions whose answers you can check. Include one easy question (for example, the capital of a country), one detailed question (for example, the population of your own town), and one question that asks for a source (for example, "Name a book about the history of my city, with its author").
2. Ask the chatbot each question in a new, separate message.
3. Copy each answer into a table with three columns: "Question", "Chatbot answer", "What I found".
4. Check each answer in a reliable source. Write "correct", "partly correct" or "wrong".
5. For any error, write one sentence about why the next-word idea could explain it.
**What good looks like:** A completed table with 3 rows, a named source for each check, and at least one sentence connecting an error (or a near-error) to next-word prediction. If all answers were correct, you note which question was most at risk and why.
**Time:** about 20 minutes

## Review Flags
- None. The example is hypothetical, no model names or figures are used, and the explanation of next-word prediction is intentionally simplified for beginners.
