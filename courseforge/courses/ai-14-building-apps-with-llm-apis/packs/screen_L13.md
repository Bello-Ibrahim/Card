# Screen Demo Pack: AI-14 L13 Cost Control in Practice

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-14-building-apps-with-llm-apis_L13_screen_1.mp4`
- **Target length:** about 10 seconds

**Steps**

1. Open cache_test.py in VS Code with caching turned off
2. Run it twice with the same question
3. Show the usage lines: input about 3,600 tokens, cache write 0, cache read 0 (example output)

**Narration over this clip (for pacing)**

> First, she sends the same question twice without caching, and logs the usage. Both calls send the full system prompt as normal input tokens.

## Clip 2: scene 10

- **Filename:** `ai-14-building-apps-with-llm-apis_L13_screen_2.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Change system to a list with one text block and cache_control {"type": "ephemeral"}
2. Highlight the print of input_tokens, cache_creation_input_tokens and cache_read_input_tokens
3. Run with two different questions within a minute
4. Show call 1: cache write about 3,500; call 2: cache read about 3,500 (example output)

**Narration over this clip (for pacing)**

> Then she adds the cache marker to the system prompt block, and sends two different questions within a minute. You'll see something like this. The first call writes the system prompt to the cache. The second call reads it from the cache, and only the new question counts as normal input.

## Clip 3: scene 11

- **Filename:** `ai-14-building-apps-with-llm-apis_L13_screen_3.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Open log_helper.py and add constants for cache write and cache read prices, left as placeholders with a comment to copy them from the pricing page
2. Extend the cost formula with the two cache fields
3. Run run_eval.py with caching on and show the unchanged pass rate (example output)

**Narration over this clip (for pacing)**

> She adds the current prices for cache writes and cache reads to her cost helper, and compares the cost of each call. Then she runs her evaluation set with caching on. The pass rate is unchanged, because caching does not change what the model sees.

## Clip 4: scene 12

- **Filename:** `ai-14-building-apps-with-llm-apis_L13_screen_4.mp4`
- **Target length:** about 11 seconds

**Steps**

1. Show the nightly report script switched to a message batch with custom_id per request
2. Show the MODEL constant for topic classification changed to a smaller model placeholder
3. Show a 20-case eval result for the classification step (example output)

**Narration over this clip (for pacing)**

> She also moves her nightly summary report to the batch API, and sends simple topic classification to a smaller model, after checking it on twenty cases.

## Production notes for this lesson

- [VERSION] Prompt caching syntax (cache_control), minimum cacheable length, cache lifetime, cache write and read prices, the usage field names (cache_creation_input_tokens, cache_read_input_tokens), and the Batch API discount (about 50% in content.md) and rules must be checked against the current docs. The voiceover states no discount percentage and no prices; it says 'check the current pricing page'.
- The token numbers in Aroha's usage table (3620, 3500 and so on) are illustrative: label them 'example output' on screen. Show costs as formulas or placeholders, not real prices.
- Aroha Ngata and the Wellington tutoring company are fictional.
