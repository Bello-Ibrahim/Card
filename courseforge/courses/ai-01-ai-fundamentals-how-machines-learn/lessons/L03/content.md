# L03 Learning from Examples: Data, Features and Labels

Course: AI-01 · Module: M1 · Objectives: O2 · Video: 5 min

## Hook
Nobody gives a three-year-old a written definition of "cat". Yet after seeing enough cats and dogs, the child can point at an animal they have never seen before and say "cat". Machine learning works in a surprisingly similar way.

## Explanation
In L01 we said that machine learning means finding patterns in examples. This lesson gives names to the parts of those examples. Three words matter most: **data**, **features** and **labels**.

**Data** is the full collection of examples the system learns from. It could be photos, emails, sound recordings or rows in a table.

**Features** are the pieces of information in each example that the system can use to make a decision. For a photo of an animal, features could include the shape of the ears, the size of the body or the length of the nose. For an email, features could include certain words, the sender or the number of links.

A **label** is the correct answer for an example. A photo labelled "cat" tells the system: "This one is a cat." Labels are usually added by people, and they are what the system tries to predict for new examples.

So one example is a set of features plus its label. The system studies many of these and looks for which features usually go together with which label.

**Analogy:** Imagine a child and a parent looking at a picture book. On each page the parent points and says "cat" or "dog". The pictures are the data. The pointy ears, the whiskers and the long tail are the features the child notices. The words "cat" and "dog" are the labels. After many pages, the child can name animals in a new book without help.

Three things decide how well the system learns:

- **Quantity.** A few examples are rarely enough. With more examples, the system has a better chance to find the real patterns and not accidental ones.
- **Variety.** The examples should cover the situations the system will meet later. If every cat photo shows a grey cat indoors, the system may fail on a black cat in a garden.
- **Quality.** Labels must be correct and features must be clear. If some dog photos are wrongly labelled "cat", the system learns the wrong lesson. Blurry or dark images also make features hard to see.

In deep learning systems (L07), the computer finds useful features by itself. A person still decides what data to collect and which labels to use.

## Worked Example
Chidi manages quality control at a textile factory in Aba, Nigeria. Workers check every roll of fabric by eye for faults, and he wants a camera system to help.

**Data:** The team takes 2,000 photos of fabric as it comes off the machines.

**Features:** The things that might show a fault: small holes, uneven colour, loose threads and lines where the pattern breaks.

**Labels:** Experienced workers look at each photo and write "good" or "faulty".

The first version often fails on the factory floor. Chidi finds two reasons:

- **Variety was missing.** Almost all the photos showed blue cotton, because that was the main product that month. When the factory switched to patterned fabric, the system was confused.
- **Quality was uneven.** Two workers disagreed about small colour differences. One labelled them "faulty" and the other labelled them "good". The system received mixed messages.

The team adds photos of every fabric type, and the workers agree on a clear written rule for what counts as "faulty" before they label. The second version is much more useful.

Keiko, a librarian in Sapporo, Japan, uses the same ideas to sort donated books. Her data is book descriptions, her features are the words in them, and her labels are topics such as "history".

## Common Mistake
Many learners think that more data always fixes a problem. If thousands of new photos look like the old ones, or carry the same wrong labels, the system learns the same mistake with more confidence. Variety and correct labels matter as much as quantity. Before collecting more, ask: "What situations are missing, and are my labels correct?"

## Key Takeaways
1. Data is the collection of examples, features are the useful details in each example, and labels are the correct answers.
2. A system learns by finding which features usually go with which label across many examples.
3. The quantity, variety and quality of examples all affect how well the system works on new cases.

## Hands-on Exercise
**Task:** Choose features and labels for a fruit-sorting machine, then list 3 examples that could confuse it.
**Tools:** Pen and paper, or any notes app. Optional: ChatGPT or Claude (free tier) to check your ideas.
**Steps:**
1. Imagine a machine at a market that must sort fruit into apples, oranges and bananas using a camera and a scale.
2. Write the labels the machine will use.
3. List at least 4 features the machine could measure, such as colour, shape, weight or surface texture.
4. For each feature, write why it helps tell the fruits apart.
5. List 3 real examples that could confuse the machine, and say which feature would fail. For example, a green apple next to an unripe orange.
6. Optional: ask a free AI chatbot for more confusing cases.
**What good looks like:** Labels are clear and do not overlap. Features are things a camera or scale could actually measure. The confusing examples are specific and point to a variety or quality problem, such as "a very small banana that weighs the same as an apple".
**Time:** about 15 minutes

## Review Flags
- None. The examples are general and hypothetical, and no specific facts need checking.
