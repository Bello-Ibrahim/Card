# L02 Safe Data Handling Before You Upload

Course: AI-08 · Module: M1 · Objectives: O1, O6 · Video: 5 min

## Hook
You want AI to analyse last month's customer list. The file has names, email addresses and phone numbers. Before you press "upload", ask yourself one question: would each of these customers be comfortable with this?

## Explanation
When you upload a file to an AI tool, a copy of the data leaves your computer and goes to the tool provider's servers. What happens next depends on the tool, your plan and its settings. Some services may keep uploads or use them to improve their models unless you change a setting. [VERSION] So the safest rule is simple: upload only what the analysis needs.

**Never upload these, unless your organisation has approved the tool for this data:**

- Names of customers, patients, students or staff.
- Contact details: email addresses, phone numbers, home addresses.
- ID numbers: national ID, passport, tax or account numbers.
- Salaries, health information and other sensitive personal details.
- Confidential business figures, such as unpublished financial results or contract prices.

Data protection rules differ by country, and employers often have their own rules on top. This lesson gives general safe-use principles; it is not legal advice. Always follow your organisation's policy and ask your data protection or IT contact if you are unsure. [REGION]

**How to anonymise a file.** Most analysis questions ("Which plan earns most?", "Which city is growing?") do not need to know who each person is. Before uploading:

1. **Keep the original untouched.** Make a copy (File > Make a copy) and work only on the copy. [VERSION] If you make a mistake, you can start again, and you can always go back to the true data.
2. **Remove columns you do not need,** such as email and phone.
3. **Replace identifiers with codes,** for example "Customer 01" instead of a name. If you need to link results back to real people later, keep the code list in a separate, protected file that you never upload.
4. **Make details less exact.** Change a date of birth into an age band (25–34) and a full address into a city or region.
5. **Check the result.** Scroll through every column and ask: could someone work out who this person is?

**Analogy:** Anonymising a file is like sending a letter about a medical case to a specialist without the patient's name and address on it. The specialist gets everything needed to give advice, but nothing that points to one person. The full record stays locked in the clinic's own cabinet.

## Worked Example
Nadia is a marketing coordinator for a gym chain in Casablanca, Morocco. She wants AI to compare spending across membership plans. Her fictional export looks like this:

| Customer ID | Name | Email | Phone | Date of birth | City | Plan | Monthly spend |
|---|---|---|---|---|---|---|---|
| 5501 | Youssef Amrani | y.amrani@example.com | +000 555 0101 | 1990-04-12 | Casablanca | Premium | 45 |
| 5502 | Grace Mensah | g.mensah@example.com | +000 555 0102 | 1985-11-30 | Rabat | Basic | 20 |
| 5503 | Lina Haddad | l.haddad@example.com | +000 555 0103 | 2001-07-05 | Casablanca | Student | 12 |
| 5504 | Pierre Laurent | p.laurent@example.com | +000 555 0104 | 1978-02-19 | Marrakesh | Premium | 45 |
| 5505 | Amal Idrissi | a.idrissi@example.com | +000 555 0105 | 1996-09-23 | Rabat | Basic | 20 |
| 5506 | Chen Wei | c.wei@example.com | +000 555 0106 | 1969-12-01 | Casablanca | Basic | 20 |

She makes a copy and changes it:

- **Name:** deleted.
- **Email and phone:** deleted.
- **Customer ID:** replaced with new codes C01 to C06, because the old ID could be matched with the gym's own system. The link between old and new codes stays in a separate file.
- **Date of birth:** replaced with an age band: C01 35–44, C02 35–44, C03 25–34, C04 45–54, C05 25–34, C06 55–64.

She keeps City, Plan and Monthly spend, because her question needs them. The safe copy has 5 columns and still answers her question.

## Common Mistake
Many people think that deleting the name column is enough. It is not. A customer ID, an exact date of birth, or a rare combination (the only 55–64 year old on a Basic plan in a small town) can still point to one person. Remove or blur every detail the analysis does not need, and check the rows as well as the column headers.

## Key Takeaways
1. Do not upload names, contact details, ID numbers, salaries or confidential figures unless your organisation has approved the tool for that data.
2. Always keep an untouched original, and anonymise a copy by removing columns, replacing identifiers with codes and making details less exact.
3. Rules differ by country and employer, so follow your organisation's policy and ask when you are unsure.

## Hands-on Exercise
**Task:** Create an anonymised copy of the customer dataset from the Worked Example and list what you changed.
**Tools:** Google Sheets (free).
**Steps:**
1. Copy the table into a Google Sheet and name the tab "Original".
2. Duplicate the tab and name the copy "Safe copy". Do all your work there.
3. Remove or replace at least 4 types of personal data: for example name, email, phone, Customer ID and date of birth.
4. Replace dates of birth with age bands and Customer IDs with new codes.
5. Scroll through each row and check that no one could be identified.
6. Write a short change log: column, what you did, and why.
**What good looks like:** The safe copy keeps City, Plan and Monthly spend. Name, Email and Phone are deleted, IDs are new codes, and dates of birth are age bands that match those in the Worked Example. Your log has one line per change, for example "Phone: deleted, not needed for spending analysis." The Original tab is unchanged.
**Time:** about 20 minutes

## Review Flags
- [REGION] Data protection rules differ by country and employer; the lesson gives general principles only and directs learners to their organisation's rules and contacts.
- [VERSION] How Claude and ChatGPT store uploaded files and whether uploads can be used for model training (and the related settings) must be checked against current provider policies before scripting.
- [VERSION] The Google Sheets menu path File > Make a copy must be checked against the current interface.
