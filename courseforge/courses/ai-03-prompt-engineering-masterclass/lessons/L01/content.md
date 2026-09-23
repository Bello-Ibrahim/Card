# L01 How AI Chat Tools Respond to You

Course: AI-03 · Module: M1 · Objectives: O2 · Video: 5 min

## Hook
You type "write an email to a client" into an AI chat tool. In a few seconds you get a polite, well-written email. But it could be sent by anyone, to anyone, about anything. Why did a clever tool give you such a general answer?

## Explanation
An AI chat tool, such as Claude, ChatGPT or Gemini, is a program that reads the text you type and writes a reply. You do not need any technical knowledge to use one. You type a request in normal language, which is called a **prompt**, and the tool responds.

The tool learned from a very large amount of text during its training. When you send a prompt, it predicts a likely, useful answer, word by word, based on your words and on the patterns it learned. It does not look into your inbox, your files or your company systems unless you give it that material. It also does not know your client, your team or your goal.

This explains two things that surprise many new users.

First, a **vague prompt gives a generic answer**. If your prompt only says "email to a client", the most likely answer is an average email that fits many situations. The tool fills the gaps with safe, common choices, because you did not give it anything more specific.

Second, **the same prompt can give different answers**. If you ask the same question twice, or in two different tools, the wording and sometimes the content can change. The tool is predicting, not looking up one fixed answer. Clear context and clear instructions reduce this variation, because they leave fewer gaps for the tool to fill.

The good news is that you control the most important input: your prompt. The more the tool knows about who, what and why, the more useful its answer often becomes.

**Analogy:** Imagine a capable new colleague on their first day. They have read a lot and can write well, but they know nothing about your team, your client or your goal. If you say "write to the client", they will produce something polite and general. If you say "write to Mr Diallo, whose delivery was three days late, apologise, and offer a new date of Friday", they can do excellent work. The AI tool is that new colleague, every time you start a new chat.

## Worked Example
Mariana is an account manager at a hypothetical engineering firm in São Paulo. A client's inspection visit has to move because a key engineer is ill.

Her first prompt:

```text
Write an email to a client.
```

The tool returns a friendly email that thanks the client "for their continued partnership" and offers "to discuss any questions". Nothing in it is wrong, but Mariana cannot send it. It does not mention the visit, the new date or the reason.

Her second prompt:

```text
Write a short email to [CLIENT CONTACT], facilities manager at a
food-processing company. Our site inspection planned for Tuesday must
move because our lead engineer is ill. Offer Thursday or Friday
morning instead. Apologise once, keep a professional and warm tone,
and ask them to confirm by Monday.
```

This time the email names the visit, gives the reason in one sentence, offers the two dates and asks for a reply by Monday. Mariana changes one phrase and sends it.

Notice two things. She did not use any special words or tricks. She simply gave the information a new colleague would need. She also used a placeholder, [CLIENT CONTACT], instead of the client's real name. You will learn more about this in L03.

## Common Mistake
Many people think a generic answer means the tool is "not very smart", so they give up or keep pressing "regenerate" and hope for a better result. Usually the problem is missing information, not a weak tool. Before you judge the output, ask yourself: "Did I tell it who, what and why?" Adding two or three lines of context often helps more than asking again with the same words.

## Key Takeaways
1. An AI chat tool predicts a likely answer from your prompt and its training. It does not know your situation unless you tell it.
2. Vague prompts get generic answers, and the same prompt can give different answers each time.
3. Clear context and instructions leave fewer gaps for the tool to fill, so the output is often more useful and more consistent.

## Hands-on Exercise
**Task:** Compare a vague prompt with a detailed prompt for the same client email.
**Tools:** Claude (free tier). ChatGPT or Gemini (free tiers) also work. [VERSION]
**Steps:**
1. Open a new chat and type: "Write an email to a client." Copy the answer into a notes app.
2. Think of a realistic, non-confidential client situation, for example a delay, a price change or a meeting request. Use placeholders such as [CLIENT] instead of real names.
3. Open a new chat and write a second prompt that says who the client is, what happened and what you want the client to do.
4. Copy the second answer next to the first one.
5. Write three bullet points that compare the two answers: what is more specific, what is still missing, and which one you could send with the fewest changes.
**What good looks like:** Three clear bullet points that name concrete differences, for example "the second email gives the new date and asks for a reply by Monday; the first one has no date". No real client names or confidential details appear in either prompt.
**Time:** about 15 minutes

## Review Flags
- [VERSION] Availability of Claude, ChatGPT and Gemini free tiers, and whether a free account is needed, must be checked before scripting.
- Judgement call from the curriculum: the prerequisite is only basic computer literacy, so this lesson briefly explains what an AI chat tool does before any prompting technique.
