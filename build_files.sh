#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Collect static files (if you're using Django, for example)
python manage.py collectstatic --noinput
