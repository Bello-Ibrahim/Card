# L04 Hallucinations, Misinformation and Deepfakes

Course: AI-29 · Module: M1 · Objectives: O1, O3 · Video: 5 min

## Hook
You ask a chatbot for three research articles on your topic. It gives you three titles, three author names and three publication years, all in perfect format. You search for them. None of them exists.

## Explanation
To understand why this happens, you need to know one thing about how chatbots work. A chatbot, such as Claude or ChatGPT, is built on a large language model. It writes by **predicting the next likely words**, based on patterns in the huge amount of text it learned from. It does not look up facts in a database unless it is connected to a search tool, and even then it can make mistakes.

This means a chatbot can produce text that *sounds* right but *is* wrong. This is called a **hallucination**. Hallucinations are especially common with:
- exact numbers, dates and quotes;
- sources, such as articles, books, court cases or web links;
- local or specialist topics that had little text in the training data;
- very recent events.

A hallucination is dangerous because it is written with the same confidence as a correct answer. The chatbot does not usually say "I am guessing".

**Misinformation** is false or misleading information that spreads. AI can add to misinformation in two ways. First, people copy hallucinated answers into reports, posts or emails without checking. Second, AI can quickly produce large amounts of convincing false content.

**Deepfakes** are AI-generated or AI-edited images, voices or videos that show people saying or doing things they never did. A deepfake voice message from a "manager" could ask a staff member to make an urgent payment. A deepfake video could show a public figure making a false statement. Deepfakes make false stories look and sound real.

Three simple habits reduce the risk:
1. **Check claims against a trusted source**, such as an official website, a reputable publisher or an expert you know.
2. **Ask for sources, then open them.** Do not trust a link or a title until you have seen the real page.
3. **Slow down when content makes you feel a strong emotion**, such as anger, fear or excitement. False content often tries to make you share or act fast.

**Analogy:** A chatbot is like a very confident friend who has read a lot but never checks notes. Most of the time their answers are helpful. Sometimes they fill a gap in their memory with something that sounds right, and they say it in exactly the same calm voice. You enjoy the conversation, but you check before you repeat it.

## Worked Example
Aigerim Bekova writes a newsletter for a hypothetical farming cooperative in Kazakhstan. She asks a chatbot: "What is the average wheat yield per hectare in our region, and which study shows this?"

The chatbot gives a precise number and names a study, with an author, a year and a journal. Aigerim follows the three habits:
1. She checks the number on her country's official agriculture statistics website. The official figure is different.
2. She searches for the study. She cannot find it in the journal, and the author does not appear to have written it. The source was invented.
3. She notes that the answer was very specific and very confident, which made it feel reliable.

Aigerim uses the official figure, links to the official source and adds a line to her team's guidance: "Never publish a number or a source from a chatbot until you have opened the original."

The same week, a cooperative member forwards a voice message that claims to be from the director, asking for a quick payment to a new supplier. Aigerim remembers the risk of deepfakes. She calls the director on a known number. The director did not send the message.

## Common Mistake
Many people think that if a chatbot gives a source, the answer must be correct. But a chatbot can invent sources that look real, and it can also give a real source that does not say what the chatbot claims. The correction: a source only counts after you have opened it and found the claim in it yourself. A second common mistake is to think that deepfakes are always easy to spot. Some are, but many are not, so check the context and confirm through a different channel.

## Key Takeaways
1. Chatbots predict likely text, so they can produce confident answers that are false, including invented sources. This is a hallucination.
2. Deepfakes are AI-made images, voices or videos that can make false stories look real and add to misinformation.
3. Check claims against a trusted source, open every source yourself, and slow down when content makes you feel a strong emotion.

## Hands-on Exercise
**Task:** Ask Claude or ChatGPT 3 factual questions about your own country or industry, check every answer against a trusted source, and record each error you find.
**Tools:** Claude or ChatGPT (free versions) [VERSION]; a web browser for trusted sources; a notes app or paper.
**Steps:**
1. Write 3 factual questions you can check, for example about a national holiday, a public organisation in your industry, or an official figure. Include at least one question that asks for a source. Do not include any personal or confidential information.
2. Ask the chatbot each question and copy its answer into your notes.
3. For each answer, find a trusted source, such as an official website or a reputable publisher, and compare.
4. Open every source or link the chatbot gave you. Check that it exists and that it really says what the chatbot claims.
5. Record in a table: question, chatbot answer, trusted source, correct / partly correct / wrong, and any invented source.
**What good looks like:** A table of 3 questions with a trusted source for each, an honest result for every answer, and a note on any invented or wrong sources. If you find no errors, you explain how you checked, and you note that a few correct answers do not prove the tool is always reliable.
**Time:** about 20 minutes

## Review Flags
- [VERSION] Free access to Claude and ChatGPT, and whether the free versions can search the web, differ by plan and change often. Check the live tools before scripting.
