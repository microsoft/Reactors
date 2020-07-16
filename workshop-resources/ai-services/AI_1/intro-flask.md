# Flask fundamentals

> **NOTE:** If you want to follow along with the class, you'll need to [install Python](./install-python.md) and [the starter site](./install-starter.md).

[Prerequisite: Python fundamentals](./intro-python.md)

To quote the [creators](https://palletsprojects.com/p/flask/):

> "Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks."

Flask is a perfect framework for quickly creating web front ends. Unlike a framework like [Django](https://www.djangoproject.com/) which, while powerful, is rather [opinionated](https://stackoverflow.com/questions/802050/what-is-opinionated-software), Flask is lightweight and designed to allow developers to focus on their solution code rather than the framework. Put simply, Flask just gets out of your way. :-)

## Introducing Flask

Every Flask application has an entry point file, commonly called `app.py`. The simplest Flask application would print *Hello world* for the user, and would look like this:

``` python
# Load Flask
from flask import Flask

# Create the app
app = Flask(__name__)

# Add a route
@app.route("/")
# Define what happens when someone visits the page
def index():
    # Return some content to the user
    return "<h1>Hello, world</h1>"
```

The first statement imports a class named `Flask` from the `flask` package installed with `pip`. The second statement instantiates that class to create a `Flask` app and assigns it to the variable named `app`.

The fourth and fifth statements define a function that’s called when the user requests the site’s home page—for example, *http://www.contoso.com/*. The preceding statement - `@app.route("/")` is a decorator which will map the route */* (or the root) to the function. The function name is unimportant, but index is commonly used as the name for the function that renders the site’s home page.

> **Note:** By default, Flask will look for a file named `app.py` when starting. If you wish to use a different starter file, you can indicate this by setting an environment variable named `FLASK_APP`.

## Routing in Flask

Suppose that your website contains several pages rather than just one. You can use `@app.route()` to map all of the routes that the site supports to functions that render the corresponding pages:

``` python
from flask import Flask

app = Flask(__name__)

# Define a route for the app's home page
@app.route("/")
def index():
    return "<h1>This is the home page</h1>"

# Define a route for the app's About page
@app.route("/about")
def about():
    return "<h1>This is the About page</h1>"

# Define a route for the app's Contact Us page
@app.route("/contact")
def contact():
    return "<h1>This is the Contact Us page</h1>"
```

If the app is hosted at www.contoso.com, it now supports the following URLs:

- www.contoso.com/
- www.contoso.com/about
- www.contoso.com/contact

You can continue adding routes and functions until all of the pages that your site supports are accessible by URL. To reiterate, the function names are unimportant; it’s the routes that really count.

## HTML templates

You typically don’t want to include inline HTML in the functions that render your site’s pages. Instead, you want to define those pages in HTML files.

Flask contains a function named `render_template()` that looks for HTML files in a subdirectory named “templates” and renders them out to the page. The following example produces the exact same output as the previous example. It assumes that the directory in which `app.py` is located has a subdirectory named “templates” containing HTML files named `index.html`, `about.html`, and `contact.html`:

``` python
from flask import Flask, render_template

app = Flask(__name__)

# Define a route for the app's home page
@app.route("/")
def index():
    return render_template("index.html")

# Define a route for the app's About page
@app.route("/about")
def about():
    return render_template("about.html")

# Define a route for the app's Contact Us page
@app.route("/contact")
def contact():
    return render_template("contact.html")
```

Why is the function named `render_template()`? Because it can do more than simply load static HTML files. It also allows you to pass it user-defined variables and inject their values into the page at runtime. You could, for example, place a file named master.html in the “templates” subdirectory and include the following markup in it:

``` html
<h1>{{ message }}</h1>
```

You could then write **app.py** as such:

``` python
from flask import Flask, render_template

app = Flask(__name__)

# Define a route for the app's home page
@app.route("/")
def index():
    return render_template("master.html", message="This is the home page")

# Define a route for the app's About page
@app.route("/about")
def about():
    return render_template("master.html", message="This is the About page")

# Define a route for the app's Contact Us page
@app.route("/contact")
def contact():
    return render_template("master.html", message="This is the Contact Us page")
```

Flask uses the [Jinja template engine](https://jinja.palletsprojects.com/en/2.10.x/templates/) for dynamically rendering pages, such as the `{{ message }}` example above. Jinja supports additional syntax for creating powerful dynamic pages.

### Control flow expressions in Jinja

In the above example, `{{ }}` was used to contain a string which was added to the HTML. With Jinja you can add dynamic code by using `{% %}`. You can add `if` statements to your HTML templates by using the following:

``` html
{% if message %}
    <h1>{{ message }}</h1>
{% else %}
    <h1>No message specified</h1>
{% endif %}
```

Control flow statements are frequently used in conjunction with Flask’s `flash()` function to display error messages. Let’s say you encounter an error condition in **app.py** and want to display a message to the user in a JavaScript alert box. Here’s **app.py**, complete with a statement to initialize the app's `secret_key` property with a random number, which is required for flashing messages:

``` python
# inside app.py
import os
from flask import Flask, render_template, flash

app = Flask(__name__)
app.secret_key = os.urandom(1)

# Define a route for the app's home page
@app.route("/")
def index():
    flash("This is an error message")
    return render_template("index.html")
```

And inside **index.html**:

``` html
{% with messages = get_flashed_messages() %}
    {% if messages %}
        <script type="text/javascript">
            window.alert("{{ messages[0] }}");
        </script>
    {% endif %}
{% endwith %}
```

This example assumes that just one error message was flashed, but you can call `flash()` multiple times to queue up several messages and enumerate them with a `{%` for message in messages `%}` statement. For more information on message flashing in Flask, see [Message Flashing](http://flask.pocoo.org/docs/1.0/patterns/flashing/).

### Static files

Most websites contain images, style sheets, and other static files that don't change as the application runs. Flask looks for these files in a special subdirectory named **static**.

Let’s say your site includes a style sheet named **main.css** and a banner named **banner.jpg**. You can drop these files into the **static** subdirectory and reference them in HTML this way:

``` html
<link rel="stylesheet" href="/static/main.css">
<img src="/static/banner.jpg">
```

You can also use Flask’s `url_for()` function to resolve these URLs:

``` html
<link rel="stylesheet" href="url_for('static', filename='main.css')">
<img src="url_for('static', filename='banner.jpg')">
```

One benefit of using `url_for()` is that the resulting URLs are absolute, which sidesteps issues that sometimes arise when browsers handle relative URLs in inconsistent ways.

## Summary and next steps

Flask is a lightweight web framework whose greatest strength is simply getting out of the way and allowing you as a developer to focus on the problems you wish to solve. You can create both proof-of-concept and enterprise level applications with Flask, and everything in between.
