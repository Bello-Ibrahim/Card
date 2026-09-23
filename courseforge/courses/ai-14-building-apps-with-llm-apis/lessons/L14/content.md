# L14 Capstone Step 1: Build the Core Feature

Course: AI-14 · Module: M4 · Objectives: O3, O4, O7 · Video: 5 min (screen demo)

## Hook
You now know every part: prompts, structured outputs, streaming, tools and guardrails. In the next three lessons you put them together into one small app that works, that others can use, and that shows what it costs.

## Explanation
The capstone is a deployed web app that uses an LLM API with validated structured outputs, streaming, optional tool use, usage logging and a cost dashboard. This lesson covers step 1: choosing the use case, writing a spec and building the core feature.

**Choose a small, useful use case.** Good capstone features take one kind of input and return structured data that the app then uses. Examples:

- A job-advert analyser for a recruitment agency: extract role, skills, salary range and red flags.
- A meal planner for a grocery app: turn a budget and diet into a structured weekly plan with a shopping list.
- A support-ticket triage tool: category, urgency and a draft reply.

Avoid features that need search over many documents (AI-15) or long multi-step agents (AI-16).

**Write a one-page spec before any code.** Include:

1. **User and problem**: who uses it and what they need.
2. **Input and output**: what the user gives, and the output schema.
3. **Prompt plan**: role, rules, data tags and examples.
4. **Tool (optional)**: one tool only if it adds real data, such as a salary table or a product catalogue.
5. **Limits**: model, max_tokens, spend limit, what personal data is excluded.
6. **Success**: how you will know it works (you will build the eval set in L16).

**Build the core feature in layers.** First the schema and a structured call that you test in the terminal. Then streaming of any free-text part. Then the Streamlit page. Then the tool, if you have one. Test each layer before you add the next.

**Analogy:** Writing a spec before coding is like drawing a floor plan before you build a small house. The plan takes an hour, but it stops you from building a kitchen with no door.

## Worked Example
Agnieszka Nowak builds a job-advert analyser for a recruitment agency in Kraków, Poland. Recruiters paste an advert and get structured data plus a short streamed comment for the candidate.

Her schema:

```python
from typing import Optional
from pydantic import BaseModel

class JobAnalysis(BaseModel):
    job_title: str
    seniority: str                 # "junior", "mid" or "senior"
    required_skills: list[str]
    salary_min: Optional[float]
    salary_max: Optional[float]
    currency: Optional[str]
    red_flags: list[str]           # e.g. "no salary given"
```

Her core function makes two calls. The first returns the validated object with the structured-output helper from L05. The second streams a short plain-language comment built from that object:

```python
def analyse(advert):
    r = client.messages.parse(
        model=MODEL, max_tokens=600, system=EXTRACT_PROMPT,
        messages=[{"role": "user", "content": f"<advert>{advert}</advert>"}],
        output_format=JobAnalysis,   # [VERSION]
    )
    if r.stop_reason != "end_turn":
        raise RuntimeError(f"Stopped early: {r.stop_reason}")
    return r.parsed_output, r
```

In Streamlit she shows the fields with `st.json(analysis.model_dump())`, then streams the comment with `st.write_stream()` as in L08. [VERSION]

She considered a tool that looks up typical salaries by role in a local table. Her spec says it is optional, so she adds it only after the core feature passes her first five manual tests. The tool is read-only and uses the loop limits from L10.

She tests five invented adverts on screen, including one in Polish and one with no salary, and checks that `salary_min` is empty and "no salary given" appears in `red_flags` for that advert (example output).

## Common Mistake
Many learners start with an ambitious idea and a large prompt, and try to build the page, the tool and the dashboard at the same time. When something fails, they cannot tell which part is broken. Keep the feature small, write the spec first, and build and test one layer at a time.

## Key Takeaways
1. Choose a small use case that takes one kind of input and returns structured data your app uses.
2. Write a one-page spec (user, input and output schema, prompt plan, optional tool, limits, success) before coding.
3. Build in layers: validated structured call, streaming, web page, then an optional tool with guardrails.

## Hands-on Exercise
**Task:** Capstone step 1: write the spec and build the core feature with a validated schema and streaming output.
**Tools:** Python with `anthropic`, `pydantic` and `streamlit`; your code from L05–L10; a text editor for the spec.
**Steps:**
1. Choose your use case and write the one-page spec with all six headings.
2. Define the output schema as a Pydantic class.
3. Write the system prompt with data tags and at least one example, and save it in a file.
4. Build the structured call and test it in the terminal on 5 invented inputs. Check the stop reason and validation errors.
5. Add a streamed free-text part, such as a comment, summary or draft.
6. Build the Streamlit page that shows the structured fields and the streamed text.
7. Optional: add one read-only tool with a step limit and input checks.
8. Commit the spec, prompt and code to Git, with no keys in the repository.
**What good looks like:** A clear spec, a schema that validates on all 5 test inputs, streamed text in the web page, and code in version control. Any tool is small, read-only and limited.
**Time:** about 90 minutes

## Review Flags
- [VERSION] The structured-output helper (`messages.parse`, `output_format`, `parsed_output`) and Streamlit functions (`st.json`, `st.write_stream`) must be checked against the current docs.
- The agency and adverts in the worked example are invented.
