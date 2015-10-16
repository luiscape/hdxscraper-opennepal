#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import csv
import json

from os import path as p

#
# Reference default locations.
#
DATA_DIR = p.dirname(p.dirname(p.dirname(__file__)))
DEV_CONFIG_PATH = p.join(DATA_DIR, 'config', 'dev.json')
PROD_CONFIG_PATH = p.join(DATA_DIR, 'config', 'prod.json')

def LoadConfig(config_path=DEV_CONFIG_PATH, verbose=True):
  '''Load configuration parameters.'''

  try:
    with open(config_path) as json_file:
      config = json.load(json_file)

  except Exception as e:
    if verbose:
      print e
    return False

  return config
