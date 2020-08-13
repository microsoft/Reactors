# Train Face API

[Prerequisite: Introduction](./facial-recognition-concepts.md)

In order to recognize people in an image you need to first train up your model. This is done by uploading pictures containing the face of the person you wish to be able to identify, and specifying a name. There is no pre-built UI for performing the task, but it can be completed with a couple of lines of code.

## Managing the key

As we've seen, in order to us a Cognitive Service we need to have a key. You can create an [All-in-One](https://portal.azure.com/#create/Microsoft.CognitiveServicesAllInOne) key, which will give you access to almost every Cognitive Service, or create a key for each separate service. The advantage to the latter (creating a key for each service) is there is a free pricing tier available. We're going to use the key we created with [az hack create](../computer-vision-translator/create-azure-resources.md#resource-creation).

> **NOTE:** If you lost the information from the initial run of `az hack create`, you can open a terminal or command window (if runing the Azure CLI locally) or open [Cloud Shell](https://shell.azure.com) and execute `az hack show <name>`, where **\<name\>** is the name of the application

## Update app.py to include the ability to train faces

We're going to add the first part of the necessary functionality to recognize faces, which is to train the model. We will create our client, and then add the code required to perform the training.

### Create an instance of FaceClient

We're going to use `FaceClient` to interact with Face API. `FaceClient` is similar to the `ComputerVisionClient` we worked with previously.

In **app.py**, below the line which reads `# Create face_client`, add the following code:

``` python
from azure.cognitiveservices.vision.face import FaceClient

face_credentials = CognitiveServicesCredentials(COGSVCS_KEY)
face_client = FaceClient(COGSVCS_CLIENTURL, face_credentials)

person_group_id = "reactor"
```

Similar to the steps performed with Computer Vision, we import the class we'll be using (`FaceClient`), create an instance of `CognitiveServicesCredentials` with the key, and then create the client by specifying the endpoint and credentials. The final line of `person_group_id = "reactor"` is the name of the Person Group we're going to be creating. This will define our "closed universe", in which we will only be able to detect people we've already trained on.

### Create the train_person helper function

We're going to create a helper function named `train_person`. We will put all of the necessary code to create or update a person in our person group.

At the bottom of **app.py**, add the following code. You'll notice there's a fair bit of it, as `FaceClient` doesn't necessarily provide some of the functions we might expect. We will break down each section to help show what we're doing in this code.

``` python
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

    if len(people_with_name) > 0:
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
```

#### Breaking down the code

##### Create the group if needed

``` python
# Try to create the group, and just pass if it doesn't exist
try:
    client.person_group.create(person_group_id, name=person_group_id)
except:
    pass
```

The `get` function on `FaceClient` throws an exception if the group you wish to find doesn't exist. Because we need to make a round trip to the server anyway, we simply `create` the group, using the same ID as the name, and then catch any error and suppress it by using `pass` inside of `except`.

##### Create a person

``` python
name = name.lower()

# No get_by_name function, so get all persons
people = client.person_group_person.list(person_group_id)

# See if one exists with our name
people_with_name = list(filter(lambda p: p.name == name, people))

if len(people_with_name) > 0:
    person = people_with_name[0]
    operation = "Updated"
else:
    # Create if doesn't exist
    person = client.person_group_person.create(person_group_id, name)
    operation = "Created"
```

We start by changing the name provided to lower case letters for normalization. Because this becomes our key, we want to ensure it's case insensitive.

We then retrieve all of the people in our person group by using `person_group_person.list` and passing in the ID of our group. Because there is no `get` function which allows us to load a person by name, we use the [filter](https://docs.python.org/3/library/functions.html#filter) function in Python to find the person who matches the given name.

If there's at least one result, as revealed by `len`, we know there's a person with that name already. We store the person, and set the operation message to be **Updated**, since we'll be adding a face to an existing person. If the person doesn't exist, we `create` the person, and then set the operation message to **Created**.

#### Add the face and train the model

``` python
# Add the face to the person
client.person_group_person.add_face_from_stream(person_group_id, person.person_id, image)

# Retrain the model
client.person_group.train(person_group_id)

return ["{} {}".format(operation, name)]
```

We close by calling `add_face_from_stream` to add a person to a person group. We `train` the model. And finally we set an output message by passing in the operation (**Created** or **Updated**) and the name of the person.

### Add the call to train_person to train

Inside of the existing `train` function, immediately below the comment `# TODO: Add code to create or update person`, add the following code:

``` python
    # TODO: Add code to create or update person
    messages = train_person(face_client, person_group_id, name, image.blob)
```

> **NOTE:** The spaces at the beginning of the line of code is required. Python uses space levels to identify enclosures, and we want to put the call to `train_person` inside `train`. It should align with the existing comment.

We call our `train_person` function by passing in the `face_client`, the ID of our group, and the blob of the image.

## Testing our site

After saving all files, the process running our site should automatically reload. If you closed the command or terminal window you used to launch the site previously, you can open a new one, navigate to the directory containing your code, and then execute the following commands:

``` bash
# Windows
set FLASK_ENV=development
flask run

# macOS and Linux
export FLASK_ENV=development
flask run
```

In a browser, navigate to **http://localhost:5000/train**. Type the name of the person you wish to train, and then click **Upload** to select a picture of the person (such as yourself!). **The image you use can only have one face.** There is no UI for seeing the model in action; we're going to create that in the next section.

> **NOTE:** The image must be less than 3MB.

## Summary and next steps

We could have added additional code to allow someone to choose an existing name from a dropdown list, and to click an additional button to create a new name. This would have meant additional code, which we might not have had time to complete during the workshop. If you'd like, you can experiment with the code and see how you might be able to introduce functionality.

We've seen how to create the necessary key for Face API, and add the appropriate code to train the model with a person. Next, we'll see how we can [detect a person in an image](./detect-face-api.md).
