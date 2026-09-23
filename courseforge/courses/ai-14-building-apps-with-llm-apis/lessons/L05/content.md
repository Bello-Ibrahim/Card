# L05 Structured Outputs with JSON Schemas

Course: AI-14 · Module: M2 · Objectives: O3 · Video: 5 min (screen demo)

## Hook
Your code asks the model for an invoice total. The model replies: "Sure! The total appears to be around 4,500 rupees." Your code needs the number 4500 and the currency "INR". A friendly sentence is useless to a database.

## Explanation
Free text is good for people and bad for code. When another part of your program must read the result, you need **structured output**: data with fixed fields and types that your code can trust.

There are three steps.

**1. Define a schema.** A schema lists the fields, their types and which fields are required. In Python, the usual tool is **Pydantic**: you write a class, and Pydantic can produce a JSON Schema from it and check data against it. In TypeScript, **Zod** does the same job.

```python
from pydantic import BaseModel

class Invoice(BaseModel):
    supplier: str
    invoice_date: str      # ISO format, YYYY-MM-DD
    total: float
    currency: str          # ISO 4217 code, e.g. "EUR"
```

**2. Ask the API for output that matches the schema.** The Claude API has a structured-output feature: you pass a JSON Schema, and the reply is JSON that follows it. The Python SDK has a helper that accepts a Pydantic class and returns a parsed object. Parameter names and helpers change between SDK versions, so check the current docs. [VERSION]

```python
response = client.messages.parse(
    model=MODEL,
    max_tokens=500,
    system="Extract invoice fields. Use ISO dates and ISO currency codes.",
    messages=[{"role": "user", "content": f"<invoice>{text}</invoice>"}],
    output_format=Invoice,   # [VERSION]
)
invoice = response.parsed_output   # an Invoice object
```

Without the helper, you can pass the schema in the request with `output_config` and read the JSON text yourself with `json.loads`. [VERSION]

An older, widely used alternative is to define a **tool** whose `input_schema` is your schema and ask the model to call it. You then read the tool's input, which the SDK gives you as a parsed dictionary. L09 explains tools in detail.

**3. Still validate in your code.** The schema controls the shape, not the truth. The model can still read the wrong number from a blurred invoice or guess a missing date. Add business checks: is the total positive, is the date not in the future, is the currency in your allowed list? Use descriptions in the schema and the system prompt to say what to do with missing values, for example "use null if the date is not shown", and make that field optional in the schema.

**Analogy:** Asking for free text is like asking a colleague to "tell me about the invoice" by phone. Asking for structured output is like handing them a printed form with labelled boxes. The form makes the answer easy to file, but you still check that the numbers in the boxes are correct.

## Worked Example
Priya works on an accounting tool in Bengaluru, India, that reads supplier invoices sent by email. The invoices come from India, Mexico and Germany, in different layouts and date formats: "12/03/2026", "12 de marzo de 2026" and "12.03.2026".

She uses the `Invoice` class above and the system prompt "Extract invoice fields. Convert all dates to YYYY-MM-DD. Use the ISO 4217 currency code." For the Mexican invoice, example output:

```json
{"supplier": "Papelería del Centro", "invoice_date": "2026-03-12",
 "total": 18450.0, "currency": "MXN"}
```

Her code saves the `Invoice` object directly to the database. There is no string searching and no regular expressions.

Then she tests a German invoice where the total is written "1.234,50 EUR". The first result was 1.2345 (example output). The schema was valid, but the value was wrong. She adds a rule to the system prompt ("Numbers may use a comma as the decimal separator") and a business check that flags totals below 5 for human review.

## Common Mistake
Many developers ask for JSON in the prompt ("Reply only with JSON") and then parse the reply with `json.loads` and hope. Most of the time it works; sometimes the reply has extra text or a missing field, and the app crashes. Use the structured-output feature or a tool with a schema, parse the result into a typed object, and never extract fields with string matching.

## Key Takeaways
1. Define the output as a schema (Pydantic in Python, Zod in TypeScript) so your code receives fixed fields and types.
2. Use the API's structured-output feature or a tool with an input schema, and parse the result into an object, never with string matching.
3. A valid schema does not mean correct values: add business checks and a clear rule for missing data.

## Hands-on Exercise
**Task:** Build an invoice extractor that returns validated objects for 5 sample invoices written in different formats.
**Tools:** Your L02 setup; `pip install pydantic`; a text editor; the current structured-output docs. [VERSION]
**Steps:**
1. Write 5 short invented invoices as text, from 5 different countries, with different date and number formats. Do not use real invoices or personal data.
2. Define an `Invoice` Pydantic class with supplier, date, total and currency. Make the date optional.
3. Write a system prompt with rules for dates, currency codes and missing values.
4. Call the API with the structured-output helper (or a schema in `output_config`) for each invoice. [VERSION]
5. Print each parsed object, and log tokens with your L04 helper.
6. Add two business checks (for example, total greater than 0 and currency in an allowed list), and print "REVIEW" when a check fails.
**What good looks like:** Five parsed `Invoice` objects with correct ISO dates and currency codes, at least one invoice that tests a tricky format, and business checks that flag doubtful values instead of crashing.
**Time:** about 40 minutes

## Review Flags
- [VERSION] Structured-output parameters (`output_config`, `output_format`), the `messages.parse()` helper and `parsed_output` must be checked against the current SDK and docs before scripting; the tool-based alternative must also be confirmed.
- The example outputs are illustrative and labelled as such.
