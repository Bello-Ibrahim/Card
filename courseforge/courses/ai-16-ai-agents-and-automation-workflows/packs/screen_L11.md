# Screen Demo Pack: AI-16 L11 Memory and Context

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L11_screen_1.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Open the agent workflow: Chat Trigger → AI Agent → Anthropic Chat Model + Google Sheets tool for 'tours'
2. Show the 'tours' sheet with invented packages

**Narration over this clip (for pacing)**

> Let's test it. Elena Popescu runs a travel agency in Bucharest, Romania. Her agent answers questions about invented tour packages from a sheet. It is built like the agent from the last lesson, with no memory yet.

## Clip 2: scene 9

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L11_screen_2.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Chat: 'What is the price of the Danube Delta tour?'
2. Chat: 'Is it available in May?'
3. Show the reply 'Which tour do you mean?' (example output)

**Narration over this clip (for pacing)**

> She asks: what is the price of the Danube Delta tour? Then: is it available in May? You'll see something like: which tour do you mean? Without memory, the second question has lost its subject.

## Clip 3: scene 10

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L11_screen_3.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Connect a Simple Memory sub-node to the AI Agent
2. Session key from the Chat Trigger; context window length 2
3. Hold the 6-turn conversation from content.md

**Narration over this clip (for pacing)**

> She connects a Simple Memory node, with the session key from the chat, and a window of two. Then she holds a six-turn conversation: the tour, the price, May, a group of eight, a second tour, and finally, so for the first tour, what is the total for my group?

## Clip 4: scene 11

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L11_screen_4.mp4`
- **Target length:** about 10 seconds

**Steps**

1. Show the turn-6 reply asking which tour (example output)
2. Open the memory node output to show only the last 2 exchanges

**Narration over this clip (for pacing)**

> At turn six, the agent asks which tour she means. The first tour and the group size have dropped out of the window.

## Clip 5: scene 12

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L11_screen_5.mp4`
- **Target length:** about 23 seconds

**Steps**

1. Change context window length to 6 and repeat the conversation
2. Show the correct turn-6 answer
3. Open the execution log and compare input tokens across turns
4. Set the window to 4 and add the system message rule from content.md

**Narration over this clip (for pacing)**

> She changes the window to six, and repeats. Now the answer is correct. But the execution log shows more input tokens on each later turn. So she settles on a window of four, and adds a rule to the system message: when a question refers to details you do not have, ask for them.

## Production notes for this lesson

- [VERSION] n8n memory sub-node name (Simple Memory, earlier Window Buffer Memory), session key and context window length settings, and AI Agent node connections must be checked against the current release.
- [REGION] Storing personal data in memory or Google Sheets and sending it to an external API may be restricted by local data protection law; the lesson uses invented sample data only. The voiceover says the rules differ by country and names none.
- The agent replies in the demo ('Which tour do you mean?') and the token growth are example outputs.
- Elena Popescu, her Bucharest travel agency and the tour packages are fictional.
