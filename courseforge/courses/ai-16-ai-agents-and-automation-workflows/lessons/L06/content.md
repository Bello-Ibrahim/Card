# L06 Structured Output: Getting JSON You Can Trust

Course: AI-16 · Module: M2 · Objectives: O3 · Video: 5 min (screen demo)

## Hook
A summary is nice to read, but a workflow cannot make decisions from a paragraph. It needs fields: category, urgency, language. Today you make the model return data that the next node can use, and you check it before anything depends on it.

## Explanation
**Structured output** means asking the model for a fixed shape, usually JSON, instead of free text. You describe the shape in the system prompt and give one example:

```text
Return only JSON with this shape, and no other text:
{"category": "booking" | "complaint" | "question" | "other",
 "urgency": "high" | "normal" | "low",
 "language": "<ISO 639-1 code, e.g. pt>"}
```

Good practice:

- Use a short, closed list of allowed values for each field.
- Include an "other" or "not sure" value, so the model is not forced to guess.
- Ask for JSON only, with no explanation around it.

The Claude API also offers stronger options, such as defining a tool with an input schema and asking the model to use it, so the reply arrives as structured tool input. Check the current documentation for the recommended method. [VERSION]

Even with good prompts, **never trust the output without checking it.** The model can add text before the JSON, use a value outside your list or leave out a field. So you add a **validation step** in a Code node before any other node uses the result:

```javascript
const ALLOWED = {category: ['booking','complaint','question','other'],
                 urgency: ['high','normal','low']};
return $input.all().map(item => {
  let data, ok = true;
  try { data = JSON.parse(item.json.content[0].text); } catch { ok = false; }
  if (ok) for (const [k, list] of Object.entries(ALLOWED))
    if (!list.includes(data[k])) ok = false;
  if (ok && !/^[a-z]{2}$/.test(data.language || '')) ok = false;
  return {json: {...(data || {}), email_id: item.json.email_id, valid: ok}};
});
```

Then an **IF** node sends valid items forward and invalid items to a "needs review" sheet tab. A simple policy for invalid output: **retry once**, then send the item to review. Do not retry many times; if it fails twice, a person should look at it.

**Analogy:** Validation is like a receiving desk in a warehouse. Every delivery is checked against the order form: right item, right quantity, right label. A box that does not match goes to a separate shelf for a person to inspect. It never goes straight onto the shop floor.

## Worked Example
Beatriz Carvalho manages guest services at a hypothetical hotel in Lisbon, Portugal. Guests email in Portuguese, English, French and Spanish. She wants each email sorted by category, urgency and language. She uses 10 invented emails. On screen, she:

1. Creates a sheet with tabs "emails" (`email_id`, `text`), "classified" and "needs_review".
2. Builds: Manual Trigger, Google Sheets (get rows from "emails"), HTTP Request to Claude with the system prompt above and `max_tokens` kept small. [VERSION]
3. Adds the Code node above. For one email the output is `{"category": "complaint", "urgency": "high", "language": "fr", "email_id": "E07", "valid": true}` (example output).
4. Adds an **IF** node on `valid` is true. [VERSION]
5. On the true branch: Google Sheets (append to "classified").
6. On the false branch: a second HTTP Request with the same prompt plus "Your previous answer was not valid JSON. Return only the JSON." and a second Code check. If it fails again, append to "needs_review" with the original text.

She tests with an email that says only "????". The model returns category "other", which is valid. She then tests with a very long email mixing three languages; one run lands in "needs_review", which is exactly where it should go.

## Common Mistake
Learners often write `JSON.parse` directly in the next node with no error handling. When the model once adds "Here is the JSON:" before the data, the whole workflow stops with an error, and the remaining items are not processed. Always parse inside `try/catch`, mark the item as invalid, and route it. One bad item should never stop the batch.

## Key Takeaways
1. Ask for a fixed JSON shape with closed lists of allowed values and a "not sure" or "other" option.
2. Validate every result in a Code node before other nodes use it: parse safely, check each field and mark the item valid or not.
3. For invalid output, retry once, then send the item to a "needs review" list for a person.

## Hands-on Exercise
**Task:** Classify 10 sample emails into category, urgency and language as JSON, validate each result, and send any invalid result to a separate sheet tab.
**Tools:** n8n self-hosted; Google Sheets; Claude API (paid, keep the run small).
**Steps:**
1. Write 10 invented emails in at least 3 languages. Include one nonsense email and one very long one. Do not use real guest messages or names.
2. Create the "emails", "classified" and "needs_review" tabs.
3. Build the workflow from the worked example, using your own allowed values.
4. Run it on one email, check the JSON, then run all 10.
5. Change the prompt on purpose so it asks for "a short explanation and the JSON". Run once and confirm that invalid items reach "needs_review" without stopping the workflow. Then fix the prompt.
**What good looks like:** Every email ends in exactly one tab; valid rows contain only allowed values; the broken prompt produces review items instead of a failed run.
**Time:** about 45 minutes

## Review Flags
- [VERSION] Claude API structured output: the recommended method for JSON output (prompting, tool input schemas or a dedicated structured output option) and the response path `content[0].text` must be checked against current documentation.
- [VERSION] n8n HTTP Request, Code (`$input.all()`) and IF node options must be checked against the current release.
