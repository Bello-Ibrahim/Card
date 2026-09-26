# Screen Demo Pack: AI-13 L11 Turning Text into Numbers: Tokens and Embeddings

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 10

- **Filename:** `ai-13-deep-learning-and-neural-networks_L11_screen_1.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Show the xlm-roberta-base model card on the Hugging Face Hub (licence section)
2. Run: from transformers import AutoTokenizer; tok = AutoTokenizer.from_pretrained("xlm-roberta-base")
3. Run the sentences dictionary cell from content.md with keys en, fr, pt, ar

**Narration over this clip (for pacing)**

> In Colab, she loads the tokenizer for XLM-RoBERTa base, a multilingual model. She checks the licence on its Hub page first. Then she writes the train sentence in English, French, Portuguese and Arabic.

## Clip 2: scene 11

- **Filename:** `ai-13-deep-learning-and-neural-networks_L11_screen_2.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Run: for lang, text in sentences.items(): ids = tok(text)["input_ids"]; print(lang, len(ids), tok.convert_ids_to_tokens(ids))
2. Point to the special tokens at the start and end of each row
3. Highlight one word split into several pieces (expected output: similar but unequal counts)

**Narration over this clip (for pacing)**

> For each language, she prints the number of tokens and the tokens themselves. You should see something like sub-word pieces, with special tokens at the start and end, and counts that are similar, but not equal. She notes which words were split into several pieces.

## Clip 3: scene 12

- **Filename:** `ai-13-deep-learning-and-neural-networks_L11_screen_3.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Run: batch = tok(list(sentences.values()), padding=True, return_tensors="pt"); print(batch["input_ids"].shape, batch["attention_mask"][0])
2. Point to where the mask changes from 1 to 0 in a shorter row
3. Run: tok.decode(ids) for one sentence and compare with the original

**Narration over this clip (for pacing)**

> Then she tokenises all four sentences as one padded batch. Every row now has the same length, and the attention mask shows where the padding starts. She also decodes the IDs back to text, to confirm nothing was lost. This is exactly what the model will receive.

## Production notes for this lesson

- [VERSION] Check the Hugging Face tokenizer API (AutoTokenizer, padding, return_tensors, convert_ids_to_tokens) against the installed transformers version at recording time.
- [VERIFY] Licence of the xlm-roberta-base checkpoint must be confirmed on its Hub page before recording; show the model card briefly on screen.
- [VERIFY] The French, Portuguese and Arabic example sentences must be checked by a native speaker before recording (Arabic native-speaker check stays a human review item, see DECISIONS.md). Arabic captions use Noto Sans Arabic.
- Token counts are not stated in the voiceover; content.md only says they are similar but not equal. Show the real printed output.
- Layla and the Amman support company are hypothetical; use public example sentences only, never real customer messages.
