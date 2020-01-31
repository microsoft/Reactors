# Introduction to AJAX and Fetch API

In this section let's learn how to fetch data asynchronously from an external API using web technologies like AJAX and Fetch API.

## Fetching resources and data from an API

### AJAX

AJAX stands for Asynchronous Javascript and XML(eXtensible Markup Language). We will be using  JSON(Javascript Object Notation) instead of XML so our acronymn could be AJAJ for Asychronous Javascript and JSON. AJAX is a technology that we can use to change a webpage without having to reload the entire page. This is happening all the time on our websites and is how we can have different things happening dynamically on a webpage based on an event that the user will trigger while on the page. Along with returning XML and JSON data, AJAX can also be configured to return plain text.

### How AJAX works

1. The user triggers and event on a webpage and the browser creates a request.
2. The server receives the request and prepares the data it will return to the user via a response that is sent back to the browser.
3. The browser, using JavaScript, takes the data from the response and updates the webpage in the user's browser.

In other words, a request is sent by making an AJAX call and data in JSON format is being returned asynchronosly from the remote server and the website user is viewing is updated without having to reload the webpage. There are thousands of public and private APIs, AJAX can be used to fetch data from any of them.

Let's try our first AJAX call using in the code below to get data from Dog API, an external API with AJAX. This API is free and we can use it without a key. You can also submit a picture of your dog!

## A request uses a URL with some parameters

Here is an API call that will return a random picture of a dog. Copy and paste the URL below into your browser.

[https://dog.ceo/api/breeds/image/random](https://dog.ceo/api/breeds/image/random)
The parameters for this call are the `../api/breeds/image/random` part of the URL above. This request tells the Dog API Server to use the API, and return a `random` `image` of any `breed` of dog.

## Here's the JSON response

```json
{
    "message": "https://images.dog.ceo/breeds/keeshond/n02112350_4122.jpg",
    "status": "success"
}
```

## AJAX using jQuery

We will be using AJAX in the next section with the help of a JavaScipt library called jQuery

Consider the code for a simple webpage below. First we have to make sure we have added jQuery with the Microsoft CDN using this code `<script src="https://ajax.aspnetcdn.com/ajax/jquery/jquery-1.9.0.min.js"></script>`
Notice how there is a `.click` function, that's the event that triggers the request for the dog picture. jQuery goes out and gets the picture and then returns it, in this case we take the first part of the JSON response and put it in an `img` tag so we can render it as an image with: `$("#div2").html('<img src="' + result.message + '">');`

See it working here on Codepen: <https://codepen.io/dannyooooo/pen/rNaEmKo>

```html
<!DOCTYPE html>
<html>
<head>
<script src="https://ajax.aspnetcdn.com/ajax/jquery/jquery-1.9.0.min.js"></script>
<script>
$(document).ready(function(){
  $("button").click(function(){
    $.ajax({url: "https://dog.ceo/api/breeds/image/random", success: function(result){
      $("#div2").html('<img src="' + result.message + '">');
    }});
  });
});
</script>
</head>

<body>
<div id="div1"><h2>Let jQuery AJAX Change This Text</h2></div>
<hr>
<div id="div2"> [Dog picture goes here.] </div>
<hr>
<button>Get External Content</button>
</body>
</html>
```

## AJAX using the Fetch API

The Fetch API is the newest way to fetch resources from other web services and content providers, without the need for using jQuery. Let's look at some code:

See it working here at Codepen: <https://codepen.io/dannyooooo/pen/MWYMmNL>

```javascript
fetch('https://dog.ceo/api/breeds/image/random') //call the fetch function
    .then(response => response.json()) //response type JSON -- Check out the ES6 Arrow Function!
    .then(data => console.log(data.message)); //output the data to the console log
```

## AJAX Notes

You can use either of these methods to fetch your remote data. I like the simplicity of the Fetch API but there are several ways to do API calls that are not here. All APIs differ in some ways, so you need to consult the APIs documentation so you can know what to expect!

NEXT: [Javascript Libraries](./javascript_libraries.md)
