# Screen Demo Pack: AI-14 L02 Setup: API Keys, SDKs and a Low-Cost Budget

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-14-building-apps-with-llm-apis_L02_screen_1.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Open the Claude Console and go to the billing or limits settings
2. Set a low monthly spend limit and save it
3. Go to API keys and click to create a key
4. Name the key meilin-laptop-dev
5. Copy the key once (the key is blurred on screen)

**Narration over this clip (for pacing)**

> In the Console, she opens the billing settings and sets a low monthly limit. Then she creates a key and gives it a clear name, so she always knows where it is used. She copies it once, because the Console will not show it again.

## Clip 2: scene 9

- **Filename:** `ai-14-building-apps-with-llm-apis_L02_screen_2.mp4`
- **Target length:** about 12 seconds

**Steps**

1. In the terminal (macOS or Linux), run export ANTHROPIC_API_KEY="sk-ant-..." with the value blurred
2. Show a caption with the Windows PowerShell form: $env:ANTHROPIC_API_KEY="sk-ant-..."
3. Create and activate a virtual environment
4. Run pip install anthropic and show it finish

**Narration over this clip (for pacing)**

> In her terminal, she saves the key in an environment variable. On Windows, the command looks a little different. Then she creates a virtual environment and installs the SDK.

## Clip 3: scene 10

- **Filename:** `ai-14-building-apps-with-llm-apis_L02_screen_3.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Open first_call.py in VS Code
2. Highlight the MODEL constant with the placeholder your-small-model-id and its comment to check the models page
3. Highlight anthropic.Anthropic() with the comment that it reads ANTHROPIC_API_KEY
4. Highlight messages.create with max_tokens=300 and the question 'Suggest one day trip from Penang.'
5. Highlight the loop that prints text blocks, then the stop_reason and usage prints

**Narration over this clip (for pacing)**

> Now she writes a short file for her first call. It sets the model in one constant, creates a client that reads the key automatically, asks for one day trip from Penang, and allows three hundred tokens. Then it prints the reply, the stop reason and the token counts.

## Clip 4: scene 11

- **Filename:** `ai-14-building-apps-with-llm-apis_L02_screen_4.mp4`
- **Target length:** about 24 seconds

**Steps**

1. Run python first_call.py in the terminal
2. Show the reply text, 'Stop reason: end_turn' and the input and output token counts
3. Change max_tokens to 20 and run the script again
4. Show the cut-off reply and 'Stop reason: max_tokens'

**Narration over this clip (for pacing)**

> She runs it. You'll see something like a suggestion for a day trip to Langkawi, then a stop reason of end turn, and a small number of input and output tokens. Then she lowers max tokens to twenty and runs it again. This time the reply is cut off, and the stop reason says max tokens.

## Clip 5: scene 12

- **Filename:** `ai-14-building-apps-with-llm-apis_L02_screen_5.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Run git status in the terminal
2. Show that only first_call.py and .gitignore are listed, with no .env file
3. Show a red-cross caption over the pattern api_key="sk-ant-..." inside code

**Narration over this clip (for pacing)**

> Finally, she runs git status to check that no file with her key will be committed. A common mistake is to paste the key straight into the code just to test, and then commit it. Always use the environment variable, and replace any key that has been exposed.

## Production notes for this lesson

- [VERSION] Record the Console steps (billing, spend limit, key creation), the SDK install command and the model choice against the live Console and docs on the recording day. Never show a model ID or price in the voiceover; blur or crop prices if the pricing page is shown.
- [VERIFY] Whether new accounts receive any trial credit is not stated in the voiceover; the script only tells learners to check the pricing pages.
- [REGION] [VERIFY] The API is offered directly only in supported countries, with cloud-provider alternatives. The voiceover only tells learners to check the current list; a reviewer must confirm the wording before publishing.
- Security: record with a throwaway key that is deleted right after recording. Blur the key in the Console and in the terminal at all times; the export command should show only a placeholder such as sk-ant-... on screen.
- Token counts in the demo output are illustrative; the voiceover says 'something like'.
- Mei Lin and the Penang travel start-up are fictional; the key name meilin-laptop-dev is an example.
