# Basic Functions

## How JavaScript is executed

JavaScript is read like a set of instructions. When the file or script is run, the interpreter starts with the first line, and runs whatever it sees. Let's create the following HTML file and see what happens.

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

If you save the file and open it in a browser, what do you see? You should see **Hello, world** displayed in your browser window!

## Delaying execution

Something discussed previously was the desire to respond to events. You want to execute code in response to an action: a value changing, a user clicking a button, the page loading. We need to write a block of code without it immediately executing, but rather when we call on it. This is what a [function](https://www.w3schools.com/js/js_functions.asp) is all about.

## Introducing functions

A **function** is, at its most basic level, a block of code with a name. Functions aren't executed until they are called. 

Update your file from before, and place your code into a function:

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

If you save the file and refresh your screen, you'll notice that nothing is displayed on the page.

### Breaking down your function

Let's start with the syntax, and then circle back to what's happening.

One common way to create a function is to use the keyword `function`. If you look at the first line of our script, you'll see `function` was used to create the function. Immediately after the word `function`, you'll notice `displayMessage`. This becomes the name of the function.

Functions aren't executed until they're called. You call the function by calling its name. 

Now, update your code to call the function:

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

If you look at the code, you'll notice a new line (identified by the comment **new line**). This is where you call the function. If you save the file and refresh your screen, you'll notice the page now displays **Hello, world**.

## Making your function reusable

Right now your function is static; the only thing it can do is display "Hello, world". What happens if you want it to display other messages?

This is where parameters come into play. A **parameter is an additional piece of information we can send into a function**.

A parameter behaves much like a variable for a function. You add a parameter by adding a name inside the `( )`:

``` javascript
function displayMessage(message) {
    // message will automatically be set to
    // whatever the user passes into the function
    document.write(message);
}
```

You'll notice  `message` was added into `displayMessage`. As highlighted by the comments, it will automatically store the value the user passes in. So, how does someone pass in a value? They specify it between the `( )` when calling the function:

``` javascript
displayMessage('This is the parameter message');
```

Update your code, save the file, and refresh the page. What do you notice? You should see the new message.

## What you learned

You've seen how to create functions--reusable, named blocks of code. Functions are probably the most understated yet most powerful tool in a developer's toolkit.

You likely noticed the use of the [document](https://www.w3schools.com/jsref/dom_obj_document.asp) object, and might be wondering what it is. The `document` is the core object for accessing the HTML. 

NEXT: Time to explore your document using the [Document Object Model (DOM)](./the_dom.md).
