# Capstone Rubric: Fine-Tune and Document a Neural Network

## Task
Choose a real image or text classification task with a public dataset whose licence allows your use, and train and fine-tune a neural network for it. You build a baseline and an experiment plan in L18 (capstone step 1), run and compare tracked experiments with a pretrained model in L19 (capstone step 2), and write a model-card-style report with a reproducible notebook in L20 (capstone step 3). Do not use personal data or your employer's confidential data, and do not put keys or tokens in the notebook. The project must also be able to finish on CPU with a data subset; a Colab GPU is optional.

## Deliverables
- A Colab (or Jupyter) notebook that runs from the start with "restart and run all", including data loading, the baseline, all experiments and the final test evaluation.
- A results table (CSV or notebook table) with one row per run: config, validation metric, best epoch and, for the leading settings, results over at least 3 seeds.
- An experiment plan with at least 3 hypotheses, each marked as supported, not supported or unclear.
- A model-card-style report (about 2–4 pages) with intended use, data, method, experiments table, results, error analysis, limitations and reproducibility notes.
- The best checkpoint saved with its config (on Google Drive or as a download), and the name and licence of every dataset and pretrained checkpoint used.

## Criteria
| Criterion | Objective | Excellent | Good | Developing | Not yet | Points |
|---|---|---|---|---|---|---|
| Data, baseline and training pipeline | O3 | Licensed dataset with no personal data, reproducible seeded splits, a logged baseline, and a clean PyTorch or Trainer pipeline (Dataset/DataLoader or datasets, correct train/eval modes) that runs on CPU and GPU. | Licensed dataset, fixed splits, a baseline and a working pipeline with minor issues. | Pipeline works but the baseline is missing, the splits are not reproducible, or the licence is not recorded. | No working pipeline or no usable dataset. | 20 |
| Pretrained model and fine-tuning | O4 | Uses a pretrained torchvision or Hugging Face model correctly (matching preprocessing or tokenizer, new head, sensible freezing or fine-tuning, suitable learning rates), and records the checkpoint licence. | Uses a pretrained model correctly with small gaps, such as a missing licence note. | A pretrained model is used, but with errors such as mismatched preprocessing or an optimiser that misses trainable layers. | No pretrained model used. | 20 |
| Diagnosis of training behaviour | O5 | Learning curves for key runs are plotted and correctly diagnosed (overfitting, underfitting, learning-rate or gradient problems), and each diagnosis leads to a specific change. | Curves are plotted and mostly well diagnosed, with reasonable next steps. | Curves are shown but not interpreted, or the diagnosis does not match the evidence. | No learning curves or diagnosis. | 15 |
| Experiments, comparison and final choice | O6 | At least 3 planned experiments, changed one at a time, compared on the same validation split and metric, leaders run with 3+ seeds, a justified final choice made before a single test evaluation. | 3 comparable experiments with a justified choice; seed runs or one detail missing. | Fewer than 3 experiments, unfair comparisons, or the choice is not justified. | No tracked experiments, or the model was chosen on the test set. | 25 |
| Report and reproducibility | O7 | A clear model-card-style report with all eight sections, numbers that match the notebook, specific limitations and out-of-scope uses, and a notebook a peer can run from the start with no secrets. | Report covers most sections and the notebook runs, with small inconsistencies. | Report is missing several sections, or the notebook needs manual fixes to run. | No report, or the notebook cannot be run by someone else. | 20 |

Total: 100

## Submission Checklist
- My dataset's licence and source are recorded, and it contains no personal or confidential data.
- My splits use a fixed seed, and I built and logged a baseline before any deep model.
- I used at least one pretrained model with its own preprocessing or tokenizer, and recorded its name and licence.
- I plotted learning curves for my key runs and wrote a diagnosis for each.
- I ran at least 3 planned experiments, logged every run, and ran my leading settings with at least 3 seeds.
- I chose my final model on validation data, wrote the reason down, and then evaluated it once on the test set.
- My report has all eight model-card sections, and every number in it matches my notebook or results table.
- My notebook runs with "restart and run all", has no keys or tokens in it, and a peer has run it.
- My best checkpoint is saved with its config.
