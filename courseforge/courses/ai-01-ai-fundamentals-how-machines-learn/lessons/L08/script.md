# L08 Testing a Model: Accuracy and Overfitting | Presenter Script

Course: AI-01 · Video: 5 min · Words: 714

## Hook
A company tells you its new AI tool is ninety nine percent accurate. That sounds excellent. But accurate on what? And compared with what? By the end of this lesson, you will know two questions to ask before you trust a number like that.

## Explain
You know that a model is first trained, and then used. Between those two stages comes testing. It is how we find out whether a model is ready for the real world.

To test fairly, we keep some examples aside before training. The model never sees them while it learns. This group is the test set. The examples used for learning are the training set. We never test on training examples, because the model has already seen them.

Accuracy is the simplest test result. It is the share of test examples the model got right. If it labels ninety out of a hundred test photos correctly, its accuracy is ninety percent.

But accuracy can hide problems. Suppose only five in every hundred bank transactions are fraud. A model that always says not fraud is right ninety five times out of a hundred. Yet it never catches a single fraud. And if the test examples are easier than real life, the model will look better than it is.

A very common problem is overfitting. A model overfits when it learns its training examples too closely, including accidents that do not matter, instead of the general pattern. It scores very well on training examples, and much worse on new ones.

Think of two students before an exam. The first memorises the answers to the practice exam, and scores almost one hundred percent on it. But on the real exam, with new questions, she struggles. The second studies the ideas behind the questions. Her practice score is a little lower, but she also does well on the real exam.

The first student has overfitted. The real exam is the test set. So the clearest warning sign is a large gap between the training score and the test score.

## Demonstrate
Let's see this in a factory. Nusrat is a quality manager at a garment factory in Dhaka, Bangladesh. Her team wants a camera system to spot faulty shirts. Inspectors label shirt photos faulty or fine, and the team puts one fifth of them aside as a test set.

The first model scores ninety nine percent on the training photos, but only seventy percent on the test photos. That big gap shows overfitting. Most faulty training photos were taken on one table with a blue cloth. So the model had partly learned that blue cloth means faulty.

They take new photos on several tables, and train again. The second model scores ninety one percent on training photos, and eighty nine percent on test photos. The scores are close, so it is more likely to work on new shirts.

But faulty shirts are rare. So before approving it, Nusrat also checks how many of the faulty test shirts it caught. She asks the two questions. Was it tested on examples it never saw? And which mistakes does it make?

Now look at two report cards from your exercise. A clinic wants a model that labels patient messages urgent or not urgent. Report card A says ninety nine percent on training messages, and ninety eight percent on a test set taken from those same training messages.

Report card B says ninety percent on training messages, and eighty seven percent on five hundred new messages from a different month. It also reports that it caught forty six of the fifty urgent messages. Which one would you trust?

## Recap
Let's recap. First, test a model on examples it never saw during training, called the test set. Second, accuracy is the share of test examples it got right, but it can hide which mistakes it makes, especially when one answer is rare. Third, overfitting means memorising the training examples, and a big gap between training and test scores is the main warning sign.

## CTA
Now it is your turn. In the exercise below this video, read both report cards carefully. Use the two questions, decide which model you would trust, and explain why in two or three sentences. Next week, we start the final module, with Generative AI and Chatbots. See you there.

## Thumbnail
Headline: 99% Accurate? Ask Twice
Image: Navy background, a large '99%' stamp with a teal question mark beside it, headline in teal Inter Bold.

## Production Notes
- No facts to verify: the factory, the clinic and both report cards are hypothetical, and all numbers are invented for teaching (content.md Review Flags: None). Add the caption 'Hypothetical example' to scenes 13 and 14.
- Scenes 13 and 14 show the exercise report cards as slides. Copy the numbers exactly from content.md: A = 2,000 training messages, 99% training accuracy, test set of 100 taken from the training messages, 98% test accuracy, urgent caught not reported. B = 2,000 training messages, 90% training accuracy, 500 new test messages from a different month, 87% test accuracy, 46 of 50 urgent caught.
- The presenter does not reveal which report card to trust; the answer is in the exercise key.
- Nusrat's factory in Dhaka is fictional; stock footage must not show real brand names or logos.
