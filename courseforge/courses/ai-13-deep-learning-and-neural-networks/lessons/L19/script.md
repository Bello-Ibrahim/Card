# L19 Capstone Step 2: Fine-Tune and Compare | Presenter Script

Course: AI-13 · Video: 5 min · Words: 683

## Hook
You have a baseline and a plan. This week, you train several models, and one will look best. The hard part is not training them. It is saying honestly that the winner really is better, and then testing it exactly once.

## Explain
Run your plan in order. Start with the experiment most likely to give a large gain, usually a pretrained model. A ResNet for images, or a small encoder from the Hub for text. Then add regularisation and tuning, one change at a time.

After each run, log a row to your results table, and write one line in your plan. Was the hypothesis supported? Keep failed runs too. They are evidence for your report. Also record the name and licence of every pretrained checkpoint you use.

Compare fairly. Every run must use the same validation split and preprocessing, and the same main metric, computed the same way. Budgets must be comparable, or noted. And the leading candidates need more than one seed.

Choose the final model on validation data, and justify it. The best score is not the only reason. If two models are within seed variation, prefer the smaller, faster or simpler one. Then, and only then, evaluate it once on the test split. If you change the model after seeing the test result, the test score is no longer honest, and you must say so.

It is like judging a cooking competition. Every chef cooks the same dish, with the same ingredients and time, for the same judges. The final public tasting happens once. If a chef could taste the judges' plate and then cook again, it would not be fair.

## Demonstrate
Diego is an engineer at an avocado exporter in Uruapan, Mexico. His capstone classifies leaf photos into four classes, from a public dataset with a confirmed licence. His baseline is a small CNN trained from scratch.

In Colab, he loads his results table from Drive, so nothing is lost when a session ends. It has four runs. The baseline CNN, a frozen ResNet eighteen with a new head, the same with its last block fine-tuned, and the fine-tuned model with a learning-rate schedule.

He reruns the top two with two more seeds. Then he groups the table by run, and shows the mean, the spread and the count of validation F1, sorted from best to worst. Two extra seeds per run is a small cost for an honest comparison.

The two fine-tuned runs are within seed variation of each other. So Diego chooses the version without the schedule, because it is simpler and equally good. He writes that reason next to the table, before he touches the test set.

Now he reloads the chosen checkpoint, and evaluates it on the test set, exactly once. He copies the number into his report, and does not change the model afterwards. If he changed it now, the test score would no longer be an honest estimate.

A common mistake is evaluating every candidate on the test set, just to see, and then picking the best test score. This makes the test set a second validation set, and the reported score is too optimistic. Another is comparing runs with different validation splits, for example because the split was made without a fixed seed. Check the split is identical across all runs.

## Recap
Let's recap. First, run planned experiments one change at a time, starting with a pretrained model, and log every run with its config. Second, compare on the same validation split and metric, use extra seeds for the leaders, and prefer the simpler model when results are within seed variation. Third, evaluate the chosen model once on the test set, and report that number without further changes.

## CTA
Now it is your turn. This is capstone step two. In the exercise below this video, you will run at least three tracked experiments, choose your final model, and evaluate it once on the test set. Check your work against the capstone rubric. It takes about ninety minutes. In the final lesson, capstone step three, you document your experiments. See you there.

## Thumbnail
Headline: Choose Fairly, Test Once
Image: Navy background, four result bars with error ranges, one circled, and a sealed envelope labelled test, headline in teal Inter Bold.

## Production Notes
- [VERIFY] Licences and intended uses of all pretrained checkpoints used (for example ImageNet-pretrained torchvision weights and Hub encoders) must be recorded; the course page should link to where to find them. Diego's leaf dataset must be one of the course team's confirmed-licence examples; show its card.
- No scores are stated in the voiceover (content.md gives none). Show the real summary table and the single test result; do not add numbers in captions.
- load_checkpoint and evaluate are Diego's own helpers from L17 and L05; define them above the demo cell. Record the test cell being run exactly once.
- Diego and the Uruapan avocado exporter are hypothetical; stock footage must not show a real company name or logo.
