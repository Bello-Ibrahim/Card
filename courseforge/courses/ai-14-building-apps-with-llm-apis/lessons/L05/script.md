# L05 Structured Outputs with JSON Schemas | Presenter Script

Course: AI-14 · Video: 5 min · Words: 695

## Hook
Your code asks the model for an invoice total. The model replies, sure, the total appears to be around four thousand five hundred rupees. But your code needs a number and a currency code. A friendly sentence is useless to a database.

## Explain
In the last lesson, you learned to measure what each call costs. Now let's make the output useful to code. Free text is good for people and bad for programs. When another part of your program reads the result, you need structured output. That means data with fixed fields and types that your code can trust.

There are three steps. Step one, define a schema. It lists the fields, their types, and which ones are required. In Python, the usual tool is Pydantic. You write a small class, and Pydantic turns it into a JSON schema and checks data against it. In TypeScript, Zod does the same job.

Step two, ask the API for output that matches the schema. The Claude API has a structured-output feature. The Python SDK has a helper that takes your Pydantic class and gives you back a parsed object. Names of these settings change between versions, so check the current docs.

There is also an older, widely used option. You define a tool whose input schema is your schema, and read the tool's input. Lesson nine explains tools.

Step three, still validate in your code. The schema controls the shape, not the truth. The model can read the wrong number from a blurred invoice. So add business checks. Is the total positive? Is the date not in the future? And say clearly what to do with missing values, for example use null, and make that field optional.

Asking for free text is like asking a colleague to tell you about an invoice by phone. Structured output is like handing them a printed form with labelled boxes. It is easy to file, but you still check the numbers in the boxes.

## Demonstrate
Priya works on an accounting tool in Bengaluru, India. It reads supplier invoices from India, Mexico and Germany, each with a different layout and date format.

She opens her extractor. At the top is the Invoice class. The system prompt tells the model to convert all dates to one standard format, and to use standard currency codes. The invoice text goes inside tags, as you learned in lesson three.

The call uses the parse helper, with the Invoice class as the output format. The result is an Invoice object, not a string. She runs it on the Mexican invoice. You'll see something like the supplier name, the date in standard format, the total as a number, and the Mexican peso code.

She saves the object straight to the database. No string searching, and no regular expressions. Then she tests a German invoice, where the total uses a comma for decimals. The first result is wrong. The schema was valid, but the value was not.

So she adds a rule to the system prompt about comma decimals, and a business check that flags very small totals for human review. She runs it again, and the total is now correct.

A common mistake is to write reply only with JSON in the prompt, parse the text, and hope. Usually it works. Sometimes there is extra text or a missing field, and the app crashes. Use the structured-output feature, and never pull out fields with string matching.

## Recap
Let's recap. First, define your output as a schema, with Pydantic in Python or Zod in TypeScript, so your code receives fixed fields and types. Second, use the API's structured-output feature, or a tool with an input schema, and parse the result into an object. Third, a valid schema does not mean correct values, so add business checks and a clear rule for missing data.

## CTA
Now it is your turn. In the exercise, you will build an invoice extractor that returns validated objects for five invented invoices in different formats, with two business checks. You will reuse this schema idea in your capstone. In the next lesson, Validation, Errors and Retries, you will make it survive real failures. See you there.

## Thumbnail
Headline: Data Your Code Trusts
Image: Navy background, a messy paper invoice turning into a clean JSON card with four labelled fields, headline in teal Inter Bold.

## Production Notes
- [VERSION] Structured-output parameters (output_config, output_format), the messages.parse() helper and parsed_output must be checked against the current SDK and docs before recording. If names have changed, update the on-screen code; the voiceover describes the feature without naming parameters.
- [VERSION] Confirm that the tool-based alternative (a tool whose input_schema is the schema) is still supported as described.
- The example outputs (the Mexican invoice JSON and the first German result 1.2345) are illustrative: label them 'example output' on screen.
- Priya, the Bengaluru accounting tool and the supplier 'Papelería del Centro' are invented; all invoices on screen are invented text with no real personal data.
