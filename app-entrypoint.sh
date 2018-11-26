#!/bin/bash

flask db init
flask db upgrade

gunicorn feature_requests.app:create_app\(\) -b 0.0.0.0:5000 -w 3 --timeout 90 --log-level debug
