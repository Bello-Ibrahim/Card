# L08 Testing a Model: Accuracy and Overfitting

Course: AI-01 · Module: M2 · Objectives: O6 · Video: 5 min

## Hook
A company tells you its new AI tool is "99% accurate". That sounds excellent. But accurate on what? And compared with what? By the end of this lesson, you will know the two questions to ask before you trust a number like that.

## Explanation
In L04 you learned that a model is first trained and then used to make predictions. Between those two stages there is an important step: **testing**.

To test a model fairly, we keep some examples aside before training starts. The model never sees them while it learns. This group is called the **test set**. The examples used for learning are the **training set**. After training, we ask the model to predict the test examples and compare its answers with the real labels.

Why not test on the training examples? Because the model has already seen them. A good score on familiar examples tells you very little about how the model will do on new cases, and new cases are the reason we built it.

**Accuracy** is the simplest result of a test. It is the share of test examples the model got right. If a model labels 90 out of 100 test photos correctly, its accuracy is 90%.

Accuracy is useful, but it can hide problems:
- **It hides which mistakes the model makes.** Suppose only 5 out of every 100 bank transactions are fraud. A model that always says "not fraud" is right 95 times out of 100, so its accuracy is 95%. Yet it never catches a single fraud, which was the whole purpose.
- **It depends on the test set.** If the test examples are easier, or different from real life, the accuracy will look better than the model really is.

This leads to the most common problem in machine learning: **overfitting**. A model overfits when it learns its training examples too closely, including small details and accidents that do not matter, instead of the general pattern. It scores very well on training examples and much worse on new ones.

**Analogy:** Think of two students preparing for an exam. The first student memorises the answers to the practice exam, word for word. On the practice exam, they score almost 100%. On the real exam, with new questions, they struggle, because they never understood the topic. The second student studies the ideas behind the questions. Their practice score is a little lower, but they do well on the real exam too. The first student has overfitted. The real exam is the test set.

The clearest warning sign of overfitting is a large gap between the training score and the test score.

## Worked Example
Nusrat is a quality manager at a garment factory in Dhaka, Bangladesh. Her team wants a camera system to spot faulty shirts on the production line. They collect photos of shirts, and experienced inspectors label each photo "faulty" or "fine".

Before training, Nusrat's team puts one fifth of the photos aside as a test set. They train the model on the rest.

The first model scores 99% on the training photos but only 70% on the test photos. The big gap tells Nusrat the model has overfitted. When the team looks more closely, they find that most "faulty" training photos were taken on one table with a blue cloth. The model had partly learned "blue cloth means faulty", which is an accident in the data, not a real sign of a fault.

The team takes new photos on several tables and trains again. The second model scores 91% on training photos and 89% on test photos. The scores are closer, so it is more likely to work on new shirts.

Nusrat asks one more question: how many of the truly faulty shirts in the test set did the model catch? Faulty shirts are rare, so a high accuracy alone could hide a model that misses most of them. She checks the faulty shirts separately before approving the system.

## Common Mistake
Many people think the model with the highest score is always the best model. A very high score can be a warning sign, especially if it comes from training examples, from a small test set, or from a task where one answer is much more common than the others. Always ask two questions: "Was it tested on examples it never saw?" and "Which mistakes does it make?"

## Key Takeaways
1. A model must be tested on examples it never saw during training, called the test set, to show how it will perform on new cases.
2. Accuracy is the share of test examples the model got right, but it can hide which mistakes the model makes, especially when one answer is rare.
3. Overfitting means the model memorised its training examples instead of learning the general pattern, and a large gap between training and test scores is the main warning sign.

## Hands-on Exercise
**Task:** Read two short model "report cards" and decide which model you would trust, and why.
**Tools:** Pen and paper, or any notes app. Optional: ChatGPT or Claude (free tier) to discuss your reasoning.
**Steps:**
1. Read the situation. A clinic wants a model that reads short patient messages and labels them "urgent" or "not urgent", so staff can reply to urgent messages first. At this clinic, about 1 message in 10 is urgent. Two companies offer a model. Both report cards are hypothetical.
2. Read Report Card A:
   - Training set: 2,000 messages. Accuracy on training messages: 99%.
   - Test set: 100 messages, taken from the same 2,000 training messages.
   - Accuracy on test messages: 98%.
   - Urgent messages caught: not reported.
3. Read Report Card B:
   - Training set: 2,000 messages. Accuracy on training messages: 90%.
   - Test set: 500 new messages from a different month, never used in training.
   - Accuracy on test messages: 87%.
   - Urgent messages caught: 46 of the 50 urgent messages in the test set.
4. For each report card, write down: Was the model tested on examples it never saw? Is there a large gap between training and test scores? Do we know which mistakes it makes?
5. Decide which model you would trust more, and write two or three sentences explaining why.
**What good looks like:** You choose Model B. Your reasons mention that Model A was tested on messages it had already seen, so its 98% says little about new messages, and that it does not report how many urgent messages it catches. You note that Model B's training and test scores are close, its test messages are new, and it reports that it caught most urgent messages. A strong answer also asks about the 4 urgent messages Model B missed.
**Time:** about 15 minutes

## Review Flags
- None. The factory, clinic and report cards are hypothetical, and all numbers are invented for teaching, not real statistics.
