# L03 Setting Up n8n (Self-Hosted) | Presenter Script

Course: AI-16 · Video: 5 min · Words: 701

## Hook
In ten minutes, you can have a full automation platform running on your own laptop. No subscription, and no data leaving your machine unless you send it. Today, you install n8n and run your first workflow.

## Explain
Last time, we looked inside the agent loop. Now it is time to build. n8n is a workflow tool with a visual editor. You connect nodes on a canvas, and each node does one job: start the workflow, read data, call an API, or check a condition. It also has built-in AI nodes, which we use later in the course.

We self-host n8n in this course, for three reasons. Cost: you can run it for learning at no cost, but check the current licence terms before you use it at work. Data: your workflows, keys and run history stay on your computer. And learning: you see every setting and every log.

There are two common ways to install it. Option A is Docker, which we recommend. Option B is Node.js. Commands change between releases, so always copy them from the official n8n documentation on the day you install.

Here is a picture to keep in mind. n8n is like a workshop with a pegboard of tools. Each node is one tool on the board, and a workflow is the order in which you pick them up.

The executions list is the workshop logbook. It records every job. So when something goes wrong, you can see exactly which tool was used, and what happened.

## Demonstrate
Let's watch it happen. Ingrid Solberg is an operations analyst at a ferry company in Bergen, Norway. She wants to test n8n before she asks her IT team for a server. First, she opens a terminal and runs the two Docker commands. One creates a storage volume. The other starts n8n.

When the log says the editor is ready, she opens the local address in her browser, and creates the owner account with a strong password. This account exists only on her machine.

Now a quick tour. The workflows list shows all her workflows. The canvas is where she adds and connects nodes. Credentials hold logins and API keys, so she never pastes a key into a node. And the executions list shows every run. When she double-clicks a node, its panel opens, with input on the left, settings in the middle, and output on the right.

She creates a new workflow, and names it Hello timestamp. The first node is always a trigger, so she adds a manual trigger. Then she clicks the plus sign, and adds a date and time node that puts the current time into a new field called run at.

She clicks the button to test the workflow. Both nodes turn green. In the output of the second node, you'll see something like one item, with a run at field and today's date and time.

Finally, she saves the workflow and opens the executions list. There is her run, with the data that passed through each node. She knows the tool works, and no company data went anywhere.

A common mistake is to run Docker without the storage volume. You build several workflows, restart the container, and everything has gone. Always use a named volume from the first run, and export important workflows as backup files.

One more safety point. Keep n8n on your own computer during the course. Do not open it to the internet without a login and a secure connection.

## Recap
Let's recap. First, self-hosted n8n runs on your own computer and keeps your data local. Confirm the licence terms before you use it at work. Second, install it with Docker and a storage volume, or with Node.js, using the current official commands. Third, the core parts of the editor are the canvas, nodes, triggers, credentials, and the executions list.

## CTA
Now it is your turn. In the exercise below this video, you will install n8n, build the same two-node timestamp workflow, and open the execution log. Then restart n8n, and check that your workflow is still there. It takes about thirty minutes. In the next lesson, we build Your First Workflow: Sheets In, Sheets Out. See you there.

## Thumbnail
Headline: n8n on Your Laptop
Image: Navy background, a laptop showing a simple canvas of two connected node boxes, a small house icon for self-hosting, headline in teal Inter Bold.

## Production Notes
- [VERSION] n8n installation commands (Docker image name, volume path, npx n8n), the supported Node.js version, and editor labels (create workflow, Manual Trigger, Date & Time, Edit Fields (Set), Test/Execute workflow, Executions) must be checked against the current n8n release before recording. Copy commands from the official n8n documentation on recording day.
- [VERIFY] n8n's fair-code licence: the voiceover says only that learners can run it for learning at no cost and must check the licence before using it at work. Do not add a claim that internal business use is allowed until this is confirmed.
- [VERIFY] Docker Desktop licence terms for personal, education and business use. The voiceover does not state them.
- Screen recording: use a fresh local n8n with a demo owner account; blur the password field. The terminal shows the Docker commands from content.md; the voiceover does not read them.
- Ingrid Solberg and her Bergen ferry company are fictional; no company data appears on screen.
