# L11 Testing Your Assistant: Accuracy, Tone and Safety | Presenter Script

Course: AI-26 · Video: 5 min · Words: 706

## Hook
Your assistant answers your three test questions perfectly. Is it ready? Probably not. Real customers make spelling mistakes, write in other languages, ask two things at once, and get angry. Today you learn to test for real customers.

## Explain
This is capstone step three. You have an assistant and a hand-off flow. Now you need a test set, a fixed list of questions, each with the answer or behaviour you expect. About twenty questions is a good size for a first prototype.

Mix six types. About six standard questions from your scope. About four tricky ones, with spelling mistakes, very short messages, or two questions in one. About three out-of-scope questions, where you expect, I'm not sure, and an offer of a person.

Then about three emotional questions from angry, worried or sad customers. About two hand-off and safety questions, such as a legal threat or a request for a person. And about two questions in the other languages your customers use.

Score each answer from zero to two, on three points. Accuracy: is it correct and from the knowledge base? Tone: does it follow the tone guide, with empathy where needed? And hand-off: does it hand off when it should, and not when it should not?

Also note fairness. Is the answer just as good with spelling mistakes, or in another language? And note privacy. Does the assistant ask for more personal data than it needs?

The lesson page has an eight-point checklist for every test conversation. For example, did it use only facts from the knowledge base? Did it hand off for every trigger? Did it say that it is an AI assistant?

Then fix the biggest problems first. An invented answer or a missed safety hand-off matters more than a reply that is a little too long. And run the full test set again, because one fix can break something else.

Think of a driving test. A fair test does not only use an empty car park. It includes busy junctions, bad weather and a sudden stop. An assistant that only passes easy questions is not ready for real customers.

## Demonstrate
Let's look at an example. Mateo is testing an assistant for a hypothetical chain of fitness centres in Córdoba, Argentina. It covers opening hours, membership types, and how to freeze a membership. He runs twenty questions and scores them in a sheet. Most standard questions score well. But three problems stand out.

First, an invented answer. Asked, can I bring my dog, the assistant said yes, in the outdoor area. There is no such policy. Accuracy, zero. Second, a missed hand-off. A customer wrote: I hurt my back on your machine yesterday, and I want compensation. The assistant explained how to freeze a membership. Hand-off, zero.

Third, the answers in Spanish were shorter, and left out a step about freezing a membership. That is a fairness problem.

Mateo fixes them in order of risk. He adds injury, hurt and compensation, and the Spanish words, to the hand-off triggers. He strengthens the rule: if the answer is not in the knowledge base, do not guess. He adds the full Spanish article. Then he runs all twenty questions again, and records the new scores in a second column.

A common mistake is to write test questions that match your articles word for word. Real customers do not write like help articles. Ask a colleague who did not build the assistant to write some of your questions. Include the messy, emotional and unexpected messages you see in real work, without personal details.

## Recap
Let's recap. First, a test set of about twenty questions should mix standard, tricky, out-of-scope, emotional, hand-off and non-English questions. Second, score each answer for accuracy, tone and hand-off, and check fairness and privacy. Third, fix the highest-risk problems first, then run the full test set again.

## CTA
This is capstone step three. In the exercise, you will write twenty made-up test questions, score every answer in a sheet, fix the three biggest problems, and test again. Your capstone is almost complete. In the final lesson, we look at measuring success and keeping the human touch. See you there.

## Thumbnail
Headline: Test for Real Customers
Image: Navy background, a chat window on a test track with road signs shaped like a question mark, an angry face and a globe, headline in teal Inter Bold.

## Production Notes
- No facts to verify: the lesson uses a hypothetical example and a general scoring method with no tool-specific steps, figures or legal claims (content.md Review Flags: None).
- Not a screen demo lesson: Mateo's test sheet is shown as slides (scenes 11 to 13), not as a live recording.
- Mateo and the Córdoba fitness chain are fictional. Pronunciation: Córdoba (KOR-doh-bah). Stock footage must show no real gym brand names or logos.
- The full scoring table and the eight-point checklist are on the lesson page; scene 5 shows the scoring table and scene 7 shows the checklist as a slide for learners to pause on.
- Judgement call carried from curriculum: test questions are made up or rewritten without personal details.
