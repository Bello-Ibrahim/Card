# L09 Regularisation: Dropout, Weight Decay and Early Stopping | Presenter Script

Course: AI-13 · Video: 5 min · Words: 681

## Hook
In the last lesson, the validation loss started to rise while the training loss kept falling. The model was learning the training set too well. Today, you add three tools that make it learn the pattern, not the details.

## Explain
Regularisation is any change that helps a model do better on new data, usually at some cost to its training score. In the scikit-learn course, you met penalties for linear models. Deep networks use the same idea, plus a few of their own.

Dropout randomly switches off a fraction of the units in each training step, and scales up the rest. The network cannot rely on any single unit, so it learns features that are more spread out and more robust. It is active only in train mode. In eval mode, it does nothing. Typical rates are between ten and fifty percent.

Weight decay shrinks every weight a little at each step. This keeps the weights small and the function smoother. It is the deep-learning version of an L2 penalty. With Adam, use the AdamW optimiser, which applies the decay separately.

Early stopping watches the validation loss after every epoch. It saves a copy of the weights whenever the loss improves, and stops when there has been no improvement for a set number of epochs, called the patience. Then you reload the best copy. It also saves GPU time. And remember, augmentation is a regulariser too, often the strongest one for images.

Think of a student who practises with one set of past exam questions. They can memorise the answers and still fail a new exam. A student who practises with different questions, sometimes with parts hidden, must learn the method.

Dropout hides parts of the question. Weight decay stops the student from building very complicated rules. And early stopping is the teacher saying, stop now, you are starting to memorise.

## Demonstrate
Hamid is an engineer at an argan-oil cooperative in Agadir, Morocco. His quality-check CNN overfits after a few epochs. Let's add all three tools in Colab.

First, he adds a dropout layer with a rate of zero point three, just before the final linear layer. Then he switches the optimiser to AdamW, with a weight decay of zero point zero one.

Next, the early-stopping block around his loop from lesson five, with a patience of three. After each epoch, if the validation loss improves, he saves a deep copy of the weights. If not, he counts a bad epoch, and after three in a row, he stops.

At the end, he loads the best weights back into the model. Then he runs two experiments with the same data, seed and learning rate. The original model, and the regularised one.

He plots both validation curves on one chart. You should see something like this. The regularised model's validation loss stays lower for longer, and the gap between training and validation gets smaller. He compares the best scores, not the final ones, and records both runs in a small table.

A common mistake is saving the best model without a real copy. That only stores links to the live weights, which keep changing. At the end, best is simply the last model. Use a deep copy, or save to a file. And add regularisers one at a time, or you cannot tell which one helped.

## Recap
Let's recap. First, dropout switches off random units during training only, and weight decay keeps weights small. Both reduce overfitting, at some cost to the training fit. Second, early stopping keeps the checkpoint with the best validation loss, and stops after a set number of epochs without improvement. Third, judge each regulariser by comparing validation curves across runs that change one thing at a time.

## CTA
Now it is your turn. In the exercise below this video, you will add dropout and weight decay to your own CNN, use early stopping, and compare the validation curves before and after. It takes about forty minutes. In the next lesson, we save a lot of training time with transfer learning and pretrained CNNs. See you there.

## Thumbnail
Headline: Stop Memorising, Start Generalising
Image: Navy background, a network diagram with a few nodes greyed out, a small shield icon and a stop sign shape, headline in teal Inter Bold.

## Production Notes
- Review flags: none. Hyperparameter ranges (dropout 0.1 to 0.5, weight decay about 1e-4 to 1e-2) are starting points for tuning, not claims about results.
- The comparison result is said as 'you should see something like' (content.md: expected result). Show the real curves from the two runs; do not add numbers in captions.
- train_one_epoch and evaluate are the learner's own helpers from L05; define them in a hidden cell above the demo cell before recording.
- Hamid and the Agadir argan-oil cooperative are hypothetical; stock footage must not show a real company name or logo.
