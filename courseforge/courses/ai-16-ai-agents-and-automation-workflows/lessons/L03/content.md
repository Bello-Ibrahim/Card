# L03 Setting Up n8n (Self-Hosted)

Course: AI-16 · Module: M1 · Objectives: O3 · Video: 5 min (screen demo)

## Hook
In ten minutes you can have a full automation platform running on your own laptop, with no subscription and no data leaving your machine unless you send it. Today you install n8n and run your first workflow.

## Explanation
n8n is a workflow automation tool with a visual editor. You connect **nodes** on a canvas, and each node does one job: start the workflow, read data, call an API, check a condition. It also has built-in AI nodes, which we use from L10.

We **self-host** n8n in this course for three reasons:

- **Cost.** The self-hosted version can be run for free. n8n uses its own "fair-code" licence, not a standard open-source licence. Our understanding is that internal business use is allowed, but check the current licence terms before you use it at work. [VERIFY]
- **Data.** Your workflows, credentials and execution data stay on your computer.
- **Learning.** You see every setting, log and file.

There are two common ways to install it. Commands change between releases, so copy them from the official n8n documentation on the day you install. [VERSION]

**Option A: Docker (recommended).** Install Docker Desktop, then run:

```bash
docker volume create n8n_data
docker run -it --rm --name n8n -p 5678:5678 \
  -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

The volume keeps your workflows and credentials when the container stops. [VERSION]

**Option B: Node.js.** With a supported Node.js version installed, run `npx n8n`. [VERSION]

Then open `http://localhost:5678` in your browser and create the local owner account. This account exists only on your machine.

A short tour of the editor (names and positions may differ in your release [VERSION]):

- **Workflows list:** all your workflows, each with an on/off (active) switch.
- **Canvas:** where you add and connect nodes. The first node is always a **trigger**.
- **Node panel:** opens when you double-click a node. Input data is on the left, settings in the middle and output on the right.
- **Credentials:** stored logins and API keys that nodes use. You enter a key once and never paste it into a node.
- **Executions:** a log of every run, with the data that passed through each node.

**Analogy:** n8n is like a workshop with a pegboard of tools. Each node is one tool on the board. A workflow is the order in which you pick them up. The executions list is the workshop logbook that records every job, so when something goes wrong you can see exactly which tool was used and what happened.

Keep your n8n instance on your own computer during the course. Do not open port 5678 to the internet without authentication and HTTPS.

## Worked Example
Ingrid Solberg is an operations analyst at a hypothetical ferry company in Bergen, Norway. She wants to test n8n before she asks IT for a server. On screen, she:

1. Opens a terminal and runs the two Docker commands above.
2. Waits until the log shows that the editor is available on port 5678, then opens `http://localhost:5678`.
3. Creates the owner account with a strong password.
4. Clicks the option to create a new workflow and names it "Hello timestamp". [VERSION]
5. Adds a **Manual Trigger** node ("Trigger manually"). [VERSION]
6. Clicks the plus sign after the trigger and adds a **Date & Time** node set to add the current date and time to a new field called `run_at`. An **Edit Fields (Set)** node with the expression `{{ $now.toISO() }}` gives the same result. [VERSION]
7. Clicks **Test workflow** (or **Execute workflow**). Both nodes turn green. [VERSION]
8. Opens the output panel of the second node and sees one item with `run_at`.
9. Saves the workflow and opens the **Executions** list to see the run.

She now knows the tool works on her laptop and has not sent any company data anywhere.

## Common Mistake
Learners often run the Docker command without the `-v` volume option, build several workflows, restart the container and find that everything has gone. Without a volume, the data lives inside a container that is deleted when it stops. Always use a named volume (or a folder on your disk) from the first run, and export important workflows as JSON files as a backup.

## Key Takeaways
1. Self-hosted n8n runs on your own computer, keeps your data local and costs nothing for learning; confirm the licence terms before using it at work.
2. Install with Docker plus a persistent volume, or with Node.js, and always copy the current commands from the official documentation.
3. The core parts of the editor are the canvas, nodes, triggers, credentials and the executions list.

## Hands-on Exercise
**Task:** Install n8n locally and build a two-node workflow that adds the current date and time, then open the execution log.
**Tools:** Docker Desktop (free for personal and learning use [VERIFY]) or Node.js; n8n self-hosted; a web browser.
**Steps:**
1. Install Docker Desktop or a supported Node.js version. [VERSION]
2. Start n8n with the Docker commands above (including the volume) or with `npx n8n`.
3. Open `http://localhost:5678` and create the owner account.
4. Create a workflow called "Hello timestamp".
5. Add a Manual Trigger node, then a Date & Time or Edit Fields (Set) node that creates a field `run_at` with the current date and time.
6. Run the workflow and check the output of the second node.
7. Save, then open the Executions list and click the run to see the data at each node.
8. Stop and restart n8n, and confirm that the workflow is still there.
**What good looks like:** Both nodes show a green success mark, the output contains a `run_at` field with a current timestamp, the run appears in the Executions list, and the workflow survives a restart.
**Time:** about 30 minutes

## Review Flags
- [VERSION] n8n installation commands (Docker image name, volume path, `npx n8n`), the supported Node.js version, and editor labels (create workflow, Manual Trigger, Date & Time, Edit Fields (Set), Test/Execute workflow, Executions) must be checked against the current n8n release before recording.
- [VERIFY] n8n's fair-code licence: confirm that self-hosted use for internal business automation is allowed for learners, and phrase the licence sentence accordingly.
- [VERIFY] Docker Desktop licence terms for personal, education and business use.
