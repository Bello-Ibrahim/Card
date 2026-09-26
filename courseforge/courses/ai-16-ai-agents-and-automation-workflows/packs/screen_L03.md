# Screen Demo Pack: AI-16 L03 Setting Up n8n (Self-Hosted)

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 7

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L03_screen_1.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Open a terminal
2. Run: docker volume create n8n_data
3. Run the docker run command from content.md with -p 5678:5678 and -v n8n_data:/home/node/.n8n
4. Show the log line saying the editor is available on port 5678

**Narration over this clip (for pacing)**

> Let's watch it happen. Ingrid Solberg is an operations analyst at a ferry company in Bergen, Norway. She wants to test n8n before she asks her IT team for a server. First, she opens a terminal and runs the two Docker commands. One creates a storage volume. The other starts n8n.

## Clip 2: scene 8

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L03_screen_2.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Open http://localhost:5678 in the browser
2. Fill in the owner account form with a demo email and a strong password (blur the password)
3. Arrive at the empty workflows list

**Narration over this clip (for pacing)**

> When the log says the editor is ready, she opens the local address in her browser, and creates the owner account with a strong password. This account exists only on her machine.

## Clip 3: scene 9

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L03_screen_3.mp4`
- **Target length:** about 28 seconds

**Steps**

1. Point to the Workflows list and its active switch
2. Open a new canvas
3. Double-click a node to show the panel: input left, settings middle, output right
4. Hover over Credentials in the side menu
5. Hover over Executions in the side menu

**Narration over this clip (for pacing)**

> Now a quick tour. The workflows list shows all her workflows. The canvas is where she adds and connects nodes. Credentials hold logins and API keys, so she never pastes a key into a node. And the executions list shows every run. When she double-clicks a node, its panel opens, with input on the left, settings in the middle, and output on the right.

## Clip 4: scene 10

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L03_screen_4.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Click to create a new workflow and name it 'Hello timestamp'
2. Add a Manual Trigger node ('Trigger manually')
3. Click the plus sign after the trigger
4. Add a Date & Time node that adds the current date and time to a new field run_at (alternative shown in caption: Edit Fields (Set) with {{ $now.toISO() }})

**Narration over this clip (for pacing)**

> She creates a new workflow, and names it Hello timestamp. The first node is always a trigger, so she adds a manual trigger. Then she clicks the plus sign, and adds a date and time node that puts the current time into a new field called run at.

## Clip 5: scene 11

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L03_screen_5.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Click Test workflow (or Execute workflow)
2. Both nodes show a green success mark
3. Open the output panel of the Date & Time node
4. Show one item with a run_at timestamp

**Narration over this clip (for pacing)**

> She clicks the button to test the workflow. Both nodes turn green. In the output of the second node, you'll see something like one item, with a run at field and today's date and time.

## Clip 6: scene 12

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L03_screen_6.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Click Save
2. Open the Executions list
3. Click the latest run
4. Click each node to show the data that passed through it

**Narration over this clip (for pacing)**

> Finally, she saves the workflow and opens the executions list. There is her run, with the data that passed through each node. She knows the tool works, and no company data went anywhere.

## Production notes for this lesson

- [VERSION] n8n installation commands (Docker image name, volume path, npx n8n), the supported Node.js version, and editor labels (create workflow, Manual Trigger, Date & Time, Edit Fields (Set), Test/Execute workflow, Executions) must be checked against the current n8n release before recording. Copy commands from the official n8n documentation on recording day.
- [VERIFY] n8n's fair-code licence: the voiceover says only that learners can run it for learning at no cost and must check the licence before using it at work. Do not add a claim that internal business use is allowed until this is confirmed.
- [VERIFY] Docker Desktop licence terms for personal, education and business use. The voiceover does not state them.
- Screen recording: use a fresh local n8n with a demo owner account; blur the password field. The terminal shows the Docker commands from content.md; the voiceover does not read them.
- Ingrid Solberg and her Bergen ferry company are fictional; no company data appears on screen.
