#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import json
import requests
from copy import copy
from datetime import datetime

def ExportDatasets(data):
  '''Function to export datasets in a JSON format.'''

  #
  # Default dataset.
  #
  default_dataset = {
    'name': None,
    'title': None,
    'owner_org': 'opennepal',  # default for OpenNepal
    'author': '',
    'author_email': '',  # default for OpenNepal
    'maintainer': '',  # default for OpenNepal
    'maintainer_email': '',  # default for OpenNepal
    'license_id': 'hdx-other',  # default for OpenNepal
    'license_other': None,
    'dataset_date': None,  # has to be in MM/DD/YYYY format.
    'subnational': 0,  # has to be 0 or 1. Default 1 for OpenNepal.
    'notes': None,
    'caveats': None,
    'methodology': 'Other',  # default for OpenNepal
    'methodology_other': None,
    'dataset_source': '',
    'package_creator': '',
    'private': False,  # has to be True or False
    'url': None,
    'state': 'active',  # always "active"
    'tags': [],  # has to be a list with {'name': None}
    'groups': []  # has to be ISO-3-letter-code. {'id': None}
    }

  for record in data:

    t = default_dataset

    #
    # Adding fields from records.
    #
    t['title'] = record['title']
    t['name'] = record['id']
    # t['dataset_date'] = record['created']
    t['notes'] = record['description']

    #
    # Adding tags and country.
    #
    t['tags'] = [{ 'name': record['tags'] }, { 'name': 'geodata' }]
    t['groups'] = [{ 'id': 'npl' }]


    #
    # Appending results.
    #
    data.append(copy(t))

  #
  # Write JSON to disk.
  #
  with open(os.path.join(directory, 'datasets.json'), 'w') as outfile:
    json.dump(data, outfile)



def ExportResources(directory=None):
  '''Export the UNOSAT resources for their respective datasets.'''

  print '%s Exporting Resources JSON to disk.' % item('prompt_bullet')


  #
  # Default resource.
  #
  default_resource = {
    "package_id": None,
    "url": None,
    "name": None,
    "format": None,
    "description": None  # file size could go here.
  }

  data = []
  for record in records:

    t = default_resource

    #
    # Adding fields from records.
    #
    t['package_id'] = record['hdx_dataset_id']
    t['url'] = record['link_href']
    t['name'] = record['file_name']
    t['format'] = record['file_extension']

    #
    # Appending results.
    #
    data.append(copy(t))

  #
  # Write JSON to disk.
  #
  with open(os.path.join(directory, 'resources.json'), 'w') as outfile:
    json.dump(data, outfile)