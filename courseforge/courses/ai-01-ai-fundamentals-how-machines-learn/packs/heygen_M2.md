# HeyGen Batch Pack: AI-01 M2 (How Machines Learn)

Course: AI Fundamentals: How Machines Learn. Make one HeyGen video per lesson below, using these settings for every video.

| Setting | Value |
|---|---|
| Avatar | **Vaness** (standard avatar), ID `1bd001e7e50f421d891986aad5c8bbd2` |
| Voice | `1bd001e7e50f421d891986aad5c8bbd2` (the same ID as the avatar: if HeyGen does not list it as a voice, use Vaness's paired English voice and record its ID in DECISIONS.md) |
| Background | Solid colour **#00FF00** (pure green, no gradient, no image) |
| Resolution | 1080p (1920×1080) |
| Aspect ratio | 16:9 |
| Avatar framing | Centred, head and shoulders, same size in every lesson |
| Captions/subtitles | **Off** (captions are added in Stage 6) |
| Music | Off |
| Speed | Normal (1.0×) |

How to paste: copy the whole text block for a lesson into a single HeyGen scene. Each blank line is a natural pause. Do not add or change words, because the edit is timed to this exact narration.

Save each finished video with the exact filename shown, and upload it to `/incoming/`.

## L05 Supervised Learning: Classification and Regression

- **Filename:** `ai-01-ai-fundamentals-how-machines-learn_M2_L05_presenter.mp4`
- **Expected length:** about 4.9 minutes (684 words). The quality gate accepts ±10%.

```text
A food delivery app tells you two things. Your order is likely to be on time. And, arrives in about thirty five minutes. Both answers can come from machine learning. But one is a category, and the other is a number.

Welcome to week two. You already know that a model trains on examples with features and labels. When every training example comes with the correct answer attached, we call this supervised learning. The labels act as an answer key.

Supervised learning has two main types, depending on the kind of answer you want. Classification predicts a category. The answer is one choice from a fixed list. Is this email spam or not spam? Is this loan application low, medium or high risk? Does this photo show a cat, a dog or a bird?

Regression predicts a number on a scale. The answer can be any value in a range. How many minutes will this delivery take? What price will this used car sell for? How many umbrellas will this shop sell next week?

Here is a simple test. Ask, could the answer be somewhere in between? A delivery could take thirty four minutes, or thirty five, or anything in between. That is regression. But spam or not spam has no halfway point. That is classification.

Think of a post office. A postal worker reads each letter, and puts it into one of several boxes: local, national or international. That is classification. Next to her, a scale weighs each parcel and shows a number, such as two point four kilograms. That is regression. Both learned their job from past examples. But one gives a box, and the other gives a measurement.

The type matters, because it changes the labels you collect and how you judge the model. For classification, you check how often it picks the right box. For regression, you check how close its number is to the real one.

Let's see both types in one business. Andrés manages a small courier company in Medellín, Colombia. Customers often call to ask when their parcels will arrive. He has records of five thousand past deliveries, with features such as distance, time of day, weather and neighbourhood.

First, he wants to warn customers early about problems. So he adds a label to each old record: late, or on time. A model trained on these records puts new deliveries into one of the two groups. This is classification.

Next, he wants to show an exact arrival time in the tracking message. He uses the same records, but this time the label is the actual number of minutes each delivery took. Now the model predicts a number, such as forty seven minutes. This is regression.

Notice what happened. The features stay almost the same. Only the label changes, and the label decides the type of task.

The same pattern appears in other industries. A tea farm in Sri Lanka might classify leaf photos as healthy or diseased, and use regression to predict next month's harvest in kilograms.

One common mistake is to think that any answer with a number must be regression. A star rating from one to five is written as a number. But a model that picks four stars from five fixed choices is doing classification. A shoe size or a postcode can work the same way. So ask, is this a choice from a list, or a measurement on a scale?

Let's recap. First, supervised learning means the model learns from examples that include the correct answer, called labels. Second, classification predicts a category from a fixed list, such as spam or not spam. Third, regression predicts a number on a scale, such as a delivery time in minutes, or a price.

Now it is your turn. In the exercise below this video, you will read ten business questions and label each one as classification or regression. Watch out for question nine. It looks like a scale, but think carefully. It takes about fifteen minutes. In the next lesson, we meet two more ways machines learn, in Unsupervised and Reinforcement Learning. See you there.
```

## L06 Unsupervised and Reinforcement Learning

- **Filename:** `ai-01-ai-fundamentals-how-machines-learn_M2_L06_presenter.mp4`
- **Expected length:** about 5.0 minutes (701 words). The quality gate accepts ±10%.

```text
Imagine you get ten thousand customer records, and nobody tells you what to look for. There is no answer key. Can a computer still learn something useful? It can. It can even learn to play a game it was never taught.

In the last lesson, we met supervised learning, where every example has a label. But labels cost time and money, and sometimes there is no single correct answer to label. For these situations, there are two other types of machine learning.

The first is unsupervised learning. It works with data that has no labels. The model looks for patterns on its own, most often by putting similar items into groups. This is called clustering. For example, a shop can give a model its customers' shopping habits, and the model may find groups of customers who behave in similar ways.

The second is reinforcement learning. It works through trial and error. A program, called an agent, takes actions. After an action, it receives a reward, a signal that the result was good, or a penalty, a signal that it was bad. Over many attempts, the agent learns which actions lead to more reward.

Game-playing agents are a well-known example. An agent that plays a board game may start with random moves. It loses many games. But slowly, it learns which moves tend to lead to a win.

Here is one picture for all three types. Imagine learning about food in a new country. A local friend tells you the name of every dish you taste. That is supervised learning, because you have labels.

You visit the market alone, and sort dishes into groups, such as sweet, spicy and fried, with nobody naming them. That is unsupervised learning. And you order a different dish each day, then order the ones you enjoy more often. That is reinforcement learning, because you learn from rewards.

So how do you choose? If you have examples with the correct answer, use supervised learning. If you have data but no answers, and you want to discover groups, use unsupervised learning. If there is a series of decisions, and success is only clear after acting, use reinforcement learning.

Now let's see two real-life cases. Leila runs a chain of three clothing shops in Casablanca, Morocco. She wants to send better offers, but she does not know what types of customers she has.

She gives a model two years of anonymous sales records, with no labels. The model finds four clusters. Leila studies them. She recognises one group that buys school uniforms every August, and another that buys formal wear before weddings. She names the groups herself, and creates an offer for each. This is unsupervised learning.

A warehouse company in Poland wants a robot to find fast ways to move boxes between shelves. There is no list of correct routes. Instead, the robot tries routes in a computer simulation. It gets a reward when a box arrives quickly, and a penalty when it bumps into a shelf.

After many attempts, it learns efficient routes. This is reinforcement learning. And if Leila later wanted to predict whether one customer will return next month, using past records labelled returned or did not return, she would use supervised learning.

A common mistake is to think that the computer understands the groups it finds. It does not. It only notices that some items are similar in the data. It cannot tell you that a group is wedding shoppers. A person must interpret each group, and some groups will turn out to be meaningless.

Let's recap. First, unsupervised learning finds groups or patterns in data with no labels, and a person must decide what those groups mean. Second, reinforcement learning learns through trial and error, from rewards and penalties. Third, choose by asking what you have. Labelled answers, data without answers, or a series of decisions with a reward.

Now it is your turn. In the exercise below this video, you will match six scenarios to supervised, unsupervised or reinforcement learning. Then justify one choice in a single sentence, using the words labels, groups or reward. In the next lesson, we open the box, with Neural Networks Without the Maths. See you there.
```

## L07 Neural Networks Without the Maths

- **Filename:** `ai-01-ai-fundamentals-how-machines-learn_M2_L07_presenter.mp4`
- **Expected length:** about 4.9 minutes (686 words). The quality gate accepts ±10%.

```text
You have probably heard that modern AI uses neural networks and deep learning. These words sound difficult. But the main idea is something you have already done. Turn a dial a little, check the result, and turn it again.

In lesson four, you learned what training is. Today we look inside one popular kind of model, the neural network. And there is no maths, I promise.

Picture a neural network as a machine with many small dials. Each dial controls how much one piece of information matters. The technical name for these dials is weights.

The dials are arranged in layers. The input layer receives the features, like the colours and shapes in a photo. Hidden layers in the middle combine them into more useful patterns, such as a round edge or a dark spot. And the output layer gives the prediction, such as cat or not cat.

At the start of training, the dials are set at random, so the predictions are poor. Then training repeats one simple cycle. Show the network an example. Let it make a prediction. Compare the prediction with the correct label. Then nudge every dial a tiny amount, in the direction that would make the mistake smaller.

One nudge changes very little. But after many thousands of examples, the dials settle into good positions. That is what learning means here. Not understanding, but many small adjustments that reduce mistakes.

Think of a sound engineer at a concert, with a mixing desk full of sliders. She listens, moves a few sliders a little, and listens again. A neural network does the same, but it has far more sliders, and the listening is the comparison with the correct label.

A network with many hidden layers is called deep. That is where deep learning gets its name. In a photo network, early layers might react to edges, middle layers to shapes, and later layers to whole objects. More layers can learn more complex patterns, but they need more data and computing power.

Let's see this at work. Kwame works for a cocoa farmers' cooperative in Ghana. The cooperative wants to check photos of cocoa beans, and sort them into good and mouldy before selling them.

Experienced sorters label several thousand photos, and the team trains a neural network. At first, it labels beans almost at random. For each photo, its guess is compared with the sorter's label, and all the dials are nudged slightly.

After many rounds, early layers react to colour spots and fuzzy textures. Middle layers combine these into patterns, like a white patch on a dark surface. And the output layer says mouldy, or good.

Kwame never wrote a rule that says white patches mean mould. The dials found that pattern, because it reduced mistakes. But this also means Kwame cannot easily read the dials to see why a bean was rejected. There are too many, and each one is only a small part of the decision.

In this lesson's exercise, you will feel this for yourself. The worksheet has two sliders, A and B, each from zero to ten. You start both at five. A checker tells you higher or lower, and you adjust, round by round.

One last point. A neural network does not store a copy of every training photo. After training, only the final positions of the dials remain. That is why it can handle a new photo, and also why it can make strange mistakes.

Let's recap. First, a neural network is made of layers of adjustable dials, called weights. Second, training means showing examples, checking the mistakes, and nudging the dials a little, again and again. Third, deep learning means many layers, which can learn more complex patterns, but need more data and computing power.

Now it is your turn. Play the guess and adjust game on the worksheet below this video, with a friend, or a chatbot, as your checker. Then write three sentences on how the game is like training. In the next lesson, we find out how to check a model, with Testing a Model: Accuracy and Overfitting. See you there.
```

## L08 Testing a Model: Accuracy and Overfitting

- **Filename:** `ai-01-ai-fundamentals-how-machines-learn_M2_L08_presenter.mp4`
- **Expected length:** about 5.1 minutes (714 words). The quality gate accepts ±10%.

```text
A company tells you its new AI tool is ninety nine percent accurate. That sounds excellent. But accurate on what? And compared with what? By the end of this lesson, you will know two questions to ask before you trust a number like that.

You know that a model is first trained, and then used. Between those two stages comes testing. It is how we find out whether a model is ready for the real world.

To test fairly, we keep some examples aside before training. The model never sees them while it learns. This group is the test set. The examples used for learning are the training set. We never test on training examples, because the model has already seen them.

Accuracy is the simplest test result. It is the share of test examples the model got right. If it labels ninety out of a hundred test photos correctly, its accuracy is ninety percent.

But accuracy can hide problems. Suppose only five in every hundred bank transactions are fraud. A model that always says not fraud is right ninety five times out of a hundred. Yet it never catches a single fraud. And if the test examples are easier than real life, the model will look better than it is.

A very common problem is overfitting. A model overfits when it learns its training examples too closely, including accidents that do not matter, instead of the general pattern. It scores very well on training examples, and much worse on new ones.

Think of two students before an exam. The first memorises the answers to the practice exam, and scores almost one hundred percent on it. But on the real exam, with new questions, she struggles. The second studies the ideas behind the questions. Her practice score is a little lower, but she also does well on the real exam.

The first student has overfitted. The real exam is the test set. So the clearest warning sign is a large gap between the training score and the test score.

Let's see this in a factory. Nusrat is a quality manager at a garment factory in Dhaka, Bangladesh. Her team wants a camera system to spot faulty shirts. Inspectors label shirt photos faulty or fine, and the team puts one fifth of them aside as a test set.

The first model scores ninety nine percent on the training photos, but only seventy percent on the test photos. That big gap shows overfitting. Most faulty training photos were taken on one table with a blue cloth. So the model had partly learned that blue cloth means faulty.

They take new photos on several tables, and train again. The second model scores ninety one percent on training photos, and eighty nine percent on test photos. The scores are close, so it is more likely to work on new shirts.

But faulty shirts are rare. So before approving it, Nusrat also checks how many of the faulty test shirts it caught. She asks the two questions. Was it tested on examples it never saw? And which mistakes does it make?

Now look at two report cards from your exercise. A clinic wants a model that labels patient messages urgent or not urgent. Report card A says ninety nine percent on training messages, and ninety eight percent on a test set taken from those same training messages.

Report card B says ninety percent on training messages, and eighty seven percent on five hundred new messages from a different month. It also reports that it caught forty six of the fifty urgent messages. Which one would you trust?

Let's recap. First, test a model on examples it never saw during training, called the test set. Second, accuracy is the share of test examples it got right, but it can hide which mistakes it makes, especially when one answer is rare. Third, overfitting means memorising the training examples, and a big gap between training and test scores is the main warning sign.

Now it is your turn. In the exercise below this video, read both report cards carefully. Use the two questions, decide which model you would trust, and explain why in two or three sentences. Next week, we start the final module, with Generative AI and Chatbots. See you there.
```
