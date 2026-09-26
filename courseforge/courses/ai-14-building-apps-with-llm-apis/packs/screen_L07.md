# Screen Demo Pack: AI-14 L07 Streaming Responses

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-14-building-apps-with-llm-apis_L07_screen_1.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Open stream_timing.py in VS Code
2. Highlight start = time.perf_counter()
3. Highlight the check that records first when the first text piece arrives
4. Highlight final = stream.get_final_message() and total = time.perf_counter() - start
5. Highlight the final print with TTFT, total and output tokens

**Narration over this clip (for pacing)**

> He adds timing to the streaming loop. He notes the start time. When the first piece of text arrives, he records the time to first token. After the loop, he gets the final message and records the total time. Nothing else in his code changes. Same model, same system prompt, same messages.

## Clip 2: scene 10

- **Filename:** `ai-14-building-apps-with-llm-apis_L07_screen_2.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Run python stream_timing.py with an invented question about a contract term
2. Show the text appearing piece by piece in the terminal
3. Show the final line: TTFT 0.9s, total 11.4s, output tokens 610 (labelled 'example')

**Narration over this clip (for pacing)**

> He runs it with a long contract question. Watch the terminal. Text starts almost at once, and keeps flowing. At the end, you'll see something like a time to first token under one second, a total of about eleven seconds, and the output token count.

## Clip 3: scene 11

- **Filename:** `ai-14-building-apps-with-llm-apis_L07_screen_3.mp4`
- **Target length:** about 24 seconds

**Steps**

1. Add log_call(final, "legal_explain") after the loop
2. Add two columns for TTFT and total time to the log row
3. Run once more and open usage_log.csv to show the new row

**Narration over this clip (for pacing)**

> The total time is still long, but lawyers start reading almost at once. Kenji also passes the final message to his logging helper from lesson four, so every streamed call has its tokens, cost, and both times in the log. Later, he can see if a model or prompt change makes the tool feel slower.

## Production notes for this lesson

- [VERSION] The messages.stream() helper, text_stream, get_final_message() and the names of streaming events must be checked against the current SDK docs before recording.
- The timing numbers in the hook (twelve seconds, about one second) and in Kenji's output (TTFT 0.9s, total 11.4s, 610 output tokens) are illustrative, not measured. The voiceover uses 'something like'; label the on-screen output 'example'.
- Speed up the terminal recording only after the first words appear, so the short time to first token stays visible in real time.
- Kenji Watanabe and the Osaka law firm are fictional. Use an invented contract question; no client documents on screen.
