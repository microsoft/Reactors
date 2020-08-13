# Starter site

We'll be adding functionality to an existing website, which represents our client, Contoso Travel. Contoso Travel is working to enable travelers to translate street signs and identify who is in a picture. You'll add functionality to three separate sections of the website - **translate** for sign translation, **train** for training the application to detect faces, and finally **detect** to identify faces.

## Obtaining the starter site

The sample code is provided as part of the [Reactors](https://github.com/microsoft/reactors) repository on [GitHub](https://github.com). Let's clone the repository and get the environment setup for the code.

### Clone the repository

1. Open a new command or terminal window to use solely for running your application
2. Navigate to the folder you want to put the code into, which was created earlier
3. Clone the repository

``` git
git clone https://github.com/microsoft/reactors
```

### Install Python packages

1. Navigate to the AI directory

``` console
# Windows
cd reactors\AI_1\starter-site

# Linux or macOS
cd ./reactors/AI_1/starter-site
```

2. Let's create a virtual environment for the packages we'll be using. Virtual environments allow us to separate packages from other environments. Return to the command line and issuing the following command:

``` console
# Windows
python -m venv env
.\env\Scripts\activate

# macOS or Linux
python3 -m venv env
. ./env/bin/activate
```

Note: If you're using macOS or Linux the leading `.` for the `. ./env/bin/activate` is required as it indicates to Python where your source code resides.

3. Finally, we'll install the packages listed in requirements.txt by using pip

``` console
pip install -r requirements.txt

# macOS or Linux
pip3 install -r requirements.txt
```

## Explore the current files

Take a moment to browse the files that were copied into the project directory. Open **starter-site** in the code editor of your choice. If you are using [Visual Studio Code](https://code.visualstudio.com), you can perform this operation by using the command `code .` from the terminal or command window.

Verify the following files exist:

- **app.py**, which holds the Python code that drives the site
- **image.py**, which holds a helper class we'll use for image management
- **templates/index.html**, the template for the home page
- **templates/base.html**, the template the remainder inherits from
- **templates/translate.html**, the template for translating signs
- **templates/train.html**, the template for training faces
- **templates/detect.html**, the template for detecting faces
- **static/main.css**, which contains CSS to dress up the home page
- **static/banner.jpg**, which contains the website banner
- **static/placeholder.jpg**, which contains a placeholder image for photos that have yet to be uploaded

> **NOTE:** We won't be focusing on working with HTML during this course. We want to be able to focus on the code necessary for Cognitive Services.

## Start the site

Let's start the site using Flask. We will configure Flask to run in development mode by setting the `FLASK_ENV` environmental variable. Running Flask in development mode is helpful when you’re developing a website because Flask automatically reloads any files that change while the site is running. If you let Flask default to production mode and change the contents of an HTML file or other asset, you have to restart Flask to see the change in your browser.

``` bash
# Windows
set FLASK_ENV=development
flask run

# macOS or Linux
export FLASK_ENV=development
flask run
```

> **NOTE:** **Keep this terminal or command window open**, as we're going to be making changes to our site throughout the day. If you accidentally close it, you can restart your site by issuing the same commands from above.

## Open the site

Open a browser and navigate to `http://localhost:5000`. Confirm the website appears. If you click the buttons the three pages we'll be working with will each open. You will notice the functionality is limited to just displaying the image you upload. We're going to start adding code to add the ability to translate street signs, and eventually detect people in images.

## Next steps

Congratulations! You've configured your environment and are ready to complete the rest of the labs! You can start by examining [Computer Vision and Translation services](computer-vision-translator/README.md). You can also explore [Python basics](intro-python.md) or [Flask basics](intro-flask.md) if you're not familiar with the language or framework.
