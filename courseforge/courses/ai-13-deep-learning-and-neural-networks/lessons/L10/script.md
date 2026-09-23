# L10 Transfer Learning with Pretrained CNNs | Presenter Script

Course: AI-13 · Video: 5 min · Words: 690

## Hook
You have about a thousand labelled photos of bean leaves. That is far too few to train a deep CNN from scratch. But what if a network that has already seen a huge number of everyday photos only had to learn the last step?

## Explain
This is transfer learning. You reuse a network trained on a large dataset, such as ImageNet, for a new task. Its early and middle layers have learned general visual features, like edges, textures and shapes, that are useful for almost any photo. Only the last layer is specific to its original one thousand classes.

The recipe has two stages. First, feature extraction. Load the pretrained model, freeze the backbone so its weights do not change, replace the final layer with a new one for your classes, and train only that new layer. It is fast, and it needs little data.

Second, fine-tuning. Unfreeze the last block or two, and train them together with the new layer, with a smaller learning rate for the pretrained part. You adjust its features gently, instead of destroying them.

Think of an experienced chef learning a new cuisine. The chef already knows how to cut, season and control heat. Feature extraction is following new recipes with old skills. Fine-tuning is carefully adjusting a few techniques as well.

Two details are easy to miss. Preprocess images exactly the way the model was trained, and in torchvision, the weights object gives you those transforms. And use the newer weights argument. Older tutorials use a different option that newer versions no longer support. Pretrained checkpoints also have their own licences, so check them before you use a model in a product.

## Demonstrate
Grace is a data scientist at an agricultural extension service in Mbale, Uganda. Farmers send her leaf photos, and she wants to classify them as healthy, angular leaf spot or bean rust. She uses a public bean-leaf dataset from the Hugging Face Hub.

In Colab, she loads ResNet eighteen with its default pretrained weights, and freezes every parameter. Then she replaces the final layer with a new one that has three outputs. Only this new head can learn. Everything else keeps what it learned before.

She counts the trainable parameters. Only one thousand five hundred and thirty-nine, which is five hundred and twelve features times three classes, plus three biases. So each epoch is fast, even on a CPU.

Next, she loads the dataset and applies the pretrained model's own transforms to every image. A small collate function stacks the images and labels into batches of thirty-two.

Stage one trains only the head for a few epochs. For stage two, she unfreezes the last block, and builds a new optimiser with two learning rates. A small one for the pretrained block, and a larger one for the head.

Grace compares three runs on the validation split. Her CNN trained from scratch, the frozen ResNet, and the fine-tuned ResNet. You should see something like both pretrained runs doing clearly better on this small dataset. She reports her own measured numbers.

A common mistake is changing what is trainable, but forgetting to rebuild the optimiser. Build the optimiser after you set which layers learn, and print the trainable count. Also, never use your own normalisation values, such as the Fashion-MNIST ones, with a pretrained model. Its features would then receive inputs in a range they never saw during pretraining.

## Recap
Let's recap. First, transfer learning reuses a pretrained backbone's general features. Freeze it, replace the final layer, and train the new head first. Second, fine-tune a few top layers afterwards with a smaller learning rate, and rebuild the optimiser whenever you change what is trainable. Third, preprocess with the pretrained weights' own transforms, and check the licences of both the checkpoint and the dataset.

## CTA
Now it is your turn. In the exercise below this video, you will fine-tune a pretrained ResNet on the bean-leaf dataset, and compare it with your CNN trained from scratch. It takes about forty-five minutes. In the next module, we move to text, starting with tokens and embeddings. See you there.

## Thumbnail
Headline: Teach Only the Last Step
Image: Navy background, a large grey pretrained network with a lock icon and a small bright teal final layer, next to a green bean leaf, headline in teal Inter Bold.

## Production Notes
- [VERSION] torchvision weights API: weights= and ResNet18_Weights.DEFAULT replaced pretrained=True in newer versions. Check against the Colab version at recording time.
- [VERIFY] Bean-leaf disease dataset: Hub dataset ID (AI-Lab-Makerere/beans in content.md), source (collected in Uganda), class names (healthy, angular leaf spot, bean rust) and licence must be confirmed on the Hub page before recording. The voiceover does not state the dataset's origin or licence as fact.
- [VERIFY] Licence of the ImageNet-pretrained ResNet-18 checkpoint. The voiceover only tells learners to check checkpoint licences.
- Results are said as 'you should see something like' (content.md: expected result). Show Grace's three real validation scores; do not add numbers in captions.
- The trainable-parameter count 1,539 (512 × 3 + 3) must match the printed output.
- Grace and the Mbale extension service are hypothetical; stock footage must not show a real organisation's name or logo.
