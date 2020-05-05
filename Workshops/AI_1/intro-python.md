# Overview of Python

> **NOTE:** If you want to follow along with the class, you'll need to [install Python](./install-python.md) and [the starter site](./install-starter.md).

Since its first release in 1991, Python has risen to become a popular general-purpose programming language. Because Python is easy to pick up for programmers familiar with other languages, this section provides only a quick overview of the specific Python syntax we will use to create our website.

We assume you have programmed in another language, such as Java, JavaScript, or C#. Python supports many of the same features as those languages, while the syntax will be different. We won't explain what an `if` statement is, but we'll show how to create one in Python.

Let's start by taking a look at variables.

## Variables

Unlike many other languages, Python has no keyword used for declaring variables. To declare a variable you simply assign it to its first value.

``` Python
country = 'France'
```

## Compound data types

Python has a number of compound data types used to group together other values. We will use two of them to build this website: [lists](https://docs.python.org/3.7/library/stdtypes.html#typesseq-list) and [dictionaries](https://docs.python.org/3.7/library/stdtypes.html#mapping-types-dict).

### Lists

One of the most versatile compound data types in Python are lists. Lists can be written as a sequence of comma-separated values inside square brackets. Lists might contain items of different types, but typically all items will be the same type.

``` python
scores = [100,90,94]
```

Python also includes functions which are available to all lists. For example, [append()](https://docs.python.org/3.7/tutorial/datastructures.html) allows you to add items to the end of your list.

``` python
scores = [100,90,94]
scores.append(88)
print(scores)

# output:
[100,90,94,88]
```

### Dictionaries

Another Python data type that we will use in this hands-on section are dictionaries. Dictionaries in Python provide a means of mapping information between unique keys and values. You create dictionaries by listing zero or more key-value pairs inside of braces, similar to [JSON](https://en.wikipedia.org/wiki/JSON).

``` python
capitals = {
    'France': 'Paris',
    'Germany': 'Berlin'
}
```

## Control flow expressions

Although Python has a number of control flow expressions familiar to programmers coming from other languages, we will use only two in this section: the [if](https://docs.python.org/3/tutorial/controlflow.html#if-statements) statement and the [for](https://docs.python.org/3/tutorial/controlflow.html#for-statements) loop.

### If statements

If statements in Python are similar to those in other programming languages like Java, and they will form the backbone of the logical flow of our Python coding in this section.

``` python
index = 5
if index % 2 == 0:
    print('Even')
else:
    print('Odd')

# output
Odd
```

> **Note:** Unlike many other languages, Python does not use any syntax to denote the boundaries of control such as `{}` or `End If`. Instead, Python blocks are based on tab levels.

### For loops

To iterate through a collection of items, Python offers `for` loops.

``` python
scores = [100,90,94]
for score in scores:
    print(score)

# output:
100
90
94
```

## Functions

As in other programming languages, it is often essential in Python to break down programs into reusable chunks. A primary means of doing that is through functions. For example, we could create a function to print the values in a list.

``` python
def print_list(list):
    for score in scores:
        print(score)

scores = [100,90,94]
print_list(scores)

# output:
100
90
94
```

> **Note:** You'll notice again indentation denotes blocks. Python also has a rather well defined style convention defined by [PEP 8](https://www.python.org/dev/peps/pep-0008/). [Naming is different than many languages](https://www.python.org/dev/peps/pep-0008/#function-and-variable-names); function and variable names should be lower case, with words separated by underscores.

## Exception handling

You can write Python programs to handle selected [exceptions](https://docs.python.org/3/tutorial/errors.html). Consider the following example, which asks the user for input until a valid integer has been entered. (Note that although we don’t use it in producing the website in this section, this while loop helps illustrate how exception-handling works in Python.)

``` python
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Invalid number. Try again")
```

This `try` statement works as follows:

1. Python runs the `try` clause (the statements between the try and except keywords).
2. If no exception occurs, Python skips the except clause and completes execution of the `try` statement.
3. If an exception occurs during execution of the `try` clause, Python skips the rest of the clause. If its type matches the exception named after the except keyword (in this case, `ValueError`), Python runs the except clause and then continues executing after the `try` statement.
4. If an exception occurs that does not match the exception named in the except clause, it is passed on to any outer `try` statements. If no handler is found there, Python halts execution and passes an unhandled exception.

## Importing modules

Python stores definitions for later use in another program in files called [modules](https://docs.python.org/3/tutorial/modules.html). Python uses this syntax to import a module into a program:

``` python
# Import the entire module
# All components in the module will be
# in the namespace flask
import flask

# import specific items from a module
from flask import render_template
```

## Summary and next steps

We've highlighted some of the most common pieces of syntax in Python, and in this course. Using this knowledge you can continue to grow your Python skills, and begin looking at frameworks like [Flask](./intro-flask.md).
