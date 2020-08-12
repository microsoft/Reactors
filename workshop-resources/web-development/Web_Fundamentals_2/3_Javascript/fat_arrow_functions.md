# Anonymous Functions

In the [prior example on DOM](./the_dom.md), you saw how you could create a function and make it an event handler. Commonly, this is shorthanded by using an anonymous function. **An anonymous function is a function that doesn't have a name**.

## Creating an anonymous function

Let's bring back the full page you were using previously:

``` html
<html>
<head>
  <title>Demo page</title>
<body>
  <button type="button">Button One</button>
  <button type="button">Button Two</button>
  <button type="button">Button Three</button>
  <div id="output"></output>
  <script>
    function handleButtonClick() {
      console.log('Button was clicked!');
      this.style.color = 'red';
      buttonText = this.innerText;
      message = 'You clicked ' + buttonText;
      document.getElementById('output').innerText = message;
    }

    const buttons = document.getElementsByTagName('button');
    for(button of buttons) {
      button.addEventListener('click', handleButtonClick);  
    }
  </script>
</body>
</html>
```

`handlebuttonClick` was only used inside the event handler. Let's make the code more succinct by creating the function inside of `addEventListener`. You do this by using the syntax `function() { }` and applying the same logic inside of `{ }`:

``` javascript
// Replace the contents of the script block
const buttons = document.getElementsByTagName('button');
for(button of buttons) {
  button.addEventListener('click', function() {
    console.log('Button was clicked!');
    this.style.color = 'red';
    buttonText = this.innerText;
    message = 'You clicked ' + buttonText;
    document.getElementById('output').innerText = message;
  });  
}
```

If you save the page and run it again, you'll notice the same behavior as before.

### Fat arrow functions

ES6 introduced a new shorthand syntax for anonymous functions, known as a **fat arrow function**. A fat arrow is represented as `=>`. You create a fat arrow function by removing the word `function` and instead using the syntax of `() => { }`, where your code is placed inside of `{ }`. Let's update the code one last time:

``` javascript
// Replace the contents of the script block
const buttons = document.getElementsByTagName('button');
for(button of buttons) {
  button.addEventListener('click', () => {
    console.log('Button was clicked!');
    this.style.color = 'red';
    buttonText = this.innerText;
    message = 'You clicked ' + buttonText;
    document.getElementById('output').innerText = message;
  });  
}
```

Save the page, refresh the browser, and you'll notice the same output!

### Why use fat arrow functions

When you first see a fat arrow function, it looks odd. You might be wondering why you'd use it at all. Fat arrow functions allow you to create code which is more succinct, and in the long run more readable. It's especially helpful in scenarios where you want to do something requiring a very small amount of code.

Let's consider the [filter method](https://www.w3schools.com/jsref/jsref_filter.asp) of a JavaScript array. `filter` allows you to find items that meet the criteria you specify by using a function. `filter` will loop through each item, pass it to the function, and then return an array filled with the items that match the logic you provided.

Take the following array:

``` javascript
const names = ['Christopher', 'Justin', 'Sarah', 'Shana', 'Meaghan'];
```

Imagine you want to find all names longer than 6 characters. You could do this by testing the `length` of each item to see if it's greater than 6. A function that would perform this task would look like this:

``` javascript
function checkLength(name) {
  return name.length > 6;
  // return means send the result back
}
```

As highlighted earlier, you want to avoid creating a function that is only being used in one instance, especially if it only contains one line of code.

In addition, fat arrow functions allow you to take certain shortcuts. `filter` is looking for a return value. JavaScript will help by performing this so you can leave off the `return` statement. The fat arrow function for the `checkLength` function would look like this:

``` javascript
(name) => name.length;
```

To bring this together, use `filter` inline with the rest of your code, so it takes up less space.

``` javascript
const names = ['Christopher', 'Justin', 'Sarah', 'Shana', 'Meaghan'];
const longNames = names.filter((name) => name.length > 6);
console.log(longNames);
```

If you run this code in a tool like [CodePen](https://codepen.io), you'll see the new `longNames` array only contains Christopher and Meaghan.

## What you learned

Arrow functions provide a syntax with implicit returns for succinct expressions. They allow you to create functions "on the fly", without placing code all over the place for short operations.

NEXT: You don't have to write everything yourself. You can take advantage of [JavaScript Libraries and Frameworks](./javascript_libraries.md).
