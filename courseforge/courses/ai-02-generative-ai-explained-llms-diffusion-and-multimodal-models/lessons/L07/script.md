# L07 Multimodal Models: Text, Images and Audio Together | Presenter Script

Course: AI-02 · Video: 5 min · Words: 689

## Hook
You take a photo of a handwritten note, and seconds later the text appears neatly typed on your screen. You speak a question, and get a written answer. One tool understood a picture, a voice and a sentence. What kind of model does that?

## Explain
In the last two lessons, we worked with images. Most models so far use one type of data. A language model takes in text and gives text. A diffusion model takes in text and gives images. Each type of data, such as text, images, audio or video, is called a modality.

A multimodal model can take in, and sometimes produce, more than one modality. You upload a photo, chart or screenshot, and it describes it or copies out the text. You speak, and it writes down what you said. It can read its answer aloud. Or you give a photo and a question together, and it uses both.

These tools are very useful for turning messy real-world input into clean text. Think of a helpful colleague who can read your notes, look at your photos and listen to your voice messages, and then write a summary.

The colleague is fast and usually right, but sometimes misreads untidy handwriting. You would not send their summary to a client without checking it. Multimodal tools make typical mistakes too. They misread small, blurred or handwritten characters. They confuse numbers like one and seven. They skip a row, or fill in text that looks likely but is not there.

So you must check every value against the original. And think about safety. Photos often contain more personal information than you notice, such as names, addresses, card numbers or faces. Crop or cover these first, or use a sample document.

## Demonstrate
Let's see it in action. Diego owns a small hardware shop in Lima. His price list is handwritten on paper, and he wants a clean table he can paste into a spreadsheet.

First, he takes a clear photo in good light, straight from above, and crops out everything that is not the list. Then he opens Google AI Studio and starts a new chat. Claude or ChatGPT would also work.

He uses the upload button to add the photo. Then he types his request. Copy this price list into a table with the columns item, unit and price. And one important line. Do not guess. If a value is unclear, write unclear. That line gives the model permission to say it is not sure, instead of inventing a value.

He sends it, and a neat fifteen-row table comes back. It looks complete. But Diego does not trust the look. He places the table next to the photo and checks every row, one line at a time.

He finds two problems. A price of seventeen is really eleven in his handwriting. And one item is missing, because it was written at the edge of the paper. One value is marked unclear, which is helpful. He fixes them all.

Then he copies the corrected table into his spreadsheet. The task took minutes instead of an hour of typing. But it only worked because he checked it.

A common mistake is to trust a table because it looks neat and complete. A neat format says nothing about the values. The model predicts likely text from what it sees, so it can turn an unclear seven into a one. Ask it to mark unclear values, and check every one.

## Recap
Let's recap. First, a multimodal model can take in or produce more than one type of data, such as images, speech and text. Second, it can turn photos, charts and recordings into clean text or tables, but it can misread small or unclear details. Third, check every value against the original, and remove personal details before you upload.

## CTA
Now it is your turn. In the exercise below, upload a photo of a receipt, a timetable or a chart, ask for a table, and check every value against the original. Remember to cover any personal details first. It takes about twenty minutes. Next, we look at where each model type fails. See you there.

## Thumbnail
Headline: Photo In, Table Out
Image: Navy background, a photo of a handwritten price list on the left and a clean teal-lined table on the right, joined by an arrow, headline in teal Inter Bold.

## Production Notes
- Screen demo tool: Google AI Studio (named in the course brief), signed in with a clean demo Google account.
- [VERSION] Before recording, check that the free plan of Google AI Studio allows image upload, and the position of the upload or attach button. Claude and ChatGPT free plans are mentioned only as alternatives in the voiceover; check their upload options too.
- [VERIFY] content.md's conceptual description of how multimodal models work inside (images split into patches, audio into short pieces, all turned into a shared internal representation) is left out of the voiceover. It stays on the lesson page after review.
- Prop needed: a hypothetical handwritten price list for Diego's hardware shop, about 15 rows (Item, Unit, Price), with a price of 11.00 written so it can be misread as 17.00, one item written at the very edge of the paper, and one smudged value. No real shop name or personal data.
- The tool's real output may differ from content.md. If the live run does not show the 17.00 error, the missing edge item or an 'unclear' value, re-run with a less clear photo or adjust the voiceover in scene 11 to describe what actually appears. Do not fake the output.
- Diego and his Lima hardware shop are fictional.
