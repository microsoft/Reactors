# ☁️ Exercise 3: Deploy on Azure Static Web App

In this exercise, you will learn how to deploy the `portal` project on Azure using the Azure Static Web Apps CLI and GitHub Actions. You'll need to use your Azure account for this exercise. If you don't have an account, create a free [Azure Free Trial](https://azure.microsoft.com/free/?WT.mc_id=academic-101248-cyzanon) or use the [GitHub Student Developer Pack — GitHub Education](https://aka.ms/Copilot4Students) program.

## Preparing the scenario

### Create a new branch

First, you will need to create a new branch in your GitHub repository and follow some configuration steps. To do this, run the following commands in the Visual Studio Code terminal in Codespaces:

```bash
  git checkout -b portal-deploy
```

### Create a copy and rename

Create a copy of the `portal` folder and rename it to `portal-deploy` This duplication is necessary so that we can deploy the portal scenario separately from other parts of the project, such as the `blog` and `api`.

```bash
  cp -r packages/portal packages/portal-deploy
```

With the `portal-deploy` folder created, access the file `packages/portal-deploy/package.json` and change the `name` property to `portal-deploy`.

![Package.json](./images/new-portal-package-json.jpg)

## Navigate and delete existing files

Go back to the terminal, as we will run some routines with basic Linux commands and configure the project deployment with the Azure Static Web Apps CLI.

```bash
  cd packages/portal-deploy
```

We need to delete the `swa-cli.config.json` file. To do this, we will use the linux command `rm -rf`. The -r is used to delete folders and the -f is used to force deletion.

**Remove the swa-cli.config.json file:**

```bash
  rm -rf swa-cli.config.json
```

## Customize your portal

> Remember, we will use the portal-deploy for deployment on Azure. So make your changes in the portal-deploy folder and not in the portal.

**1️⃣ Change the title of the portal**

Access the file `app/homepage/homepage.component.html` and change the `h1` tag to `Contoso Real Estate - Your Name`.

You can also add a paragraph below the title with the following text: `Welcome to the best real estate experience!`.

**2️⃣ Add social media links**

In the footer section, add the a list of social media links. If you want download the LinkedIn, Instagram and Twitter icons from [Font Awesome](https://fontawesome.com/).

Use GitHub Copilot to help you with the code and don't forget to add some CSS to make the links look good. The CSS code can be added in the `app.component.scss` file.

**3️⃣ Update the About page**

The About page is a static page with information about the Contoso Real Estate company. This page is located in the `app/about/` folder. 

Work on the following tasks:

- Change the title of the page to `About Contoso Real Estate`.
- Add a paragraph below the title with the following text: `Contoso Real Estate is a company that has been in the market for more than 20 years. We are a company that values ​​the quality of our services and the satisfaction of our customers.`
- Add a paragraph with the following text: `We are always looking for new talents to join our team. If you are interested in working with us, send your resume to real@contoso.com.`
- Add a photo of the Contoso Real Estate team. You can save the image in the `assets/images` folder


## Azure Static Web Apps (SWA) CLI

With the initial settings completed, you will need to initialize Azure Static Web Apps so that we can deploy the `portal` to Azure.

To do this, use the terminal to navigate to the root of the Contoso Real Estate project by running the following command:

```bash
  cd ../..
```

**Initialize Azure Static Web Apps**

```bash
  swa init
```

The SWA CLI will identify the existing projects in Contoso Real Estate and you should choose the `portal-deploy`. Check if the project name is correct and press `y` to confirm.

![Visual Studio Code Terminal in Codespaces](./images/swa-init.gif)

A `swa-cli.config.json` file will be generated and will have the following information:

```json
  {
    "$schema": "https://aka.ms/azure/static-web-apps-cli/schema",
    "configurations": {
      "contoso-real-estate": {
        "appLocation": "packages/portal-deploy",
        "apiLocation": "packages/api",
        "outputLocation": "dist/contoso-app",
        "apiLanguage": "node",
        "apiVersion": "16",
        "appBuildCommand": "npm run build",
        "apiBuildCommand": "npm run build --if-present",
        "run": "npm start",
        "appDevserverUrl": "http://localhost:4200"
      }
    }
  }
```

In the previous exercise, we explained how the communication between the backend and the frontend works and how the `swa-cli.config.json` file is generated. In this exercise, the values of the properties are different because we are deploying the `portal` project separately from the other parts of the project and we are poining to the `portal-deploy` folder.

**Execution test**

```bash
  swa start
```

During execution, a popup will open in the lower right corner of Visual Studio Code. Click on the `Ports` tab and check if port `4280` is open. If it is, click the `Open Browser` button so you can view the portal.

![Ports](./images/ports-executing-new-deploy.gif)


### Creating the artifacts

Artifacts are the files that will be sent to Azure Static Web Apps. Artifacts are static files, such as HTML, CSS, JavaScript, and images, that are generated by the build process. All artifacts generated by the SWA CLI are stored in the `dist/contoso-app` folder. To generate the `portal` artifacts, run the following command:

```bash
  swa build
```

### Configuring GitHub Actions

Having the artifacts created, we need to configure GitHub Actions to deploy `portal-deploy` on Azure Static Web Apps. You can work with [Azure Static Web Apps CLI](https://azure.github.io/static-web-apps-cli/docs/cli/swa-deploy/) or use the Azure portal.

**Azure portal**

Access the Azure portal and create a new Azure Static Web Apps following the steps below:

1. Access the Azure portal and click the `Create a resource` button.
2. In the search bar, type `Static Web Apps` and click on the first result.
3. Click the `Create` button.
4. On the "Create Static Web App" page, fill in the following information:
    - ***Subscription***: Select your Azure subscription.
    - ***Resource Group***: Click the `Create new` button and type the name `contoso-real-estate`.
    - ***Name***: Type the name `contoso-real-estate-portal-deploy`.
    - ***Plan type***: Select the `Free` option.
    - ***Region***: Select the region closest to you.
    - ***Source***: Select the `GitHub` option. You will need to log in with your GitHub account so that Azure can access your repositories.
    - ***Organization***: Select your GitHub organization.
    - ***Repository***: Select the `contoso-real-estate` repository.
    - ***Branch***: Select the `portal-deploy` branch.
    - ***Build Presets***: Select the `Angular` option.
    - ***App location***: Type the path `packages/portal-deploy`.
    - ***Api location***: Type the path `packages/api`.
    - ***Output location***: Type the path `dist/contoso-app`.
5. Click the `Review + create` button.
6. Click the `Create` button.

Access your repository on GitHub and click on the `Actions` tab. You will see that GitHub Actions has already created a workflow called `Azure Static Web Apps CI/CD`, and it will be in progress.

The steps performed on the Azure portal during the creation of Azure Static Web Apps have created a new file in the `.github/workflows` folder. This file is responsible for deploying the `portal-deploy` to Azure Static Web Apps. You can follow the progress of the deploy in GitHub Actions or in Azure Static Web Apps.

![GitHub Actions Workflow](./images/github-actions-workflow.jpg)

With the execution completed, access the link generated by Azure Static Web Apps. You will see the portal running on Azure.

![Azure Portal](./images/azure-portal-swa-portal.png)

## Congratulations
You have successfully deployed the `portal` on Azure Static Web Apps. 🎉
