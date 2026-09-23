# L12 Testing Prompts with a Small Evaluation Set | Presenter Script

Course: AI-14 · Video: 5 min · Words: 704

## Hook
You change one line in your prompt to fix a bad answer. It works. A week later, a user reports that dates are wrong again, and the bug came from your fix. Without tests, every prompt change is a gamble.

## Explain
In the last lesson, you tested attacks by hand. Now let's make testing a habit. An evaluation set is a fixed list of test inputs, with the properties you expect in the output. It is the prompt version of unit tests. You run it every time you change the prompt, the model or the code.

For a small feature, twenty to thirty cases are enough to start. Include normal cases from everyday use, and hard cases, like unusual formats or other languages. Add bad inputs, such as empty text or injection attempts. And every time a user reports a real bug, add that case too.

Check expected properties, not exact text, because the wording changes between runs. Automatic checks are cheap and objective. Did the output pass the schema? Are the required fields present, with the expected values? Is the length right? Did the app call the right tool?

For qualities like tone, you can ask a model to act as a judge, with a short, specific rubric. For example, does the reply avoid promising a refund? Answer pass or fail with one reason. Keep the rubric narrow, check some grades by hand, and remember that each judgement is another paid call.

Then compare versions. Run each prompt version on the same set, and record the pass rate, the cost from your logger, and the speed if it matters. A new version is better only if it passes at least as many cases, without an unacceptable rise in cost. A case that passed before and fails now is a regression. Fix it before you ship.

An eval set is like the fixed practice route at a driving school. Every student drives the same streets, with the same difficult roundabout. Because the route never changes, the instructor sees real progress, not a lucky day.

## Demonstrate
Johan Lindqvist maintains an invoice extractor for an accounting firm in Gothenburg, Sweden. He keeps twenty invented test invoices, each with expected values.

Here is one case in his cases file. It has an ID, the invoice file, and the expected currency, total and date. His set mixes normal Swedish invoices, hard formats from other countries, and a few bad inputs.

His runner loads every case and calls the extractor with a chosen prompt version. It checks that each expected field matches, adds up the cost from his logger, and prints any failing case. At the end, it prints the pass rate and total cost.

He runs version one and version two. You'll see something like this. Version one passes eighteen of twenty. Version two passes nineteen. It looks better. But look closer. Version two fixed two cases, and broke one that passed before, a Mexican invoice. That is a regression.

So Johan does not ship version two. He finds that his new rule about decimal commas confused Mexican number formats. He fixes the rule in version three, and ships only when it passes every case that version one passed.

A common mistake is to test a new prompt on two or three easy examples, see good answers, and ship it. Keep a fixed set, run it on every change, and look at regressions first, not just the total score.

## Recap
Let's recap. First, an evaluation set of twenty to thirty fixed cases, with expected properties, is the unit test for your prompts. Second, use automatic checks wherever you can, and use a model as a judge only with a narrow rubric and some checking by hand. Third, compare versions on the same set by pass rate and cost, and treat any regression as a bug to fix before shipping.

## CTA
Now it is your turn. In the exercise, you will build a twenty-case test set for your extractor, run two prompt versions, and report the pass rate and cost of each, with a clear recommendation. You will run this set again before your capstone launch. In the next lesson, Cost Control in Practice, you will cut your costs. See you there.

## Thumbnail
Headline: Test Every Prompt Change
Image: Navy background, a checklist of twenty small ticks with one red cross marked regression, headline in teal Inter Bold.

## Production Notes
- content.md Review Flags: none. All cases are invented and all outputs are example output.
- The eval results (v1 18 of 20, v2 19 of 20 with the mx-02 regression) are example output; label them on screen. Costs on screen stay as 0.0xx placeholders; do not show real prices.
- Johan Lindqvist and the Gothenburg accounting firm are fictional; test invoices are invented text.
