# L02 How an Agent Works: The Agent Loop | Presenter Script

Course: AI-16 · Video: 5 min · Words: 739

## Hook
A language model on its own can only produce text. It cannot open a file, check a database, or send a message. So how does an agent finish a task with several steps? The answer is a simple loop that your software runs around the model.

## Explain
Last time, you saw that an agent chooses its own next step. Today, we see how. An agent repeats four actions until it has to stop.

First, observe. Collect the current situation: the task, the conversation so far, and the results of earlier steps. Second, decide. Send all of this to the model. The model replies with either a final answer, or a request to use a tool.

Third, act. Your software, not the model, runs the tool and gets a result. Fourth, check. Add that result to the situation, and go back to the start.

The loop stops when the model gives a final answer, or when it reaches a limit on steps, time or cost. Always set a maximum. Without one, a confused agent can call tools again and again.

Every agent has four parts. The model makes the decisions. The tools are the actions it may request, each with a name, a description and the inputs it expects. The memory is what it can see from earlier steps. And the instructions describe the goal, the rules, the tone, and when to stop or ask a person.

The agent can only do what its tools allow. So the tool list is your main safety control.

Here is a way to picture it. Think of a detective on a case. The detective looks at the evidence, decides which witness to interview next, goes to the interview, and adds the new facts to the case file.

The detective repeats this until the case is solved, or the manager says, stop, we are out of time. The detective is the model. The interviews are the tools. The case file is the memory. And the manager's brief is the instructions.

In code, the loop is short. On screen is some pseudocode. While the step count is under the maximum, ask the model to decide. If it gives a final answer, stop. If not, run the tool it asked for, save the result, and count one more step.

## Demonstrate
Let's follow one run. Priya Raman works in finance at a consultancy in Chennai, India. She designs an expense-checking agent, using sample data only.

Her instructions say: check each claim against the travel policy, flag any problem with a reason, and never approve or reject a claim yourself. The agent has three tools. One reads a receipt. One looks up the policy. One flags a claim. It may use at most six tool calls.

The task is: check claim one hundred and four. The agent decides to read the receipt. The result is a meal for three people, with an amount above the usual level.

Next, it decides to look up the policy for meals. The result is a limit per person, and a rule that client meals need the client name.

The amount per person is over the limit, and no client name is given. So it flags the claim with both reasons. Then it gives its final answer: claim one hundred and four is flagged for review, with two issues. The loop stops.

Notice what the agent did not do. It did not reject the claim. A person makes that decision, using the agent's reasons.

A common mistake is to think the model runs the tools itself, or has access to the database. It does not. The model only asks for a tool. Your software decides whether to run it. That is good news, because you control exactly which actions are possible.

## Recap
Let's recap. First, an agent repeats observe, decide, act and check, until it gives a final answer or reaches a limit. Second, its four parts are the model, the tools, the memory and the instructions. Third, the model only requests tools. Your software runs them, which makes the tool list your main safety control.

## CTA
Now it is your turn. In the exercise below this video, you will draw the agent loop for a customer-support agent at an online bookshop. Label its tools, write its stop condition, and add a path to a person. It takes about twenty minutes. In the next lesson, we start building, with Setting Up n8n. See you there.

## Thumbnail
Headline: Inside the Agent Loop
Image: Navy background, a teal circular arrow with four stops (observe, decide, act, check) around a small model icon, headline in teal Inter Bold.

## Production Notes
- No facts to verify: the lesson is conceptual, uses pseudocode rather than a real API, and uses a hypothetical example (content.md Review Flags: None).
- Scene with the code slide shows the pseudocode loop from content.md; the voiceover describes it and does not read it. Label the slide 'Pseudocode, not a real library'.
- Priya Raman and her Chennai consultancy are fictional; the expense claim uses sample data only.
