#!/bin/bash
## Script for running inside .venv

# Check requirements
source scripts/requirements.sh

# Run Flask application
PYTHONPATH=./ FLASK_ENV=development python3 ./api/app.py
