# L08 Where Each Model Type Fails

Course: AI-02 · Module: M2 · Objectives: O5 · Video: 5 min

## Hook
A chatbot gives you a perfect-looking reference to a report that does not exist. An image generator draws a person with six fingers. A photo reader turns "1.5 kg" into "15 kg". Each tool failed in a different way. If you know why, you can predict where to check.

## Explanation
Each model family has typical weaknesses that come from **how the model works**. If you know the cause, you know what to check.

**Language models** generate likely text, token by token (L02). Their typical failures are:

- **Invented facts and sources:** names, numbers, quotes or references that sound real but are not. This is hallucination (L04).
- **Out-of-date answers:** because of the knowledge cut-off.

**Image models** build pictures from patterns learned in training (L05). Their typical failures are: [VERIFY]

- **Hands, fingers and small body details** that look wrong, because these vary a lot and are small in most training images.
- **Text inside images:** letters that are not real words, because the model learned what text looks like, not how to spell.
- **Exact counts and positions:** "exactly seven chairs" or "the cup to the left of the plate" may not be followed.
- **Typical instead of specific:** a request for "a doctor" may give a very typical-looking person, because the model fills gaps with common patterns.

**Multimodal models** read images and audio and answer in text (L07). Their typical failures are:

- **Misread details:** small, blurred, handwritten or low-contrast characters and numbers.
- **Missing parts:** skipped rows, cut edges or quiet speech.
- **Filled gaps:** likely-looking values that are not in the input.

**Bias affects all three families.** Models learn from very large collections of human-made text and images. If some groups, languages or places are under-represented, or shown in stereotyped ways, in the training data, the model can repeat those patterns. This can appear in a chatbot's words, the people an image model draws or how well a speech tool understands different accents.

**Deception risk.** Generated audio and video can now look and sound very realistic. [VERIFY] This makes it easier for someone to create a fake voice message or video of a person saying something they never said. Here the problem is not a model mistake but a person using realistic output to deceive.

**Analogy:** Think of three skilled but different workers. The writer is fluent but sometimes invents a quote to finish a story. The painter makes beautiful scenes but struggles with small hands and signs. The typist is fast but misreads untidy handwriting. A good manager does not stop using them. The manager knows where each one usually goes wrong and checks those places first.

## Worked Example
Farida is an editor at a hypothetical news website in Casablanca, Morocco. Her team uses three types of AI tool, and she writes a simple checking guide for her staff.

- **Text tool:** a reporter asks for background on a local water project. The draft includes a quote from "a ministry spokesperson" that the reporter cannot find anywhere. Farida's rule: every quote, number and source in AI text must be checked against an original document.
- **Image tool:** a designer creates an illustration of a market. The signs over the stalls show letters that are not real words. Rule: add real text in a design tool, and label AI images as illustrations, not photos.
- **Multimodal tool:** an intern turns a photo of a printed table into text. One row is missing. Rule: count the rows and check every number.

Farida also adds a hypothetical case. A staff member receives a voice message that sounds exactly like Farida, asking for an urgent payment to a new supplier. The message is fake, made with a voice-generation tool. Rule: for any unusual request involving money or private data, confirm through a second, known channel, such as calling back on a saved number.

## Common Mistake
Many learners think that a newer or more expensive model has no failures. Newer models may fail less often, but the causes remain. The correction is to learn each family's typical failures and check those points every time, whatever tool you use.

## Key Takeaways
1. Language models can invent facts and sources, image models can struggle with hands, text in images and exact counts, and multimodal models can misread small or unclear details.
2. All three families can repeat bias from their training data.
3. Realistic generated audio and video increase the risk of deception, so confirm unusual requests through a second, known channel.

## Hands-on Exercise
**Task:** Collect one failure example from a text tool, one from an image tool and one from a multimodal tool, and for each write one sentence about the likely cause.
**Tools:** Claude, ChatGPT or Google AI Studio (free) [VERSION]; a free image generator of your choice [VERSION]; a notes app.
**Steps:**
1. **Text:** ask a chatbot for three published sources about a narrow topic in your field. Try to find each source. Record any that do not exist or have wrong details.
2. **Image:** ask an image generator for "a shop sign that says OPEN 24 HOURS above a door, with exactly four plants in pots". Record any wrong letters or counts.
3. **Multimodal:** upload a photo of a small printed or handwritten note (with no personal data) and ask for the exact text. Record any misread words or numbers.
4. For each failure, write one sentence about the likely cause, using what you learned in L02–L07.
5. Do not use real people's names, faces or voices in any test.
**What good looks like:** Three failure examples, each with a screenshot or copy of the output, and a cause sentence such as "The image model misspelled the sign because it learned what letters look like, not how to spell."
**Time:** about 25 minutes

## Review Flags
- [VERIFY] Confirm that hands, text inside images, exact counts and typical-looking people are still common failure types for current image models, and that the stated causes are accurate enough for beginners.
- [VERIFY] Confirm the wording that generated audio and video can look and sound very realistic, without naming specific tools or incidents.
- [VERSION] Free text, image and multimodal tools, and their upload options, must be chosen and checked by a reviewer before recording.
- Note for reviewer: deception and bias cases are hypothetical on purpose, to avoid unverified claims about real companies or people.
