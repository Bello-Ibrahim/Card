# L07 Clean Code Habits | Presenter Script

Course: AI-11 · Video: 5 min · Words: 675

## Hook
Code is read far more often than it is written. Your teammates read it. Reviewers read it. And you read it again in three months' time. If you cannot understand your own code next month, it does not matter that it worked today.

## Explain
In the last lesson, we packaged logic into functions. Today, we make our code easy to read. Clean code is code that a person can read, check and change safely. Python has an official style guide called PEP eight. You don't need to learn all of it. A few habits cover most of what matters.

Habit one is clear names. A name like weekly orders says what the variable holds. A single letter like x does not. Use lowercase words joined by underscores, for variables and for functions. Avoid single letters, except in very short loops.

Habit two is short functions that do one job. If you need the word and to describe a function, it probably does two jobs, so split it. Habit three is comments that explain why, not what. A comment that repeats the code adds nothing. A comment that explains a decision helps the reader.

Habit four is docstrings. Add one line at the top of each function that says what it does and what it returns. Habit five is layout. Indent the same way every time, keep lines short, leave blank lines between parts, and put spaces around the equals sign.

Clean code is like a tidy shared kitchen. Knives go back in the same drawer, jars have labels, and the counter is cleared after cooking. Nobody wastes time searching, and nobody picks up salt thinking it is sugar. A messy kitchen still produces meals, but every cook is slower, and mistakes are more likely.

Improving the structure of code without changing what it does is called refactoring. The output before and after must be the same. So refactor in small steps, and run the code after each step. Then you know which change broke something.

## Demonstrate
Let's see a real example. Sipho volunteers for a food bank in Durban, South Africa. He wrote a quick script to find the average value of the week's donation orders. The numbers are made up.

Here is the first version. It stores four order values in a list called x, adds them up in a loop, divides by the number of orders, and prints one hundred and eleven point two five. It works. But what are x, t and a? A reader must trace every line to find out.

And here is the clean version. First, x became weekly orders, so the data explains itself. Second, the loop became the built-in sum function, which is shorter and harder to get wrong.

Third, the calculation moved into a function with a clear name and a docstring, so Sipho can reuse it for next week's orders. He ran the script after each change, and the output stayed the same, one hundred and eleven point two five.

A common mistake is thinking that clean code means many comments. Comments that repeat the code quickly become wrong when the code changes. First make the code explain itself with good names and small functions. Then comment only on the reasons behind decisions. A second mistake is changing the behaviour while you refactor. Keep the output identical, and compare it before and after.

## Recap
Let's recap. First, use clear, descriptive names in lowercase with underscores, and follow the main PEP eight layout rules. Second, keep functions short, give each one a single job, and add a one-line docstring. Third, refactor in small steps, and check that the output does not change.

## CTA
Now it is your turn. In the exercise below this video, you will refactor a messy twenty-line script about tour guide ratings. You will rename the variables, split it into two functions, and add docstrings, while keeping the output exactly the same. It takes about twenty-five minutes. In the next lesson, we look at errors and how to fix them. See you there.

## Thumbnail
Headline: Code Others Can Read
Image: Navy background, a messy code block on the left and a tidy one on the right with a teal tick, headline in teal Inter Bold.

## Production Notes
- Not a screen-demo lesson: the worked example uses before-and-after code slides only, as content.md specifies.
- [VERIFY] PEP 8 details (79-character line limit, 4-space indentation, two blank lines between top-level functions) should be checked against the current PEP 8 text. The voiceover only says 'keep lines short' and 'indent the same way every time' and does not state the numbers; the layout slide can show them only after the check.
- Sipho and the Durban food bank are fictional; all order values are made up. Both code slides must show the output 111.25, as in content.md.
- Code slides must show the before and after code from content.md exactly.
