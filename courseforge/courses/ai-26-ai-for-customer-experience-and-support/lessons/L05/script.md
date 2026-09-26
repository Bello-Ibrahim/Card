# L05 Ticket Triage: Sorting and Routing with AI | Presenter Script

Course: AI-26 · Video: 5 min · Words: 689

## Hook
A customer writes: my card was used in another country, and I did not make these payments. If that message waits behind fifty password questions, the customer may lose more money. Sorting tickets well is not only about speed. Sometimes it is about safety.

## Explain
Welcome to week two. This week we design AI-assisted workflows, and we start with ticket triage. Triage means reading each new message, deciding what kind it is, and sending it to the right place.

AI can do the first step by adding labels. The common ones are topic, such as billing or delivery. Urgency, such as high, normal or low. Language, so the right agent can read it. And sentiment, the customer's mood. Then a routing rule sends the ticket on. For example, card fraud goes to the fraud team with high priority.

How does AI choose a label? A language model compares the meaning of the message with the category names and descriptions you give it. It does not only look for keywords, so it understands that the courier never came is a delivery problem. But it is still a prediction, and predictions can be wrong, even when they sound confident.

A wrong label has a real cost. A fraud report labelled as a billing question may wait for days. A calm message from a vulnerable customer may be marked low urgency.

So two things matter. First, clear categories. Each one needs a short description and one or two examples, and categories must not overlap. If payments and billing both exist, and nobody can explain the difference, the AI will not know either. Second, checking the results. Compare AI labels with labels from experienced agents, and keep checking a sample after launch.

A useful extra rule is an unsure category. Tell the AI: if the message does not clearly fit one category, label it needs review. A person sorts these by hand. That is better than a confident wrong label.

Think of a sorting desk at a big post office. Most letters have clear addresses and go straight to the right van. A good sorter puts the hard-to-read ones in a box for a supervisor, instead of guessing.

## Demonstrate
Here is an example. Katarzyna leads support at a hypothetical digital bank in Poland. Customers write in Polish, English and Ukrainian. Her team uses five categories: card and fraud, payments and transfers, account access, loans, and other.

She writes a short description for each. Card and fraud means lost or stolen cards, payments the customer did not make, and suspicious messages that ask for codes. Every card and fraud ticket is high priority, and any ticket the AI is unsure about goes to needs review.

Before launch, she takes sixty old tickets, with all personal details removed. Two senior agents label them, and then the AI labels the same tickets. They agree on most, but not all.

Katarzyna studies the differences. The AI labelled, someone called me pretending to be from the bank, as account access, not fraud. So she adds phone calls from people pretending to be the bank to the fraud description. She tests again, and the results improve. A senior agent now checks a small sample every week.

A common mistake is to test once and stop checking. A new product, a new scam or an outage brings new kinds of messages. The categories that worked last month may not fit this month. Keep checking samples, and update your descriptions.

## Recap
Let's recap. First, AI triage labels tickets by topic, urgency, language and sentiment, so routing rules can send them to the right team. Second, clear categories with short descriptions and a needs review option reduce wrong labels. Third, compare AI labels with human labels before launch, and check a sample regularly after launch.

## CTA
Now it is your turn. In the exercise, you will define five categories, write fifteen made-up tickets, and label them yourself. Then an AI assistant labels them too, and you count the differences. In the next lesson, we map the workflow and decide what to automate, what to assist, and what stays human. See you there.

## Thumbnail
Headline: Sort Tickets, Protect Customers
Image: Navy background, a stream of ticket cards splitting into coloured lanes, one red card marked with a shield going into a fast lane, headline in teal Inter Bold.

## Production Notes
- [VERSION] Free-plan access and data-use terms of Claude and ChatGPT must be checked before recording.
- Katarzyna and the Polish digital bank are fictional; stock footage must show no real bank names, cards or logos.
- Pronunciation: Katarzyna (kah-tah-ZHIH-nah).
- The worked example uses old tickets with all personal details removed; the exercise uses made-up tickets only.
- The content says the AI and the senior agents 'agree on most tickets but not all'; no agreement percentage is given, and none should be added to slides.
