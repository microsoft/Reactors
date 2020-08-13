# Getting Data from an API

Some URLs have JavaScript Object Notation (JSON) that can be used. JSON is one of many ways of representing data. 

Check out the [Pokeman API](https://pokeapi.co/api/v2/pokemon/1/) to see JSON data about Bulbasaur. This means that instead of having your own database about Bulbasaur, you can refer to this link to get more data about Pokemon. How can you use this JSON data to display Bulbasaur's types (grass and poison), its height, and weight onto your website?

Thanks to jQuery, there is a convenient function called `$.get` to perform AJAX (a method of gathering information from another URL without reloading your page). If you were to do this using pure JavaScript (which is how the `$.get` function in jQuery is implemented), you would need to write a lot of code to make AJAX work for the different types and versions of browsers. Thanks, jQuery!

``` html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Gotta Catch'em All</title>
        <script src="https://code.jquery.com/jquery-3.1.0.min.js"></script>
        <script>
            $(document).ready(function(){
                $.get("https://pokeapi.co/api/v2/pokemon/1/", function(res) {
                    console.log(res);
                }, "json");
            })
        </script>
    </head>
    <body>
        <div id="bulbasaur">
        </div>
    </body>
</html>
```

You are using jQuery to load the JSON data that lives in `http://pokeapi.co/api/v2/pokemon/1/` and logging it to the console. 

You are passing three arguments to the `$.get` function.

* The URL that you want to load information from (i.e. `"http://pokeapi.co/api/v1/pokemon/1/"`).
* The function you want to run after information was successfully loaded (i.e. `function(res) { console.log(res) }`).
`$.get` will automatically pass an argument to the function that holds the information from the URL you requested.
You can access this argument by having the function take an argument (i.e. `res`).
You can name this argument anything you want--"data", for example.
* The type of information you are expecting back, which in this case is JSON.

You can [read more about the `$.get` function on W3Schools](https://www.w3schools.com/jquery/ajax_get.asp).

## Traversing JSON

Go ahead and play with the JavaScript object that is logged onto your console. Chrome has done a great job allowing you to traverse through different parts of the object by clicking inside. Let's say you want to display Bulbasaur's types (poison, grass) onto your console. How can you do this?

## Getting Bulbasaur's types

Once you click on the object that is logged in your console, you will see many attributes. One of those attributes is named 'types'. Chrome provides a GUI arrow that specifies that there's more inside. Click the arrow and notice that the 'types' attribute is storing an array of two objects. If you open each of these objects, you see that they both have a 'name' attribute. This looks like the data that you want. How can you traverse the JSON to get here?

```javascript
$.get("https://pokeapi.co/api/v2/pokemon/1/", function(res) {
    console.log(res.types[0].type.name);
    console.log(res.types[1].type.name);
}, "json");
```

The first console.log indicates to go to the 'types' attribute of the object that you got back, which can be referred to as 'res'. Because the 'types' attribute is holding an array of two objects, you are indexing to the first value to grab the first object. Then, you access that object's name attribute to have 'poison' logged to your console. In the second console.log, you are doing the same thing except you are grabbing the second object inside the res.types array. Since you know that res.types is an array, you can rewrite your code using a `for` loop. What if the link you are using updates Bulbasaur and adds another type? Using a `for` loop makes your application more flexible:

```javascript
$.get("https://pokeapi.co/api/v2/pokemon/1/", function(res) {
    for(var i = 0; i < res.types.length; i++) {
        console.log(res.types[i].type.name);
    }
}, "json");
```

## Building HTML

**Hint: Use the code below in your Capstone project.**
What if you wanted to display the JSON data to your website instead of just logging it to your console? You can include the data from the JSON object into your HTML so that website users can see that Bulbasaur's types are poison and grass:

``` html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Gotta Catch'em All</title>
        <script src="https://code.jquery.com/jquery-2.1.3.min.js"></script>
        <script>
            $(document).ready(function(){
                $.get("https://pokeapi.co/api/v2/pokemon/1/", function(res) {
                    var html_str = "";
                    html_str += "<h4>Types</h4>";
                    html_str += "<ul>";
                    for(var i = 0; i < res.types.length; i++) {
                        html_str += "<li>" + res.types[i].type.name + "</li>";
                    }
                    html_str += "</ul>";
                    $("#bulbasaur").html(html_str);
                }, "json");
            })
        </script>
    </head>
    <body>
        <div id="bulbasaur">
        </div>
    </body>
</html>
```

You are passing three arguments to the `$.get` function:

* The URL that you want to load information from (i.e. `"http://pokeapi.co/api/v1/pokemon/1/"`).
* The function you want to run after information was successfully loaded.
You want to build a string that looks like "<h4>Types</h4><ul><li>poison</li><li>grass</li></ul>" and insert its content inside the div with the ID of bulbasaur.
The browser will read the string and render it as HTML when you call $("#bulbasaur").html(html_str).
* The type of information you are expecting back, which in this case is JSON.

NEXT: [Part 5. Capstone Project and Deployment with Azure](../Part%205.%20%20Capstone%20%2B%20Web%20Publishing)
