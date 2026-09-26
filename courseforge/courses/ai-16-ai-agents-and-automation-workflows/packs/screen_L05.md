# Screen Demo Pack: AI-16 L05 Calling the Claude API from n8n

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L05_screen_1.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Show the 'reviews' sheet: review_id, review, summary, tokens, with 5 invented reviews
2. Open the Claude Console and create an API key (blurred)
3. Set a monthly spending limit

**Narration over this clip (for pacing)**

> Let's build it. Mei-Lin Chen runs a tea shop in Taipei. Her reviews sheet has five invented reviews, with empty summary and tokens columns. First, she creates an API key in the Claude Console, and sets a monthly spending limit.

## Clip 2: scene 10

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L05_screen_2.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Credentials → new Header Auth credential named 'Claude API'
2. Name: x-api-key, Value: the key (blurred)
3. New workflow: Manual Trigger → Google Sheets (get rows from 'reviews')

**Narration over this clip (for pacing)**

> In n8n, she creates a header credential called Claude API, with the key as its value. Then she builds a manual trigger, and a Sheets node that gets rows from reviews.

## Clip 3: scene 11

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L05_screen_3.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Add an HTTP Request node
2. Method POST, URL https://api.anthropic.com/v1/messages
3. Authentication: the 'Claude API' Header Auth credential
4. Add headers anthropic-version and content-type
5. Paste the JSON body from content.md with the review expression

**Narration over this clip (for pacing)**

> Next, an HTTP Request node. She sets the method to POST, pastes the Messages address, and picks her Claude API credential. She adds the other two headers, and the body with her system prompt.

## Clip 4: scene 12

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L05_screen_4.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Limit the run to one item
2. Execute the HTTP Request node
3. Open the output and point to content[0].text (example output)
4. Point to usage: input_tokens and output_tokens

**Narration over this clip (for pacing)**

> She runs it with a single row first. In the output, you'll see something like: the customer liked the oolong, but found the delivery slow. You also see the token usage.

## Clip 5: scene 13

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L05_screen_5.mp4`
- **Target length:** about 24 seconds

**Steps**

1. Add Edit Fields (Set): summary = {{ $json.content[0].text }}, tokens = input + output tokens, keep review_id
2. Add Google Sheets (update row, match on review_id)
3. Remove the one-item limit and run all 5
4. Show the sheet with 5 summaries and token counts

**Narration over this clip (for pacing)**

> Then she adds a Set node. It takes the summary text, adds the input and output tokens together, and keeps the review ID. Finally, a Sheets node updates the rows, matching on review ID. She removes the one-row limit and runs all five. Her sheet now has five summaries, and a token count for each row.

## Production notes for this lesson

- [VERSION] Claude API: the anthropic-version header value, the request and response fields (content[0].text, stop_reason, usage), the current model IDs for the MODEL placeholder, the anthropic SDK call, and the Claude Console steps for API keys and spending limits must be checked against current documentation. No free tier is assumed and no prices are named in the voiceover.
- [VERSION] n8n: HTTP Request node options, Header Auth credential, Anthropic chat model node names and Edit Fields (Set) expressions must be checked against the current release.
- Screen recording: blur the API key everywhere (Console, credential form). The JSON body on screen keeps the literal MODEL placeholder or a current model ID; the voiceover never names a model ID or a price.
- The summary shown in the demo is an example output; the real output will differ. The optional Python SDK snippet stays on the lesson page, not in the video.
- Mei-Lin Chen and her Taipei tea shop are fictional; reviews are invented.
