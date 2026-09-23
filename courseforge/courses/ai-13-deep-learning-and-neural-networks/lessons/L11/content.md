# L11 Turning Text into Numbers: Tokens and Embeddings

Course: AI-13 · Module: M3 · Objectives: O1, O2 · Video: 5 min (screen demo)

## Hook
Write "The train leaves the station at eight in the morning" in English, French, Portuguese and Arabic. A person sees four sentences of similar length. A tokenizer may see four quite different numbers of pieces, and that affects cost, speed and sometimes accuracy.

## Explanation
A neural network needs numbers, so text goes through two steps.

**1. Tokenisation** splits text into **tokens** and maps each one to an integer **ID** from a fixed **vocabulary**. Modern models use **sub-word** tokenisers (for example BPE, WordPiece or SentencePiece). Common words stay whole; rare or long words are split into pieces, such as "un", "believ", "able". This keeps the vocabulary to tens of thousands of entries while still handling any word, including names and spelling mistakes.

A Hugging Face tokenizer also:

- adds **special tokens** that the model expects, such as a start token and an end or separator token;
- **pads** shorter texts and **truncates** longer ones in a batch, and returns an **attention mask** (1 for real tokens, 0 for padding).

Every pretrained model has its own tokenizer. Always load them together from the same checkpoint name.

**Why counts differ by language.** A tokenizer's vocabulary is learned from its training text. Languages and scripts that were common in that text get more whole-word tokens; others are split into more pieces. A multilingual tokenizer is more balanced, but counts still differ. More tokens mean more compute, and the text fills the model's maximum length sooner.

**2. Embeddings.** An **embedding layer** (`nn.Embedding(vocab_size, dim)`) is a lookup table: row `i` is a learned vector for token `i`. It is trained with the rest of the network by backpropagation (L04), so tokens used in similar contexts end up with similar vectors. You measure closeness with **cosine similarity**. In a transformer (L12), these vectors are then updated by context, so the same word can get different vectors in different sentences.

**Analogy:** Tokenisation is like a library giving every book a shelf code, and splitting a very long encyclopedia into several volumes, each with its own code. Embeddings are like arranging the shelves so that books on similar subjects stand near each other. The codes are arbitrary numbers; the positions on the shelves carry the meaning.

## Worked Example
Layla is an NLP engineer at a hypothetical customer-support company in Amman, Jordan, that answers messages in several languages. Before choosing a model, she checks how a multilingual tokenizer handles one sentence in four languages.

**Screen demo steps:**

1. Load a multilingual tokenizer. [VERSION] [VERIFY] Check the checkpoint's licence on its Hub page.
2. Tokenise the four sentences and print the tokens and counts.
3. Decode the IDs back to text to confirm nothing was lost.

```python
from transformers import AutoTokenizer

tok = AutoTokenizer.from_pretrained("xlm-roberta-base")      # [VERIFY] licence
sentences = {
    "en": "The train leaves the station at eight in the morning.",
    "fr": "Le train quitte la gare à huit heures du matin.",
    "pt": "O trem sai da estação às oito horas da manhã.",
    "ar": "القطار يغادر المحطة في الساعة الثامنة صباحًا.",
}
for lang, text in sentences.items():
    ids = tok(text)["input_ids"]
    print(lang, len(ids), tok.convert_ids_to_tokens(ids))

batch = tok(list(sentences.values()), padding=True, return_tensors="pt")
print(batch["input_ids"].shape, batch["attention_mask"][0])
```

The expected output is a list of sub-word tokens for each language, with special tokens at the start and end, and counts that are similar but not equal. Layla notes which words are split into several pieces. She also checks the padded batch: all rows have the same length, and the attention mask shows where the padding starts. She uses public example sentences only and never pastes real customer messages into a notebook or an online tool.

## Common Mistake
Many learners load a tokenizer from one checkpoint and a model from another, for example a multilingual tokenizer with an English-only model. The code runs, because IDs are just integers, but each ID now points to the wrong embedding row, and the model receives nonsense. Always load both with the same checkpoint name. A second mistake is counting words instead of tokens when estimating length limits; use the tokenizer to count.

## Key Takeaways
1. Tokenisers split text into sub-word tokens with IDs, add special tokens, and pad or truncate batches with an attention mask.
2. The same sentence can produce different token counts in different languages, which affects compute and maximum length.
3. An embedding layer is a learned lookup table from token IDs to vectors, where tokens used in similar contexts end up close together.

## Hands-on Exercise
**Task:** Tokenise the same sentence in English, French, Portuguese and Arabic with a multilingual tokenizer, and compare the tokens and counts.
**Tools:** Google Colab (free; CPU is enough); Hugging Face `transformers`. Do not paste personal or confidential text; use your own neutral sentences.
**Steps:**
1. Load a multilingual tokenizer from the Hub and note its checkpoint name and licence. [VERSION] [VERIFY]
2. Write one neutral sentence and its translation into French, Portuguese and Arabic (or other languages you know).
3. Print the tokens and the token count for each, and decode the IDs back to text.
4. Tokenise all four as one padded batch and inspect `input_ids` and `attention_mask`.
5. Load an English-only tokenizer and compare the counts for the same four sentences.
6. Write a short table and two sentences on what the differences mean for cost and maximum length.
**What good looks like:** A table of tokens and counts for both tokenizers, correct reading of special tokens and the attention mask, and a clear explanation that is based on your own output.
**Time:** about 25 minutes

## Review Flags
- [VERSION] Hugging Face tokenizer API (`AutoTokenizer`, call options such as `padding` and `return_tensors`, and `convert_ids_to_tokens`) must be checked against the installed `transformers` version.
- [VERIFY] Licence of the `xlm-roberta-base` checkpoint and of any English-only tokenizer used in the exercise; the Arabic, French and Portuguese example sentences should be checked by a native speaker.
