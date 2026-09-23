# L02 The Anatomy of a Strong Prompt

Course: AI-03 · Module: M1 · Objectives: O1 · Video: 5 min

## Hook
Most strong prompts are built from the same six parts. Once you know them, you can look at any weak prompt and quickly see what is missing.

## Explanation
A structured prompt can contain six parts. You do not need all six every time. Think of them as a checklist.

1. **Role**: the point of view the AI should take. "You are an experienced HR officer." A role often helps with tone and vocabulary.
2. **Task**: the action you want, with a clear verb. "Write", "summarise", "compare", "list". The task is the only part you always need.
3. **Context**: the background the AI cannot know. Who the audience is, why you need this, and what the situation is. You will study context in L03.
4. **Format**: the shape of the output. An email, a table, five bullet points, a slide outline. You will study format in L04.
5. **Constraints**: limits and rules. A word limit, words to avoid, facts that must be included, a reading level.
6. **Examples**: a sample of what good output looks like. You will study examples in L05.

When is each part worth adding? A quick question, such as "What is a purchase order?", needs only a task. A document that other people will read usually needs task, context, format and constraints. A role helps when tone or expertise matters. Examples help most when you want a specific style or a repeated pattern.

The order is flexible. Many people write role and task first, then context, then format and constraints. What matters is that each part is clear and that the parts do not contradict each other.

**Analogy:** A structured prompt is like a good order form for a print shop. The shop needs to know what you want printed (task), for which event (context), in what size and paper (format), by which date and within which budget (constraints), and it helps if you bring a sample (example). Leave out a field, and the shop has to guess.

## Worked Example
Amara is an HR officer at a hypothetical logistics company in Lagos. She needs a job advert for a logistics coordinator.

Before:

```text
Write a job advert.
```

The result is a general advert with invented benefits and no details about the job.

After:

```text
You are an experienced HR officer at a mid-sized logistics company.
Write a job advert for a Logistics Coordinator based in Lagos.
The person will schedule deliveries for about 20 trucks, work with
warehouse staff and update customers on delays. We need 2+ years of
experience in logistics and good spreadsheet skills.
Format: a short introduction, then "Responsibilities" and
"Requirements" as bullet lists, then how to apply.
Keep it under 250 words, use inclusive, plain language, and do not
invent salary figures or benefits.
```

Amara labels the parts for her team:

- Role: "You are an experienced HR officer..."
- Task: "Write a job advert for a Logistics Coordinator."
- Context: the trucks, the warehouse staff, the experience needed.
- Format: introduction, two bullet lists, how to apply.
- Constraints: under 250 words, inclusive language, no invented salary or benefits.
- Examples: not used this time, because the format is already clear.

The new advert is specific and ready for her manager to review. The constraint "do not invent salary figures" is important. AI tools often fill gaps with plausible details, so it is safer to say what the tool must not add.

## Common Mistake
Some learners think a longer prompt is always a better prompt. They add every part, repeat themselves and include background that does not matter. Long prompts can hide the task and create conflicting instructions. Use the six parts as a checklist, not as a form you must fill completely. Add a part when it changes the result.

## Key Takeaways
1. The six parts of a structured prompt are role, task, context, format, constraints and examples.
2. Only the task is always needed. Add the other parts when they change the result, especially for documents other people will read.
3. Constraints such as "do not invent figures" help reduce made-up details.

## Hands-on Exercise
**Task:** Rewrite three weak prompts using the six parts, run one of them, and label each part.
**Tools:** Claude or ChatGPT (free tier) [VERSION]; a notes app.
**Steps:**
1. Take these three weak prompts: "Write a product description." "Make a training plan." "Reply to this complaint."
2. For each one, invent a realistic, hypothetical work situation, for example a coffee brand in Colombia, a new cashier at a supermarket in Poland, or a late parcel for an online shop in Kenya.
3. Rewrite each prompt with at least four of the six parts.
4. Run one rewritten prompt in Claude or ChatGPT.
5. In your final version, label each part in brackets, for example "(Role)", "(Task)", "(Constraints)".
6. Write one sentence about which part changed the output the most.
**What good looks like:** Three rewritten prompts, each with a clear task and at least three other labelled parts. The prompt you ran produced a specific, usable output. No real names or confidential details are included.
**Time:** about 20 minutes

## Review Flags
- [VERSION] Free-tier availability of Claude and ChatGPT must be checked before scripting.
