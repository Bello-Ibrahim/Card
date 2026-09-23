# L02 The Anatomy of a Strong Prompt

Course: AI-20 · Module: M1 · Objectives: O2, O3 · Video: 5 min

## Hook
Two people type "a coffee cup" into the same tool. One gets a flat, forgettable picture. The other gets a warm, inviting image that could go on a café menu tomorrow. The tool is the same. The difference is the prompt.

## Explanation
In L01 you saw that anything you do not describe is filled in by the model, often differently each time. A strong prompt reduces this guessing. It tells the model what matters to you.

A simple formula helps you remember what to include. Read it as a checklist, not a rule that you must follow in exact order:

1. **Subject:** what the image is about. "A white ceramic coffee cup."
2. **Action:** what the subject is doing, if anything. "Steam rising from the coffee."
3. **Setting:** where it is. "On a marble café counter."
4. **Style:** the kind of image. "Product photograph", "flat vector illustration", "watercolour painting".
5. **Composition:** how the image is framed. "Close-up, seen from slightly above, cup in the left third of the frame."
6. **Lighting:** where the light comes from and how it feels. "Soft morning light from a window on the right."
7. **Colour:** the main colours or palette. "Warm browns and cream, with one small touch of blue."

You do not need all seven every time. A quick idea may need three parts. A picture for a client usually needs all of them.

**Analogy:** A prompt is like instructions for a taxi driver in a city they do not know. "Take me to the centre" gets you somewhere, but perhaps not where you wanted. "Take me to the north entrance of the central station, near the bus stop" gets you to the right door. Each extra detail removes one wrong destination.

**Specific words beat long lists of adjectives.** Beginners often add words like "beautiful, stunning, amazing, high quality, ultra detailed". These words do not tell the model anything it can draw. Compare "a beautiful cup" with "a cup with a thin gold rim". The second phrase gives the model something it can show. Replace praise words with visible details: a material, a shape, a light direction, a colour.

Keep the language plain. Write in full phrases separated by commas or short sentences. Most tools handle natural language well, so you do not need special codes.

## Worked Example
Inês owns a small café in Lisbon, Portugal. She wants a photo-style image for her online menu. Her first prompt is:

```text
A coffee cup
```

The result is a plain cup on a grey background. It could belong to any café in the world.

She uses the formula to rewrite it:

```text
A white ceramic cup of coffee with a thin gold rim, light steam rising,
on a pale marble café counter with a small plate of custard tarts behind it,
product photograph, close-up from slightly above, cup in the left third,
soft morning light from a window on the right,
warm cream and brown tones with a small blue-and-white tile pattern in the background
```

Now the image looks like it belongs to her café: the tiles suggest Lisbon, the light feels like early morning, and there is empty space on the right where she can add the price later in a design tool.

Notice what Inês did not write. She did not write "amazing" or "4K masterpiece". Every word in her prompt describes something the viewer can see.

## Common Mistake
A common mistake is to fix a weak result by adding more and more words at the end of the prompt. The prompt becomes long and confusing, and some details start to fight each other, for example "dark moody lighting" and "bright sunny day" in the same prompt. When a result is wrong, find the part of the formula that caused the problem and change only that part. Then generate again and compare. Changing one thing at a time shows you what each word does.

## Key Takeaways
1. A strong prompt covers subject, action, setting, style, composition, lighting and colour, as needed for the task.
2. Specific, visible details such as materials, angles and light direction work better than praise words like "beautiful" or "stunning".
3. When a result is wrong, change one part of the prompt at a time and compare, instead of adding more words.

## Hands-on Exercise
**Task:** Rewrite 3 weak prompts with the formula, generate both versions in Gemini, and compare them side by side.
**Tools:** Gemini (free) or Google AI Studio; a notes app, slide or document for the comparison. [VERSION]
**Steps:**
1. Use these 3 weak prompts: "a pair of shoes", "a city street", "a bowl of soup".
2. For each one, choose a small business that might use it, for example a shoe repair shop in Nairobi or a soup kitchen in Montreal.
3. Rewrite each prompt with at least 5 parts of the formula. Label each part in your notes (subject, setting, style and so on).
4. Generate the weak version and the rewritten version of each prompt in Gemini. Do not include personal or confidential information in your prompts.
5. Place each pair side by side in your document.
6. Under each pair, write 2 sentences: what improved, and which single word or phrase made the biggest difference.
**What good looks like:** Three pairs of images where the rewritten version clearly fits a business purpose. Each rewritten prompt uses visible details instead of praise words, and each note identifies one specific phrase that changed the result.
**Time:** about 20 minutes

## Review Flags
- [VERSION] Gemini and Google AI Studio availability and free-tier image limits must be checked against the live tools before recording.
