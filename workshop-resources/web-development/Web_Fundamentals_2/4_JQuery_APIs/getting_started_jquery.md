# Getting Started with jQuery

1. To get started with jQuery, go to [Microsoft jQuery Releases on the CDN](https://docs.microsoft.com/en-us/aspnet/ajax/cdn/overview#jQuery_Releases_on_the_CDN_0) and copy the link. This is the URL the browser will use to import the library. 

2. In the `<head>` portion of your HTML document, include the link you copied:

`<script src="https://ajax.aspnetcdn.com/ajax/jquery/jquery-1.9.0.js"></script>`

Notice that what you are doing is adding a **'source' attribute** to your JavaScript. You are effectively telling the page "Take all the code hosted at this URL and allow me to use it on this page." **Also, notice you added an `http://` in front of the URL. You must do this!!!**

3. Open a new `<script>`tag and type the following:

`console.log($)`

The `$` is how you access the jQuery library. Everything you do with jQuery has to be preceded by `$`. 

4. You can utilize jQuery by adding () to the end of `$`:

`console.log($())`

The `$()` is how you select an HTML tag. If you were to select the tag, you would write `$('body')`. This selector can grab any HTML tag; you will learn the different ways you can grab HTML items.

```javascript
$('body').click(function(){
    // more code will go here
});
```

```javascript
$(document).ready(function(){
 });
```

Inside the curly brackets of the function above is where you insert **all** the jQuery functions. This code tells the browser to execute the jQuery functions when the document itself is ready. "Ready" means when the document is fully loaded. **This is very important: If you don't use the `ready()` function, your code will run before the HTML content you wrote gets rendered--meaning, the browser will run code for HTML that doesn't yet exist.**

## The basic flow of jQuery

1. Select the _element, class_, or _id_ using the jQuery selector.
2. Add an event listener: How do you want this event to be triggered?
3. Write the code instructing what you want to happen when the event is triggered.

NEXT: [Activity: Debugging jQuery](./debugging_jquery.md)
