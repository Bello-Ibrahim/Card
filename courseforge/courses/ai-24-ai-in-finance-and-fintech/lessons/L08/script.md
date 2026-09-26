# L08 AI for Customer Service in Banking | Presenter Script

Course: AI-24 · Video: 5 min · Words: 684

## Hook
At two in the morning, a customer realises her card is missing. She wants it blocked now, and an AI assistant can do that in seconds. But what should the same assistant do when the next customer asks, should I move my savings into gold?

## Explain
Last time, we measured fairness in credit decisions. Now we move to the front line. AI assistants in banking handle high-volume, routine requests in chat apps, websites and phone menus.

Typical tasks fall into three groups. Information, such as balances, fees and opening hours. Simple actions, such as blocking a lost card or ordering a replacement. And guided processes, such as collecting the details for a disputed payment and opening a case.

Good banking assistants follow three design rules. Rule one: answer only from approved texts. A language model can produce a fluent answer that is wrong, such as an old fee or a rule from another country. Grounding it in the bank's approved policy texts, and telling it to say I don't know, reduces this risk.

Rule two: know the limits, and hand over to a human. Complaints, which often have formal handling rules. Vulnerable customers, such as someone in financial difficulty or under pressure from another person. Anything unclear or high-risk. And any request for personal investment advice. The assistant must not give it. It offers a licensed adviser instead.

Rule three: protect data. The assistant confirms identity before sharing account data, shows only what the customer is allowed to see, and never asks for full PINs or passwords. Even a PIN reset happens only through secure steps.

Think of a well-trained receptionist at a branch. She answers common questions from the official leaflet, handles simple forms, and knows exactly when to say, let me take you to a colleague. A good receptionist does not guess, and never gives financial advice.

## Demonstrate
Omar Haddad leads digital service at Al Waha Bank, a hypothetical bank in Dubai, in the United Arab Emirates. The bank serves customers in Arabic and English, and its assistant answers in the customer's language. Before launch, Omar tests it with five synthetic messages.

The first three go well. A lost card is blocked after an identity check. A balance question written in Arabic gets an answer in Arabic. And a question about investing in gold funds gets a clear reply: the assistant cannot give investment advice, but can connect a licensed adviser.

The last two fail. A customer writes that this is the third time, and nobody fixed her dispute. The assistant only repeats the dispute steps, but this is a complaint and must go to a human. Another says a man on the phone told him to move all his money today. The assistant gives transfer instructions. This is a possible scam and needs an urgent human handover.

So two of five answers are unsafe. Omar adds clear handover triggers for repeat contacts, complaint words and pressure to move money. And a bilingual reviewer, Layla Mansour, checks a sample of Arabic replies every week, because quality can differ between languages.

A common mistake is to judge an assistant only by how many chats it closes without a human. This rewards the assistant for keeping customers away from staff, even when they need a person. So measure correct handovers and customer outcomes too, not only automation rates.

## Recap
Let's recap. First, banking assistants work well for routine information, simple actions and guided processes, and they must answer only from approved policy texts. Second, complaints, vulnerable customers, possible scams and any request for personal investment advice go to a trained human. Third, test assistants with realistic messages in every language they serve, and measure correct handovers, not only automation.

## CTA
Now it is your turn. In the exercise below this video, you will give Claude or ChatGPT a synthetic policy text and draft replies to five customer messages. Check each reply against the policy, and mark which messages must go to a human. It takes about twenty-five minutes. In the next lesson, we look at AI for financial analysis and reporting. See you there.

## Thumbnail
Headline: Know When to Hand Over
Image: Navy background, a chat window with a friendly assistant icon passing a message to a smiling staff member icon, headline in teal Inter Bold.

## Production Notes
- [REGION] Complaint-handling rules and time limits differ by country and regulator. The script says only that complaints often have formal handling rules; keep that wording.
- [VERSION] Free-plan access and data-use terms of Claude and ChatGPT must be checked before recording.
- The Arabic balance question (ما هو رصيد حسابي؟) may appear on the test-table slide only. It must be checked by a native Arabic speaker before recording, and rendered in Noto Sans Arabic. The voiceover describes it in English.
- No investment advice: the gold question is shown only as a message that the assistant correctly refuses and routes to a licensed adviser.
- Omar Haddad, Layla Mansour and Al Waha Bank are fictional. Stock footage must not show a real bank brand or logo.
