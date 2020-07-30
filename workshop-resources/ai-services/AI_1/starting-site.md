# Starter Site

We'll be adding functionality to an existing website, called Contoso Travel. Contoso Travel enables travelers to translate street signs and identify people in a picture. You'll add functionality to three separate sections of the website: **translate** for sign translation, **train** for training the application to detect faces, and **detect** to identify faces.

## Obtaining the starter site

The sample code is provided as part of the [Reactors](https://github.com/microsoft/reactors) repository on [GitHub](https://github.com). Let's clone the repository and get the environment set up for the code.

### Clone the repository

1. Open a command or terminal window to use solely for running your application.
2. Navigate to the folder you want to put the code into (which was created earlier).
3. Clone the repository.

``` git
git clone https://github.com/microsoft/reactors
```

### Install Python packages

1. Navigate to the AI directory.

``` console
# Windows
cd reactors\AI_1\starter-site

# Linux or macOS
cd ./reactors/AI_1/starter-site
```

2. Let's create a virtual environment for the packages we'll be using. Virtual environments allow us to separate packages from other environments. Return to the command line and issue the following command:

``` console
# Windows
python -m venv env
.\env\Scripts\activate

# macOS or Linux
python3 -m venv env
. ./env/bin/activate
```

Note: If you're using macOS or Linux, the leading `.` in `. ./env/bin/activate` is required, as it tells Python where your source code resides.

3. Finally, we'll use pip to install the packages listed in requirements.txt.

``` console
pip install -r requirements.txt

# macOS or Linux
pip3 install -r requirements.txt
```

## Explore the current files

Take a moment to browse the files that were copied into the project directory. In the code editor of your choice, open **starter-site**. If you are using [Visual Studio Code](https://code.visualstudio.com), you can perform this operation by using the command `code .` from the terminal or command window.

Verify the following files exist:

- **app.py**: Holds the Python code that drives the site.
- **image.py**: Holds a helper class we'll use for image management.
- **templates/index.html**: The template for the home page.
- **templates/base.html**: The template the remainder inherits from.
- **templates/translate.html**: The template for translating signs.
- **templates/train.html**: The template for training faces.
- **templates/detect.html**: The template for detecting faces.
- **static/main.css**: Contains CSS to dress up the home page.
- **static/banner.jpg**: Contains the website banner.
- **static/placeholder.jpg**: Contains a placeholder image for photos that have yet to be uploaded.

> **NOTE:** We won't be working with HTML during this course. We want to focus on the necessary code for Azure Cognitive Services.

## Start the site

Let's start the site using Flask. We will configure Flask to run in development mode by setting the `FLASK_ENV` environmental variable. Running Flask in development mode is helpful when you’re developing a website because Flask automatically reloads files that change while the site is running. If you let Flask default to production mode and change the contents of an HTML file or other asset, you have to restart Flask to see the changes in your browser.

``` bash
# Windows
set FLASK_ENV=development
flask run

# macOS or Linux
export FLASK_ENV=development
flask run
```

> **NOTE:** **Keep this terminal or command window open**, as we're going to make changes to our site throughout the day. If you accidentally close it, you can restart your site by issuing the same commands from above.

## Open the site

Open a browser and navigate to `http://localhost:5000`. Confirm the website appears. If you click the buttons, the three pages we'll be working with will each open. You will notice the functionality is limited to displaying the image you upload. We're going to start adding code to translate street signs and eventually detect people in images.

## Next steps

Congratulations! You've configured your environment and are ready to complete the rest of the labs! You can start by examining [Computer Vision and Text Analytics APIs](computer-vision-translator/README.md). You can also explore [Overview of Python](intro-python.md) or [Flask Fundamentals](intro-flask.md) if you're not familiar with the language or framework.
