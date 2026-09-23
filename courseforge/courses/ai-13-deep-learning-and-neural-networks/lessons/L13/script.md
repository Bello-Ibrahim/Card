# L13 Fine-Tuning a Transformer for Text Classification | Presenter Script

Course: AI-13 · Video: 5 min · Words: 678

## Hook
In lesson ten, you gave a pretrained image network a new head, and taught it bean diseases. The same idea works for text. With Hugging Face, the whole process, from raw dataset to evaluated model, fits in about thirty lines.

## Explain
Fine-tuning a transformer for classification has five parts. First, the dataset. The datasets library loads public data from the Hub with its splits. You can take a shuffled subset, and split off a validation set from the training data.

Second, tokenisation in batches. The map method runs the tokenizer on many rows at once, and caches the result. Truncate to a maximum length that fits most texts. Padding happens later, per batch, with a data collator, which is faster.

Third, the model. The auto class for sequence classification loads the pretrained encoder and adds a new, random classification head. A warning that some weights are newly initialised is expected.

Fourth, the training arguments. They hold the learning rate, batch size, epochs, weight decay, and when to evaluate and save. Parameter names change between versions, so check them against your installed library. Fifth, the Trainer runs the loop from lesson five for you, and a metrics function reports accuracy and F1.

Unlike lesson ten, you usually fine-tune all layers of a small transformer, with a small learning rate, often around two to five times ten to the minus five, for a few epochs.

Think of an experienced translator who joins a new publishing house. They do not relearn the language. They spend a few days learning the house style. Fine-tuning is those few days. Small, careful adjustments to skills that are already there.

## Demonstrate
Joaquín is a data scientist at a news aggregator in Rosario, Argentina. He wants to sort English headlines into four topics. World, Sports, Business, and Science and Technology. He prototypes with AG News, a public topic dataset.

In Colab, he loads the dataset and takes small subsets, so training fits in free GPU time. Four thousand training examples, with twenty percent split off for validation, and two thousand test examples.

He loads the DistilBERT tokenizer, tokenises both splits with map, truncating at one hundred and twenty-eight tokens, and creates the model with four labels.

Next, a metrics function for accuracy and macro F1. Then the training arguments. A learning rate of three times ten to the minus five, two epochs, batches of thirty-two, evaluation and saving every epoch, and keep the best model at the end.

He builds the Trainer with the validation split as the evaluation set, and a data collator for padding. He trains, and then evaluates the test subset only once, at the end. He reports the accuracy and F1 he measured, and notes the subset sizes, because results on four thousand examples are not comparable with published results on the full dataset.

A common mistake is passing the test split as the evaluation set, with keep best model switched on. The Trainer then picks the checkpoint that is best on the test set, and the test score is too optimistic.

Use a validation split during training, and touch the test split once. And if you copy arguments from an old tutorial, you may get an unexpected keyword error. Check the names for your version.

## Recap
Let's recap. First, load data with the datasets library, tokenise in batches with map, and pad per batch with a data collator. Second, the sequence classification model adds a new head to a pretrained encoder. Fine-tune all layers with a small learning rate for a few epochs. Third, choose checkpoints on a validation split, evaluate the test split once, and check argument names against your installed version.

## CTA
Now it is your turn. In the exercise below this video, you will fine-tune a small pretrained model on a subset of AG News, and report accuracy and F1 on the test split. On a CPU, use one thousand training examples and shorter texts. It takes about forty-five minutes. In the next lesson, we learn to evaluate deep models properly. See you there.

## Thumbnail
Headline: Fine-Tune in Thirty Lines
Image: Navy background, a pretrained transformer block with a small new teal head sorting headlines into four coloured topic boxes, headline in teal Inter Bold.

## Production Notes
- [VERSION] Check TrainingArguments and Trainer parameter names (eval_strategy compared with the older evaluation_strategy, and other renamed options) and datasets loading and train_test_split behaviour against the Colab versions at recording time.
- [VERIFY] AG News Hub dataset ID (fancyzhx/ag_news in content.md), source and licence, and the licence and intended use of distilbert-base-uncased, must be confirmed before recording. Show both Hub pages briefly on screen.
- Results: content.md gives no numbers. The voiceover says learners report their own accuracy and macro F1; do not add numbers in captions. Results on the 4,000-example subset are not comparable with published full-dataset results.
- The Trainer needs accelerate; if missing, install with pip install transformers[torch] in a hidden cell before recording. Speed up the training segment in the edit.
- Joaquín and the Rosario news aggregator are hypothetical; stock footage must not show real news brands or logos.
