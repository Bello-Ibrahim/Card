# L13 Turning Findings into a Story

Course: AI-08 · Module: M3 · Objectives: O7 · Video: 5 min

## Hook
You have a findings log with twelve checked findings. You put all twelve on slides, and your audience remembers none of them. People do not remember lists of numbers. They remember one clear message and the reason to act on it.

## Explanation
A data story has three parts:

1. **One main finding:** the single most important thing the audience should remember. It answers your business question.
2. **Supporting evidence:** two or three findings, each with a chart, that show why the main finding is true.
3. **A recommended action:** what the audience should do next, and how they could measure whether it worked.

To choose the main finding, look at your findings log and ask: which finding matters most for the business question, is well checked, and leads to an action? A surprising finding is interesting, but if it does not lead to a decision, it belongs in the notes, not in the story.

Apply the **"so what?" test** to every chart. Read the chart and ask, "So what?" If the answer is "so we should change the reminder system", the chart supports the story. If the answer is "it is interesting", remove it or move it to an appendix.

For this capstone, the storyline has five slides, with one message per slide:

1. **The question:** what the business wanted to know, and the data you used.
2. **The key finding:** one sentence, with the most important number.
3. **The evidence:** charts that support the finding, each with a title that states its message.
4. **The recommendation:** a specific action and how to measure it.
5. **The limits:** what the data cannot tell you, and what would make the analysis stronger.

Write the message of each slide as a full sentence before you design anything. If you can read the five sentences aloud and they make sense as a story, the structure is right.

**Analogy:** A data story is like a news report. The headline gives the main point. The next paragraphs give the evidence. The end says what happens next. A reporter who reads out every note from their notebook does not have a story yet.

## Worked Example
Ananya manages an outpatient clinic in Chennai, India. Her business question: "Why do so many patients miss appointments, and what can we do?" Her fictional, anonymised data covers 1,000 appointments, with 180 no-shows (18%). Her findings log has 12 confirmed findings.

She applies the "so what?" test. "Most appointments are for general check-ups" is true but leads to no action, so she removes it. She chooses one main finding and three supporting findings:

- **Main finding:** "Patients booked more than three weeks ahead miss appointments much more often."
- **Support 1:** Appointments booked more than three weeks ahead: 124 no-shows out of 400 (31%). Booked within three weeks: 56 out of 600 (about 9%). Chart: a bar chart comparing the two groups.
- **Support 2:** Patients who received an SMS reminder missed 50 of 500 appointments (10%); those without a reminder missed 130 of 500 (26%). Chart: a bar chart.
- **Support 3:** No-shows are highest on Monday mornings. Chart: a bar chart by weekday and time.

Her five slide messages:

1. "We wanted to know why 18% of appointments are missed, using 1,000 appointments from the last six months."
2. "Patients booked more than three weeks ahead miss 31% of appointments."
3. "The gap is large, and reminders appear to help." (three charts)
4. "Send an SMS reminder to every patient two days before the visit, and compare the no-show rate after three months."
5. "The data shows patterns, not proof: patients who got reminders may differ in other ways, and we do not know patients' reasons."

Slide 5 is honest: the reminder finding is a correlation, and a trial is needed to test cause (L08).

## Common Mistake
Many learners present findings in the order they found them. That is the order of your work, not the order your audience needs. Start with the main finding, then show the evidence. Another mistake is a recommendation that is too general, such as "improve communication". Make it specific and measurable.

## Key Takeaways
1. A data story has one main finding, two or three supporting findings, and a specific recommended action.
2. Apply the "so what?" test to every chart and remove charts that do not support the message.
3. Plan five slides with one message each, and write each message as a sentence before designing anything.

## Hands-on Exercise
**Task:** Capstone step 2: choose your main finding and 3 supporting findings, and sketch a five-slide storyline with one message per slide.
**Tools:** Your findings log in Google Sheets; paper or a notes app. Optional: Claude or ChatGPT to comment on your storyline (paste only your messages, not raw or personal data).
**Steps:**
1. Read your findings log and mark each confirmed finding "action" or "no action" using the "so what?" test.
2. Choose one main finding that answers your business question.
3. Choose 3 supporting findings and name the chart you will use for each.
4. Write one full-sentence message for each of the five slides: question, key finding, evidence, recommendation, limits.
5. Read the five sentences aloud. If the story is not clear, change the order or the main finding.
6. Optional: ask an AI tool, "Is this storyline clear for a manager? What is missing?"
**What good looks like:** Five sentences that tell a clear story; a main finding with a number from your log; 3 supporting findings, each with a named chart type; a specific, measurable recommendation; and a limits sentence that names at least one weakness of the data.
**Time:** about 40 minutes

## Review Flags
- None. The clinic case and all figures are fictional and were checked for internal consistency.
