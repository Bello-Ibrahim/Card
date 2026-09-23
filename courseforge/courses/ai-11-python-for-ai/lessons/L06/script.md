# L06 Functions: Package Your Logic | Presenter Script

Course: AI-11 · Video: 5 min · Words: 680

## Hook
You have already used functions many times. Print, len, sum and type are all functions. Someone else wrote them once, and you use them every day. Today, you write your own.

## Explain
Last time, loops helped us repeat work. Functions help us reuse it. A function is a named block of code that does one job. You define it once, and then you call it, which means run it, as many times as you need.

Here is a function that converts Celsius to Fahrenheit. The word def starts the definition, followed by the name. Inside the brackets is a parameter, called celsius. It is a name for the input the function will receive.

The indented lines are the body. The text in triple quotation marks is a docstring, a short description of what the function does. And return sends the result back to the code that called the function.

When you call it with thirty-five, the value thirty-five is called an argument. Inside the function, celsius becomes thirty-five, and the function returns ninety-five. Return and print are different. Print only shows a value. Return gives it back, so your code can store it, compare it, or use it again.

Think of a function as a recipe card. You write the recipe once, and then cook it many times with different ingredients. The ingredients are the arguments, and the finished dish is the return value. If you improve the recipe, every future meal improves too, because there is only one card to change.

Functions help in three ways. You avoid copying the same code. You give a clear name to a piece of logic. And you can test each piece on its own.

## Demonstrate
Let's write one in Colab. Kwame prepares a weather summary for a travel website that covers cities on three continents. The temperatures are made up.

We type the function with its docstring and run the cell. Notice that nothing is printed. Defining a function only teaches Python the recipe. It does not cook anything yet.

Now we call it in a loop. We have a small dictionary of three cities, Cairo, Oslo and Manila, with their temperatures. The items method gives us each city and its temperature on every pass. For each one, we print the city and the converted value.

Run it. Cairo is ninety-five degrees Fahrenheit, Oslo is twenty-four point eight, and Manila is eighty-seven point eight. One function, called three times.

Next, Kwame writes a second function called describe. It takes a city, a temperature, and a unit. The unit has a default value, F. If the unit is F, describe calls our first function. Otherwise, it keeps the temperature in Celsius. Parameters with default values always come after those without.

We call it twice for Oslo. The first call gives no unit, so it uses the default, and we get Fahrenheit. The second call names the unit as C, which makes the call easy to read. And we get minus four degrees Celsius.

A common mistake is using print inside a function when you mean return. The function shows a value, but gives back nothing, which Python calls None. If you then try to add one to it, you get an error. Use return when the caller needs the result. A second mistake is defining a function and forgetting to call it. Defining teaches Python the recipe. Calling it cooks the meal.

## Recap
Let's recap. First, you define a function with def, a name, parameters and an indented body, and you call it with its name and arguments. Second, return sends a result back to the caller, while print only shows it. Third, default values make parameters optional, and a short docstring explains what the function does.

## CTA
Now it is your turn. In the exercise below this video, you will write a currency conversion function that takes an amount and a rate, and call it for three currencies. Use made-up rates. It takes about twenty minutes. In the next lesson, we learn clean code habits. See you there.

## Thumbnail
Headline: Write Your Own Function
Image: Navy background, a recipe card with an input arrow (35) and an output arrow (95.0), headline in teal Inter Bold.

## Production Notes
- No facts to verify (content.md Review Flags: None). Kwame, the travel website and all temperatures are made up.
- Printed outputs on screen must match content.md exactly: 'Cairo 95.0 / Oslo 24.8 / Manila 87.8' and 'Oslo: 24.8 °F / Oslo: -4 °C'.
- When the definition cell is first run, show clearly that nothing is printed before the loop is added, as described in content.md.
