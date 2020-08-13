# What Is jQuery?

jQuery is a JavaScript library. What this means to you is that it allows every browser to read JavaScript code. In the same manner, browser compatibility is a big issue when working on the front end. The jQuery code you write can be used by all browsers without change. JavaScript is interpreted differently in some browsers. You don't want to write different versions of your code for different browsers, so cross-browser compatibility is important. All jQuery functions work the same way regardless of the browser.

JQuery also converts long blocks of code into a few lines. As a developer, you should practice the DRY method (Don't Repeat Yourself), which a group of developers discovered after writing the same lines of code repeatedly (and it was a good amount of code!). So, why not cut down on code by making a library and simplifying it for everyone? It sounds like a great idea!

## Tips for jQuery functions

``` html
<head>
<script>
   $(document).ready(function() {
       // your jquery codes here
   });
</script>
</head>
```

Developers don't want jQuery to wait for the document to be fully ready, so insert their jQuery code before the ```</body>``` tag ends.

``` html
<script>
  // your jquery codes here
</script>
</body>
```

Make sure you close open parenthesis and curly brackets where appropriate. Also, use the [Inspect Element](../2_CSS_CSS3/inspect_element.md) frequently to look for javaScript errors in your code.

## Other tips

* You can use .html or .text to retrieve the value. For example, on the bootstrap pricing page:

```javascript
var a = $('h1').html()
console.log(a); // would print "Pricing"
```

* As you read the documentation, you will learn how the same method could be used both to retrieve information (usually if no argument is passed to the method) or to set information (usually by passing additional information to its method).

* You can grab an element by tagging that element with a specific ID.  For example, if you had a button with an ID of 'btn_fade' that hides the paragraphs with a class of 'sp' when the button is clicked, you could write:

```javascript
$('#btn_fade').click(function() {
   $('p.sp').hide();
});
```

* Make sure when you use jQuery that you're very careful where you open the parenthesis and the curly brackets. 
* Always check your browser's [Inspect Console](https://docs.microsoft.com/en-us/microsoft-edge/devtools-guide/console) to detect JavaScript errors. 
* Add `console.log()` statements within the function to ensure that the browser looks at that function when certain events are triggered.

NEXT: [Getting Started with jQuery](./getting_started_jquery.md)
