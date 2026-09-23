# L08 AI for Customer Service in Banking

Course: AI-24 · Module: M2 · Objectives: O3 · Video: 5 min

## Hook
At two in the morning, a customer realises her card is missing. She does not want to wait on the phone. She wants it blocked now. An AI assistant can do that in seconds. But what should the same assistant do when the next customer asks, "Should I move my savings into gold?"

## Explanation
AI assistants in banking handle high-volume, routine requests in chat apps, websites and phone menus. Typical tasks are:

- **Information:** balance and recent transactions, opening hours, fees, how to update contact details.
- **Simple actions:** blocking a lost card, resetting a PIN through secure steps, ordering a replacement card.
- **Guided processes:** collecting the details for a disputed payment and opening a case.

Good banking assistants follow three design rules.

**1. Answer only from approved texts.** The assistant should use the bank's approved policy and product texts, not general knowledge from the internet. A language model can produce a fluent answer that is wrong, for example an old fee or a rule from another country. Grounding it in approved texts, and telling it to say "I don't know" when the answer is not there, reduces this risk.

**2. Know the limits and hand over to a human.** Some requests must always go to a trained person:
- **Complaints**, which often have formal handling rules and time limits [REGION].
- **Vulnerable customers**, for example someone in financial difficulty, bereaved, confused, or who mentions harm or pressure from another person.
- **Any request for personal investment advice**, such as "Should I buy these shares?" The assistant must not give investment advice. It explains that it cannot advise and offers a licensed adviser or a trained staff member.
- **Anything unclear or high-risk**, such as a large transfer the customer says they were told to make urgently.

**3. Protect data.** The assistant confirms identity before sharing account data, shows only what the customer is allowed to see, and never asks for full PINs or passwords.

**Analogy:** A banking assistant is like a well-trained receptionist at a branch. The receptionist answers common questions from the official leaflet, handles simple forms, and knows exactly when to say, "Let me take you to a colleague who can help with that." A good receptionist does not guess, and never gives financial advice.

## Worked Example
Omar Haddad leads digital service at Al Waha Bank, a hypothetical bank in Dubai, United Arab Emirates. The bank serves customers in Arabic and English, and its assistant answers in the language the customer uses. Omar tests it with synthetic messages before launch.

| Customer message | Assistant action | Correct? |
|---|---|---|
| "My card is lost, please block it." | Confirms identity, blocks the card, offers a replacement | Yes |
| "ما هو رصيد حسابي؟" ("What is my account balance?") | Confirms identity, shows the balance in Arabic | Yes |
| "Is it a good time to invest in gold funds?" | Explains it cannot give investment advice; offers to connect a licensed adviser | Yes |
| "This is the third time I am writing. Nobody fixed my dispute." | Answers with dispute steps only | **No:** this is a complaint and must go to a human |
| "A man on the phone says I must move all my money today." | Gives transfer instructions | **No:** possible scam and vulnerable customer; urgent human handover |

Two of five answers are unsafe. Omar adds clear handover triggers for repeat contacts, complaint words and pressure to move money, and he asks a bilingual reviewer, Layla Mansour, to check a sample of Arabic replies every week, because quality can differ between languages.

## Common Mistake
Many teams judge an assistant by how many chats it closes without a human. This rewards the assistant for keeping customers away from staff, even when they need a person. Measure correct handovers and customer outcomes too, not only automation rates.

## Key Takeaways
1. Banking assistants work well for routine information, simple actions and guided processes, and they must answer only from approved policy texts.
2. Complaints, vulnerable customers, possible scams and any request for personal investment advice go to a trained human.
3. Test assistants with realistic messages in every language they serve, and measure correct handovers, not only automation.

## Hands-on Exercise
**Task:** Draft replies to 5 customer messages from a synthetic policy text, check them, and mark which must go to a human.
**Tools:** Claude or ChatGPT (free plan) [VERSION]; the course's synthetic policy text and 5 synthetic customer messages.
**Steps:**
1. Open the synthetic policy text and the 5 messages. Never paste real customer messages or account details into a public AI tool.
2. Give the AI assistant the policy text and this instruction: "Answer only from this policy. If the answer is not in the policy, or the message is a complaint, shows vulnerability, or asks for investment advice, say it must go to a human."
3. Paste the 5 messages one at a time and copy each reply.
4. Check each reply against the policy: is every fact in the policy? Is anything invented?
5. Mark each message "AI reply OK", "AI reply needs correction" or "Must go to a human", with a reason.
**What good looks like:** Every reply is checked line by line against the policy; the investment question, the complaint and any sign of vulnerability are marked "Must go to a human"; and invented facts are corrected.
**Time:** about 25 minutes

## Review Flags
- [REGION] Complaint-handling rules and time limits differ by country and regulator; confirm local rules.
- [VERSION] Free-plan access and data-use terms of Claude and ChatGPT must be checked before recording.
- Arabic example sentence should be checked by a native Arabic speaker before recording.
