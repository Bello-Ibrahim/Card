# HeyGen Batch Pack: AI-24 M2 (Fairness, Service and Analysis)

Course: AI in Finance and Fintech. Make one HeyGen video per lesson below, using these settings for every video.

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

## L06 Fairness in Credit Decisions

- **Filename:** `ai-24-ai-in-finance-and-fintech_M2_L06_presenter.mp4`
- **Expected length:** about 5.1 minutes (714 words). The quality gate accepts ±10%.

```text
A credit model never sees an applicant's gender or ethnicity. Its designers removed those columns on purpose. Can it still treat one group of customers unfairly? Yes. And this lesson shows how.

Welcome to week two. Last time, we saw that credit models learn from past decisions. A credit decision affects whether a person can start a business, buy a home or handle an emergency. That is why fairness is a central question for any credit model.

Protected characteristics are personal traits that the law in many countries says must not be the basis for unfair treatment. Common examples include gender, ethnicity, religion, age, disability and marital status. The exact list differs by country, so always check it with your compliance team.

There are two forms of discrimination. Direct discrimination means treating someone less favourably because of a protected characteristic. It is usually easy to see. Indirect discrimination means a rule that looks neutral, but puts one protected group at a clear disadvantage without a good reason. In AI, this is the more common risk, and it is harder to see.

Indirect discrimination often comes through proxy variables. A proxy is a feature closely linked to a protected characteristic. Postcode can be linked to ethnicity or income. Phone type can be linked to income or age. And gaps in employment can be linked to caring responsibilities, and therefore to gender.

Removing the protected column does not remove the pattern. The model can rebuild it from proxies. So fairness must be checked by looking at outcomes by group, not only at the list of inputs.

A first, simple measure is the approval rate for each group, and the ratio between the lowest and the highest rate. A ratio of one means equal approval rates. A lower ratio means a larger gap. A gap is not automatic proof of discrimination. But it is a signal that must be investigated and explained.

Imagine a set of market scales that is slightly wrong for one type of container. Every time a customer uses that container, the weight is wrong. The error is small, but it happens every time, to the same customers. A biased model works the same way, on thousands of decisions.

Priya Raman is a credit risk analyst at Maple Ridge Credit, a hypothetical consumer lender. The model does not use gender. Priya tests its decisions on a synthetic sample, grouped by gender for testing only. Of four hundred men, two hundred and eighty were approved. That is seventy percent. Of three hundred women, one hundred and sixty-five were approved. That is fifty-five percent.

The ratio is fifty-five divided by seventy, which is about zero point seven nine. So Priya looks for explanations. One of the model's strongest features is months in continuous employment. In the sample, women more often have short career breaks for childcare. So employment gaps may be acting as a proxy for gender.

She also checks whether the groups differ in actual repayment, because that would be a legitimate reason for part of the gap. Her note to the credit committee does not say the model is sexist. It says there is a fifteen percentage point gap, one feature may act as a proxy, and the team should test the model without it and compare error rates by group.

A common mistake is to believe a model is fair if it does not use protected characteristics. This is called fairness through unawareness, and it does not work well, because proxies carry the same information.

Let's recap. First, direct discrimination uses a protected characteristic, while indirect discrimination uses a neutral-looking rule or feature that disadvantages a protected group. Second, proxy variables such as postcode, phone type or employment gaps can bring bias back into a model. Third, check fairness by measuring outcomes by group, such as approval rates and their ratio, then investigate the reasons behind any gap.

Now it is your turn. In the exercise below this video, you will open a synthetic set of loan decisions in Google Sheets, calculate the approval rate for each group, and the ratio between the lowest and highest rate. Then note what could explain the gap. It takes about twenty-five minutes. In the next lesson, we look at measuring and reducing bias. See you there.
```

## L07 Measuring and Reducing Bias

- **Filename:** `ai-24-ai-in-finance-and-fintech_M2_L07_presenter.mp4`
- **Expected length:** about 5.0 minutes (694 words). The quality gate accepts ±10%.

```text
Two analysts check the same credit model. One reports that it is unfair to Group B. The other reports that it protects Group B from bad loans. Both used correct numbers. How can that be?

In the last lesson, we measured the approval-rate ratio. But that only looks at decisions, not whether they were right. Error rates by group add that view. Today we measure them, and look at ways to reduce bias.

The false rejection rate asks: of the applicants who would have repaid, what share did the model decline? These are good customers wrongly turned away. The bad-loan approval rate asks: of the applicants who would not have repaid, what share did the model approve? These cause losses, and can leave borrowers with debt they cannot manage.

These measures can disagree. In general, you cannot make them all equal at once. So a team must choose which measure matters most for the decision, and explain why. Also, in real data we never see whether declined applicants would have repaid. In our synthetic data, we know the answer, which makes it good for learning.

You may hear of the four-fifths ratio, or zero point eight. It comes from US employment practice, not credit law. Treat it only as a rough rule of thumb that a gap needs investigating, never as a legal safe harbour for lending.

There are four main ways to reduce bias. Remove or change proxies. Rebalance the data, so the model learns from enough cases in each group. Add human review for applications near the threshold. And monitor the same fairness numbers every month, because they can change after launch.

Let's see this in Google Colab. Alejandro Ruiz is a risk analyst at Crédito Solar, a hypothetical consumer lender in Mexico. He uses the course's ready-made notebook, with one thousand three hundred synthetic loan decisions. No coding is needed. First, open the notebook link from the course page.

Next, save your own copy. Open the File menu and choose Save a copy in Drive. Now you can change it without affecting anyone else.

Here is what the code does. The first line lists how many applicants in each group repaid or not, and were approved or not. The rest builds a table and calculates three rates for each group, plus the approval-rate ratio. You do not need to change any of it yet.

Now open the Runtime menu and choose Run all. Wait a few seconds until the output table appears under the code. Check that your numbers match the table on the lesson page.

Group B's approval rate is fifty-six percent, against seventy-two point five percent for Group A. The ratio is zero point seven seven two. Group B's good payers are declined about twice as often: twenty-six point four percent, against thirteen point three. But the model approves far fewer bad loans for Group B: ten point seven percent, against thirty.

So both analysts were right. Alejandro reports the false rejection rate to his credit committee as the main measure, because it shows good customers being turned away. He recommends human review for Group B applications near the threshold.

Finally, try a change. In the counts line, change the number ninety-five to forty-five, and two hundred and sixty-five to three hundred and fifteen. Run all again. The ratio rises to zero point nine one, and Group B's false rejection rate falls to twelve point five percent.

Let's recap. First, approval-rate ratios compare decisions, while error rates by group show whether those decisions were right. Second, fairness measures can disagree, so choose and justify the main measure, and treat the four-fifths ratio only as a rule of thumb. Third, reduce bias by removing proxies, rebalancing data, adding human review and monitoring results, and test again after every change.

Now it is your turn. In the exercise below this video, you will run the same notebook, compare false rejection rates by group, and write three sentences on which fairness measure you would report to a credit committee, and why. It takes about thirty minutes. In the next lesson, we look at AI for customer service in banking. See you there.
```

## L08 AI for Customer Service in Banking

- **Filename:** `ai-24-ai-in-finance-and-fintech_M2_L08_presenter.mp4`
- **Expected length:** about 4.9 minutes (680 words). The quality gate accepts ±10%.

```text
At two in the morning, a customer realises her card is missing. She wants it blocked now, and an AI assistant can do that in seconds. But what should the same assistant do when the next customer asks, should I move my savings into gold?

Last time, we measured fairness in credit decisions. Now we move to the front line. AI assistants in banking handle high-volume, routine requests in chat apps, websites and phone menus.

Typical tasks fall into three groups. Information, such as balances, fees and opening hours. Simple actions, such as blocking a lost card or ordering a replacement. And guided processes, such as collecting the details for a disputed payment and opening a case.

Good banking assistants follow three design rules. Rule one: answer only from approved texts. A language model can produce a fluent answer that is wrong, such as an old fee or a rule from another country. Grounding it in the bank's approved policy texts, and telling it to say I don't know, reduces this risk.

Rule two: know the limits, and hand over to a human. Complaints, which often have formal handling rules. Vulnerable customers, such as someone in financial difficulty or under pressure from another person. Anything unclear or high-risk. And any request for personal investment advice. The assistant must not give it. It offers a licensed adviser instead.

Rule three: protect data. The assistant confirms identity before sharing account data, shows only what the customer is allowed to see, and never asks for full PINs or passwords. Even a PIN reset happens only through secure steps.

Think of a well-trained receptionist at a branch. She answers common questions from the official leaflet, handles simple forms, and knows exactly when to say, let me take you to a colleague. A good receptionist does not guess, and never gives financial advice.

Omar Haddad leads digital service at Al Waha Bank, a hypothetical bank in Dubai, in the United Arab Emirates. The bank serves customers in Arabic and English, and its assistant answers in the customer's language. Before launch, Omar tests it with five synthetic messages.

The first three go well. A lost card is blocked after an identity check. A balance question written in Arabic gets an answer in Arabic. And a question about investing in gold funds gets a clear reply: the assistant cannot give investment advice, but can connect a licensed adviser.

The last two fail. A customer writes that this is the third time, and nobody fixed her dispute. The assistant only repeats the dispute steps, but this is a complaint and must go to a human. Another says a man on the phone told him to move all his money today. The assistant gives transfer instructions. This is a possible scam and needs an urgent human handover.

So two of five answers are unsafe. Omar adds clear handover triggers for repeat contacts, complaint words and pressure to move money. And a bilingual reviewer, Layla Mansour, checks a sample of Arabic replies every week, because quality can differ between languages.

A common mistake is to judge an assistant only by how many chats it closes without a human. This rewards the assistant for keeping customers away from staff, even when they need a person. So measure correct handovers and customer outcomes too, not only automation rates.

Let's recap. First, banking assistants work well for routine information, simple actions and guided processes, and they must answer only from approved policy texts. Second, complaints, vulnerable customers, possible scams and any request for personal investment advice go to a trained human. Third, test assistants with realistic messages in every language they serve, and measure correct handovers, not only automation.

Now it is your turn. In the exercise below this video, you will give Claude or ChatGPT a synthetic policy text and draft replies to five customer messages. Check each reply against the policy, and mark which messages must go to a human. It takes about twenty-five minutes. In the next lesson, we look at AI for financial analysis and reporting. See you there.
```

## L09 AI for Financial Analysis and Reporting

- **Filename:** `ai-24-ai-in-finance-and-fintech_M2_L09_presenter.mp4`
- **Expected length:** about 4.9 minutes (673 words). The quality gate accepts ±10%.

```text
It is the last day of the quarter-end close. You have a profit-and-loss sheet, a budget, and two hours to write the management commentary. An AI assistant can write a first draft in thirty seconds. Can you trust the numbers in it?

Last time, we tested an assistant that talks to customers. Today we look inside the finance team. AI assistants are useful for tasks built around text and structure.

They can summarise long documents, such as board packs or audit reports. They can explain variances between actual results and budget in clear sentences. They can draft commentary for management reports in a set format. And they can check whether the commentary and the tables tell the same story.

But language models are built to produce fluent text, not to calculate. They can invent numbers that are not in the source. They can misread numbers, for example reading thousands as millions. They can calculate percentages wrongly. And they can give a convincing but wrong reason for a variance.

So the rule in this course is simple. Every figure in AI-drafted commentary is checked against the source before it leaves the team.

Where possible, calculate the variances yourself in the spreadsheet first, and give the AI the calculated table. Then its only job is to write the words, which is what it does best. Also, never paste confidential results or customer data into a public AI tool. And keep commentary factual. It must not turn into investment advice or a forecast presented as fact.

Think of an AI assistant as a fast, eager junior analyst. The junior can produce a well-written draft in minutes, and the draft is often useful. But no experienced manager sends a junior's work to the board without checking every number.

Arjun Mehta is a finance analyst at Kaveri Home Appliances, a synthetic company in India. He gives an AI assistant the quarterly profit-and-loss summary, in thousands of rupees, and asks for variance commentary against budget. Revenue was budgeted at twelve thousand, and came in at eleven thousand four hundred.

The AI's draft says revenue fell six percent below budget, gross margin improved thanks to lower costs, and operating profit was six hundred and eighteen below budget, mainly because of higher operating expenses.

Arjun checks each figure. Revenue fell six percent is wrong. Six hundred on twelve thousand is five percent. Gross margin improved is also wrong. It was forty percent in the budget and thirty-eight percent in the actual results, because costs fell less than revenue.

Six hundred and eighteen below budget is correct, but the reason is wrong. Lower gross profit explains four hundred and sixty-eight of it. Higher operating expenses explain only one hundred and fifty.

So Arjun rewrites the commentary. Revenue was five percent below budget. Gross margin fell from forty percent to thirty-eight percent, so gross profit was four hundred and sixty-eight below budget. Operating expenses were one hundred and fifty above budget. Together, operating profit was six hundred and eighteen, or thirty-four point three percent, below budget.

A common mistake is to check only the numbers you expect to be wrong, or only the first paragraph. Errors often hide in the reasons and comparisons, not only in the raw figures. Check every number, and every because.

Let's recap. First, AI assistants are good at summarising, explaining variances and drafting commentary in a set format. Second, language models can invent, misread or miscalculate numbers, and give convincing but wrong reasons, so every figure and every reason must be checked against the source. Third, calculate variances in the spreadsheet first, use only synthetic or approved data, and keep commentary factual, with no investment advice.

Now it is your turn. In the exercise below this video, you will give a free AI assistant the synthetic quarterly profit-and-loss sheet and ask for variance commentary. Then check every number against the sheet, and correct any errors. It takes about thirty minutes. In the next lesson, we look at explainability, and the question, why was I declined? See you there.
```

## L10 Explainability: Why Was I Declined?

- **Filename:** `ai-24-ai-in-finance-and-fintech_M2_L10_presenter.mp4`
- **Expected length:** about 4.9 minutes (681 words). The quality gate accepts ±10%.

```text
Your application was unsuccessful. This decision was based on a number of factors. Imagine receiving that message after applying for a loan for your family business. What would you do next? You would not know. And that is the problem this lesson solves.

In lessons six and seven, we measured whether decisions are fair. Now we ask whether they can be explained. Three groups need to understand a credit decision. Customers need to know why they were declined, and what they could change. Staff need to explain and check decisions. And supervisors and auditors need evidence that the model works as intended.

In many countries, lenders must give applicants the main reasons for a decline, and some laws give people rights around automated decisions. The rules differ from place to place, so always check the rules where you work. Lesson eleven looks at examples.

Lenders use two main tools. Reason codes are short, standard statements linked to the factors that lowered a score the most. For example, high level of existing debt compared with income. In a scorecard, they come directly from the points. In a machine learning model, they come from an explanation method.

The second tool is feature importance. Global importance shows which features matter most across all decisions. Local importance shows which features pushed one applicant's score up or down. That is what a decline reason needs. These methods give estimates, not perfect truth, so they must be tested too.

There is a big difference between an accurate explanation and a comforting one. We had a very high number of applications this month may feel kind. But if it is not the real reason, it is misleading, and it stops the customer fixing the real problem. A good reason is true, specific, understandable, actionable where possible, and respectful. And it never names a protected characteristic or a proxy.

It is like a doctor explaining a test result. Your results were not ideal is kind but useless. Your blood pressure is high, and reducing salt could help, is true, specific and useful.

Youssef Hassan applies for a personal loan at Nile Gate Finance, a hypothetical lender in Cairo, Egypt. The model declines him. The top three factors are his debt payments, at fifty-two percent of his income, two missed payments in the last twelve months, and a credit card balance at ninety-five percent of its limit.

The system's first draft reads: declined, debt-to-income above threshold, two delinquencies in twelve months, utilisation high. It is accurate, but full of jargon and abbreviations. A customer would not understand it, and could not act on it.

The credit officer, Nour El-Sayed, rewrites it. We could not approve your application at this time. The main reasons were: your monthly debt payments are high compared with your income. Two payments were missed in the last twelve months. And your credit card balance is close to its limit. Reducing your debt and paying on time can improve future applications.

She checks that each reason matches the data and the order of importance, and that the letter makes no promise of future approval. A common mistake is to let an explanation tool or an AI assistant write reasons with no check. The result may be fluent but wrong, for example naming a factor that did not lower the score. Every reason must be traced back to that applicant's data.

Let's recap. First, customers, staff and supervisors all need explanations, and many countries require decline reasons. Second, reason codes and local feature importance show which factors lowered one applicant's score, and they must be tested and checked. Third, a good decline reason is true, specific, understandable, actionable and respectful. A comforting but inaccurate reason is misleading.

Now it is your turn. In the exercise below this video, you will write customer-friendly decline reasons for three synthetic applicants. Ask an AI assistant to check them for jargon, without adding new reasons. Then confirm that each reason matches the data. It takes about twenty-five minutes. Next week, we start with regulatory principles for AI in finance. See you there.
```
