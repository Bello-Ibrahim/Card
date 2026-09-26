# Screen Demo Pack: AI-14 L06 Validation, Errors and Retries

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-14-building-apps-with-llm-apis_L06_screen_1.mp4`
- **Target length:** about 27 seconds

**Steps**

1. Open extract.py and scroll to the extract() function
2. Highlight the stop_reason checks for max_tokens and refusal
3. Highlight Invoice.model_validate_json(raw) and check_business_rules(inv)
4. Highlight the line that appends 'Your last answer failed a check' to the content
5. Highlight return None with the comment 'send to human review'

**Narration over this clip (for pacing)**

> Look at the order of the checks. After the call, the function checks the stop reason first. Only then does it read the text and validate it against the schema and her business rules. If a check fails, it adds the error to the request and tries once more. After two attempts, it returns nothing, so the item goes to human review.

## Clip 2: scene 9

- **Filename:** `ai-14-building-apps-with-llm-apis_L06_screen_2.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Highlight the try block around messages.create
2. Highlight each except clause in order: AuthenticationError, BadRequestError, RateLimitError, APIStatusError, APIConnectionError

**Narration over this clip (for pacing)**

> Around the call, the error handler catches each class separately, from the most specific to the most general. Each handler prints a clear message that says what to do next, such as check the key, fix the request, or try again later. Now she tests three failures on screen.

## Clip 3: scene 10

- **Filename:** `ai-14-building-apps-with-llm-apis_L06_screen_3.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Change max_tokens to 10
2. Run the extractor on one invoice
3. Show the message 'Output cut off. Raise max_tokens.'

**Narration over this clip (for pacing)**

> Test one. She sets max tokens to ten. The stop reason is max tokens, and the function stops with a clear message, instead of saving half a record.

## Clip 4: scene 11

- **Filename:** `ai-14-building-apps-with-llm-apis_L06_screen_4.mp4`
- **Target length:** about 14 seconds

**Steps**

1. In a new terminal, set ANTHROPIC_API_KEY to an obviously fake value
2. Run the extractor
3. Show 'Invalid API key. Check ANTHROPIC_API_KEY.' and no retry messages
4. Close that terminal

**Narration over this clip (for pacing)**

> Test two. In one terminal only, she sets the key variable to a wrong value. The SDK raises an authentication error, and her handler prints a clear key message. There are no retries.

## Clip 5: scene 12

- **Filename:** `ai-14-building-apps-with-llm-apis_L06_screen_5.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Run the extractor on a text file with a shopping list
2. Show the first validation failure and the retry
3. Show the result None and the 'sent to review' message

**Narration over this clip (for pacing)**

> A common mistake is to catch every exception and retry three times. That hides the real problem. It retries invalid keys, saves cut-off output, and sends refusals again and again. Check the stop reason, catch by class, let the SDK retry temporary errors, and send permanent failures to a person.

## Production notes for this lesson

- [VERSION] SDK error class names (AuthenticationError, BadRequestError, RateLimitError, APIStatusError, APIConnectionError), the default max_retries value, which status codes are retried automatically, and the output_config structured-output parameter must be checked against the current SDK docs before recording. The voiceover names no default retry count.
- The three test results in the demo are hypothetical; record them live and adjust the voiceover only if the behaviour differs.
- For the invalid-key test, set a clearly fake value in one terminal only; never show the real key. Restore it off camera.
- Sofia Petrova and the Sofia logistics company are fictional; invoices are invented text.
