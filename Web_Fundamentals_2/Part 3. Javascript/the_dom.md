# The Document Object Model

When an HTML (or XML) file is interpreted by a browser, it also generates what we call the Document Object Model (DOM) – a representation of the entire web page as objects. We can manipulate these objects with JavaScript.

W3 Schools has a list of some of the methods and properties of an HTML document: [http://www.w3schools.com/jsref/dom_obj_document.asp](http://www.w3schools.com/jsref/dom_obj_document.asp)

You can think of the document as a big container, inside of which sits information (properties) and instructions (methods). You can access these objects – for example, the body – by calling `document.body`in the console. In other instances, fetching the object requires you to use a built-in method such as `getElementsByTagName`( e.g. `document.getElementsByTagName('div')`). This will return an array of DOM elements.

Each specific element also has a [wealth of methods](http://www.w3schools.com/jsref/dom_obj_all.asp) to exploit.

Open up your browser and right click on a webpage and click "Inspect", from there you should see a tab labeled, "console." Ask your instructor for guidance if you can't find the browser console for Javascript.

Once you're ready, let's play with the DOM a little bit:

Try this in the console:

```javascript
console.log(document.body);
```

Next, try this:

```javascript
var body = document.body;
// this is more fun if it's a random page with stuff already on it (like the learning platform for example).
body. innerHTML = "Hello World";
```

Awesome ---- we are manipulating the DOM using JavaScript. Good work!

Let's try this:

```javascript
var bod = document.body;
for (var i = 0; i < 10; i ++){
  bod. innerHTML += "<p>This has gone through the loop completely: " +i+ " times</p>";
}
```

Lastly, these DOM elements **can listen for events**. After we've placed all the **p**-tags into the body (using the above loop), let's put an event listener on them!

```javascript
var paragraphs = document.getElementsByTagName('p');
console.log(paragraphs);
for (var i = 0; i < paragraphs.length; i ++){
  console.log(paragraphs[i].addEventListener);
  paragraphs[i].addEventListener('click', function(){
    this.style.background='blue';
  });
}
```

Now click on the text in the ```<p>``` tags to see the listener change the color. It's listening for your mouse-click.

Unfortunately, that was a bit tedious (the interface to access and manipulate the DOM is widely viewed as clunky), and it'd be great if there was a more streamlined way to get the job done (more on this later).

This is exactly where _front-end frameworks or libraries_ come in handy. By layering some functionality atop regular JavaScript, the DOM becomes much easier to manipulate. That means faster development and, hopefully, a better end product.

NEXT: [Fat Arrow Functions](./fat_arrow_functions.md)
