# L07 Neural Networks Without the Maths

Course: AI-01 · Module: M2 · Objectives: O1, O2 · Video: 5 min

## Hook
You have probably heard that modern AI uses "neural networks" and "deep learning". These words sound difficult, but the main idea is something you have already done: turning a dial a little, checking the result, and turning it again until it sounds right.

## Explanation
In L01 you saw that deep learning is a circle inside machine learning. In L04 you learned that training is the stage where a model learns from examples. A **neural network** is one popular way to build that model.

Picture a neural network as a machine with many small **dials**. Each dial controls how much one piece of information matters. The technical name for these dials is **weights**.

The dials are arranged in **layers**:
- The **input layer** receives the features, for example the colours and shapes in a photo.
- One or more **hidden layers** in the middle combine those features into more useful patterns, such as "round edge" or "dark spot".
- The **output layer** gives the prediction, such as "cat" or "not cat".

At the start of training, the dials are set at random, so the network's predictions are poor. Training then repeats the same simple cycle many times:
1. Show the network an example.
2. Let it make a prediction.
3. Compare the prediction with the correct label.
4. Nudge every dial a tiny amount in the direction that would have made the mistake smaller.

One nudge changes very little. But after thousands or millions of examples, the dials settle into positions that give good predictions. That is what "learning" means for a neural network: not understanding, but a very long series of small adjustments that reduce mistakes.

Why is it called **deep** learning? Because a network with many hidden layers is called "deep". Each layer builds on the one before it. In a network that recognises photos, early layers might react to simple edges, middle layers to shapes such as eyes or wheels, and later layers to whole objects. More layers allow the network to learn more complex patterns, but they also need more data and more computing power.

**Analogy:** Think of a sound engineer at a concert with a large mixing desk full of sliders for bass, voice, drums and more. At first the sound is poor. The engineer listens, moves a few sliders a little, and listens again. Nobody gives them the perfect settings. They get there by repeated small corrections. A neural network does the same, except it has far more sliders, and the "listening" is the comparison with the correct label.

The word "neural" comes from a loose comparison with brain cells, called neurons. A neural network does not work like a real brain. The name is historical, not a description of how it thinks.

## Worked Example
Kwame works for a cocoa farmers' cooperative in Ghana. The cooperative wants to check photos of cocoa beans and sort them into "good" and "mouldy" before selling them.

The team collects several thousand photos, and experienced sorters label each one. They use these labelled photos to train a neural network. At the beginning, the network labels beans almost at random. For each photo, it makes a guess, the guess is compared with the sorter's label, and all the dials are nudged slightly.

After many rounds, the early layers react to small details such as colour spots and fuzzy textures. The middle layers combine these into patterns like "white patch on a dark surface". The output layer uses those patterns to say "mouldy" or "good".

Kwame never wrote a rule such as "white patches mean mould". The dials found that pattern on their own because it helped reduce mistakes. This also means Kwame cannot easily read the dials to see exactly why a bean was rejected. There are too many of them, and each one is only a small part of the decision.

## Common Mistake
Many people think a neural network stores a copy of every training photo and looks up the closest match. It does not. After training, the photos are not needed. What remains is only the final positions of the dials. This is why a network can handle a photo it has never seen, and also why it can make strange mistakes: it has learned patterns in the dial settings, not a list of facts.

## Key Takeaways
1. A neural network is made of layers of adjustable dials, called weights, that decide how much each piece of information matters.
2. Training means showing examples, checking the mistakes and nudging the dials a little, repeated many times.
3. "Deep" learning means the network has many layers, which lets it learn more complex patterns but needs more data and computing power.

## Hands-on Exercise
**Task:** Play a guess-and-adjust game: tune two sliders on a worksheet to hit a secret target, then write down how this resembles training.
**Tools:** The worksheet below, a pen, and one "checker". The checker can be a friend or family member, or ChatGPT or Claude (free tier).
**Steps:**
1. Copy this worksheet onto paper or into a notes app:

   | Round | Slider A (0–10) | Slider B (0–10) | Feedback for A | Feedback for B | What I changed and why |
   |---|---|---|---|---|---|
   | 1 | 5 | 5 | | | |
   | 2 | | | | | |
   | 3 | | | | | |
   | 4 | | | | | |
   | 5 | | | | | |
   | 6 | | | | | |
   | 7 | | | | | |
   | 8 | | | | | |

2. Set up the checker. If you use a friend, ask them to write two secret whole numbers from 0 to 10 on a hidden piece of paper, one for Slider A and one for Slider B. If you use a chatbot, send this message: "Let's play a game. Secretly choose two whole numbers from 0 to 10, called Slider A and Slider B. Do not tell me. Each time I guess both, reply only with 'higher', 'lower' or 'correct' for each slider. When I get both correct, tell me the numbers." [VERIFY]
3. Start with both sliders at 5. Tell the checker your guess and write the feedback in the table.
4. Change your sliders using the feedback. Try moving by big steps at first, then small steps when you are close. Write why you changed each slider.
5. Continue until both sliders are correct, or until round 8.
6. Below the table, write three sentences that answer: What were the "dials"? What told you how wrong you were? Why did you need several rounds instead of one?
**What good looks like:** The table shows the guesses moving closer to the target round by round, with a short reason for each change. The three sentences connect the game to training: the sliders are like weights, the feedback is like comparing a prediction with the correct label, and the rounds are like repeated small adjustments. A strong answer also notes that a real network has thousands or millions of dials, not two.
**Time:** about 15 minutes

## Review Flags
- [VERIFY] Step 2: check that the free tiers of ChatGPT and Claude play this game consistently and keep the same secret numbers across turns. If they do not, make the friend or family member version the main option.
