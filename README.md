Feature Requests
===============================

[![Build Status](https://travis-ci.org/yudori/feature-requests.svg?branch=master)](https://travis-ci.org/yudori/feature-requests)


A web application that allows users to create feature requests running at http://feature-requests-dev.us-east-2.elasticbeanstalk.com/

Dependencies
------------

This project makes use of the tech stack and more:

 * Python 3.6 - Programming language
 * Flask - Web framework
 * Docker - Container platform
 * Pipenv - Python packaging
 * AWS - Deployment & Cloud services


Overview
--------

This is a python (flask) web application that allows for entering in feature requests. Pushed code changes are validated by continuous integration using travis ci. Frontend and backend linting and tests are carried out to ensure conformity with adopted standards.

Automated builds are carried out on the resulting main docker image via the docker cloud [repository](https://cloud.docker.com/repository/docker/yudori/feature-requests/builds) upon each push. A single command `eb deploy` is then needed to deploy the latest build to a Multicontainer Elastic Beanstalk infrastructure on AWS.


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

Initialize elasticbeanstalk

    eb init
    eb create

Ensure that the appropriate production environment variables (see .env) are set on the aws console.

To deploy:

    eb deploy

In your production environment, make sure the ``FLASK_DEBUG`` environment
variable is unset or is set to ``0``.


Running Tests
-------------

To run all tests, run :

    pytest
