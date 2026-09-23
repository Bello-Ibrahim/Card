# L14 Cost, Latency and Deployment | Presenter Script

Course: AI-15 · Video: 5 min · Words: 677

## Hook
Your assistant is accurate, but each answer takes eight seconds, and your manager asks what it will cost for a thousand users. You cannot answer either question by guessing. You need to measure where the time and money go.

## Explain
In the last lesson, we made the assistant safe for real users. Now we make it fast enough and affordable, and then we put it online. Every choice today uses numbers, not guesses.

One query has four main stages. Optional rewriting is one small model call. Embedding the question is free when the model runs locally. Retrieval is fast, but a reranker adds time for every candidate. Generation is usually the largest share of both time and cost. Its cost depends on input tokens, the prompt plus chunks plus question, and output tokens, the answer.

Think of planning a delivery route. You time each part of the trip: loading, driving, and waiting at the door. Only then can you decide whether a bigger van, fewer stops or a different route saves the most time and fuel. Your pipeline works the same way.

Then use the levers you control. Top k: more chunks can raise recall, but also cost, time and distracting text. Ask for short answers with a sensible token limit. Cache the stable part of the prompt, such as the system instructions, so repeated requests process it more cheaply and often faster. Test a smaller model for simple steps. And stream answers, so users see the first words sooner.

## Demonstrate
Let's follow Tomás. He runs support tooling for an online electronics shop in Rosario, Argentina. His assistant answers staff questions about returns and warranties. First, he wraps his pipeline in a timing function. It times retrieval and generation separately, and reads the token counts from the API response.

One rule matters here. Prices change, so he reads them from configuration after checking the current pricing page. They are never written into the code. He runs twenty test questions at three settings: three, five and ten chunks. You'll see something like a table of timings, token counts and cost per query.

He adds his hit rate and faithfulness scores from the last two lessons. His example results: three chunks costs least, but misses answers that need two policies. Five chunks raises the hit rate clearly, for about forty percent more input tokens. Ten chunks adds almost nothing, but doubles the input tokens of five, and slows answers.

He chooses five chunks, turns on prompt caching for the system prompt, and limits answers to four hundred tokens. Caching needs just one small setting on the stable block. Caching has minimum lengths and its own prices, so check the current documentation before you rely on it.

Then he deploys. For a demo or internal tool, Streamlit gives a chat interface in a few lines. For a service that other systems call, a FastAPI endpoint wraps the same pipeline. He deploys a Streamlit app on an internal server for five support staff, with the API key kept on the server, never in the browser.

A common mistake is to measure only average latency and guess the cost. Averages hide slow queries. Report a slow case too, such as the ninetieth percentile, and calculate cost from the real usage numbers. Remember that real token counts include the system prompt, all the chunks and the rewriting step.

## Recap
Let's recap. First, generation usually dominates cost and time, local embeddings are free, and rerankers add time per candidate. Second, choose top k, chunk size, answer length and model size using your evaluation results together with measured cost and latency. Third, cache the stable part of the prompt, read prices and model names from configuration, and deploy with Streamlit or FastAPI.

## CTA
Now it is your turn. In the exercise below, measure latency and cost per query for three top k settings, try prompt caching, and choose one setting with a short justification. Keep these numbers, because your capstone report needs them. In the next lesson, Capstone Step One: Build Your RAG Assistant, you start your final project.

## Thumbnail
Headline: Where Time Goes
Image: Navy background, a stopwatch beside a horizontal bar split into four stages, with the generation stage largest in teal, headline in teal Inter Bold.

## Production Notes
- [VERSION] Claude API prices, usage fields (input_tokens, output_tokens), prompt caching syntax, minimum cacheable length and cache pricing, and model names. Prices are read from environment variables; never show or say a price or model ID. Blur any terminal line that shows them.
- [VERIFY] Realistic cost per learner (course-level flag).
- [VERSION] Streamlit, FastAPI and free hosting plan limits; the voiceover names no hosting provider.
- Timings, token counts and costs in the demo come from a real run; the voiceover says 'you'll see something like' and gives no values.
- Tomás's comparison (k=5 adds about 40% more input tokens than k=3; k=10 doubles the input tokens of k=5) is hypothetical; the slide carries a 'hypothetical results' label.
- Tomás and the Rosario electronics shop are hypothetical.
