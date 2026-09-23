# L05 Supervised Learning: Classification and Regression

Course: AI-01 · Module: M2 · Objectives: O3 · Video: 5 min

## Hook
A food delivery app tells you two things when you order: "Your order is likely to be on time" and "Arrives in about 35 minutes." Both answers come from machine learning. But they are two different kinds of answer. One is a category. The other is a number. This lesson explains why that difference matters.

## Explanation
In L03 and L04 you learned that a model studies examples with features and labels during training, and then makes predictions about new cases. When every training example comes with the correct answer attached, we call this **supervised learning**. The labels act as an answer key. The model makes a guess, compares it with the answer key, and improves.

Supervised learning has two main types. The type depends on what kind of answer you want.

**Classification** predicts a category. The answer is one choice from a fixed list. Examples:
- Is this email "spam" or "not spam"?
- Is this loan application "low risk", "medium risk" or "high risk"?
- Does this photo show a cat, a dog or a bird?

**Regression** predicts a number on a scale. The answer can be any value in a range. Examples:
- How many minutes will this delivery take?
- What price will this used car sell for?
- How many umbrellas will this shop sell next week?

A simple test helps you tell them apart. Ask: "Could the answer be 'somewhere in between'?" If the answer is a delivery time, 34 minutes and 35 minutes are both possible, and so is everything in between. That is regression. If the answer is "spam" or "not spam", there is no halfway point. That is classification.

**Analogy:** Think of a postal worker and a weighing scale in the same post office. The postal worker reads each letter and puts it into one of several boxes: local, national or international. That is classification. The scale measures each parcel and shows a number, such as 2.4 kilograms. That is regression. Both are useful, and both learned their job from past examples, but one gives a box and the other gives a measurement.

Why does the type matter? Because it changes the data you collect and the way you judge the model. For classification, your labels are category names, and you check how often the model picks the right box. For regression, your labels are numbers, and you check how close the model's number is to the real one.

## Worked Example
Andrés manages a small courier company in Medellín, Colombia. Customers keep calling to ask when their parcels will arrive. He has records of 5,000 past deliveries. Each record includes features such as the distance, the time of day, the day of the week, the weather and the neighbourhood.

First, Andrés wants to warn customers early about problems. He adds a label to each old record: "late" or "on time". A model trained on these records learns to put new deliveries into one of the two groups. This is **classification**.

Next, he wants to show an exact arrival estimate in the tracking message. He uses the same records, but this time the label is the actual number of minutes each delivery took. A model trained on these records predicts a number, such as 47 minutes. This is **regression**.

The features stay almost the same. Only the label changes, and the label decides the type of task.

Across the world, the same pattern appears. A tea farm in Sri Lanka might classify leaf photos as "healthy" or "diseased", and use regression to predict next month's harvest in kilograms. A hotel in Portugal might classify reviews as "positive" or "negative", and use regression to predict how many rooms will be booked on a holiday weekend.

## Common Mistake
Many learners think that if the answer contains a number, the task must be regression. This is not always true. A shoe size, a star rating from 1 to 5, or a postcode are written as numbers, but they often work as categories. A model that picks "4 stars" from five fixed choices is doing classification. Always ask whether the answer is a choice from a list or a measurement on a scale, not whether it looks like a number.

## Key Takeaways
1. Supervised learning means the model learns from examples that include the correct answer, called labels.
2. Classification predicts a category from a fixed list, such as "spam" or "not spam".
3. Regression predicts a number on a scale, such as a delivery time in minutes or a price.

## Hands-on Exercise
**Task:** Label 10 business questions as classification or regression.
**Tools:** Pen and paper, or any notes app. Optional: ChatGPT or Claude (free tier) to compare your answers.
**Steps:**
1. Read these 10 questions:
   1. Will this customer cancel their phone contract this month?
   2. How many kilograms of rice will this shop sell next week?
   3. Is this product review positive, negative or neutral?
   4. What will this flat rent for per month?
   5. Which department should receive this customer email: sales, billing or support?
   6. How many minutes will this patient wait at the clinic?
   7. Is this bank transaction fraud or not fraud?
   8. What temperature will the warehouse reach tomorrow afternoon?
   9. Which of five sizes (XS, S, M, L, XL) will this customer most likely order?
   10. How many hours will this machine run before it needs repair?
2. For each question, write "classification" or "regression".
3. Next to each answer, write the kind of label the model would learn from, such as "yes/no" or "number of minutes".
4. Optional: ask a free AI chatbot to label the same list, and note any question where it disagrees with you. Decide who is right, and why.
**What good looks like:** Questions 1, 3, 5, 7 and 9 are classification. Questions 2, 4, 6, 8 and 10 are regression. Each answer names the label, and question 9 is correctly treated as classification even though sizes look like a scale.
**Time:** about 15 minutes

## Review Flags
- None. All examples are general and hypothetical, and no specific facts need checking.
