# Screen Demo Pack: AI-15 L02 Embeddings: Meaning as Numbers

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L02_screen_1.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Open a new notebook cell and show the import of SentenceTransformer from sentence_transformers.
2. Set EMBED_MODEL to the chosen multilingual model name and run model = SentenceTransformer(EMBED_MODEL).
3. Briefly show the model card page in the browser: vector size, prefixes, licence.

**Narration over this clip (for pacing)**

> Let's try it in a notebook. We use the free, open-source sentence-transformers library, which runs locally. First we load a multilingual model that we chose on the model hub, after checking its card and its licence.

## Clip 2: scene 9

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L02_screen_2.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Type the sentences list: 'How do I reset my password?', 'Comment réinitialiser mon mot de passe ?', 'The invoice is due in 30 days.'
2. Run vecs = model.encode(sentences, normalize_embeddings=True).
3. Run sims = vecs @ vecs.T, then print(vecs.shape) and print(sims.round(2)).

**Narration over this clip (for pacing)**

> Next we write three sentences. The password question in English, the same question in French, and an unrelated sentence about an invoice. We encode them with normalised vectors, and multiply the matrix by itself to get every pairwise similarity.

## Clip 3: scene 10

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L02_screen_3.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Show the printed shape and the 3 by 3 similarity matrix from the real run.
2. Highlight the high English–French cell and the two low invoice cells.

**Narration over this clip (for pacing)**

> You'll see something like this. The shape shows three vectors, each a few hundred numbers long, depending on the model. The English and French password sentences score high with each other, and both score low with the invoice sentence.

## Clip 4: scene 11

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L02_screen_4.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Show a cell with three French policy passages: cancellation, luggage, airport transfer.
2. Show three guest questions: English 'Can I cancel my tour?', an Arabic luggage question, a French airport shuttle question.
3. Encode all six with normalize_embeddings=True and print the 6 by 6 similarity matrix.

**Narration over this clip (for pacing)**

> Now a real case. Farid builds a help assistant for a tour operator in Marrakesh. Guests write in Arabic, French and English, but the booking policies are only in French. He embeds three policy passages and three guest questions, one in each language, and prints a six by six matrix.

## Clip 5: scene 12

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L02_screen_5.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Highlight the highest score in each question row, including the Arabic row.
2. Add the English question 'bags on the bus' and show its two close scores for luggage and transfer.

**Narration over this clip (for pacing)**

> Each question scores highest with the matching French policy, even the Arabic one. But one pair surprises him. A question about bags on the bus scores almost as high with the transfer passage as with the luggage passage, because both mention the bus. Close topics can compete.

## Production notes for this lesson

- [VERSION] sentence-transformers API (SentenceTransformer, encode, normalize_embeddings) and current multilingual embedding model names: check at recording time. Do not say the model name in the voiceover; the screen shows whatever model is chosen.
- [VERIFY] Licence of the multilingual embedding model shown in the demo.
- The example output in content.md (shape 3 by 384, similarities 0.87 / 0.08 / 0.11) is illustrative. Record a real run and show its real numbers; the voiceover only says 'you'll see something like' and gives no exact values.
- Farid and the Marrakesh tour operator are hypothetical. Guest questions and policy passages are invented text, not personal data.
- The demo runs on a laptop CPU or in a free notebook environment; no paid API is used in this lesson.
