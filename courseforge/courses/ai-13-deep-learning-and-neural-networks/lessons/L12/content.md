# L12 From Sequences to Transformers

Course: AI-13 · Module: M3 · Objectives: O2 · Video: 5 min

## Hook
In the sentence "The bank refused the loan because it was too risky", what does "it" refer to? You answered at once, because you looked at the whole sentence together. Older networks had to read it one word at a time and remember. Transformers look at everything together, and that one change is behind most modern language models.

## Explanation
Text is a **sequence**: order matters. After L11, a sentence is a sequence of token vectors. The question is how to combine them into a meaning.

**Recurrent networks (RNNs)**, including LSTMs and GRUs, read tokens one at a time. At each step they update a **hidden state**, a summary of everything read so far. This has two problems:

- **Slow:** step 50 cannot start until step 49 is finished, so the work cannot be spread across a GPU's parallel units.
- **Forgetful:** information from early tokens must pass through every later step. Over long texts it fades, and gradients through many steps can vanish (L15). LSTMs reduce this but do not remove it.

**Attention** takes a different approach. For each token, the model asks: "Which other tokens in this text are relevant to me, and how much?" In simple terms:

1. Each token produces a **query** (what it is looking for), a **key** (what it offers) and a **value** (the information it passes on). All three are learned linear projections of its embedding.
2. The query of one token is compared with the keys of all tokens. Similar pairs get high scores. A softmax turns the scores into weights that add up to 1.
3. The token's new vector is the weighted average of all the values.

For "it" in the example, a trained model can give a high weight to "loan". Every token does this at the same time, so the computation is parallel. **Multi-head attention** runs several of these in parallel, so different heads can follow different relationships, such as grammar or meaning. Because attention itself ignores order, **positional information** is added to the token embeddings.

A **transformer block** is attention followed by a small feed-forward network, with residual connections and layer normalisation that help deep stacks train. Models stack many blocks.

**Encoders and decoders.** An **encoder** (for example BERT-style models) lets every token see every other token, which is ideal for understanding tasks such as classification and similarity. A **decoder** only looks at earlier tokens and is used to generate text; that is covered in AI-14. For classification, the encoder's output vectors are pooled into one sentence vector, and a small linear head predicts the class (L13).

**Analogy:** An RNN is like passing a message along a line of people by whispering: it is slow, and details from the start are lost. Attention is like a meeting where everyone can hear everyone else at once, and each person decides who is worth listening to for their own question.

## Worked Example
Kenji is an ML engineer at a hypothetical legal-services firm in Osaka, Japan. The firm has hundreds of FAQ answers, and clients ask the same questions in different words. He wants to find the closest FAQ for each new question.

A keyword search fails on "How do I end my rental contract?" compared with "What is the process for terminating a lease?", because they share almost no words. An encoder gives each sentence a vector that reflects meaning, so the two can have high cosine similarity.

Kenji's steps: take a small pretrained sentence encoder, tokenise each sentence, run the encoder, **mean-pool** the token vectors (ignoring padding with the attention mask), and compare vectors with cosine similarity.

```python
import torch
from transformers import AutoTokenizer, AutoModel

name = "sentence-transformers/all-MiniLM-L6-v2"     # [VERIFY] licence  [VERSION]
tok, enc = AutoTokenizer.from_pretrained(name), AutoModel.from_pretrained(name)

def embed(texts):
    b = tok(texts, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        h = enc(**b).last_hidden_state                # (N, tokens, dim)
    m = b["attention_mask"].unsqueeze(-1).float()
    return torch.nn.functional.normalize((h * m).sum(1) / m.sum(1), dim=1)

a = embed(["How do I end my rental contract?"])
b = embed(["What is the process for terminating a lease?", "What time does the office open?"])
print(a @ b.T)
```

The expected output is a clearly higher score for the paraphrase than for the unrelated question. Kenji tests only with invented example questions, never with real client messages.

## Common Mistake
Many learners believe attention weights are a reliable explanation of why the model made a decision. They show where information flowed in one layer and one head, not the full reasoning across many layers. Use them as a rough hint, not as proof. Another mistake is averaging token vectors without the attention mask, which mixes padding into the sentence vector and changes the result with batch composition.

## Key Takeaways
1. RNNs read one token at a time, which is slow to compute and tends to lose early information in long texts.
2. Attention lets every token weigh every other token in parallel using queries, keys and values; transformers stack attention and feed-forward layers.
3. Encoder models see the whole text at once and suit classification and similarity; pool their token vectors into one sentence vector.

## Hands-on Exercise
**Task:** Get sentence embeddings from a pretrained encoder and compute similarity scores for 5 pairs of paraphrases and 5 unrelated pairs.
**Tools:** Google Colab (free; CPU is enough); Hugging Face `transformers`; a small pretrained sentence encoder. Use invented sentences, not personal or confidential text.
**Steps:**
1. Load the encoder and check its licence and maximum input length on its Hub page. [VERIFY]
2. Write 5 paraphrase pairs and 5 unrelated pairs on one topic you know.
3. Embed all sentences with mean pooling and the attention mask, and compute cosine similarity for each pair.
4. Plot or list the 10 scores, sorted, with their pair type.
5. Find the lowest-scoring paraphrase pair and the highest-scoring unrelated pair, and suggest why each happened.
**What good looks like:** Ten scores where most paraphrase pairs score above most unrelated pairs, correct use of the attention mask, and a short, thoughtful analysis of the exceptions.
**Time:** about 25 minutes

## Review Flags
- [VERIFY] Licence and intended use of the `sentence-transformers/all-MiniLM-L6-v2` checkpoint must be confirmed on its Hub page.
- [VERSION] Hugging Face `AutoModel` output field names (such as `last_hidden_state`) must be checked against the installed `transformers` version.
