# L01 The AI Map of Financial Services

Course: AI-24 · Module: M1 · Objectives: O1 · Video: 5 min

## Hook
A customer opens an account on her phone, pays a supplier, applies for a loan, asks a question at midnight and repays on time. At how many of those steps did an AI system look at her data? At a modern financial institution, the answer can be every one.

## Explanation
AI in finance is not one product. It is a set of tools that support different steps of the value chain. In this course we group them into five families.

1. **Onboarding and identity.** Checking identity documents, matching a selfie to an ID photo, and screening new customers against sanctions and watch lists. Data: ID images, application forms, screening lists.
2. **Payments and fraud detection.** Scoring each card payment, transfer or mobile-money transaction for fraud risk in real time. Data: transaction history, device and location details, and past fraud labels.
3. **Lending and credit scoring.** Estimating how likely an applicant is to repay, setting limits and spotting early signs of arrears. Data: credit bureau records, income, account behaviour and sometimes alternative data such as utility payments.
4. **Customer service.** Assistants that answer routine questions, block lost cards and guide disputes, and tools that sort complaints. Data: approved policy texts, chat and call transcripts, and account data the customer is allowed to see.
5. **Back-office analysis and compliance.** Summarising reports, drafting management commentary, reconciling accounts and flagging unusual activity for anti-money-laundering (AML) teams. Data: ledgers, reports, and case notes from investigators.

Two points apply across all five families. First, each use case is only as good as the data behind it. Second, each one produces an output that a person or a process must act on: approve, block, reply or report. The quality of that human step matters as much as the model.

**Analogy:** Think of AI as an extra pair of eyes at each step of a loan's journey. One pair checks the applicant's documents. Another looks at the risk of non-payment. Another watches the repayments for early warning signs. Another reads the customer's messages. None of these eyes makes the final decision alone. Each one helps the person responsible at that step to see more, faster.

Not every task needs AI. A fee calculation that follows a fixed table is better done with a simple formula. AI helps most when there are many cases, patterns change, and speed matters.

## Worked Example
Consider three hypothetical institutions.

**Mavuno Pay**, a mobile-money provider in Kenya, processes a large number of small transfers every day. Its main AI use case is fraud detection: a model scores each transfer and holds the riskiest ones for a quick check. It also uses a simple classifier to sort customer complaints sent by text message into "wrong transfer", "PIN problem" and "other". Its key data is transaction history and complaint text.

**Aurora Digital**, a digital bank in Brazil, uses AI in onboarding, where it matches selfies to ID documents, and in lending, where a model supports decisions on small personal loans. A human credit officer reviews every application that the model places near the decision boundary. Its key data is ID images, bureau records and account behaviour.

**Rheinfeld Insurance**, an insurer in Germany, uses AI in the back office. An assistant drafts summaries of long claim files for handlers, and a model flags claims with unusual patterns for the fraud team. Handlers make every final decision. Its key data is claim documents and past claim outcomes.

Juliana Costa, a product manager at Aurora Digital, maps all of this in a simple table: the step, the use case family, the data needed, and who acts on the output. The table quickly shows her a gap. The bank has no AI support in customer service, where queue times are longest.

## Common Mistake
Many people think "AI in finance" means one large model that runs the whole bank. In practice, institutions run many small, separate models, each with its own data, owner and risks. A fraud model and a chatbot have very different data needs and very different failure costs. When you assess a use case, always look at one specific task, not "AI" in general.

## Key Takeaways
1. AI use cases in finance fall into five families: onboarding and identity, payments and fraud, lending and credit, customer service, and back-office analysis and compliance.
2. Each use case depends on specific data, and its value depends on the quality of that data and the human step that acts on the output.
3. Assess AI one task at a time, and use a simple formula instead of AI when a task follows fixed rules.

## Hands-on Exercise
**Task:** Map 8 finance tasks from your own work to the five use case families and note the data each would need.
**Tools:** Google Sheets (free). Excel or any spreadsheet also works.
**Steps:**
1. Create a sheet with five columns: Task, Use case family, Data needed, Who acts on the output, Rules or AI?
2. List 8 tasks you or your team do, for example "check new supplier bank details" or "answer card-block requests".
3. Assign each task to one of the five families.
4. For each task, note the data it would need. Describe data types only; do not copy real customer data into the sheet.
5. In the last column, write "rules" if a fixed formula would do the job, or "AI" if patterns and variety make learning useful.
6. Highlight the one task where you think AI would add the most value, and write one sentence explaining why.
**What good looks like:** 8 real tasks, each placed in a family, with specific data types (for example "12 months of transaction history") rather than "customer data", and at least one task honestly marked "rules".
**Time:** about 20 minutes

## Review Flags
- None. All institutions and people are hypothetical, and the lesson states no statistics or country-specific rules.
