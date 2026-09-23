# L11 Turning Text into Numbers: Tokens and Embeddings | Presenter Script

Course: AI-13 · Video: 5 min · Words: 690

## Hook
Write one sentence about a morning train in English, French, Portuguese and Arabic. You see four sentences of similar length. A tokenizer may see quite different numbers of pieces, and that affects cost, speed and sometimes accuracy.

## Explain
Welcome to module three, where we work with text. A network needs numbers, so text goes through two steps. The first is tokenisation. It splits text into tokens, and maps each token to a whole-number ID from a fixed vocabulary.

Modern models use sub-word tokenisers. Common words stay whole. Rare or long words are split into pieces, such as un, believ and able. This keeps the vocabulary to tens of thousands of entries, while still handling any word, including names and spelling mistakes.

A Hugging Face tokenizer also adds the special tokens the model expects, at the start and the end. In a batch, it pads short texts and cuts long ones, and returns an attention mask. One for real tokens, zero for padding. Every model has its own tokenizer, so always load them together.

Why do counts differ by language? A tokenizer learns its vocabulary from its training text. Languages and scripts that were common there get more whole-word tokens. Others are split into more pieces. More tokens mean more compute, and the text fills the model's maximum length sooner.

The second step is embeddings. An embedding layer is a lookup table. Row i is a learned vector for token i. It is trained with the rest of the network, so tokens used in similar contexts end up with similar vectors. You measure closeness with cosine similarity.

In a transformer, which we meet next, these vectors are then updated by context, so one word can get different vectors in different sentences.

Think of a library. Tokenisation gives every book a shelf code, and splits a very long encyclopedia into several volumes. Embeddings arrange the shelves so that books on similar subjects stand near each other. The codes are arbitrary. The positions carry the meaning.

## Demonstrate
Layla is an NLP engineer at a customer-support company in Amman, Jordan, that answers messages in several languages. Before choosing a model, she checks how a multilingual tokenizer handles one sentence in four languages.

In Colab, she loads the tokenizer for XLM-RoBERTa base, a multilingual model. She checks the licence on its Hub page first. Then she writes the train sentence in English, French, Portuguese and Arabic.

For each language, she prints the number of tokens and the tokens themselves. You should see something like sub-word pieces, with special tokens at the start and end, and counts that are similar, but not equal. She notes which words were split into several pieces.

Then she tokenises all four sentences as one padded batch. Every row now has the same length, and the attention mask shows where the padding starts. She also decodes the IDs back to text, to confirm nothing was lost. This is exactly what the model will receive.

Layla uses public example sentences only. She never pastes real customer messages into a notebook or an online tool.

A common mistake is loading the tokenizer from one checkpoint and the model from another, for example a multilingual tokenizer with an English-only model. The code runs, because IDs are just numbers, but each ID now points to the wrong embedding row. Always use the same checkpoint name. And count tokens, not words, when you check length limits.

## Recap
Let's recap. First, tokenisers split text into sub-word tokens with IDs, add special tokens, and pad or truncate batches with an attention mask. Second, the same sentence can produce different token counts in different languages, which affects compute and maximum length. Third, an embedding layer is a learned lookup table from token IDs to vectors, where tokens used in similar contexts end up close together.

## CTA
Now it is your turn. In the exercise below this video, you will tokenise your own neutral sentence in English, French, Portuguese and Arabic, and compare the tokens and counts. It takes about twenty-five minutes. In the next lesson, we go from sequences to transformers. See you there.

## Thumbnail
Headline: Same Sentence, Different Tokens
Image: Navy background, one short sentence shown in four scripts, each broken into coloured token blocks of different counts, headline in teal Inter Bold.

## Production Notes
- [VERSION] Check the Hugging Face tokenizer API (AutoTokenizer, padding, return_tensors, convert_ids_to_tokens) against the installed transformers version at recording time.
- [VERIFY] Licence of the xlm-roberta-base checkpoint must be confirmed on its Hub page before recording; show the model card briefly on screen.
- [VERIFY] The French, Portuguese and Arabic example sentences must be checked by a native speaker before recording (Arabic native-speaker check stays a human review item, see DECISIONS.md). Arabic captions use Noto Sans Arabic.
- Token counts are not stated in the voiceover; content.md only says they are similar but not equal. Show the real printed output.
- Layla and the Amman support company are hypothetical; use public example sentences only, never real customer messages.
