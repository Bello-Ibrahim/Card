# L02 The AI Capability Menu | Presenter Script

Course: AI-27 · Video: 5 min · Words: 700

## Hook
Let's add AI is not a product decision. Let's predict delivery time from past trips is. The first step from a vague idea to a real feature is naming the capability you need, and sometimes finding that you need none.

## Explain
In the last lesson, we saw that AI features give likely answers. Today we look at the menu. Most AI features use one of six capability types. Knowing them helps you talk clearly with engineers, and choose the simplest option.

Prediction estimates a number or a future value from past data, such as a price, a time or a demand level. Ideally it gives a range. Classification puts an input into one of a fixed set of groups, such as urgent or normal. It gives a label, and often a confidence score.

Generation creates new content, such as text, images, code or audio. Large language models like Claude belong here. Because the content is new, it can contain invented details. Retrieval finds the most relevant existing items, such as help articles. It is often combined with generation, so the model answers from real sources instead of from memory.

Recommendation ranks items for a specific user, based on their behaviour and similar users. And agents are systems where a model plans steps and uses tools to finish a task, such as searching, filling a form and sending a message. They can do more, so they can also go wrong in more ways.

These types differ in risk. Prediction and classification have fixed output types, so they are easier to test. Generation and agents produce open outputs and actions, so testing and guardrails take more work. Keep this in mind when you estimate the work.

Think of a hardware shop. A saw, a drill and a power multi tool can all make a hole in wood. The multi tool can do the most, but it is heavier, more expensive and easier to use badly. A good builder picks the simplest tool that does the job. Agents and generation are the multi tools of AI.

And many problems need no AI at all. A fixed rule, a sort order or a good form may be clearer, cheaper and always correct. Use AI when the task needs judgement across many varied cases that people cannot write rules for.

## Demonstrate
Let's use the menu with three hypothetical teams. Priya Raman builds an agriculture app in India. Farmers ask whether they should sell their onions now or in two weeks. The team first imagined a chatbot.

But the real need is prediction: an expected price range for the next two weeks, from past market prices, season and local supply. A chatbot could explain it later. The value comes from the number and its range.

Emeka Obi runs a delivery service in Nigeria. Customers want to know when their parcel will arrive in Lagos traffic. That is prediction again. He also wants to sort complaints into late, damaged and wrong address. That is classification, a separate feature with its own data and tests.

Agnieszka Nowak runs an online home goods shop in Poland. Customers who bought this also liked is recommendation. A help assistant that answers from the shop's policy pages is retrieval plus generation. And an AI discount calculator? She drops it. Discounts follow fixed rules, so normal code is the right tool.

The common mistake is to start from the most exciting capability, often a chatbot or an agent, and then look for a problem. Start from the user task. Name the output the user needs, and let that output choose the capability.

## Recap
Let's recap. First, the six types are prediction, classification, generation, retrieval, recommendation and agents, and each gives a different output. Second, generation and agents are flexible, but need more testing and guardrails. Third, choose the simplest capability that solves the problem, and remember that many ideas need a rule instead of AI.

## CTA
Now it is your turn. In the exercise below, you will sort twelve product ideas by capability type on a FigJam board, and mark the ones that need no AI. It takes about twenty minutes. In the next lesson, we look at finding AI opportunities in your product. See you there.

## Thumbnail
Headline: Pick the Simplest Tool
Image: Navy background, a menu card with six small teal icons (chart, tag, pen, magnifier, star list, robot arm) and a seventh greyed-out 'no AI' icon, headline in teal Inter Bold.

## Production Notes
- [VERSION] FigJam free-plan limits must be checked before recording (exercise tool).
- Priya Raman (India), Emeka Obi (Nigeria) and Agnieszka Nowak (Poland) and their companies are hypothetical; no real brands or logos in stock footage.
- Claude is named only as an example of a large language model, as in content.md.
