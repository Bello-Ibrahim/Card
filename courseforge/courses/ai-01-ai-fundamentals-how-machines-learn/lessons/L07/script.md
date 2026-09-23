# L07 Neural Networks Without the Maths | Presenter Script

Course: AI-01 · Video: 5 min · Words: 686

## Hook
You have probably heard that modern AI uses neural networks and deep learning. These words sound difficult. But the main idea is something you have already done. Turn a dial a little, check the result, and turn it again.

## Explain
In lesson four, you learned what training is. Today we look inside one popular kind of model, the neural network. And there is no maths, I promise.

Picture a neural network as a machine with many small dials. Each dial controls how much one piece of information matters. The technical name for these dials is weights.

The dials are arranged in layers. The input layer receives the features, like the colours and shapes in a photo. Hidden layers in the middle combine them into more useful patterns, such as a round edge or a dark spot. And the output layer gives the prediction, such as cat or not cat.

At the start of training, the dials are set at random, so the predictions are poor. Then training repeats one simple cycle. Show the network an example. Let it make a prediction. Compare the prediction with the correct label. Then nudge every dial a tiny amount, in the direction that would make the mistake smaller.

One nudge changes very little. But after many thousands of examples, the dials settle into good positions. That is what learning means here. Not understanding, but many small adjustments that reduce mistakes.

Think of a sound engineer at a concert, with a mixing desk full of sliders. She listens, moves a few sliders a little, and listens again. A neural network does the same, but it has far more sliders, and the listening is the comparison with the correct label.

A network with many hidden layers is called deep. That is where deep learning gets its name. In a photo network, early layers might react to edges, middle layers to shapes, and later layers to whole objects. More layers can learn more complex patterns, but they need more data and computing power.

## Demonstrate
Let's see this at work. Kwame works for a cocoa farmers' cooperative in Ghana. The cooperative wants to check photos of cocoa beans, and sort them into good and mouldy before selling them.

Experienced sorters label several thousand photos, and the team trains a neural network. At first, it labels beans almost at random. For each photo, its guess is compared with the sorter's label, and all the dials are nudged slightly.

After many rounds, early layers react to colour spots and fuzzy textures. Middle layers combine these into patterns, like a white patch on a dark surface. And the output layer says mouldy, or good.

Kwame never wrote a rule that says white patches mean mould. The dials found that pattern, because it reduced mistakes. But this also means Kwame cannot easily read the dials to see why a bean was rejected. There are too many, and each one is only a small part of the decision.

In this lesson's exercise, you will feel this for yourself. The worksheet has two sliders, A and B, each from zero to ten. You start both at five. A checker tells you higher or lower, and you adjust, round by round.

One last point. A neural network does not store a copy of every training photo. After training, only the final positions of the dials remain. That is why it can handle a new photo, and also why it can make strange mistakes.

## Recap
Let's recap. First, a neural network is made of layers of adjustable dials, called weights. Second, training means showing examples, checking the mistakes, and nudging the dials a little, again and again. Third, deep learning means many layers, which can learn more complex patterns, but need more data and computing power.

## CTA
Now it is your turn. Play the guess and adjust game on the worksheet below this video, with a friend, or a chatbot, as your checker. Then write three sentences on how the game is like training. In the next lesson, we find out how to check a model, with Testing a Model: Accuracy and Overfitting. See you there.

## Thumbnail
Headline: AI Is Dials and Nudges
Image: Navy background, a mixing desk of glowing teal sliders that fade into a network of connected dots, headline in teal Inter Bold.

## Production Notes
- [VERIFY] Exercise step 2: check that free-tier ChatGPT and Claude keep the same secret numbers across turns. The CTA names a friend as the checker and says a chatbot can also play; if the check fails, cut the words 'or a chatbot' from the CTA and rebuild.
- Scene 13 shows the exercise worksheet as a slide: a table with 6 rounds and the columns Round, Slider A (0–10), Slider B (0–10), Feedback for A, Feedback for B, What I changed and why. Round 1 is pre-filled with 5 and 5.
- Kwame's cooperative in Ghana is fictional; stock footage of cocoa beans must not show real brand names or logos.
- Keep all visuals free of equations, as the lesson title promises.
