# L04 Making Decisions with if, elif and else | Presenter Script

Course: AI-11 · Video: 5 min · Words: 705

## Hook
A delivery app shows a different price for a short trip and a long one. Somewhere in its code, a program asked a question. Is the distance more than three kilometres? Today, you write that kind of question in Python.

## Explain
Last time, we stored many values in lists and dictionaries. Now we teach a program to choose. First, you need a condition. A condition is a question whose answer is either True or False.

You build conditions with comparison signs. Two equals signs mean equal to. Remember, one equals sign means store. There are also signs for not equal, less than, greater than, and so on. You can join conditions with and, or, and not.

Here is the structure. An if line, then any number of elif lines, which means else if, and finally an else line. Python checks the conditions from top to bottom. It runs only the block under the first condition that is true, and skips the rest. Else runs only if nothing else was true. You can have many elif lines, or none at all.

Two layout rules. Each of these lines ends with a colon. And the code that belongs to it is moved right by four spaces. In Python, this indentation is not just for looks. It decides which lines belong to which block. A wrong indent changes the meaning, or causes an error. Colab adds the indent for you after a colon.

Picture a security guard checking tickets at a stadium. The first question is, VIP ticket? If yes, you go through the VIP gate, and no more questions are asked. If not, the next question is, standard ticket? If no ticket matches, you are sent to the ticket office. Only one gate opens for each person.

## Demonstrate
Let's build one. Dewi makes a price calculator for a delivery app in Jakarta. The prices are made up. Up to three kilometres costs eight thousand rupiah. Up to ten kilometres costs fifteen thousand. Anything further costs twenty-five thousand.

In Colab, we set the distance to seven and a half kilometres. Then an if line for three or less, an elif line for ten or less, and an else line for anything further. Each one sets the price. Finally, we print the distance and the price.

Before we run it, let's trace it. Is seven and a half three or less? No, so we skip the first block. Is it ten or less? Yes, so the price becomes fifteen thousand, and else is skipped. Now run it. Seven point five kilometres costs fifteen thousand rupiah.

Notice that the elif line does not need to say more than three. If the distance were three or less, Python would already have stopped at the first block. The order does part of the work.

Next, Dewi adds a long-distance fee, but members don't pay it. The condition says the distance is more than five, and the customer is not a member. The distance part is true, but the member part is false. And needs both, so we see no extra fee.

Now you try. What happens if I change the distance to two? And to twelve? Pause the video, make your prediction, and then watch the result.

A common mistake is putting the conditions in the wrong order. If the ten kilometre check came first, a two kilometre trip would pay fifteen thousand, and the three kilometre band would never be used. Put the smallest range first. And never write one equals sign in a condition, because that causes a syntax error.

## Recap
Let's recap. First, conditions are True or False. You build them with comparison signs and join them with and, or, and not. Second, Python checks if and elif from top to bottom, and runs only the first block that is true. Third, the colon and the four-space indentation decide which lines belong to each block.

## CTA
Now it is your turn. In the exercise below this video, you will turn an exam score into a grade band, and predict the output for five test scores before you run the code. It takes about twenty minutes. In the next lesson, we learn how to repeat work with loops. See you there.

## Thumbnail
Headline: Teach Code to Decide
Image: Navy background, a road that splits into three lanes labelled 3 km, 10 km and further, headline in teal Inter Bold.

## Production Notes
- No facts to verify (content.md Review Flags: None). Dewi, the Jakarta delivery app, the price bands and the rupiah amounts are made up.
- Printed outputs on screen must match content.md exactly: '7.5 km costs 15000 rupiah' and 'No extra fee'.
- Verified with Python 3.11 on 2026-09-23: 2 km prints 8000 rupiah and 12 km prints 25000 rupiah.
- Trace scene: show the trace as an overlay (7.5 <= 3? No. 7.5 <= 10? Yes.) before running the cell.
