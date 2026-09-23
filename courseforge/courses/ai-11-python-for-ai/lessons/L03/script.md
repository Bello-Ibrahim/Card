# L03 Lists and Dictionaries | Presenter Script

Course: AI-11 · Video: 5 min · Words: 688

## Hook
One variable holds one value. But a real dataset has hundreds of prices, names or cities. So how do you keep many values together under one name? Python has two main answers: lists and dictionaries.

## Explain
In the last lesson, each variable held one value. Now let's hold many. A list is an ordered collection of values, written inside square brackets. Here is a list of four market stalls: fruit, bread, fish and spices.

Each item has a position, called an index. And here is the surprise. Python starts counting at zero. So position zero is fruit, and position two is fish. A negative index counts from the end, so minus one gives the last item.

A list is like a numbered shopping list. You read it from top to bottom, and you can say, give me item number three. You can add an item at the end with append, replace an item at a position, and count the items with len.

A dictionary is different. It stores pairs of a key and a value, inside curly brackets. You find a value by its key, not by its position. Here, the keys are names, and the values are phone numbers.

Think of the contact book in your phone. You don't scroll to contact number fifty-seven. You type a name, and the phone finds the number. The name is the key, and the number is the value. Two contacts with exactly the same name would be confusing. That is why dictionary keys must be unique.

So when should you use which? Use a list when order matters, or when you have many values of the same kind, like daily sales. Use a dictionary when each value has a label you will look up, like a country and its capital.

## Demonstrate
Let's try both in Colab. Tomás organises a weekend market in Montevideo, in Uruguay. He keeps a list of stall types and a small contact book of stall holders. All names and numbers are made up.

We create the list of stalls, and print the items at position zero, position two and position minus one. Before I run it, a quick question. What will position two print? Many people say bread, because it is the second item.

Let's run it. Fruit, fish, spices. Position two is fish, because counting starts at zero.

Now we add flowers at the end with append, and replace position one, bread, with cakes. Then we print the whole list and its length. The list now has five items, and cakes sits in position one.

Next, the contact book. We look up Arjun by his name and get his number. Then we add a new contact, Mei, and change Lucía's number. When we print the dictionary, Lucía has her new number and Mei is at the end. The length is three, because len counts the pairs.

Finally, what if a key is missing? We ask for Omar with the get method, and give it a second value to use if he is not there. Python prints not found, instead of stopping with an error.

Watch out for two common mistakes. The first is expecting position one to be the first item. It is position zero. The second is looking up a key that does not exist, which stops your program with an error. Use get when a key might be missing, and remember that keys are case-sensitive.

## Recap
Let's recap. First, a list is an ordered collection in square brackets, and positions start at zero. Second, a dictionary stores key and value pairs in curly brackets, and you look up values by key. Third, you add or change items by assigning to an index or a key, and len counts them.

## CTA
Now it is your turn. In the exercise below this video, you will build a dictionary of five countries and their capital cities, look up two of them, add a sixth, and print how many entries it holds. Write down your prediction first. It takes about fifteen minutes. In the next lesson, we learn to make decisions with if, elif and else. See you there.

## Thumbnail
Headline: Lists vs Dictionaries
Image: Navy background, a numbered shopping list on the left and a phone contact card on the right, headline in teal Inter Bold.

## Production Notes
- No facts to verify (content.md Review Flags: None). Tomás, the Montevideo market, and all names and phone numbers are made up.
- Printed outputs on screen must match content.md exactly: 'fruit fish spices', "['fruit', 'cakes', 'fish', 'spices', 'flowers'] 5", '555-0199', "{'Lucía': '555-0150', 'Arjun': '555-0199', 'Mei': '555-0107'}", '3', 'not found'.
- Scene with the stalls[2] question: pause on screen for about two seconds before running the cell, so learners can guess.
