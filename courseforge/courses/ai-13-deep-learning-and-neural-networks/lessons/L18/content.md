# L18 Capstone Step 1: Choose a Task and Build a Baseline

Course: AI-13 · Module: M4 · Objectives: O3, O7 · Video: 5 min (screen demo)

## Hook
The most common reason capstone projects fail is not a bad model. It is a dataset that cannot be used, a task with no clear measure of success, or no simple result to compare with. You will fix all three this week, before you train anything large.

## Explanation
Your capstone has three steps: choose and baseline (today), experiment and choose (L19), and document (L20). Today's step has four parts.

**1. Choose a task.** It must be an **image or text classification** task with a clear label set, such as plant diseases, product categories, support-ticket topics or review sentiment. Pick something small enough for free GPU time: a few thousand examples is plenty, and you can use a subset of a larger dataset.

**2. Choose a public dataset with a clear licence.** The Hugging Face Hub and similar sources describe datasets on dataset cards. Check:

- the **licence**, and whether it allows your use; [VERIFY]
- the **source** and how labels were created;
- whether it contains **personal data**. Avoid datasets with faces, names, health records or private messages. Never upload your company's confidential data or personal data to a notebook service or the Hub.
- the **splits**: if there is no validation split, create one from the training data with a fixed seed.

**3. Build a baseline.** A baseline is the simplest reasonable model, trained quickly, that gives you a score to beat. For text, TF-IDF with logistic regression from AI-12 is a strong baseline. For images, a small CNN from L07, or a frozen pretrained backbone with a new head (L10), works well. Record the baseline in your results table (L17) with its config.

**4. Write an experiment plan.** List at least 3 planned experiments. Each has a **hypothesis** ("If I fine-tune the last block, validation F1 will improve, because the classes differ in fine texture"), the **one change** you will make, and the **metric** you will use to decide. Choose a main metric that fits the task: macro F1 when classes are unbalanced, accuracy when they are balanced and all errors cost the same.

**Analogy:** A baseline is like the time a runner records on the first day of training. Without it, a later time of 52 minutes means nothing. With it, the runner knows whether the new training plan actually helped.

## Worked Example
Fatima is a data scientist at a hypothetical telecoms company in Dakar, Senegal. For her capstone she chooses public, English-language customer-review text with three sentiment labels, from a Hub dataset whose card states a licence that allows educational use. She does not use her employer's customer messages.

**Screen demo steps:**

1. Open the dataset card, read the licence and label description, and write them in the notebook.
2. Load the data and check the class balance.
3. Build and score the TF-IDF baseline on the validation split.
4. Add the baseline row to the results table.

```python
from datasets import load_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score

ds = load_dataset("your-chosen/dataset")                        # [VERIFY] licence
split = ds["train"].train_test_split(test_size=0.2, seed=0)
train, val = split["train"], split["test"]
print(train.features["label"], train.to_pandas()["label"].value_counts())

vec = TfidfVectorizer(ngram_range=(1, 2), min_df=2)
clf = LogisticRegression(max_iter=1000, class_weight="balanced")
clf.fit(vec.fit_transform(train["text"]), train["label"])
preds = clf.predict(vec.transform(val["text"]))
print("baseline macro F1:", f1_score(val["label"], preds, average="macro"))
```

Fatima's plan lists three experiments: (1) fine-tune a small pretrained encoder with default settings; (2) the same model with a learning-rate sweep and warm-up; (3) the best setting with a larger maximum length, because some reviews are long. Each has a hypothesis and uses validation macro F1 to decide. The test split is not touched.

## Common Mistake
Many learners skip the baseline because it "will obviously lose". Sometimes it does not: on short or simple texts, TF-IDF can come close to a fine-tuned transformer at a tiny fraction of the cost. Without a baseline, you cannot show that your deep model is worth it. Another mistake is choosing a dataset first and checking the licence later, when changing is expensive. Check the licence before you write any code.

## Key Takeaways
1. Choose an image or text classification task with a public dataset whose licence, source and content you have checked, and avoid personal data.
2. Build a fast baseline and record it in your results table; it is the score every later experiment must beat.
3. Write an experiment plan with at least 3 experiments, each with a hypothesis, one change and a decision metric.

## Hands-on Exercise
**Task:** Capstone step 1: choose a dataset, train a baseline, and write an experiment plan with at least 3 planned experiments.
**Tools:** Google Colab (free); Hugging Face `datasets`; scikit-learn or PyTorch; your results table from L17. CPU is enough for text baselines; for image baselines, use a subset or a frozen backbone.
**Steps:**
1. Shortlist 2 or 3 datasets and read each dataset card. Record the licence, source, size, labels and any personal-data concerns. [VERIFY]
2. Choose one and create train, validation and test splits with a fixed seed.
3. Check and record the class balance, and choose your main metric with a one-line reason.
4. Train a baseline and log it to the results table with its config.
5. Write an experiment plan: at least 3 experiments, each with a hypothesis, the single change and the metric.
6. Save the notebook and the plan to Drive.
**What good looks like:** A clearly licensed dataset with no personal data, reproducible splits, a logged baseline score, and a plan whose hypotheses are specific and testable.
**Time:** about 60 minutes

## Review Flags
- [VERIFY] Every learner-chosen dataset licence and source must be checked by the learner; the course team should provide 3 example datasets with confirmed licences and IDs to replace the placeholder `your-chosen/dataset`.
