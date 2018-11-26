Feature Requests
===============================

[![Build Status](https://travis-ci.org/yudori/feature-requests.svg?branch=master)](https://travis-ci.org/yudori/feature-requests)


A web application that allows users to create feature requests

Dependencies
------------

This project makes use of the tech stack and more:

 * Python 3.6 - Programming language
 * Flask - Web framework
 * Docker - Container platform
 * Pipenv - Python packaging
 * AWS - Deployment & Cloud services


Quickstart
----------

Run the following commands to bootstrap your environment :

    git clone https://github.com/yudori/feature_requests
    cd feature_requests
    pipenv install --dev
    cp .env.example .env
    npm install

For the sake of simplicity, the project has been configured with sqlite database. However, you can configure any database of your choice and run:

    flask db init
    flask db upgrade

To start up the application, run:

    npm start


Deployment
----------

To deploy:

    export FLASK_ENV=production
    export FLASK_DEBUG=0
    export DATABASE_URL="<YOUR DATABASE URL>"
    npm run build   # build assets with webpack
    flask run       # start the flask server

In your production environment, make sure the ``FLASK_DEBUG`` environment
variable is unset or is set to ``0``.


Running Tests
-------------

To run all tests, run :

    pytest

