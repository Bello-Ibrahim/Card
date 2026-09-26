# HeyGen Batch Pack: AI-08 M1 (Preparing Data with AI)

Course: AI-Powered Data Analysis (No Code). Make one HeyGen video per lesson below, using these settings for every video.

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

## L01 What AI Can Do with Your Spreadsheets

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_M1_L01_presenter.mp4`
- **Expected length:** about 5.3 minutes (736 words). The quality gate accepts ±10%.

```text
You upload a spreadsheet and type, which product sold best? Ten seconds later, you get a neat answer with a chart. It feels like magic. But how does the AI get that number? And how do you know it is right?

Hi, and welcome to AI-Powered Data Analysis, No Code. In this first lesson, we look at what AI can do with your spreadsheets, and where it goes wrong.

Some AI assistants, such as Claude and ChatGPT, can analyse files that you upload. When you upload a spreadsheet, a typical tool does three things. First, it reads the data. It looks at the column names and the first rows to understand what each column contains.

Second, it calculates. Many tools write and run a small hidden program to sort, filter, add up or count the data. Third, it describes the result in words, and sometimes in a chart.

This makes AI useful for three kinds of work. Fast summaries, like totals, averages and counts by group, in seconds. Formula ideas, when you describe what you need in plain words. And chart suggestions that fit your question.

But it also fails in predictable ways. It can use the wrong column, for example adding up units when you asked about revenue. It can round too early, or skip rows with blank cells without telling you. And it can state a cause or a trend that the data does not support, in a very sure tone.

Anything you upload leaves your computer. So never upload personal or confidential data unless your organisation has approved the tool for that data. You will learn how to prepare a safe file in the next lesson.

Think of it this way. Imagine a very fast junior analyst in their first week. They produce a summary in minutes, and it is often good. But they do not yet know your business, they sometimes pick the wrong column, and they never say, I am not sure.

You would always review their work before you send it to your manager. Treat AI answers in the same way.

Hiroshi runs a small shop in Osaka that sells handmade soap and candles, online and at a weekend market. He uploads a fictional sales sheet to an AI assistant.

The sheet has eight rows. Two months, January and February. Two products, soap bars and candles. Two channels, online and market. And for each row, the units sold and the revenue.

He asks, what was total revenue by channel? The AI answers. Online, one thousand four hundred and ninety. Market, eight hundred and ninety. So online brought in about sixty-three percent of revenue.

Hiroshi checks one number in Google Sheets. He uses a formula that adds up the revenue column, but only for rows where the channel is online. The result is one thousand four hundred and ninety. The answer matches.

Then he asks, which product is more popular? The AI says soap bars are much more popular, with four hundred and twenty units against one hundred and forty candles. That is true for units.

But look at revenue. Soap bars brought in one thousand two hundred and sixty, and candles one thousand one hundred and twenty. The two products are close. Popular was a vague word, and the AI chose units without saying so. Hiroshi learns to name the column he means.

A common mistake is to think that because the AI runs code, its numbers must be correct. But the AI may have understood a different question. So always check at least one number by hand, and always ask which columns the AI used.

Let's recap. First, AI file-analysis tools read your data, run hidden calculations, and describe the results in words and charts. Second, they are fast at summaries, formula ideas and chart suggestions, but they can use the wrong column, skip rows, and sound sure when they are wrong.

Third, treat the AI like a fast junior analyst. Check at least one number by hand, and never upload personal or confidential data to a tool your organisation has not approved.

Now it is your turn. In the exercise below this video, you will upload the same sample sales sheet to Claude or ChatGPT, ask three questions, and check one answer by hand in Google Sheets. It takes about twenty minutes. In the next lesson, we look at safe data handling before you upload. See you there.
```

## L02 Safe Data Handling Before You Upload

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_M1_L02_presenter.mp4`
- **Expected length:** about 5.2 minutes (718 words). The quality gate accepts ±10%.

```text
You want AI to analyse last month's customer list. The file has names, email addresses and phone numbers. Before you press upload, ask yourself one question. Would each of these customers be comfortable with this?

In the last lesson, we saw what AI can do with a spreadsheet. Today, we make sure the file you upload is safe.

When you upload a file to an AI tool, a copy of the data leaves your computer and goes to the tool provider's servers. What happens next depends on the tool, your plan and its settings. So the safest rule is simple. Upload only what the analysis needs.

Never upload these, unless your organisation has approved the tool for this data. Names of customers, patients, students or staff. Contact details, like email addresses, phone numbers and home addresses. ID numbers, such as national ID, passport, tax or account numbers. Salaries, health information and other sensitive details. And confidential business figures, like unpublished results or contract prices.

Data protection rules differ by country, and employers often have their own rules on top. This lesson gives general principles, not legal advice. Always follow your organisation's policy, and ask your data protection or IT contact if you are unsure.

Most analysis questions do not need to know who each person is. So before uploading, anonymise the file in five steps. First, keep the original untouched. Make a copy, and work only on the copy. Second, remove columns you do not need, such as email and phone.

Third, replace identifiers with codes, for example customer zero one instead of a name. Keep the code list in a separate, protected file that you never upload. Fourth, make details less exact. Change a date of birth into an age band, and a full address into a city. Fifth, check the result. Could someone work out who this person is?

Think of a doctor who sends a letter about a case to a specialist, without the patient's name and address. The specialist gets everything needed to give advice, but nothing that points to one person. The full record stays locked in the clinic's own cabinet.

Let's see it in practice. Nadia is a marketing coordinator for a gym chain in Casablanca, Morocco. She wants AI to compare spending across membership plans.

Her fictional export has six customers and eight columns. Customer ID, name, email, phone, date of birth, city, plan and monthly spend. Only the last three are needed for her question.

She makes a copy and changes it. She deletes the name, email and phone columns. She replaces the customer IDs with new codes, C zero one to C zero six, because the old IDs could be matched with the gym's own system. The link between old and new codes stays in a separate file.

She replaces each date of birth with an age band. For example, the first customer, born in nineteen ninety, becomes thirty-five to forty-four. The customer born in two thousand and one becomes twenty-five to thirty-four.

She keeps city, plan and monthly spend, because her question needs them. The safe copy has five columns, and it still answers her question.

A common mistake is to think that deleting the name column is enough. It is not. A customer ID, an exact date of birth, or a rare combination can still point to one person. For example, the only person aged fifty-five to sixty-four on a basic plan in a small town. So check the rows as well as the column headers.

Let's recap. First, do not upload names, contact details, ID numbers, salaries or confidential figures, unless your organisation has approved the tool for that data. Second, always keep an untouched original, and anonymise a copy by removing columns, replacing identifiers with codes, and making details less exact. Third, rules differ by country and employer, so follow your organisation's policy, and ask when you are unsure.

Now it is your turn. In the exercise below this video, you will take Nadia's customer table and build a safe copy in Google Sheets. You will remove or replace at least four types of personal data, and write a short log of what you changed. It takes about twenty minutes. In the next lesson, we go from business question to data question. See you there.
```

## L03 From Business Question to Data Question

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_M1_L03_presenter.mp4`
- **Expected length:** about 4.9 minutes (682 words). The quality gate accepts ±10%.

```text
How is the shop doing? Every owner asks this question. But if you type it into an AI tool with your sales sheet, you get a long, general answer that does not help you decide anything. The problem is not the AI. The problem is the question.

In the last lesson, we made our files safe to upload. Now we make our questions clear, because good analysis starts with a clear question.

A business question is what you or your manager want to know, in everyday words. Are we losing money? Is the new menu working? A data question is one that your spreadsheet can answer with a number.

To turn a business question into data questions, make each one measurable with four parts. What to measure. Revenue, units, profit, or number of customers? Which group. All products, or one product? All shops, or one region? Which time period. Last month, this quarter, or January to April?

And the fourth part, compared with what? This is the one people forget most often. Revenue was five thousand in March means little on its own. Revenue was five thousand in March, against six thousand in February, tells you something.

Next, check that your data can answer each question. Name the columns you need. If a column does not exist, you need more data or a different question. This step saves time. You find missing data before you start the analysis, not after. And write your data questions before you open any AI tool.

Here is a way to picture it. A business question is like telling a taxi driver, take me somewhere nice. A data question is like giving the exact address. Both start the journey, but only one gets you to a place you can check you have reached.

Let's meet Kwame. He runs a bakery in Accra, Ghana, and he is worried. My profits are falling, he says. His fictional sales sheet has five columns. Month, product, units sold, revenue, and ingredient cost, both in Ghanaian cedis.

Profits are falling is a feeling, not yet a question. So Kwame breaks it into three data questions. First, is profit really falling, and since when? He looks at profit per month, which is revenue minus ingredient cost, from January to June, month by month. He needs the month, revenue and ingredient cost columns.

Second, is it all products, or only some? He compares each product's profit in January with its profit in June. This adds the product column.

Third, is it fewer sales, or higher costs? He compares units sold per month with ingredient cost per unit. That is ingredient cost divided by units sold.

The answers are clear. Total units are stable. But the ingredient cost per loaf of one bread type has risen since April. The worry, profits are falling, is now a specific finding he can act on. He can review the price or the recipe of one product.

Notice what Kwame did not ask. Why are customers unhappy? His sheet has no column about customer opinions, so that question needs different data.

A common mistake is to write data questions that are still vague, like look at sales trends. Ask yourself, could two people answer this question and get the same number? If not, it is not yet measurable. Add the measure, the group, the time period and the comparison.

Let's recap. First, a business question is what you want to know in everyday words. A data question can be answered with a number from your data. Second, make each data question measurable. What to measure, which group, which time period, and compared with what. Third, name the columns each question needs, so you discover missing data before you start.

Now it is your turn. In the exercise below this video, you will write one business question from your own work, or use the sample café dataset, and break it into three measurable data questions, with the columns each one needs. It takes about twenty minutes. In the next lesson, we clean messy data with AI help. See you there.
```

## L04 Cleaning Messy Data with AI Help

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_M1_L04_presenter.mp4`
- **Expected length:** about 5.3 minutes (732 words). The quality gate accepts ±10%.

```text
You ask AI for sales by region, and it reports six regions. Your company has three. The maths was right, but the data was messy. And messy data gives wrong answers, however clever the tool.

Last time, we turned vague worries into clear data questions. Before we answer them, we need clean data.

Five problems appear again and again. Duplicates, where the same order is entered twice, so totals are too high. Blank cells, which some tools skip and others treat as zero. And inconsistent spellings. South, lower-case south, S T H, and South with a space at the end are four different values to a computer.

Then there are mixed date formats. Zero eight, zero one, twenty twenty-six can mean the eighth of January or the first of August, depending on the country. And numbers stored as text. They look like numbers, but they are not added up in totals.

AI can help, but there is a right way and a wrong way. The wrong way is to upload the file, say clean this, and download whatever comes back. You cannot see what was changed, deleted or guessed. The right way is to describe the problem, and ask for step-by-step fixes that you make yourself in Google Sheets.

Google Sheets has useful tools for this. TRIM removes extra spaces. PROPER fixes capital letters. VALUE turns a number stored as text into a real number. There are also menu tools to remove duplicates, and find and replace to change one spelling into another.

And keep a cleaning log. One line for each change, saying what you changed, how, and why.

Cleaning data is like washing and sorting vegetables before you cook. If you skip it, the meal may look fine, but there is sand in the salad. And you wash them yourself, so you know what was thrown away.

Mateus is the office manager of a fictional online office-supplies shop in Porto Alegre, Brazil. He exports his orders sheet. It has eleven rows, and revenue is in US dollars.

Look closely, and the problems appear. Order ten oh six is there twice. One revenue cell is empty. Regions are spelled in different ways. Dates come in three formats. And some numbers have an apostrophe or a dollar sign, so they are stored as text.

He asks an AI assistant to list the problems and suggest fixes, and makes each change himself. First, he removes the duplicate row. Second, the blank revenue for order ten oh four. He checks that three units times one hundred and twenty gives three hundred and sixty, and enters it.

Third, spellings. He fixes the regions with TRIM, then find and replace, so south and S T H become South. He tidies the product names in the same way.

Fourth, dates. The AI warns that zero eight, zero one is ambiguous. The order IDs are in date order, and order ten oh two is the fifteenth of January. So order ten oh one must be the eighth of January. He changes every date to one format, year, month, day.

Fifth, text numbers. He converts them into real numbers with VALUE, or by retyping them.

Before cleaning, the sum of the revenue column gave only one thousand four hundred and seventy. The blank and the one thousand eight hundred stored as text were left out, and the duplicate was counted twice. The clean sheet has ten orders, and total revenue of three thousand four hundred and fifty.

A common mistake is to let the AI clean the file, and never check what changed. It may delete real repeat orders as duplicates, or fill blanks with guesses. Ask for steps, make each change yourself, and log it.

Let's recap. First, the five common problems are duplicates, blank cells, inconsistent spellings, mixed date formats, and numbers stored as text. Second, describe the problem to AI, and ask for step-by-step fixes that you apply yourself, instead of letting it change the data invisibly. Third, keep a cleaning log with every change, how you made it, and why.

Now it is your turn. In the exercise below this video, you will clean Mateus's messy orders sheet in Google Sheets with AI suggestions. Fix at least five types of problem, and log each change. It takes about thirty minutes. In the next lesson, we look at AI-written formulas in Google Sheets. See you there.
```

## L05 AI-Written Formulas in Google Sheets

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_M1_L05_presenter.mp4`
- **Expected length:** about 5.3 minutes (732 words). The quality gate accepts ±10%.
- **Pronunciation:** [VERSION] [REGION] [VERIFY] Argument separators and function names depend on locale settings. The narration only says that some locale settings use semicolons; it does not name which locales, and it does not say whether function names are translated. Confirm for the fr, pt and ar versions, and re-record the formula close-ups with semicolons where needed.

```text
You want total revenue for the South region, but you do not remember the formula. AI can write it in seconds. But a formula that looks right can still give the wrong number.

Last time, we cleaned Mateus's orders sheet. Now we ask AI to write formulas for it, and we test every one.

Describe what you need in plain words, and an AI assistant can write the formula. A good request has four parts. Where the data is. What each column contains. What you want. And which tool, because formulas differ between spreadsheet tools.

Four functions are useful here. SUMIFS adds numbers that meet conditions. XLOOKUP finds a value in one column and returns the matching value from another. IF gives one result when a condition is true, and another when it is false. And date functions, such as TEXT and MONTH, take out parts of a date.

Always test a new formula on a few rows you can check by hand. If the formula and your hand check agree on three rows, you can trust it much more. And if you do not understand a formula, ask the AI to explain it.

One more thing. In some locale settings, Google Sheets uses semicolons instead of commas between the parts of a formula. If an AI formula shows a parse error, check the separators.

Think of an AI-written formula as a recipe from a friend who has never seen your kitchen. It is usually close, but you still taste the dish before you serve it.

Let's watch. Aigerim is a finance assistant in Almaty, Kazakhstan. She uses the clean, fictional orders sheet from the last lesson, with ten orders and revenue in US dollars.

First, a total by region. She asks the AI for total revenue where region is South. It returns a SUMIFS formula. She types it into cell J2, and the result is zero.

Zero cannot be right. She checks by hand. The South orders are two hundred and forty, one hundred and eighty, and one thousand eight hundred. That makes two thousand two hundred and twenty. The AI swapped the ranges. In SUMIFS, the range to add comes first.

She puts the revenue range first. Now the result is two thousand two hundred and twenty. She checks North the same way, which gives six hundred and eighty, and West, which gives five hundred and fifty.

Second, a lookup. She asks for the revenue of a given order ID. The AI gives an XLOOKUP formula. For order ten oh eight, it returns one thousand eight hundred. She tests order ten oh two, which gives two hundred and forty, and order ten ten, which gives one hundred and twenty. An ID that does not exist returns not found, as expected.

Third, a month column for grouping. The AI first suggests the MONTH function, which returns just the number one. So she asks, will this mix January twenty twenty-six with January twenty twenty-seven? It will. The AI suggests a better version with TEXT, which shows the year and the month.

She types the header Month in H1, puts the formula in H2, and fills it down. She checks three rows. H2 shows twenty twenty-six, zero one. H6 shows twenty twenty-six, zero two. And H10 shows twenty twenty-six, zero three.

Finally, she asks the AI to explain the SUMIFS formula step by step, and points to each range as she reads.

A common mistake is to accept a formula because it returns a number without an error. A wrong formula often returns a real-looking number, or zero, with no warning. Only a hand check shows it is correct.

Let's recap. First, describe the data, the columns, what you want and the tool, and AI can write a useful formula. Second, test every AI formula on at least three rows by hand, and correct it if the results differ. Third, ask the AI to explain any formula you do not understand, and watch the separators for your locale.

Now it is your turn. In the exercise below this video, you will ask Claude or ChatGPT for three formulas: a total by region, a lookup, and a date calculation. Test each one on three rows by hand, and correct any that are wrong. It takes about thirty minutes. Next time, we start week two with asking good questions of your data. See you there.
```
