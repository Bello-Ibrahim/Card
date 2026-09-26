# Screen Demo Pack: AI-11 L10 Working Locally: Files and VS Code

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-11-python-for-ai_L10_screen_1.mp4`
- **Target length:** about 18 seconds

**Steps**

1. In VS Code, choose File > Open Folder and open a new folder named ai11-local
2. Create a new file named guests.csv
3. Type: name,city / Samira,Casablanca / Diego,Quito / Hana,Busan / Emeka,Casablanca
4. Save the file

**Narration over this clip (for pacing)**

> In VS Code, we open a new folder called a i eleven local. Inside it, we create a file called guests dot csv. The first line has the column names, name and city, followed by four guests from Casablanca, Quito and Busan.

## Clip 2: scene 9

- **Filename:** `ai-11-python-for-ai_L10_screen_2.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Create a new file named summary.py
2. Type: import csv
3. Type: with open("guests.csv", encoding="utf-8") as f: / rows = list(csv.DictReader(f)) (indented)

**Narration over this clip (for pacing)**

> Next, a file called summary dot p y. We import the csv module and open the guests file with a with block. The DictReader reads each line as a dictionary, using the first line as keys. So for each row, we can ask for the city.

## Clip 3: scene 10

- **Filename:** `ai-11-python-for-ai_L10_screen_3.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Type: cities = {}
2. Type: for row in rows: / cities[row["city"]] = cities.get(row["city"], 0) + 1 (indented)

**Narration over this clip (for pacing)**

> Then we count the cities in a dictionary. For each row, get looks up the city's count, starting at zero for a new city, and adds one.

## Clip 4: scene 11

- **Filename:** `ai-11-python-for-ai_L10_screen_4.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Type: with open("summary.txt", "w", encoding="utf-8") as out:
2. Type (indented): out.write(f"Guests: {len(rows)}\n")
3. Type (indented): for city, count in cities.items(): / out.write(f"{city}: {count}\n")
4. Type (not indented): print("Saved summary.txt")
5. Save the file

**Narration over this clip (for pacing)**

> Finally, we open summary dot t x t for writing. We write the total number of guests, then one line for each city and its count. The backslash n in the text starts a new line. At the end, we print a short message.

## Clip 5: scene 12

- **Filename:** `ai-11-python-for-ai_L10_screen_5.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Open the terminal in VS Code
2. Type: python summary.py and press Enter
3. Output: Saved summary.txt
4. Open summary.txt: Guests: 4 / Casablanca: 2 / Quito: 1 / Busan: 1

**Narration over this clip (for pacing)**

> Now we open the terminal and run the script. It prints saved summary. When we open the new file, it shows four guests. Two from Casablanca, one from Quito and one from Busan.

## Production notes for this lesson

- [VERSION] Python and VS Code installation steps, the Python extension, File > Open Folder, how to open the terminal, and whether the command is python or python3 differ by operating system and version. Check against the current official instructions before recording. The demo does not show installation step by step; it starts with both tools installed.
- Screen demo uses VS Code (the brief's tool), not Colab. Record on one operating system and note it in the lesson page.
- Printed output and file content on screen must match content.md: 'Saved summary.txt' and 'Guests: 4 / Casablanca: 2 / Quito: 1 / Busan: 1'.
- Nikolai, the Tbilisi guesthouse, and all guest names and cities are made up. Use a clean user account with no personal files or folder names visible.
