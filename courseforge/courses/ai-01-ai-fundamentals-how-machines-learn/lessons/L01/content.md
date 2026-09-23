# L01 What Is AI, Really?

Course: AI-01 · Module: M1 · Objectives: O1 · Video: 5 min

## Hook
Your phone unlocks when it sees your face. Your email moves some messages to spam before you read them. Nobody wrote a rule for your face or for every spam message ever sent. So how does the phone know? This lesson answers that question.

## Explanation
Artificial intelligence (AI) is a broad name for computer systems that do tasks we usually connect with human intelligence. Examples include recognising faces, understanding speech, translating text and making recommendations.

There are two main ways to make a computer do a task.

The first way is **rules**. A person writes exact instructions: "If the message contains the word 'lottery' and comes from an unknown sender, move it to spam." Rules work well when the task is simple and stable. They break down when the task has too many cases for a person to describe.

The second way is **learning from examples**. Instead of writing the rules, we show the computer many examples, such as thousands of emails that people have already marked as "spam" or "not spam". The computer finds patterns in those examples and uses them to decide about new emails. This approach is called **machine learning**.

**Analogy:** Think of two ways to learn a new city. You can follow a printed list of directions: turn left, then right, then straight for 200 metres. That works until a road is closed. Or you can walk around the city for weeks until you recognise the streets and find your own way. Rules are the printed list. Machine learning is learning the city by experience.

Four terms are often mixed up. They fit inside each other like circles:

- **Artificial intelligence** is the largest circle: any system that performs "intelligent" tasks, whether it uses rules or learning.
- **Machine learning** is a circle inside AI: systems that learn patterns from data.
- **Deep learning** is a circle inside machine learning: systems that use large "neural networks" with many layers. You will meet these in L07.
- **Generative AI** is inside deep learning: systems that create new text, images or sound, such as chatbots. You will meet these in L09.

## Worked Example
Amina runs a small online shop in Nairobi that sells handmade baskets. Customers send her messages every day, and she wants them sorted automatically into "order question", "delivery problem" and "other".

First she tries rules: "If the message contains 'where is my', label it 'delivery problem'." It works for some messages. But customers write in many different ways, such as "still waiting for my parcel", "has it shipped?" or "the courier never came". Amina keeps adding rules, and the list grows longer and still misses messages.

Then she tries a machine learning tool. She labels 300 old messages by hand and gives them to the tool as examples. The tool learns which words and phrases usually appear in each group. It now labels most new messages correctly, including phrasings Amina never thought to write a rule for.

The same tool would not be useful for calculating delivery fees. Those follow a fixed price table, so a simple rule is clearer, cheaper and always correct.

## Common Mistake
Many people believe that "AI" means a thinking machine that understands the world the way a person does. Today's AI systems do not understand in that way. A system that labels Amina's messages has learned patterns in words. It does not know what a basket or a courier is. This matters because a system that only finds patterns can be confidently wrong when it meets something unlike its examples.

## Key Takeaways
1. AI is a broad term for systems that perform tasks we link with human intelligence. It can be built with hand-written rules or by learning from examples.
2. Machine learning means the computer finds patterns in many examples instead of following rules a person wrote.
3. AI, machine learning, deep learning and generative AI fit inside each other like circles, from the broadest to the most specific.

## Hands-on Exercise
**Task:** Sort 8 everyday systems into "follows fixed rules" or "learns from examples".
**Tools:** Pen and paper, or any notes app. Optional: ChatGPT or Claude (free tier) to compare your answers.
**Steps:**
1. Look at this list: a calculator; an email spam filter; a traffic light on a timer; a music app that suggests songs; a lift (elevator) that stops at the floor you press; a phone keyboard that suggests your next word; a vending machine; a photo app that groups pictures of the same person.
2. For each item, write "rules" or "learns from examples" and one sentence explaining why.
3. Compare your answers with the answer key on the course page.
4. Optional: ask a free AI chatbot to sort the same list, and note any answer where it disagrees with you.
**What good looks like:** Items that deal with variety and change (spam, songs, next-word suggestions, faces) are labelled "learns from examples". Each label has a short reason, such as "no person could write a rule for every face".
**Time:** about 15 minutes

## Review Flags
- None. The examples are general and hypothetical, and no specific facts need checking.
