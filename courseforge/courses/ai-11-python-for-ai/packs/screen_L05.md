# Screen Demo Pack: AI-11 L05 Repeating Work with Loops

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-11-python-for-ai_L05_screen_1.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Add a new code cell
2. Type: boxes = [12, 9, 15, 11]
3. Type: total = 0
4. Type: for count in boxes: / total = total + count (indented) / print("Running total:", total) (indented)
5. Type (not indented): print("Average:", total / len(boxes))

**Narration over this clip (for pacing)**

> We store four days of boxes in a list, and set the total to zero. Inside the loop, we add each day's count to the total and print it. After the loop, not indented, we print the average.

## Clip 2: scene 10

- **Filename:** `ai-11-python-for-ai_L05_screen_2.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Press Shift + Enter
2. Output: Running total: 12 / 21 / 36 / 47
3. Output: Average: 11.75
4. Highlight the indentation of the two print lines

**Narration over this clip (for pacing)**

> Run it. The running total grows from twelve to forty-seven, one line per day. Then the average appears once, eleven point seven five, because that line runs after the loop ends.

## Clip 3: scene 11

- **Filename:** `ai-11-python-for-ai_L05_screen_3.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Add a new code cell
2. Type: for day in range(1, 4): / print("Day", day)
3. Type: stock = 5 / while stock > 0: / stock = stock - 2
4. Type: print("Stock after loop:", stock)
5. Press Shift + Enter
6. Output: Day 1 / Day 2 / Day 3 / Stock after loop: -1

**Narration over this clip (for pacing)**

> Next, a quick look at range and a while loop. The for loop prints day one, day two and day three. Then the stock starts at five, and the while loop takes away two, while the stock is above zero. The result is minus one. Why not zero?

## Clip 4: scene 12

- **Filename:** `ai-11-python-for-ai_L05_screen_4.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Show trace overlay: 5 → 3 → 1 → -1
2. Add a new code cell
3. Type: print(sum(boxes), max(boxes))
4. Press Shift + Enter
5. Output: 47 15

**Narration over this clip (for pacing)**

> Let's trace it. Five becomes three, then one, then minus one. Only then is the condition false. This is why we trace loops by hand. Finally, the built-in shortcut. Sum and max give forty-seven, and the best day, fifteen.

## Production notes for this lesson

- [VERSION] Check the Colab button for stopping a running cell against the live interface before recording.
- Ayşe and her İzmir textile workshop are fictional; all box and sales figures are made up.
- Printed outputs on screen must match content.md exactly: 'Running total: 12 / 21 / 36 / 47' and 'Average: 11.75'; 'Day 1 / Day 2 / Day 3' and 'Stock after loop: -1'; '47 15'.
- Stock -1 question: pause on screen for about two seconds before revealing the trace (5 → 3 → 1 → -1).
