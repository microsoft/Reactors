# Examining the user interface

[Prerequisite: Detecting people with Face API](./detect-face-api.md)

With our model built, we're now ready to turn our attention to deploying our site.

## Deploy the application to Azure

With all the functionality added to our application, we're ready to publish to Azure! We will use the same [remote Git we created earlier](../computer-vision-translator/deploy.md#add-azure-as-a-remote-destination).

Open (or use) a command or terminal window *on your local system*.

1. Commit changes

``` terminal
git add app.py
git commit -m "Added facial recognition"
```

2. Push to auzre

``` terminal
git push azure
```

> **NOTE:** When you push you will be prompted for the username and password which was created by `az hack create` and displayed as part of the output. If no password was generated, you can [reset your password with Azure CLI](../computer-vision-translator/deploy.md#set-a-deployment-password)

## Run the website

Now it's time to see your site in the real world! Open your browser and navigate to **https://APP_NAME.azurewebsites.net/detect**, replacing **APP_NAME** with the name of your application. Because you were training the model on Azure, you'll be able to run the detection feature without having to retrain! And, if you open the site on your mobile device you could even take a selfie to test your site.

## Summary and next steps

We've seen how to create a facial recognition application. You could enhance the site quite a bit if you'd like. You could add links to the pages (of course). You could also list the names available, and offer someone the option to either add to an existing name or create new. Maybe allow for multiple files to be uploaded? There's a lot of room to explore!
