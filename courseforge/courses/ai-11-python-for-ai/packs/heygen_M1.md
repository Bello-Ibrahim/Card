# HeyGen Batch Pack: AI-11 M1 (Python Basics in Google Colab)

Course: Python for AI. Make one HeyGen video per lesson below, using these settings for every video.

| Setting | Value |
|---|---|
| Avatar | **Vaness** (standard avatar), ID `1bd001e7e50f421d891986aad5c8bbd2` |
| Voice | `1bd001e7e50f421d891986aad5c8bbd2` (the same ID as the avatar: if HeyGen does not list it as a voice, use Vaness's paired English voice and record its ID in DECISIONS.md) |
| Background | Solid colour **#00FF00** (pure green, no gradient, no image) |
| Resolution | 1080p (1920×1080) |
| Aspect ratio | 16:9 |
| Avatar framing | Centred, head and shoulders, same size in every lesson |
| Captions/subtitles | **Off** (captions are added in Stage 6) |
| Music | Off |
| Speed | Normal (1.0×) |

How to paste: copy the whole text block for a lesson into a single HeyGen scene. Each blank line is a natural pause. Do not add or change words, because the edit is timed to this exact narration.

Save each finished video with the exact filename shown, and upload it to `/incoming/`.

## L01 Welcome to Python and Google Colab

- **Filename:** `ai-11-python-for-ai_M1_L01_presenter.mp4`
- **Expected length:** about 5.3 minutes (735 words). The quality gate accepts ±10%.

```text
Most of the AI tools you hear about were prepared, tested or trained with the same programming language. It is called Python. In the next five minutes, you will write your first line of Python and run it, without installing anything.

Hi, and welcome to Python for AI. This course is for people who have never written code. In this first lesson, we meet Python, and the free tool we will use to write it.

A program is a list of instructions that a computer follows exactly, in order. A programming language is a way to write those instructions, so that both people and computers can read them.

Python is the most common language for data and AI work, for two reasons. First, it is readable. Python code often looks close to plain English. A line that says print, followed by the word hello, does exactly what it says. It shows the word on the screen.

Second, Python has a very large set of free libraries. A library is a package of ready-made code that other people wrote and shared. There are free libraries for tables of data, charts, maths and machine learning. You will use one of them, called pandas, from week three.

We write Python in Google Colab, a free notebook that runs in your web browser. The code runs on a computer owned by Google, so you only need a browser and a Google account.

A Colab notebook is made of cells, and there are two kinds. Code cells hold Python. When you run one, the result appears right below it. Text cells hold notes, headings and explanations, in plain language.

Think of a scientist's lab notebook. On one page, the scientist writes what they plan to test, and why. Next to it, they record the result. In Colab, text cells are the notes, and code cells are the experiments. They sit side by side, so anyone can follow the work later.

Your notebook is saved to your Google Drive. The free version has limits that change, so check the Colab website. And if you cannot use Colab where you live, lesson ten shows how to use Python on your own computer.

Let's try it together. Open the Colab website and sign in with your Google account. Choose New notebook. A notebook opens with one empty code cell. Click the name at the top, and rename it L01 first notebook.

Now click inside the code cell and type two short lines. The first line prints a greeting in Swahili. The second line asks Python to multiply seven by twenty-four.

To run the cell, press Shift and Enter together, or click the round play button on the left. The first run can take a few seconds while Colab connects. And there is our output, right below the cell.

The greeting is inside quotation marks, so Python shows it exactly as written. The second line has no quotation marks, so Python calculates the answer. One hundred and sixty-eight, the number of hours in a week.

Next, choose plus Text to add a text cell. Type a heading, such as My first notebook, and one sentence about what the code does. Then open the File menu and choose Save. The notebook is now in your Google Drive.

One common mistake. Beginners sometimes type code into a text cell, and nothing happens. Text cells never run code. A code cell has a play button on its left, so check before you type. Forgetting the quotation marks around text also causes an error.

And one safety note. Colab notebooks are stored in your Google account, and they can be shared. So never type passwords, ID numbers or other private data into a notebook.

Let's recap. First, Python is widely used for AI because it is readable and has many free libraries for data and machine learning. Second, Google Colab runs Python in your browser. Code cells run code, and text cells hold your notes. Third, you run a cell with Shift and Enter, and the result appears directly below it.

Now it is your turn. In the exercise below this video, you will create your own notebook, print a greeting in your own language, and add a text cell with your name and one goal for this course. It takes about fifteen minutes. In the next lesson, we look at variables and data types. See you there.
```

## L02 Variables and Data Types

- **Filename:** `ai-11-python-for-ai_M1_L02_presenter.mp4`
- **Expected length:** about 5.0 minutes (690 words). The quality gate accepts ±10%.
- **Pronunciation:** No facts to verify (content.md Review Flags: None). Prices and the 10% tax rate are made up; say so on screen as in content.md.

```text
Ask Python to add the text three to the text three, and you get thirty-three, not six. Why? The answer is data types. They explain many of the surprises beginners meet when they work with data.

In the last lesson, you ran your first code in Colab. Today, we learn how Python remembers values. A variable is a name that holds a value. You create one with the equals sign.

Here, the equals sign does not mean is equal to. It means store. We store three point five in a variable called rice price. Later, you can use the name instead of the number, and you can store a new value in it at any time.

Think of a labelled box on a shelf. The label is the name. The box holds one value. When you need the value, you look for the label. You can empty the box and put something new inside, and the label stays the same.

Every value has a data type. The type tells Python what the value is, and what you can do with it. There are four basic types. Int is for whole numbers. Float is for decimal numbers. String, or str, is for text, always inside quotation marks. And bool has only two values, True or False.

You can check a value's type with the type function, and convert it with int, float or str. This matters, because Python treats the text three and the number three very differently. The plus sign adds numbers, but it joins text.

One more thing. Choose names that describe what they hold. Use lowercase letters and underscores. Names cannot start with a number or contain spaces.

Let's see this in a real situation. Wanjiru runs a small food shop in Nairobi. She wants a quick way to total a customer's basket and add a ten percent tax. The prices and the tax rate are made up for this example.

In a new cell, we create four variables. The price of rice, the quantity of rice, the shop name, and whether the shop is open. Then we print the type of each one. The text after the hash sign is a comment. Python ignores it. It is a note for people.

When we run it, Python shows the four types in order. Float, int, str and bool. One of each.

Next, Wanjiru adds four cups of tea. We multiply each price by its quantity and add them to get the subtotal. The tax is ten percent of the subtotal, and the total is the two added together.

To print a clear receipt line, we use an f-string. The letter f before the quotation marks tells Python to put each variable's value inside the text. We also ask for two decimal places, which suits money. Run it, and we see a subtotal of twelve, tax of one twenty, and a total of thirteen twenty.

Finally, the puzzle from the start. We store the text three and add it to itself. Python joins the text and prints thirty-three. When we convert both values to whole numbers first, we get six. And to join a number with text, we convert the number to text with str.

This is the most common mistake. Data from a form, a file or a user is often text, even when it looks like a number. Add text to a number and you get an error. So always check the type, and convert before you calculate.

Let's recap. First, a variable is a name that stores a value, and the equals sign means store this value. Second, the four basic types are int, float, str and bool, and you can check them with type. Third, convert values before you mix text and numbers, and use f-strings to print clear results.

Now it is your turn. In the exercise below this video, you will store the prices and quantities of three items, calculate the total with a ten percent tax, and print a receipt line with an f-string. It takes about twenty minutes. In the next lesson, we look at lists and dictionaries. See you there.
```

## L03 Lists and Dictionaries

- **Filename:** `ai-11-python-for-ai_M1_L03_presenter.mp4`
- **Expected length:** about 4.9 minutes (686 words). The quality gate accepts ±10%.

```text
One variable holds one value. But a real dataset has hundreds of prices, names or cities. So how do you keep many values together under one name? Python has two main answers: lists and dictionaries.

In the last lesson, each variable held one value. Now let's hold many. A list is an ordered collection of values, written inside square brackets. Here is a list of four market stalls: fruit, bread, fish and spices.

Each item has a position, called an index. And here is the surprise. Python starts counting at zero. So position zero is fruit, and position two is fish. A negative index counts from the end, so minus one gives the last item.

A list is like a numbered shopping list. You read it from top to bottom, and you can say, give me item number three. You can add an item at the end with append, replace an item at a position, and count the items with len.

A dictionary is different. It stores pairs of a key and a value, inside curly brackets. You find a value by its key, not by its position. Here, the keys are names, and the values are phone numbers.

Think of the contact book in your phone. You don't scroll to contact number fifty-seven. You type a name, and the phone finds the number. The name is the key, and the number is the value. Two contacts with exactly the same name would be confusing. That is why dictionary keys must be unique.

So when should you use which? Use a list when order matters, or when you have many values of the same kind, like daily sales. Use a dictionary when each value has a label you will look up, like a country and its capital.

Let's try both in Colab. Tomás organises a weekend market in Montevideo, in Uruguay. He keeps a list of stall types and a small contact book of stall holders. All names and numbers are made up.

We create the list of stalls, and print the items at position zero, position two and position minus one. Before I run it, a quick question. What will position two print? Many people say bread, because it is the second item.

Let's run it. Fruit, fish, spices. Position two is fish, because counting starts at zero.

Now we add flowers at the end with append, and replace position one, bread, with cakes. Then we print the whole list and its length. The list now has five items, and cakes sits in position one.

Next, the contact book. We look up Arjun by his name and get his number. Then we add a new contact, Mei, and change Lucía's number. When we print the dictionary, Lucía has her new number and Mei is at the end. The length is three, because len counts the pairs.

Finally, what if a key is missing? We ask for Omar with the get method, and give it a second value to use if he is not there. Python prints not found, instead of stopping with an error.

Watch out for two common mistakes. The first is expecting position one to be the first item. It is position zero. The second is looking up a key that does not exist, which stops your program with an error. Use get when a key might be missing, and remember that keys are case-sensitive.

Let's recap. First, a list is an ordered collection in square brackets, and positions start at zero. Second, a dictionary stores key and value pairs in curly brackets, and you look up values by key. Third, you add or change items by assigning to an index or a key, and len counts them.

Now it is your turn. In the exercise below this video, you will build a dictionary of five countries and their capital cities, look up two of them, add a sixth, and print how many entries it holds. Write down your prediction first. It takes about fifteen minutes. In the next lesson, we learn to make decisions with if, elif and else. See you there.
```

## L04 Making Decisions with if, elif and else

- **Filename:** `ai-11-python-for-ai_M1_L04_presenter.mp4`
- **Expected length:** about 5.0 minutes (702 words). The quality gate accepts ±10%.

```text
A delivery app shows a different price for a short trip and a long one. Somewhere in its code, a program asked a question. Is the distance more than three kilometres? Today, you write that kind of question in Python.

Last time, we stored many values in lists and dictionaries. Now we teach a program to choose. First, you need a condition. A condition is a question whose answer is either True or False.

You build conditions with comparison signs. Two equals signs mean equal to. Remember, one equals sign means store. There are also signs for not equal, less than, greater than, and so on. You can join conditions with and, or, and not.

Here is the structure. An if line, then any number of elif lines, which means else if, and finally an else line. Python checks the conditions from top to bottom. It runs only the block under the first condition that is true, and skips the rest. Else runs only if nothing else was true. You can have many elif lines, or none at all.

Two layout rules. Each of these lines ends with a colon. And the code that belongs to it is moved right by four spaces. In Python, this indentation is not just for looks. It decides which lines belong to which block. A wrong indent changes the meaning, or causes an error. Colab adds the indent for you after a colon.

Picture a security guard checking tickets at a stadium. The first question is, VIP ticket? If yes, you go through the VIP gate, and no more questions are asked. If not, the next question is, standard ticket? If no ticket matches, you are sent to the ticket office. Only one gate opens for each person.

Let's build one. Dewi makes a price calculator for a delivery app in Jakarta. The prices are made up. Up to three kilometres costs eight thousand rupiah. Up to ten kilometres costs fifteen thousand. Anything further costs twenty-five thousand.

In Colab, we set the distance to seven and a half kilometres. Then an if line for three or less, an elif line for ten or less, and an else line for anything further. Each one sets the price. Finally, we print the distance and the price.

Before we run it, let's trace it. Is seven and a half three or less? No, so we skip the first block. Is it ten or less? Yes, so the price becomes fifteen thousand, and else is skipped. Now run it. Seven point five kilometres costs fifteen thousand rupiah.

Notice that the elif line does not need to say more than three. If the distance were three or less, Python would already have stopped at the first block. The order does part of the work.

Next, Dewi adds a long-distance fee, but members don't pay it. The condition says the distance is more than five, and the customer is not a member. The distance part is true, but the member part is false. And needs both, so we see no extra fee.

Now you try. What happens if I change the distance to two? And to twelve? Pause the video, make your prediction, and then watch the result.

A common mistake is putting the conditions in the wrong order. If the ten kilometre check came first, a two kilometre trip would pay fifteen thousand, and the three kilometre band would never be used. Put the smallest range first. And never write one equals sign in a condition, because that causes a syntax error.

Let's recap. First, conditions are True or False. You build them with comparison signs and join them with and, or, and not. Second, Python checks if and elif from top to bottom, and runs only the first block that is true. Third, the colon and the four-space indentation decide which lines belong to each block.

Now it is your turn. In the exercise below this video, you will turn an exam score into a grade band, and predict the output for five test scores before you run the code. It takes about twenty minutes. In the next lesson, we learn how to repeat work with loops. See you there.
```

## L05 Repeating Work with Loops

- **Filename:** `ai-11-python-for-ai_M1_L05_presenter.mp4`
- **Expected length:** about 5.0 minutes (692 words). The quality gate accepts ±10%.

```text
Adding up four numbers by hand is easy. Adding up forty thousand rows of sales is not. Computers are very good at doing the same small job again and again, without getting tired. In Python, the tool for this is the loop.

Last time, our code made decisions. Now it will repeat work. A for loop runs the same block of code once for each item in a collection. Read this example as, for each item in boxes, call it count, and run the indented code.

On the first pass, count is the first item. On the second pass, it is the second item, and so on, until the list ends. Just like if, the line ends with a colon, and the body is indented.

Think of a cashier at a supermarket. The cashier picks up each item in the basket, one after another, scans it, and adds its price to the total. The cashier doesn't need to know how many items there are. When the basket is empty, the cashier stops and shows the total.

That is a very common pattern, called the running total. You create a variable at zero before the loop, and add to it inside the loop. You can also loop over range, which gives a sequence of numbers. It starts at the first number, and stops before the second.

A while loop is different. It repeats as long as a condition stays true. It is useful when you don't know how many passes you need. But be careful. If the condition never becomes false, the loop never ends. In Colab, you can stop a running cell with the stop button next to it.

When is a loop the right tool? Use one when you must do the same steps for every item. For simple totals, Python also has built-in functions, such as sum, max, min and len. They do the loop for you. And in week three, you will see that pandas does most loops for you too.

Let's see a loop in action. Ayşe manages a small textile workshop in İzmir, in Türkiye. She records how many boxes of towels her team packs each day. The numbers are made up.

We store four days of boxes in a list, and set the total to zero. Inside the loop, we add each day's count to the total and print it. After the loop, not indented, we print the average.

Run it. The running total grows from twelve to forty-seven, one line per day. Then the average appears once, eleven point seven five, because that line runs after the loop ends.

Next, a quick look at range and a while loop. The for loop prints day one, day two and day three. Then the stock starts at five, and the while loop takes away two, while the stock is above zero. The result is minus one. Why not zero?

Let's trace it. Five becomes three, then one, then minus one. Only then is the condition false. This is why we trace loops by hand. Finally, the built-in shortcut. Sum and max give forty-seven, and the best day, fifteen.

Here is the most common mistake with loops. It is putting the starting value inside the loop. Then the total resets on every pass, and you only get the last item. Create the total before the loop, update it inside, and use it after. The indentation of each line shows you which of these three places it is in.

Let's recap. First, a for loop runs its indented block once for each item in a list or a range. Second, for a running total, create the variable before the loop, update it inside, and use it after. Third, a while loop repeats while a condition is true, so trace it carefully to check where it ends.

Now it is your turn. In the exercise below this video, you will loop over seven daily sales figures from a café in Lima, and print the weekly total, the average and the best day. It takes about twenty minutes. In the next lesson, we package our logic into functions. See you there.
```
