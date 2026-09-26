# L04 Scoring Opportunities: Value, Feasibility and Risk | Presenter Script

Course: AI-27 · Video: 5 min · Words: 690

## Hook
Two AI ideas can promise the same value. One costs staff a few minutes when it is wrong. The other pays money to the wrong person when it is wrong. A good scoring method sees that difference before anyone writes code.

## Explain
Last time, you found opportunities that start from real user pain. Now you need to choose. You already know how to prioritise a backlog. For AI features, add one dimension that normal scoring often ignores: the cost of errors.

Score each idea from one to five on three dimensions. Value: how much it helps users and the business. Feasibility: do you have the data, the skills and a realistic technical path? And error cost: how bad is a wrong output? One means a user loses a few seconds. Five means financial, legal, safety or serious trust harm.

Because a high error cost is bad, flip it before you add. The total is value plus feasibility plus six minus error cost, with a maximum of fifteen. Keep the formula visible and the same for every idea, and write one sentence of reasoning next to each score. You can weight value more if your team prefers.

The numbers are not precise. Their purpose is to make the team state its assumptions, and argue about the right thing.

The most useful insight comes from ideas with high value and high error cost. Do not simply drop them. Ask whether a narrower scope lowers the error cost. Suggest instead of decide. Keep a human in the loop. Limit it to low stakes cases, or help staff instead of customers. Then score the narrow version as a new row.

Think of an investment committee. It does not only ask how much a project could earn. It also asks what could go wrong, and how much it would lose. A risky project might still be approved, but with a smaller first investment. Narrowing an AI feature is that smaller first investment.

## Demonstrate
Let's see it in action. Youssef Amrani is a PM at a hypothetical car insurance company in Morocco. His team has five AI ideas for the claims journey, and they score each one. In insurance, a wrong output can cost real money.

A plain language summary of claim status scores thirteen. A checklist of missing documents also scores thirteen. Both use data the company already has, and a wrong output is easy to notice and correct. Flagging possible fraud for human reviewers scores ten.

Automatically approving small claims has the highest value, but a very high error cost. A wrong approval pays money, and a wrong rejection harms a customer. It scores nine. So Youssef writes a narrower version: suggest approve or refer, and a claims officer confirms every decision.

The narrow version scores four, three and two, for a total of eleven. It is now a serious candidate, and it creates labelled data from officer decisions that could support a wider version later. That is a lower risk first step.

Repair cost from photos scores only eight, because the company has few labelled photos. Youssef notes it as a data problem to revisit, not a dead idea. His top three are the status summary, the checklist and the narrow approval suggestion, each with one sentence of reasoning.

A common mistake is scoring only value and feasibility, so the most dangerous ideas rise to the top. Always score error cost separately, and test a narrower scope first. Others make the opposite mistake, and give up on any high risk idea.

## Recap
Let's recap. First, score AI opportunities on value, feasibility and error cost, with the same formula for every idea. Second, feasibility depends mostly on data. An idea without examples is not ready, however valuable. Third, for high value, high risk ideas, score a narrower version with human confirmation before you decide.

## CTA
Now it is your turn. In the exercise below, score your ideas from the last lesson in a Google Sheets matrix and choose your top three, with one sentence of reasoning each. It takes about twenty five minutes. In the next lesson, we look at scoping an MVP AI feature. See you there.

## Thumbnail
Headline: Score the Cost of Errors
Image: Navy background, a three-column score card labelled V, F and E with teal bars, the E column highlighted, headline in teal Inter Bold.

## Production Notes
- [VERSION] Google Sheets formula and sorting features used in the exercise must be checked before recording.
- Youssef Amrani and the car insurance company in Morocco are hypothetical; no real insurer names or logos in stock footage.
- The scoring table slide must match content.md exactly: A 13, B 8, C 13, D 10, E 9, E2 11. The formula is shown on screen, not read symbol by symbol.
