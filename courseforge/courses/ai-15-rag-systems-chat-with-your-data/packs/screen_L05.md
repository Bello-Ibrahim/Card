# Screen Demo Pack: AI-15 L05 Chunking Strategies

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 6

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L05_screen_1.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Show the chunk_sentences function in a notebook cell.
2. Highlight the sentence split, the max_chars check, the overlap line cur = cur[-overlap:] and the title prefix.

**Narration over this clip (for pacing)**

> Here is a sentence-based chunker in plain Python. It splits the text into sentences, collects them until the next one would pass the size limit, and then starts a new chunk. It carries the last sentence into the next chunk as overlap, and puts the title at the front.

## Clip 2: scene 7

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L05_screen_2.mp4`
- **Target length:** about 24 seconds

**Steps**

1. Show the four-sentence text and run the loop with title 'Returns > Online' and max_chars=60.
2. Show the exact three printed chunks from content.md.
3. Highlight the repeated sentences 'Returns are free.' and 'Refunds take 10 days.'

**Narration over this clip (for pacing)**

> We run it on four short sentences about orders, returns and refunds, with the title Returns, Online, and a limit of sixty characters. We get three chunks. Each starts with the title, and each shares one sentence with its neighbour. So a fact near a boundary appears in two chunks, and is less likely to be lost.

## Clip 3: scene 8

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L05_screen_3.mp4`
- **Target length:** about 23 seconds

**Steps**

1. Show the hit_at_k function.
2. Show the results and expected dictionaries for q1 and q2.
3. Run print(hit_at_k(results, expected)) and show the output 0.5.

**Narration over this clip (for pacing)**

> But which size is best? There is no answer for every collection, so measure, do not guess. The simplest measure is hit at five: for each question, is a correct chunk in the top five results? In this tiny test, one of two questions finds its chunk, so the score is zero point five.

## Clip 4: scene 9

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L05_screen_4.mp4`
- **Target length:** about 23 seconds

**Steps**

1. Show the loop that creates three collections: chunks_300, chunks_800 and chunks_1500.

**Narration over this clip (for pacing)**

> Now a real comparison. Mei-Lin maintains technical manuals for an equipment maker in Hsinchu, Taiwan. Engineers ask things like, what torque does the M4 bolt on the cooling plate need? She builds three Chroma collections, with chunks of three hundred, eight hundred and fifteen hundred characters, each with overlap and the section title.

## Clip 5: scene 10

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L05_screen_5.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Show the test questions file: each question with an expected doc_id and a short answer phrase.
2. For each collection, retrieve the top 5 for the 10 questions and mark a hit if a chunk comes from the expected document and contains the phrase.

**Narration over this clip (for pacing)**

> Chunk IDs change when the size changes, so she labels each expected answer by document and a short phrase instead. Then, for ten test questions, she checks the top five chunks in each collection.

## Production notes for this lesson

- [VERSION] chromadb and sentence-transformers APIs used in the exercise and the demo.
- The chunk_sentences output and the hit_at_k result are tested plain Python: the screen must show exactly the three lines in content.md ('Returns > Online: Orders ship in 2 days. Returns are free.' / 'Returns > Online: Returns are free. Refunds take 10 days.' / 'Returns > Online: Refunds take 10 days. Gift cards cannot be refunded.') and the value 0.5.
- Mei-Lin's results (6, 9 and 7 of 10) are hypothetical and illustrate the method only; the voiceover calls them example results. Show a 'hypothetical results' label on the table slide.
- Mei-Lin and the Hsinchu equipment maker are hypothetical; do not show a real company's manuals.
