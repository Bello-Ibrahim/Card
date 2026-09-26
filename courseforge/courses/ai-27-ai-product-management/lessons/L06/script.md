# L06 Data Needs: What Your Feature Learns From | Presenter Script

Course: AI-27 · Video: 5 min · Words: 724

## Hook
Your team can choose the best model available and still ship a poor feature. If the data behind it is old, incomplete or collected without permission, the model will faithfully repeat those problems to your users.

## Explain
This is week two, and we start with data. Every AI feature depends on data in up to three ways, and as a PM, you own the questions about all three.

Training or tuning data is the examples a model learns from, if you train or adapt a model. Context data is information given to the model at the moment of use, such as a product catalogue or a user's order history. And evaluation data is examples with known good answers, used to test quality. Even with a ready made model, you still need context and evaluation data.

Check each source against six points. Source and owner: where does it come from, and who can approve its use? Labels: do the examples include the correct answer, and how consistent are they? Quality: is it accurate, complete and current? Old prices or deleted products create wrong answers.

Coverage: does it represent all your users, such as regions, languages and new customers? Gaps in coverage become quality gaps for those users. Consent and privacy: did users agree to this use, and is any personal data really necessary? Rules differ by country, so involve your privacy or legal team early. And access and cost: how long will it take to get?

A new product, or a new market, often has no usage data yet. This is the cold start problem. You can start with a rule based version and collect data from it. You can use a general model with good context data. You can label a small set of examples by hand. Or you can run a human in the loop version first, so human decisions become labels.

Think of a recipe. It is only as good as its ingredients. A skilled chef with old vegetables still serves a poor meal. And if the kitchen only stocks ingredients for one dish, guests who want something else go hungry. Quality is the freshness of your ingredients. Coverage is the range of dishes you can make.

## Demonstrate
Let's see an example. Mateo Fuentes is a PM at a hypothetical online grocery service in Chile. When an item is out of stock, pickers in the store choose a substitute. Mateo wants AI to suggest the best substitute, and the picker confirms it.

He fills in a data requirements table. The product catalogue has no personal data, but sizes are missing and categories are used inconsistently. So the team cleans the top five hundred products first. Past substitutions record whether customers accepted or refunded, but not why. They are linked to accounts, so identity is removed, and only the item pair and outcome are used.

Customer dietary preferences are sensitive personal data, and few customers fill them in. They need clear consent and a legal review. And a new store in the south has almost no substitution history at all.

The table leads to two decisions. First, the MVP will not use dietary preferences, because the privacy questions need more time, and the feature works without them. Second, the new store has a cold start problem. So it begins with simple catalogue rules, and picker confirmations build labelled data over time.

A common mistake is thinking lots of data means the right data. A large data set can still lack labels, miss whole user groups, or contain personal data you may not use. And never paste real customer data into an AI tool to check it quickly. Use invented or anonymised examples.

## Recap
Let's recap. First, an AI feature needs context and evaluation data even with a ready made model, and sometimes training data too. Second, check every source for owner, labels, quality, coverage, consent and access, because each gap becomes a product problem. Third, plan for cold start with rules, hand labelled examples, or a human in the loop version.

## CTA
Now it is your turn. In the exercise below, complete a data requirements table for your feature, with sources, owners, quality risks, privacy questions and how you would fill the gaps. It takes about twenty five minutes. In the next lesson, we ask a big question: build, buy or use an API? See you there.

## Thumbnail
Headline: Check Your Ingredients
Image: Navy background, a recipe card next to a basket of fresh vegetables, with a small data-table icon on the card, headline in teal Inter Bold.

## Production Notes
- [VERSION] Claude free-plan limits and data-use terms must be checked before recording (optional exercise tool).
- Data protection is described only as general principles; no country's law is named, as in content.md.
- Mateo Fuentes and the online grocery service in Chile are hypothetical; stock footage must not show a real supermarket brand or logo.
- Do not show real customer data on any slide; the data requirements table uses only the invented rows from content.md.
