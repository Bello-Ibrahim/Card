# L05 Supervised Learning: Classification and Regression | Presenter Script

Course: AI-01 · Video: 5 min · Words: 684

## Hook
A food delivery app tells you two things. Your order is likely to be on time. And, arrives in about thirty five minutes. Both answers can come from machine learning. But one is a category, and the other is a number.

## Explain
Welcome to week two. You already know that a model trains on examples with features and labels. When every training example comes with the correct answer attached, we call this supervised learning. The labels act as an answer key.

Supervised learning has two main types, depending on the kind of answer you want. Classification predicts a category. The answer is one choice from a fixed list. Is this email spam or not spam? Is this loan application low, medium or high risk? Does this photo show a cat, a dog or a bird?

Regression predicts a number on a scale. The answer can be any value in a range. How many minutes will this delivery take? What price will this used car sell for? How many umbrellas will this shop sell next week?

Here is a simple test. Ask, could the answer be somewhere in between? A delivery could take thirty four minutes, or thirty five, or anything in between. That is regression. But spam or not spam has no halfway point. That is classification.

Think of a post office. A postal worker reads each letter, and puts it into one of several boxes: local, national or international. That is classification. Next to her, a scale weighs each parcel and shows a number, such as two point four kilograms. That is regression. Both learned their job from past examples. But one gives a box, and the other gives a measurement.

The type matters, because it changes the labels you collect and how you judge the model. For classification, you check how often it picks the right box. For regression, you check how close its number is to the real one.

## Demonstrate
Let's see both types in one business. Andrés manages a small courier company in Medellín, Colombia. Customers often call to ask when their parcels will arrive. He has records of five thousand past deliveries, with features such as distance, time of day, weather and neighbourhood.

First, he wants to warn customers early about problems. So he adds a label to each old record: late, or on time. A model trained on these records puts new deliveries into one of the two groups. This is classification.

Next, he wants to show an exact arrival time in the tracking message. He uses the same records, but this time the label is the actual number of minutes each delivery took. Now the model predicts a number, such as forty seven minutes. This is regression.

Notice what happened. The features stay almost the same. Only the label changes, and the label decides the type of task.

The same pattern appears in other industries. A tea farm in Sri Lanka might classify leaf photos as healthy or diseased, and use regression to predict next month's harvest in kilograms.

One common mistake is to think that any answer with a number must be regression. A star rating from one to five is written as a number. But a model that picks four stars from five fixed choices is doing classification. A shoe size or a postcode can work the same way. So ask, is this a choice from a list, or a measurement on a scale?

## Recap
Let's recap. First, supervised learning means the model learns from examples that include the correct answer, called labels. Second, classification predicts a category from a fixed list, such as spam or not spam. Third, regression predicts a number on a scale, such as a delivery time in minutes, or a price.

## CTA
Now it is your turn. In the exercise below this video, you will read ten business questions and label each one as classification or regression. Watch out for question nine. It looks like a scale, but think carefully. It takes about fifteen minutes. In the next lesson, we meet two more ways machines learn, in Unsupervised and Reinforcement Learning. See you there.

## Thumbnail
Headline: A Box or a Number?
Image: Navy background, split card: three labelled sorting boxes on the left and a digital scale showing a number on the right, headline in teal Inter Bold.

## Production Notes
- No facts to verify: all examples are general or hypothetical (content.md Review Flags: None).
- The delivery app in the hook is generic: show an unbranded mock-up, not a real delivery app.
- Andrés's courier company in Medellín and the tea farm in Sri Lanka are fictional; stock footage must not show real company names or logos.
