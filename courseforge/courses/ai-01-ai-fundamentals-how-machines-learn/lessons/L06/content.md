# L06 Unsupervised and Reinforcement Learning

Course: AI-01 · Module: M2 · Objectives: O3 · Video: 5 min

## Hook
Imagine you are given 10,000 customer records and nobody tells you what to look for. There is no answer key. Can a computer still learn something useful? It can, and it can also learn to play a game it was never taught, simply by trying again and again.

## Explanation
In L05 you met supervised learning, where every example comes with a label. Labels are useful, but they cost time and money, because a person usually has to add them. Sometimes there are no labels at all. Sometimes there is no single correct answer to label. For these situations there are two other types of machine learning.

**Unsupervised learning** works with data that has no labels. The model looks for patterns on its own, most often by putting similar items into groups. This is called **clustering**. For example, a shop can give a model its customers' shopping habits, and the model may find groups such as "weekend family shoppers", "late-night snack buyers" and "people who only buy during sales". Nobody told the model these groups existed. It found them because the customers in each group behave in similar ways. A person must still look at each group and decide what it means and whether it is useful.

**Reinforcement learning** works through trial and error. A program, called an **agent**, takes actions in an environment. After each action, or after a series of actions, it receives a **reward** (a signal that the result was good) or a penalty (a signal that it was bad). Over many attempts, the agent learns which actions lead to more reward. Game-playing agents are the best-known example. An agent that plays a board game or a video game may start by making random moves. It loses many games, but slowly it learns which moves tend to lead to a win, and it can become very strong.

**Analogy:** Think of three ways to learn about food in a new country. In the first, a local friend tells you the name of every dish you taste. That is supervised learning, because you have labels. In the second, you visit the market alone and sort the dishes into groups: sweet, spicy, fried, soups. Nobody names them for you. That is unsupervised learning. In the third, you order a different dish each day and notice which ones make you happy. Over time you order the good ones more often. That is reinforcement learning, because you learn from rewards.

How do you choose between the three types? Ask these questions:
- Do I have examples with the correct answer? Use **supervised learning**.
- Do I have data but no answers, and I want to discover groups or patterns? Use **unsupervised learning**.
- Is there a series of decisions, where success is only clear after acting? Use **reinforcement learning**.

## Worked Example
Leila runs a chain of three clothing shops in Casablanca, Morocco. She wants to send better offers to her customers, but she does not know what types of customers she has.

She gives a model two years of anonymous sales records: what people bought, when, how often and how much they spent. There are no labels. The model finds four clusters. When Leila studies them, she recognises one group that buys school uniforms every August and another that buys only formal wear before weddings and holidays. She names the groups herself and creates a different offer for each. This is **unsupervised learning**.

Now consider a different business. A warehouse company in Poland wants a robot to find the fastest way to move boxes between shelves. There is no list of correct routes to learn from. Instead, the robot tries routes in a computer simulation. It gets a reward when a box arrives quickly and a penalty when it bumps into a shelf or takes too long. After many thousands of attempts, it learns efficient routes. This is **reinforcement learning**.

If Leila later wanted to predict whether a single customer will return next month, and she had past records labelled "returned" or "did not return", she would use **supervised learning**.

## Common Mistake
Many people believe unsupervised learning means the computer "understands" the groups it finds. It does not. The model only notices that some items are similar in the data. It cannot tell you that one group is "wedding shoppers". A person must interpret each group, and some groups will turn out to be meaningless. Another common mistake is to think reinforcement learning is the best choice for every task because it sounds powerful. It usually needs a very large number of attempts, so it is often trained in a simulation first.

## Key Takeaways
1. Unsupervised learning finds groups or patterns in data that has no labels, and a person must decide what those groups mean.
2. Reinforcement learning learns through trial and error, by trying actions and receiving rewards or penalties.
3. Choose the type by asking what you have: labelled answers (supervised), data without answers (unsupervised), or a series of decisions with a reward (reinforcement).

## Hands-on Exercise
**Task:** Match 6 scenarios to supervised, unsupervised or reinforcement learning, and justify one choice in a sentence.
**Tools:** Pen and paper, or any notes app. Optional: ChatGPT or Claude (free tier) to compare your answers.
**Steps:**
1. Read these 6 scenarios:
   1. A bank uses thousands of past loans marked "repaid" or "not repaid" to judge new applications.
   2. A music app groups millions of songs by how they sound, with no genre names given.
   3. A program learns to play a card game by playing against itself and winning or losing.
   4. A hospital uses X-ray images labelled "fracture" or "no fracture" to help check new X-rays.
   5. An online shop finds groups of products that customers often buy together, without any labels.
   6. A heating system in an office tries different settings and is rewarded when people are comfortable and energy use is low.
2. Write "supervised", "unsupervised" or "reinforcement" next to each scenario.
3. Choose one scenario and write one sentence that explains your choice, using the words "labels", "groups" or "reward".
4. Optional: ask a free AI chatbot to match the same scenarios, and compare its reasons with yours.
**What good looks like:** Scenarios 1 and 4 are supervised, 2 and 5 are unsupervised, and 3 and 6 are reinforcement. The justification names the key clue, for example: "Scenario 6 is reinforcement learning because the system learns from a reward after trying different settings, not from labels."
**Time:** about 15 minutes

## Review Flags
- None. The game-playing agents, shops and warehouse are described generically and hypothetically, and no specific systems or facts need checking.
