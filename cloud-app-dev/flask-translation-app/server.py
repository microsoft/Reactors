import requests, os, uuid, json
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, redirect, url_for, request, render_template, session

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def index_post():
    # Read the values from the form
    original_text = request.form['text']
    target_language = request.form['language']

    ################################
    # TRANSLATION CODE GOES HERE!  #
    ################################

    # Load the values from .env
    key =  os.getenv('KEY')
    endpoint =  os.getenv('ENDPOINT')
    print("#########ENPOINT: ", endpoint)
    location =  os.getenv('LOCATION')

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

    print(translator_response)
    # Retrieve the translation
    translated_text = translator_response[0]['translations'][0]['text']

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

@app.route('/pretty', methods=['GET'])
def index_pretty():
    return render_template('index-pretty.html')

@app.route('/pretty', methods=['POST'])
def index_post_pretty():
    # Read the values from the form
    original_text = request.form['text']
    target_language = request.form['language']

    ################################
    # TRANSLATION CODE GOES HERE!  #
    ################################

    # Load the values from .env
    key =  os.getenv('KEY')
    endpoint =  os.getenv('ENDPOINT')
    print("#########ENPOINT: ", endpoint)
    location =  os.getenv('LOCATION')

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

    print(translator_response)
    # Retrieve the translation
    translated_text = translator_response[0]['translations'][0]['text']

    ################################
    # IT WASN'T SO HARD WAS IT? :) #
    ################################


    # Call render template, passing the translated text,
    # original text, and target language to the template
    return render_template(
        'results-pretty.html',
        translated_text=translated_text,
        original_text=original_text,
        target_language=target_language
    )

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host='0.0.0.0', port=8000)