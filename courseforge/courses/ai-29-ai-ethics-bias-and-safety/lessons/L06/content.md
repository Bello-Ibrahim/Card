# L06 Safety Risks and Human Oversight

Course: AI-29 · Module: M2 · Objectives: O3, O6 · Video: 5 min

## Hook
"A human is in the loop," the vendor says. But what if that human has 400 AI decisions to approve before lunch and no power to change any of them? Is that really human control?

## Explanation
In AI, **safety** means avoiding physical, financial, emotional or social harm. Four kinds of safety risk appear again and again:

1. **Harmful advice.** A tool gives wrong or dangerous guidance about health, money, law or relationships, for example a wrong medicine dose or a risky investment "tip".
2. **Unsafe instructions.** A tool explains how to do something dangerous, such as mixing chemicals or bypassing a safety system.
3. **Over-trust in automated decisions.** People accept the AI's answer without checking because it is fast, confident and usually right. When it is wrong, nobody notices.
4. **High-stakes use without checks.** AI is used in areas where a mistake can seriously hurt someone, such as health, education results, credit, hiring or public services, with no review step.

Many AI tools have safety filters, but filters are not perfect. The strongest protection is often **human oversight**.

Human oversight means that a person can question and change the AI's decision. For oversight to be real, not just a signature, the person needs three things:
- **Time:** enough time to look at each case properly.
- **Knowledge:** enough training to understand the task and to recognise when the AI is wrong.
- **Authority:** the power to change or stop the AI's decision, without being punished for it.

Where should a person review the output? A simple rule: **the higher the impact of a mistake, the closer the human review.** For low-impact tasks, such as suggesting a title for a blog post, occasional spot checks may be enough. For high-impact tasks, such as rejecting a loan or flagging a patient, a person should review before the decision takes effect, or people should have an easy way to appeal.

**Analogy:** An aeroplane autopilot is very useful. It flies smoothly for hours and reduces the pilot's workload. But the pilot is still trained, alert and able to take control at any moment, especially at take-off, landing and in bad weather. Human oversight of AI works the same way: the system does the routine work, and a capable person stays ready to step in when it matters most.

## Worked Example
Youssef Benali runs customer support for a hypothetical chain of pharmacies in Morocco. The company launches a chatbot on its website to answer questions about opening hours, stock and deliveries.

In the first month, Youssef reviews a sample of chats and finds three safety risks:
- A customer asks how many tablets of a pain medicine they can take in a day. The chatbot gives a number without asking about age, weight or other medicines. This is **harmful advice**.
- A customer asks whether two medicines can be taken together. The chatbot says "yes" with confidence. The answer is not checked by anyone. This is **high-stakes use without checks**.
- Staff start to copy the chatbot's answers into emails without reading them, because "it is usually right". This is **over-trust**.

Youssef decides where human oversight is needed:
- **Opening hours, stock and deliveries:** the chatbot answers alone, and staff review a weekly sample.
- **Any question about doses, side effects or combining medicines:** the chatbot does not answer. It says a pharmacist will reply, and passes the question to a pharmacist on duty. The pharmacist has time in their schedule for this, the training to answer, and the authority to contact the customer directly.
- **Staff emails:** a new rule says staff must read every AI-drafted reply before sending.

## Common Mistake
Many people believe that adding a person anywhere in the process solves the safety problem. But a person who has no time, no training or no power to change the result cannot provide real oversight. They only approve what the machine already decided. The correction: check that the reviewer has enough time, knowledge and authority, and place the review where the impact of a mistake is highest.

## Key Takeaways
1. Key AI safety risks include harmful advice, unsafe instructions, over-trust in automated decisions and high-stakes use without checks.
2. Human oversight is real only when the reviewer has enough time, knowledge and authority to question and change the AI's decision.
3. The higher the impact of a possible mistake, the closer and earlier the human review should be.

## Hands-on Exercise
**Task:** For 3 hypothetical uses of AI, decide where a human should review the output and explain why.
**Tools:** Pen and paper, or any notes app.
**Steps:**
1. Read the three hypothetical uses:
   a. A school in Egypt uses AI to grade students' essays for a final-year exam.
   b. A bank in India uses a chatbot to answer customer questions, including questions about blocked cards and suspicious payments.
   c. An app in Ghana helps farmers identify crop diseases from a photo and suggests a treatment.
2. For each use, list one or two things that could go wrong and who could be harmed.
3. Rate the impact of a mistake as low, medium or high.
4. Decide where a person should review the output: before the result is used, after it is used through spot checks, or through an easy appeal. Name who the person is, for example a teacher, a bank agent or an agricultural adviser.
5. For each reviewer, write one sentence on the time, knowledge and authority they need.
**What good looks like:** Each use has specific risks, an impact rating and a named reviewer. For example: essay grades are high impact, so a teacher reviews every grade before results are released, and students can appeal. Suspicious-payment questions pass to a trained bank agent. Crop-treatment advice is checked by an adviser when it involves chemicals. Your reasons link the review point to the impact of a mistake.
**Time:** about 15 minutes

## Review Flags
- None. The pharmacy chatbot and the three exercise uses are hypothetical on purpose, as the curriculum requires, and no real incidents or statistics are used.
