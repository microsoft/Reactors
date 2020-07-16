import os
from flask import Flask, render_template, request
from markupsafe import escape
from dotenv import load_dotenv
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

load_dotenv()

vision_client = ComputerVisionClient(
    os.getenv('COGSVCS_ENDPOINT'),
    CognitiveServicesCredentials(os.getenv('COGSVCS_KEY'))
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/isdog', methods=['GET', 'POST'])
def is_dog():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        image = request.files['image']
        image_info = vision_client.describe_image_in_stream(image)
        dog_found = False
        if 'dog' in image_info.tags:
            dog_found = True
        return render_template('result.html', dog_found=dog_found)
