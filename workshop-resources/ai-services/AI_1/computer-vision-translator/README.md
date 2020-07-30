# Computer Vision and Text Analytics APIs

As we've discussed, AI is a useful tool that spans the practical and inspirational. We can sometimes see its capabilities even within a single app. For example, consider an application which could translate signage in a foreign language. Such an application would be useful for tourists on vacation, or could even help doctors save lives as they travel to foreign countries to stop an epidemic, such as ebola, before it can spread.

In this module, we'll examine building a web application like this by creating a website we'll call Contoso Travel. Users of this website, whether travelling for business or pleasure, will be able to upload photos of street signs from their phones and see the translated text. To build the application, we'll use the [Computer Vision API](https://azure.microsoft.com/services/cognitive-services/computer-vision/) to read the text, and the [Translator Text API](https://azure.microsoft.com/services/cognitive-services/translator-text-api/) to translate it.

To build the website, you'll perform the following tasks:

1. [Explore app.py](./explore-app-py.md), the core of our application.
2. [Create keys](./create-azure-resources.md) for the Computer Vision and Translator Text APIs.
3. [Call the Computer Vision API](./computer-vision.md) to extract text from photos.
4. [Call the Translator Text API](./translator.md) to translate text from extracted photos.
5. [Deploy the application](./deploy.md) to Azure.

To produce the application, you'll use [Python](https://python.org), one of the world's most popular programming languages, and [Flask](http://flask.pocoo.org/) for web development. Don't worry if you're not familiar with either Python or Flask; we will cover enough in this section for you to be able to produce the website.
