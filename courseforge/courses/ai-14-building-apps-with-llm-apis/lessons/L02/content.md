# L02 Setup: API Keys, SDKs and a Low-Cost Budget

Course: AI-14 · Module: M1 · Objectives: O1, O6 · Video: 5 min (screen demo)

## Hook
An API key is like a credit card number for your code. If it leaks into a public repository, someone else can spend your money. Today you will make your first call, and you will set it up safely and cheaply from the first minute.

## Explanation
The Claude API is a **paid service**. You pay for every input and output token. The costs for this course can stay small, but only if you set limits before you start. Check whether new accounts receive any trial credit on the current pricing pages. [VERIFY]

**Availability.** The API is offered directly only in supported countries. If your country is not on the list, you may be able to reach the same models through a cloud provider. Check the current list before you create an account. [REGION] [VERIFY]

**Five setup steps.**

1. **Create an account** in the Claude Console and add a payment method. [VERSION]
2. **Set a monthly spend limit** in the billing or limits settings. Choose a small amount that you are happy to lose if something goes wrong. [VERSION]
3. **Create an API key** and copy it once. The Console will not show the full key again. [VERSION]
4. **Store the key in an environment variable**, never in your code. The official SDK reads `ANTHROPIC_API_KEY` automatically.
5. **Install the SDK**: `pip install anthropic` for Python, or `npm install @anthropic-ai/sdk` for the optional TypeScript path. [VERSION]

**Keep keys out of Git.** If you use a `.env` file, add `.env` to `.gitignore` before your first commit. If a key is ever committed, even for one minute, delete it in the Console and create a new one. Removing the file from Git is not enough, because the key stays in the history.

**Three habits that keep costs low while developing:**

- Use a **smaller, cheaper model** for building and testing. Switch to a larger model only when you have evidence that you need it.
- Keep **max_tokens low** (for example 300) while testing. You can raise it later for real features.
- Keep the model name in **one constant**, so you can change it in one place.

Model IDs and prices change, so this course never hard-codes them. Look them up on the models and pricing pages. [VERSION]

**Analogy:** Setting up an API account is like giving a teenager a prepaid travel card instead of your main bank card. The prepaid card has a fixed limit, you can cancel it at any time, and a mistake cannot empty your main account. The spend limit is the fixed limit; a new key is the replacement card.

## Worked Example
Mei Lin is a developer at a small travel start-up in Penang, Malaysia. She follows these steps on screen:

1. In the Console, she opens the billing settings and sets a low monthly limit. [VERSION]
2. She creates a key named `meilin-laptop-dev`, so she knows where it is used.
3. In her terminal (macOS or Linux) she runs `export ANTHROPIC_API_KEY="sk-ant-..."`. On Windows PowerShell she would use `$env:ANTHROPIC_API_KEY="sk-ant-..."`.
4. She creates a virtual environment and runs `pip install anthropic`.
5. She writes `first_call.py`:

```python
import anthropic

MODEL = "your-small-model-id"  # check the current models page [VERSION]

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY

response = client.messages.create(
    model=MODEL,
    max_tokens=300,
    messages=[{"role": "user", "content": "Suggest one day trip from Penang."}],
)

for block in response.content:
    if block.type == "text":
        print(block.text)
print("Stop reason:", response.stop_reason)
print("Input tokens:", response.usage.input_tokens)
print("Output tokens:", response.usage.output_tokens)
```

Example output:

```text
A day trip to Langkawi by ferry ...
Stop reason: end_turn
Input tokens: 17
Output tokens: 142
```

Notice that the key does not appear anywhere in the file. Mei Lin can share this file with her team safely.

## Common Mistake
Many beginners paste the key directly into the code "just to test", for example `anthropic.Anthropic(api_key="sk-ant-...")`, and then commit the file. Automated bots scan public repositories for keys. Always use an environment variable, check `git status` before each commit, and replace any key that has been exposed.

## Key Takeaways
1. The Claude API is paid: set a monthly spend limit before you make your first call.
2. Store the API key in the `ANTHROPIC_API_KEY` environment variable, never in code or Git, and replace any key that leaks.
3. While developing, use a smaller model, a low max_tokens value and a single MODEL constant, and look up model IDs and prices on the live pages.

## Hands-on Exercise
**Task:** Make your first API call, then print the reply text, the stop reason and the input and output token counts.
**Tools:** Claude Console; Python 3 with the `anthropic` package (or Node.js with `@anthropic-ai/sdk`); a terminal; a code editor such as VS Code (free).
**Steps:**
1. Check that the API is available in your country. [REGION] [VERIFY]
2. Create an account, set a monthly spend limit and create an API key. [VERSION]
3. Save the key as the `ANTHROPIC_API_KEY` environment variable. If you use a `.env` file, add it to `.gitignore` first.
4. Create a virtual environment and install the SDK.
5. Choose a small model from the models page and put its ID in a MODEL constant. [VERSION]
6. Copy the worked example, change the question to one about your own project, and run it with max_tokens set to 300.
7. Run it again with max_tokens set to 20. Compare the stop reason and the output token count.
8. Run `git status` and confirm that no file with your key will be committed.
**What good looks like:** The script prints a reply, `end_turn` for the first run, `max_tokens` for the 20-token run, and token counts for both. A spend limit is set, and the key is not in any file tracked by Git.
**Time:** about 30 minutes

## Review Flags
- [VERSION] Console steps (billing, spend limits, key creation), SDK install commands, model IDs and prices must be checked against the live Console and docs at recording time.
- [VERIFY] Whether new accounts receive any trial credit; estimate a realistic cost per learner before publishing.
- [REGION] [VERIFY] The API is offered only in supported countries; check the current country list and the cloud-provider alternatives.
- Token counts in the example output are illustrative, not real measurements.
