# L02 Embeddings: Meaning as Numbers | Presenter Script

Course: AI-15 · Video: 5 min · Words: 688

## Hook
How do I reset my password? I can't log in, I forgot my passcode. These two sentences share almost no words. A keyword search would not match them. Yet a good retrieval system must treat them as the same question.

## Explain
In the last lesson, we saw the six stages of RAG. Today we look at the stage that makes meaning searchable: embeddings.

An embedding model takes a piece of text and returns a vector, a fixed-length list of numbers, often a few hundred long. The model is trained so that texts with similar meanings get vectors that point in similar directions.

Similar meaning means similar direction. Different meaning means a different direction. That is the whole idea, and it is why embeddings can match two questions that share almost no words, like our password example.

Think of a large library where the librarian places each book on a map by topic, not by title. Books about river pollution end up near books about water treatment, even if their titles share no words.

An embedding places each text at a point on a map of meaning. We measure how close two points are with cosine similarity. It is close to one for very similar meaning, and near zero for unrelated text. If the vectors are normalised, it is simply the dot product. And it can even be negative.

Three practical points matter for RAG. Embed chunks and questions with the same model, because different models make different maps. Multilingual models place the same meaning in different languages close together. And some models expect a short prefix for queries and passages, so read the model card.

## Demonstrate
Let's try it in a notebook. We use the free, open-source sentence-transformers library, which runs locally. First we load a multilingual model that we chose on the model hub, after checking its card and its licence.

Next we write three sentences. The password question in English, the same question in French, and an unrelated sentence about an invoice. We encode them with normalised vectors, and multiply the matrix by itself to get every pairwise similarity.

You'll see something like this. The shape shows three vectors, each a few hundred numbers long, depending on the model. The English and French password sentences score high with each other, and both score low with the invoice sentence.

Now a real case. Farid builds a help assistant for a tour operator in Marrakesh. Guests write in Arabic, French and English, but the booking policies are only in French. He embeds three policy passages and three guest questions, one in each language, and prints a six by six matrix.

Each question scores highest with the matching French policy, even the Arabic one. But one pair surprises him. A question about bags on the bus scores almost as high with the transfer passage as with the luggage passage, because both mention the bus. Close topics can compete.

Farid learns that embeddings capture topic and meaning, but close topics can compete. He writes two notes for later. Add the section title to each chunk, which we cover in lesson five, and consider reranking, which we cover in lesson seven.

A common mistake is to treat a score as a fixed measure of truth, like anything above zero point seven is relevant. Scores are not comparable between models. Use them to rank results, and never mix vectors from two models in one index.

## Recap
Let's recap. First, an embedding model turns text into a vector, so that texts with similar meanings are close together, measured with cosine similarity. Second, chunks and questions must use the same model, and multilingual models can match across languages. Third, use similarity to rank passages, and choose any cut-off only by testing on your own data.

## CTA
Now it is your turn. In the exercise below, embed twelve sentences on four topics in English, French and Arabic, and plot a similarity heatmap. Look for the four bright blocks, and write a short, honest note on any weak matches. In the next lesson, Your First RAG Pipeline, we connect everything and get our first cited answer.

## Thumbnail
Headline: Meaning as Numbers
Image: Navy background, three short sentences in different scripts floating as dots that cluster together on a faint grid, headline in teal Inter Bold.

## Production Notes
- [VERSION] sentence-transformers API (SentenceTransformer, encode, normalize_embeddings) and current multilingual embedding model names: check at recording time. Do not say the model name in the voiceover; the screen shows whatever model is chosen.
- [VERIFY] Licence of the multilingual embedding model shown in the demo.
- The example output in content.md (shape 3 by 384, similarities 0.87 / 0.08 / 0.11) is illustrative. Record a real run and show its real numbers; the voiceover only says 'you'll see something like' and gives no exact values.
- Farid and the Marrakesh tour operator are hypothetical. Guest questions and policy passages are invented text, not personal data.
- The demo runs on a laptop CPU or in a free notebook environment; no paid API is used in this lesson.
