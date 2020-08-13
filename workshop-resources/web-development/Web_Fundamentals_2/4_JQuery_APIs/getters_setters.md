# Getter and Setter Functions

Certain jQuery functions can behave differently depending on whether you run them with parameters. To demonstrate this, look at the following code:

```javascript
<script>
    $(document).ready(function(){
        $('#myParagraph').text();
    });
</script>
<body>
    <p id='myParagraph'>This is my paragraph! </p>
</body>
```

Notice that _myParagraph's_ text will stay the same, even though you know `.text()` can be used to change the text value of HTML elements. This is because when you call the function `.text()` without a parameter, the function will behave as a **getter** function. **A getter function is a function that _gets_ the value of a particular item and returns it**. In this example, the function returns the value of the text of the paragraph called _myParagraph_. To illustrate this, run the following code:

```javascript
<script>
  $(document).ready(function(){
      var myText = $('#myParagraph').text();
      alert(myText);
  })
</script>
<body>
    <p id='myParagraph'> This is my paragraph! </p>
</body>
```

When you load this page, you will see the content of _myParagraph_ in a pop-up box on the screen. Because the function _gets_ the value of a particular item and returns it, you can get the value of the text and assign it to the variable _myText_ that you made.

Another way to use the `.text()` function is as a **setter function, which allows you to set the value of an attribute**. You will probably find yourself using `.text()` in this capacity more so than as a `getter` function. To demonstrate the use of `.text()` as a setter, look at the following code:

```javascript
<script>
  $(document).ready(function(){
      $('button').click(function(){
          $('#myParagraph').text('see how I .text() works as a setter!');
      })
  })
</script>
<body>
    <p id='myParagraph'> This is my paragraph! </p>
    <button> Click me to change the paragraph! </button>
</body>
```

See the difference? By running `.text()` with a value inside of the parentheses, you **set** the value of the selected attribute. This is the difference between using `.text()` as a getter vs. a setter. Use the jQuery documentation to determine if a particular function behaves differently depending on the parameters you choose.
