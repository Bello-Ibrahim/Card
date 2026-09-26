# L09 Building a Test Set and Running Evaluations | Presenter Script

Course: AI-27 · Video: 5 min · Words: 696

## Hook
Test an AI feature only with questions from a team meeting, and it will pass. Real users will ask everything else. A good test set is your chance to meet those users before launch.

## Explain
Last time, you designed a metric tree. Today, we build the test set behind your offline metrics, and run it live. A test set is a fixed list of inputs, with a clear idea of what a good output looks like.

Include four types of case. Common cases, the questions most users ask. Edge cases, unusual but valid inputs, such as a deadline passed by one day. Different users and languages, every group you serve. And should refuse cases, requests the feature must decline, such as asking for another person's data.

Score each output with a three point rubric. Two is a pass: correct, complete and following policy. One is partial. Zero is a fail: wrong, inventing policy, or answering something it should refuse. Write the criteria before you run anything, and report the pass rate for each case type, because an average hides weak groups.

Human rating is the reference. LLM as judge means asking a model to score outputs against your rubric. It is fast, but it can be too generous, prefer long answers and miss policy errors. So use it only with human spot checks, and look at every disagreement.

Think of a driving test. A test only on empty roads on sunny days tells you little. A good test includes night driving, rain and a sudden obstacle. Your edge cases and refusal cases are the night driving and the rain.

## Demonstrate
Let's run one. Maria Santos is a PM at a hypothetical home goods shop in the Philippines. Her feature answers questions about returns, using the shop's return policy. In Google Sheets, she creates columns for ID, type, input, expected behaviour, output, human score and judge score.

She fills twenty rows with invented cases: eight common, five edge, four language, and three should refuse. All cases are invented, with no real customer data. She pastes each input into Claude with the policy, and copies the answer into the output column. Then she scores each answer with the rubric.

Next, she opens a new Claude chat, gives it the rubric, and sends one case at a time, asking for a score of zero, one or two with one reason. She records each score in the judge column.

Now she adds formulas for the pass rate, the pass rate for each type, and the agreement between her and the judge. Her human pass rate is twelve of twenty, or sixty percent. By type, common cases pass at seventy five percent, but edge cases only at forty percent.

The judge gives fourteen passes, which is seventy percent. It agrees with Maria on fifteen of twenty cases, which is seventy five percent. It scores higher than Maria on four cases, and lower on one.

She filters the rows where the two scores differ, and reads each one. The biggest miss is case sixteen. The answer in Cebuano was wrong, but the judge gave it a two. So the judge is too generous, and weak on less common languages. Every judge score in those languages needs human review.

A common mistake is letting the judge replace human rating because it is faster. Keep humans as the reference, and never report a judge only score without saying so. The judge then inherits blind spots, such as a language it handles poorly.

## Recap
Let's recap. First, a test set needs common cases, edge cases, different users and languages, and cases that should be refused, with the rubric written first. Second, report the pass rate for each case type, because averages hide weak groups. Third, LLM as judge is useful but limited. Measure its agreement with humans, and review every disagreement.

## CTA
Now it is your turn. In the exercise below, write a twenty case test set in Google Sheets, run each case through Claude, and score the outputs with a three point rubric, just as Maria did. It takes about forty minutes. In the next lesson, we look at working with data scientists and engineers. See you there.

## Thumbnail
Headline: Test for Night Driving
Image: Navy background, a car on a wet night road beside a small spreadsheet with scores 0, 1 and 2, headline in teal Inter Bold.

## Production Notes
- [VERSION] Claude free-plan limits and data-use terms, and the Google Sheets COUNTIF, COUNTIFS and SUMPRODUCT formulas, must be checked before recording the screen demo.
- Screen demo: record in Google Sheets and Claude with a prepared sheet holding Maria's 20 invented cases from content.md (types, inputs, human and judge scores exactly as in the table). Use a short invented return policy as context. No real customer data.
- The metrics must be spoken and shown exactly: human pass rate 12 of 20, 60 percent; judge 14 passes, 70 percent; agreement 15 of 20, 75 percent; judge higher on 4 cases and lower on 1; biggest miss case 16 (Cebuano). These were checked against the sample table in content.md.
- LLM-as-judge is taught as a technique with limits and human spot checks, never as a replacement for human rating (curriculum flag).
- Maria Santos and the online home-goods shop in the Philippines are hypothetical. Tagalog, Taglish and Cebuano inputs on screen should be checked by a speaker before recording.
