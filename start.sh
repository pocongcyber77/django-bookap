#!/bin/bash

# Set PYTHONPATH to include the project directory
export PYTHONPATH=$PYTHONPATH:/app

# Collect static files
python manage.py collectstatic --noinput

# Run Gunicorn
gunicorn library_project.wsgi:application