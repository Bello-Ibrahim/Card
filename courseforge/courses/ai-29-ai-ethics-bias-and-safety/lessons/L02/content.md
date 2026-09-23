# L02 How Bias Gets into AI

Course: AI-29 · Module: M1 · Objectives: O1, O2 · Video: 5 min

## Hook
Nobody sits down and writes "treat women worse" or "ignore rural customers" into an AI system. Yet biased systems appear again and again. If nobody plans the bias, where does it come from?

## Explanation
In L01 you met **bias**: results that are systematically better or worse for some groups. Bias rarely comes from one bad decision. It usually enters quietly, at one or more of three points.

**1. The data.** An AI system learns patterns from examples. If the examples are unbalanced, the patterns will be too. Some common data problems:
- **Missing groups:** a skin-condition app trained mostly on photos of light skin may perform badly on darker skin.
- **Over-represented groups:** a speech tool trained mostly on city speakers may struggle with rural accents.
- **Past unfairness in the records:** if past decisions were unfair, the data records that unfairness as if it were "correct".

**2. The design.** People decide what the system should predict and which information it may use. These choices matter.
- **The target:** a tool told to predict "who will cost the most" is not the same as a tool told to predict "who needs the most care". Poorer patients may cost less because they get less care, not because they are healthier.
- **Proxies:** even if a system does not see gender or ethnicity, other details, such as a postcode, a school name or a gap in employment, can stand in for them.

**3. The use.** A system can be fair in one place and unfair in another.
- It may be used for a different purpose than it was built for.
- It may be used in a country or group it was never tested on.
- People may trust its output too much and stop checking.

**Analogy:** A recipe copied from an old cookbook repeats its mistakes, however carefully you cook. If the cookbook used too much salt, your dish will be too salty, even if you measure perfectly. An AI system trained on old data is the same: careful training cannot fix the mistakes that were already in the recipe.

## Worked Example
Claire Tremblay leads recruitment at a hypothetical engineering company in Canada. The company wants to save time, so it builds a CV-screening tool. The tool is trained on ten years of past hires: CVs of people who were hired are labelled "good", and the others are labelled "not selected".

Here is how bias enters at each point:

- **Data:** in the past ten years, most engineers hired were men from three local universities. The tool learns that CVs like theirs are "good".
- **Design:** the team asked the tool to predict "people like our past hires", not "people who will do the job well". These are different questions. The tool also reads hobbies and clubs, which can act as proxies for gender or background.
- **Use:** recruiters start to trust the tool's top-20 list and stop reading the other CVs. Qualified applicants from other universities, and many women, are never seen by a person.

Nobody in the team wanted this result. But the tool now repeats the company's past hiring patterns at high speed.

Claire's team makes three changes. They check which groups are in the training data. They change the goal to match skills listed in the job description. And they require a person to review a sample of rejected CVs every week.

## Common Mistake
Many people think that removing sensitive details, such as name, gender or age, makes a system fair. It often does not. Other details can act as proxies: a women's sports club, a school for girls, a postcode in a certain area or a career gap for childcare. The system can still learn the same pattern through these clues. Removing sensitive details can be one step, but you still need to test the results for different groups, as you will learn in L03 and L08.

## Key Takeaways
1. Bias can enter an AI system through the data (who is missing or over-represented), the design (what it predicts and which details it uses) and the use (who applies it, where and how).
2. Data that records past decisions can also record past unfairness, and the system learns it as if it were correct.
3. Removing names or gender is not enough, because other details can act as proxies. Results must be tested.

## Hands-on Exercise
**Task:** For a hypothetical loan-approval model at a bank in Kenya, list one way bias could enter through the data, one through the design and one through the use.
**Tools:** Pen and paper, or any notes app.
**Steps:**
1. Read the scenario: a hypothetical bank in Kenya builds a model to approve small business loans. It is trained on the bank's past loan records. Most past loans went to applicants in large cities who had formal bank accounts.
2. Write one way bias could enter through the **data**. Think about who is missing or over-represented.
3. Write one way bias could enter through the **design**. Think about what the model predicts and which details it uses. Could any detail act as a proxy?
4. Write one way bias could enter through the **use**. Think about who uses the model, where, and how much they trust it.
5. For each point, add one sentence on who could be harmed.
**What good looks like:** Three specific points, one for each stage, for example: data, few rural or informal-sector borrowers in the records; design, using "has a formal bank account" as a strong factor, which may act as a proxy for location or income; use, loan officers in rural branches accepting every rejection without review. Each point names a group that could be harmed.
**Time:** about 15 minutes

## Review Flags
- None. The CV-screening and loan examples are hypothetical on purpose, as the curriculum requires, and no real companies, incidents or statistics are used.
