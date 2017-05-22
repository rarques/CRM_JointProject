#!/usr/bin/env bash

# This file is generated due to the project structure. CicleCI detects automatically tests in the projetcs if they are
# in the custom paths.

# Execute the commands for the tests

python manage.py makemigrations
python manage.py migrate
python manage.py test