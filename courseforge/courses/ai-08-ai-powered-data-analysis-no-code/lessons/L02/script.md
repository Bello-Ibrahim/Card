# L02 Safe Data Handling Before You Upload | Presenter Script

Course: AI-08 · Video: 5 min · Words: 724

## Hook
You want AI to analyse last month's customer list. The file has names, email addresses and phone numbers. Before you press upload, ask yourself one question. Would each of these customers be comfortable with this?

## Explain
In the last lesson, we saw what AI can do with a spreadsheet. Today, we make sure the file you upload is safe.

When you upload a file to an AI tool, a copy of the data leaves your computer and goes to the tool provider's servers. What happens next depends on the tool, your plan and its settings. So the safest rule is simple. Upload only what the analysis needs.

Never upload these, unless your organisation has approved the tool for this data. Names of customers, patients, students or staff. Contact details, like email addresses, phone numbers and home addresses. ID numbers, such as national ID, passport, tax or account numbers. Salaries, health information and other sensitive details. And confidential business figures, like unpublished results or contract prices.

Data protection rules differ by country, and employers often have their own rules on top. This lesson gives general principles, not legal advice. Always follow your organisation's policy, and ask your data protection or IT contact if you are unsure.

Most analysis questions do not need to know who each person is. So before uploading, anonymise the file in five steps. First, keep the original untouched. Make a copy, and work only on the copy. Second, remove columns you do not need, such as email and phone.

Third, replace identifiers with codes, for example customer zero one instead of a name. Keep the code list in a separate, protected file that you never upload. Fourth, make details less exact. Change a date of birth into an age band, and a full address into a city. Fifth, check the result. Could someone work out who this person is?

Think of a doctor who sends a letter about a case to a specialist, without the patient's name and address. The specialist gets everything needed to give advice, but nothing that points to one person. The full record stays locked in the clinic's own cabinet.

## Demonstrate
Let's see it in practice. Nadia is a marketing coordinator for a gym chain in Casablanca, Morocco. She wants AI to compare spending across membership plans.

Her fictional export has six customers and eight columns. Customer ID, name, email, phone, date of birth, city, plan and monthly spend. Only the last three are needed for her question.

She makes a copy and changes it. She deletes the name, email and phone columns. She replaces the customer IDs with new codes, C zero one to C zero six, because the old IDs could be matched with the gym's own system. The link between old and new codes stays in a separate file.

She replaces each date of birth with an age band. For example, the first customer, born in nineteen ninety, becomes thirty-five to forty-four. The customer born in two thousand and one becomes twenty-five to thirty-four.

She keeps city, plan and monthly spend, because her question needs them. The safe copy has five columns, and it still answers her question.

A common mistake is to think that deleting the name column is enough. It is not. A customer ID, an exact date of birth, or a rare combination can still point to one person. For example, the only person aged fifty-five to sixty-four on a basic plan in a small town. So check the rows as well as the column headers.

## Recap
Let's recap. First, do not upload names, contact details, ID numbers, salaries or confidential figures, unless your organisation has approved the tool for that data. Second, always keep an untouched original, and anonymise a copy by removing columns, replacing identifiers with codes, and making details less exact. Third, rules differ by country and employer, so follow your organisation's policy, and ask when you are unsure.

## CTA
Now it is your turn. In the exercise below this video, you will take Nadia's customer table and build a safe copy in Google Sheets. You will remove or replace at least four types of personal data, and write a short log of what you changed. It takes about twenty minutes. In the next lesson, we go from business question to data question. See you there.

## Thumbnail
Headline: Check Before You Upload
Image: Navy background, a spreadsheet with the name and email columns blurred out and a teal shield icon over the upload arrow, headline in teal Inter Bold.

## Production Notes
- [REGION] Data protection rules differ by country and employer. The script gives general principles only, says it is not legal advice, and points learners to their organisation's policy and contacts.
- [VERSION] How Claude and ChatGPT store uploaded files and whether uploads can be used for model training must be checked against current provider policies. The claim that some services may keep uploads or use them to improve models is left out of the narration for this reason.
- [VERSION] The Google Sheets menu path File > Make a copy is shown only as 'Make a copy' on the slide; check it in the current interface.
- Nadia, the Casablanca gym chain and all names, emails and phone numbers are fictional (example.com addresses, +000 numbers). Spoken age bands match content.md: C01 (born 1990) 35–44, C03 (born 2001) 25–34.
- Stock footage of the gym must show no real brand names or logos.
