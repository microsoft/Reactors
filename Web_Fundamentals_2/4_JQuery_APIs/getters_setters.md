# Getters/setters

Certain jQuery functions can behave differently depending on whether or not you run them with parameters. To demonstrate this, let's use the following code:

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

Notice that _myParagraph's_ text will stay the same, even though we know `.text()`can be used to change the text value of HTML elements. This is because when we call the function `.text()` without a parameter, the function will behave as what is called a **getter** function. This function will actually return the value of the text of the paragraph called _myParagraph_. To illustrate this, let's run the following code:

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

When you load this page now, you will see the content of _myParagraph_ in a pop-up box on the screen. The use of the term 'getter function' means that the function **gets**the value of a particular item and returns it, which is why we were able to get the value of the text and assign it to the variable _myText_that we just made.

The other way to use the `.text()` function is as a **setter** function. You will probably find yourself using **`.text()`**in this capacity more so than as a **`getter`**. To demonstrate the use of `.text()` as a setter, look at the following code:

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

See the difference? By running **`.text()`** with a value inside of the parentheses, we **`set`**the value of the selected attribute. This is the difference between using**`.text()`**as a getter and a setter. Use the jQuery documentation to figure out if a particular function behaves differently depending on the parameters you execute it with!
