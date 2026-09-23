# L02 Embeddings: Meaning as Numbers

Course: AI-15 · Module: M1 · Objectives: O2 · Video: 5 min (screen demo)

## Hook
"How do I reset my password?" and "I can't log in, I forgot my passcode" share almost no words. A keyword search would not match them. Yet a good retrieval system must treat them as the same question. Embeddings make this possible.

## Explanation
An **embedding model** takes a piece of text and returns a **vector**: a fixed-length list of numbers, often a few hundred long. The model is trained so that texts with similar meanings get vectors that point in similar directions, and texts with different meanings get vectors that point in different directions.

We measure "similar direction" with **cosine similarity**. For two vectors *a* and *b* it is the dot product divided by the product of their lengths. The result is close to 1 for very similar meaning, near 0 for unrelated text, and it can be negative. If you ask the model to **normalise** the vectors (make each one length 1), cosine similarity is simply the dot product, which is fast to compute.

**Analogy:** Think of a large library where the librarian places each book on a map of the building by topic, not by title. Books about river pollution end up near books about water treatment, even if their titles share no words. An embedding places each text at a point on a map of meaning, and cosine similarity measures how close two points are.

Three practical points matter for RAG:

- **Same model for chunks and questions.** Vectors from different models live on different maps and cannot be compared.
- **Multilingual models** are trained so that the same meaning in different languages lands close together. A question in French can then find a passage in English. This is useful for collections and users in several languages.
- **Asymmetric search.** Some models expect a short prefix to mark a text as a query or a passage. Read the model card: if it asks for prefixes and you skip them, quality drops.

We use the open-source **sentence-transformers** library, which runs locally for free, on a laptop CPU or in a free notebook environment. [VERSION]

```python
from sentence_transformers import SentenceTransformer

# Choose a multilingual model from the model hub and check its card and licence.
EMBED_MODEL = "your-multilingual-embedding-model"  # [VERSION] [VERIFY licence]
model = SentenceTransformer(EMBED_MODEL)

sentences = ["How do I reset my password?",
             "Comment réinitialiser mon mot de passe ?",
             "The invoice is due in 30 days."]
vecs = model.encode(sentences, normalize_embeddings=True)
sims = vecs @ vecs.T  # cosine similarity, because vectors are normalised
print(vecs.shape)
print(sims.round(2))
```

Example output (numbers depend on the model):

```
(3, 384)
[[1.   0.87 0.08]
 [0.87 1.   0.11]
 [0.08 0.11 1.  ]]
```

The English and French password sentences score high with each other and low with the invoice sentence. The vector length (384 here) depends on the model you choose.

## Worked Example
Farid builds a help assistant for a hypothetical tour operator in Marrakesh, Morocco. Guests write in Arabic, French and English, but the booking policies are written only in French.

He embeds three policy passages (cancellation, luggage, and airport transfer) and three guest questions, one in each language: "Can I cancel my tour?" in English, a question about luggage in Arabic, and a question about the airport shuttle in French. He then prints a 6-by-6 similarity matrix.

Each question scores highest with the matching French policy, even the Arabic one. One pair surprises him: an English question about "bags on the bus" scores almost as high with the transfer passage as with the luggage passage. Both passages mention the bus. Farid learns that embeddings capture topic and meaning, but close topics can compete. He notes that later he should add the section title to each chunk (L05) and consider reranking (L07).

## Common Mistake
Learners often treat a similarity score as a fixed measure of truth, for example "anything above 0.7 is relevant". Scores are not comparable between models, and even within one model the typical range depends on the language and text length. Use similarity to **rank** results, and set any cut-off only after testing it on your own questions. Also, do not mix vectors from two different models in one index; the results will look random.

## Key Takeaways
1. An embedding model turns text into a vector so that texts with similar meanings are close together, which we measure with cosine similarity.
2. Chunks and questions must be embedded with the same model; multilingual models can match a question and a passage in different languages.
3. Use similarity scores to rank passages, not as an absolute truth score, and choose any threshold by testing on your own data.

## Hands-on Exercise
**Task:** Embed 12 sentences in English, French and Arabic with an open-source multilingual model, and plot a similarity heatmap.
**Tools:** Python 3 with sentence-transformers and matplotlib (free), locally or in a free notebook environment. [VERSION]
**Steps:**
1. Install the libraries: `pip install sentence-transformers matplotlib`.
2. Choose a multilingual model on the model hub. Read its card: note the vector size, any query or passage prefixes, and the licence. [VERIFY]
3. Write 4 short sentences on 4 different topics, for example weather, banking, cooking and sport. Translate each into French and Arabic, so you have 12 sentences. Use invented text, not personal data.
4. Encode them with `normalize_embeddings=True` and compute `sims = vecs @ vecs.T`.
5. Plot the matrix with `plt.imshow(sims)`, label both axes with short sentence names, and add a colour bar.
6. On screen, point out the four bright blocks where the same topic appears in three languages.
7. Write 3 sentences: which pairs matched well, which did not, and one possible reason.
**What good looks like:** A labelled 12-by-12 heatmap where same-topic sentences in different languages have clearly higher similarity than different-topic sentences, and a short, honest note on any weak matches.
**Time:** about 30 minutes

## Review Flags
- [VERSION] sentence-transformers API (`SentenceTransformer`, `encode`, `normalize_embeddings`) and the names of current multilingual embedding models must be checked at recording time. The vector size of 384 in the example output is illustrative.
- [VERIFY] Licence of the multilingual embedding model shown in the demo.
- Example output numbers are illustrative and must be replaced with real output from the recorded run.
