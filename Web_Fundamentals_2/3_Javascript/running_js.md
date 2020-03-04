# Running JavaScript

To be able to learn JavaScript, first we need to be able to run JavaScript. JavaScript is an interpreted language, meaning it needs an interpreter to parse through our code and turn it into actions for the computer. As a client-facing scripting language, JavaScript is most comfortable running in a browser. You can do this one of three ways.

## Online Interpreters

If you need to write and test just a few lines of JavaScript, an online interpreter can be a good option. [JavaScriptFiddle](https://JavaScriptfiddle.net/), [JavaScriptbin](http://JavaScriptbin.com/?JavaScript,console), and [CodePen](http://codepen.io/) are a few examples. These can be great for algorithm challenges!

Every online interpreter will have its own interface, just make sure you have an area to write code and a console to read outputs.

## Browser Console

We can also run JavaScript right out of the browser console. This can be useful for debugging, however it will only interpret JavaScript one input at a time, rather than running an entire file.

![console](../images/browser_console.png)

This is also where we will read the majority of our console messages.

## Adding JavaScript to a page

When just getting started, we recommend writing `.html` files and including your JavaScript in a `script` tag. You will need to do this to complete some of the assignments in the JavaScript chapter, and it's the best representation of how client side JavaScript actually performs. This is also the JavaScript you are already familiar with!

``` html
<html>
<head>
  <script>
        console.log('Hello, world!');
    </script>  
</head>
<body>
</body>
</html>
```

### Breaking down the code

`console.log` is probably the most common way to write some information out for developers. It uses the `log` function of the [`console`](https://www.w3schools.com/jsref/obj_console.asp) object to write out to the console in the browser's developer toolkit. Because it's sort of "tucked away", it can be a nice place to leave little notes for debugging or other purposes.

> **NOTE**: Remember, you should never put sensitive information into JavaScript or into the `console`. Always assume the user can see what you're writing!

## What we learned

We saw how we can add JavaScript into a page. But there's of course more to the story. Let's explore JavaScript's close cousin [ECMAScript & ES6](./es6.md)
