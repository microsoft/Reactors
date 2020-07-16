# AI Code Solution

If you're a little lost, don't want to type out the code, or simply want to see the solution site in action, this is the folder for you. This folder contains the working site so you can see [Computer Vision](https://azure.microsoft.com/services/cognitive-services/computer-vision), [Translator Text](https://azure.microsoft.com/services/cognitive-services/translator-text-api/) and [Face API](https://azure.microsoft.com/services/cognitive-services/face/) in action!

## Setup

In order to run the solution site, there is a little work which needs to be done. The sample project uses [Python](https://python.org) and [Flask](https://palletsprojects.com/p/flask/), and you'll need a code editor to explore the application. You'll need an [Azure account](https://azure.microsoft.com/account/free) and the [Azure CLI](https://docs.microsoft.com/cli/azure/) to create the resources the application will use. We have a full setup document to walk you through the process.

### Prerequisites

Let's start by installing the prerequisites, which includes a code editor, Python and the Azure CLI.

Pleas follow the [instructions to install the prerequisites](../setup.md), **stopping at the step titled "Install Python Packages"** towards the bottom.

### Setting up the solution site

To use the solution site, we'll get to the solution directory, install the packages, and then create some keys.

#### Navigating to the directory and installing packages

In a command or terminal window, navigate to the solution directory:

``` console
# Windows
cd reactors\Artifical Intelligence 1_Building Software That Recognizes You\solution-site

# Linux or macOS
cd ./reactors/Artifical Intelligence 1_Building Software That Recognizes You/solution-site
```

Then, we'll create a [virtual environment](https://docs.python.org/3/library/venv.html). A virtual environment allows us to install Python packages into a local directory, insuring we don't accidentally overwrite other versions.

``` console
# Windows
python -m venv env
.\env\Scripts\activate

# macOS or Linux
python3 -m venv env
. ./env/bin/activate
```

Finally, we'll perform the installation of the packages listed in **requirements.txt**, which includes Flask, Requests, and the Azure libraries.

``` console
pip install -r requirements.txt

# macOS or Linux
pip3 install -r requirements.txt
```

### Creating keys and updating the application

Our application uses [Azure Cognitive Services](https://azure.microsoft.com/services/cognitive-services/), which means we need to create keys. We'll need three keys - one for Face API, one for Translator Text API, and one for Computer Vision.

#### Login to Azure CLI

Let's start by logging into Azure CLI. In the same command or terminal window, execute the following command. This will open a browser into which you will enter your credentials.

``` console
az login
```

#### Create a resource group

A resource group in Azure is, as the name implies, a collection of resources. This makes it easier to clean up everything we're creating when you're done with this workshop!

``` bash
az group create  --name contoso-travel-rg --location northcentralus
```

> **NOTE:** You'll notice we're creating the resource group in *northcentralus*, even though you might not be anywhere near the United States. We're using northcentralus to allow the steps in this workshop to be consistent. Do not worry if the location isn't near you. When look at Azure performance, the most important factor is ensuring all resources are created in the same region, which is what we'll be dong.

#### Create and store a Computer Vision key

The following two commands will create and then expose a key for use with [Computer Vision](https://docs.microsoft.com/azure/cognitive-services/Computer-vision/Home). Copy this key somewhere; we'll need it in a few moments.

``` bash
az cognitiveservices account create --resource-group contoso-travel-rg --name computer-vision --location northcentralus --kind ComputerVision --sku F0 --yes

az cognitiveservices account keys list --resource-group contoso-travel-rg --name computer-vision --query key1 --output tsv
```

#### Create and store a Translator Text API key

The following commands will create and then expose a key for use with [Translator Text API](https://azure.microsoft.com/services/cognitive-services/translator-text-api/). Copy this key somewhere; we'll need it in a few moments.

``` console
az cognitiveservices account create --resource-group contoso-travel-rg --name translator-text --location global --kind TextTranslation --sku F0 --yes

az cognitiveservices account keys list --resource-group contoso-travel-rg --name translator-text --query key1 --output tsv
```

#### Create and store a Face API key

The following commands will create and then expose a key for use with [Face API](https://azure.microsoft.com/services/cognitive-services/face/). Copy this key somewhere; we'll need it in a few moments.

``` console
az cognitiveservices account create --resource-group contoso-travel-rg --name face-api --location northcentralus --kind Face --sku S0 --yes

az cognitiveservices account keys list --resource-group contoso-travel-rg --name face-api --query key1 --output tsv
```

> **NOTE:** The key created for Face API is on the Standard tier. Please consult [Face API Pricing Details](https://azure.microsoft.com/pricing/details/cognitive-services/face-api/) for information about possible costs.

### Update and run the application

The application uses [Python dotenv](https://github.com/theskumar/python-dotenv) to ease management of keys and system variables. To configure dotenv, we'll create a file named **.env**, and then add in the appropriate key/value pairs.

#### Open the application in a code editor

Start by opening the site in a code editor of your choosing. If you're using [Visual Studio Code](https://code.visualstudio.com), you can perform this operation in your command terminal window by executing the command `code .` (where the `.` means the current directory).

#### Create a .env file and populate it with the appropriate keys

Create a new file using Visual Studio Code (or another editor) in the root of **solution-site** (the directory you're currently using) named **.env**. The leading **.** is required. Copy/paste the template below, and set the values of the keys to the ones you created above.

``` text
ENDPOINT=https://northcentralus.api.cognitive.microsoft.com
VISION_KEY=
TRANSLATE_KEY=
FACE_KEY=
```

#### Run the application

Congratulations!! You made it to the end!!! Now it's time to run the application and play with it! In the same console/terminal window, exectue the following command to start the application:

``` console
flask run
```

Then navigate to **localhost:5000** and you can play with the site! You can upload pictures of signs to [translate](http://localhost:5000/translate), photos of yourself to [train facial recognition](http://localhost:5000/train) (don't forget to add in a name!), and see if you can [detect yourself in a photo](http://localhost:5000/detect).
