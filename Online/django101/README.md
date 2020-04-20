# Django demos

Demo files being used during a broadcast on [MicrosoftDeveloper Twitch](https://twitch.tv/MicrosoftDeveloper).

## Installation steps

1. Install [Python](https://python.org) (if needed)
2. [Clone the Reactors repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
3. Change directory into `online/django101`
4. Create a virtual environment and install requirements

``` bash
# Windows
python -m venv venv
.\venv\scripts\activate
pip install -r requirements.txt

# Linux / macOS
python3 -m venv venv
. ./venv/bin/activate
pip3 install -r requirements.txt
```

5. Run the site

``` bash
# Windows
python manage.py runserver

# Linux / macOS
python3 manage.py runserver
```