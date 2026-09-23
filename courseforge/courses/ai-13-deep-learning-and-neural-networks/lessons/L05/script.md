# L05 The Training Loop | Presenter Script

Course: AI-13 · Video: 5 min · Words: 690

## Hook
In scikit-learn, training is one line. You call fit. In PyTorch, you write the loop yourself. That sounds like extra work, but it is why PyTorch is so flexible. Every later lesson is a small change to the loop you write today.

## Explain
First, the data. A dataset answers two questions. How many examples are there, and what is example number i? For data already in tensors, a ready-made tensor dataset is enough. A data loader wraps it and gives you mini-batches, shuffled for training and in a fixed order for validation.

One step processes one batch and updates the weights once. One epoch is one full pass over the training data. With eight thousand examples and a batch size of sixty-four, one epoch has one hundred and twenty-five steps. Smaller batches give noisier but more frequent updates. Larger batches use the GPU better, but need more memory.

The core loop has five lines, always in this order. Clear the old gradients. Run the forward pass. Compute the loss. Compute the gradients with backward. Then let the optimiser update the weights.

Validation needs two switches. Eval mode changes how layers such as dropout behave. The no-grad block stops autograd from recording, which saves memory and time. You need both. Then switch back to train mode for the next epoch.

Think of a language class. Each batch is one lesson with a few exercises. The teacher marks them, explains each error, and the student adjusts. An epoch is the whole textbook once. Validation is a mock exam. There is no feedback, and the student does not study from it.

## Demonstrate
Folasade is a data scientist at a microfinance lender in Ibadan, Nigeria. She has a table of eight thousand loans with twenty features, and a logistic regression baseline. Does a small network do better? In the demo, a synthetic table stands in for her data.

She creates the synthetic data, splits it, and fits the scaler on the training part only, as in the scikit-learn course. Then she fits the logistic regression baseline and prints its validation score.

Next, she wraps the arrays in tensor datasets, with float features and long integer labels. The training loader uses batches of sixty-four and shuffles. The validation loader uses bigger batches and does not shuffle.

The model is small. Twenty inputs, sixty-four hidden units with ReLU, and two outputs. She moves it to the device, and chooses the Adam optimiser and cross-entropy loss.

Now the loop, for ten epochs. Train mode, then for each batch, the five lines. After that, eval mode and no grad, and she counts correct predictions on the validation set. Each epoch prints its validation accuracy.

She compares both scores on the same validation split. On data like this, you should see something like a network that is only slightly better, or about the same. Folasade records that honestly. The network costs more, so it must earn its place.

A common mistake is forgetting eval mode and no grad during validation, or forgetting to switch back to train mode. With dropout, scores look noisy and too low. Or the model trains with dropout switched off. Put train mode at the top of the training part, and eval mode with no grad around validation, every epoch. And never shuffle or augment the validation data in a way that changes it.

## Recap
Let's recap. First, a dataset returns single examples, and a data loader turns them into shuffled mini-batches. A step is one batch, and an epoch is one full pass. Second, the core loop is always zero grad, forward, loss, backward, step. Third, use train mode for training, eval mode with no grad for validation, and compare against a classical baseline on the same split.

## CTA
Now it is your turn. In the exercise below this video, you will write a full training and validation loop for a small tabular classifier, and compare it with a logistic regression on the same split. It takes about thirty-five minutes. In the next lesson, we move to images, with image data and transforms. See you there.

## Thumbnail
Headline: Five Lines That Train
Image: Navy background, a circular loop of five teal steps (zero_grad, forward, loss, backward, step) around a small network icon, headline in teal Inter Bold.

## Production Notes
- Review flags: none. content.md states no accuracy values. The voiceover gives no scores; it says the network may be only slightly better or about the same. Show whatever the notebook prints and do not add numbers in captions.
- The dataset is synthetic (make_classification); say so on screen. Folasade and the Ibadan microfinance lender are hypothetical; stock footage must not show a real company name or logo.
- Run the full cell once before recording. On CPU it finishes in well under a minute.
