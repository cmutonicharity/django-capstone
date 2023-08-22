# Django Capstone Project

Project used as an introduction to Django

## Secrets

The secret has been removed from the project. You can add your
own to `hyperion/settings.py`. This will need to be done before going
any futher.

## Development setup

Follow these steps to setup your development environment to
run the Django Capstone Project:

1. Ensure that you have python installed [Python Official Website](https://www.python.org/downloads/)
2. Create a virtualenv `python -m venv .venv`
3. Activate the virtualenv `source .venv/bin/activate`
4. Install required packages `pip install -r requirements.txt`

### Running in Dev

Once you have followed these steps you can run the project by:

1. Change into the project directory `cd ./hyperion`
2. Initialise the database `python manage.py migrate`
3. Run the development server `python manage.py runserver`

### Running on Docker

To run on Docker after initialising the database you can:

1. Build the docker image `docker build -t capstone:latest .`
2. Run it `docker run -p 8000:8000 capstone:latest`