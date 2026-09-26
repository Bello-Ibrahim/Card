# L09 Rating and Prioritising Risks | Presenter Script

Course: AI-29 · Video: 5 min · Words: 685

## Hook
After a good audit, you may have a list of ten risks. You cannot fix all ten this week. So which two do you fix first, and how do you explain that choice to your manager?

## Explain
In the last lesson, you tested a tool with paired prompts. Now you need to decide what matters most. Not all risks are equal. A useful way to compare them is a risk matrix, which rates each risk on two scales. Likelihood asks how often this could happen. Impact asks how badly it could hurt someone. Each is rated low, medium or high.

Place each risk in a three by three grid. Risks in the top-right corner, high likelihood and high impact, are fixed first. And a high-impact risk usually deserves attention even when it is rare, because the harm is serious. Always ask who is harmed. A risk that falls mainly on one group is also a fairness problem.

Your ratings are judgements, not exact measurements. So write a short reason for each one, so others can understand and question it.

Then choose ways to reduce the risks. There are five common options. Better data, which includes the missing groups. Clear limits, which stop the tool from handling some tasks. Human review before outputs are used. User warnings about what the tool can and cannot do. And monitoring, because tools and uses change. Choose options the team can do in weeks, not only in an ideal world.

Think of a hospital emergency room deciding who to see first. A small cut that happens often is less urgent than a rare but serious chest pain. Staff treat the most urgent first. Nobody is ignored, but not everyone is seen at the same time.

## Demonstrate
Let's rate some real-looking risks. Dewi Lestari leads quality at a telecom company in Indonesia. Its customer-service chatbot answers questions about bills, data plans and network problems. Her team has tested it and found four risks.

Risk one. The chatbot gives wrong prices for data plans. That is high likelihood, medium impact. Risk two. Customers type their full ID number into the chat, and it is stored. That is medium likelihood, but high impact, because stored numbers could be misused.

Risk three. The chatbot understands regional languages less well, so those customers get weaker answers. That is high likelihood, medium impact, and also a fairness problem. Risk four. It tells a customer who reports a phone fire to restart the device. It was seen only once, but the impact is high, because it is a physical danger.

Dewi's team fixes two first. For the ID numbers, the chatbot warns customers not to share them, hides long number sequences, and the IT team checks what is stored. For the fire risk, a clear limit. Any message about fire, smoke or injury gets a fixed safety message and passes to a human agent.

Risks one and three are planned for next month, with better price data and weekly checks, more testing in regional languages, and a talk to a person button. Dewi records all four, so none is forgotten.

A common mistake is to fix the most frequent risk first, because it is the most visible. But a rare, high-impact risk can matter more. Always rate both scales. Another mistake is to choose unrealistic fixes, such as rebuild the model. Pick actions the team can take soon.

## Recap
Let's recap. First, a risk matrix rates each risk by likelihood and impact, and the highest combinations are fixed first. Second, serious, high-impact risks need attention even when they are rare, and risks that fall mainly on one group are also fairness problems. Third, realistic ways to reduce risk are better data, clear limits, human review, user warnings and monitoring.

## CTA
Now it is your turn. This exercise is step two of your capstone. List at least five risks for the tool you tested, place each one on the matrix, and pick your top three. It takes about thirty minutes. In the next and final lesson, we will write your audit and recommendations. See you there.

## Thumbnail
Headline: Which Risk First?
Image: Navy background, a three-by-three grid glowing from green in the bottom-left to red in the top-right, with a pin in the red corner, headline in teal Inter Bold.

## Production Notes
- No facts to verify: the telecom chatbot and its four risks are hypothetical on purpose, with no real companies, incidents or statistics (content.md Review Flags: None).
- Dewi Lestari and her telecom company in Indonesia are fictional; stock footage must not show a real operator name, logo or network brand.
- Scene 3 matrix must match the content.md grid exactly: top-right = highest priority, bottom-left = lowest priority.
- Risk ratings in scenes 8 and 9: Risk 1 wrong prices High/Medium; Risk 2 ID numbers stored Medium/High; Risk 3 regional languages High/Medium; Risk 4 phone fire Low/High.
