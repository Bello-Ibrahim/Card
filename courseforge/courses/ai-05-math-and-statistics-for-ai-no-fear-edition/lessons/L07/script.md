# L07 Probability and Conditional Probability | Presenter Script

Course: AI-05 · Video: 5 min · Words: 699

## Hook
An email arrives with the word prize in the subject line. Is it spam? You probably feel: very likely. But how likely, exactly? With one small table and some counting, you can put a number on that feeling.

## Explain
Last time, we described data with a few numbers. Today we measure how likely things are. Probability is a number from zero to one. Zero means it never happens, one means it always happens, and zero point five means half of the time. You can also say zero point two is twenty percent.

When you have counts, probability is simply a fraction: the number of times the event happens, divided by the total number of cases. We write P of A, the probability of A. Joint probability is the chance that two things are both true, like spam and contains prize.

Conditional probability is the chance that something is true, when we already know something else is true. We write P of A, a vertical line, then B. The line is read as given. The rule in words: look only at the cases where B is true, and ask what fraction of them also have A.

A two-way frequency table makes this visible. The rows answer one question, spam or not. The columns answer another, contains prize or not. Machine learning uses this all the time. When a classifier says eighty-five percent likely to be spam, that is a conditional probability: the chance of a class, given the features it sees.

Here is an easy way to picture it. Conditional probability is like a filter in a spreadsheet. First you filter the table to show only the rows where B is true. Then you count how many visible rows also have A. Everything filtered out no longer matters.

## Demonstrate
Aigerim is a data analyst for an email service in Almaty, Kazakhstan. She takes a sample of one thousand labelled emails. All the counts are invented for the example.

Two hundred emails are spam, and eight hundred are not. Of the spam emails, sixty contain prize and one hundred and forty do not. Of the other emails, twenty contain prize and seven hundred and eighty do not. So eighty emails in total contain prize.

First, the simple ones. The probability of spam is two hundred divided by one thousand, which is zero point two. The probability of prize is eighty divided by one thousand, zero point zero eight. The probability of spam and prize is sixty divided by one thousand, zero point zero six.

Now the conditional ones. Spam given prize: look only at the prize column. It has eighty emails, and sixty are spam. Sixty divided by eighty is zero point seven five. Prize given spam: look only at the spam row. It has two hundred emails, and sixty contain prize. Sixty divided by two hundred is zero point three.

So knowing that an email contains prize raises the chance of spam from zero point two to zero point seven five. But only thirty percent of spam contains prize, so this word alone would miss most spam. In NumPy, Aigerim puts the four inner counts in an array and gets the same three answers.

The most common mistake is swapping the two sides of the line. Spam given prize and prize given spam are different questions, with different answers: zero point seven five and zero point three. Before you divide, say in words which group you are looking inside. That group goes at the bottom of the fraction.

## Recap
Let's recap. First, probability is a number from zero to one, and with counts it is matching cases divided by the total. Second, P of A given B means: look only at the cases where B is true, and find the fraction that also have A. Third, A given B and B given A are usually different, because they divide by different groups.

## CTA
Your turn. In the exercise, you fill in a table for five hundred online orders, late or on time, returned or kept, and calculate five probabilities. It takes about twenty-five minutes. Next, we use these tables to update beliefs, in Bayes' Theorem with Frequency Tables. See you there.

## Thumbnail
Headline: Spam, Given 'Prize'?
Image: Navy background, a grid of small squares with some red and some starred, one column highlighted in teal, headline in teal Inter Bold.

## Production Notes
- No facts to verify: content.md Review Flags say None. All counts and probabilities are hypothetical.
- Aigerim, the Almaty email service and the 1,000 emails are fictional. Stock inbox footage must not show real email brands, real addresses or readable personal messages.
- Say P(spam | prize) as 'the probability of spam, given prize'; the slides show the notation.
- Not a screen demo lesson: code appears only on a code slide.
