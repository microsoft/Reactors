# URL Types and Usages

Any URL on the Internet can be used to make your websites better. Remember that a URL is simply a human-friendly way to identify the location of the computer that holds the data you seek. The data can take many forms--an HTML page, an image, a video, a JavaScript library or JSON (more on that later).

## Pages

Some URLs lead you to a page. For example, if you navigate to  <https://www.microsoft.com>, your browser will render the landing page for Microsoft. You navigated to a URL and that URL rendered HTML, CSS, and JavaScript as its response. The browser interprets the HTML, CSS, and JavaScript to display a complete page.

## Images

Some URLs only hold an image. For example, navigate to (Please copy and paste the link below. Hotlinking has been prohibited by this API):

`raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png`

Your browser will render a picture of Bulbasaur. Now that you know the link contains a picture of Bulbasaur, you can use that URL to make your website better. You can include the image of Bulbasaur on your website by including an `img` tag:

`<img src="raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png"> <!-- add http:// before the website name -->`

## Videos

Some URLs only hold a video. You can include this video on your website by including a video tag:

`<video src="http://a1068.v.phobos.apple.co..." controls></video>`

## Content delivery network (CDN)

Some URLs hold useful code. CDN (also called content distribution network) is a fancy way of saying that. For an example, [look at the code for jQuery](https://code.jquery.com/jquery-2.1.3.js).

Now, include this code on your website by using a script tag:

`<script src="https://code.jquery.com/jquery-2.1.3.js"></script>`

## Request response

How many requests do you think this web page will send? Load the code into a browser, open the developer console, click the Network tab, and refresh the page.

``` html
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

To load this page, the browser made four Get requests. First, to get the page. As the page loaded, the browser detected jQuery's CDN and made another Get request to retrieve the code from the URL specified in the `src` attribute and include it on the page. The browser sent another Get request upon realizing the `img` tag's source is located in the pokeapi URL. Finally, the browser made the fourth Get request to load the video from the URL in the video element's `src` attribute.
