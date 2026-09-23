# L02 Variables and Data Types

Course: AI-11 · Module: M1 · Objectives: O1 · Video: 5 min (screen demo)

## Hook
Type `"3" + "3"` into Python and you get `33`, not `6`. Why? The answer is data types, and they explain many of the surprises beginners meet when working with data.

## Explanation
A **variable** is a name that holds a value. You create one with the equals sign:

```python
rice_price = 3.50
```

Read this as "store 3.50 in a variable called `rice_price`". The equals sign here means "store", not "is equal to". Later you can use the name instead of the number, and you can store a new value in it at any time.

**Analogy:** A variable is like a labelled box on a shelf. The label is the name, such as `rice_price`. The box holds one value. When you need the value, you look for the label, not the contents. You can empty the box and put something new in it, and the label stays the same.

Every value has a **data type**. The type tells Python what the value is and what you can do with it. The four basic types are:

- **int**: whole numbers, such as `2`, `0` or `-15`.
- **float**: decimal numbers, such as `3.50` or `0.1`.
- **str** (string): text, always inside quotation marks, such as `"Nairobi"` or `"3"`.
- **bool** (Boolean): only two values, `True` or `False`.

Use `type()` to check a value's type. Use `int()`, `float()` and `str()` to convert a value to another type. This matters because Python treats `"3"` (text) and `3` (a number) very differently. `+` adds numbers, but it joins text.

Variable names should describe what they hold. Use lowercase letters and underscores, such as `tea_qty`. Names cannot start with a number or contain spaces.

## Worked Example
Wanjiru runs a small food shop in Nairobi, Kenya. She wants a quick way to total a customer's basket and add a 10% tax. The prices and the tax rate are made up for this example.

The presenter types each line in a new Colab cell and runs it.

```python
rice_price = 3.50      # float
rice_qty = 2           # int
shop_name = "Duka La Wanjiru"   # str
is_open = True         # bool
print(type(rice_price), type(rice_qty), type(shop_name), type(is_open))
```

```
<class 'float'> <class 'int'> <class 'str'> <class 'bool'>
```

The text after `#` is a **comment**. Python ignores it; it is a note for people.

Next, she adds tea and calculates the total:

```python
tea_price = 1.25
tea_qty = 4
subtotal = rice_price * rice_qty + tea_price * tea_qty
tax = subtotal * 0.10
total = subtotal + tax
print(f"{shop_name}: subtotal {subtotal:.2f}, tax {tax:.2f}, total {total:.2f}")
```

```
Duka La Wanjiru: subtotal 12.00, tax 1.20, total 13.20
```

The `f` before the quotation marks makes an **f-string**. Python replaces each name inside curly brackets `{}` with its value. `:.2f` means "show 2 decimal places", which suits money.

Finally, she checks what happens with text that looks like a number:

```python
typed = "3"
print(typed + typed)
print(int(typed) + int(typed))
print("Items: " + str(rice_qty + tea_qty))
```

```
33
6
Items: 6
```

## Common Mistake
Beginners often mix text and numbers. Data that comes from a form, a file or a user is often text, even when it looks like a number. If you add two text values, Python joins them (`"33"`). If you add text and a number, you get a TypeError. Always check the type with `type()` and convert with `int()` or `float()` before you calculate. In week 3 you will see the same problem in real datasets, where a column of prices is stored as text.

## Key Takeaways
1. A variable is a name that stores a value; `=` means "store this value".
2. The four basic types are int, float, str and bool. Check them with `type()`.
3. Convert with `int()`, `float()` and `str()` before mixing text and numbers, and use f-strings to print clear results.

## Hands-on Exercise
**Task:** Store the prices and quantities of 3 items in variables, calculate the total with a 10% tax, and print a receipt line with an f-string.
**Tools:** Google Colab (free).
**Steps:**
1. Create a new code cell. Choose 3 items that a shop in your area might sell, with made-up prices.
2. Create 6 variables with clear names, such as `bread_price` and `bread_qty`.
3. Calculate `subtotal`, `tax` (10% of the subtotal) and `total` in separate variables.
4. Print one receipt line with an f-string that shows all three values with 2 decimal places.
5. Use `type()` to check the type of one price and one quantity.
6. Store one quantity as text, such as `"2"`, and convert it with `int()` before you use it.
**What good looks like:** The cell runs without errors, the names describe the values, and the printed total equals the subtotal multiplied by 1.10. Money values show 2 decimal places.
**Time:** about 20 minutes

## Review Flags
- None. All prices and the tax rate are labelled as made up, and every code output was produced by running the code with Python 3.11.
