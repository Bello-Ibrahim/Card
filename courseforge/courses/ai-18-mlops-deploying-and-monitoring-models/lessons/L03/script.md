# L03 Structuring an ML Project for Production | Presenter Script

Course: AI-18 · Video: 5 min · Words: 688

## Hook
If you deleted your laptop today, could a teammate rebuild your model tomorrow, and get exactly the same score? If the honest answer is probably not, this lesson is for you.

## Explain
Last time, we mapped the MLOps lifecycle. Now we build its first piece. You already know scikit-learn and Git, so we focus only on what changes for production. A production project has five features that a notebook usually lacks.

First, a training script that runs from start to finish with one command. Second, a configuration file for settings such as the random seed, the test size and model parameters. Third, pinned dependencies, so every machine installs the same library versions.

Fourth, fixed random seeds, everywhere randomness appears. Fifth, a clear folder layout under Git. The Git rule in one line: commit code and configuration, but not data files, model files or secrets.

Our running example predicts whether a red wine is good, meaning a quality score of seven or higher, from four features. If the real data file is missing, the loader builds a synthetic practice dataset with a fixed seed, so the course works offline.

The model is a scikit-learn pipeline, a scaler plus logistic regression. So preprocessing is saved inside the model file. This avoids the mismatch we saw in the last lesson, where the service skipped a scaling step.

Think of it this way. A notebook is like cooking from memory. A production project is like a printed recipe card, with exact amounts, oven temperature and cooking time. Anyone with the card and the same ingredients gets the same dish.

## Demonstrate
Let's watch Aarav Mehta, an ML engineer at a hypothetical grocery chain in Pune, refactor the wine notebook. In a terminal, he creates the project folder and starts Git. Then he creates a virtual environment and installs four packages.

Next, the configuration file. It holds the seed, the test size and the model settings. When he wants to try a new setting, he changes this file, not the code. And because the seed lives here, every function that uses randomness gets the same value.

Now the training script. It reads the configuration, loads the data, and splits it using the seed from the file. It builds the pipeline, trains it, and measures the F1 score. Then it saves the model and writes the score to a small metrics file. Notice that the scaler is inside the pipeline, so the saved file carries its own preprocessing.

He pins the exact versions he tested with, using pip freeze. The file now lists every library with an exact version number. Your versions may differ from ours. What matters is that you pin the ones you actually tested.

Now the real test. He runs the script twice. On our synthetic data, both runs print an F1 of zero point five five six eight. The score is modest, because the practice data is deliberately noisy. The point is that it is identical.

Finally, he adds the model file, the metrics file and the data folder to the ignore file, and commits. Git status shows no model or data files.

A common mistake is to set the seed in the model but forget the data split, or the reverse. The score then moves a little on every run, and you cannot tell if your change caused it. Set the seed in one place, and pass it everywhere.

## Recap
Let's recap. First, a production project has a training script, a configuration file, pinned dependencies, fixed seeds and a clear layout under Git. Second, keep preprocessing inside the saved pipeline, so training and serving use the same steps. Third, test reproducibility directly: run training twice and compare.

## CTA
In the exercise below this video, you will refactor a notebook into this structure, run it twice, and prove the results are identical. It takes about forty minutes. Check that git status shows no data or model files. Keep this project safe, because it becomes the base of your capstone at the end of the course.

In the next lesson, we record every training run automatically, in Experiment Tracking with MLflow. See you there.

## Thumbnail
Headline: Same Score, Every Time
Image: Navy background, two identical terminal windows side by side both showing F1 = 0.5568 with a teal equals sign between them, headline in teal Inter Bold.

## Production Notes
- [VERSION] The pinned versions in requirements.txt (scikit-learn 1.9.1, pandas 3.0.6) were the versions used to test the code; check and update them before recording. The voiceover does not say version numbers.
- [VERIFY] The Wine Quality dataset licence and location are checked in L04. The demo uses the offline synthetic fallback from data.py, so the voiceover makes no claim about the dataset itself.
- F1 = 0.5568 is a real output from two runs on the synthetic fallback data; it must match on screen. If the recording gives a different value, update the voiceover before release.
- Screen recording: use a clean terminal and editor with a large font. No personal folder names, usernames or tokens visible in the prompt or paths.
- Aarav Mehta and the Pune grocery chain are hypothetical. Git basics are a prerequisite, so the lesson gives a one-line recap only (curriculum judgement call).
