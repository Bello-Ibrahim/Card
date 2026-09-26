# Screen Demo Pack: AI-11 L06 Functions: Package Your Logic

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-11-python-for-ai_L06_screen_1.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Add a new code cell
2. Type: def to_fahrenheit(celsius):
3. Type (indented): """Convert a temperature from Celsius to Fahrenheit."""
4. Type (indented): return celsius * 9 / 5 + 32
5. Press Shift + Enter; no output appears

**Narration over this clip (for pacing)**

> We type the function with its docstring and run the cell. Notice that nothing is printed. Defining a function only teaches Python the recipe. It does not cook anything yet.

## Clip 2: scene 10

- **Filename:** `ai-11-python-for-ai_L06_screen_2.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Below the function, type: for city, temp in {"Cairo": 35, "Oslo": -4, "Manila": 31}.items():
2. Type (indented): print(city, to_fahrenheit(temp))

**Narration over this clip (for pacing)**

> Now we call it in a loop. We have a small dictionary of three cities, Cairo, Oslo and Manila, with their temperatures. The items method gives us each city and its temperature on every pass. For each one, we print the city and the converted value.

## Clip 3: scene 11

- **Filename:** `ai-11-python-for-ai_L06_screen_3.mp4`
- **Target length:** about 11 seconds

**Steps**

1. Press Shift + Enter
2. Output: Cairo 95.0 / Oslo 24.8 / Manila 87.8

**Narration over this clip (for pacing)**

> Run it. Cairo is ninety-five degrees Fahrenheit, Oslo is twenty-four point eight, and Manila is eighty-seven point eight. One function, called three times.

## Clip 4: scene 12

- **Filename:** `ai-11-python-for-ai_L06_screen_4.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Add a new code cell
2. Type: def describe(city, celsius, unit="F"):
3. Type (indented): if unit == "F": / return f"{city}: {to_fahrenheit(celsius):.1f} °F"
4. Type (indented): return f"{city}: {celsius} °C"
5. Highlight unit="F" as the default value

**Narration over this clip (for pacing)**

> Next, Kwame writes a second function called describe. It takes a city, a temperature, and a unit. The unit has a default value, F. If the unit is F, describe calls our first function. Otherwise, it keeps the temperature in Celsius. Parameters with default values always come after those without.

## Clip 5: scene 13

- **Filename:** `ai-11-python-for-ai_L06_screen_5.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Type: print(describe("Oslo", -4))
2. Type: print(describe("Oslo", -4, unit="C"))
3. Press Shift + Enter
4. Output: Oslo: 24.8 °F / Oslo: -4 °C

**Narration over this clip (for pacing)**

> We call it twice for Oslo. The first call gives no unit, so it uses the default, and we get Fahrenheit. The second call names the unit as C, which makes the call easy to read. And we get minus four degrees Celsius.

## Production notes for this lesson

- No facts to verify (content.md Review Flags: None). Kwame, the travel website and all temperatures are made up.
- Printed outputs on screen must match content.md exactly: 'Cairo 95.0 / Oslo 24.8 / Manila 87.8' and 'Oslo: 24.8 °F / Oslo: -4 °C'.
- When the definition cell is first run, show clearly that nothing is printed before the loop is added, as described in content.md.
