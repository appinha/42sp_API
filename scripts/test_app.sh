#!/bin/bash
## Script to test the application

# Check requirements
source scripts/requirements.sh

# Run tests
py.test $1
