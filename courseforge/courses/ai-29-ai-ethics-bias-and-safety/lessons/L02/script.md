# L02 How Bias Gets into AI | Presenter Script

Course: AI-29 · Video: 5 min · Words: 687

## Hook
Nobody sits down and writes treat women worse, or ignore rural customers, into an AI system. Yet biased systems appear again and again. If nobody plans the bias, where does it come from?

## Explain
In the last lesson, you met bias. Results that are better or worse for some groups. Bias rarely comes from one bad decision. It usually enters quietly, at one or more of three points. The data, the design, and the use.

First, the data. An AI system learns patterns from examples. If the examples are unbalanced, the patterns will be too. Some groups may be missing, like darker skin in a skin-condition app. Some may be over-represented, like city speakers in a speech tool. And if past decisions were unfair, the data records that unfairness as if it were correct.

Second, the design. People decide what the system should predict, and which details it may use. A tool that predicts who will cost the most is not the same as one that predicts who needs the most care. And even if the system never sees gender, details like a postcode or a gap in employment can stand in for it. We call these proxies.

Third, the use. A system can be fair in one place and unfair in another. It may be used for a different purpose, or in a group it was never tested on. And people may trust it too much and stop checking.

Here is a simple picture. A recipe copied from an old cookbook repeats its mistakes, however carefully you cook. If the cookbook used too much salt, your dish will be too salty, even if you measure perfectly. Careful training cannot fix mistakes that were already in the recipe.

## Demonstrate
Let's follow one example. Claire Tremblay leads recruitment at an engineering company in Canada. To save time, the company builds a CV-screening tool, trained on ten years of past hires. CVs of people who were hired are labelled good, and all the others are labelled not selected. It sounds sensible. Let's see what happens.

Now watch the three points. The data: most engineers hired in those ten years were men from three local universities, so the tool learns that CVs like theirs are good. The design: the team asked it to predict people like our past hires, not people who will do the job well. It also reads hobbies and clubs, which can act as proxies.

The use: recruiters start to trust the tool's top twenty list and stop reading the other CVs. Qualified people from other universities, and many women, are never seen by a person. Nobody wanted this. But the tool now repeats old hiring patterns at high speed.

Claire's team makes three changes. They check which groups are in the training data. They change the goal to match the skills in the job description. And a person reviews a sample of rejected CVs every week.

A common mistake is to think that removing names, gender or age makes a system fair. Other details can still act as proxies, A women's sports club, a school for girls, or a career gap for childcare can all carry the same pattern. So removing details can be one step, but you still need to test results for different groups, as you will learn later in this course.

## Recap
Let's recap. First, bias can enter through the data, the design and the use. Second, data that records past decisions can also record past unfairness, and the system learns it as if it were correct. Third, removing names or gender is not enough, because other details can act as proxies. Results must be tested. Keep these three points in mind whenever you meet a new AI tool.

## CTA
Now it is your turn. In the exercise below this video, you will look at a loan-approval model at a bank in Kenya, and list one way bias could enter through the data, the design and the use. It takes about fifteen minutes. In the next lesson, we will look at fairness, and who gets helped and who gets hurt. See you there.

## Thumbnail
Headline: Where Does Bias Start?
Image: Navy background, three glowing doorways labelled by icons (a database, a blueprint, a hand) with a thin red thread running through them, headline in teal Inter Bold.

## Production Notes
- No facts to verify: the CV-screening and loan examples are hypothetical on purpose, with no real companies, incidents or statistics (content.md Review Flags: None).
- Claire Tremblay and her engineering company in Canada are fictional; stock footage must not show a real company name or logo, and CVs on screen must use invented placeholder details only.
