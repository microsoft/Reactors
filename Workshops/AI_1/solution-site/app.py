# app.py
import os, base64, json, requests
from flask import Flask, render_template, request

# Load system variables with dotenv
from dotenv import load_dotenv
load_dotenv()

# Load keys
COGSVCS_CLIENTURL = os.environ["COGSVCS_CLIENTURL"]
COGSVCS_KEY = os.environ["COGSVCS_KEY"]
COGSVCS_REGION = 'northcentralus'

# Create vision_client
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import ComputerVisionErrorException

vision_credentials = CognitiveServicesCredentials(COGSVCS_KEY)
vision_client = ComputerVisionClient(COGSVCS_CLIENTURL, vision_credentials)

# Create face_client
from azure.cognitiveservices.vision.face import FaceClient

face_credentials = CognitiveServicesCredentials(COGSVCS_KEY)
face_client = FaceClient(COGSVCS_CLIENTURL, face_credentials)

person_group_id = 'reactor'

# Create the application
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

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
    messages = extract_text_from_image(image.blob, vision_client)

    # TODO: Add code to translate text
    messages = translate_text(messages, target_language, COGSVCS_KEY, COGSVCS_REGION)

    return render_template("translate.html", image_uri=image.uri, target_language=target_language, messages=messages)

@app.route("/train", methods=["GET", "POST"])
def train():
    # Load image or placeholder
    image = get_image(request)

    # If it"s a GET, just return the form
    if request.method == "GET":
        return render_template("train.html", image_uri=image.uri)

    # Retrieve name from form
    name = ""
    if "name" in request.form:
        name = request.form["name"]

    # Placeholder for messages
    messages = []

    # TODO: Add code to create or update person
    messages = train_person(face_client, person_group_id, name, image.blob)

    return render_template("train.html", messages=messages, image_uri=image.uri)

@app.route("/detect", methods=["GET", "POST"])
def detect():
    # Load image or placeholder
    image = get_image(request)

    # If it"s a GET, just return the form
    if request.method == "GET":
        return render_template("detect.html", image_uri=image.uri)

    # Placeholder for message
    messages = []

    # TODO: Add code to detect people in picture
    messages = detect_people(face_client, person_group_id, image.blob)

    if not messages:
        messages.append("I don't recognize anyone")

    return render_template("detect.html", messages=messages, image_uri=image.uri)

def get_image(request):
    # Helper class 
    from image import Image
    if request.files:
        return Image(request.files["file"])
    else:
        return Image()

def extract_text_from_image(image, client):
    try:
        result = client.recognize_printed_text_in_stream(image=image)

        lines=[]
        if not result.regions:
            lines.append("Photo contains no text to translate")
        else:
            for line in result.regions[0].lines:
                text = " ".join([word.text for word in line.words])
                lines.append(text)
        return lines
    except ComputerVisionErrorException as e:
        print(e)
        return ["Computer Vision API error: " + e.message]

    except Exception as e:
        print(e)
        return ["Error calling the Computer Vision API"]

def translate_text(lines, target_language, key, region):
    uri = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=" + target_language

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': region,
        'Content-type': 'application/json'
    }

    input=[]

    for line in lines:
        input.append({ "text": line })

    try:
        response = requests.post(uri, headers=headers, json=input)
        response.raise_for_status() # Raise exception if call failed
        results = response.json()

        translated_lines = []

        for result in results:
            for translated_line in result["translations"]:
                translated_lines.append(translated_line["text"])

        return translated_lines

    except requests.exceptions.HTTPError as e:
        return ["Error calling the Translator Text API: " + e.strerror]

    except Exception as e:
        return ["Error calling the Translator Text API"]

def train_person(client, person_group_id, name, image):
    # Try to create the group, and just pass if it doesn't exist
    try:
        client.person_group.create(person_group_id, name=person_group_id)
    except:
        pass

    name = name.lower()

    # No get_by_name function, so get all persons
    people = client.person_group_person.list(person_group_id)

    # See if one exists with our name
    people_with_name = list(filter(lambda p: p.name == name, people))

    if people_with_name:
        # Person exists; flag as update
        person = people_with_name[0]
        operation = "Updated"
    else:
        # Create if doesn't exist
        person = client.person_group_person.create(person_group_id, name)
        operation = "Created"

    # Add the face to the person
    client.person_group_person.add_face_from_stream(person_group_id, person.person_id, image)

    # Retrain the model
    client.person_group.train(person_group_id)

    return ["{} {}".format(operation, name)]

def detect_people(client: FaceClient, person_group_id, image):
    # Find all faces in the image
    faces = face_client.face.detect_with_stream(image)

    # Get just the IDs (for identification)
    face_ids = list(map((lambda face: face.face_id), faces))

    for face in faces:
        print(face)

    # Identify the faces
    identified_faces = face_client.face.identify(face_ids, person_group_id)

    results = []
    # Loop through each identified face
    for face in identified_faces:
        # Get all candidates - who might this face be?
        candidates = face.candidates

        # If no candidates, continue
        if not candidates:
            continue

        # Sort by most likely candidate
        candidates = sorted(candidates, key=(lambda candidate: candidate.confidence), reverse=True)
        
        # Get just the top candidate
        top_candidate = candidates[0]

        # Ask our model who this person is
        person = face_client.person_group_person.get(person_group_id, top_candidate.person_id)

        # Add the person to the list of results
        if top_candidate.confidence > .8:
            results.append('I see ' + person.name + ' - ' + str(top_candidate.confidence))
        else:
            results.append('I think I see ' + person.name + ' - ' + str(top_candidate.confidence))

    return results
