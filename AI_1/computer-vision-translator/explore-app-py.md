# Exploring app.py

To help focus attention on calling Cognitive Services, we've provided a starter file for your use during the workshop. Some of the work has already been done, and we'll be adding the code to perform tasks like translating text and detecting faces. Let's walk through **app.py** to better understand the structure and what we'll be updating.

## Initial import statements

``` python
import os, base64, json, requests
from flask import Flask, render_template, request

app = Flask(__name__)
```

The import statements at the top are the necessary base components for a [Flask](https://flask.palletsprojects.com/en/1.1.x/) application. `os` will give us access to [environmental variables], and [base64](https://docs.python.org/2/library/base64.html) will allow us to decode images. `json` is a built-in library for working with [JSON](https://docs.python.org/3.7/library/json.html) objects. Finally, [requests] (not to be confused with [request]), is a popular Python library for [making REST and HTTP calls](https://2.python-requests.org/en/master/).

`Flask` will be used to create our Flask app, `render_template` will be used to send [Jinja](https://jinja.palletsprojects.com/en/2.10.x/) templates in response to user requests, and `request` will be used to access the [user request and retrieve form values](https://flask.palletsprojects.com/en/1.1.x/api/?highlight=request#flask.Request).

## dotenv

``` python
# Load system variables with dotenv
from dotenv import load_dotenv
load_dotenv()
```

[dotenv](https://pypi.org/project/python-dotenv/) is a common package across multiple frameworks and languages which simplify the management of environmental variables. Rather than constantly setting keys via the command line, or hard-coding them into the application, dotenv allows you to create a file named **.env** where you store your key/value pairs. Then the library is imported, and `load_dotenv()` will read the values and store them into environmental variables for execution of the application. When deployed to production, you specify the environmental variables like you normally would, like setting [App Settings](https://docs.microsoft.com/azure/app-service/configure-common) in App Services.

## Configure index route

``` python
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
```

`@app.route` is a [decorator](https://www.python.org/dev/peps/pep-0318/) which adds additional meaning to a component immediately following its declaration. In this case, we're specifying `index` will be executed in response to a **GET** call to a route of **/**. In other words, if our site was hosted at **www.contoso.com**, and somone visited **www.contoso.com/** `index` would be executed in response to it. [Routing in Flask](https://flask.palletsprojects.com/en/1.1.x/api/?highlight=route#url-route-registrations) is extremely powerful, and you can both limit and expand how matches are detected, and how to retrieve values the user specifies in the URL.

## Translate

``` python
@app.route("/translate", methods=["GET", "POST"])
def translate():
    # Load image or placeholder
    image = get_image(request)

    # Set the default for language translation
    target_language = "en"
    if request.form and "target_language" in request.form:
        target_language = request.form["target_language"]

    # If it"s a GET, just return the form
    if request.method == "GET":
        return render_template("translate.html", image_uri=image.uri, target_language=target_language)

    # Create a placeholder for messages
    messages = []

    # TODO: Add code to retrieve text from picture

    # TODO: Add code to translate text

    return render_template("translate.html", image_uri=image.uri, target_language=target_language, messages=messages)
```

## translate, train and detect

In the middle of **app.py** you'll notice there's a set of three routes and functions - `translate`, `train`, and `detect`. These are the functions you'll be updating as you add AI functionality to the application. We'll hold off on explaining what's in these functions until we need them.

## Helper function

``` python
def get_image(request):
    from image import Image
    if request.files:
        return Image(request.files["file"])
    else:
        return Image()
```

Down at the bottom of **app.py** you'll notice a function titled `get_image`. When working with images in our application we'll need to perform two tasks - obtain a URI to allow us to display the uploaded image in the page, and to send the image to Cognitive Services. To avoid code duplication, we've created a helper function which uses a helper class `Image`. The code looks to see if there's a file in `request.files`, which is where Flask gives access to files stored in a form. If there is, then it creates an `Image` object with the uploaded file. Otherwise, it simply uses the default.

## Image helper class

``` python
# image.py
import base64

class Image:
    """
    A helper class to wrap an image
    """
    def __init__(self, blob=None):
        self._blob = blob

    @property
    def uri(self):
        """
        Returns the location of the placeholder if no image exists, or dynamically creates a URI for an uploaded image
        """
        # Placeholder default value
        uri = "/static/placeholder.png"
        if self.blob:
            # Convert image to uri
            uri = "data:;base64," + base64.b64encode(self.blob.read()).decode("utf-8")
            # Reset the stream to 0
            self._blob.seek(0)
        return uri

    @property
    def blob(self):
        """
        Returns the blob of the image
        """
        if self._blob:
            # Reset the stream to 0 just in case
            self._blob.seek(0)
        return self._blob
```

Inside of **image.py** is our `Image` helper class. `Image` exposes a `uri` property, which will either return the default placeholder image, or convert the uploaded image into a stream for display on the page. `blob` provides the blob of the image, and will be used to upload the image to Cognitive Services. `seek(0)` is used to reset the stream back to the beginning.

## Summary and next steps

**app.py** represents a small Flask application. From this base structure we will add our functionality. To begin using Cognitive Services, we need to [create the resources we'll be using on Azure](./create-azure-resources.md).
