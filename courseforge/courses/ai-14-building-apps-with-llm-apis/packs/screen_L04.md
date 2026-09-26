# Screen Demo Pack: AI-14 L04 Tokens, Context and Cost

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-14-building-apps-with-llm-apis_L04_screen_1.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Open log_helper.py in VS Code
2. Highlight PRICE_IN and PRICE_OUT with the comment to copy them from the pricing page (values left as 0.0 placeholders)
3. Highlight the cost line inside log_call()
4. Highlight the csv.writer row: time, feature, model, input tokens, output tokens, cost

**Narration over this clip (for pacing)**

> She writes a small helper. At the top are two price constants, copied from the pricing page. The helper reads the usage from each response, calculates the cost, and adds one row to a CSV file with the time, the feature, the model, both token counts and the cost.

## Clip 2: scene 10

- **Filename:** `ai-14-building-apps-with-llm-apis_L04_screen_2.mp4`
- **Target length:** about 10 seconds

**Steps**

1. Open compare_languages.py
2. Show the English and Arabic versions of the same invented grammar question
3. Run count_tokens for both and show the two input token counts in the terminal

**Narration over this clip (for pacing)**

> Before sending, she counts the input tokens for the same grammar question, once in English and once in Arabic, with the same system prompt.

## Clip 3: scene 11

- **Filename:** `ai-14-building-apps-with-llm-apis_L04_screen_3.mp4`
- **Target length:** about 25 seconds

**Steps**

1. Run the script to send both requests and call log_call() after each
2. Open usage_log.csv and show the two rows, labelled 'example numbers'
3. Highlight the input and output token columns for both rows

**Narration over this clip (for pacing)**

> Then she sends both requests with the same max tokens, and logs them. You'll see something like two rows in the CSV file. She compares the token counts in the two rows. But one test is not enough, so she will measure a sample of real questions in each language before she sets prices for her premium plan.

## Clip 4: scene 12

- **Filename:** `ai-14-building-apps-with-llm-apis_L04_screen_4.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Open the system prompt file and show its token count from count_tokens
2. Add a TODO comment in the code: try prompt caching (L13)

**Narration over this clip (for pacing)**

> She also notices something bigger. Her system prompt is six hundred tokens long, and it is sent with every call. She makes a note to try prompt caching in lesson thirteen.

## Production notes for this lesson

- [VERSION] Prices per model, the token-counting endpoint and its SDK method (count_tokens), and any limits or pricing for it must be checked against the current docs at recording time. The voiceover names no prices; the PRICE_IN and PRICE_OUT constants stay at 0.0 placeholders on screen, and cost values in the log are shown as 0.00xxxx.
- [VERIFY] The claim that the same meaning can use different token counts in different languages is NOT stated as fact in the voiceover; the script only tells learners to measure their own languages. The Arabic and English numbers in Farida's log (212/180 and 241/205) are illustrative: label them 'example numbers' on screen.
- Farida and the Cairo language-learning app are fictional. Use an invented grammar question; no learner data on screen.
