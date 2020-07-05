### Setup:

Pre-installation: Make sure you have a Python 3 environment with virtualenv installed.

1. Create a virtualenv: `python -m virtualenv my_venv_name`
2. `cd my_venv_name`
3. Activate it: `source bin/activate` (POSIX), `.\Scripts\activate` (Windows)
4. `mkdir src`
5. `cd src` and and clone this repo into it (`git clone git@github.com:knazran/ilmia-hack.git .`)
6. `pip install -r requirements.txt` (may require `sudo` opn POSIX systems)

### Start the server

1. `python manage.py runserver`
2. Navigate to http://127.0.0.1:8000



