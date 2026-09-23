# L09 Rating and Prioritising Risks

Course: AI-29 · Module: M2 · Objectives: O6 · Video: 5 min

## Hook
After a good audit you may have a list of ten risks. You cannot fix all ten this week. So which two do you fix first, and how do you explain that choice to your manager?

## Explanation
Not all risks are equal. A useful way to compare them is a **risk matrix**, which rates each risk on two scales.

- **Likelihood:** how often could this happen? Rate it **low** (rare), **medium** (sometimes) or **high** (often or regularly).
- **Impact:** how badly could it hurt someone if it happens? Rate it **low** (small annoyance, easy to fix), **medium** (real cost, stress or delay) or **high** (serious harm to health, money, rights, safety or trust).

Place each risk in a 3-by-3 grid:

| | Low impact | Medium impact | High impact |
|---|---|---|---|
| **High likelihood** | Medium priority | High priority | Highest priority |
| **Medium likelihood** | Low priority | Medium priority | High priority |
| **Low likelihood** | Lowest priority | Low priority | Medium priority |

Risks in the top-right corner are fixed first. A high-impact risk usually deserves attention even if it is not very likely, because the harm is serious. Always ask **who** is harmed: a risk that falls mainly on one group, such as older customers or speakers of one language, is also a fairness problem.

Your ratings are judgements, not exact measurements. Write a short reason for each one, so others can understand and question it.

After you rate the risks, choose ways to reduce them. Five common options:
1. **Better data:** test with, or train on, examples that include the missing groups.
2. **Clear limits:** stop the tool from handling certain tasks, such as medical or legal advice.
3. **Human review:** a capable person checks outputs before they are used (L06).
4. **User warnings:** tell users what the tool can and cannot do, and when to check with a person.
5. **Monitoring:** test and review samples regularly, because tools and uses change.

Choose options that are **realistic** for the team: something it can do in weeks, not only in an ideal world.

**Analogy:** A risk matrix is like a hospital emergency room deciding who to see first. A small cut that happens often is less urgent than a rare but serious chest pain. Staff look at how serious each case is and how quickly it could get worse, and they treat the most urgent first. Nobody is ignored, but not everyone is seen at the same time.

## Worked Example
Dewi Lestari leads quality for a hypothetical telecom company in Indonesia. The company's customer-service chatbot answers questions about bills, data plans and network problems. Dewi's team has tested it and found four risks. They rate each one:

| Risk | Likelihood | Impact | Reason |
|---|---|---|---|
| 1. The chatbot gives wrong prices for data plans | High | Medium | Tests found wrong prices in several answers; customers may pay more than expected. |
| 2. Customers type their full ID number into the chat, and it is stored | Medium | High | The chat invites "account details"; stored ID numbers could be misused. |
| 3. The chatbot understands questions in regional languages less well and gives unhelpful answers | High | Medium | Paired tests in Bahasa Indonesia and a regional language showed weaker answers; those customers may give up. |
| 4. The chatbot tells a customer who reports a phone fire to "restart the device" | Low | High | Seen once in testing; physical danger if followed. |

Dewi's team picks two to fix first:
- **Risk 2 (privacy):** high impact and it happens regularly. **Action:** the chatbot warns customers not to share ID numbers and hides long number sequences; the IT team checks what is stored.
- **Risk 4 (safety):** rare but very serious. **Action:** a clear limit: any message about fire, smoke or injury gets a fixed safety message and passes to a human agent.

Risks 1 and 3 are planned for next month: better price data with weekly checks, and more testing with regional-language examples plus a "talk to a person" button. Dewi records all four, so none is forgotten.

## Common Mistake
Many people fix the most frequent risk first, because it is the most visible. But a frequent, low-impact problem can matter less than a rare, high-impact one. The correction: always rate both likelihood and impact, and give extra weight to risks that could cause serious harm or fall mainly on one group. Another mistake is to choose unrealistic fixes, such as "rebuild the model". Pick actions the team can actually take soon.

## Key Takeaways
1. A risk matrix rates each risk by likelihood (how often) and impact (how badly), and the highest combinations are fixed first.
2. Serious, high-impact risks need attention even when they are rare, and risks that fall mainly on one group are also fairness problems.
3. Common, realistic ways to reduce risk are better data, clear limits, human review, user warnings and monitoring.

## Hands-on Exercise
**Task:** Capstone step 2: list at least 5 bias, misinformation, privacy or safety risks for the tool you tested, place each one on a likelihood-and-impact matrix, and pick your top 3.
**Tools:** Your L08 test table; a spreadsheet, notes app or paper.
**Steps:**
1. Review your L08 results and your L04 to L06 notes. List at least 5 risks for your chosen tool, covering at least 3 of the four types: bias, misinformation, privacy and safety.
2. Describe each risk in one sentence: what could happen, and to whom.
3. Rate each risk's likelihood and impact as low, medium or high, with a one-line reason. Link to your test evidence where you have it.
4. Place each risk in the 3-by-3 matrix.
5. Choose your top 3 risks and, for each one, suggest one realistic way to reduce it from the five options.
**What good looks like:** At least 5 clearly described risks across at least 3 types, each with ratings and a reason, a completed matrix, and a top 3 that is explained, including why any high-impact risk was or was not chosen. Keep this work for L10.
**Time:** about 30 minutes

## Review Flags
- None. The telecom chatbot and its risks are hypothetical on purpose, as the curriculum requires, and no real companies, incidents or statistics are used.
