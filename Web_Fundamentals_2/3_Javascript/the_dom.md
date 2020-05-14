# The Document Object Model

When an HTML file is interpreted by a browser, it generates what we call the Document Object Model (DOM) – a representation of the entire page as objects. We can manipulate these objects with JavaScript. While there are [several methods and properties for the DOM](http://www.w3schools.com/jsref/dom_obj_document.asp), we're going to focus on some of the most common.

You can think of the document as a big container, inside of which sits information (properties) and instructions (methods). You can access these objects – for example, the body – by calling `document.body`. In other instances you may need to fetch the item. For example, if you want to grab all `div` elements, you can ask `document` to do this for you by saying `document.getElementsByTagName('div')`. This will return an array of all your `div` elements. Each specific [element also has a wealth of methods and properties](http://www.w3schools.com/jsref/dom_obj_all.asp) to exploit.

Open up your browser and right click on a webpage and click "Inspect", from there you should see a tab labeled, "console." Ask your instructor for guidance if you can't find the browser console for Javascript.

Once you're ready, let's play with the DOM a little bit:

Try this in the console:

```javascript
console.log(document.body);
```

Next, try this:

```javascript
let body = document.body;
body.innerHTML = "Hello World";
```

And just like that we're manipulating the DOM using JavaScript.

## Creating a page to play with

Let's create a new **html** file, and add the following HTML:

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
    // more to come!!
  </script>
</body>
</html>
```

If you save the file and open it in your browser you'll see three buttons created with very clever names.

### Grabbing items

Let's get all the buttons! We can do this by using the `getElementsByTagName` method we saw earlier. We will print out the number of buttons.

> **NOTE**: For ease of display, we're going to just focus on the `script` tag. The rest of the page will remain the same.

``` javascript
// inside the <script> block
const buttons = document.getElementsByTagName('button');
console.log(buttons.length);
```

Run the page and open the developer tools in the browser. You'll notice it will display **3**, because there are three buttons.

### Adding event handlers

Remember when we were talking about events - those things but we don't know when? Let's see how we can **listen** to an event. The method which will allow us to add a listener to an event is `addEventListener`. It's available on all DOM objects. There are a [long list of events available for DOM objects](https://www.w3schools.com/jsref/dom_obj_event.asp).

`addEventListener` accepts two parameters, the name of the event, and then a [function](basic_functions.md) you wish to execute when the event occurs (sometimes known as the event handler).

Let's create a function for handling our event, and then add a listener to the first button. We're going to **replace all our JavaScript code (everything in the `script` element)**.

``` javascript
// inside the <script> block
function handleButtonClick() {
  console.log('Button was clicked!');
}

const buttons = document.getElementsByTagName('button');
buttons[0].addEventListener('click', handleButtonClick);
```

> **NOTE**: Notice there are **no parenthesis** after `handleButtonClick`. The reason is if we add the parenthesis we would be calling the function we created right away, rather than having the event handler call it.

Save the page, hit refresh, and notice the change. When you click the first button you should see the console displays the message! You've now created an interactive page!

### Adding the handler to all buttons

We've got three buttons. It'd be nice to be able to add it to all buttons without counting 0, 1, 2. After all, what would happen if we added another button?

This is where loops come into play. [Loops](https://www.w3schools.com/js/js_loop_for.asp) allow you to execute the same piece of code multiple times. One of the most common is the [for/of](https://www.w3schools.com/jsref/jsref_forof.asp) loop.

The `for/of` loop will execute for each item in an array. This is helpful for us, because we have an array of buttons. In addition, it will allow us to assign a variable to the current button. So the first time the loop executes, our variable will be the first button, the second time the second button, and so on. This allows us to add the event handler to every button.

Let's update our code and add our `for/of` loop:

``` javascript
// inside the <script> block
function handleButtonClick() {
  console.log('Button was clicked!');
}

const buttons = document.getElementsByTagName('button');
for(button of buttons) {
  button.addEventListener('click', handleButtonClick);  
}
```

Notice the `for of` loop. We're creating a variable called `button` for each button. Then we're calling `addEventListener` just like we did before to add the handler.

Save the page, hit refresh, and see the updates. You'll notice now each time you click any button the console updates!

### Accessing the clicked button

When we were creating our loop we had access to each button. But you'll notice our function of `handleButtonClick` doesn't have a button property. How does `handleButtonClick` know what button the user clicked on?

This is where `this` comes into play! `this` can be a little tricky in JavaScript, as what it actually means will vary depending on where we are. In the case of an event handler, which `handleButtonClick` is, `this` will be whatever raised the event - or in other words, it'll be the button the user clicked on. We can use `this` to then manipulate the clicked button. Let's turn the clicked button text to **red**.

``` javascript
// inside the <script> block
function handleButtonClick() {
  console.log('Button was clicked!');
  this.style.color = 'red';
}

const buttons = document.getElementsByTagName('button');
for(button of buttons) {
  button.addEventListener('click', handleButtonClick);  
}
```

### Updating our page

Up until now we've been writing out to the console. While this is useful for developers, it's not really built for end users. Typically, you want to update the page.

Typically, you will add a placeholder to the page to add information to on the page. It's what we did when we added the `<div id="output"></div>` to our page. We can access an element by its ID by using `document.getElementById`. (Note the casing on `Id`.) Let's update our page one last time (for now), adding in the code to display the button text on the page.

``` javascript
// inside the <script> block
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
```

> **NOTE**: As mentioned previously, [DOM objects have several properties](https://www.w3schools.com/jsref/dom_obj_all.asp) you can manipulate as needed.

## What we learned

Congratulations! You've now built a dynamic web page with JavaScript! There's one last bit of clean-up we'd like to do on our code, which involves [anonymous and fat arrow functions](./fat_arrow_functions.md).
