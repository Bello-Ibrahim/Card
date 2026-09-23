# L06 Functions: Package Your Logic

Course: AI-11 · Module: M2 · Objectives: O2, O3 · Video: 5 min (screen demo)

## Hook
You have already used functions many times: `print()`, `len()`, `sum()` and `type()`. Someone else wrote them once, and you use them every day. Today you write your own.

## Explanation
A **function** is a named block of code that does one job. You **define** it once and **call** it (run it) as many times as you need.

```python
def to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32
```

The parts are:

- `def` starts the definition, followed by the function's name and brackets.
- `celsius` is a **parameter**: a name for the input the function will receive.
- The indented lines are the **body**. The text in triple quotation marks is a **docstring**, a short description of what the function does.
- `return` sends a result back to the code that called the function. The function stops at `return`.

When you call `to_fahrenheit(35)`, the value 35 is called an **argument**. Inside the function, `celsius` becomes 35 and the function returns 95.0.

A parameter can have a **default value**, used when the caller does not give one: `def describe(city, celsius, unit="F"):`. Parameters with defaults come after those without.

`return` and `print` are different. `print` only shows a value on the screen. `return` gives the value back so your code can store it in a variable, compare it or pass it to another function. Most useful functions return a value.

**Analogy:** A function is like a recipe card. You write the recipe once: "Take the flour and eggs, mix, bake for 20 minutes." Then you can cook it many times with different ingredients. The ingredients are the arguments, and the finished dish is the return value. If you improve the recipe, every future meal improves too, because there is only one card to change.

Functions help in three ways: you avoid copying the same code, you give a clear name to a piece of logic, and you can test each piece on its own.

## Worked Example
Kwame is preparing a weather summary for a travel website that covers cities on three continents. The temperatures are made up.

The presenter defines the function in one Colab cell, runs it (nothing is printed yet, because defining a function does not run it), and then calls it in a loop:

```python
def to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

for city, temp in {"Cairo": 35, "Oslo": -4, "Manila": 31}.items():
    print(city, to_fahrenheit(temp))
```

```
Cairo 95.0
Oslo 24.8
Manila 87.8
```

`.items()` gives each key and value pair of the dictionary, so the loop receives a city and its temperature on each pass.

Next, Kwame writes a second function that **calls** the first one and has a default value:

```python
def describe(city, celsius, unit="F"):
    if unit == "F":
        return f"{city}: {to_fahrenheit(celsius):.1f} °F"
    return f"{city}: {celsius} °C"

print(describe("Oslo", -4))
print(describe("Oslo", -4, unit="C"))
```

```
Oslo: 24.8 °F
Oslo: -4 °C
```

The first call uses the default `"F"`. The second call gives `unit="C"` by name, which makes the call easy to read.

## Common Mistake
Many beginners use `print` inside a function when they mean `return`. The function then shows a value but gives back `None` (Python's word for "nothing"). If you later write `total = to_fahrenheit(35) + 1`, you get a TypeError, because `None + 1` has no meaning. Use `return` when the caller needs the result. A second mistake is defining a function and forgetting to call it: defining only teaches Python the recipe; calling it cooks the meal.

## Key Takeaways
1. Define a function with `def`, a name, parameters and an indented body; call it with its name and arguments.
2. `return` sends a result back to the caller; `print` only shows it on the screen.
3. Default values make parameters optional, and a short docstring explains what the function does.

## Hands-on Exercise
**Task:** Write a currency-conversion function that takes an amount and a rate (use made-up rates), then call it for 3 currencies.
**Tools:** Google Colab (free).
**Steps:**
1. Define `convert(amount, rate)` with a one-line docstring. It should return `amount * rate`, rounded to 2 decimal places with `round(value, 2)`.
2. Create a dictionary of 3 currency codes and made-up rates, for example `{"EUR": 0.9, "INR": 80.0, "BRL": 5.0}`. Do not rely on these as real exchange rates.
3. Loop over the dictionary and print a line such as "100 USD = 90.0 EUR" for each currency.
4. Add a default value: `rate=1.0`. Call `convert(50)` and explain the result in a text cell.
5. Store one result in a variable and add 1 to it, to confirm that your function returns a number.
**What good looks like:** The function has a clear name and docstring, returns a value (not only prints it), and the 3 printed conversions match the rates you chose. `convert(50)` returns 50.0.
**Time:** about 20 minutes

## Review Flags
- None. All temperatures and currency rates are made up and labelled as such, and every output was produced by running the code with Python 3.11.
