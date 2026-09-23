# L12 Testing Prompts with a Small Evaluation Set

Course: AI-14 · Module: M3 · Objectives: O5, O6 · Video: 5 min (screen demo)

## Hook
You change one line in your prompt to fix a bad answer. It works. A week later, a user reports that dates are wrong again, and the bug came from your "fix". Without tests, every prompt change is a gamble.

## Explanation
An **evaluation set** (eval set) is a fixed list of test inputs with the properties you expect in the output. It is the prompt version of unit tests. You run it every time you change the prompt, the model or the code, and compare the results.

**How big?** For a small feature, 20 to 30 cases are enough to start. Include:

- **Normal cases** that represent everyday use.
- **Hard cases**: unusual formats, long inputs, other languages, missing fields.
- **Bad inputs**: empty text, wrong document type, injection attempts from L11.
- **Real bugs**: every time a user reports a problem, add that case.

**What do you check?** Expected properties, not exact text, because the wording can change between runs.

**Automatic checks** are cheap and objective. Write them as normal code:

- Did the output pass schema validation?
- Are the required fields present, with the expected values (for example, total = 18450.0)?
- Is the length within limits? Is the language correct?
- Did the app call the right tool, or refuse to change data without confirmation?

**Model as a judge.** Some qualities, such as tone or helpfulness, are hard to check with code. You can ask a model to grade an output against a short, specific rubric, for example "Does the reply avoid promising a refund? Answer PASS or FAIL with one reason." Use this carefully: keep the rubric narrow, check a sample of its grades by hand, and remember that each judgement is another paid API call.

**Compare versions.** Run each prompt version on the same set and record the **pass rate**, the **cost** from your L04 log and, if relevant, the **latency**. A new version is better only if it passes at least as many cases without an unacceptable rise in cost. A case that passed before and fails now is a **regression**, and you should fix it before you ship.

**Analogy:** An eval set is like the fixed practice route a driving school uses. Every student drives the same streets, with the same difficult roundabout. Because the route never changes, the instructor can see real progress, not just a lucky day.

## Worked Example
Johan Lindqvist maintains an invoice extractor for an accounting firm in Gothenburg, Sweden. He stores 20 test invoices (all invented) in `evals/cases.json`, each with expected values:

```json
{"id": "se-07", "file": "evals/se-07.txt",
 "expect": {"currency": "SEK", "total": 12500.0, "invoice_date": "2026-02-28"}}
```

His runner calls the extractor for each case and applies automatic checks:

```python
import json

def run_eval(prompt_version):
    cases = json.load(open("evals/cases.json"))
    passed, cost = 0, 0.0
    for case in cases:
        text = open(case["file"]).read()
        inv, call_cost = extract(text, prompt_version)  # returns object and cost
        ok = inv is not None and all(
            getattr(inv, field) == value for field, value in case["expect"].items())
        passed += ok
        cost += call_cost
        if not ok:
            print("FAIL", case["id"])
    print(f"{prompt_version}: {passed}/{len(cases)} passed, cost {cost:.4f}")
```

Example output:

```text
FAIL se-07
FAIL de-03
v1: 18/20 passed, cost 0.0xx
FAIL mx-02
v2: 19/20 passed, cost 0.0xx
```

Version 2 fixed se-07 and de-03 but broke mx-02, which passed before. Johan does not ship v2. He finds that his new rule about decimal commas confused Mexican number formats, fixes the rule in v3, and ships only when v3 passes all cases that v1 passed.

## Common Mistake
Many developers test a new prompt on two or three examples they have in mind, see good answers, and ship it. Those examples are usually the easy cases, and nobody checks the older cases that used to work. Keep a fixed set, run it on every change, and look at regressions first, not just at the total score.

## Key Takeaways
1. An eval set of 20 to 30 fixed cases, with expected properties, is the unit test for your prompts.
2. Use automatic checks wherever possible, and use a model as a judge only with a narrow rubric and some checking by hand.
3. Compare prompt versions on the same set by pass rate and cost, and treat any regression as a bug to fix before shipping.

## Hands-on Exercise
**Task:** Build a 20-case test set for your extractor, run 2 prompt versions, and report the pass rate and cost of each.
**Tools:** Your extractor from L05–L06; your L04 cost logger; a JSON or CSV file for the cases.
**Steps:**
1. Write 20 invented test inputs: at least 10 normal, 6 hard and 4 bad inputs (including 1 injection attempt). Use no real personal data.
2. For each case, write the expected properties.
3. Write a runner that applies automatic checks and adds up the cost of each run.
4. Run the current prompt (v1) and record the pass rate, the cost and the failing case IDs.
5. Write a v2 prompt that tries to fix at least one failure, and run the same set.
6. List any regressions, and write a short recommendation: ship v2 or not, and why.
**What good looks like:** A saved 20-case set, a runner that prints pass rates and costs for both versions, a list of failures and regressions, and a clear recommendation based on the numbers.
**Time:** about 45 minutes

## Review Flags
- None. The lesson uses invented cases and example output only; any model ID or price comes from the learner's own L02 and L04 setup, which are flagged in those lessons.
