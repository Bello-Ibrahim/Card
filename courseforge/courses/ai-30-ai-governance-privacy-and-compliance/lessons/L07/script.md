# L07 Lawful Basis for AI Processing | Presenter Script

Course: AI-30 · Video: 5 min · Words: 680

## Hook
A retailer says, customers accepted our terms, so we can use their data to train our AI. Is that enough? Often it is not, because training a model and using it are different processing activities, and each one needs its own lawful basis.

## Explain
Last time, we followed the principles across the AI lifecycle. Now we focus on lawfulness. Remember, this course is educational and is not legal advice. The GDPR and the NDPA both list lawful bases. The lists are similar, but check the exact wording and conditions in each.

Under the GDPR, the lawful bases are consent, contract, legal obligation, vital interests, public task and legitimate interests. The NDPA contains a comparable list. For private-sector AI, three bases come up most often.

Consent must be freely given, specific, informed and unambiguous, and easy to withdraw. That makes it hard to use for training, because withdrawal may mean removing a person's data from a model. Contract covers only what is genuinely necessary to deliver a contract with the person. Training a general model usually is not.

Legitimate interests needs a three-part test. Is the purpose legitimate? Is the processing necessary for that purpose? And in a balancing test, are the organisation's interests overridden by the person's interests, rights and freedoms? Regulators have published guidance on using this basis for AI.

So split your AI processing into separate activities, such as collecting data, training the model and using the model on a person. Each activity needs a basis, and the answer may be different for each one.

Special category data, such as health data, biometric data used for identification, ethnic origin or religion, needs a lawful basis and an extra condition, such as explicit consent. And AI can infer special category data from ordinary data, which may bring it into scope.

Think of a lawful basis as a ticket for a specific train. A ticket from Warsaw to Kraków does not let you continue to Vienna. If you want to take the data further, to a new purpose, check whether your ticket covers that journey, or whether you need a new one.

## Demonstrate
Let's see this in practice. Magdalena Nowak is a privacy lawyer for a fictional online fashion retailer in Poznań, Poland. The retailer wants an AI system that recommends products based on browsing and purchase history.

Magdalena separates two activities: training the model on past purchases, and showing recommendations to a logged-in customer. For both, contract is weak, and consent is possible but hard to manage in a trained model. Legitimate interests looks possible, if the balancing test is met.

So she runs the test. The purpose, relevant product suggestions, is legitimate. For necessity, history in the retailer's own shop is needed, but data bought from third parties is not. For balancing, customers would reasonably expect some suggestions from a shop they use.

But risks rise if the model infers sensitive facts, such as pregnancy or health conditions. Her controls: exclude sensitive product categories from training, give a simple opt-out and explain it clearly in the privacy notice. She records her conclusion and marks it for review against regulator guidance.

A common mistake is to choose consent to be safe. Consent is not safer if people cannot really refuse, or if you cannot honour a withdrawal. And if consent is withdrawn, you usually cannot simply switch to another basis. Choose the most suitable basis at the start, and document why.

## Recap
Let's recap. First, every processing activity needs a lawful basis, and training a model may need a different basis from using it. Second, legitimate interests needs a documented three-part test: purpose, necessity and balancing, with controls that protect people. Third, special category data needs an extra condition, and AI may infer it.

## CTA
In the exercise below this video, you will take three fictional AI processing activities and choose the most suitable lawful basis for each, under the GDPR and under the NDPA. Justify each choice in two sentences.

In the next lesson, we turn to Nigeria: the NDPA's structure and key duties. See you there.

## Thumbnail
Headline: Is Consent Enough?
Image: Navy background, a train ticket icon split into two halves labelled train and use, headline in teal Inter Bold.

## Production Notes
- Legal/compliance reviewer sign-off required before release.
- Disclaimer spoken once in scene 2 (educational, not legal advice).
- [VERIFY] [REGION] Lawful bases: content.md placeholders [the GDPR article on lawful basis] and [the NDPA section on lawful basis]. The voiceover lists the GDPR bases in general terms and says only that the NDPA has a comparable list; any NDPA differences in the list must be checked.
- [VERIFY] [REGION] Special categories: content.md placeholder [the special categories article and section] (scene 7).
- [VERIFY] [REGION] Current EU and national regulator guidance on legitimate interests and AI model training must be checked (scenes 5 and 12). No regulator or guidance document is named in the voiceover.
- [VERIFY] Official sources for the exercise must be chosen, with date recorded.
- Magdalena Nowak and the Poznań fashion retailer are fictional. Stock footage must not show a real retailer's website or logo.
