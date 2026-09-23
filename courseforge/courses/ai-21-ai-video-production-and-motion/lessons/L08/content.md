# L08 Keeping Characters and Scenes Consistent

Course: AI-21 · Module: M2 · Objectives: O3, O5 · Video: 5 min

## Hook
In shot 2 your character wears a blue scarf. In shot 3 the scarf is green. In shot 4 her hair is shorter. Viewers may not name the problem, but they feel that something is wrong. This lesson shows why this happens and how to reduce it.

## Explanation
**Why clips drift.** A video model does not remember your previous clip. Each generation starts again from your prompt, and sometimes an image. Words such as "a woman in a scarf" allow many possible results, so the model chooses a slightly different one each time. The common changes are:

- **Faces:** shape, age or features change.
- **Clothes:** colours, patterns and accessories change.
- **Colours and light:** one shot is warm, the next is cool.
- **Props:** a cup becomes a glass; a logo changes shape.
- **Setting:** a window moves to the other wall.

**Techniques that reduce drift:**

1. **Reuse keyframes.** Start clips from keyframes that already match (L05). This is the strongest technique for beginners.
2. **Use a fixed character description.** Paste the same words every time: "a man in his forties with a short grey beard, round glasses, dark green apron over a white shirt".
3. **Use reference features where tools offer them.** Some tools let you give a reference image of a character or object to reuse [VERSION]. Use only fictional characters or images you have the rights to.
4. **Keep the style block fixed** in every prompt.
5. **Make editing choices that hide small changes.** Cut from a wide shot to a close-up of hands, so a small face change is less visible. Keep shots of the same character short. Avoid placing two very similar shots next to each other.

Perfect consistency is not always possible with current tools [VERSION]. Your job is to make changes small enough that viewers do not notice them.

**Analogy:** Film crews have a continuity supervisor. This person photographs every actor and set before each take, so that the coffee cup is still half full and the collar is still open in the next shot. When you work with AI video, you are your own continuity supervisor.

## Worked Example
Tomás runs a hypothetical bookshop in Córdoba, Argentina. He wants a friendly fictional bookseller character in 3 shots. His fixed description:

```text
A man in his fifties with short grey hair, a neat grey beard, round black glasses, a dark green apron over a white shirt with rolled sleeves.
```

He generates 3 clips from text only: the man takes a book from a shelf, reads at a counter, and hands a paper bag to a customer. His continuity list:

| Shot | Change noticed | Visible? |
|---|---|---|
| 2 | Glasses are thinner and gold | Yes, in a close-up |
| 3 | Apron is dark blue, not green | Yes |
| 3 | Beard is longer | Small |
| 2–3 | The counter is wood in shot 2 and white in shot 3 | Yes |

His fixes: he generates one keyframe of the bookseller and uses it as the starting image for all 3 shots. He adds "wooden counter" to every prompt. For shot 3, he changes the framing to a close-up of hands and the paper bag, so the face is not needed. The new version has only one small change, which he accepts.

## Common Mistake
Many learners check each clip on its own and decide it is good. Continuity problems only appear when clips are next to each other. Always review clips in order, side by side or in a rough timeline, before you decide which ones to keep.

## Key Takeaways
1. Clips drift because each generation starts again, so faces, clothes, colours, props and settings can change between shots.
2. Reusing keyframes, a fixed character description, reference features and a fixed style block all reduce drift.
3. Review clips in order, not one by one, and use editing choices to hide small changes you cannot fix.

## Hands-on Exercise
**Task:** Generate 3 clips of the same character and list every continuity change you notice between them.
**Tools:** Google Flow or Kling [VERSION] [REGION]; your character description and keyframes; a table.
**Steps:**
1. Write or reuse a fixed character description for a fictional character.
2. Generate 3 short clips of the character doing 3 different actions, using the same description and style block each time.
3. Place the clips side by side, or in order on a simple timeline.
4. Pause each clip at a similar moment and compare face, clothes, colours, props and setting.
5. List every change in a table with the shot number, the change, and whether a viewer would notice it.
6. Choose one technique from this lesson to fix the biggest change, and note it.
7. Optional: regenerate one clip with that fix and compare again.
**What good looks like:** A table with at least 4 specific changes, such as "apron changes from green to blue in shot 3", an honest note on visibility, and a clear fix for the biggest problem.
**Time:** about 30 minutes

## Review Flags
- [VERSION] Which tools offer character or object reference features, and how consistent current models are, must be checked against the live tools before scripting.
- [REGION] Google Flow availability differs by country; learners can use Kling for this exercise.
