# L02 Tokens and Next-Token Prediction

Course: AI-02 · Module: M1 · Objectives: O2 · Video: 5 min (screen demo)

## Hook
When you type "See you" on your phone, the keyboard suggests "tomorrow" or "soon". A large language model does something very similar, but it can write a full report this way. How does a simple guess about the next word become a whole page of text?

## Explanation
A large language model (LLM) does not read text the way you do. First it splits the text into small pieces called **tokens**. A token can be a whole short word ("cat"), part of a longer word ("un" + "believ" + "able"), a number or a punctuation mark. Each token is turned into numbers the model can work with. Different models split text in different ways, so the same sentence can have a different number of tokens in different tools.

The model then does one job again and again: **next-token prediction**. It looks at all the tokens so far and calculates how likely each possible next token is. For example, after "The capital of France is", the token "Paris" gets a very high score. The model chooses a token, adds it to the text, and then repeats the process with the new, longer text. One token at a time, it builds sentences, paragraphs and pages.

This explains two important facts. First, the model writes by choosing **likely** text, not by looking up checked facts. Second, the model considers the **whole conversation** each time, not only the last word. This is why it can keep a consistent topic and style.

The model does not always choose the single most likely token. A setting called **temperature** controls how much variety it allows.

- A **low temperature** makes the model choose the most likely tokens almost every time. Answers are more predictable and repeat more closely when you run the same prompt again. This suits tasks such as extracting data or summarising.
- A **high temperature** gives less likely tokens more chance. Answers are more varied and sometimes more creative, but also more likely to drift off topic. This can suit brainstorming or story ideas.

Many chat apps do not show a temperature control, and the provider chooses a value for you. Developer tools such as Google AI Studio often show it. [VERSION]

**Analogy:** Next-token prediction is like the word suggestions on your phone keyboard, but trained on far more text and able to consider the whole conversation, not only the last few words. Temperature is like deciding whether to always tap the first suggestion (low temperature) or sometimes tap the second or third one (high temperature).

## Worked Example
Tomasz leads a hypothetical customer support team at an online furniture shop in Kraków, Poland. He wants a model to write short replies to customers. He tests the same prompt in Google AI Studio: "Write a two-sentence reply to a customer whose sofa delivery is one day late."

A presenter can follow these steps on screen. [VERSION]

1. Open Google AI Studio in a browser and sign in with a Google account.
2. Start a new chat or prompt.
3. Find the run settings panel and the **Temperature** control.
4. Set the temperature to a low value, near the bottom of the range.
5. Paste the prompt and run it. Copy the answer into a notes file.
6. Run the same prompt two more times and copy both answers.
7. Set the temperature to a high value, near the top of the range, and run the prompt three more times, copying each answer.

At low temperature, Tomasz sees three replies that are almost the same: a polite apology and a new delivery date. At high temperature, the replies differ more. One offers a discount code, one uses a very informal tone, and one mentions a "free cushion" that the shop does not offer. Tomasz decides that customer replies need a low temperature, because the shop cannot promise things it does not provide.

## Common Mistake
Many learners think the model "knows the answer" and then types it out. In fact, the model does not plan the full answer first and then write it. It predicts each token based on what came before. This is why a small change in the prompt, or a higher temperature, can send the answer in a different direction. It is also why a model can sound confident while being wrong: fluent text is likely text, not checked text.

## Key Takeaways
1. A language model splits text into tokens and generates an answer by predicting the next token again and again.
2. The model chooses likely text based on the whole conversation, so fluent answers are not automatically correct.
3. Temperature controls variety: low values give more predictable answers, high values give more varied ones.

## Hands-on Exercise
**Task:** Run the same prompt three times at a low temperature and three times at a high temperature in Google AI Studio, and describe the difference in two sentences.
**Tools:** Google AI Studio (free, needs a Google account) [VERSION]; a notes app.
**Steps:**
1. Open Google AI Studio and start a new prompt. Check that the temperature control is visible in the settings panel. [VERSION]
2. Write a short prompt, for example "Suggest a name and a one-line slogan for a new café that sells tea and books." Do not include personal or confidential information.
3. Set a low temperature. Run the prompt three times and save each answer.
4. Set a high temperature. Run the prompt three times and save each answer.
5. Compare the two groups and write two sentences about the difference.
**What good looks like:** Six saved answers labelled "low" or "high", and two clear sentences, for example: "At low temperature the three names were almost the same. At high temperature the names were more varied, and one slogan did not match the café idea."
**Time:** about 20 minutes

## Review Flags
- [VERSION] Check that Google AI Studio still shows a temperature control in the free interface, its current name, its position in the run settings panel and its range. Confirm the screen-demo steps (new prompt, settings panel) against the live tool, and that a free Google account is enough.
