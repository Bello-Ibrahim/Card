# L06 Structured Output: Getting JSON You Can Trust | Presenter Script

Course: AI-16 · Video: 5 min · Words: 678

## Hook
A summary is nice to read, but a workflow cannot make decisions from a paragraph. It needs fields: category, urgency, language. Today, you make the model return data the next node can use, and you check it before anything depends on it.

## Explain
Last time, the model gave us one sentence per review. Now we want structured output. That means asking the model for a fixed shape, usually JSON, instead of free text. You describe the shape in the system prompt, and give one example.

Three habits help. Use a short, closed list of allowed values for each field. Include an other or not sure value, so the model is not forced to guess. And ask for JSON only, with no explanation around it. The Claude API also offers stronger methods, so check the current documentation for the recommended one.

But even with a good prompt, never trust the output without checking it.

The model can add text before the JSON, use a value outside your list, or leave out a field. So you add a validation step in a Code node, before any other node uses the result. It tries to read the JSON safely. It checks each field against your allowed values. And it marks the item as valid or not valid.

Then an IF node sends valid items forward, and invalid items to a needs review tab. A simple rule for invalid output: retry once, then send it to review. Do not retry many times. Each retry costs money, and if the model fails twice on the same email, a person should look at it.

Think of the receiving desk in a warehouse. Every delivery is checked against the order form. A box that does not match goes to a separate shelf, for a person to inspect. It never goes straight onto the shop floor.

## Demonstrate
Let's build it. Beatriz Carvalho manages guest services at a hotel in Lisbon, Portugal. Guests write in Portuguese, English, French and Spanish. She wants each email sorted by category, urgency and language, so the right person sees it first. She uses ten invented emails. Her sheet has three tabs: emails, classified, and needs review.

In n8n, she builds a manual trigger, a Sheets node that reads the emails, and an HTTP Request to Claude, with the system prompt and a small output limit.

Next, she adds the validation Code node. For one email, you'll see something like: category complaint, urgency high, language French, and valid set to true.

She adds an IF node on valid. Valid items go to the classified tab. Invalid items get one retry, with a note that says the last answer was not valid JSON. If the second check fails too, the item goes to needs review, with its original text.

Now she tests the edges. An email that says only question marks comes back as category other, which is valid. A very long email that mixes three languages lands in needs review, which is exactly where it should go.

A common mistake is to read the JSON in the next node with no error handling. Then, when the model adds a line like here is the JSON, the whole workflow stops, and the other items are never processed. Always read the JSON safely, mark the item as invalid, and route it. One bad item should never stop the batch.

## Recap
Let's recap. First, ask for a fixed JSON shape, with closed lists of allowed values and an other or not sure option. Second, validate every result in a Code node before other nodes use it. Third, for invalid output, retry once, then send the item to a needs review list for a person.

## CTA
Now it is your turn. In the exercise below this video, you will classify ten sample emails as JSON, validate each one, and send invalid results to a separate tab. You will also break the prompt on purpose, and check that the workflow keeps running. It takes about forty-five minutes. In the next lesson, we look at Routing and Decisions. See you there.

## Thumbnail
Headline: JSON You Can Trust
Image: Navy background, a curly-brace data card passing through a teal checkpoint gate, one card continuing and one card diverted to a 'review' shelf, headline in teal Inter Bold.

## Production Notes
- [VERSION] Claude API structured output: the recommended method for JSON output (prompting, tool input schemas or a dedicated structured output option) and the response path content[0].text must be checked against current documentation. The voiceover says only that stronger options exist and learners should check the documentation.
- [VERSION] n8n HTTP Request, Code ($input.all()) and IF node options must be checked against the current release.
- Screen recording: the validation JavaScript and the JSON shape come from content.md and are shown on screen; the voiceover describes them and does not read them. The JSON result for email E07 is an example output.
- Beatriz Carvalho and her Lisbon hotel are fictional; all 10 emails are invented, with no real guest names.
