# L11 Memory and Context

Course: AI-16 · Module: M3 · Objectives: O2, O4 · Video: 5 min (screen demo)

## Hook
Ask your agent, "What does product P-0412 cost?" and then, "And how many are in stock?" Without memory, the second question makes no sense to it. With too much memory, it becomes slow, expensive and confused. Today you find the right amount.

## Explanation
A model has no memory between API calls. Each request must contain everything the model should know. "Memory" in an agent is simply the information your system chooses to send again. There are two kinds.

**Short-term memory** is the recent conversation: the last few user messages, agent replies and tool results. In n8n you connect a memory sub-node, such as **Simple Memory** (earlier called Window Buffer Memory), to the AI Agent node. [VERSION] Two settings matter:

- **Session key:** which conversation the memory belongs to. Each user or chat needs its own key, or conversations will mix. [VERSION]
- **Context window length:** how many recent exchanges are kept. Older ones are dropped. [VERSION]

**Longer-term context** is information the agent looks up when it needs it, instead of carrying it all the time: a customer's order history in a sheet, a policy document, notes from an earlier case. You give the agent a tool to fetch it (L09, L10). This is usually better than putting everything into memory.

**More is not always better:**

- **Cost:** every remembered message is sent again with each request, so tokens grow with the conversation.
- **Confusion:** long, mixed histories can lead the model to use old or unrelated details.
- **Privacy:** anything stored may include personal data. Store only what the task needs, keep it only as long as needed, and use sample or anonymised data in this course. Data protection rules on storing personal data and sending it to an external API differ by country. [REGION] Do not paste real personal or confidential data into the agent.

A good design keeps a short window of recent messages, fetches records with tools when needed, and stores long-term notes only with a clear reason.

**Analogy:** Short-term memory is the notepad on a receptionist's desk: the last few things the visitor said. Longer-term context is the filing cabinet: the receptionist opens the right file only when needed. A receptionist who copies every old file onto the notepad cannot find anything, and a notepad left on the desk may be read by the wrong person.

## Worked Example
Elena Popescu runs a hypothetical travel agency in Bucharest, Romania. Her agent answers questions about invented tour packages from a sheet. On screen, she:

1. Opens her L10-style agent with a Chat Trigger, AI Agent, Anthropic Chat Model and a Sheets tool for "tours". [VERSION]
2. Without memory, she asks: "What is the price of the Danube Delta tour?" then "Is it available in May?" The agent replies, "Which tour do you mean?" (example output)
3. Connects a **Simple Memory** node with the session key from the chat and a context window length of 2. [VERSION]
4. Holds a 6-turn conversation: tour name, price, May availability, group size of 8, a question about a second tour, then "So for the first tour, what is the total for my group?"
5. At turn 6 the agent asks which tour she means. The first tour and the group size have dropped out of the window. (example output)
6. Changes the window length to 6 and repeats. Now the agent answers correctly, but the execution log shows more input tokens on each later turn.
7. Decides on a window of 4, plus a system message rule: "When a question refers to earlier details you do not have, ask for them."

## Common Mistake
Learners often think the agent "remembers" a customer because it answered well yesterday. In a new session, or after the window moves on, the details are gone. Others set a very large window and store full personal details in memory "to be safe". Decide what the agent really needs, fetch records with tools, and do not keep personal data without a clear purpose.

## Key Takeaways
1. The model itself remembers nothing; memory is the history your system sends again with each request.
2. Keep a short window of recent messages and fetch longer-term records with tools when they are needed.
3. More memory costs more tokens, can confuse the model, and may store personal data, so keep only what the task needs.

## Hands-on Exercise
**Task:** Add conversation memory to your agent, hold a 6-turn conversation, note where it forgets earlier details, then change the memory size and compare.
**Tools:** n8n self-hosted; your L10 agent; Google Sheets; Claude API.
**Steps:**
1. Connect a Simple Memory node to your L10 agent with a context window length of 2. [VERSION]
2. Plan a 6-turn conversation in which turn 6 depends on a detail from turn 1 or 2.
3. Hold the conversation and write down the turn where the agent first forgets something.
4. Repeat with a window of 6. Compare the answers and the input tokens of the last turn in the execution log.
5. Choose a window size and write two sentences to justify it using cost and accuracy.
6. Check what your memory stores. Confirm that it contains only invented sample data. [REGION]
**What good looks like:** A clear record of when the agent forgot, a token comparison between the two sizes, and a justified choice that balances accuracy and cost.
**Time:** about 30 minutes

## Review Flags
- [VERSION] n8n memory sub-node name (Simple Memory, earlier Window Buffer Memory), session key and context window length settings, and AI Agent node connections must be checked against the current release.
- [REGION] Storing personal data in memory or Google Sheets and sending it to an external API may be restricted by local data protection law; the lesson uses invented sample data only.
