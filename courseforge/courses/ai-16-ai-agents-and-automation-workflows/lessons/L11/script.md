# L11 Memory and Context | Presenter Script

Course: AI-16 · Video: 5 min · Words: 675

## Hook
Ask your agent, what does product P zero four one two cost? And then, how many are in stock? Without memory, the second question makes no sense to it. With too much memory, it becomes slow, expensive and confused. Today, you find the right amount.

## Explain
Here is the key fact. A model has no memory between API calls. Each request must contain everything the model should know. So memory in an agent is simply the information your system chooses to send again. There are two kinds.

Short-term memory is the recent conversation. In n8n, you connect a memory node, such as Simple Memory, to the agent. Two settings matter. The session key says which conversation the memory belongs to. Each user needs their own key, or conversations will mix. And the window length says how many recent exchanges to keep. Older ones are dropped.

Longer-term context is information the agent looks up only when it needs it. For example, a customer's order history, a policy document, or notes from an earlier case. You give the agent a tool to fetch it. This is usually better than putting everything into memory.

More memory is not always better. Cost: every remembered message is sent again with each request. Confusion: long, mixed histories can lead the model to use old details. And privacy: anything stored may include personal data. Rules on this differ by country. So store only what the task needs, and use sample data in this course.

Picture a receptionist. Short-term memory is the notepad on the desk: the last few things the visitor said. Longer-term context is the filing cabinet. The receptionist opens the right file only when needed.

A receptionist who copies every old file onto the notepad cannot find anything. And a notepad left on the desk may be read by the wrong person.

## Demonstrate
Let's test it. Elena Popescu runs a travel agency in Bucharest, Romania. Her agent answers questions about invented tour packages from a sheet. It is built like the agent from the last lesson, with no memory yet.

She asks: what is the price of the Danube Delta tour? Then: is it available in May? You'll see something like: which tour do you mean? Without memory, the second question has lost its subject.

She connects a Simple Memory node, with the session key from the chat, and a window of two. Then she holds a six-turn conversation: the tour, the price, May, a group of eight, a second tour, and finally, so for the first tour, what is the total for my group?

At turn six, the agent asks which tour she means. The first tour and the group size have dropped out of the window.

She changes the window to six, and repeats. Now the answer is correct. But the execution log shows more input tokens on each later turn. So she settles on a window of four, and adds a rule to the system message: when a question refers to details you do not have, ask for them.

A common mistake is to think the agent remembers a customer because it answered well yesterday. In a new session, the details are gone. Another is to set a huge window and store full personal details, to be safe. Decide what the agent really needs, and fetch records with tools.

## Recap
Let's recap. First, the model itself remembers nothing. Memory is the history your system sends again with each request. Second, keep a short window of recent messages, and fetch longer-term records with tools. Third, more memory costs more tokens, can confuse the model, and may store personal data, so keep only what the task needs.

## CTA
Now it is your turn. In the exercise below this video, you will add memory to your agent, hold a six-turn conversation, and note where it forgets. Then change the window size, compare the tokens, and justify your choice. It takes about thirty minutes. In the next lesson, we add Human-in-the-Loop Approval. See you there.

## Thumbnail
Headline: How Much Should It Remember?
Image: Navy background, a small notepad beside a filing cabinet with one drawer open, a teal slider labelled window size above them, headline in teal Inter Bold.

## Production Notes
- [VERSION] n8n memory sub-node name (Simple Memory, earlier Window Buffer Memory), session key and context window length settings, and AI Agent node connections must be checked against the current release.
- [REGION] Storing personal data in memory or Google Sheets and sending it to an external API may be restricted by local data protection law; the lesson uses invented sample data only. The voiceover says the rules differ by country and names none.
- The agent replies in the demo ('Which tour do you mean?') and the token growth are example outputs.
- Elena Popescu, her Bucharest travel agency and the tour packages are fictional.
