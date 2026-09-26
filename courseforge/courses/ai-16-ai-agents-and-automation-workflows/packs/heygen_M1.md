# HeyGen Batch Pack: AI-16 M1 (Workflows and Agents: The Foundations)

Course: AI Agents and Automation Workflows. Make one HeyGen video per lesson below, using these settings for every video.

| Setting | Value |
|---|---|
| Avatar | **Vaness** (standard avatar), ID `1bd001e7e50f421d891986aad5c8bbd2` |
| Voice | `1bd001e7e50f421d891986aad5c8bbd2` (the same ID as the avatar: if HeyGen does not list it as a voice, use Vaness's paired English voice and record its ID in DECISIONS.md) |
| Background | Solid colour **#00FF00** (pure green, no gradient, no image) |
| Resolution | 1080p (1920×1080) |
| Aspect ratio | 16:9 |
| Avatar framing | Centred, head and shoulders, same size in every lesson |
| Captions/subtitles | **Off** (captions are added in Stage 6) |
| Music | Off |
| Speed | Normal (1.0×) |

How to paste: copy the whole text block for a lesson into a single HeyGen scene. Each blank line is a natural pause. Do not add or change words, because the edit is timed to this exact narration.

Save each finished video with the exact filename shown, and upload it to `/incoming/`.

## L01 From Scripts to Agents

- **Filename:** `ai-16-ai-agents-and-automation-workflows_M1_L01_presenter.mp4`
- **Expected length:** about 5.3 minutes (741 words). The quality gate accepts ±10%.

```text
Two teams want to use AI agents. One needs to copy invoice totals into a spreadsheet every morning. The other needs to answer unusual customer questions that nobody can predict. Only one of them needs an agent. Let's find out which one, and why.

Hi, and welcome to AI Agents and Automation Workflows. In this first lesson, we look at a simple idea. Automation is not one thing. It is a spectrum, with three main points.

The first point is a fixed workflow, with rules only. Something starts a run, and the same steps follow every time. It is fast, cheap and easy to test. But it fails when the input does not match what the rules expect.

The second point is a workflow with an AI step. The path is still fixed, but one step asks a language model to do something that rules do badly, such as summarise a message, classify it, or pull out details from free text. The model does not decide what happens next. Your workflow does.

The third point is an agent. The model gets a goal, a set of tools and some instructions. It chooses its own next step, uses a tool, looks at the result, and decides again, until it reaches the goal or a stop condition. Nobody writes the path in advance.

As you move from one to three, you gain flexibility. But you also pay more, because an agent may call the model many times for one task. Results are harder to predict. And risk grows, because the system can take actions you did not plan for.

Here is a simple way to picture it. A fixed workflow is a recipe that a cook follows exactly. Same ingredients, same order, same result.

An agent is a chef who opens the fridge, sees what is there, and decides what to cook. The chef can handle surprises. But you cannot be sure what will arrive on the plate, and the chef may use expensive ingredients.

For a school canteen that serves the same meal to five hundred children, you want the recipe.

In this course, you will use five building blocks. A trigger starts a run. A node is one step, like reading a sheet or checking a condition. A tool is an action an agent may choose. Memory is what the agent keeps between steps. And the agent loop is the repeated cycle of decide, act and check.

Let's use this on a real list. Tomás Herrera manages operations at a logistics company in Montevideo, Uruguay. He has three tasks to automate.

Task one. Every night, copy the delivery counts from a scanner export into a report sheet. The format never changes. So this is a fixed workflow. Rules are cheaper, and always correct.

Task two. Read driver notes, such as gate locked, left with neighbour, and tag each one as delivered, failed, or needs follow-up. The notes are free text, so a model helps. But the next step for each tag is known. That is a workflow with an AI step.

Task three. A customer writes: my parcel is late, can I change the address, and why was I charged twice? The steps depend on the message. Check tracking, check billing, maybe draft an address change. This is where an agent makes sense.

But notice the limits. Tomás does not let the agent issue refunds or change addresses on its own. It may look up data and draft replies, but a person approves any change. That keeps the flexibility, and limits the risk.

One common mistake is to start with an agent because it sounds more advanced. Teams then find it is slower, costs more per task, and sometimes takes a different path for the same input.

Let's recap. First, automation is a spectrum: fixed workflow, workflow with an AI step, and agent. Each step to the right adds flexibility, cost and risk. Second, an agent chooses its own next step, while a workflow follows your path. Third, choose the least freedom that solves the problem, and limit what an agent may do alone.

So, which team needed an agent? The one with unpredictable customer questions. Now it is your turn. In the exercise below this video, you will sort eight business tasks into the three types, and justify two of your choices. It takes about fifteen minutes. In the next lesson, we look inside the agent loop. See you there.
```

## L02 How an Agent Works: The Agent Loop

- **Filename:** `ai-16-ai-agents-and-automation-workflows_M1_L02_presenter.mp4`
- **Expected length:** about 5.3 minutes (737 words). The quality gate accepts ±10%.

```text
A language model on its own can only produce text. It cannot open a file, check a database, or send a message. So how does an agent finish a task with several steps? The answer is a simple loop that your software runs around the model.

Last time, you saw that an agent chooses its own next step. Today, we see how. An agent repeats four actions until it has to stop.

First, observe. Collect the current situation: the task, the conversation so far, and the results of earlier steps. Second, decide. Send all of this to the model. The model replies with either a final answer, or a request to use a tool.

Third, act. Your software, not the model, runs the tool and gets a result. Fourth, check. Add that result to the situation, and go back to the start.

The loop stops when the model gives a final answer, or when it reaches a limit on steps, time or cost. Always set a maximum. Without one, a confused agent can call tools again and again.

Every agent has four parts. The model makes the decisions. The tools are the actions it may request, each with a name, a description and the inputs it expects. The memory is what it can see from earlier steps. And the instructions describe the goal, the rules, the tone, and when to stop or ask a person.

The agent can only do what its tools allow. So the tool list is your main safety control.

Here is a way to picture it. Think of a detective on a case. The detective looks at the evidence, decides which witness to interview next, goes to the interview, and adds the new facts to the case file.

The detective repeats this until the case is solved, or the manager says, stop, we are out of time. The detective is the model. The interviews are the tools. The case file is the memory. And the manager's brief is the instructions.

In code, the loop is short. On screen is some pseudocode. While the step count is under the maximum, ask the model to decide. If it gives a final answer, stop. If not, run the tool it asked for, save the result, and count one more step.

Let's follow one run. Priya Raman works in finance at a consultancy in Chennai, India. She designs an expense-checking agent, using sample data only.

Her instructions say: check each claim against the travel policy, flag any problem with a reason, and never approve or reject a claim yourself. The agent has three tools. One reads a receipt. One looks up the policy. One flags a claim. It may use at most six tool calls.

The task is: check claim one hundred and four. The agent decides to read the receipt. The result is a meal for three people, with an amount above the usual level.

Next, it decides to look up the policy for meals. The result is a limit per person, and a rule that client meals need the client name.

The amount per person is over the limit, and no client name is given. So it flags the claim with both reasons. Then it gives its final answer: claim one hundred and four is flagged for review, with two issues. The loop stops.

Notice what the agent did not do. It did not reject the claim. A person makes that decision, using the agent's reasons.

A common mistake is to think the model runs the tools itself, or has access to the database. It does not. The model only asks for a tool. Your software decides whether to run it. That is good news, because you control exactly which actions are possible.

Let's recap. First, an agent repeats observe, decide, act and check, until it gives a final answer or reaches a limit. Second, its four parts are the model, the tools, the memory and the instructions. Third, the model only requests tools. Your software runs them, which makes the tool list your main safety control.

Now it is your turn. In the exercise below this video, you will draw the agent loop for a customer-support agent at an online bookshop. Label its tools, write its stop condition, and add a path to a person. It takes about twenty minutes. In the next lesson, we start building, with Setting Up n8n. See you there.
```

## L03 Setting Up n8n (Self-Hosted)

- **Filename:** `ai-16-ai-agents-and-automation-workflows_M1_L03_presenter.mp4`
- **Expected length:** about 5.0 minutes (694 words). The quality gate accepts ±10%.

```text
In ten minutes, you can have a full automation platform running on your own laptop. No subscription, and no data leaving your machine unless you send it. Today, you install n8n and run your first workflow.

Last time, we looked inside the agent loop. Now it is time to build. n8n is a workflow tool with a visual editor. You connect nodes on a canvas, and each node does one job: start the workflow, read data, call an API, or check a condition. It also has built-in AI nodes, which we use later in the course.

We self-host n8n in this course, for three reasons. Cost: you can run it for learning at no cost, but check the current licence terms before you use it at work. Data: your workflows, keys and run history stay on your computer. And learning: you see every setting and every log.

There are two common ways to install it. Option A is Docker, which we recommend. Option B is Node.js. Commands change between releases, so always copy them from the official n8n documentation on the day you install.

Here is a picture to keep in mind. n8n is like a workshop with a pegboard of tools. Each node is one tool on the board, and a workflow is the order in which you pick them up.

The executions list is the workshop logbook. It records every job. So when something goes wrong, you can see exactly which tool was used, and what happened.

Let's watch it happen. Ingrid Solberg is an operations analyst at a ferry company in Bergen, Norway. She wants to test n8n before she asks her IT team for a server. First, she opens a terminal and runs the two Docker commands. One creates a storage volume. The other starts n8n.

When the log says the editor is ready, she opens the local address in her browser, and creates the owner account with a strong password. This account exists only on her machine.

Now a quick tour. The workflows list shows all her workflows. The canvas is where she adds and connects nodes. Credentials hold logins and API keys, so she never pastes a key into a node. And the executions list shows every run. When she double-clicks a node, its panel opens, with input on the left, settings in the middle, and output on the right.

She creates a new workflow, and names it Hello timestamp. The first node is always a trigger, so she adds a manual trigger. Then she clicks the plus sign, and adds a date and time node that puts the current time into a new field called run at.

She clicks the button to test the workflow. Both nodes turn green. In the output of the second node, you'll see something like one item, with a run at field and today's date and time.

Finally, she saves the workflow and opens the executions list. There is her run, with the data that passed through each node. She knows the tool works, and no company data went anywhere.

A common mistake is to run Docker without the storage volume. You build several workflows, restart the container, and everything has gone. Always use a named volume from the first run, and export important workflows as backup files.

One more safety point. Keep n8n on your own computer during the course. Do not open it to the internet without a login and a secure connection.

Let's recap. First, self-hosted n8n runs on your own computer and keeps your data local. Confirm the licence terms before you use it at work. Second, install it with Docker and a storage volume, or with Node.js, using the current official commands. Third, the core parts of the editor are the canvas, nodes, triggers, credentials, and the executions list.

Now it is your turn. In the exercise below this video, you will install n8n, build the same two-node timestamp workflow, and open the execution log. Then restart n8n, and check that your workflow is still there. It takes about thirty minutes. In the next lesson, we build Your First Workflow: Sheets In, Sheets Out. See you there.
```

## L04 Your First Workflow: Sheets In, Sheets Out

- **Filename:** `ai-16-ai-agents-and-automation-workflows_M1_L04_presenter.mp4`
- **Expected length:** about 4.9 minutes (683 words). The quality gate accepts ±10%.

```text
Many small businesses already run on a spreadsheet. If your automation can read a sheet, change the data, and write it back, you can automate real work before you add any AI at all.

Last time, you installed n8n. Now let's connect it to real data. In this course, Google Sheets is our simple database, and a workflow that uses it has three parts.

First, read. A Google Sheets node reads rows, and each row becomes one item in n8n, with the column headers as field names. Second, change. A Set, IF or Code node adds or changes fields on each item. Third, write. A second Sheets node updates the rows, or adds new ones.

Most nodes handle items one by one. If fifteen rows come in, fifteen items go out, and each node runs its settings for every item.

Before any of this, n8n needs permission to use your Google account. You create a credential. In the self-hosted version, this usually means setting up a Google Cloud project and turning on the Sheets API. The steps change often, so follow the current n8n guide. And use a test account, with access only to the sheets you need.

Here is a way to picture it. The workflow is like a clerk with a clipboard. The clerk copies rows from the ledger, writes a note next to each one, then copies the notes back into the right lines of the ledger, by checking the order number.

If the order numbers are missing, the clerk cannot find the right line. That is why updates need a column that identifies each row, such as an order ID.

Let's build it. Wanjiru Kamau runs a bakery in Nairobi, Kenya. She wants to phone every customer who orders more than five thousand Kenyan shillings, to confirm before baking. She uses sample data only. First, she creates a sheet called orders, with fifteen invented rows.

In n8n, she creates a Google Sheets credential using the current steps, and tests that it connects. Then she adds a manual trigger, and a Sheets node that gets rows from the orders sheet. When she runs it, the output shows fifteen items.

Next, she adds a Code node. For a simple rule like this, a few lines of code are short and clear. The code sets a limit of five thousand at the top. Then, for every item, it sets the flag to check if the amount is above the limit, and to ok if not. You'll see something like four items marked check, and the rest marked ok.

To write back, she adds a second Sheets node, with the update operation. She sets the column to match on to the order ID, and maps the flag field. She runs the whole workflow, opens the sheet, and the flag column is filled.

Then she notices a problem. One amount was typed as text, with a comma, so the comparison failed. She adds a small step to remove the comma and turn it into a number. Real data is always less tidy than you expect.

A common mistake is to use append when you mean update. The workflow runs without an error, but it adds fifteen new rows at the bottom, instead of filling the flag column. So before you write, ask: am I adding new records, or changing existing ones? For changes, use update, with a unique ID column to match on.

Let's recap. First, a Sheets workflow reads rows as items, changes them with Set, IF or Code nodes, and writes them back. Second, updating rows needs a unique ID column to match on. Appending adds new rows instead. Third, set up the Google credential with the current guide, and give it access to test data only.

Now it is your turn. In the exercise below this video, you will build the same orders workflow with your own threshold, then add one messy row and make the workflow handle it. It takes about forty minutes. In the next lesson, we add AI, with Calling the Claude API from n8n. See you there.
```
