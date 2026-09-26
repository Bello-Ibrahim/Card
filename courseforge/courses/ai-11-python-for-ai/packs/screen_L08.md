# Screen Demo Pack: AI-11 L08 Errors and How to Fix Them

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-11-python-for-ai_L08_screen_1.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Add a new code cell
2. Type: prices = [4, 6, 9]
3. Type: print(prices[3])
4. Press Shift + Enter; a traceback appears

**Narration over this clip (for pacing)**

> First, a list of three prices. We ask for the item at position three and run the cell. Python stops with a traceback. Let's read it the right way.

## Clip 2: scene 10

- **Filename:** `ai-11-python-for-ai_L08_screen_2.mp4`
- **Target length:** about 24 seconds

**Steps**

1. Highlight the last line: IndexError: list index out of range
2. Highlight the marked line above: print(prices[3])
3. Change prices[3] to prices[2] (or prices[-1])
4. Press Shift + Enter; the cell runs

**Narration over this clip (for pacing)**

> The last line says IndexError, list index out of range. So a list position doesn't exist. Just above, it points to our print line. The list has three items, at positions zero, one and two. So position three is outside it. We change it to two, or minus one for the last item, and it works.

## Clip 3: scene 11

- **Filename:** `ai-11-python-for-ai_L08_screen_3.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Add a new code cell
2. Type: def ask_boxes(answer):
3. Type (indented): try: / return int(answer)
4. Type (indented): except ValueError: / print("Please type a whole number, such as 12.") / return None

**Narration over this clip (for pacing)**

> Next, the input problem. Staff sometimes type words instead of numbers. We write a function called ask boxes. Inside a try block, it converts the answer to a whole number and returns it. If a ValueError happens, the except block prints a friendly message and returns None.

## Clip 4: scene 12

- **Filename:** `ai-11-python-for-ai_L08_screen_4.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Type: print(ask_boxes("12"))
2. Type: print(ask_boxes("twelve"))
3. Press Shift + Enter
4. Output: 12 / Please type a whole number, such as 12. / None

**Narration over this clip (for pacing)**

> We call it twice, once with the text twelve in digits, and once with the word twelve. The first call returns twelve. The second prints our friendly message, then None. Without try, the whole script would stop with a ValueError. With it, the script continues.

## Production notes for this lesson

- [VERSION] Traceback layout differs between plain Python and Colab, and message wording changes between Python versions (newer versions add hints such as 'Did you mean'). Check the last-line messages in the current Colab runtime before recording; content.md messages were produced with Python 3.11.
- [VERSION] Check how Colab marks the failing line (arrow and line number) before recording.
- Printed outputs on screen must match content.md: 'IndexError: list index out of range' and '12 / Please type a whole number, such as 12. / None'.
- Farida and the Almaty spice shop are fictional; all values are made up.
