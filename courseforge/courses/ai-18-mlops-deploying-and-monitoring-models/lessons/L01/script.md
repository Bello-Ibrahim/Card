# L01 Why Models Fail After the Notebook | Presenter Script

Course: AI-18 · Video: 5 min · Words: 735

## Hook
Your model scored well in the notebook last month. Today a colleague runs the same notebook on a new laptop. First the score is different, then there is an error. Nothing about the model changed. So what broke?

## Explain
Hi, and welcome to MLOps: Deploying and Monitoring Models. In this first lesson, we look at the gap between it works on my machine, and it works every day for real users.

A notebook is an excellent place to explore. It is a poor place to run a production system. Most production failures of machine learning models are not caused by the algorithm. They come from everything around it. Four groups of problems appear again and again.

The first group is missing or changing dependencies. The notebook imports libraries without fixed versions, and a new release changes a default value. The second group is different data. Training used a file on one laptop, but live data brings new categories, missing values or different units.

The third group is silent errors. A cell ran out of order, a random seed was never set, or a preprocessing step lives only in the notebook. The model still answers, but the answer is wrong, and nothing raises an error. The fourth group is nobody watching. The world changes, and the model slowly becomes less accurate. We call this drift.

MLOps, short for machine learning operations, is the set of practices that closes this gap. You will meet six key terms. An artefact is any file the pipeline produces, such as a model or a Docker image. A model registry stores each model version and marks which one is in production. CI and CD mean every change is tested and built automatically.

Serving means making a model available to other systems, for example through an API. Drift means production data no longer looks like training data. And rollback means returning quickly to the last working version. The central idea is reproducibility. Version the code, the data and the model together, and anyone can rebuild the same model.

Here is a simple picture. A recipe that works in your home kitchen is not ready for a food factory. The factory needs written steps, exact measures, known suppliers and quality checks on every batch. A notebook is the home recipe. An MLOps project is the factory version.

## Demonstrate
Valentina Rojas is a data scientist at a car insurance company in Chile. The company is hypothetical. She trained a claim fraud classifier in a notebook, and it looked good. Her team deployed it by copying the notebook code into a web service.

Three weeks later, the operations team asked a question. Why does the model flag almost no claims? Valentina investigated, and she found four separate causes.

First, the notebook scaled the claim amount before training, but the service sent raw amounts. Second, the server installed a newer library version, and one default setting had changed. Third, a new claim type appeared in the live data, and the model had never seen it. Fourth, nobody had checked the share of flagged claims since launch, so the problem ran for weeks.

None of these problems was about choosing a better algorithm. Each one had a process fix. Keep preprocessing inside the saved model pipeline. Pin library versions. Check live inputs against the training data. And monitor the prediction rate.

One common mistake is to believe that a high test score means the model is ready. A test score tells you how the model did on one dataset, on one machine, on one day. It says nothing about whether someone else can rebuild it. Treat it as an entry requirement, not the finish line.

## Recap
Let's recap. First, most production failures come from dependencies, data differences, silent errors and missing monitoring, not from the algorithm. Second, the key terms are artefact, model registry, CI and CD, serving, drift and rollback. Third, versioning code, data and model together makes results reproducible and explainable.

## CTA
Now it is your turn. In the exercise below this video, you will review a sample notebook from a teammate. You will find at least six problems that would break it in production, and write a fix for each. It takes about twenty minutes.

Everything in this course leads to the capstone, where you deploy and monitor your own model API. In the next lesson, we look at the MLOps lifecycle and maturity levels. See you there.

## Thumbnail
Headline: It Worked on My Machine
Image: Navy background, a laptop with a notebook chart on the left and a red broken link to a server rack on the right, headline in teal Inter Bold.

## Production Notes
- No facts to verify: content.md Review Flags are None; the Chile insurance company and Valentina Rojas are hypothetical.
- Stock footage must not show a real insurance company name or logo.
- Scenes 5 and 6: reveal the six key terms one by one, in the order spoken, so the glossary slide builds up.
