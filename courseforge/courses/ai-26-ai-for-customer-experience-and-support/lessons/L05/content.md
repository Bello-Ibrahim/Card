# L05 Ticket Triage: Sorting and Routing with AI

Course: AI-26 · Module: M2 · Objectives: O2, O4 · Video: 5 min

## Hook
A customer writes "My card was used in another country and I did not make these payments." If this message waits in a general queue behind fifty password questions, the customer may lose more money. Sorting tickets well is not only about speed. Sometimes it is about safety.

## Explanation
**Ticket triage** means reading each new message, deciding what kind of message it is, and sending it to the right place. Many teams do this by hand. AI can do the first step for them by adding labels to each ticket.

Common labels are:

- **Topic:** billing, delivery, technical problem, account access, complaint, and so on.
- **Urgency:** for example high, normal or low.
- **Language:** so the ticket goes to an agent who reads that language.
- **Sentiment:** the customer's mood, such as calm, worried or angry.

After labelling, a routing rule sends the ticket somewhere: "Topic = card fraud → Fraud team, high priority."

How does AI choose a label? A language model reads the message and compares its meaning with the category names and descriptions you give it. It does not look for exact keywords only, so it can understand "the courier never came" as a delivery problem. But it is still making a prediction, and predictions can be wrong. As you saw in L02, the model can also be confident when it is wrong.

A wrong label has a real cost. A fraud report labelled "billing question" may wait for days. A calm-sounding message from a vulnerable customer may be labelled "low urgency". So two things matter:

1. **Clear categories.** Each category needs a short description and one or two examples. Categories should not overlap. If "Payments" and "Billing" both exist and nobody can explain the difference, the AI will not know either.
2. **Checking the results.** Before you trust AI labels, compare them with labels that experienced agents give to the same tickets. Keep checking a sample after launch. Some tickets, such as fraud or safety reports, should go to a person even when the AI is unsure.

A useful extra rule is an **"unsure" category**. Tell the AI: "If the message does not clearly fit one category, label it 'Needs review'." A person then sorts these by hand. This is better than a confident wrong label.

**Analogy:** AI triage is like a sorting desk at a large post office. Most letters have clear addresses and go quickly to the right van. Some are hard to read. A good sorter puts those in a separate box for a supervisor, rather than guessing and sending them to the wrong city.

## Worked Example
Katarzyna leads support at a hypothetical digital bank in Poland. Customers write in Polish, English and Ukrainian. Her team uses five categories: Card and fraud, Payments and transfers, Account access, Loans, and Other.

She writes a short description for each, for example: "Card and fraud: lost or stolen cards, payments the customer did not make, suspicious messages that ask for codes." She adds a rule: every Card and fraud ticket is high priority, and any ticket the AI is unsure about goes to "Needs review".

Before launch, she takes 60 old tickets with all personal details removed and asks two senior agents to label them. Then she asks the AI to label the same tickets. They agree on most tickets but not all. Katarzyna studies the differences. The AI labelled "Someone called me pretending to be from the bank" as Account access, not Card and fraud. She adds "phone calls from people pretending to be the bank" to the fraud description and tests again. The results improve. She also decides that a senior agent will check a small sample of AI labels every week.

## Common Mistake
Many teams test AI triage once, see good results and stop checking. But customer messages change: a new product, a new type of scam or a service outage brings new kinds of messages. The categories that worked last month may not fit this month. Keep checking a sample of labels regularly, and update your category descriptions when you find new patterns.

## Key Takeaways
1. AI triage labels tickets by topic, urgency, language and sentiment, so that routing rules can send them to the right team.
2. Clear, non-overlapping categories with short descriptions and a "Needs review" option reduce wrong labels.
3. Compare AI labels with human labels before launch and check a sample regularly after launch, especially for urgent or sensitive topics.

## Hands-on Exercise
**Task:** Define 5 ticket categories, then ask an AI assistant to classify 15 sample tickets. Compare its labels with your own and count the differences.
**Tools:** Claude or ChatGPT (free plan) [VERSION]; a spreadsheet (Google Sheets, Excel or LibreOffice Calc).
**Steps:**
1. Choose a made-up company, such as an internet provider or an online clothes shop.
2. Write 5 categories, each with a one-sentence description. Include "Needs review" as one of them, or add it as a sixth option.
3. Write 15 short, made-up customer messages. Include at least 2 that are unclear, 2 that are urgent and 1 in another language. Use no real names or account details.
4. In your sheet, create columns: Message, My label, AI label, Match (yes/no).
5. Label all 15 messages yourself first.
6. Paste your categories and descriptions into the AI assistant, then the 15 messages, and ask it to give one label per message.
7. Copy its labels into the sheet and mark each match.
8. Count the differences. For each one, write whether the problem was the AI, your category description, or a message that really fits two categories.
**What good looks like:** A sheet with 15 labelled messages, a count of differences, and a short note for each difference. You have improved at least one category description based on what you found.
**Time:** about 30 minutes

## Review Flags
- [VERSION] Free-plan access and data-use terms of Claude and ChatGPT must be checked before recording.
- Judgement call (from curriculum): exercises use made-up tickets; the worked example uses old tickets with all personal details removed.
