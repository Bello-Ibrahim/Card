# L01 From Business Question to ML Problem | Presenter Script

Course: AI-12 · Video: 5 min · Words: 727

## Hook
A manager asks, can we use machine learning to fix late deliveries? That is a wish, not a machine learning problem. Before you open a notebook, you must turn that wish into something a model can actually learn.

## Explain
Hi, and welcome to Machine Learning with scikit-learn. Over four weeks, you will build, test and explain real models in Python. And everything starts with a well-framed problem.

You already know the idea of supervised learning. We show a model many past examples with known answers, and it learns patterns that connect the inputs to the answers. A good framing has four parts.

First, the business question. What decision will the prediction support? Which deliveries should we warn customers about today is much better than predict delays, because it tells you who uses the result, and when.

Second, the target. This is the one column the model predicts, also called the label, or y. It must be something you can see in past data, with an exact definition. For example, late means it arrived more than twenty-four hours after the promised time.

Third, the features. These are the input columns, also called X. A feature is only useful if it is known at the moment of prediction. The distance of a route is known before the truck leaves. The actual arrival time is not, so it can never be a feature.

Fourth, the success measure. You need a model metric, and also a business measure, such as fewer complaints about surprise delays. Then decide the task type. If the target is a category, such as late or on time, it is classification. If it is a number, such as hours of delay, it is regression.

Here is a simple way to think about it. Framing a problem is like writing the address before you send a parcel. The truck, the driver and the route can all be excellent. But with no clear address, the parcel cannot arrive.

## Demonstrate
Let's see a real framing. Larissa Mendes is a data analyst at a logistics company in Recife, Brazil. The operations director asks her to use AI to reduce late deliveries. Larissa writes a one-page framing.

Her business question: each morning, which of today's deliveries are likely to be late, so the customer service team can contact those customers early? Her target is called is late. It is one if the parcel arrived more than twenty-four hours after the promised date, and zero otherwise.

Her features are route distance, number of stops, day of the week, vehicle type, depot, and the weather forecast for the day. The task type is binary classification. For success, the model should find most late deliveries, without so many calls that they become useless.

She also removes one tempting column, the driver delay reason. It is filled in after the delivery, so the model would not have it in the morning. Using it would make the model look excellent in testing and fail in real use. You will meet this again as data leakage in lesson five.

Larissa notes one limit too. The company only has eight months of data, so seasonal effects, such as a holiday peak, may be missing.

A common mistake is to pick the target, and then add every column in the table as a feature. That often includes columns recorded after the event, or almost a copy of the target, such as a refund issued for late delivery. It scores well in the notebook, and fails in production. For every feature, ask one question. Would I know this value when I need the prediction?

## Recap
Let's recap. First, a machine learning problem needs a business question, one target column, features known at prediction time, and a success measure. Second, a category target means classification, and a number target means regression. The decision you support tells you which to choose. Third, decide early which kind of mistake costs more, because that choice will guide your metric.

## CTA
Now it is your turn. In the exercise below this video, you will frame three business problems, from loan default in Kenya to hotel cancellations in Portugal and crop yield in India. You do not need code, and it takes about twenty minutes. In the next lesson, Your First Model: fit and predict, you will train a real model in Colab. See you there.

## Thumbnail
Headline: Wish or ML Problem?
Image: Navy background; left, a speech bubble with a vague wish; right, a neat four-part framing card (question, target, features, success); headline in teal Inter Bold.

## Production Notes
- No facts to verify: all cases are hypothetical (content.md Review Flags: None).
- This lesson is not a screen demo: slides, stock and one hero clip only. No notebook is shown.
- Larissa Mendes and the Recife logistics company are fictional; stock footage must not show a real courier brand, logo or vehicle livery.
- Say the target name is_late as 'is late' and the leaking column as 'driver delay reason'; the slide shows the exact column names.
- Scene 4 hero clip is 7 seconds and the scene is about 15 seconds: hold with a slow push-in, then cut.
