# Create a site to upload photos

[Prerequisite: Getting started with Flask](./flask.md)

Now we're ready to start creating our Flask application. We're going to begin by cloning the starter, then creating a virtual environment and installing the necessary components. Then we'll explore the starter, and see what we're going to be building.

## Create a directory

1. Start by opening a command or terminal window. Create a directory for use during this workshop:

``` bash
# Windows
md contoso
cd contoso

# macOS or Linux
mkdir contoso
cd contoso
```

``` bash
git clone https://github.com
```

2. Create a directory in the location of your choice. This will be the *project directory*, and will hold all the files for the Contoso Travel website. It's also where our virtual environment will be created. Change directories into the directory you created.

``` bash
# Windows
md contoso && cd contoso

# macOS or Linux
mkdir contoso && cd contoso
```

## Download the starter site

1. If Git isn’t installed on your computer, go to the [Git website](https://git-scm.com/) and install it now. Versions are available for Windows, macOS, and Linux.
2. In a command window or terminal, use `cd` to switch to the project directory you created in the previous subsection. Then use the following command to clone the GitHub repo containing the starter files for the website:

``` bash
git clone https://github.com/GeekTrainer/ai-workshop-starter.git .
```

> **Note:** Don’t forget to include the period at the end of the command. Otherwise, the files will be copied into a subdirectory of the project directory rather than into the project directory itself.

## Create a virtual environment and install packages

Let's create a virtual environment for the packages we'll be using. Virtual environments allow us to separate packages from other environments.

1. Create the virtual environment by returning to the command line and issuing the following command:

``` bash
# Windows
python -m venv env
.\env\Scripts\activate

# macOS or Linux
python3 -m venv env
. ./env/bin/activate
```

> **Note:** If you're using macOS or Linux the leading `.` for the `. ./env/bin/activate` **is** required as it indicates to Python where your source code resides.

2. Install the packages listed in `requirements.txt` by using `pip`

``` bash
pip install -r requirements.txt
```

## Explore the current files

1. Take a moment to browse the files that were copied into the project directory. Verify that they include:

- **app.py**, which holds the Python code that drives the site
- **templates/index.html**, the template for the home page
- **templates/base.html**, the template the remainder inherits from
- **templates/translate.html**, the template for translating signs
- **templates/train.html**, the template for training faces
- **templates/detect.html**, the template for detecting faces
- **static/main.css**, which contains CSS to dress up the home page
- **static/banner.jpg**, which contains the website banner
- **static/placeholder.jpg**, which contains a placeholder image for photos that have yet to be uploaded

> **NOTE:** We won't be focusing on working with HTML during this course. Again, we want to be able to focus on the code necessary for Cognitive Services.

## Test the starter site

Let's see the starter site.

1. Configure Flask to run in development mode by setting the `FLASK_ENV` environmental variable. Running Flask in development mode is helpful when you’re developing a website because Flask automatically reloads any files that change while the site is running. If you let Flask default to production mode and change the contents of an HTML file or other asset, you have to restart Flask to see the change in your browser.

``` bash
# Windows
set FLASK_ENV=development

# macOS or Linux
export FLASK_ENV=development
```

2. Now use the following command to start Flask:

``` bash
flask run
```

3. Open a browser and navigate to `http://localhost:5000`. Confirm the website appears. If you click the buttons the three pages we'll be working with will each open. You will notice the functionality is limited to just displaying the image you upload. We're going to start adding code to add the ability to translate street signs, and eventually detect people in images.

## Summary and next steps

We have a Flask application to allow users to upload images, and to display them on the page. Next we'll see how to [create keys](./create-azure-keys.md) so we can call Computer Vision and Translator Text.
