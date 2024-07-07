#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Use the Python and pip installed by Vercel
python3 -m pip install -r requirements.txt

# Run database migrations
python3 manage.py migrate

# Collect static files
python3 manage.py collectstatic --noinput
