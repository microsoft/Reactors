# Names and variables

## Naming things in JavaScript

One of the core things you'll do in any language, including JavaScript, is name things - functions, classes, variables, etc. JavaScript has a few set rules about naming, and a few conventions we should follow.

### The rules

Variable names must start with a letter or an underscore (\_). After the first letter, they can contain letters, numbers or underscores.

### The conventions

- The conventions vary depending on what you're naming. For our purposes, everything will be [camelCased](https://en.wikipedia.org/wiki/Camel_case), meaning the first word will be lower case, and any following word will start with an upper case letters.
- We won't use single letters for variables. When naming items we should be as descriptive as possible to make our code more readable.

## Variables in programming

One constant through all programming languages is the need to store information while an application is running. You might ask the user for their name, read the price of a stock, or calculate a value for use later. The way we store values is by the use of a **variable**.

If you've never worked with a variable before, you actually have. (Yes, you read the previous sentence correctly.) If you remember back to various math classes, you undoubtedly equations questions which looked like this:

> `42 + x = 206`

`x` was a placeholder for a value, in this case 164. In programming the same thing is true - variables are placeholders for values.

### Variables in JavaScript

Variables in JavaScript are declared in one of three ways - `const`, `let`, and `var`.

#### var

`var` is the traditional way to declare variables in JavaScript. `var` is short for **variable** as you might expect. Put `var` in front of the variable name, and away you go.

``` javascript
var name = 'Christopher';
```

#### let

Introduced with ES6, `let` is a relatively new way to declare variables. It behaves much in the same way as `var`, but overcomes some of `var`'s shortcomings. To declare a variable using `let`, you do the same thing as you did with `var`.

``` javascript
let name = 'Christopher';
```

#### const

`const` behaves like `let` and `var`, except it doesn't allow the variable to be reassigned - it becomes constant (thus the name `const`). `const` is advantageous because it can help you avoid any bug where you accidentally try to reassign a variable.

The main thing to note about `const` is only reassignment is prohibited. You can still call methods to update the state of the item.

``` javascript
const name = 'Christopher';
name = 'Justin'; //this fails

const names = ['Christopher'];
// Christopher is stored in the array
names.push('Justin')
// Justin and Christopher are stored in the array
```

##### The problem with var

In JavaScript, one creates [blocks](https://en.wikipedia.org/wiki/Block_(programming)) of code by using `{` and `}`. Normally, a block defines [scope](https://en.wikipedia.org/wiki/Scope_(computer_science)), or the region in which the variables created are available. Typically, the following happens:

``` java
// sample code in Java, not JavaScript

if (true) {
    int x = 42;
}

// x is no longer available
```

Unfortunately, JavaScript doesn't behave that way when using `var`. In JavaScript, variables declared inside some scopes (but not all to make things even more confusing) are still available outside of them. So in JavaScript, the following works:

``` javascript
if (true) {
    var x = 42;
}
// x is still available!!!!
```

## What we learned

We saw how we can store values in memory in JavaScript, and how we can name them. Let's talk a little about [data types](./data_types.md).
