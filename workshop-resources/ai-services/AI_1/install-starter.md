# Install the Starter Site

## Create a directory

We'll start by opening a command or terminal window, and then creating a directory for use during this workshop:

``` bash
# Windows
md contoso
cd contoso

# macOS or Linux
mkdir contoso
cd contoso
```

## Download the starter site

1. If Git isn’t installed on your computer, go to the [Git website](https://git-scm.com/) and install it now. Versions are available for Windows, macOS, and Linux.
2. In a command window or terminal, use `cd` to switch to the project directory you created in the previous subsection. Then use the following command to clone the GitHub repo containing the starter files for the website.

# Using Git

To download the starter and solution files, you will [clone](https://help.github.com/en/articles/cloning-a-repository) a repository from [GitHub](https://github.com) using Git. Git is a distributed source code management system.

### Installation

To install Git, navigate to [Git downloads](https://git-scm.com/downloads) and follow the instructions.

## Starter code

The sample code is provided as part of the [Reactors](https://github.com/microsoft/reactors) repository on [GitHub](https://github.com). Let's clone the repository and get the environment set up for the code.

### Clone the repository

1. Open a command or terminal window.
2. Navigate to the folder where you want to put the code.
3. Clone the repository.

``` git
git clone https://github.com/microsoft/reactors
```

4. Navigate to the AI directory.

``` console
# Windows
cd reactors\Artifical Intelligence 1_Building Software That Recognizes You\starter-site

# Linux or macOS
cd ./reactors/Artifical Intelligence 1_Building Software That Recognizes You/starter-site
```

5. Create a virtual environment and install packages.
Let's create a virtual environment for the packages we'll be using. Virtual environments allow us to separate packages from other environments. Return to the command line and issue the following command:

``` console
# Windows
python -m venv env
.\env\Scripts\activate

# macOS or Linux
python3 -m venv env
. ./env/bin/activate
```

> **Note**: If you're using macOS or Linux, the leading `.` in `. ./env/bin/` is required as it tells Python where your source code resides.

6. Install the necessary Python packages.
Install the packages listed in requirements.txt by using pip.

``` console
pip install -r requirements.txt
```
7. Confirm the site starts.

``` console
flask run
```

8. Navigate to **http://localhost:5000**.

If you're following along, the next step is to [start the site](./starting-site.md).
