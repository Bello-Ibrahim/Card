# L09 Build Your Support Assistant

Course: AI-26 · Module: M3 · Objectives: O3, O6 · Video: 5 min (screen demo)

## Hook
You have a clean knowledge base, a tone guide and hand-off rules. This week you combine them into a working support assistant. A good first version is not clever. It is small and honest.

## Explanation
You will use **a free chatbot builder of your choice** [VERSION]. Interfaces differ, so this lesson describes the four decisions that every builder asks you to make.

**1. Scope.** Decide which topics the assistant covers. Choose 3 to 5 frequent, low-risk topics from your L01 list, for example opening hours, order tracking and returns. Everything else is out of scope and goes to a person.

**2. Knowledge.** Add the articles you wrote in L03, or similar clean articles for your made-up company. Most builders let you paste text, upload a document or add a web page [VERSION]. Add only content for your scope, and never upload real customer data or confidential documents to a free tool.

**3. Instructions.** Most builders have a box for instructions, sometimes called a "system prompt", "persona" or "behaviour" [VERSION]. Write clear, short rules, for example:

- "You are the support assistant for Kestrel Bikes. Answer only questions about opening hours, repair bookings and express repairs."
- "Use only the information in the knowledge base. If the answer is not there, say you are not sure and offer to connect the customer with a person."
- "Follow this tone guide: [your 5 lines from L04]."
- "Never promise refunds, discounts or dates that are not in the knowledge base."
- "If the customer asks for a person, is very upset, or mentions a legal or safety issue, offer a person at once."

**4. Transparency.** Tell customers they are talking to AI. Put it in the welcome message, for example: "Hi, I am Kestrel's AI assistant. I can help with opening hours and repairs. You can ask for a person at any time." It builds trust, and in some regions the law requires it, for example under the EU AI Act transparency rules [REGION] [VERIFY]. You will look at this again in L12.

**Analogy:** Opening a support assistant is like opening a small food stall before a full restaurant. You serve a few dishes you can make well, you tell people clearly what is on the menu, and you point them to the restaurant next door for anything else.

## Worked Example
Leila works at a hypothetical language school in Amman, Jordan. She builds an assistant for three topics: course start dates, choosing a level, and payment methods.

The presenter follows these steps on screen. Names of buttons and menus depend on the builder chosen [VERSION].

1. Sign up for the free plan of the chosen chatbot builder and create a new assistant (often called a "bot", "agent" or "assistant") [VERSION].
2. Name it "Noor – Language school assistant (test)".
3. Open the knowledge or content section and add three short articles: "When do courses start?", "How do I choose my level?", "How can I pay?". Paste the text rather than uploading large files.
4. Open the instructions section and paste the scope, knowledge-only rule, tone guide and hand-off rules.
5. Write the welcome message: "Hello, I am Noor, the school's AI assistant. I can help with course dates, levels and payment. You can ask for a person at any time."
6. Open the preview or test chat. Ask one question for each topic and check each answer against the articles.
7. Ask one out-of-scope question, such as "Can you help with my visa?", and check that Noor says it is not sure and offers a person.
8. Ask in Arabic: "متى تبدأ الدورة القادمة؟" (When does the next course start?) and check the answer and the tone.
9. Save or publish the assistant in test mode only, and note its share link for testing.

In testing, Noor gives general visa advice. Leila adds the instruction "Do not give advice on visas or legal matters; offer a person", and the retest passes.

## Common Mistake
Many beginners add every document they have to the assistant, hoping it will answer everything. Old or overlapping content gives it more chances to find the wrong text. Keep the first version small, test it well, and add new topics only when the current ones work.

## Key Takeaways
1. Every chatbot builder asks you to decide four things: scope, knowledge, instructions and transparency.
2. Start with 3 to 5 frequent, low-risk topics and clean, made-up or approved content.
3. Tell customers they are talking to AI and that they can ask for a person at any time.

## Hands-on Exercise
**Task:** Capstone step 1: build a support assistant in a free chatbot builder that answers questions on at least 3 topics from your knowledge base.
**Tools:** A free chatbot builder of your choice [VERSION]; your articles from L03 and tone guide from L04.
**Steps:**
1. Choose a made-up company (or keep the one from earlier lessons) and 3 to 5 topics.
2. Write or reuse one short, clean article for each topic.
3. Create a new assistant in the chatbot builder's free plan.
4. Add the articles to its knowledge section.
5. Write instructions covering scope, "knowledge only", tone and hand-off offers.
6. Write a welcome message that says it is an AI assistant and that the customer can ask for a person.
7. Test one question per topic in the preview, plus one out-of-scope question.
8. Fix at least one problem and test again. Take screenshots of the setup and the test chat.
**What good looks like:** An assistant in test mode that answers at least 3 topics correctly, says it is AI, and offers a person for out-of-scope questions, using no real customer data.
**Time:** about 45 minutes

## Review Flags
- [VERSION] The brief names no chatbot builder: a reviewer must choose one or two with a usable free tier, then check its section names and upload options before recording.
- [VERSION] Free-plan limits of the chosen builder (number of assistants, messages, knowledge size) and its data-use terms.
- [REGION] [VERIFY] Rules requiring customers to be told they are talking to AI, for example the EU AI Act transparency obligations, and local data protection laws; the lesson treats disclosure as a principle and does not state legal detail.
- Reviewer check: a native speaker should check the Arabic sample question.
