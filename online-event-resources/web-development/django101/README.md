# Django Demos

Demo files being used during a broadcast on [MicrosoftDeveloper Twitch](https://twitch.tv/MicrosoftDeveloper). You can find the on demand version of this presentation on [YouTube](https://www.youtube.com/watch?v=yVyzA9GseI4&t=7s).

## Installation steps:

1. If needed, install [Python](https://python.org).
2. [Clone the Reactors repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).
3. Change directory to `online/django101`.
4. Create a virtual environment and install requirements.

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

5. Run the site.

``` bash
# Windows
python manage.py runserver

# Linux / macOS
python3 manage.py runserver
```
