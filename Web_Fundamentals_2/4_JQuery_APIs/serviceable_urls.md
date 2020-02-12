# Serviceable URLs & Traversing JSON

Any URL on the Internet can be used to make our websites better. Remember that URLs are just a human-friendly way to identify the location of the computer that holds the data we're looking for. The data we found can be a few different things, either an HTML page, an image, a video, JavaScript libraries or JSON (more on that later).

## Pages

Some URLs lead you to a page. For example, if you navigate to  <https://www.microsoft.com> your browser will render the landing page of MIcrosoft. You navigated to a URL and that URL rendered HTML, CSS, and JavaScript as its response. The browser interprets the HTML, CSS, and JavaScript to display a complete page.

## Images

Some URLs only hold an image. For example, if you navigate to (please copy and paste the link, hotlinking has been prohibited by this API):

`raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png`

your browser will render a picture of Bulbasaur. Now that we know that the link contains a picture of a Bulbasaur, we can use that URL to make our website better. We can include the image of Bulbasaur on our website by including an img tag to our website:

`<img src="raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png"> <!-- add http:// before the website name -->`

## Videos

Some URLs only hold a video. We can include this video on our website by including a video tag to our website:

`<video src="http://a1068.v.phobos.apple.co..." controls></video>`

## CDN

Some URLs hold useful code. CDNs (Content Distribution Network or Content Delivery Network) is a fancy way of saying that. For example, if you navigate to  <https://code.jquery.com/jquery-2.1.3.js> you will see the code for jQuery.

We can include this code on our website by using a script tag:

`<script src="https://code.jquery.com/jquery-2.1.3.js"></script>`

## Request Response

How many requests do you think this web page will send? Load the code into a browser, open up the developer console, click on the network tab, and refresh the page.

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>HTTP Request Response</title>
    <script src="https://code.jquery.com/jquery..."></script>
  </head>
  <body>
    <img src="raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png" alt="bulbasaur"><!-- add http:// before the website name -->
    <video
      src="http://a1068.v.phobos.apple.co..."
      controls></video>
  </body>
</html>
```

To load this page, the browser had to make 4 GET requests. First to GET the page. Then as it was reading the page it saw that we are including jQuery's CDN. So the browser makes another GET request to get the code located in the URL specified in the src attribute and includes it on the page. Then the browser has to send another GET request when it realizes the img tag's source is located in the pokeapi URL. Finally, the browser makes another GET request to load the video located in the URL provided in the video element's src attribute.
