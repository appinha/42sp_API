#!/bin/bash
## Script for running inside .venv

# Check requirements
source scripts/requirements.sh

# Run Flask application
#PYTHONPATH=./ FLASK_ENV=development python3 ./app/app.py
PYTHONPATH=./ FLASK_APP=app FLASK_ENV=development flask run
