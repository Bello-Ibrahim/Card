# HeyGen Batch Pack: AI-28 M2 (Building the Lean MVP)

Course: Building an AI Startup. Make one HeyGen video per lesson below, using these settings for every video.

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

## L06 Scoping the MVP

- **Filename:** `ai-28-building-an-ai-startup_M2_L06_presenter.mp4`
- **Expected length:** about 4.8 minutes (676 words). The quality gate accepts ±10%.

```text
Your list of features is probably long: accounts, a dashboard, five languages, a mobile app, reports. If you build all of it, months may pass before anyone uses it. What is the smallest thing you could build next week that would teach you the most?

Welcome to week two. Last week, you found and tested a problem, and asked how to defend your idea. Now we start building, and the first step is deciding what not to build.

MVP means minimum viable product. It is the smallest product that lets real users do one important job, so you can test your riskiest assumption. An assumption is something you believe but have not proved. The riskiest one is the belief that would sink the whole business if it were wrong.

For example, users will trust the AI's answer enough to act on it. Or, the AI can produce a good enough result for this type of document.

To scope an MVP, answer five questions. What is the core job, the one task the user must complete? What is the riskiest assumption? What is in, meaning what you must build? What can you do by hand for now? And what is out, even if it is attractive?

Then define a success measure, the number that tells you whether the assumption is true. For example, eight of ten test users complete the core job without help. A lean MVP is not a poor product. The part you build should work well. It is simply narrow.

Think of a road engineer who wants to know whether a new bridge is needed. She does not build the whole bridge. First, she runs a small ferry and counts the people who use it. The ferry is small, but it answers the real question: do people need to cross here?

Let's scope a real idea. Valentina is a made up founder in Buenos Aires, Argentina. Her interviews showed that many tenants sign rental contracts they do not fully understand. Her big vision is an AI assistant that explains any legal document in plain Spanish.

That vision is too wide for an MVP. There are hundreds of document types, each with its own rules. So she narrows it to one document type, for one kind of user, and writes a one page scope.

The core job: a tenant uploads one rental contract and gets a plain language summary of the key terms, with a list of clauses to ask a lawyer about. The riskiest assumption: tenants find the summary clear and useful before signing, and it is accurate.

In: an upload form, one AI step with a fixed structure, and a results page that clearly says this is not legal advice. By hand: a lawyer friend reviews every summary in the first month, and results go by email. Out: other documents, accounts, payments, a mobile app and other languages.

Her success measure: in one month, twenty tenants use it, the lawyer rates at least seventeen summaries as accurate, and at least twelve tenants say it helped them ask better questions. She also removes personal details before sending any contract to an AI model.

A common mistake is treating the MVP as version one of the full product, only faster. Founders build accounts, payments and settings first, and none of it tests the riskiest assumption. Another mistake is refusing manual work because it does not scale. At this stage, manual work is a tool for learning.

Let's recap. First, an MVP is the smallest product that lets users complete one core job and tests your riskiest assumption. Second, decide clearly what is in, what is done by hand, and what is out. Third, set a success measure with numbers before you start building.

Now it is your turn. In the exercise below this video, write a one page MVP scope: the core job, the assumption you are testing, what is in, what is out, and the success measure. Try to cut at least one item. Next, we start building with no-code tools. See you there.
```

## L07 Building with No-Code Tools

- **Filename:** `ai-28-building-an-ai-startup_M2_L07_presenter.mp4`
- **Expected length:** about 5.1 minutes (710 words). The quality gate accepts ±10%.

```text
Can you build a working AI product without writing a single line of code? In this lesson, you will watch a prototype being built from start to finish. Then you will build your own.

In the last lesson, you scoped your MVP. Now we build it. A no-code builder is a tool where you build apps by choosing and connecting blocks on screen, instead of writing code.

Most no-code prototypes use four parts. A form, where the user enters information. A database, a table that saves each request, like a spreadsheet. An AI step, which sends the input and your instructions to an AI model. And an output page, where the user sees the result.

The AI step runs on a prompt, the instructions you give the model. In a product, the prompt runs every time a user presses the button, so it is part of your product. Write it carefully and save every version. Some builders connect to a provider with an API key, a secret password between programs. Keep it private.

A no-code builder is like construction toy bricks. You cannot make every shape, but you can quickly build a working model of a house and show it to people before you pour concrete.

Let's build one. Sipho is a made up founder in Durban, South Africa. Small plumbing businesses lose jobs because they send price quotes too slowly. His core job: a plumber enters job details and gets a clear, professional quote.

First, we draft the prompt with Claude. We ask for instructions that turn a plumber's short notes into a polite quote. Two rules matter most. Use only the prices the plumber enters, and never invent prices. If something is missing, list what is missing.

Next, in Glide, the builder we use here, we create a new blank app. Any no-code builder with a table, a form and an AI step will work. The buttons may simply have different names.

We add a table called Quotes. It has fields for the job description, materials and prices, labour hours, hourly rate, the quote text, and a status.

Then we add a form linked to the table, with the first four fields. All four are required, so a plumber cannot send an empty request.

Now the AI step. We add an AI column that generates text from each new row. We paste Prompt version one and insert the form fields where the builder allows. The answer is saved into the quote text field, and the status is set to draft.

Next, an output page shows the quote text, with a button to copy it. The core flow now runs from start to finish. It looks plain, and that is fine.

Time to test, with fake data only. Replace kitchen tap, tap four hundred and fifty, labour one hour at three hundred and fifty. We check that the quote uses only these numbers.

And here is a problem. The AI added a call out fee that Sipho never entered. So we add a rule to the prompt: do not add any fee that is not listed. We save it as Prompt version two and test again.

We also test a missing field. Without the hourly rate, the quote should ask for it, not invent it. Finally, we share the preview link with one test user and watch them finish the task without help.

If your free plan cannot run an AI step, you can still test the flow. Collect inputs with the form, make the result yourself with Claude, and send it back. That is the Wizard of Oz test from lesson four.

Let's recap. First, a no-code prototype usually connects a form, a database, an AI step and an output page. Second, the prompt is part of your product, so write it carefully, test it and save each version. Third, build and test the core flow before you add colours or extra pages.

Now it is your turn. In the exercise below this video, build a working prototype of your core flow with a free no-code builder and Claude. Test it with fake data, and watch one real user try it. Next, we look at making the AI part work, with prompts and quality checks. See you there.
```

## L08 Making the AI Part Work: Prompts and Quality Checks

- **Filename:** `ai-28-building-an-ai-startup_M2_L08_presenter.mp4`
- **Expected length:** about 4.9 minutes (685 words). The quality gate accepts ±10%.

```text
Your prototype works on the example you tried. But your users will not type your example. They will write in a hurry, make spelling mistakes, and ask for things you never imagined. How do you know the AI part will still work?

In the last lesson, you built a working prototype. Now we make the AI part reliable. AI models do not give the same quality every time, and they can be confidently wrong. You cannot remove this risk completely, but you can reduce it and plan for it.

The first tool is clear instructions. A good product prompt gives the role and the task, the rules, the format, and what to do when unsure. For example: if a review mentions food poisoning or a legal threat, do not reply. Output only, needs human.

The second tool is good examples. Show the model one or two examples of a good input and a good output. Examples often teach style and format better than long explanations. Keep them short, and make sure they follow every rule in your prompt.

The third tool is a small test set: a list of inputs, each with a description of a good answer. Include normal cases, difficult cases, and cases the AI should refuse. Every time you change the prompt, run the whole set again, because fixing one case can break another. Score each result as pass, partial or fail. Your pass rate is passes divided by cases.

You also need a fallback plan, what the product does when the AI is wrong or unsure. It can send the case to a person, ask the user for more information, or show a draft only after a human approves it. In health, money or law, a human check is often necessary.

Picture a busy restaurant. A new chef follows the recipe card exactly. That is your prompt. The head chef tastes each dish before it leaves the kitchen. That is your quality check. And if a dish is wrong, it goes back to the kitchen, not to the customer. That is your fallback plan.

Let's see it in practice. Putri is a made up founder in Yogyakarta, Indonesia. Her MVP writes draft replies to online reviews for small restaurants, in Indonesian or English.

She writes fifteen made up test cases. Six are normal reviews. Four are difficult, with mixed languages, spelling mistakes or sarcasm. Three should be refused, such as food poisoning. And two are tricky, like a review asking for a discount.

Prompt version one passes nine of fifteen. Two replies offered a free dessert. Two sarcastic reviews got cheerful thanks. And two cases that should be refused got normal replies.

For version two, she adds a rule, never offer anything for free. She adds one example of a sarcastic review with a good reply, and a clearer list of topics that need a human. Now thirteen of fifteen pass, and both refusal failures are fixed.

Putri decides thirteen of fifteen is good enough for a first test, because the restaurant owner approves every draft before it is posted. That human approval is her fallback plan. She keeps the two failures in her test set for the next round, so she can see if a later change fixes them.

A common mistake is testing on two or three easy examples, then moving on. Another is assuming a bigger model fixes everything. You only know if it helps by running the same test set. And never use real customer data in tests without permission.

Let's recap. First, clear instructions, one or two good examples, and a small test set make AI output more reliable. Second, run the whole test set after every prompt change, and score each case. Third, plan what the product does when the AI is wrong or unsure.

Now it is your turn. In the exercise below this video, write fifteen test cases for your MVP, run them, score the results, and improve your prompt until most cases pass. It takes about fifty minutes. Next, we look at the unit economics of an AI product. See you there.
```

## L09 Unit Economics of an AI Product

- **Filename:** `ai-28-building-an-ai-startup_M2_L09_presenter.mp4`
- **Expected length:** about 4.9 minutes (690 words). The quality gate accepts ±10%.

```text
A traditional app costs almost nothing extra when one more customer uses it. An AI product is different. Every time a customer presses the button, you pay the model supplier. So do you know which of your customers are making you money?

Last time, you made the AI part reliable. Now we check that it can pay for itself. Unit economics means looking at the money for one unit of your business, usually one customer per month. How much does one customer bring in, and how much does it cost to serve them?

Revenue per customer is what they pay you, such as a monthly plan. Cost to serve is everything you spend because that customer uses the product. Model usage, which suppliers usually charge by the amount of text processed. Your share of hosting and tools. Support time. And payment fees.

Gross profit is revenue minus cost to serve. Gross margin is gross profit as a percentage of revenue. It shows how much of each unit of money you keep, to pay for salaries, marketing and rent.

Two more terms. CAC, or customer acquisition cost, is what you spend on marketing and sales to win one new customer. The payback period is how many months of gross profit it takes to earn that back.

Think of an all you can eat restaurant. The price is fixed, but the cost depends on how much each guest eats. Most guests are profitable. A few very hungry guests cost more than they pay. The owner must know the average guest and the hungriest guest before setting the price. Your AI product works in the same way.

Let's do the maths. Karim is a made up founder in Marrakech, Morocco. His product drafts replies to guest messages for small guesthouses. All the prices here are placeholders, not real prices. Always check current prices on the day you calculate.

Karim charges twenty dollars a month. An average customer sends six hundred requests, at four tenths of a cent each. That is two dollars forty. Add one dollar fifty for hosting, two dollars for support, and a three percent payment fee, which is sixty cents. The total cost to serve is six dollars fifty.

So gross profit is twenty dollars minus six dollars fifty, which is thirteen dollars fifty a month. And the gross margin is thirteen fifty divided by twenty. That is sixty seven point five percent. So far, so good.

Now the heavy user. One large guesthouse sends five thousand requests a month. Model usage alone becomes twenty dollars. The total cost to serve becomes twenty four dollars ten. Karim loses four dollars ten on this customer, every month.

Finally, CAC and payback. Karim spent three hundred dollars on local advertising and won ten customers. So his CAC is thirty dollars. Thirty divided by thirteen fifty gives a payback period of about two point two months. An average customer must stay more than two months before he earns back the cost of winning them.

So Karim makes three decisions. He adds a usage limit to the twenty dollar plan. He creates a higher priced plan for large guesthouses. And he shortens his prompts to reduce model usage per request. Each change protects his margin without making the product worse for most customers.

The common mistake is calculating only the average user. With AI, a few heavy users can remove your profit. Always calculate at least two cases, and do not forget support and payment fees.

Let's recap. First, unit economics compares what one customer pays with what it costs to serve them. Second, gross margin is gross profit divided by revenue, and heavy AI usage can make a cheap plan lose money. Third, CAC and payback show how long a customer must stay before you earn back the cost of winning them.

Now it is your turn. In the exercise below this video, estimate the monthly cost and revenue per customer for your MVP in a free spreadsheet, for an average and a heavy user. Then ask Claude to check your formulas. Next, we look at choosing a business model. See you there.
```

## L10 Choosing a Business Model

- **Filename:** `ai-28-building-an-ai-startup_M2_L10_presenter.mp4`
- **Expected length:** about 4.9 minutes (682 words). The quality gate accepts ±10%.

```text
Two founders build the same product. One charges a monthly subscription. The other charges for each use. A year later, one business is healthy and the other is losing money. The only difference was how they asked customers to pay.

In the last lesson, you worked out what one customer costs. Now we decide how customers pay. A business model describes who pays you, for what, and how.

There are four common models for AI products. A subscription is a fixed price each month or year. It is predictable for you and the customer, but heavy users can cost more than they pay, as we saw last time. Pay per use charges for each action, such as each page translated. Your revenue rises with your costs, but income is harder to predict.

Pay per result charges only when an outcome happens, such as a recovered unpaid invoice. Customers like it, but you carry the risk. And freemium offers a free basic version, with payment for more. It can attract many users, but free users still create model costs.

You also choose who pays. B2B means business to business, selling to companies. Prices can be higher, but sales take longer. B2C means business to consumer, selling to individuals. Sales are faster, but people are often more sensitive to price.

Local habits matter too. In many emerging markets, fewer people use credit cards, and mobile money, meaning payments from a phone account, may be more common. Small, frequent payments can feel safer than a monthly commitment.

Think of a gym and a swimming pool. The gym sells monthly memberships and hopes most members come only sometimes. The pool sells single tickets, so it earns more when people swim more. Neither is wrong. Each works for a different kind of customer.

Let's compare. Awa is a made up founder in Dakar, Senegal. Her tool translates documents for small businesses between French, English and Wolof. All prices are placeholders. Each page costs her one cent in model usage. Each customer costs one dollar twenty a month in hosting and support. And the mobile money provider keeps two percent.

She compares a subscription of eight dollars a month for unlimited pages, with pay per use at five cents a page. For a typical customer with two hundred pages, the subscription costs her three dollars thirty six and earns four dollars sixty four. Pay per use earns six dollars sixty. Both work.

But look at the edges. A heavy customer with a thousand pages makes the subscription lose three dollars thirty six a month. A light customer with twenty pages makes pay per use lose forty two cents, because the fixed cost is bigger than the revenue.

So each model loses money on a different kind of customer. Awa's interviews showed that her customers prefer small mobile money payments, and their use changes a lot from month to month. So she chooses pay per use, with a minimum charge of two dollars a month. That covers the fixed cost for light users.

A common mistake is copying a famous software company's model, usually a low monthly subscription, without checking your own costs or how your customers like to pay. Test every model against light, typical and heavy customers, and against how your customers actually prefer to pay.

The model also affects defensibility, from lesson five. A product paid per result, or built deep into a company's daily process, is harder to replace than a cheap subscription anyone can cancel in one click.

Let's recap. First, common models are subscription, pay per use, pay per result and freemium, sold to businesses or consumers. Second, test each model against light, typical and heavy users, because each loses money on a different customer. Third, local payment habits, like mobile money, can decide which model works.

Now it is your turn. In the exercise below this video, compare two business models for your idea in a table, with price, cost to serve, margin and the main risk of each. Next week, we look at legal, ethical and data risks. See you there.
```
