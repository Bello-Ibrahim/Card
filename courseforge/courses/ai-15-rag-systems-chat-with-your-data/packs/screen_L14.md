# Screen Demo Pack: AI-15 L14 Cost, Latency and Deployment

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 6

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L14_screen_1.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Show timed_answer: perf_counter around col.query and around client.messages.create.
2. Highlight msg.usage.input_tokens and output_tokens and the cost formula.
3. Show PRICE_IN and PRICE_OUT read from environment variables (values blurred).

**Narration over this clip (for pacing)**

> Let's follow Tomás. He runs support tooling for an online electronics shop in Rosario, Argentina. His assistant answers staff questions about returns and warranties. First, he wraps his pipeline in a timing function. It times retrieval and generation separately, and reads the token counts from the API response.

## Clip 2: scene 7

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L14_screen_2.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Run the 20 test questions at k=3, k=5 and k=10 with timed_answer.
2. Show the results table from the real run: median and slowest latency, average input and output tokens, cost per query.

**Narration over this clip (for pacing)**

> One rule matters here. Prices change, so he reads them from configuration after checking the current pricing page. They are never written into the code. He runs twenty test questions at three settings: three, five and ten chunks. You'll see something like a table of timings, token counts and cost per query.

## Clip 3: scene 9

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L14_screen_3.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Show SYSTEM_BLOCKS with cache_control on the system prompt block.
2. Set max_tokens=400 and k=5, then re-run one setting and compare timings.

**Narration over this clip (for pacing)**

> He chooses five chunks, turns on prompt caching for the system prompt, and limits answers to four hundred tokens. Caching needs just one small setting on the stable block. Caching has minimum lengths and its own prices, so check the current documentation before you rely on it.

## Clip 4: scene 10

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L14_screen_4.mp4`
- **Target length:** about 24 seconds

**Steps**

1. Show the short FastAPI /ask endpoint from content.md.
2. Run the Streamlit app and ask a warranty question; show the answer with citations.
3. Show the API key set as a server environment variable (masked).

**Narration over this clip (for pacing)**

> Then he deploys. For a demo or internal tool, Streamlit gives a chat interface in a few lines. For a service that other systems call, a FastAPI endpoint wraps the same pipeline. He deploys a Streamlit app on an internal server for five support staff, with the API key kept on the server, never in the browser.

## Production notes for this lesson

- [VERSION] Claude API prices, usage fields (input_tokens, output_tokens), prompt caching syntax, minimum cacheable length and cache pricing, and model names. Prices are read from environment variables; never show or say a price or model ID. Blur any terminal line that shows them.
- [VERIFY] Realistic cost per learner (course-level flag).
- [VERSION] Streamlit, FastAPI and free hosting plan limits; the voiceover names no hosting provider.
- Timings, token counts and costs in the demo come from a real run; the voiceover says 'you'll see something like' and gives no values.
- Tomás's comparison (k=5 adds about 40% more input tokens than k=3; k=10 doubles the input tokens of k=5) is hypothetical; the slide carries a 'hypothetical results' label.
- Tomás and the Rosario electronics shop are hypothetical.
