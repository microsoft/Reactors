# Adding Computer Vision to our application

[Prerequisites: Create Computer Vision keys](./create-azure-resources.md)

## Overview of Computer Vision

Azure Cognitive Services is a set of more than 20 services and APIs for infusing intelligence backed by machine learning and neural networks into the applications that you write. One member of the Cognitive Services family is the [Computer Vision API](https://azure.microsoft.com/services/cognitive-services/computer-vision/), which can analyze images uploaded to it and:

- Identify objects in the images.
- Generate captions for the images (for example, "A woman riding a bicycle").
- Use Optical Character Recognition (OCR) to extract text from the images.
- Find faces in the images and identify attributes of those faces, such as age and gender.
- Generate "smart thumbnails" centered around the subjects of the images.
- Recognize famous people and landmarks in the images.

Like all Cognitive Services APIs, the Computer Vision API is invoked by placing calls over the Internet to a REST endpoint. Rather than placing those calls directly, you can use the [Python SDK for the Computer Vision API](https://pypi.org/project/azure-cognitiveservices-vision-computervision/) to simplify your code. The SDK abstracts calls to the Computer Vision API and handles JSON payloads for you so that you don’t have to write code to generate and consume JSON yourself.

It is the OCR feature of the Computer Vision API that will enable the Contoso Travel site to extract text from images. In this unit, you will modify Contoso Travel to use the Computer Vision API to extract text from photos uploaded to the site.

## Create .env file

As mentioned before, we are using [dotenv](https://github.com/theskumar/python-dotenv) to manage our environmental variables. Let's create the file we'll be using.

In your code editor, create a new file named **.env**, ensuring you have the leading **.** in front of the filename. **.env** is a set of key/value pairs, so we'll add the appropriate values:

``` bash
COGSVCS_CLIENTURL=<clienturl>
COGSVCS_KEY=<key>
```

Replace `<clienturl>` and `<key>` with the clienturl and key values you stored from the prior exercise. No quotes or other special characters are needed to contain the values.

> **NOTE:** In Azure Cognitive Services, the `<clienturl>` is called the `Endpoint`.

## Add configuration code to app.py

You have now subscribed to the Computer Vision API and stored the endpoint and API key. The next step is to modify the Contoso Travel site to load these values.

Open **app.py**. Just below the comment which reads `# Load keys` add the following code, which will read environmental variables of `COGSVCS_CLIENTURL`, which contains the URL of the endpoint, and `COGSVCS_KEY`, which is the authentication key for Computer Vision. We'll also set the COGSVCS_REGION to be **northcentralus**:

``` python
# Load keys
COGSVCS_CLIENTURL = os.environ["COGSVCS_CLIENTURL"]
COGSVCS_KEY = os.environ["COGSVCS_KEY"]
COGSVCS_REGION = 'northcentralus'
```

## Create the client

We'll be using the `ComputerVisionClient` to use [Computer Vision](https://docs.microsoft.com/azure/cognitive-services/Computer-vision/Home). We'll need to load the appropriate classes, `CognitiveServiceCredentials`, which will be used to store the password, `ComputerVisionClient`, which is the actual client, and `ComputerVisionErrorException`, which represents errors raised by the service. The code finishes with the creation of the credentials, followed by the client. Add the following below the comment `# Create vision_client`.

``` python
# Create vision_client
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import ComputerVisionErrorException

vision_credentials = CognitiveServicesCredentials(COGSVCS_KEY)
vision_client = ComputerVisionClient(COGSVCS_CLIENTURL, vision_credentials)
```

## Calling Computer Vision

Let's create the helper function which will send the image to Computer Vision and prepare the results. Add the following function to the end of **app.py**.

``` python
# Function that extracts text from images
def extract_text_from_image(image, client):
    try:
        result = client.recognize_printed_text_in_stream(image=image)

        lines=[]
        if len(result.regions) == 0:
            lines.append("Photo contains no text to translate")

        else:
            for line in result.regions[0].lines:
                text = " ".join([word.text for word in line.words])
                lines.append(text)

        return lines

    except ComputerVisionErrorException as e:
        return ["Computer Vision API error: " + e.message]
```

### Breaking down the code

#### Calling Optical Character Recognition

``` python
try:
    result = client.recognize_printed_text_in_stream(image=image)
```

Using the Computer Vision client, we call `recognize_printed_text_in_stream` to retrieve the words found in the image from Compuer Vision.

#### Preparing the result

``` python
lines=[]
if len(result.regions) == 0:
    lines.append("Photo contains no text to translate")

else:
    for line in result.regions[0].lines:
        text = " ".join([word.text for word in line.words])
        lines.append(text)

return lines
```

The result we receive from Computer Vision is in JSON. We are going to convert it to an `list` of lines of text for simplicity. We start by creating an `list` to store the lines. We then examine `result.regions` to see if there are any regions on the image which contain text. An image could have one or more regions. If no regions are returned there is no text, so we append an error message.

Assuming there are regions, we are going to retrieve the lines from the first region. `regions` is a list, so you could create another `for` loop to iterate through all of the regions if you desire. In our case we just use the first. We then grab all of the `words` in each `line` and add a space between them by using `join`. Finally, we append the `line` to our `lines` list and return it.

#### Basic error handling

``` python
except ComputerVisionErrorException as e:
    return ["Computer Vision API error: " + e.message]

except:
    return ["Error calling the Computer Vision API"]
```

We finish off by returning whatever error messages were raised.

## Adding the call to Computer Vision to translate

With our helper function created, let's add the code necessary to `translate` to call it. Just below the comment which reads `# TODO: Add code to retrieve text from picture`, add the following:

``` python
    # TODO: Add code to retrieve text from picture
    messages = extract_text_from_image(image.blob, vision_client)
```

> **NOTE:** The spaces at the beginning of the line of code are required. Python uses spacing levels to identify enclosures, and we want to put the call to `extract_text_from_message` inside `index`. It should be aligned with the existing comment.

### Breaking down the code

`messages` is the variable we're using to send to our template for display to our user. Because we want to output the lines we read from the image, we're going to store the result of `extract_text_from_image` in this variable. The function `extract_text_from_image` is looking for both the blob of the image, so we use `image.blob`, and the client, which we're providing.

## Testing our site

Make sure you've saved all of the files you created or modified. Let's see if the page works.

Navigate to **http://localhost:5000** in your browser. Click **Upload Photo** and upload a picture which contains text. Confirm that after a brief pause the extracted text from the photo appears in the modal dialog box.

> **NOTE:** The image must be smaller than 4MB. If you receive an error message indicating your key or endpoint are invalid (or None), try restarting the application manually.

## Summary and next steps

You'll probably notice the text recognition isn't perfect. Depending on the clarity of the photo, the fonts, etc., there may be some small differences between actual text and what is detected. But you'll notice a high degree of success. Now we can take the text and [translate it](translator.md).
