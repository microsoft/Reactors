# Basic Functions

## How JavaScript is executed

JavaScript is read like a set of instructions. When the file or script is run, the interpreter starts with the first line, and runs whatever it sees. Let's create the following HTML file, and see what happens.

``` html
<html>
<head>
    <title>Sample</title>
</head>
<body>
    <script>
        document.write('Hello, world');
    </script>
</body>
</html>
```

If you save the file and open it in a browser, what do you see? You should see **Hello, world** displayed on your browser window!

## Delaying execution

One thing we discussed previously is the desire to respond to events. We would like to be able to execute code in response to something happening - a value changing, a user clicking on a button, the page loading. We need to be able to write a block of code and not have it be executed right away, but rather only when we call on it. This is what a [function](https://www.w3schools.com/js/js_functions.asp) is all about.

## Introducing functions

A **function** is, at its most basic, a block of code with a name. And it won't be executed until we decide we want to call it. Let's update our file from before, and put our code into a function.

``` html
<html>
<head>
    <title>Sample</title>
</head>
<body>
    <script>
        function displayMessage() {
            document.write('Hello, world');
        }
    </script>
</body>
</html>
```

If you save the file, and hit refresh, you're going to notice nothing is displayed on the page.

### Breaking down our function

Let's start with the syntax, and then circle back to what's happening.

One common way to create a function is to use the keyword `function`. If we take a look at the first line of our script, we're going to see we used `function` to create our function. Immediately after the word `function`, you'll notice we said `displayMessage`. This now becomes the name of the function.

Functions aren't executed until they're called. We call the function by calling its name. Let's update our code to call the function:

``` html
<html>
<head>
    <title>Sample</title>
</head>
<body>
    <script>
        function displayMessage() {
            document.write('Hello, world');
        }
        // new line
        displayMessage();
    </script>
</body>
</html>
```

If we take a look at our code, we'll notice a new line (identified by the comment of **new line**). There's where we call the function! If you save the file, and hit refresh, you'll notice the page now displays **Hello, world**.

## Making our function reusable

Right now our function is pretty static; the only thing it can do is display **Hello, world**. What happens if I'd like it to display other messages?

This is where parameters come into play. A parameter is an additional piece of information we can send into a function.

A parameter behaves an awful lot like a variable for a function. We add a parameter by adding a name inside the `( )`:

``` javascript
function displayMessage(message) {
    // message will automatically be set to
    // whatever the user passes into the function
    document.write(message);
}
```

You'll notice we added `message` into our `displayMessage`. As highlighted by the comments, it will automatically store the value the user passes in. So, how does someone pass in a value? They specify it between the `( )` when calling the function.

``` javascript
displayMessage('This is the parameter message');
```

Go ahead and update your code, save the file, and refresh the page. What do you notice? You should see the new message.

## What we learned

We've seen how we can create functions, which are reusable, named blocks of code. Functions are probably the most understated yet most powerful tool in any developer's toolkit.

You likely noticed the use of the [document](https://www.w3schools.com/jsref/dom_obj_document.asp) object, and might be wondering what it is. The `document` is the core object for accessing the HTML. Let's [explore our document](./the_dom.md) next.
