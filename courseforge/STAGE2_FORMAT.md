# Stage 2 formats

`check_content.py` enforces these formats.

## lessons/{lesson_id}/content.md

This is the teaching source for the lesson. Stage 3 turns it into a spoken
script of about 700 words, so it can be longer and more detailed than the
script (450–1,100 words in total).

```markdown
# L01 What Is AI, Really?

Course: AI-01 · Module: M1 · Objectives: O1 · Video: 5 min

## Hook
One or two sentences: a question, surprise or everyday situation.

## Explanation
Plain-language teaching. Include one paragraph that starts with **Analogy:**.

## Worked Example
A concrete example with globally diverse names, countries and industries.

## Common Mistake
The misunderstanding learners usually have, and the correction.

## Key Takeaways
1. ...
2. ...
3. ...

## Hands-on Exercise
**Task:** ...
**Tools:** ... (free options first)
**Steps:**
1. ...
**What good looks like:** ...
**Time:** about N minutes

## Review Flags
- [VERIFY] / [VERSION] / [REGION] items for a human reviewer, or "- None."
```

Rules: use B2-level international English with no idioms. Don't state
unverified facts. Every [VERIFY], [VERSION] or [REGION] tag in the body must
also appear in Review Flags.

## modules/{module_id}/quiz.json

```json
{
  "course_id": "AI-01",
  "module_id": "M1",
  "questions": [
    {
      "id": "Q1",
      "lesson_id": "L01",
      "objective": "O1",
      "question": "...",
      "options": ["...", "...", "...", "..."],
      "answer_index": 2,
      "explanation": "Why the answer is right and the most tempting wrong option is wrong."
    }
  ]
}
```

Each module has exactly 5 questions and each question has 4 different
options. Spread the correct answers across positions. Every lesson in the
module is tested at least once.

## capstone_rubric.md

```markdown
# Capstone Rubric: <capstone title>

## Task
## Deliverables
## Criteria
| Criterion | Objective | Excellent | Good | Developing | Not yet | Points |
|---|---|---|---|---|---|---|
| ... | O4 | ... | ... | ... | ... | 25 |

Total: 100

## Submission Checklist
- ...
```

Include 4–6 criteria. Their points must add up to 100, and every objective
that the capstone assesses must appear in at least one criterion.
