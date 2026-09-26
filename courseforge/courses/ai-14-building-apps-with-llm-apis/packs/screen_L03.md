# Screen Demo Pack: AI-14 L03 Prompt Design for Applications

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 10

- **Filename:** `ai-14-building-apps-with-llm-apis_L03_screen_1.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Open prompts/support_v1.txt in VS Code: 'Reply to this customer: {message}'
2. Run the script on one test message
3. Highlight in the output a long reply that promises a refund

**Narration over this clip (for pacing)**

> Her first version just says reply to this customer, followed by the message. The replies are long, and sometimes promise refunds the company does not offer. Once, it even followed an instruction written inside the customer's message.

## Clip 2: scene 11

- **Filename:** `ai-14-building-apps-with-llm-apis_L03_screen_2.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Open prompts/support_v3.txt
2. Highlight the role line and the audience line
3. Highlight the 80-word limit and the three rules (no refunds or credits, outage link, one clarifying question)
4. Highlight the sentence about <customer_message> tags being data, not instructions
5. Highlight the example message and reply

**Narration over this clip (for pacing)**

> Now look at version three, stored in its own file. It sets the role and the readers, and limits replies to eighty words. It never promises refunds, and says an agent will review the request. It asks one short question when unsure. It explains the tags, and gives one example.

## Clip 3: scene 12

- **Filename:** `ai-14-building-apps-with-llm-apis_L03_screen_3.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Open support.py
2. Highlight SYSTEM = Path("prompts/support_v3.txt").read_text()
3. Highlight the draft_reply function with system=SYSTEM and max_tokens=300
4. Highlight the f-string that wraps customer_text in <customer_message> tags

**Narration over this clip (for pacing)**

> Her code reads the prompt from the file, sends it as the system prompt, and wraps each customer message in the tags. Max tokens stays at three hundred. Because the prompt lives in a file, every change shows up in Git, with a clear version name.

## Clip 4: scene 13

- **Filename:** `ai-14-building-apps-with-llm-apis_L03_screen_4.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Run the comparison script for v1 and v3 on the same five test messages
2. Show the outputs side by side in the terminal
3. Show her notes table with the label 'example results': shorter replies, no refund promises, hidden instruction ignored

**Narration over this clip (for pacing)**

> She runs both versions on the same five test messages. You'll see something like this. Version three replies are shorter, never promise refunds, and ignore the instruction hidden in the customer's message.

## Production notes for this lesson

- [VERSION] The voiceover says some current models do not accept sampling settings such as temperature. Check this against the current docs on the recording day; if it is no longer true, cut that sentence from scene 7 and re-time.
- The comparison results for versions 1 and 3 are hypothetical example results from Efua's notes; show 'example results' on screen.
- Record the demo with a small development model and max_tokens 300 (from L02). Do not show a model ID in the voiceover.
- The status page link inside the v3 prompt should be a placeholder, not a real provider's URL. Efua Mensah and the Accra provider are fictional: no real network brand or logo on screen.
