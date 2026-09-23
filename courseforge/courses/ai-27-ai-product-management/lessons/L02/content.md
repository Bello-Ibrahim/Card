# L02 The AI Capability Menu

Course: AI-27 · Module: M1 · Objectives: O1 · Video: 5 min

## Hook
"Let's add AI" is not a product decision. "Let's predict delivery time from past trips" is. The first step from a vague idea to a real feature is naming which kind of AI capability you actually need, and sometimes discovering that you need none.

## Explanation
Most AI features use one of six capability types. Knowing them helps you talk clearly with engineers and choose the simplest option.

1. **Prediction** estimates a number or a future value from past data: a price, a time, a demand level. Output: a number, ideally with a range.
2. **Classification** puts an input into one of a fixed set of groups: spam or not spam, urgent or normal, which product category. Output: a label and often a confidence score.
3. **Generation** creates new content: text, images, code or audio. Large language models such as Claude belong here. Output: new content that did not exist before, so it can contain invented details.
4. **Retrieval** finds the most relevant existing items for a query, such as help articles or documents. It is often combined with generation, so the model answers from retrieved sources instead of from memory.
5. **Recommendation** ranks items for a specific user based on their behaviour and similar users: products, songs, courses.
6. **Agents** are systems where a model plans steps and uses tools to complete a task, such as searching, filling a form and sending a message. They can do more, so they can also go wrong in more ways.

The capabilities differ in risk. Classification and prediction have fixed output types, so they are easier to test. Generation and agents produce open-ended outputs and actions, so testing and guardrails take more work.

**Choose the simplest capability that solves the problem.** Many problems need no AI at all. A fixed business rule, a sort order or a good form may be clearer, cheaper and always correct. Use AI when the task needs judgement across many varied cases that people cannot write rules for.

**Analogy:** Think of a hardware shop. A saw, a drill and a power multi-tool can all make a hole in wood. The multi-tool can do the most, but it is heavier, more expensive and easier to use badly. A good builder picks the simplest tool that does the job well. Agents and generation are the multi-tools of AI.

## Worked Example
Three hypothetical product teams show the menu in use.

**Priya Raman, India, agriculture app.** Farmers ask, "Should I sell my onions now or in two weeks?" Priya's team first imagined a chatbot. After discussion, they see the core need is **prediction**: an expected price range for the next two weeks, based on past market prices, season and local supply data. A chatbot could explain the prediction later, but the value comes from the number and its range.

**Emeka Obi, Nigeria, delivery service.** Customers want to know when their parcel will arrive in Lagos traffic. This is **prediction** again: a delivery-time estimate from past trips, time of day and route. Emeka also wants to sort incoming complaints into "late", "damaged" and "wrong address". That is **classification**, a separate feature with its own data and tests.

**Agnieszka Nowak, Poland, online home-goods shop.** She wants "customers who bought this also liked" on product pages. This is **recommendation**. She also wants a help assistant that answers delivery questions from the shop's policy pages. That is **retrieval plus generation**. She drops an idea for an "AI discount calculator": discounts follow fixed rules, so normal code is the right tool.

## Common Mistake
The most common mistake is to start from the most exciting capability, often a chatbot or an agent, and then look for a problem it could solve. This produces features that are expensive, hard to test and not clearly better than a simple alternative. Start from the user task, name the output the user needs (a number, a label, a ranked list, text or a completed action), and let that output choose the capability.

## Key Takeaways
1. The six main capability types are prediction, classification, generation, retrieval, recommendation and agents, and each produces a different kind of output.
2. Open-ended capabilities such as generation and agents are more flexible but need more testing and guardrails than prediction or classification.
3. Choose the simplest capability that solves the user's problem, and remember that many ideas need a rule or a better design instead of AI.

## Hands-on Exercise
**Task:** Sort 12 product ideas by capability type on a FigJam board and mark the ones that do not need AI.
**Tools:** FigJam (free plan) or any whiteboard tool; sticky notes on paper also work [VERSION].
**Steps:**
1. Create a board with seven columns: the six capability types and "No AI needed".
2. Add these 12 ideas as sticky notes: estimate next month's demand for a café; tag support tickets by topic; write product descriptions from a spec sheet; find the right help article for a question; suggest courses to a learner; book a meeting by checking calendars and sending invites; calculate sales tax; flag possibly fake reviews; forecast energy use for a building; answer questions about an employee handbook; sort orders by date; draft a reply to a customer email.
3. Place each note in one column. If an idea combines two types, place it in the main one and draw an arrow to the second.
4. For each note in "No AI needed", write the simpler solution on it.
5. Add two ideas from your own product and place them too.
**What good looks like:** Every note is in a column with a clear reason. Sales tax and sorting by date are in "No AI needed". The handbook question is marked as retrieval plus generation, and the meeting booking is marked as an agent with a note about its extra risk.
**Time:** about 20 minutes

## Review Flags
- [VERSION] FigJam free-plan limits must be checked before recording.
