# L08 Where Each Model Type Fails | Presenter Script

Course: AI-02 · Video: 5 min · Words: 706

## Hook
A chatbot gives you a perfect-looking reference to a report that does not exist. An image generator draws a person with six fingers. A photo reader turns one point five kilos into fifteen. Each tool failed differently. If you know why, you know where to check.

## Explain
In the last lesson, Diego caught two errors in his table. Today we look at the typical failures of all three families. Each one comes from how the model works. Start with language models.

Language models generate likely text, token by token. So they can invent facts and sources, like names, numbers, quotes or references that sound real but are not. And because of the knowledge cut-off, their answers can be out of date.

Image models build pictures from learned patterns. They can struggle with hands and fingers, which vary a lot and are small in most images. They can produce letters that are not real words, because they learned what text looks like, not how to spell.

They may not follow exact counts or positions, like exactly seven chairs. And if you ask for a doctor, you may get a very typical-looking person, because the model fills gaps with common patterns.

Multimodal models read images and audio and answer in text. They can misread small, blurred or handwritten details. They can miss parts, like a skipped row or quiet speech. And they can fill gaps with likely values that are not in the input.

Bias affects all three families. Models learn from huge collections of human-made text and images. If some groups, languages or places are missing or stereotyped in that data, the model can repeat it. In a chatbot's words, in the people an image model draws, or in how well a speech tool understands accents.

There is one more risk. Realistic generated audio and video make it easier for someone to fake a voice message or a video of a person saying something they never said. Here the problem is not a model mistake. It is a person using the output to deceive.

Think of three skilled workers. The writer is fluent, but sometimes invents a quote. The painter makes beautiful scenes, but struggles with small hands and signs. The typist is fast, but misreads untidy handwriting. A good manager knows where each one goes wrong and checks there first.

## Demonstrate
Let's see how this works in a newsroom. Farida is an editor at a news website in Casablanca. Her team uses three types of AI tool, and she writes a simple checking guide for her staff.

A reporter's AI draft includes a quote from a ministry spokesperson that nobody can find. Rule one: check every quote, number and source against an original document.

A designer's market illustration shows signs with letters that are not real words. Rule two: add real text in a design tool, and label AI images as illustrations, not photos. An intern turns a photo of a printed table into text, and one row is missing. Rule three: count the rows and check every number.

Farida adds a hypothetical case. A staff member gets a voice message that sounds exactly like Farida, asking for an urgent payment to a new supplier. It is fake. Rule four: for unusual requests about money or private data, confirm through a second, known channel, like calling back on a saved number.

A common mistake is to think a newer or more expensive model has no failures. It may fail less often, but the causes remain. So learn each family's typical failures, and check those points every time.

## Recap
Let's recap. First, language models can invent facts and sources, image models can struggle with hands, text and counts, and multimodal models can misread details. Second, all three can repeat bias from their training data. Third, realistic generated audio and video increase the risk of deception, so confirm unusual requests another way.

## CTA
Your turn. In the exercise below, collect one failure from a text tool, one from an image tool and one from a multimodal tool. For each, write one sentence about the likely cause. It takes about twenty-five minutes. Next week, we start choosing tools, with matching the task to the model. See you there.

## Thumbnail
Headline: Know Where to Check
Image: Navy background, three cards in a row, a document with a question mark, a hand with six fingers and a blurred number, each with a teal magnifying glass, headline in teal Inter Bold.

## Production Notes
- [VERIFY] Hands, text inside images, exact counts and typical-looking people are presented as things image models 'can' struggle with (scenes 4 and 5). A reviewer must confirm these are still common failure types for current image models and that the stated causes are accurate enough for beginners. Drop any that no longer apply.
- [VERIFY] Scene 8 says realistic generated audio and video make it easier to fake a message. Confirm this wording, without naming specific tools or incidents.
- [VERSION] Free text, image and multimodal tools for the exercise, and their upload options, must be chosen and checked before recording (image tool: Google Gemini, per DECISIONS.md).
- The deception and bias cases are hypothetical on purpose, to avoid unverified claims about real companies or people. Do not use real people's faces or voices in any visual; the fake voice message in scene 13 is shown only as a generic audio waveform on a phone screen.
- Farida and the Casablanca news website are fictional; no real outlet name or logo in stock footage.
