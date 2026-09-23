# L03 Lists and Dictionaries

Course: AI-11 · Module: M1 · Objectives: O1, O2 · Video: 5 min (screen demo)

## Hook
One variable holds one value. But a real dataset has hundreds of prices, names or cities. How do you keep many values together under one name? Python has two main answers: lists and dictionaries.

## Explanation
A **list** is an ordered collection of values inside square brackets:

```python
stalls = ["fruit", "bread", "fish", "spices"]
```

Each item has a **position**, called an **index**. Python starts counting at 0, so `stalls[0]` is `"fruit"` and `stalls[2]` is `"fish"`. A negative index counts from the end: `stalls[-1]` is the last item. Lists can change: `append()` adds an item at the end, and `stalls[1] = "cakes"` replaces the item at position 1. `len(stalls)` gives the number of items.

A list is like a numbered shopping list. You read it from top to bottom, and you can say "give me item number 3".

A **dictionary** stores **key: value** pairs inside curly brackets. You find a value by its key, not by its position:

```python
phone_book = {"Lucía": "555-0142", "Arjun": "555-0199"}
```

`phone_book["Arjun"]` gives `"555-0199"`. To add a pair or change a value, assign to a key: `phone_book["Mei"] = "555-0107"`. Keys must be unique. If you assign to a key that already exists, the old value is replaced.

**Analogy:** A dictionary is like the contact book in your phone. You do not scroll to "contact number 57". You type a name, and the phone finds the number. The name is the key and the phone number is the value. Two contacts with exactly the same name would be confusing, which is why dictionary keys must be unique.

When should you use which?

- Use a **list** when order matters, or when you have many values of the same kind: daily sales, a list of cities.
- Use a **dictionary** when each value has a label you will look up: a country and its capital, a product and its price.

## Worked Example
Tomás organises a weekend market in Montevideo, Uruguay. He keeps a list of stall types and a small contact book of stall holders. All names and numbers are made up.

The presenter runs each cell in Colab and explains the output before running the next.

```python
stalls = ["fruit", "bread", "fish", "spices"]
print(stalls[0], stalls[2], stalls[-1])
stalls.append("flowers")
stalls[1] = "cakes"
print(stalls, len(stalls))
```

```
fruit fish spices
['fruit', 'cakes', 'fish', 'spices', 'flowers'] 5
```

Before running the cell, the presenter pauses and asks: "What will `stalls[2]` print?" Many learners say "bread", because it is the second item. The answer is "fish", because counting starts at 0.

Now the contact book:

```python
phone_book = {"Lucía": "555-0142", "Arjun": "555-0199"}
print(phone_book["Arjun"])
phone_book["Mei"] = "555-0107"    # add a new pair
phone_book["Lucía"] = "555-0150"  # change an existing value
print(phone_book)
print(len(phone_book))
print(phone_book.get("Omar", "not found"))
```

```
555-0199
{'Lucía': '555-0150', 'Arjun': '555-0199', 'Mei': '555-0107'}
3
not found
```

`len()` counts the key: value pairs. `get()` is a safe way to look up a key: if the key is missing, it returns the second value you give it instead of stopping with an error.

## Common Mistake
The most common mistake is an off-by-one error: expecting `stalls[1]` to be the first item. Remember that the first item is at index 0 and the last is at index `len(stalls) - 1`. A second mistake is looking up a dictionary key that does not exist, such as `phone_book["Omar"]`. This stops the program with a KeyError. Use `get()` when a key might be missing. Keys are also case-sensitive: `"lucía"` and `"Lucía"` are different keys.

## Key Takeaways
1. A list is an ordered collection in square brackets; positions start at 0.
2. A dictionary stores key: value pairs in curly brackets, and you look up values by key.
3. Add or change items by assigning to an index or key, and use `len()` to count them.

## Hands-on Exercise
**Task:** Build a dictionary of 5 countries and their capital cities, look up two of them, add a sixth, and print how many entries it holds.
**Tools:** Google Colab (free).
**Steps:**
1. Create a dictionary called `capitals` with 5 countries from at least 3 continents as keys and their capital cities as values.
2. Before you run anything, write down what `len(capitals)` will print.
3. Print the capitals of 2 countries by looking them up by key.
4. Add a sixth country and its capital.
5. Print `len(capitals)` and check that your prediction was correct after adding the sixth item.
6. Try `capitals.get("Atlantis", "unknown")` and explain the result in a text cell.
**What good looks like:** The cell runs without errors, prints 2 correct capitals and then the number 6. Country names are spelled the same way in the dictionary and in the lookups.
**Time:** about 15 minutes

## Review Flags
- None. The names and phone numbers are made up, and every output was produced by running the code with Python 3.11. Learners supply the country and capital pairs themselves.
