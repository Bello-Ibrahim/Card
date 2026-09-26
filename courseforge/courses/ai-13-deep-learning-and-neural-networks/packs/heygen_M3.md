# HeyGen Batch Pack: AI-13 M3 (Neural Networks for Text)

Course: Deep Learning and Neural Networks. Make one HeyGen video per lesson below, using these settings for every video.

| Setting | Value |
|---|---|
| Avatar | **Vaness** (standard avatar), ID `1bd001e7e50f421d891986aad5c8bbd2` |
| Voice | `1bd001e7e50f421d891986aad5c8bbd2` (the same ID as the avatar: if HeyGen does not list it as a voice, use Vaness's paired English voice and record its ID in DECISIONS.md) |
| Background | Solid colour **#00FF00** (pure green, no gradient, no image) |
| Resolution | 1080p (1920×1080) |
| Aspect ratio | 16:9 |
| Avatar framing | Centred, head and shoulders, same size in every lesson |
| Captions/subtitles | **Off** (captions are added in Stage 6) |
| Music | Off |
| Speed | Normal (1.0×) |

How to paste: copy the whole text block for a lesson into a single HeyGen scene. Each blank line is a natural pause. Do not add or change words, because the edit is timed to this exact narration.

Save each finished video with the exact filename shown, and upload it to `/incoming/`.

## L11 Turning Text into Numbers: Tokens and Embeddings

- **Filename:** `ai-13-deep-learning-and-neural-networks_M3_L11_presenter.mp4`
- **Expected length:** about 4.9 minutes (681 words). The quality gate accepts ±10%.

```text
Write one sentence about a morning train in English, French, Portuguese and Arabic. You see four sentences of similar length. A tokenizer may see quite different numbers of pieces, and that affects cost, speed and sometimes accuracy.

Welcome to module three, where we work with text. A network needs numbers, so text goes through two steps. The first is tokenisation. It splits text into tokens, and maps each token to a whole-number ID from a fixed vocabulary.

Modern models use sub-word tokenisers. Common words stay whole. Rare or long words are split into pieces, such as un, believ and able. This keeps the vocabulary to tens of thousands of entries, while still handling any word, including names and spelling mistakes.

A Hugging Face tokenizer also adds the special tokens the model expects, at the start and the end. In a batch, it pads short texts and cuts long ones, and returns an attention mask. One for real tokens, zero for padding. Every model has its own tokenizer, so always load them together.

Why do counts differ by language? A tokenizer learns its vocabulary from its training text. Languages and scripts that were common there get more whole-word tokens. Others are split into more pieces. More tokens mean more compute, and the text fills the model's maximum length sooner.

The second step is embeddings. An embedding layer is a lookup table. Row i is a learned vector for token i. It is trained with the rest of the network, so tokens used in similar contexts end up with similar vectors. You measure closeness with cosine similarity.

In a transformer, which we meet next, these vectors are then updated by context, so one word can get different vectors in different sentences.

Think of a library. Tokenisation gives every book a shelf code, and splits a very long encyclopedia into several volumes. Embeddings arrange the shelves so that books on similar subjects stand near each other. The codes are arbitrary. The positions carry the meaning.

Layla is an NLP engineer at a customer-support company in Amman, Jordan, that answers messages in several languages. Before choosing a model, she checks how a multilingual tokenizer handles one sentence in four languages.

In Colab, she loads the tokenizer for XLM-RoBERTa base, a multilingual model. She checks the licence on its Hub page first. Then she writes the train sentence in English, French, Portuguese and Arabic.

For each language, she prints the number of tokens and the tokens themselves. You should see something like sub-word pieces, with special tokens at the start and end, and counts that are similar, but not equal. She notes which words were split into several pieces.

Then she tokenises all four sentences as one padded batch. Every row now has the same length, and the attention mask shows where the padding starts. She also decodes the IDs back to text, to confirm nothing was lost. This is exactly what the model will receive.

Layla uses public example sentences only. She never pastes real customer messages into a notebook or an online tool.

A common mistake is loading the tokenizer from one checkpoint and the model from another, for example a multilingual tokenizer with an English-only model. The code runs, because IDs are just numbers, but each ID now points to the wrong embedding row. Always use the same checkpoint name. And count tokens, not words, when you check length limits.

Let's recap. First, tokenisers split text into sub-word tokens with IDs, add special tokens, and pad or truncate batches with an attention mask. Second, the same sentence can produce different token counts in different languages, which affects compute and maximum length. Third, an embedding layer is a learned lookup table from token IDs to vectors, where tokens used in similar contexts end up close together.

Now it is your turn. In the exercise below this video, you will tokenise your own neutral sentence in English, French, Portuguese and Arabic, and compare the tokens and counts. It takes about twenty-five minutes. In the next lesson, we go from sequences to transformers. See you there.
```

## L12 From Sequences to Transformers

- **Filename:** `ai-13-deep-learning-and-neural-networks_M3_L12_presenter.mp4`
- **Expected length:** about 4.9 minutes (685 words). The quality gate accepts ±10%.

```text
The bank refused the loan because it was too risky. What does it refer to? You knew at once, because you saw the whole sentence together. Older networks read one word at a time. Transformers look at everything together.

After the last lesson, a sentence is a sequence of token vectors, and order matters. The question is how to combine them into one meaning. Recurrent networks read the tokens one at a time. At each step, they update a hidden state, a summary of everything read so far.

This has two problems. It is slow, because step fifty cannot start until step forty-nine is finished, so a GPU's parallel units sit idle. And it is forgetful. Early information must pass through every later step, and over long texts it fades. LSTMs reduce this problem, but do not remove it.

An RNN is like passing a message down a line of people by whispering. It is slow, and details from the start are lost. Attention is like a meeting where everyone can hear everyone else at once, and each person decides who is worth listening to.

Here is attention in simple terms. Each token makes three vectors. A query, which is what it is looking for. A key, which is what it offers. And a value, the information it passes on. All three are learned from its embedding.

Then one token's query is compared with the keys of all tokens. Similar pairs get high scores. A softmax turns the scores into weights that add up to one. The token's new vector is the weighted average of all the values. For the word it, a trained model can give a high weight to loan.

Every token does this at the same time, so the work is parallel. Multi-head attention runs several of these side by side, so different heads can follow different relationships. Position information is added, because attention itself ignores order. A transformer block is attention plus a small feed-forward network, with residual connections and layer normalisation that help deep stacks train. Models stack many blocks.

An encoder lets every token see every other token. That is ideal for understanding tasks such as classification and similarity. A decoder only looks at earlier tokens, and generates text, which is covered in the LLM apps course.

Kenji is an engineer at a legal-services firm in Osaka, Japan. The firm has hundreds of FAQ answers, and clients ask the same questions in different words. He wants the closest FAQ for each new question.

Keyword search fails here. How do I end my rental contract, and what is the process for terminating a lease, share almost no words. But an encoder gives each sentence a vector that reflects meaning.

His steps are short. Tokenise each sentence, run a small pretrained sentence encoder, and average the token vectors, using the attention mask so padding is ignored. That gives one vector per sentence.

Then he compares the vectors with cosine similarity. You should see something like a clearly higher score for the paraphrase than for an unrelated question about office hours. Kenji tests only with invented questions, never real client messages.

A common mistake is treating attention weights as a full explanation of a decision. They show where information flowed in one layer and one head. Use them as a rough hint, not proof. Another mistake is averaging token vectors without the attention mask. Padding then mixes into the sentence vector, and the result changes with the batch.

Let's recap. First, recurrent networks read one token at a time, which is slow and tends to lose early information. Second, attention lets every token weigh every other token in parallel, using queries, keys and values. Transformers stack attention and feed-forward layers. Third, encoders see the whole text at once, and suit classification and similarity.

Now it is your turn. In the exercise below this video, you will get sentence embeddings from a pretrained encoder, and compare five pairs of paraphrases with five unrelated pairs. It takes about twenty-five minutes. In the next lesson, we fine-tune a transformer for text classification. See you there.
```

## L13 Fine-Tuning a Transformer for Text Classification

- **Filename:** `ai-13-deep-learning-and-neural-networks_M3_L13_presenter.mp4`
- **Expected length:** about 4.8 minutes (670 words). The quality gate accepts ±10%.

```text
In lesson ten, you gave a pretrained image network a new head, and taught it bean diseases. The same idea works for text. With Hugging Face, the whole process, from raw dataset to evaluated model, fits in about thirty lines.

Fine-tuning a transformer for classification has five parts. First, the dataset. The datasets library loads public data from the Hub with its splits. You can take a shuffled subset, and split off a validation set from the training data.

Second, tokenisation in batches. The map method runs the tokenizer on many rows at once, and caches the result. Truncate to a maximum length that fits most texts. Padding happens later, per batch, with a data collator, which is faster.

Third, the model. The auto class for sequence classification loads the pretrained encoder and adds a new, random classification head. A warning that some weights are newly initialised is expected.

Fourth, the training arguments. They hold the learning rate, batch size, epochs, weight decay, and when to evaluate and save. Parameter names change between versions, so check them against your installed library. Fifth, the Trainer runs the loop from lesson five for you, and a metrics function reports accuracy and F1.

Unlike lesson ten, you usually fine-tune all layers of a small transformer, with a small learning rate, often around two to five times ten to the minus five, for a few epochs.

Think of an experienced translator who joins a new publishing house. They do not relearn the language. They spend a few days learning the house style. Fine-tuning is those few days. Small, careful adjustments to skills that are already there.

Joaquín is a data scientist at a news aggregator in Rosario, Argentina. He wants to sort English headlines into four topics. World, Sports, Business, and Science and Technology. He prototypes with AG News, a public topic dataset.

In Colab, he loads the dataset and takes small subsets, so training fits in free GPU time. Four thousand training examples, with twenty percent split off for validation, and two thousand test examples.

He loads the DistilBERT tokenizer, tokenises both splits with map, truncating at one hundred and twenty-eight tokens, and creates the model with four labels.

Next, a metrics function for accuracy and macro F1. Then the training arguments. A learning rate of three times ten to the minus five, two epochs, batches of thirty-two, evaluation and saving every epoch, and keep the best model at the end.

He builds the Trainer with the validation split as the evaluation set, and a data collator for padding. He trains, and then evaluates the test subset only once, at the end. He reports the accuracy and F1 he measured, and notes the subset sizes, because results on four thousand examples are not comparable with published results on the full dataset.

A common mistake is passing the test split as the evaluation set, with keep best model switched on. The Trainer then picks the checkpoint that is best on the test set, and the test score is too optimistic.

Use a validation split during training, and touch the test split once. And if you copy arguments from an old tutorial, you may get an unexpected keyword error. Check the names for your version.

Let's recap. First, load data with the datasets library, tokenise in batches with map, and pad per batch with a data collator. Second, the sequence classification model adds a new head to a pretrained encoder. Fine-tune all layers with a small learning rate for a few epochs. Third, choose checkpoints on a validation split, evaluate the test split once, and check argument names against your installed version.

Now it is your turn. In the exercise below this video, you will fine-tune a small pretrained model on a subset of AG News, and report accuracy and F1 on the test split. On a CPU, use one thousand training examples and shorter texts. It takes about forty-five minutes. In the next lesson, we learn to evaluate deep models properly. See you there.
```

## L14 Evaluating Deep Models Properly

- **Filename:** `ai-13-deep-learning-and-neural-networks_M3_L14_presenter.mp4`
- **Expected length:** about 5.0 minutes (694 words). The quality gate accepts ±10%.

```text
You change the learning rate, and accuracy goes up by one point. Is the new setting better? Run the old setting again with a different random seed, and it may move by one point on its own. So how much is just chance?

A quick recap from the scikit-learn course. Use three splits. Training to fit the weights. Validation to make choices, such as epochs and hyperparameters. And test, to measure the final choice once. Look beyond one number. A confusion matrix and per-class scores show which classes get confused.

Deep models add two reasons to be careful. First, randomness is everywhere. The seed controls the new layer's starting weights, the shuffling order, dropout and augmentation. Two runs with the same settings but different seeds can give noticeably different scores, especially on small datasets.

So run important settings with three or more seeds, and report the mean and the spread. If two settings' ranges overlap a lot, you have not shown that one is better.

Second, many choices use up the validation set. Every time you look at validation results and change something, you fit your decisions a little to that split. After many experiments, the validation score becomes optimistic. That is why the test set stays locked until the end.

Finally, error analysis turns a score into a plan. Collect the misclassified validation examples, read them, and group them. Wrong or unclear labels, examples that really belong to two classes, very short or unusual inputs, or a pattern the model has not learned.

One football match does not tell you which team is stronger. A lucky goal can decide it. A league of many matches is fairer. Several seeds are a small league for your models. And error analysis is watching the recording of the matches you lost.

Ayesha is an engineer at a non-profit in Dhaka, Bangladesh, that sorts English news summaries by topic for a media-monitoring project. She uses the AG News setup from the last lesson, and wants a result she can trust.

In Colab, she has wrapped her training code in a function that takes a seed and returns the validation predictions and labels. The function sets the seed everywhere, so each run can be repeated. The same seed always gives the same result.

She runs it with seeds zero, one and two, computes macro F1 for each, and prints the mean, standard deviation, minimum and maximum. This is the number she reports, not the best single run.

Next, a confusion matrix for one run, with the four topic names. Then she lists the first ten misclassified validation examples, with the true label, the predicted label, and the start of the text.

She reads them and groups them. Most errors are between Business and Science and Technology. Summaries about technology companies' earnings could fit either label. A few look mislabelled.

Her conclusion. A larger model may help a little, but the class definitions themselves overlap, and she writes this down as a limitation. Each error group points to a different fix. Clean the labels, change the class definitions, collect data, or change the model.

A common mistake is comparing two settings with one run each, when the difference is smaller than normal seed variation. Another is doing error analysis on the test set. It then becomes a second validation set, and the final score is no longer honest.

Do error analysis on validation data, and keep the test set for the final, single check.

Let's recap. First, keep separate validation and test splits. Make every choice on validation, and use test once, at the end. Second, run key settings with at least three seeds, and report the mean and spread before claiming that one is better. Third, read and group misclassified examples, to find whether the problem is the labels, the class definitions, the data or the model.

Now it is your turn. In the exercise below this video, you will run your text model with three seeds, report the mean and spread, and review ten misclassified examples to find a pattern. It takes about forty minutes. In the next lesson, we debug common training problems. See you there.
```

## L15 Common Training Problems and Fixes

- **Filename:** `ai-13-deep-learning-and-neural-networks_M3_L15_presenter.mp4`
- **Expected length:** about 4.9 minutes (681 words). The quality gate accepts ±10%.

```text
Your loss prints not a number at step eight. Or it never moves. Or memory runs out after ten minutes. Each looks like a disaster. But most have a small number of causes, and you can check them in a fixed order.

First, NaN or exploding loss. The loss grows fast, becomes infinity, then not a number. Usual causes are a learning rate that is too high, inputs with very large values, or an invalid operation. Normalise the inputs, lower the learning rate, and add gradient clipping between backward and step.

Second, vanishing gradients. The loss hardly moves, and the early layers' gradients are close to zero. Gradients are multiplied layer by layer on the way back, and sigmoid makes each factor small. Use ReLU, normalisation layers, residual connections, or fewer layers. Diagnose by printing each layer's gradient norm.

Third, the wrong loss for the label shape. Cross-entropy wants logits with one column per class, and integer labels. The binary loss wants float labels with the same shape as the logits. Fourth, out of memory. Use a smaller batch, and mixed precision, which runs most operations in sixteen-bit numbers. And do not keep graphs alive by accident.

Debugging is like a mechanic with a car that will not start. A good mechanic does not replace the engine first. They check the fuel, then the battery, then the spark plugs. Cheapest check first.

Here is the checklist. Read the full error, and print shapes, types and devices. Overfit one small batch. Check the loss and label format. Lower the learning rate by ten. Print gradient norms. Check memory per step.

Step two is a powerful test. A correct model and loop can reach almost zero loss on thirty-two examples. If yours cannot, the bug is in the code, not the settings.

Nguyen Thi Hoa is an engineer at a logistics firm in Da Nang, Vietnam. She inherits four broken notebooks. You can open the same four from the course page. For each one, she writes the symptom in one line before she changes anything.

Notebook A trains a linear model on raw inputs in the thousands. The loss explodes to infinity within a few steps, then becomes not a number. She standardises the inputs and targets, adds clipping, and the loss falls smoothly.

Notebook B stops with an error. The target size must match the input size. The logits have an extra column, and the labels are integers. She squeezes the logits and turns the labels into floats.

In Notebook C, the loss stays flat, near the level of random guessing. Twenty sigmoid layers make the gradients vanish. She prints each layer's gradient norm, and the first layer's is almost zero. With ReLU and batch normalisation, the gradients recover and the loss starts to fall.

In Notebook D, training runs, but memory keeps rising every step. The loop logs an extra loss as a tensor, and that graph was never used for backward, so it is never freed. Logging the plain number with item fixes it, and memory stays flat. Only if memory is still short, reduce the batch size or add mixed precision.

A common mistake is answering every problem by changing the learning rate or the architecture, without reading the error first. A missing zero grad, or a stored loss tensor, can look like a tuning problem. Follow the checklist, one change at a time.

Let's recap. First, NaN or exploding loss usually means a high learning rate or unscaled inputs. Normalise, lower the rate, and clip gradients. Second, vanishing gradients show as a flat loss and near-zero early gradients. Use ReLU, normalisation or fewer layers. Third, for memory problems, stop storing graphs, reduce the batch size and use mixed precision. And for any problem, follow a fixed checklist.

Now it is your turn. In the exercise below this video, you will debug the four broken notebooks yourself, and record the symptom, the cause, the fix and the evidence for each one. It takes about forty minutes. In the next lesson, we tune hyperparameters and learning-rate schedules. See you there.
```
