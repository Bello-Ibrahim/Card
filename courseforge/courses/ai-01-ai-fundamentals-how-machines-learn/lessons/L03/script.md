# L03 Learning from Examples: Data, Features and Labels | Presenter Script

Course: AI-01 · Video: 5 min · Words: 714

## Hook
Nobody gives a three year old a written definition of cat. Yet after seeing enough cats and dogs, the child can point at an animal they have never seen before, and say cat. Machine learning works in a surprisingly similar way.

## Explain
In lesson one, we said that machine learning means finding patterns in examples. Today we give names to the parts of those examples. Three words matter most: data, features and labels.

Data is the full collection of examples the system learns from. It could be photos, emails, sound recordings, or rows in a table.

Features are the pieces of information in each example that the system can use to decide. For a photo of an animal, features could be the shape of the ears, the size of the body, or the length of the nose. For an email, they could be certain words, the sender, or the number of links.

A label is the correct answer for an example. A photo labelled cat tells the system, this one is a cat. Labels are usually added by people, and they are what the system tries to predict for new examples. So one example is a set of features, plus its label.

Here is a picture to remember. A child and a parent look at a picture book. On each page, the parent points and says cat, or dog. The pictures are the data. The pointy ears, the whiskers and the long tail are the features the child notices.

The words cat and dog are the labels. After many pages, the child can name animals in a new book, without help.

Three things decide how well the system learns. Quantity: a few examples are rarely enough. Variety: the examples should cover the situations the system will meet later. If every cat photo shows a grey cat indoors, it may fail on a black cat in a garden. And quality: labels must be correct, and images must be clear.

## Demonstrate
Let's see this in a real situation. Chidi manages quality control at a textile factory in Aba, Nigeria. Workers check every roll of fabric by eye for faults, and he wants a camera system to help.

The data is two thousand photos of fabric, taken as it comes off the machines. The features are the things that might show a fault: small holes, uneven colour, loose threads, and lines where the pattern breaks. The labels come from experienced workers, who mark each photo good or faulty.

But the first version often fails on the factory floor. Chidi finds two reasons. First, variety was missing. Almost all the photos showed blue cotton. When the factory switched to patterned fabric, the system was confused.

Second, quality was uneven. Two workers disagreed about small colour differences. One labelled them faulty, and the other labelled them good. So the system received mixed messages.

The team adds photos of every fabric type. The workers also agree on a clear written rule for what counts as faulty, before they label. The second version is much more useful.

The same ideas work far from a factory. Keiko, a librarian in Sapporo, Japan, sorts donated books. Her data is book descriptions, her features are the words in them, and her labels are topics, such as history.

A common mistake is to think that more data always fixes a problem. If thousands of new photos look like the old ones, or carry the same wrong labels, the system learns the same mistake with more confidence. Before collecting more, ask: what situations are missing, and are my labels correct?

## Recap
Let's recap. First, data is the collection of examples, features are the useful details in each example, and labels are the correct answers. Second, a system learns by finding which features usually go with which label, across many examples. Third, the quantity, variety and quality of examples all affect how well it works on new cases.

## CTA
Now it is your turn. In the exercise below this video, you will design a fruit-sorting machine. Choose its labels and features, then list three examples that could confuse it, like a green apple next to an unripe orange. In the next lesson, Training versus Using a Model, we see what the system does with all these examples. See you there.

## Thumbnail
Headline: Data, Features, Labels
Image: Navy background, a photo card of a cat with small teal tags pointing to ears and whiskers and a large label tag reading 'cat', headline in teal Inter Bold.

## Production Notes
- No facts to verify: all examples are general or hypothetical (content.md Review Flags: None).
- Chidi's factory in Aba and Keiko's library in Sapporo are fictional; stock footage must not show a real company name or logo.
- Keep the number 2,000 on the slide as '2,000 photos'; the presenter says 'two thousand'.
