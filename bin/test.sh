#!/bin/bash

#
# Running tests with Nose.
#
source venv/bin/activate
nosetests --with-coverage -v -d
coverage report -m
