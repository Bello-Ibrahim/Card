# Screen Demo Pack: AI-11 L04 Making Decisions with if, elif and else

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-11-python-for-ai_L04_screen_1.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Add a new code cell
2. Type: distance_km = 7.5
3. Type: if distance_km <= 3: / price = 8000 (indented)
4. Type: elif distance_km <= 10: / price = 15000 (indented)
5. Type: else: / price = 25000 (indented)
6. Type: print(f"{distance_km} km costs {price} rupiah")

**Narration over this clip (for pacing)**

> In Colab, we set the distance to seven and a half kilometres. Then an if line for three or less, an elif line for ten or less, and an else line for anything further. Each one sets the price. Finally, we print the distance and the price.

## Clip 2: scene 9

- **Filename:** `ai-11-python-for-ai_L04_screen_2.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Point at each condition in turn and show the trace overlay: 7.5 <= 3? No. 7.5 <= 10? Yes.
2. Press Shift + Enter
3. Output: 7.5 km costs 15000 rupiah

**Narration over this clip (for pacing)**

> Before we run it, let's trace it. Is seven and a half three or less? No, so we skip the first block. Is it ten or less? Yes, so the price becomes fifteen thousand, and else is skipped. Now run it. Seven point five kilometres costs fifteen thousand rupiah.

## Clip 3: scene 10

- **Filename:** `ai-11-python-for-ai_L04_screen_3.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Highlight the elif line: elif distance_km <= 10:

**Narration over this clip (for pacing)**

> Notice that the elif line does not need to say more than three. If the distance were three or less, Python would already have stopped at the first block. The order does part of the work.

## Clip 4: scene 11

- **Filename:** `ai-11-python-for-ai_L04_screen_4.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Add a new code cell
2. Type: is_member = True
3. Type: if distance_km > 5 and not is_member: / print("Add a long-distance fee")
4. Type: else: / print("No extra fee")
5. Press Shift + Enter
6. Output: No extra fee

**Narration over this clip (for pacing)**

> Next, Dewi adds a long-distance fee, but members don't pay it. The condition says the distance is more than five, and the customer is not a member. The distance part is true, but the member part is false. And needs both, so we see no extra fee.

## Clip 5: scene 12

- **Filename:** `ai-11-python-for-ai_L04_screen_5.mp4`
- **Target length:** about 11 seconds

**Steps**

1. In the first cell, change distance_km to 2 and pause for a prediction
2. Run the cell and show the result
3. Change distance_km to 12, pause, run and show the result

**Narration over this clip (for pacing)**

> Now you try. What happens if I change the distance to two? And to twelve? Pause the video, make your prediction, and then watch the result.

## Production notes for this lesson

- No facts to verify (content.md Review Flags: None). Dewi, the Jakarta delivery app, the price bands and the rupiah amounts are made up.
- Printed outputs on screen must match content.md exactly: '7.5 km costs 15000 rupiah' and 'No extra fee'.
- Verified with Python 3.11 on 2026-09-23: 2 km prints 8000 rupiah and 12 km prints 25000 rupiah.
- Trace scene: show the trace as an overlay (7.5 <= 3? No. 7.5 <= 10? Yes.) before running the cell.
