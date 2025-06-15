#!/bin/bash

# Start Nginx
service nginx start

# Start Django
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn camsbe.wsgi:application --bind 0.0.0.0:8000