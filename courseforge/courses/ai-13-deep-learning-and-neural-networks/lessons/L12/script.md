# L12 From Sequences to Transformers | Presenter Script

Course: AI-13 · Video: 5 min · Words: 692

## Hook
The bank refused the loan because it was too risky. What does it refer to? You knew at once, because you saw the whole sentence together. Older networks read one word at a time. Transformers look at everything together.

## Explain
After the last lesson, a sentence is a sequence of token vectors, and order matters. The question is how to combine them into one meaning. Recurrent networks read the tokens one at a time. At each step, they update a hidden state, a summary of everything read so far.

This has two problems. It is slow, because step fifty cannot start until step forty-nine is finished, so a GPU's parallel units sit idle. And it is forgetful. Early information must pass through every later step, and over long texts it fades. LSTMs reduce this problem, but do not remove it.

An RNN is like passing a message down a line of people by whispering. It is slow, and details from the start are lost. Attention is like a meeting where everyone can hear everyone else at once, and each person decides who is worth listening to.

Here is attention in simple terms. Each token makes three vectors. A query, which is what it is looking for. A key, which is what it offers. And a value, the information it passes on. All three are learned from its embedding.

Then one token's query is compared with the keys of all tokens. Similar pairs get high scores. A softmax turns the scores into weights that add up to one. The token's new vector is the weighted average of all the values. For the word it, a trained model can give a high weight to loan.

Every token does this at the same time, so the work is parallel. Multi-head attention runs several of these side by side, so different heads can follow different relationships. Position information is added, because attention itself ignores order. A transformer block is attention plus a small feed-forward network, with residual connections and layer normalisation that help deep stacks train. Models stack many blocks.

An encoder lets every token see every other token. That is ideal for understanding tasks such as classification and similarity. A decoder only looks at earlier tokens, and generates text, which is covered in the LLM apps course.

## Demonstrate
Kenji is an engineer at a legal-services firm in Osaka, Japan. The firm has hundreds of FAQ answers, and clients ask the same questions in different words. He wants the closest FAQ for each new question.

Keyword search fails here. How do I end my rental contract, and what is the process for terminating a lease, share almost no words. But an encoder gives each sentence a vector that reflects meaning.

His steps are short. Tokenise each sentence, run a small pretrained sentence encoder, and average the token vectors, using the attention mask so padding is ignored. That gives one vector per sentence.

Then he compares the vectors with cosine similarity. You should see something like a clearly higher score for the paraphrase than for an unrelated question about office hours. Kenji tests only with invented questions, never real client messages.

A common mistake is treating attention weights as a full explanation of a decision. They show where information flowed in one layer and one head. Use them as a rough hint, not proof. Another mistake is averaging token vectors without the attention mask. Padding then mixes into the sentence vector, and the result changes with the batch.

## Recap
Let's recap. First, recurrent networks read one token at a time, which is slow and tends to lose early information. Second, attention lets every token weigh every other token in parallel, using queries, keys and values. Transformers stack attention and feed-forward layers. Third, encoders see the whole text at once, and suit classification and similarity.

## CTA
Now it is your turn. In the exercise below this video, you will get sentence embeddings from a pretrained encoder, and compare five pairs of paraphrases with five unrelated pairs. It takes about twenty-five minutes. In the next lesson, we fine-tune a transformer for text classification. See you there.

## Thumbnail
Headline: Everyone Hears Everyone
Image: Navy background, a sentence of word blocks with teal arcs connecting every word to every other word, one bold arc from 'it' to 'loan', headline in teal Inter Bold.

## Production Notes
- L12 is not a screen-demo lesson: concepts are taught with diagrams, and Kenji's code is shown as short code slides only.
- [VERIFY] Licence and intended use of the sentence-transformers/all-MiniLM-L6-v2 checkpoint must be confirmed on its Hub page. The voiceover says only 'a small pretrained sentence encoder'.
- [VERSION] Hugging Face AutoModel output field names (such as last_hidden_state) must be checked against the installed transformers version before the code slide is finalised.
- The similarity result is said as 'you should see something like' (content.md: expected output); no scores are stated.
- Kenji and the Osaka legal-services firm are hypothetical; use invented questions only, never real client messages.
