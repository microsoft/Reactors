# Streamline Code with `$(this)`

Consider the following HTML code:

``` html
<img src="image1.jpg" />
<img src="image2.jpg" />
<img src="image3.jpg" />
<img src="image4.jpg" />
<img src="image5.jpg" />
```

Let's say that you want your app to remove an image when a user clicks on it. How would you do this?

One way is to change your HTML by adding a unique ID for each image and a jQuery code as shown below:

``` html
<html>
<head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
    <script>
        $(document).ready(function(){
            $('#image1').click(function(){
                $('#image1').hide();
            });
            $('#image2').click(function(){
                $('#image2').hide();
            });
            $('#image3').click(function(){
                $('#image3').hide();
            });
            $('#image4').click(function(){
                $('#image4').hide();
            });
            $('#image5').click(function(){
                $('#image5').hide();
            });
        });
    </script>
</head>
<body>
    <img src="image1.jpg" id="image1" />
    <img src="image2.jpg" id="image2" />
    <img src="image3.jpg" id="image3" />
    <img src="image4.jpg" id="image4" />
    <img src="image5.jpg" id="image5" />
</body>
```

But the above code is redundant! What if there is a way to choose the element within the selector that triggered the event? And there is! It's called `$(this)`. `$(this)` selects the element that triggered that event. Using this, element, you can clean up the code:

``` html
<html>
<head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
    <script>
        $(document).ready(function(){
        //attach a click event listener to all the img tags when the document is ready
            $('img').click(function(){
                $(this).hide();
            });
        });
    </script>
</head>
<body>
    <img src="image1.jpg" />
    <img src="image2.jpg" />
    <img src="image3.jpg" />
    <img src="image4.jpg" />
    <img src="image5.jpg" />
</body>
```

This is an example of how to streamline your jQuery code and never write the same code twice. By leveraging the power of the `$(this)` selector, you can cut down the lines of code you need.
