# Screen Demo Pack: AI-14 L10 Tool Loops and Guardrails

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-14-building-apps-with-llm-apis_L10_screen_1.mp4`
- **Target length:** about 29 seconds

**Steps**

1. Open support_loop.py in VS Code
2. Highlight MAX_STEPS = 5 and WRITE_TOOLS = {"change_delivery_address"}
3. Highlight the unknown-tool check that returns 'Unknown tool' with err True
4. Highlight the confirm() check for write tools
5. Highlight the tool_result with is_error, then the else branch: 'Stopped: too many tool steps.'

**Narration over this clip (for pacing)**

> Here is the core of his loop. It runs for at most five steps. For each tool request, it first checks that the tool exists. If it is a tool that writes data, it asks the customer to confirm. Only then does it run the handler. Every result carries an error flag, and if the loop reaches the limit, it stops and says a person will follow up.

## Clip 2: scene 9

- **Filename:** `ai-14-building-apps-with-llm-apis_L10_screen_2.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Open the change_delivery_address handler
2. Highlight the check that the order belongs to the current customer
3. Highlight the not-shipped check and the empty-address check

**Narration over this clip (for pacing)**

> Each handler validates its input first. The address handler checks that the order belongs to the customer who is logged in, that it has not shipped yet, and that the address is not empty. It changes only the address field, through the shop's normal business rules.

## Clip 3: scene 10

- **Filename:** `ai-14-building-apps-with-llm-apis_L10_screen_3.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Run the script and type 'Send my order CO-778 to my office instead'
2. Show the confirm prompt: 'Change the address of order CO-778 to Calle 10 #43-12, Medellín? (yes/no)'
3. Type no
4. Show the model's reply (labelled 'example output')

**Narration over this clip (for pacing)**

> Now he tests it. He writes, send my order to my office instead. His code shows the planned change and asks yes or no. He answers no. You'll see something like, no problem, I have not changed the address.

## Clip 4: scene 11

- **Filename:** `ai-14-building-apps-with-llm-apis_L10_screen_4.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Ask for the status of four orders in one message
2. Print the user message and show four tool_result blocks together
3. Change MAX_STEPS to 1, run again, and show 'Stopped: too many tool steps.'

**Narration over this clip (for pacing)**

> Then he asks about four orders at once. The loop returns four results in one message. Finally, he sets the step limit to one, and checks that the stop message appears.

## Production notes for this lesson

- [VERSION] Strict tool schema checking, the is_error field on tool results and parallel tool-call behaviour must be checked against the current tool-use docs before recording.
- The model reply 'No problem, I have not changed the address.' is example output; the voiceover says 'something like'.
- Scope note: multi-step agents and approval workflows are covered in AI-16; the voiceover mentions this once.
- Carlos Mendoza, the Medellín furniture shop, order numbers and the address are invented; the data is a local dictionary.
