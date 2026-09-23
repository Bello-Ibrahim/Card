# L01 From Business Question to ML Problem

Course: AI-12 · Module: M1 · Objectives: O1 · Video: 5 min

## Hook
A manager says, "Can we use machine learning to fix late deliveries?" That is a wish, not a machine learning problem. Before you open a notebook, you must turn the wish into something a model can learn: one column to predict, a set of columns to learn from, and a clear way to measure success.

## Explanation
You already know the idea of supervised learning: we show a model many past examples with known answers, and it learns patterns that connect the inputs to the answers. This course uses scikit-learn to do that in Python. Everything starts with a well-framed problem.

A good framing has four parts.

1. **The business question.** What decision will the prediction support? "Which deliveries should we warn customers about today?" is better than "Predict delays", because it tells you who uses the result and when.
2. **The target.** This is the one column the model predicts, also called the label or `y`. It must be something you can observe in past data. "Late" needs an exact definition, for example "arrived more than 24 hours after the promised time".
3. **The features.** These are the input columns, also called `X`. A feature is only useful if it is **known at the moment of prediction**. The distance of a route is known before the truck leaves. The actual arrival time is not, so it can never be a feature.
4. **The success measure.** How will you know the model is good enough? This includes a model metric and a business measure, such as "fewer complaints about surprise delays".

Next, decide the **task type**. If the target is a category, such as late / on time, or fraud / not fraud, it is **classification**. If the target is a number, such as hours of delay or kilograms of crop, it is **regression**. The same business wish can become either task. "Will this parcel be late?" is classification. "How many hours late will it be?" is regression. Choose the one that matches the decision.

Finally, choose a first metric. For classification you will meet accuracy, precision, recall, F1 and ROC AUC in Module 2. For regression you will meet MAE, RMSE and R² in Module 3. At this stage, write down which mistake is more costly. For example, is it worse to warn a customer when the parcel is on time, or to stay silent when it is late? That answer will guide your metric later.

**Analogy:** Framing a problem is like writing the address before you send a parcel. The truck, the driver and the route can all be excellent, but with no clear address the parcel cannot arrive. The target, the features and the success measure are the address for your model.

## Worked Example
Larissa Mendes is a data analyst at a hypothetical logistics company in Recife, Brazil. The operations director asks her to "use AI to reduce late deliveries". Larissa writes a one-page framing:

- **Business question:** Each morning, which of today's deliveries are likely to be late, so the customer service team can contact those customers early?
- **Target:** `is_late` = 1 if the parcel arrived more than 24 hours after the promised date, otherwise 0.
- **Features:** route distance in km, number of stops on the route, day of the week, vehicle type, depot, and the weather forecast for the day.
- **Task type:** binary classification.
- **Success measure:** the model should find most of the late deliveries (a recall target to be agreed), and the team should not have to call so many customers that the calls become useless.

She also removes one tempting column: `driver_delay_reason`. It is filled in after the delivery, so the model would not have it in the morning. Using it would make the model look excellent in testing and fail in real use. You will meet this problem again as **data leakage** in L05.

Larissa notes one limit: the company only has 8 months of data, so seasonal effects, such as a holiday peak, may be missing.

## Common Mistake
Many learners pick the target first and then add every column in the table as a feature. This often includes columns that are recorded after the event, or that are almost a copy of the target, such as a "refund issued for late delivery" flag. The model then scores very well in the notebook and fails in production. For every feature, ask: "Would I know this value at the moment I need the prediction?" If not, remove it.

## Key Takeaways
1. A machine learning problem needs a business question, one target column, features that are known at prediction time, and a success measure.
2. A category target means classification; a number target means regression. The decision you support tells you which one to choose.
3. Decide early which kind of mistake costs more, because that choice will guide your metric.

## Hands-on Exercise
**Task:** Frame 3 business problems as machine learning problems.
**Tools:** A notes app, a spreadsheet or paper. You do not need code for this exercise.
**Steps:**
1. Use these hypothetical cases: a microlender in Kenya that wants to predict loan default; a hotel group in Portugal that wants to predict booking cancellations; a farming cooperative in India that wants to predict crop yield per hectare.
2. For each case, write the business question as one sentence that names who will use the prediction and when.
3. Define the target column exactly, including units or the rule for "yes".
4. List 4 features and, for each one, write "known before prediction: yes/no". Replace any feature marked "no".
5. Write the task type (classification or regression) and one metric you would start with.
6. Write one sentence about which mistake would be more costly.
**What good looks like:** Three short framings in a table. Each target is precise (for example, "cancelled within 7 days of arrival: yes/no"). All features are known at prediction time. Loan default and cancellation are classification; crop yield is regression.
**Time:** about 20 minutes

## Review Flags
- None. All cases are hypothetical and the lesson has no code, tool steps or statistics to check.
