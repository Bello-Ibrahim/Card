# L07 Multimodal Models: Text, Images and Audio Together

Course: AI-02 · Module: M2 · Objectives: O1, O4 · Video: 5 min (screen demo)

## Hook
You take a photo of a handwritten note and, a few seconds later, the text appears neatly typed on your screen. You speak a question into your phone and receive a written answer. The same tool understood a picture, a voice and a sentence. What kind of model can do all this?

## Explanation
Most models you have met in this course work with one type of data. A language model takes in text and produces text. A diffusion model takes in text and produces images. Each type of data, such as text, images, audio or video, is called a **modality**.

A **multimodal model** can take in, and sometimes produce, more than one modality. Common examples are:

- **Image to text:** you upload a photo, chart or screenshot, and the model describes it, answers questions about it or copies out the text in it.
- **Speech to text:** you speak, and the model writes down what you said or answers your question.
- **Text to speech:** the model reads its answer aloud in a generated voice.
- **Mixed conversations:** you give a photo and a written question together, and the model uses both.

Conceptually, a multimodal model turns each type of input into the same kind of internal representation, a common "language" of numbers. An image is split into small patches and a sound recording into short pieces, in a similar way to how text is split into tokens (L02). The model can then reason about all of them together and write its answer token by token, as a language model does. This description is simplified; tools are built in different ways. [VERIFY]

Multimodal tools are very useful for turning messy real-world input into clean, usable text. But they make typical mistakes. They can misread small, blurred or handwritten characters, confuse similar numbers (such as 1 and 7), skip a row in a table or "fill in" text that looks likely but is not in the image. So **you must check every value** against the original.

**Safety:** Photos and recordings often contain more personal information than you notice, such as names, addresses, card numbers or faces. Do not upload personal or confidential material to an AI tool. Crop or cover these details first, or use a sample document.

**Analogy:** A multimodal model is like a helpful colleague who can read your notes, look at your photos and listen to your voice messages, and then write you a summary. The colleague is fast and usually right, but they sometimes misread untidy handwriting. You would not send their summary to a client without checking it first.

## Worked Example
Diego owns a small hardware shop in Lima, Peru. His price list is handwritten on a sheet of paper, and he wants a clean table he can paste into a spreadsheet. This is a hypothetical case. A presenter can follow these steps on screen. [VERSION]

1. Take a clear photo of the price list in good light, straight from above. Crop out anything that is not the list.
2. Open a multimodal tool such as Google AI Studio, Claude or ChatGPT, and start a new chat. [VERSION]
3. Use the upload or attach button to add the photo. [VERSION]
4. Type: "Copy this price list into a table with the columns Item, Unit and Price. Do not guess: if a value is unclear, write 'unclear'."
5. Send the request and wait for the table.
6. Compare every row of the table with the photo, one line at a time.
7. Correct any mistakes, then copy the table into a spreadsheet.

The tool returns a 15-row table. Diego checks it and finds two problems: a price of "17.00" that is really "11.00" in his handwriting, and one item that is missing because it was written at the edge of the paper. One value is marked "unclear", which is helpful. After his corrections, the table is ready to paste. The task took minutes instead of an hour of typing, but only because he checked it.

## Common Mistake
Many learners trust a table from a photo because it looks neat and complete. A neat format says nothing about the accuracy of the values. The model predicts likely text from what it sees, so it can confidently turn an unclear "7" into a "1" or invent a missing value. The correction is simple: ask the model to mark unclear values, and always check every value against the original.

## Key Takeaways
1. A multimodal model can take in or produce more than one type of data, such as images, speech and text.
2. Multimodal tools are useful for turning photos, charts and recordings into clean text or tables, but they can misread small, blurred or handwritten details.
3. Check every value against the original, and remove personal or confidential details before you upload anything.

## Hands-on Exercise
**Task:** Upload a photo of a receipt, a timetable or a chart to a multimodal tool, ask for the content as a table, then check every value against the original.
**Tools:** Google AI Studio, Claude or ChatGPT (free plans) [VERSION]; a phone camera; a spreadsheet or notes app. File upload options differ between free plans.
**Steps:**
1. Choose a receipt, a public timetable or a chart. Cover or crop any personal details, such as names, card numbers or addresses.
2. Take a clear, straight photo in good light.
3. Upload it to the tool and ask: "Put the content of this image into a table. If a value is unclear, write 'unclear'."
4. Copy the result into a spreadsheet or notes app.
5. Check every value against the photo and highlight each error.
6. Count the correct values, the wrong values and the values marked "unclear".
**What good looks like:** A table next to the original photo, every error highlighted, and a one-line summary such as "24 values: 21 correct, 2 wrong (both small handwritten numbers), 1 marked unclear."
**Time:** about 20 minutes

## Review Flags
- [VERSION] File and image upload availability on the free plans of Google AI Studio, Claude and ChatGPT, and the position of the upload or attach button, must be checked before scripting the screen demo.
- [VERIFY] Confirm that the conceptual description of how multimodal models represent images and audio (patches and short pieces turned into a shared internal representation) is accurate enough for beginners and not tied to one provider.
