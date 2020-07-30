# Workshop Setup

To follow along with the exercises in his workshop, you will need to install a few utilities, including Python and an IDE. Specifically, you will need the following:

- An [Azure](https://azure.microsoft.com/) account
- [Git](https://git-scm.com/)
- [Python](https://python.org)
- A code editor, such as [Visual Studio Code](https://code.visualstudio.com/) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) installed
- (Optional) [Azure Command Line Interface (CLI)](https://docs.microsoft.com/cli/azure/install-azure-cli?view=azure-cli-latest), a command line tool for managing Azure resources. You can also access the CLI without having to perform a local installation by navigating to [Azure Shell](https://shell.azure.com).

If you have these utilities installed, you can skip to [Obtaining the Starter Site](./starting-site.md).

> **NOTE** During the installation process, you will install utilities commonly used in a command or terminal window, such as Python and Git. The installation process will update system variables that aren't always detected in an open command or terminal window. If you install a tool and receive an error message telling you it's not available, try closing the window and opening a new one.

## Azure account

We will be using [Azure](https://azure.microsoft.com/) for the artificial intelligence (AI) services. To follow the code during the workshop, you'll need an account on Azure. If you don't have one, you can register in a couple of ways.

> **NOTE:** During the exercises, you will create a key to use with Azure Cognitive Services, specifically an All-in-One key. This key is only available at the standard tier, meaning there will be some cost incurred. For information on pricing, consult the [pricing documentation](https://azure.microsoft.com/pricing/details/cognitive-services/). As of today, the cost is typically $1 US for 1,000 transactions. We will be executing about 40 transactions. Your instructor can also provide a key for you to use during this course should you desire.

### Active student

If you're an [active student](https://azure.microsoft.com/free/free-account-students-faq/), you can enroll for [Azure for Students](https://aka.ms/a4s) for **free**. Azure for Students offers $100 in credit over 12 months, and includes many free services for testing and learning. You can visit [Azure for Students](https://aka.ms/a4s) to enroll!

### Lifelong learner

If you're already in the industry and are expanding your skills into Azure, you can create a **free** trial account on Azure. When creating a new account, you will receive $200 in credit for the first 30 days. Several free services are also included with this account for testing and learning. **No commitment** is required. You can [enroll on the Azure website](https://azure.microsoft.com/free/).

## Install quickstart guides

If you are using Windows, macOS, or Ubuntu, you can follow the quick install guides below to complete the local installation required to complete the labs that are part of this course. If you want more information about the software, you can peruse the [Python](#python), [Code Editor](#code-editor-visual-studio-code), and [Git](#git) sections. The steps listed here will install Git, Python, and Visual Studio Code.

### Windows

To streamline the installation of the required components, this quickstart guide uses [Chocolatey](https://chocolatey.org/), a package management tool for Windows, and will install Git, Visual Studio Code, and Python 3.

1. [Install Chocolatey](https://chocolatey.org/install)
2. Execute the following command in a new command window:

``` shell
choco install python3 git vscode
```

### MacOS

To streamline the installation of the required components, this quickstart guide uses [Homebrew](https://brew.sh/), a package management tool for macOS, and will install Git, Visual Studio Code, and Python 3.

1. [Install Homebrew](https://brew.sh/)
2. Execute the following command in a new terminal window:

``` shell
brew install git visual-studio-code python3
```

### Debian and Ubuntu

This quickstart guide uses the [apt](https://help.ubuntu.com/community/AptGet/Howto) and [snap](https://snapcraft.io/) package managers, and will install Git, Visual Studio Code, and Python 3.

1. In a terminal window, execute the following command to install Python 3 and Git:

``` shell
# Package update
sudo apt-get update
sudo apt-get upgrade -y

sudo apt-get install python3 python3-pip git -y
```

2. In a terminal window, execute the following command to install Visual Studio Code:

``` shell
sudo snap install --classic code
```

> **Note**: If snap isn't available in your Linux distribution, please check the following [installing snapd guide](https://snapcraft.io/docs/installing-snapd) to help you get set up.

## Python

This workshop presents a scenario where you will build a website using [Flask](https://palletsprojects.com/p/flask/), which is a lightweight [Python](https://python.org) framework.

### Installing Python

If Python 3.6 or higher isn't installed on your computer, you can install it by visiting [Python.org](https://python.org) and following the installation steps. If you're not sure if it's installed, you can test it by running the following command. If Python is installed, the version number will appear in the console window:

``` bash
# Windows
python --version

# macOS or Linux
python3 --version
```

> **NOTE** If installing on Windows, ensure you select the option to add Python to your PATH system variable.

![Dialog box for installing Python showing PATH option selected](./images/vision_python.png)

### Upgrading pip

[Pip](https://pypi.org/) is the package manager for Python. You should always ensure you have the latest version of `pip`. To perform the upgrade, open a command or terminal window and issue the following command:

``` bash
# Windows
python -m pip install --upgrade pip

# macOS or Linux
python3 -m pip install --upgrade pip
```

## Code editor (Visual Studio Code)

To work with the code, you will need a code editor. You are free to use any editor you like. Your instructor will use Visual Studio Code, an open source (OSS) editor from Microsoft.

### Installing Visual Studio Code

The [Visual Studio Code website](https://code.visualstudio.com/) will allow you to download and install Visual Studio Code.

### Adding Python extension

To enhance your Python development experience, you should install the [Visual Studio Code Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) by clicking the link and following the instructions on the page.

## Azure Command Line Interface (CLI) (optional)

To make it easier to create resources on Azure, this workshop uses the Azure CLI. By using the Azure CLI, you can manage all Azure resources. You can either install the Azure CLI locally or use [Azure Cloud Shell](https://shell.auzre.com), which requires no local installation.

### Installing the Azure CLI

To install the Azure CLI, navigate to the [Azure CLI installation page](https://docs.microsoft.com/cli/azure/install-azure-cli?view=azure-cli-latest) and follow the instructions. Because the Azure CLI is based on Python, it will run on all operating systems.

Once installed, log in to the Azure CLI by using `az login`. This operation will open a browser for authentication.

## Git

To download the starter and solution files, you will [clone](https://help.github.com/en/articles/cloning-a-repository) a repository from [GitHub](https://github.com) using Git. Git is a distributed source code management system.

### Installation

To install Git, navigate to [Git downloads](https://git-scm.com/downloads) and follow the instructions.

## Obtaining the starter site

Congratulations! All prerequisites are now installed. Let's take a look at [Obtaining the Starter Site](./starting-site.md).
