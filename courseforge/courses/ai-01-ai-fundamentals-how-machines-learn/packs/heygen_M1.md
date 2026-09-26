# HeyGen Batch Pack: AI-01 M1 (What AI Is and Where You Meet It)

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

## L01 What Is AI, Really?

- **Filename:** `ai-01-ai-fundamentals-how-machines-learn_M1_L01_presenter.mp4`
- **Expected length:** about 5.1 minutes (708 words). The quality gate accepts ±10%.

```text
Your phone unlocks when it sees your face. Your email hides spam before you even open it. But nobody wrote a rule for your face, or for every spam message ever sent. So how does the machine know? Let's find out.

Hi, and welcome to AI Fundamentals. In this first lesson, we answer a simple question. What is artificial intelligence, really?

Artificial intelligence, or AI, is a broad name for computer systems that do tasks we usually connect with human intelligence. For example, recognising faces, understanding speech, translating text, or recommending the next song you might like.

There are two main ways to make a computer do a task like this. The first way is rules. A person writes exact instructions. For example: if a message contains the word lottery, and it comes from an unknown sender, move it to spam.

Rules work well when a task is simple and does not change. But they break down when there are too many cases for a person to describe. Spammers simply change their words, and the rule stops working.

The second way is learning from examples. Instead of writing rules, we show the computer thousands of emails that people have already marked as spam or not spam. The computer finds patterns in those examples, and uses them to decide about new emails. This is called machine learning.

Here is a simple way to picture it. Imagine you arrive in a new city. You can follow a printed list of directions: turn left, then right, then straight on. That works, until a road is closed.

Or you can walk around the city for a few weeks, until you know the streets and find your own way. Rules are the printed list. Machine learning is learning the city by experience.

You will often hear four terms that sound similar. Picture them as circles, one inside the other. Artificial intelligence is the biggest circle. Inside it is machine learning, systems that learn patterns from data. Inside that is deep learning, which uses large neural networks. And inside that is generative AI, which creates new text, images or sound, like the chatbots you may already use.

Let's see this in a real situation. Amina runs a small online shop in Nairobi that sells handmade baskets. Every day, customers send her messages, and she wants them sorted into three groups: order questions, delivery problems, and other.

First, she tries rules. If a message contains the words where is my, label it delivery problem. It works for some messages. But customers write in many different ways. Still waiting for my parcel. Has it shipped yet? The courier never came. Her list of rules keeps growing, and it still misses messages.

So she tries a machine learning tool. She labels three hundred old messages by hand, and gives them to the tool as examples. The tool learns which words and phrases usually appear in each group. Now it labels most new messages correctly, even ones Amina never thought to write a rule for.

But notice this. For calculating delivery fees, Amina keeps a simple rule. Fees follow a fixed price table, so a rule is clearer, cheaper and always correct. Machine learning is not always the answer.

One common mistake is to think that AI means a thinking machine that understands the world like a person. Today's AI does not understand in that way. Amina's tool has learned patterns in words. It does not know what a basket is. So it can be confidently wrong when it sees something unlike its examples.

Let's recap. First, AI is a broad name for systems that do tasks we connect with human intelligence, built with rules or by learning from examples. Second, machine learning means the computer finds patterns in examples, instead of following rules a person wrote. Third, AI, machine learning, deep learning and generative AI fit inside each other like circles.

Now it is your turn. In the exercise below this video, you will sort eight everyday systems, from a calculator to a spam filter, into rules or learning from examples. It takes about fifteen minutes. In the next lesson, we will go on a tour of the AI you already use every day. See you there.
```

## L02 AI in Your Day

- **Filename:** `ai-01-ai-fundamentals-how-machines-learn_M1_L02_presenter.mp4`
- **Expected length:** about 5.1 minutes (720 words). The quality gate accepts ±10%.

```text
Before lunch today, you may already have used five or more AI systems, without noticing any of them. In this lesson, we follow one ordinary day, and we stop each time AI is working in the background.

In the last lesson, we saw that machine learning systems learn patterns from examples. Now let's learn to spot them in daily life. For any feature, ask two simple questions.

Question one. What does it predict? Almost every machine learning feature makes a guess about something it cannot know for certain. Is this email spam? Which song will this person enjoy next? Question two. What data did it probably learn from? To make that guess, the system needed many past examples.

Let's try the questions on some common features. A spam filter predicts whether a new email is spam. It probably learned from huge numbers of emails that people marked as spam or not spam. Video and music recommendations predict what you will play next. They probably learned from what many people chose, skipped or replayed.

A map app predicts how long your trip will take right now, from past trips on the same roads. Face unlock predicts whether the face in front of the camera is yours. And translation tools and voice assistants predict the most likely words, from large collections of text and speech.

Notice the word probably. Companies do not always explain what data they use, so our answers are informed guesses. That is fine. The goal is the habit of asking the two questions.

Here is a helpful way to picture it. Think of a weather forecaster. They cannot see tomorrow. But they have studied years of past weather, so each morning they can say, there is a seventy percent chance of rain.

Every AI feature in your day is a small forecaster. It looks at the situation right now, and it makes a guess based on past examples.

Let's follow one ordinary day. Rahul is a delivery driver in Pune, India. At seven in the morning, he opens his email. Two messages about free prizes are already in the spam folder. The prediction is spam or not spam. The data is emails that other users have marked.

At eight, he checks his map app. It says the route to the warehouse will take twenty five minutes, not the usual fifteen. The prediction is travel time. The data is past and current trips by many drivers on those roads.

At half past twelve, a customer writes to him in Tamil, which he does not read well. So he uses a translation tool. The prediction is the most likely English sentence. The data is texts that exist in both languages.

In the evening, a video app suggests a cricket highlights video. The prediction is what he will watch next. The data is his own viewing history, and the choices of people with similar habits.

Sofía, a nurse in Valparaíso, Chile, has a different day. Her keyboard suggests the next word in Spanish, and a music app builds a playlist for her night shift. The features change, but the pattern stays the same: a prediction, plus past data.

Now, a common mistake. Many people think that anything smart on a phone must be AI. But an alarm that rings at half past six every day follows a fixed rule. So does a calculator.

Here is a useful test. If the feature makes a guess that could be wrong, and it improves with more examples, it is probably machine learning. If it always gives the same output for the same input, it is probably not.

Let's recap. First, you can spot machine learning by asking two questions. What does it predict, and what data did it probably learn from? Second, common examples include spam filters, recommendations, map travel times, face unlock, translation and voice assistants. Third, not every automatic feature is AI. Fixed rules, like a timed alarm, do not learn from examples.

Now it is your turn. In the exercise below this video, you will keep an AI diary for one day. List five AI features you use, and write what each one predicts and what data it probably learned from. In the next lesson, we look inside those examples, with Learning from Examples: Data, Features and Labels. See you there.
```

## L03 Learning from Examples: Data, Features and Labels

- **Filename:** `ai-01-ai-fundamentals-how-machines-learn_M1_L03_presenter.mp4`
- **Expected length:** about 5.1 minutes (713 words). The quality gate accepts ±10%.

```text
Nobody gives a three year old a written definition of cat. Yet after seeing enough cats and dogs, the child can point at an animal they have never seen before, and say cat. Machine learning works in a surprisingly similar way.

In lesson one, we said that machine learning means finding patterns in examples. Today we give names to the parts of those examples. Three words matter most: data, features and labels.

Data is the full collection of examples the system learns from. It could be photos, emails, sound recordings, or rows in a table.

Features are the pieces of information in each example that the system can use to decide. For a photo of an animal, features could be the shape of the ears, the size of the body, or the length of the nose. For an email, they could be certain words, the sender, or the number of links.

A label is the correct answer for an example. A photo labelled cat tells the system, this one is a cat. Labels are usually added by people, and they are what the system tries to predict for new examples. So one example is a set of features, plus its label.

Here is a picture to remember. A child and a parent look at a picture book. On each page, the parent points and says cat, or dog. The pictures are the data. The pointy ears, the whiskers and the long tail are the features the child notices.

The words cat and dog are the labels. After many pages, the child can name animals in a new book, without help.

Three things decide how well the system learns. Quantity: a few examples are rarely enough. Variety: the examples should cover the situations the system will meet later. If every cat photo shows a grey cat indoors, it may fail on a black cat in a garden. And quality: labels must be correct, and images must be clear.

Let's see this in a real situation. Chidi manages quality control at a textile factory in Aba, Nigeria. Workers check every roll of fabric by eye for faults, and he wants a camera system to help.

The data is two thousand photos of fabric, taken as it comes off the machines. The features are the things that might show a fault: small holes, uneven colour, loose threads, and lines where the pattern breaks. The labels come from experienced workers, who mark each photo good or faulty.

But the first version often fails on the factory floor. Chidi finds two reasons. First, variety was missing. Almost all the photos showed blue cotton. When the factory switched to patterned fabric, the system was confused.

Second, quality was uneven. Two workers disagreed about small colour differences. One labelled them faulty, and the other labelled them good. So the system received mixed messages.

The team adds photos of every fabric type. The workers also agree on a clear written rule for what counts as faulty, before they label. The second version is much more useful.

The same ideas work far from a factory. Keiko, a librarian in Sapporo, Japan, sorts donated books. Her data is book descriptions, her features are the words in them, and her labels are topics, such as history.

A common mistake is to think that more data always fixes a problem. If thousands of new photos look like the old ones, or carry the same wrong labels, the system learns the same mistake with more confidence. Before collecting more, ask: what situations are missing, and are my labels correct?

Let's recap. First, data is the collection of examples, features are the useful details in each example, and labels are the correct answers. Second, a system learns by finding which features usually go with which label, across many examples. Third, the quantity, variety and quality of examples all affect how well it works on new cases.

Now it is your turn. In the exercise below this video, you will design a fruit-sorting machine. Choose its labels and features, then list three examples that could confuse it, like a green apple next to an unripe orange. In the next lesson, Training versus Using a Model, we see what the system does with all these examples. See you there.
```

## L04 Training vs. Using a Model

- **Filename:** `ai-01-ai-fundamentals-how-machines-learn_M1_L04_presenter.mp4`
- **Expected length:** about 4.9 minutes (692 words). The quality gate accepts ±10%.

```text
When you ask a chatbot a question, is it searching a giant list of stored answers? The real answer explains why AI can be both very helpful, and sometimes wrong.

In the last lesson, we met data, features and labels. Now we look at what the system does with them. A machine learning system has two separate phases.

Phase one is training. The system studies many labelled examples and looks for patterns that connect the features to the labels. It adjusts itself again and again, until its guesses on the training examples are mostly correct. The result of training is called a model.

This is important. A model is a stored set of patterns. It is not a stored copy of the examples.

Phase two is prediction. The finished model is given a new example it has never seen, and it uses its patterns to produce an answer. This phase is also called inference. When you unlock your phone, or get a song suggestion, you are seeing inference.

Training usually happens once, or from time to time, and it can take a lot of data, time and computing power. Inference happens every time someone uses the model, and it is usually fast. And during inference, the model normally does not learn. If the world changes, the model only improves when people collect new data and train it again.

Think of a student preparing for an exam. For weeks, the student studies past questions and their answers. That is training.

Then the student sits the exam, without the textbook, and answers new questions using only what they learned. That is inference. A good student learns the ideas behind the answers, not every answer, so they can handle new questions.

Let's see both phases in a real situation. Grace is a farm adviser in Mbarara, Uganda. Her organisation wants a phone app that helps farmers check whether cassava leaves look healthy or diseased.

First, training. The organisation collects thousands of leaf photos. Plant experts label each one healthy or diseased. A technical team trains a model on powerful computers. This takes time, and it happens before any farmer uses the app.

Then, inference. The model is placed inside the app. A farmer takes a photo of a leaf, and within seconds the app says, probably diseased. It has never seen this exact leaf, so it is not searching a list. It compares the features in the new photo with the patterns it learned.

Later, farmers in a hilly region report wrong answers. Their photos are taken in strong morning light, which was rare in the training photos. The model does not fix itself. Grace's team collects new photos from that region, and trains a new version.

Chatbots work the same way. Mateus, a hotel owner in Recife, Brazil, asks a chatbot to write a welcome message for guests. The model was trained earlier on a large amount of text. His request triggers inference. The model produces new text from patterns, one piece at a time. It does not copy a stored message.

This clears up a common mistake. AI does not look up the answer, like a search engine. That is why it can handle questions it has never seen. It is also why it can sound correct but be wrong. There is no stored true answer to check against.

Let's recap. First, training is the phase where a system finds patterns in labelled examples, and the result is a model. Second, inference is the phase where the model applies those patterns to new examples, and it normally does not learn while doing this. Third, models do not look up stored answers. They produce answers from patterns, so they can handle new cases, but they can also be confidently wrong.

Now it is your turn. In the exercise below this video, ask a free chatbot, ChatGPT or Claude, to explain training and inference to a ten year old. Then write down one thing it got right, and one thing it simplified. It takes about fifteen minutes. In the next lesson, we start a new module with Supervised Learning: Classification and Regression. See you there.
```
