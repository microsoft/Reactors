import logging
import os, io
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

import azure.functions as func


def main(input: func.InputStream, output: func.Out[func.InputStream]):
    logging.info(f"Processing {input.name}")
    vision_client = ComputerVisionClient(
        os.getenv('COGSVCS_CLIENT_URL'),
        CognitiveServicesCredentials(os.getenv('COGSVCS_KEY'))
    )
    
    result = vision_client.generate_thumbnail_in_stream(
        300, 300, input
    )

    thumbnail = io.BytesIO()
    for chunk in result:
        thumbnail.write(chunk)
    thumbnail.seek(0)
    output.set(thumbnail)
