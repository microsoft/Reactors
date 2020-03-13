# Getting Started

To get started with jQuery, go to [Microsoft's jQuery Releases on the CDN](https://docs.microsoft.com/en-us/aspnet/ajax/cdn/overview#jQuery_Releases_on_the_CDN_0) and copy the link from there. This is the address we will tell our browser to import the library from. Next, in the `<head>` portion of your HTML document, include the link you just copied:

`<script src="https://ajax.aspnetcdn.com/ajax/jquery/jquery-1.9.0.js"></script>`

Notice that what we are doing is adding a **'source' attribute** to our JavaScript. We are effectively telling our page: "take all the code hosted at this URL and allow me to use it on this page." **Also, notice we added an `http://` in front of the URL. You must do this!!!**

Next, open a new `<script>`tag and type the following:

`console.log($)`

The `$` is how we access the whole jQuery library. Everything we do with jQuery has to be preceded by a `$`. Next, you can utilize jQuery by adding () to the end of our `$`.

`console.log($())`

The `$()` is how we select an HTML tag. If we were to select the tag, we would have to write `$('body')`. This selector can grab any HTML tag, we will go into the different ways we can grab HTML items.

```javascript
$('body').click(function(){
    // more code will go here
});
```

```javascript
$(document).ready(function(){
 });
```

Inside the curly brackets of the function above is where you are to insert **all** of the jQuery functions. This code tells the browser to execute the jQuery functions when the document itself is ready. By _'ready'_, we mean when the document is fully loaded. This is **very important** because if you don't use this `ready()` function, your code will run before the HTML content you wrote gets rendered--meaning, the browser will run code for HTML that doesn't exist yet.

## **Keep in mind the basic flow of using jQuery:**

1. **Select the _element, class_ or _id_ using the jQuery selector.**
2. **Add an event listener: How do you want this event to be triggered?**
3. **Write the code on what you want to happen when the event is triggered.**

NEXT: [Activity: Debugging jQuery](./debugging_jquery.md)
