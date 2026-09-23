# L05 Chunking Strategies | Presenter Script

Course: AI-15 · Video: 5 min · Words: 696

## Hook
In lesson three, one answer failed because a chunk cut a table in half. Chunking looks like a small detail, but it decides what retrieval can find. Too small, and a chunk loses its meaning. Too large, and the answer hides among other topics.

## Explain
Welcome to week two. We start with chunking. A chunk is the unit you embed, retrieve and cite, so its size and shape matter at every later stage.

There are three common strategies. Fixed-size chunks cut every so many characters, with a small overlap. They are simple, but they can cut sentences and tables. Sentence-based chunks collect whole sentences up to a size limit. Structure-based chunks split by headings, so each chunk stays inside one topic. Short, factual FAQs often work well with small chunks. Long technical explanations often need larger ones.

One simple improvement helps all three. Add the document and section title to each chunk. A chunk that says only, the limit is thirty days, becomes, refund policy, online orders, the limit is thirty days. Now a question about refunds can find it.

Think of cutting a book into index cards for a study group. If each card holds half a sentence, nobody understands it. If each card holds a whole chapter, you cannot find the fact you need. Good cards hold one idea each, with the chapter title written at the top.

## Demonstrate
Here is a sentence-based chunker in plain Python. It splits the text into sentences, collects them until the next one would pass the size limit, and then starts a new chunk. It carries the last sentence into the next chunk as overlap, and puts the title at the front.

We run it on four short sentences about orders, returns and refunds, with the title Returns, Online, and a limit of sixty characters. We get three chunks. Each starts with the title, and each shares one sentence with its neighbour. So a fact near a boundary appears in two chunks, and is less likely to be lost.

But which size is best? There is no answer for every collection, so measure, do not guess. The simplest measure is hit at five: for each question, is a correct chunk in the top five results? In this tiny test, one of two questions finds its chunk, so the score is zero point five.

Now a real comparison. Mei-Lin maintains technical manuals for an equipment maker in Hsinchu, Taiwan. Engineers ask things like, what torque does the M4 bolt on the cooling plate need? She builds three Chroma collections, with chunks of three hundred, eight hundred and fifteen hundred characters, each with overlap and the section title.

Chunk IDs change when the size changes, so she labels each expected answer by document and a short phrase instead. Then, for ten test questions, she checks the top five chunks in each collection.

Here are her example results. The small chunks find six of ten, because they lost the name of the part, which was in the previous sentence. The large chunks find seven of ten, because they mixed several procedures. The middle size finds nine of ten. She chooses eight hundred, and writes down why, with the numbers.

A common mistake is to copy a chunk size from a tutorial and never test it. A size that works for news may fail for contracts. And measure retrieval directly, because a good prompt cannot fix a missing chunk.

## Recap
Let's recap. First, fixed-size, sentence-based and structure-based chunking each have trade-offs, and overlap protects facts near chunk boundaries. Second, adding the document and section title gives short chunks the context they need to be found. Third, choose chunk size by measuring a retrieval metric, such as hit at five, on your own test questions.

## CTA
Now it is your turn. In the exercise below, index your collection with three chunk sizes, and check ten test questions against each one. Make a small table of size, number of chunks and hit at five, and choose a size based on your numbers. In the next lesson, Vector Databases: Chroma and pgvector, we look closely at where these chunks live.

## Thumbnail
Headline: Cut It Right
Image: Navy background, a long document being cut into neat index cards, each card with a small teal title strip at the top, headline in teal Inter Bold.

## Production Notes
- [VERSION] chromadb and sentence-transformers APIs used in the exercise and the demo.
- The chunk_sentences output and the hit_at_k result are tested plain Python: the screen must show exactly the three lines in content.md ('Returns > Online: Orders ship in 2 days. Returns are free.' / 'Returns > Online: Returns are free. Refunds take 10 days.' / 'Returns > Online: Refunds take 10 days. Gift cards cannot be refunded.') and the value 0.5.
- Mei-Lin's results (6, 9 and 7 of 10) are hypothetical and illustrate the method only; the voiceover calls them example results. Show a 'hypothetical results' label on the table slide.
- Mei-Lin and the Hsinchu equipment maker are hypothetical; do not show a real company's manuals.
