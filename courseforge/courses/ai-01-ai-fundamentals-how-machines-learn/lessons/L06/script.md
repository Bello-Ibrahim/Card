# L06 Unsupervised and Reinforcement Learning | Presenter Script

Course: AI-01 · Video: 5 min · Words: 704

## Hook
Imagine you get ten thousand customer records, and nobody tells you what to look for. There is no answer key. Can a computer still learn something useful? It can. It can even learn to play a game it was never taught.

## Explain
In the last lesson, we met supervised learning, where every example has a label. But labels cost time and money, and sometimes there is no single correct answer to label. For these situations, there are two other types of machine learning.

The first is unsupervised learning. It works with data that has no labels. The model looks for patterns on its own, most often by putting similar items into groups. This is called clustering. For example, a shop can give a model its customers' shopping habits, and the model may find groups of customers who behave in similar ways.

The second is reinforcement learning. It works through trial and error. A program, called an agent, takes actions. After an action, it receives a reward, a signal that the result was good, or a penalty, a signal that it was bad. Over many attempts, the agent learns which actions lead to more reward.

Game-playing agents are a well-known example. An agent that plays a board game may start with random moves. It loses many games. But slowly, it learns which moves tend to lead to a win.

Here is one picture for all three types. Imagine learning about food in a new country. A local friend tells you the name of every dish you taste. That is supervised learning, because you have labels.

You visit the market alone, and sort dishes into groups, such as sweet, spicy and fried, with nobody naming them. That is unsupervised learning. And you order a different dish each day, then order the ones you enjoy more often. That is reinforcement learning, because you learn from rewards.

So how do you choose? If you have examples with the correct answer, use supervised learning. If you have data but no answers, and you want to discover groups, use unsupervised learning. If there is a series of decisions, and success is only clear after acting, use reinforcement learning.

## Demonstrate
Now let's see two real-life cases. Leila runs a chain of three clothing shops in Casablanca, Morocco. She wants to send better offers, but she does not know what types of customers she has.

She gives a model two years of anonymous sales records, with no labels. The model finds four clusters. Leila studies them. She recognises one group that buys school uniforms every August, and another that buys formal wear before weddings. She names the groups herself, and creates an offer for each. This is unsupervised learning.

A warehouse company in Poland wants a robot to find fast ways to move boxes between shelves. There is no list of correct routes. Instead, the robot tries routes in a computer simulation. It gets a reward when a box arrives quickly, and a penalty when it bumps into a shelf.

After many attempts, it learns efficient routes. This is reinforcement learning. And if Leila later wanted to predict whether one customer will return next month, using past records labelled returned or did not return, she would use supervised learning.

A common mistake is to think that the computer understands the groups it finds. It does not. It only notices that some items are similar in the data. It cannot tell you that a group is wedding shoppers. A person must interpret each group, and some groups will turn out to be meaningless.

## Recap
Let's recap. First, unsupervised learning finds groups or patterns in data with no labels, and a person must decide what those groups mean. Second, reinforcement learning learns through trial and error, from rewards and penalties. Third, choose by asking what you have. Labelled answers, data without answers, or a series of decisions with a reward.

## CTA
Now it is your turn. In the exercise below this video, you will match six scenarios to supervised, unsupervised or reinforcement learning. Then justify one choice in a single sentence, using the words labels, groups or reward. In the next lesson, we open the box, with Neural Networks Without the Maths. See you there.

## Thumbnail
Headline: No Answer Key? No Problem
Image: Navy background, left: coloured dots gathering into four clusters; right: a small robot next to a star reward icon, headline in teal Inter Bold.

## Production Notes
- No facts to verify: game-playing agents, the shops and the warehouse are generic and hypothetical (content.md Review Flags: None). Do not name or show any real game-playing system.
- Leila's shops in Casablanca and the warehouse company in Poland are fictional; stock footage must not show real brand names or logos.
- Scene 11 hero clip is 6 seconds and the scene is about 22 seconds: hold the clip with a slow push-in, or extend it with stock footage of a warehouse robot moving between shelves.
