# L02 Tokens and Next-Token Prediction | Presenter Script

Course: AI-02 · Video: 5 min · Words: 692

## Hook
When you type see you on your phone, the keyboard suggests tomorrow, or soon. A large language model does something very similar, but it can write a full report this way. How does a simple guess about the next word become a whole page?

## Explain
In the last lesson, we placed language models on our map. Now let's look inside. A language model does not read text the way you do. First, it splits the text into small pieces called tokens.

A token can be a short word, like cat. It can be part of a longer word. Unbelievable might become three pieces. It can also be a number or a punctuation mark. Each token is turned into numbers the model can work with.

Different models split text in different ways. So the same sentence can have a different number of tokens in different tools.

Then the model does one job, again and again. It looks at all the tokens so far, and it calculates how likely each possible next token is. After the capital of France is, the token Paris gets a very high score.

The model chooses a token, adds it to the text, and repeats the process with the new, longer text. One token at a time, it builds sentences, paragraphs and pages.

This explains two important facts. The model writes by choosing likely text, not by looking up checked facts. And it looks at the whole conversation each time, not only the last word. That is why it can keep the same topic and style.

So it is like the suggestions on your phone keyboard, but trained on far more text. Now, the model does not always pick the most likely token. A setting called temperature controls how much variety it allows.

At a low temperature, it picks the most likely tokens almost every time. Answers are predictable, which suits summaries or extracting data. At a high temperature, less likely tokens get more chance. Answers are more varied and creative, but they can drift off topic. Think of always tapping the first suggestion, or sometimes the second or third.

## Demonstrate
Let's try it. Tomasz leads a customer support team at an online furniture shop in Kraków. He wants a model to write short replies to customers, so he tests one prompt in Google AI Studio.

He opens Google AI Studio in his browser, signs in with a Google account and starts a new prompt. On the right is the run settings panel, with the temperature control.

He sets the temperature low, near the bottom of the range. Then he pastes his prompt. Write a two-sentence reply to a customer whose sofa delivery is one day late. He runs it three times and copies each answer.

The three replies are almost the same. A polite apology, and a new delivery date. Now he moves the temperature near the top of the range and runs the same prompt three more times.

This time the replies differ more. One offers a discount code. One uses a very informal tone. And one promises a free cushion, which the shop does not offer. Tomasz decides that customer replies need a low temperature. The shop cannot promise things it does not provide.

A common mistake is to think the model knows the full answer first and then types it out. It does not. It predicts each token from what came before. So a small change can send the answer in a new direction. Fluent text is likely text, not checked text.

## Recap
Let's recap. First, a language model splits text into tokens and writes by predicting the next token, again and again. Second, it chooses likely text based on the whole conversation, so fluent answers are not automatically correct. Third, temperature controls variety. Low values are more predictable, and high values are more varied.

## CTA
Now you try. In the exercise below, run one prompt three times at a low temperature and three times at a high temperature in Google AI Studio. Then describe the difference in two sentences. It takes about twenty minutes. Next, we look at how a language model is trained. See you there.

## Thumbnail
Headline: One Token at a Time
Image: Navy background, a sentence built from small teal token blocks with the last block still appearing, headline in teal Inter Bold.

## Production Notes
- [VERSION] Screen demo in Google AI Studio: before recording, check that the free interface still shows a temperature control, its current name, its position in the run settings panel and its range. Confirm the steps (new prompt, settings panel) and that a free Google account is enough.
- Record the demo with a clean, signed-in demo Google account; hide the account name and any personal data.
- The six demo answers will differ from the ones described in content.md. Keep the low-temperature runs similar to each other; if a high-temperature run does not invent an offer such as a free cushion, re-run or adjust the voiceover in scene 14 to describe what actually appears.
- Tomasz and the furniture shop in Kraków are fictional; do not show a real shop name.
