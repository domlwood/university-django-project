## Overview
This is a web application built using [Django](https://www.djangoproject.com/) with the intention to be used as a help desk, it utilises the django-admin as an admin panel, with a frontend for end users to create, update and read their tickets.

Admins have the added ability to delete, while also having access to every ticket and the ability to update statuses.

All users can leave comments on tickets.

## Dependencies
- [python](https://www.python.org/)
- All other dependencies are outlined in the [requirements folder](requirements.txt)

## Getting started
- setup a virtual environment: `python3 -m venv env`
- start the virtual environment: `source env/bin/activate`
- enter the helpdesk app: `cd helpdesk`
- install dependencies: `pip3 install -r requirements.txt`

- start the app: 
    - `python3 manage.py runserver`
