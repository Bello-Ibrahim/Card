# L15 Capstone Step 1: Build Your RAG Assistant | Presenter Script

Course: AI-15 · Video: 5 min · Words: 683

## Hook
You have built every stage of a RAG system in separate exercises. Now you put them together, for real users and a real collection. The question changes from, does this technique work, to, would these people trust this assistant with their work?

## Explain
Welcome to your capstone. Step one, in this lesson, is the build. Step two, in the next lesson, is evaluation, improvement and the report. Everything you learned in the last fourteen lessons comes together here.

Choose the collection and the users together. For example, public health guidance for clinic staff in Kenya, or open-source documentation for developers in Brazil who ask in Portuguese. Check three things first. The licence allows your use. The collection has at least thirty documents, so retrieval is not trivial. And you can write questions that real users would ask.

Then combine what you built. Clean loading with metadata. Chunking with the size your evidence chose. Chroma or pgvector with filters. Hybrid retrieval with query rewriting. Grounded answers with validated citations and the I don't know reply. And a simple web interface with clickable sources.

Keep the project organised, so step two is easy. One file builds the index, one answers questions, and one is the interface. Put settings like chunk size, top k, the model name and prices in one configuration file, read from environment variables. Never write keys, model names or prices into the code.

Think of assembling a kitchen from parts you tested one by one. The oven works, the tap works, the fridge works. Now you connect them in one room for a specific cook, and you find problems that only appear when the parts work together.

## Demonstrate
Let's follow Wanjiru, a developer volunteering for a network of community clinics near Kisumu, Kenya. Clinic staff need quick answers from public health guidance, such as vaccination schedules and referral steps. She collects forty-five public guidance PDFs, records each link and licence, and runs her ingestion script. The log shows two scanned files skipped.

After a quick hit at five check, she chooses sentence chunks of about eight hundred characters, with section titles. She stores two thousand nine hundred chunks in Chroma, with metadata that includes the year, so answers prefer current guidance. She checks a few chunks by eye before moving on.

In the answering file, she connects hybrid retrieval, reranking and the grounded prompt, with a structured output for the answer, citations and the found flag. Then she builds the Streamlit app, with a notice at the top: the assistant supports, but does not replace, professional judgement.

She asks five realistic questions, including one in Kiswahili. You'll see something like short answers, each with clickable sources that show the title and page. Then she asks about a drug that is not in the guidance. The reply is exactly: I don't know. The documents do not contain this information.

Finally, she writes her open issues in a notes file. Tables in dosage charts are sometimes split, and two guidance versions overlap. These become her first candidates for improvement in step two. Writing issues down now saves time later, because the evaluation will show which one matters most.

A common mistake is a collection that is too small, so every metric looks perfect, or too big, so ingestion takes all week. Make the pipeline work end to end on a small part first.

## Recap
Let's recap. First, choose a real, licensed collection and a named user group together, and check that real users would ask questions it can answer. Second, combine the stages you built, from clean metadata to grounded, cited answers. Third, organise the code into ingestion, answering and interface files, with one configuration file. That makes step two much easier.

## CTA
Now it is your turn. This is capstone step one. In the exercise below, name your users and collection, then build the assistant with cited answers in a simple web interface. Test it with an unanswerable question and a follow-up, and record your open issues. In the final lesson, Capstone Step Two: Evaluate, Improve and Report, you prove how good it is.

## Thumbnail
Headline: Build Your RAG Assistant
Image: Navy background, six pipeline stage icons snapping together into one chat window with teal source links, headline in teal Inter Bold.

## Production Notes
- [VERIFY] Licence and reuse terms of the public health guidance used in Wanjiru's demo, and of the open-source documentation example. Confirm before recording, or use another collection whose licence is confirmed.
- [VERSION] Streamlit chat API (chat_input, chat_message) and all libraries used in the pipeline; Claude model choice read from config (check the current models page). Never say a model ID or price.
- Content check: content.md step 4 says 'a forced tool output'; L08 warns that some current models reject a forced tool_choice. The voiceover says 'structured output'. Record with the method that works at recording time. [VERSION]
- Health example: the Streamlit app on screen must show the notice that the assistant supports but does not replace professional judgement.
- The Kiswahili question shown on screen needs a native-speaker check before release.
- Wanjiru and the clinic network near Kisumu are hypothetical; the counts (45 PDFs, 2 skipped, 2,900 chunks) describe her example build. Answers on screen come from a real run and are introduced with 'you'll see something like'. The refusal sentence must match exactly: 'I don't know. The documents do not contain this information.'
- Stock footage of clinic staff must not show a real clinic name, logo or identifiable patients.
