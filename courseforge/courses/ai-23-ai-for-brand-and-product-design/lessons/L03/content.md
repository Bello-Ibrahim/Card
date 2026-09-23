# L03 From Insights to Personas and Jobs to Be Done

Course: AI-23 · Module: M1 · Objectives: O2, O5 · Video: 5 min

## Hook
Ask an AI tool for a persona and you will get one in seconds: a name, an age, a job, a favourite coffee order and three frustrations. It sounds real. But where did any of it come from?

## Explanation
Verified themes from research are useful, but they are not yet easy to design with. Two common tools help you turn them into something a team can use: **jobs-to-be-done statements** and **personas**.

A **job-to-be-done (JTBD) statement** describes what a person is trying to achieve in a situation, without describing a solution. A common structure is:

> When [situation], I want to [motivation], so I can [expected outcome].

For example: "When my child has a fever at night, I want to see which clinic has an open slot tomorrow morning, so I can plan my day before I go to sleep." JTBD statements keep the team focused on needs, not features.

A **persona** is a short profile that represents a group of real users. A lightweight persona needs only a few parts: a name and role, a goal, key behaviours, pain points and the evidence behind each point. Details such as a favourite film are not useful unless research shows they matter.

Claude is good at turning verified themes into draft JTBD statements and personas, because it can phrase ideas clearly and quickly. The risk is **synthetic users**: personas or "user quotes" that the model invents to fill gaps. They sound realistic, but they are not based on data. If a team designs for a synthetic user, it designs for a person who may not exist.

The protection is simple: **label every claim.** Each line in a persona or JTBD statement is either:

- **From research:** supported by named themes or participant IDs.
- **Assumption:** reasonable, but not yet supported. It becomes a question for the next round of research.

When you prompt Claude, give it only your verified themes and ask it to cite the theme for every claim and to write "assumption" where it has no support.

**Analogy:** A persona is like a composite sketch made from witness statements. A good sketch artist draws only what the witnesses described. If the artist adds a scar that nobody mentioned, the sketch looks more complete, but it is now misleading. Labelling claims shows which parts of the sketch came from witnesses.

## Worked Example
Dewi Santoso is a product designer at a hypothetical health-tech company in Surabaya, Indonesia. Her team is designing a clinic booking app for patients. She has four verified themes from interviews with 10 patients:

- T1: Patients book for family members more often than for themselves (7 participants).
- T2: Uncertain waiting times at the clinic cause stress (6 participants).
- T3: Many patients prefer to confirm bookings through a messaging app (5 participants).
- T4: Some older patients ask younger relatives to book for them (3 participants).

She asks Claude: "Using only these themes, write 3 JTBD statements and one lightweight persona. After every claim, cite the theme in brackets or write (assumption)."

Claude's persona includes: "Rina, 34, books appointments for her two children and her mother (T1, T4). She gets anxious when she cannot see how long she will wait (T2). She prefers confirmations by messaging app (T3). She works as a teacher and mostly books during lunch breaks (assumption)."

Dewi reviews the output. The job and booking time are assumptions, so she keeps "books during short breaks" as a question for research and removes the job title. One JTBD statement mentions "paying online", which is not in any theme. She marks it as an assumption and moves it to the research backlog. The final persona is shorter but every line can be defended.

## Common Mistake
Many designers accept a full, detailed AI persona because it feels more "real" than a short one. More detail does not mean more truth. A second mistake is to use AI-generated "interviews" with imaginary users as a replacement for research. They can help you prepare interview questions, but they are not evidence about real people.

## Key Takeaways
1. JTBD statements describe a situation, a motivation and an outcome; lightweight personas summarise goals, behaviours and pain points with evidence.
2. "Synthetic users" invented by AI sound real but are not data, so they must never replace research.
3. Label every persona and JTBD claim as "from research" or "assumption", and turn assumptions into research questions.

## Hands-on Exercise
**Task:** Write 3 jobs-to-be-done statements and one persona with Claude, then mark each claim as "from research" or "assumption".
**Tools:** Claude (free plan); your verified themes from the L02 exercise; a document or Figma frame.
**Steps:**
1. Copy your verified themes from L02, with their participant IDs. Do not include any personal data.
2. Ask Claude for 3 JTBD statements using the "When... I want to... so I can..." structure, citing a theme for each part.
3. Ask Claude for one lightweight persona: name, goal, 3 behaviours, 3 pain points, each with a theme reference or "(assumption)".
4. Check every citation against your themes. Correct any that are wrong.
5. Mark each line "from research" or "assumption", and remove decorative details with no evidence.
6. List the assumptions as questions for future research.
**What good looks like:** 3 clear JTBD statements with no solutions in them, a persona where every line is labelled, and a short list of research questions made from the assumptions.
**Time:** about 25 minutes

## Review Flags
- None. The example is hypothetical and the lesson teaches general research practice without tool-specific or legal claims.
