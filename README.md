# Rental-app

This is a repository for a web application developed with Django, built with [Rental-App](https://github.com/arslan578/rental_app)

## Table of Contents

1. [Project Structure](#project-structure)
   - [Local Setup](#local-setup)

## Project Structure

    ..
    ├── rental_app                           # Starter home app
    ├── reservation                        # Crowdbotics Modules app
    ├── manage.py
    ├── README.md
    └── requirements.txt

# Getting Started

Following are instructions on setting up your development environment.

It's possible to also run the project without Docker.

## Local Setup
1. [Python](https://www.python.org/downloads/release/python-365/)

### Installation

1. Install [pipenv](https://pypi.org/project/pipenv/)
2. Clone this repo and `cd volunteer-app`
3. Run `pip install --user --upgrade pipenv` to get the latest pipenv version.
4. Run `pipenv --python 3.8`
5. Run `pipenv install`
6. Run `cp .env.example .env`
7. Update .env file `DATABASE_URL` with your `database_name`, `database_user`, `database_password`, if you use postgresql.
   Can alternatively set it to `sqlite:////tmp/my-tmp-sqlite.db`, if you want to use sqlite for local development.

### Getting Started

1. Run `pipenv shell`
2. Run `python manage.py makemigrations`
3. Run `python manage.py migrate`
4. Run `python manage.py runserver`
