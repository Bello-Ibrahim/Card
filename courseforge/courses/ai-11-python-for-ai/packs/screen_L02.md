# Screen Demo Pack: AI-11 L02 Variables and Data Types

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-11-python-for-ai_L02_screen_1.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Add a new code cell
2. Type: rice_price = 3.50  # float
3. Type: rice_qty = 2  # int
4. Type: shop_name = "Duka La Wanjiru"  # str
5. Type: is_open = True  # bool
6. Type: print(type(rice_price), type(rice_qty), type(shop_name), type(is_open))

**Narration over this clip (for pacing)**

> In a new cell, we create four variables. The price of rice, the quantity of rice, the shop name, and whether the shop is open. Then we print the type of each one. The text after the hash sign is a comment. Python ignores it. It is a note for people.

## Clip 2: scene 10

- **Filename:** `ai-11-python-for-ai_L02_screen_2.mp4`
- **Target length:** about 8 seconds

**Steps**

1. Press Shift + Enter
2. Output: <class 'float'> <class 'int'> <class 'str'> <class 'bool'>

**Narration over this clip (for pacing)**

> When we run it, Python shows the four types in order. Float, int, str and bool. One of each.

## Clip 3: scene 11

- **Filename:** `ai-11-python-for-ai_L02_screen_3.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Add a new code cell
2. Type: tea_price = 1.25 and tea_qty = 4
3. Type: subtotal = rice_price * rice_qty + tea_price * tea_qty
4. Type: tax = subtotal * 0.10
5. Type: total = subtotal + tax

**Narration over this clip (for pacing)**

> Next, Wanjiru adds four cups of tea. We multiply each price by its quantity and add them to get the subtotal. The tax is ten percent of the subtotal, and the total is the two added together.

## Clip 4: scene 12

- **Filename:** `ai-11-python-for-ai_L02_screen_4.mp4`
- **Target length:** about 24 seconds

**Steps**

1. Type: print(f"{shop_name}: subtotal {subtotal:.2f}, tax {tax:.2f}, total {total:.2f}")
2. Highlight the f before the quotes and the :.2f parts
3. Press Shift + Enter
4. Output: Duka La Wanjiru: subtotal 12.00, tax 1.20, total 13.20

**Narration over this clip (for pacing)**

> To print a clear receipt line, we use an f-string. The letter f before the quotation marks tells Python to put each variable's value inside the text. We also ask for two decimal places, which suits money. Run it, and we see a subtotal of twelve, tax of one twenty, and a total of thirteen twenty.

## Clip 5: scene 13

- **Filename:** `ai-11-python-for-ai_L02_screen_5.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Add a new code cell
2. Type: typed = "3"
3. Type: print(typed + typed)
4. Type: print(int(typed) + int(typed))
5. Type: print("Items: " + str(rice_qty + tea_qty))
6. Press Shift + Enter
7. Output: 33 / 6 / Items: 6

**Narration over this clip (for pacing)**

> Finally, the puzzle from the start. We store the text three and add it to itself. Python joins the text and prints thirty-three. When we convert both values to whole numbers first, we get six. And to join a number with text, we convert the number to text with str.

## Production notes for this lesson

- No facts to verify (content.md Review Flags: None). Prices and the 10% tax rate are made up; say so on screen as in content.md.
- Wanjiru and 'Duka La Wanjiru' in Nairobi are fictional; do not show a real shop name or logo in stock footage.
- Printed outputs on screen must match content.md exactly: "<class 'float'> <class 'int'> <class 'str'> <class 'bool'>", 'Duka La Wanjiru: subtotal 12.00, tax 1.20, total 13.20', and '33 / 6 / Items: 6'.
- Screen demo: the presenter types each code block from content.md into a new Colab cell, including the # comments, and runs it.
