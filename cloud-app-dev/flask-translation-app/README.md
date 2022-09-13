# The Penpal Project Sample (instructions and code samples)
Sample code to create penpal project translation web app

# Getting Started
To do this project you'll need to:
- Have VS Code installed with the Python extension (Learn how here)[https://aka.ms/pythoninstallvscode17183]
- Have the GitHub extensions for VS Code installed. (Learn how here)[[https://aka.ms/pythoninstallvscode17183](https://aka.ms/IntroToGitHub17183)] - *You only need to do the first 3 pages.*
- Have created a GitHub repo and cloned it into VS Code.

<br>

# How to set up your dev environment

Now that we've cloned in our Git repo to VS Code, we'll set up our dev evnironment.

<details>
    <summary>See steps</summary>

For this project we're going to need a couple of libraries. 
You'll see how to set up a virtula enviroment and add the needed libraries.

## Create the virtual environment
If you do lots of projects it's best to store your libraries for each project seperatelyusing a **virtual environment**.

*If this seems to tricky for you right now in your learning journey, it's ok to skip it and install the things to your whole computer! (go to the next step)*

### Windows
1. Create the virtual environment
    
    ```
    python -m venv venv
    ```

2. Activate the environment
    
    ```
    .\venv\scripts\activate
    ```

3. Click "yes" in the box that pops up in the bottom right corner of VS Code to select to use the virtual environment.

### Mac/Linux

1. Create the virtual environment
    
    ```
    python -m venv venv
    ```

2. Activate the environment
    
    ```
    source ./venv/bin/activate
    ```

3. Click "yes" in the box that pops up in the bottom right corner of VS Code to select to use the virtual environment.

<br>

## Setting up your requirements file

We'll need a requirements.txt file. This is a way to list all the needed libraries, and will be used by Azure when we deploy the project. 

1. in your project folder, make a requirements.txt file. 

2. inside the file copy this text, these are the libraries we need to install:

    ```
    flask
    python-dotenv
    requests
    ```

<br>

## Install the libraries

Whether your installing in your virtual environment, or to your whole computer system, you should now run this comand to install the libraries we listed above from the requirements file. 

```pip install -r requirements.txt```

**You should be ready to go now!**
<br>

</details>

<br>

### Set up - Troubshooting

***Hopefully*** your libraries are all their and working for you now!

We'll find out in the next step if VS Code knows about your libraries. (Some times it can get a little confused)

<details>
    <summary><strong>See help options</strong></summary>


If VS Code later says that you are missing something, eg Flask, you can come back here and try these trouble shooting steps.

1. Make sure you have the Python Extension installed. If not, install it and close and re-open VS Code.

2. In the bottom right corner of VS Code, see if VS Code thinks you are using the correct virtual enviroment (or correct version of Pythnon if your not using a virtual env). Click on the Pyton/Virtual env that is has selected if it is incorrect, and select the correct one. 

3. If you're unable to select the correct Pyton/Virtual env in step 2, close VS Code and re-open the project 🤞.

4. If it's still not working, try not using a virtual env if you are using one **(or try making a new virtual env with a different name, eg: ```python -m venv venv2```)**. 

    If you skipped that step try creating a virtual env if you skipped that before. 

</details>

<br>
<br>

# Let's build our translator app!
## Making our first page
To get started we'll need to make a form that collects the text to be translated and the language to translate it to. For this we'll need a web server and some HTML!

<details>
    <summary><strong>See steps and code</strong></summary>

1. Create a file called server.py

2. Copy in this code to import your libraries and create your web app.

    ```python
    from flask import Flask, redirect, url_for, request, render_template, session

    app = Flask(__name__)
    ```

3. Add this handy code at the bottom or your file, which will help run your code. 
    ```python
    ### Step 3 - Add helpful code that runs our server
    if __name__ == '__main__':
        app.run(debug=True, use_reloader=True, host='0.0.0.0', port=8000)
    ```

4. Create a folder called templates

5. Inside the templates floder create a file called index.html

6. Add this code to index.html create the first page of our website.
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
            integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
        <title>Translator</title>
    </head>
    <body>
        <div class="container">
            <h1>Translation service</h1>
            <div>Enter the text you wish to translate, choose the language, and click Translate!</div>
            <div>
                <form method="POST">
                    <div class="form-group">
                        <textarea name="text" cols="20" rows="10" class="form-control"></textarea>
                    </div>
                    <div class="form-group">
                        <label for="language">Language:</label>
                        <select name="language" class="form-control">
                            <option value="en">English</option>
                            <option value="it">Italian</option>
                            <option value="ja">Japanese</option>
                            <option value="ru">Russian</option>
                            <option value="de">German</option>
                        </select>
                    </div>
                    <div>
                        <button type="submit" class="btn btn-success">Translate!</button>
                    </div>
                </form>
            </div>
        </div>
    </body>
    </html>
    ```

7. Run your code and go to the address in a web browser.


</details>

<br>

> **Bonus Activity - Make it pretty**
>
> If you want a little more to do, you can make yours pretty too!
> 1. Create a folder called static
> 2. In static create a file called style.css
> 3. copy the contents of my style.css file to yours
> 4. I've made a few changes to the index.html file (and stored them in pretty-index.html), update your index.html file to match my pretty-index.html
> 5. Finally you just need the typewritter image. Download typewriter.jpg from my static folder, and add it to your static folder. 


<br>

## Make a second route for the result page

Next up lets add our second page, where we'll later display the resutls of our translation. To start with though, we'll just include a message saying the translation does work yet. 

<details>
    <summary><strong>See steps and code</strong></summary>

1. Copy this code, and put it below your first route. (But above your run server code)

    ```python
    @app.route('/', methods=['POST'])
    def index_post():
        # Read the values from the form
        original_text = request.form['text']
        target_language = request.form['language']

        ################################
        # TRANSLATION CODE GOES HERE!  #
        ################################

        translated_text = "Sorry, I don't know how to translate yet...""

        ################################
        # IT WASN'T SO HARD WAS IT? :) #
        ################################


        # Call render template, passing the translated text,
        # original text, and target language to the template
        return render_template(
            'results.html',
            translated_text=translated_text,
            original_text=original_text,
            target_language=target_language
        )
    ```

2. Create another file in the templates folder, call it **results.html**

3. Copy this code into results.html

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
            integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
        <title>Result</title>
    </head>
    <body>
        <div class="container">
            <h2>Results</h2>
            <div>
                <strong>Original text:</strong> {{ original_text }}
            </div>
            <div>
                <strong>Translated text:</strong> {{ translated_text }}
            </div>
            <div>
                <strong>Target language code:</strong> {{ target_language }}
            </div>
            <div>
                <a href="{{ url_for('index') }}">Try another one!</a>
            </div>
        </div>
    </body>
    </html>
    ```

</details>

4. Try using your website again. What happens now when you submit the form?

> **Bonus Activity - Make it pretty**
>
> If you want a little more to do, you can make yours pretty too!
> 1. If you haven't completed the previous bonus activity, do that first. 
> 2. In static create a file called result-style.css
> 3. copy the contents of my result-style.css file to yours
> 4. I've made a few changes to the results.html file (and stored them in pretty-index.html), update your results.html file to match my pretty-results.html
> 5. Finally you just need the paper image. Download paper.jpeg from my static folder, and add it to your static folder. 




<br>

## Creating a translation service
Now we have a place to put our translated text, we should get Azure ot help us translate it! We'll set up the Azure service that we can ask to translate text.

<details>
    <summary><strong>See steps and code</strong></summary>


1. Follow along in the stream to do the set up in Azure, or if you need to go back (and see pictures), checkout the flow process here: [Create an Azure Translation Service](https://aka.ms/ExerciseCreateTranslatorservice17183)

2. Back in your project folder, create a file called `.env`

3. Copy the values from Azure to fill out your `.env` file so it has this format:

    ```
    KEY=<your_key>
    ENDPOINT=<your_endpoint>
    LOCATION=<your_location>
    ```

    ***It will look ~something~ like this in the end.***
    (Make sure to use your own keys though.)
    ```
    KEY=00d09299d68548d646c097488f7d9be9
    ENDPOINT=https://api.cognitive.microsofttranslator.com/
    LOCATION=westus2
    ```

4. Go back to your server.py file, below your first line where you import things, add this code too:

    ```python
    import requests, os, uuid, json
    from dotenv import load_dotenv
    load_dotenv()
    ```

</details>

<br>

## Use the translation service in your app

We now have an API we can call from our server.py file. Let's make our web server translate the text from the form before showing the result page.

<details>
    <summary><strong>See steps</strong></summary>


1. Previouly, **we left a gap** in our code where we want to add the translation service. It looked like this

    ```python
    ################################
    # TRANSLATION CODE GOES HERE!  #
    ################################

    translated_text = "Sorry, I don't know how to translate yet...""

    ################################
    # IT WASN'T SO HARD WAS IT? :) #
    ################################
    ```

    We're going to replace this code with working code. **So you can delete this code now.**

2. where you just removed the code, add this code instead.

    ```python
    # Load the values from .env
    key = os.environ['KEY']
    endpoint = os.environ['ENDPOINT']
    location = os.environ['LOCATION']

    # Indicate that we want to translate and the API version (3.0) and the target language
    path = '/translate?api-version=3.0'
    # Add the target language parameter
    target_language_parameter = '&to=' + target_language
    # Create the full URL
    constructed_url = endpoint + path + target_language_parameter

    # Set up the header information, which includes our subscription key
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # Create the body of the request with the text to be translated
    body = [{ 'text': original_text }]

    # Make the call using post
    translator_request = requests.post(constructed_url, headers=headers, json=body)
    # Retrieve the JSON response
    translator_response = translator_request.json()
    # Retrieve the translation
    translated_text = translator_response[0]['translations'][0]['text']
    ```

3. Test your website again, how does it do?

</details>

<br>

## Use the translation service in your app

We can now deploy our app to the web using Azure App Service.

<details>
    <summary><strong>See steps</strong></summary>
1. Commit and push you code to GitHub

2. Create an Azure App Service instanstance. In the set-up process be sure to click "allow continuous deployment", then link you're GitHub repo. Create and wait for it to deploy.

3. In the App service instance, add your secret keys for your Translation service to Azure. 

4. Wait for your code to deploy!

</details>
