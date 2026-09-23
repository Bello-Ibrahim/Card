# L02 Variables and Data Types | Presenter Script

Course: AI-11 · Video: 5 min · Words: 695

## Hook
Ask Python to add the text three to the text three, and you get thirty-three, not six. Why? The answer is data types. They explain many of the surprises beginners meet when they work with data.

## Explain
In the last lesson, you ran your first code in Colab. Today, we learn how Python remembers values. A variable is a name that holds a value. You create one with the equals sign.

Here, the equals sign does not mean is equal to. It means store. We store three point five in a variable called rice price. Later, you can use the name instead of the number, and you can store a new value in it at any time.

Think of a labelled box on a shelf. The label is the name. The box holds one value. When you need the value, you look for the label. You can empty the box and put something new inside, and the label stays the same.

Every value has a data type. The type tells Python what the value is, and what you can do with it. There are four basic types. Int is for whole numbers. Float is for decimal numbers. String, or str, is for text, always inside quotation marks. And bool has only two values, True or False.

You can check a value's type with the type function, and convert it with int, float or str. This matters, because Python treats the text three and the number three very differently. The plus sign adds numbers, but it joins text.

One more thing. Choose names that describe what they hold. Use lowercase letters and underscores. Names cannot start with a number or contain spaces.

## Demonstrate
Let's see this in a real situation. Wanjiru runs a small food shop in Nairobi. She wants a quick way to total a customer's basket and add a ten percent tax. The prices and the tax rate are made up for this example.

In a new cell, we create four variables. The price of rice, the quantity of rice, the shop name, and whether the shop is open. Then we print the type of each one. The text after the hash sign is a comment. Python ignores it. It is a note for people.

When we run it, Python shows the four types in order. Float, int, str and bool. One of each.

Next, Wanjiru adds four cups of tea. We multiply each price by its quantity and add them to get the subtotal. The tax is ten percent of the subtotal, and the total is the two added together.

To print a clear receipt line, we use an f-string. The letter f before the quotation marks tells Python to put each variable's value inside the text. We also ask for two decimal places, which suits money. Run it, and we see a subtotal of twelve, tax of one twenty, and a total of thirteen twenty.

Finally, the puzzle from the start. We store the text three and add it to itself. Python joins the text and prints thirty-three. When we convert both values to whole numbers first, we get six. And to join a number with text, we convert the number to text with str.

This is the most common mistake. Data from a form, a file or a user is often text, even when it looks like a number. Add text to a number and you get an error. So always check the type, and convert before you calculate.

## Recap
Let's recap. First, a variable is a name that stores a value, and the equals sign means store this value. Second, the four basic types are int, float, str and bool, and you can check them with type. Third, convert values before you mix text and numbers, and use f-strings to print clear results.

## CTA
Now it is your turn. In the exercise below this video, you will store the prices and quantities of three items, calculate the total with a ten percent tax, and print a receipt line with an f-string. It takes about twenty minutes. In the next lesson, we look at lists and dictionaries. See you there.

## Thumbnail
Headline: Why Is 3 + 3 = 33?
Image: Navy background, two text blocks "3" + "3" = 33 next to 3 + 3 = 6, headline in teal Inter Bold.

## Production Notes
- No facts to verify (content.md Review Flags: None). Prices and the 10% tax rate are made up; say so on screen as in content.md.
- Wanjiru and 'Duka La Wanjiru' in Nairobi are fictional; do not show a real shop name or logo in stock footage.
- Printed outputs on screen must match content.md exactly: "<class 'float'> <class 'int'> <class 'str'> <class 'bool'>", 'Duka La Wanjiru: subtotal 12.00, tax 1.20, total 13.20', and '33 / 6 / Items: 6'.
- Screen demo: the presenter types each code block from content.md into a new Colab cell, including the # comments, and runs it.
