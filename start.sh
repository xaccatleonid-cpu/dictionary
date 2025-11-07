#!/bin/bash
python manage.py migrate --noinput
gunicorn dictionary.wsgi