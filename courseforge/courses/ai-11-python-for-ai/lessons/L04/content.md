# L04 Making Decisions with if, elif and else

Course: AI-11 · Module: M1 · Objectives: O2 · Video: 5 min (screen demo)

## Hook
A delivery app shows a different price for a short trip and a long one. Somewhere in its code, a program asked a question: "Is the distance more than 3 kilometres?" Today you write that kind of question in Python.

## Explanation
A program often needs to choose between actions. In Python you do this with `if`, `elif` ("else if") and `else`.

First you need a **condition**: an expression that is either `True` or `False`. You build conditions with **comparison operators**:

- `==` equal to (two equals signs; one `=` means "store")
- `!=` not equal to
- `<`, `<=`, `>`, `>=` less than, less than or equal to, and so on

You can join conditions with `and` (both must be true), `or` (at least one must be true) and `not` (reverses True and False).

The structure looks like this:

```python
if condition_1:
    action_a
elif condition_2:
    action_b
else:
    action_c
```

Python checks the conditions **from top to bottom** and runs only the block under the **first** condition that is true. It then skips the rest. `else` runs only if no condition was true. You can have many `elif` lines, or none.

Two rules about the layout:

- Each `if`, `elif` and `else` line ends with a colon `:`.
- The code that belongs to it is **indented** (moved right) by 4 spaces. Colab adds the indent for you after a colon. In many languages indentation only makes code easier to read. In Python it decides which lines belong to which block, so a wrong indent changes the meaning or causes an error.

**Analogy:** An `if`/`elif`/`else` chain is like a security guard checking tickets at a stadium. The guard asks the first question: "VIP ticket?" If yes, you go through the VIP gate and no more questions are asked. If not, the next question: "Standard ticket?" If no ticket matches, the `else` gate sends you to the ticket office. Only one gate opens per person.

## Worked Example
Dewi builds a price calculator for a delivery app in Jakarta, Indonesia. The price bands are made up: up to 3 km costs 8,000 rupiah, up to 10 km costs 15,000, and anything further costs 25,000.

The presenter types the code in Colab, but **before** running it, traces it line by line out loud.

```python
distance_km = 7.5
if distance_km <= 3:
    price = 8000
elif distance_km <= 10:
    price = 15000
else:
    price = 25000
print(f"{distance_km} km costs {price} rupiah")
```

Trace: Is 7.5 <= 3? No, so skip the first block. Is 7.5 <= 10? Yes, so `price` becomes 15000. The `else` block is skipped. Now run it:

```
7.5 km costs 15000 rupiah
```

Notice that the second condition does not need to say `distance_km > 3 and distance_km <= 10`. If the distance had been 3 or less, Python would already have stopped at the first block. The order of conditions does part of the work.

Next, Dewi adds a rule that combines conditions: long trips have an extra fee unless the customer is a member.

```python
is_member = True
if distance_km > 5 and not is_member:
    print("Add a long-distance fee")
else:
    print("No extra fee")
```

```
No extra fee
```

`distance_km > 5` is True, but `not is_member` is False, and `and` needs both to be true.

The presenter then changes `distance_km` to 2, then to 12, and asks learners to predict each result before running the cell.

## Common Mistake
The order of conditions matters. Suppose Dewi had written `if distance_km <= 10:` first and `elif distance_km <= 3:` second. A 2 km trip would match the first condition and pay 15,000, and the 3 km band would never be used. Always put the most specific or smallest range first, and trace a few values by hand. A second mistake is writing `=` instead of `==` in a condition, which gives a SyntaxError.

## Key Takeaways
1. Conditions are True or False; build them with `==`, `!=`, `<`, `>`, `<=`, `>=` and join them with `and`, `or`, `not`.
2. Python checks `if` and `elif` from top to bottom and runs only the first block whose condition is true.
3. The colon and the 4-space indentation decide which lines belong to each block.

## Hands-on Exercise
**Task:** Write code that turns an exam score (0–100) into a grade band, then predict the output for 5 test scores before you run it.
**Tools:** Google Colab (free).
**Steps:**
1. Choose made-up bands, for example: 80 or more is "A", 65 or more is "B", 50 or more is "C", and below 50 is "Not yet".
2. Store a score in a variable called `score`, and write an `if`/`elif`/`else` chain that stores the band in `grade`. Print both.
3. In a text cell, write your predicted grade for these scores: 95, 80, 64, 50 and 12.
4. Run the cell once for each score and compare with your predictions.
5. Add a check: if the score is below 0 or above 100, print "Invalid score" instead of a grade.
**What good looks like:** All 5 predictions match the output, including the boundary scores 80 and 50. The invalid-score check catches values such as 120 and -5.
**Time:** about 20 minutes

## Review Flags
- None. The prices, bands and currency amounts are made up, and every output was produced by running the code with Python 3.11.
