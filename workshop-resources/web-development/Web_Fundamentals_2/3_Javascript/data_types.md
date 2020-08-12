# Data Types in JavaScript

JavaScript is a [weakly-typed language](https://en.wikipedia.org/wiki/Strong_and_weak_typing), meaning the type of a variable (such as a string or number) is determined at runtime. However, JavaScript does offer support for several types of data.

## Strings

One of the most common data types supported by any language is a string. **A string is a collection of characters**. You indicate a string literal in JavaScript by using quotes, either single `'` or double `"`. It doesn't matter which you use as long as you are consistent.

``` javascript
let name = 'Christopher';
let manager = "Justin";
```

### Concatenation

You will often want to combine (or concatenate) strings. You can perform this operation by using the `+` operator.

``` javascript
let firstName = 'Christopher';
let lastName = 'Harrison';
let fullName = firstName + ' ' + lastName;
```

## Numbers

JavaScript, unlike many other programming languages, supports only one type of number. You can add decimal places to your numbers as you see fit.

``` javascript
let age = 20;
let gpa = 3.87;
```

### Operating on numbers

Numbers in JavaScript support all operations you would expect, including multiplication (`*`), division (`/`), addition (`+`), and subtraction (`-`).

You can also perform exponential functions (`^`) and [Modulo operations](https://en.wikipedia.org/wiki/Modulo_operation) (`%`), where the remainder is returned.

``` javascript
console.log(42 + 206); // 248
console.log(206 - 42); // 164
console.log(5 * 4); // 20
console.log(20 / 4); // 5
console.log(5 ^ 4); // 625
console.log(5 % 2); // 1
```

## Objects

In programming, an [object](https://en.wikipedia.org/wiki/Object_(computer_science)) is a complex data type, meaning it can contain multiple named pieces of information and can potentially have additional means of functionality.

For example, you've seen the ability to create a `firstName` and `lastName` [string variables](#strings). What if you wanted to group those together as a new item, with both `firstName` and `lastName` attached, as opposed to creating them as separate items? Fortunately, you can do that with an object!

There are numerous ways to create objects in JavaScript. One way to do it is by using [JavaScript Object Notation (JSON)](https://en.wikipedia.org/wiki/JSON). As the name implies, JSON is a notation for objects in JavaScript. You can indicate an object with JSON by using the following syntax:

``` javascript
let person = {
    firstName: 'Christopher',
    lastName: 'Harrison'
};
console.log(person.firstName); // Christopher
console.log(person.lastName); // Harrison
```

## Arrays

Arrays are collections of items. In JavaScript, you can create arrays by using the `[]` operator. The core array used in JavaScript is a single column collection of items. You can think of this as a table with one column in a spreadsheet.

``` javascript
let names = []; // empty array
names = ['Justin', 'Christopher']; // pre-populated
```

### Working with arrays

JavaScript offers several operators for working with arrays, including the ability to `sort`, `append`, and access items.

``` javascript
let names = [];

// add names to the end of the array
names.append('Justin');
names.append('Christopher');
// names -> Justin, Christopher

// access the first name (counting starts with 0)
console.log(names[0]);
// prints: Justin

// sort the array
names.sort();
// names -> Christopher, Justin
console.log(names[0]);
// prints: Christopher
```

> **NOTE**: The `sort` method has [side effects](https://en.wikipedia.org/wiki/Side_effect_(computer_science)), meaning it modifies the original object--the array in this case.

It's worth highlighting that you can create an array of any data type, including strings, numbers, objects, and even other arrays.

## What you learned

You explored several data types supported in JavaScript. There are many others available, but these represent the most common data types you'll use when working in JavaScript.

NEXT: [Anonymous Functions](../fat_arrow_functions.md)
