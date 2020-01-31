# What is jQuery

jQuery is a JavaScript library. What this means for us is that it allows every browser to read JavaScript code. In the same manner, browser compatibility is a big issue when working on the front-end. This means that the jQuery code you write is suited for use by all browsers without change. Javascript is interpreted differently in some browsers. We don't want to have to write different versions of our code for different browsers, so cross-browser compatibility is important. All of the jQuery's functions work the same way regardless of which browser the user is running.

JQuery also converts what would have been a long block of code into just a few lines. As a developer, you should always practice the DRY method (Don't Repeat Yourself) which a group of developers discovered when they wrote the same lines of code over and over again (and it was a good amount of code too!). So, why not cut down many lines of code by making a library, and also by simplifying it for everyone? It sounds like a great idea!

## Overview of basic jQuery functions

```html
<head>
<script>
   $(document).ready(function() {
       // your jquery codes here
   });
</script>
</head>
```

Other developers don't want jQuery to wait for the document to be fully ready, and insert their jQuery codes just before the ```</body>``` tag ends.

```html
<script>
  // your jquery codes here
</script>
</body>
```

Please make sure you're closing all the open parenthesis and curly brackets in all the appropriate places. Also, use Inspect Element frequently to see if there are any javascript errors in your codes.

## Other tips that may be helpful

You can also use .html or .text to retrieve/get the value.  For example on the bootstrap pricing page

```javascript
var a = $('h1').html()
console.log(a); // would print "Pricing"
```

As you go through the documentation, you can learn more about how the same method could be used to retrieve information (usually if no argument is passed to the method) or to set information (usually by passing some additional information to its method).

You could also grab a specific element by tagging that element with a specific id.  For example, if you had a button with an id of 'btn_fade' that hides all the paragraphs with a class of 'sp', when the button is clicked, you could do:

```javascript
$('#btn_fade').click(function() {
   $('p.sp').hide();
});
```

Please make sure whenever you use jQuery, you're very careful where you open the parenthesis and the curly brackets. Always check your browser's [inspect console](https://docs.microsoft.com/en-us/microsoft-edge/devtools-guide/console) to see if it caught any Javascript errors and also add `console.log()` statements within the function to ensure that the browser is even going inside that function when certain events are triggered.

NEXT: [Getting Started with jQuery](./getting_started_jquery.md)
