# L01 From Scripts to Agents | Presenter Script

Course: AI-16 · Video: 5 min · Words: 742

## Hook
Two teams want to use AI agents. One needs to copy invoice totals into a spreadsheet every morning. The other needs to answer unusual customer questions that nobody can predict. Only one of them needs an agent. Let's find out which one, and why.

## Explain
Hi, and welcome to AI Agents and Automation Workflows. In this first lesson, we look at a simple idea. Automation is not one thing. It is a spectrum, with three main points.

The first point is a fixed workflow, with rules only. Something starts a run, and the same steps follow every time. It is fast, cheap and easy to test. But it fails when the input does not match what the rules expect.

The second point is a workflow with an AI step. The path is still fixed, but one step asks a language model to do something that rules do badly, such as summarise a message, classify it, or pull out details from free text. The model does not decide what happens next. Your workflow does.

The third point is an agent. The model gets a goal, a set of tools and some instructions. It chooses its own next step, uses a tool, looks at the result, and decides again, until it reaches the goal or a stop condition. Nobody writes the path in advance.

As you move from one to three, you gain flexibility. But you also pay more, because an agent may call the model many times for one task. Results are harder to predict. And risk grows, because the system can take actions you did not plan for.

Here is a simple way to picture it. A fixed workflow is a recipe that a cook follows exactly. Same ingredients, same order, same result.

An agent is a chef who opens the fridge, sees what is there, and decides what to cook. The chef can handle surprises. But you cannot be sure what will arrive on the plate, and the chef may use expensive ingredients.

For a school canteen that serves the same meal to five hundred children, you want the recipe.

In this course, you will use five building blocks. A trigger starts a run. A node is one step, like reading a sheet or checking a condition. A tool is an action an agent may choose. Memory is what the agent keeps between steps. And the agent loop is the repeated cycle of decide, act and check.

## Demonstrate
Let's use this on a real list. Tomás Herrera manages operations at a logistics company in Montevideo, Uruguay. He has three tasks to automate.

Task one. Every night, copy the delivery counts from a scanner export into a report sheet. The format never changes. So this is a fixed workflow. Rules are cheaper, and always correct.

Task two. Read driver notes, such as gate locked, left with neighbour, and tag each one as delivered, failed, or needs follow-up. The notes are free text, so a model helps. But the next step for each tag is known. That is a workflow with an AI step.

Task three. A customer writes: my parcel is late, can I change the address, and why was I charged twice? The steps depend on the message. Check tracking, check billing, maybe draft an address change. This is where an agent makes sense.

But notice the limits. Tomás does not let the agent issue refunds or change addresses on its own. It may look up data and draft replies, but a person approves any change. That keeps the flexibility, and limits the risk.

One common mistake is to start with an agent because it sounds more advanced. Teams then find it is slower, costs more per task, and sometimes takes a different path for the same input.

## Recap
Let's recap. First, automation is a spectrum: fixed workflow, workflow with an AI step, and agent. Each step to the right adds flexibility, cost and risk. Second, an agent chooses its own next step, while a workflow follows your path. Third, choose the least freedom that solves the problem, and limit what an agent may do alone.

## CTA
So, which team needed an agent? The one with unpredictable customer questions. Now it is your turn. In the exercise below this video, you will sort eight business tasks into the three types, and justify two of your choices. It takes about fifteen minutes. In the next lesson, we look inside the agent loop. See you there.

## Thumbnail
Headline: Recipe or Chef?
Image: Navy background, a split card: a printed recipe card on the left and a chef's hat above an open fridge on the right, headline in teal Inter Bold.

## Production Notes
- No facts to verify: the lesson is conceptual and uses hypothetical examples (content.md Review Flags: None).
- Tomás Herrera and his Montevideo logistics company are fictional; do not show a real company name or logo in stock footage.
- The eight exercise tasks are shown on the lesson page, not read aloud in the video.
