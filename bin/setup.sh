#!/bin/bash

#
# Setting up virtual environment
# and dependencies.
#
virtualenv venv
source venv/bin/activate
pip install pip --upgrade
pip install -r requirements.txt
