# Anonymous functions

In the [prior example](./the_dom.md), we saw how we could create a function and make it an event handler. Commonly, this is short-handed by using an anonymous function. An anonymous function is a function which doesn't have a name.

## Creating an anonymous function

Let's bring back the full page we were using previously:

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

Our `handlebuttonClick` was only ever used inside the event handler. Let's make our code a little more succinct by creating the function right inside of `addEventListener`. The way we do this is by using the syntax of `function() { }`, and put the same logic inside of the `{ }`:

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

If you save the page and run it again you'll notice we see the same behavior as before.

### Fat arrow functions

ES6 introduced a new shorthand syntax for anonymous functions known as a **fat arrow function**. A fat arrow is represented as `=>`. We create a fat arrow function by leaving off the word `function`, and instead using the syntax of `() => { }`, where our code is placed inside of the `{ }`. Let's update our code one last time:

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

Save the page, refresh in the browser, and you'll notice the same output!

### Why use fat arrow functions

When you first see a fat arrow function it looks a little weird. You might be wondering why to use it at all. Fat arrow functions allow you to create code which is more succinct, and in the long run more readable. It's especially helpful in scenarios where we might want to do something requiring a very small amount of code.

Let's consider the [filter](https://www.w3schools.com/jsref/jsref_filter.asp) function of a JavaScript array. `filter` allows you to find items which meet the criteria you specify by using a function. `filter` will loop through each item, pass it into the function, and then return an array filled with all the items which match the logic you provide.

Let's take the following array:

``` javascript
const names = ['Christopher', 'Justin', 'Sarah', 'Shana', 'Meaghan'];
```

Let's say we wanted to find all the names longer than 6 characters. We could do this by testing the `length` of each item to see if it's greater than 6. A function which would perform such a task would look like this:

``` javascript
function checkLength(name) {
  return name.length > 6;
  // return means send the result back
}
```

As highlighted earlier, we'd like to avoid creating a function which is only being used in one specific instance, especially if it's only containing one line of code.

In addition, fat arrow functions allow us to take certain shortcuts. `filter` is looking for a return value. JavaScript will help us out by performing this for us, so we can leave off the `return` statement. Our fat arrow function for the `checkLength` function would look like this:

``` javascript
(name) => name.length;
```

If we bring this all together, we can use `filter` inline with the rest of our code, so it takes up a little less space.

``` javascript
const names = ['Christopher', 'Justin', 'Sarah', 'Shana', 'Meaghan'];
const longNames = names.filter((name) => name.length > 6);
console.log(longNames);
```

If you run this code in a tool like [CodePen](https://codepen.io) you'll see the new `longNames` array only contains Christopher and Meaghan.

## Conclusion

Arrow functions provide a syntax with implicit returns for succinct expressions. They allow for the ability to create functions "on the fly", without having to have code all over the place for short operations.

But we don't have to write everything ourselves. We can always take advantage of other [libraries and frameworks](./javascript_libraries.md).
