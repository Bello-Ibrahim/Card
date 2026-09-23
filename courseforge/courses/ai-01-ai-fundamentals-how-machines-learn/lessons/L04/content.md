# L04 Training vs. Using a Model

Course: AI-01 · Module: M1 · Objectives: O2 · Video: 5 min

## Hook
When you ask a chatbot a question, is it searching a giant list of stored answers? The real answer explains why AI can be both very helpful and sometimes wrong.

## Explanation
In L03 we met data, features and labels. Now we look at what the system does with them. A machine learning system has two separate phases.

**Phase 1: Training.** The system studies many labelled examples and looks for patterns that connect the features to the labels. It adjusts itself again and again until its guesses on the training examples are mostly correct. The result of training is called a **model**. A model is a stored set of patterns, not a stored copy of the examples.

**Phase 2: Prediction.** The finished model is given a new example it has never seen, and it uses its patterns to produce an answer. This phase is also called **inference**. When you unlock your phone, get a spam warning or receive a song suggestion, you are seeing inference.

Training usually happens once, or from time to time, and can take a lot of data, time and computing power. Inference happens every time someone uses the model, and it is usually fast.

During inference, the model normally does not learn. If the world changes, the model only improves when people collect new data and train it again.

**Analogy:** Think of a student preparing for an exam. For weeks the student studies past questions and their answers. That is training. Then the student sits the exam, without the textbook, and answers new questions using only what they learned. That is inference. A good student learns the ideas behind the answers, not every answer, so they can handle new questions.

## Worked Example
Grace is a farm adviser in Mbarara, Uganda. Her organisation wants a phone app that helps farmers check whether cassava leaves look healthy or diseased.

**Training:** The organisation collects thousands of leaf photos. Plant experts label each one "healthy" or "diseased". A technical team trains a model on powerful computers. This takes time, and it happens before any farmer uses the app.

**Inference:** The finished model is placed inside the app. A farmer takes a photo of a leaf, and within seconds the app says "probably diseased". It has never seen this exact leaf, so it is not searching a list. It compares the features in the new photo with the patterns it learned.

Later, farmers in a hilly region report wrong answers. Their photos are taken in strong morning light, which was rare in the training photos. The model does not fix itself. Grace's team collects new photos from that region, adds them to the data and trains a new version of the model.

Chatbots work the same way. Mateus, a hotel owner in Recife, Brazil, asks a chatbot to write a welcome message for guests. The model was trained earlier on a large amount of text. His request triggers inference: the model produces new text from patterns, one piece at a time, instead of copying a stored message. L09 explains this in more detail.

## Common Mistake
Many people believe that AI "looks up" the answer, like a search engine or a database. It does not. A model produces an answer from learned patterns. This is why it can handle questions it has never seen. It is also why it can give an answer that sounds correct but is wrong: there is no stored "true" answer that it checks against.

A second mistake is thinking that a chatbot learns from you during a conversation. The model itself does not change while you use it. Some products can save notes about your earlier chats, but that is a separate feature, and it differs between products and plans. [VERSION]

## Key Takeaways
1. Training is the phase where a system finds patterns in labelled examples. The result is a model.
2. Inference, also called prediction, is the phase where the model applies those patterns to new examples. The model does not normally learn during inference.
3. Models do not look up stored answers. They produce answers from patterns, which lets them handle new cases but also lets them be confidently wrong.

## Hands-on Exercise
**Task:** Ask a free AI chatbot (ChatGPT or Claude) to explain training vs. inference to a 10-year-old, then mark one thing it got right and one thing it simplified.
**Tools:** ChatGPT or Claude (free tier), in a web browser or phone app. [VERSION]
**Steps:**
1. Open the chatbot and sign in if it asks you to.
2. Type: "Explain the difference between training a machine learning model and using it for inference, for a 10-year-old. Use one everyday example."
3. Read the answer and write down one thing it got right, checked against this lesson. For example, did it say that training comes first and uses many examples?
4. Write down one thing it simplified or left out. For example, did it suggest that the model keeps learning while you use it?
5. In one sentence, write how you would improve the explanation for a 10-year-old.
**What good looks like:** You name one specific correct point and one specific simplification, each linked to an idea from this lesson, such as "it did not mention that the model stops learning after training". Your improved sentence is short and uses simple words.
**Time:** about 15 minutes

## Review Flags
- [VERSION] Common Mistake: "memory" features that save information between chats differ between products and plans. Check against the current free tiers of ChatGPT and Claude.
- [VERSION] Hands-on Exercise: sign-up steps and free tier limits for ChatGPT and Claude may change.
