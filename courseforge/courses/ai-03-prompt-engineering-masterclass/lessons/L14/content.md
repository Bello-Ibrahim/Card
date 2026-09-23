# L14 Building and Testing Your Library

Course: AI-03 · Module: M3 · Objectives: O5, O6 · Video: 5 min

## Hook
A template that worked once might have worked by luck. Before you trust it, and before a colleague uses it, test it with different inputs.

## Explanation
Each template in your library should be tested **at least twice, with different inputs**. One test shows that the template can work. Two or more tests show whether it works reliably.

Choose test inputs that are really different:

- a **typical case**, such as a normal weekly update,
- a **harder case**, such as a sensitive topic, a very short set of notes or an unusual request.

For each test, use the same method as in L12 and L11:

1. **Fill the placeholders** with realistic, non-confidential input.
2. **Run the template** in a new chat.
3. **Check the output** with the four-part checklist: facts, sources, bias and confidentiality.
4. **Score** it from 1 to 5 on accuracy, format and tone.
5. **Record the result** on the prompt card: the input you used, the scores, the problems and any change you made.

When a test shows a weakness, use the diagnosis from L10. Was the task unclear? Was context missing? Was the format specified? Did instructions conflict? Make one targeted change, raise the version number, for example from v1 to v2, and test again.

Free plans may limit how many messages you can send each day. [VERSION] Plan your testing across several days if needed, for example five templates a day.

**Analogy:** Testing a template is like testing a new bridge design with different loads. One light car crossing safely does not prove much. Engineers test with a typical load and a heavy load before the bridge opens to the public.

## Worked Example
Leila is a school administrator at a hypothetical private school in Amman. Her template writes letters to parents:

```text
You are a school administrator. Write a letter to parents of [YEAR
GROUP] students about [SITUATION]. Include: what is happening, what
parents need to do, and the deadline [DATE]. Warm and clear tone,
under 180 words. Use simple English for parents who may read English
as a second language. Do not add facts that are not in my notes.
Notes: [PASTE NOTES - no student names]
```

**Test 1 (typical case):** a school trip to a museum, with a consent form due on a date. The letter is clear, 160 words, and includes the deadline. Scores: accuracy 5, format 5, tone 5.

**Test 2 (harder case):** several students had a stomach illness after a school lunch, and the school has changed the catering company. The letter is under 180 words, but it says "there is no risk to any student", which is not in Leila's notes and is not something she can promise. The tone is also too cheerful for a health topic. Scores: accuracy 2, format 5, tone 2.

Leila diagnoses missing context and a gap in the constraints. She changes the template:

```text
... Match the tone to the situation: serious and calm for health or
safety topics. Do not make promises or reassurances that are not in
my notes. ...
```

She saves it as v2 and repeats both tests. The trip letter is still good. The illness letter is now calm, factual and makes no new promises. Her prompt card records both versions, the inputs, the scores and the change.

## Common Mistake
Many learners test each template with two very similar inputs, such as two routine updates. Both pass, and the weakness stays hidden until a real, difficult situation arrives. Always make one of your tests a harder case: a sensitive topic, missing information or an unusual audience.

## Key Takeaways
1. Test every template at least twice with different inputs: one typical case and one harder case.
2. Check each output with the four-part checklist, score it, and record the input, scores and changes on the prompt card.
3. When a test fails, make one targeted change, raise the version number and test again.

## Hands-on Exercise
**Task:** Capstone step 2: write all 15 prompts, test each one at least twice, and record the result and any change you made.
**Tools:** Claude, ChatGPT or Gemini (free tiers) [VERSION]; your prompt cards from L13 in a spreadsheet or document.
**Steps:**
1. Write the remaining 12 templates from your task list, using the six parts and placeholders.
2. For each template, prepare one typical input and one harder input. Use only non-confidential or invented material.
3. Run each test in a new chat and check the output with the four-part checklist.
4. Score each output from 1 to 5 on accuracy, format and tone.
5. Record the inputs, scores and problems on the prompt card.
6. Fix any weak template with one targeted change, update the version number and test again.
7. Plan your tests across several days if you reach a usage limit.
**What good looks like:** 15 prompt cards, each with at least two test results, including one harder case, scores and a clear note of any change and its version number.
**Time:** about 60 minutes, across more than one session if needed

## Review Flags
- [VERSION] Free-tier usage limits of Claude, ChatGPT and Gemini may restrict how many tests learners can run in one day; check current limits before scripting.
