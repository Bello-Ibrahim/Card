# L08 Making the AI Part Work: Prompts and Quality Checks | Presenter Script

Course: AI-28 · Video: 5 min · Words: 685

## Hook
Your prototype works on the example you tried. But your users will not type your example. They will write in a hurry, make spelling mistakes, and ask for things you never imagined. How do you know the AI part will still work?

## Explain
In the last lesson, you built a working prototype. Now we make the AI part reliable. AI models do not give the same quality every time, and they can be confidently wrong. You cannot remove this risk completely, but you can reduce it and plan for it.

The first tool is clear instructions. A good product prompt gives the role and the task, the rules, the format, and what to do when unsure. For example: if a review mentions food poisoning or a legal threat, do not reply. Output only, needs human.

The second tool is good examples. Show the model one or two examples of a good input and a good output. Examples often teach style and format better than long explanations. Keep them short, and make sure they follow every rule in your prompt.

The third tool is a small test set: a list of inputs, each with a description of a good answer. Include normal cases, difficult cases, and cases the AI should refuse. Every time you change the prompt, run the whole set again, because fixing one case can break another. Score each result as pass, partial or fail. Your pass rate is passes divided by cases.

You also need a fallback plan, what the product does when the AI is wrong or unsure. It can send the case to a person, ask the user for more information, or show a draft only after a human approves it. In health, money or law, a human check is often necessary.

Picture a busy restaurant. A new chef follows the recipe card exactly. That is your prompt. The head chef tastes each dish before it leaves the kitchen. That is your quality check. And if a dish is wrong, it goes back to the kitchen, not to the customer. That is your fallback plan.

## Demonstrate
Let's see it in practice. Putri is a made up founder in Yogyakarta, Indonesia. Her MVP writes draft replies to online reviews for small restaurants, in Indonesian or English.

She writes fifteen made up test cases. Six are normal reviews. Four are difficult, with mixed languages, spelling mistakes or sarcasm. Three should be refused, such as food poisoning. And two are tricky, like a review asking for a discount.

Prompt version one passes nine of fifteen. Two replies offered a free dessert. Two sarcastic reviews got cheerful thanks. And two cases that should be refused got normal replies.

For version two, she adds a rule, never offer anything for free. She adds one example of a sarcastic review with a good reply, and a clearer list of topics that need a human. Now thirteen of fifteen pass, and both refusal failures are fixed.

Putri decides thirteen of fifteen is good enough for a first test, because the restaurant owner approves every draft before it is posted. That human approval is her fallback plan. She keeps the two failures in her test set for the next round, so she can see if a later change fixes them.

A common mistake is testing on two or three easy examples, then moving on. Another is assuming a bigger model fixes everything. You only know if it helps by running the same test set. And never use real customer data in tests without permission.

## Recap
Let's recap. First, clear instructions, one or two good examples, and a small test set make AI output more reliable. Second, run the whole test set after every prompt change, and score each case. Third, plan what the product does when the AI is wrong or unsure.

## CTA
Now it is your turn. In the exercise below this video, write fifteen test cases for your MVP, run them, score the results, and improve your prompt until most cases pass. It takes about fifty minutes. Next, we look at the unit economics of an AI product. See you there.

## Thumbnail
Headline: Test the AI Part
Image: Navy background, a checklist with green ticks, one amber half-tick and one red cross beside a chat bubble, headline in teal Inter Bold.

## Production Notes
- No facts to verify: Putri and her test cases are hypothetical; the lesson names no model, price or tool feature (content.md Review Flags: None).
- Putri (Yogyakarta, Indonesia) is fictional. Review texts on screen are made up; no real restaurant names or reviewer names.
- Pass rates spoken: 9 of 15 (v1), 13 of 15 (v2). Keep slide numbers in sync if the example changes.
