# L14 Writing the Evaluation Plan | Presenter Script

Course: AI-27 · Video: 5 min · Words: 665

## Hook
We will evaluate it carefully is not a plan. A plan says what you measure, on which data, against which number, at which moment, and who decides what happens next.

## Explain
Last time, you wrote the product sections of your PRD. Today is capstone step two. Your evaluation plan turns the metric tree and the test set into a schedule of decisions. It has five parts.

First, test set design: its size, the case types and their shares, who writes the expected behaviour, and how the set is updated. Add new cases from real failures after launch, but keep a fixed core set, so results stay comparable over time.

Second, the rubric and rating method. Define each score with an example. Humans are the reference. If you use an LLM as judge, write a spot check rule, such as humans rate at least twenty percent of judge scored cases, and every case in a weak language.

Third, metrics and thresholds. Each metric gets a pass threshold, good enough to continue. Critical metrics also get a fail threshold that means stop or roll back. Set them before you see results. Critical failures, such as invented refunds or exposed personal data, usually have a threshold of zero.

Fourth, three evaluation moments. Before launch, the test set must pass before any user sees the feature. During the pilot, online metrics against a baseline, and weekly human review. After launch, a dashboard, regular sample reviews and test set reruns after every change. Fifth, a review schedule, with who decides to continue, fix or stop.

Think of the inspection schedule for a new bridge. Engineers test the design before building, and the structure before opening. They inspect it on a fixed schedule after opening, with clear limits that close the bridge. Nobody decides the limits after seeing the cracks.

## Demonstrate
Let's see an example. Dewi Lestari is a PM at a hypothetical telecom company in Indonesia. Her feature drafts replies for support agents answering messages about data packages, billing and network problems. Agents edit and send each draft.

Her test set has one hundred and fifty invented cases: seventy common, thirty edge, thirty split between formal Indonesian, informal Indonesian and English, and twenty that should refuse or redirect. Two senior agents write the expected behaviour. New failure cases are added every month, but the core one hundred and fifty stay fixed.

An LLM judge scores the full set after each change. Senior agents rate a random thirty of those cases, plus every informal language case and every refusal case.

Before launch, the whole set must pass at eighty percent or more, and falling below seventy percent means stop. Each language group must reach seventy five percent, with a stop below sixty five. Invented offers or refunds must be zero, and all twenty refusal cases must redirect correctly.

During the pilot, more than half of drafts should be sent with light or no editing by week four. Handling time must beat the baseline, and the complaint re open rate must not stay above it for two weeks. Dewi and the operations lead meet every two weeks to decide, and the operations lead owns the kill switch.

A common mistake is setting thresholds only for the overall pass rate. A feature can pass overall, while failing a whole language group.

## Recap
Let's recap. First, an evaluation plan covers test set design, the rubric and rating method, metrics with thresholds, three evaluation moments and a review schedule with owners. Second, set pass and fail thresholds before seeing results, for each user group, with zero tolerance for critical failures. Third, evaluation continues after launch.

## CTA
Now it is your turn. This is capstone step two. In the exercise below, write your evaluation plan, with your test set design, rubric, a threshold table of at least six metrics, and a review schedule. Start from your twenty cases from lesson nine. It takes about forty five minutes. In the final lesson, we review and present your PRD. See you there.

## Thumbnail
Headline: Limits Before the Cracks
Image: Navy background, a bridge with inspection markers at three points and a small threshold table beside it, headline in teal Inter Bold.

## Production Notes
- [VERSION] Google Sheets features and Claude free-plan limits and data-use terms must be checked before recording (exercise tools).
- Dewi Lestari and the telecom company in Indonesia are hypothetical; stock footage must not show a real telecom brand or logo.
- The test set and threshold figures (150 cases: 70 common, 30 edge, 30 language, 20 refuse; pass at least 80 percent, fail below 70 percent; each language group pass 75, fail below 65; zero invented offers; all 20 refusal cases) must match content.md exactly.
