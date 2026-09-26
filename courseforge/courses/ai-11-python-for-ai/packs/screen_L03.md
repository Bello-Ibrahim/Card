# Screen Demo Pack: AI-11 L03 Lists and Dictionaries

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-11-python-for-ai_L03_screen_1.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Add a new code cell
2. Type: stalls = ["fruit", "bread", "fish", "spices"]
3. Type: print(stalls[0], stalls[2], stalls[-1])
4. Pause and point at stalls[2] before running

**Narration over this clip (for pacing)**

> We create the list of stalls, and print the items at position zero, position two and position minus one. Before I run it, a quick question. What will position two print? Many people say bread, because it is the second item.

## Clip 2: scene 10

- **Filename:** `ai-11-python-for-ai_L03_screen_2.mp4`
- **Target length:** about 6 seconds

**Steps**

1. Press Shift + Enter
2. Output: fruit fish spices

**Narration over this clip (for pacing)**

> Let's run it. Fruit, fish, spices. Position two is fish, because counting starts at zero.

## Clip 3: scene 11

- **Filename:** `ai-11-python-for-ai_L03_screen_3.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Add lines: stalls.append("flowers") and stalls[1] = "cakes"
2. Add line: print(stalls, len(stalls))
3. Press Shift + Enter
4. Output: ['fruit', 'cakes', 'fish', 'spices', 'flowers'] 5

**Narration over this clip (for pacing)**

> Now we add flowers at the end with append, and replace position one, bread, with cakes. Then we print the whole list and its length. The list now has five items, and cakes sits in position one.

## Clip 4: scene 12

- **Filename:** `ai-11-python-for-ai_L03_screen_4.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Add a new code cell
2. Type: phone_book = {"Lucía": "555-0142", "Arjun": "555-0199"}
3. Type: print(phone_book["Arjun"])
4. Type: phone_book["Mei"] = "555-0107"  # add a new pair
5. Type: phone_book["Lucía"] = "555-0150"  # change an existing value
6. Type: print(phone_book) and print(len(phone_book))
7. Press Shift + Enter
8. Output: 555-0199 / {'Lucía': '555-0150', 'Arjun': '555-0199', 'Mei': '555-0107'} / 3

**Narration over this clip (for pacing)**

> Next, the contact book. We look up Arjun by his name and get his number. Then we add a new contact, Mei, and change Lucía's number. When we print the dictionary, Lucía has her new number and Mei is at the end. The length is three, because len counts the pairs.

## Clip 5: scene 13

- **Filename:** `ai-11-python-for-ai_L03_screen_5.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Add line: print(phone_book.get("Omar", "not found"))
2. Press Shift + Enter
3. Output: not found

**Narration over this clip (for pacing)**

> Finally, what if a key is missing? We ask for Omar with the get method, and give it a second value to use if he is not there. Python prints not found, instead of stopping with an error.

## Production notes for this lesson

- No facts to verify (content.md Review Flags: None). Tomás, the Montevideo market, and all names and phone numbers are made up.
- Printed outputs on screen must match content.md exactly: 'fruit fish spices', "['fruit', 'cakes', 'fish', 'spices', 'flowers'] 5", '555-0199', "{'Lucía': '555-0150', 'Arjun': '555-0199', 'Mei': '555-0107'}", '3', 'not found'.
- Scene with the stalls[2] question: pause on screen for about two seconds before running the cell, so learners can guess.
