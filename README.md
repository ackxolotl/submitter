# Submitter

## Setup

It is recommended to create a virtual environment for this project, e.g. with [Virtualenv](https://virtualenv.pypa.io/en/stable/).

To install the dependencies run `pip3 install -r requirements.txt`.

Apply all database migrations and create the localized messages:

```
python3 manage.py migrate
python3 manage.py compilemessages
```

Add an admin user to your installation:

`python3 manage.py createsuperuser`

Start the Django server with `python3 manage.py runserver` and head to [http://localhost:8000/](http://localhost:8000/) with your favorite browser.

