# L04 Training vs. Using a Model | Presenter Script

Course: AI-01 · Video: 5 min · Words: 692

## Hook
When you ask a chatbot a question, is it searching a giant list of stored answers? The real answer explains why AI can be both very helpful, and sometimes wrong.

## Explain
In the last lesson, we met data, features and labels. Now we look at what the system does with them. A machine learning system has two separate phases.

Phase one is training. The system studies many labelled examples and looks for patterns that connect the features to the labels. It adjusts itself again and again, until its guesses on the training examples are mostly correct. The result of training is called a model.

This is important. A model is a stored set of patterns. It is not a stored copy of the examples.

Phase two is prediction. The finished model is given a new example it has never seen, and it uses its patterns to produce an answer. This phase is also called inference. When you unlock your phone, or get a song suggestion, you are seeing inference.

Training usually happens once, or from time to time, and it can take a lot of data, time and computing power. Inference happens every time someone uses the model, and it is usually fast. And during inference, the model normally does not learn. If the world changes, the model only improves when people collect new data and train it again.

Think of a student preparing for an exam. For weeks, the student studies past questions and their answers. That is training.

Then the student sits the exam, without the textbook, and answers new questions using only what they learned. That is inference. A good student learns the ideas behind the answers, not every answer, so they can handle new questions.

## Demonstrate
Let's see both phases in a real situation. Grace is a farm adviser in Mbarara, Uganda. Her organisation wants a phone app that helps farmers check whether cassava leaves look healthy or diseased.

First, training. The organisation collects thousands of leaf photos. Plant experts label each one healthy or diseased. A technical team trains a model on powerful computers. This takes time, and it happens before any farmer uses the app.

Then, inference. The model is placed inside the app. A farmer takes a photo of a leaf, and within seconds the app says, probably diseased. It has never seen this exact leaf, so it is not searching a list. It compares the features in the new photo with the patterns it learned.

Later, farmers in a hilly region report wrong answers. Their photos are taken in strong morning light, which was rare in the training photos. The model does not fix itself. Grace's team collects new photos from that region, and trains a new version.

Chatbots work the same way. Mateus, a hotel owner in Recife, Brazil, asks a chatbot to write a welcome message for guests. The model was trained earlier on a large amount of text. His request triggers inference. The model produces new text from patterns, one piece at a time. It does not copy a stored message.

This clears up a common mistake. AI does not look up the answer, like a search engine. That is why it can handle questions it has never seen. It is also why it can sound correct but be wrong. There is no stored true answer to check against.

## Recap
Let's recap. First, training is the phase where a system finds patterns in labelled examples, and the result is a model. Second, inference is the phase where the model applies those patterns to new examples, and it normally does not learn while doing this. Third, models do not look up stored answers. They produce answers from patterns, so they can handle new cases, but they can also be confidently wrong.

## CTA
Now it is your turn. In the exercise below this video, ask a free chatbot, ChatGPT or Claude, to explain training and inference to a ten year old. Then write down one thing it got right, and one thing it simplified. It takes about fifteen minutes. In the next lesson, we start a new module with Supervised Learning: Classification and Regression. See you there.

## Thumbnail
Headline: Study First, Then Exam
Image: Navy background, split card: an open notebook with study notes on the left and an exam paper with a pen on the right, headline in teal Inter Bold.

## Production Notes
- [VERSION] The script says the model itself does not change while you chat. It does not mention memory features that save notes between chats; content.md flags these as differing between products and plans. Keep it that way unless the check against current free tiers of ChatGPT and Claude says otherwise.
- [VERSION] Exercise: sign-up steps and free-tier limits for ChatGPT and Claude may change. The CTA names the tools but no plan details.
- Grace in Mbarara and Mateus in Recife are fictional. Stock of cassava leaves and farmers must not show real organisation logos or app names.
- The leaf-check app on the scene 11 slide is a generic mock-up, not a real product.
